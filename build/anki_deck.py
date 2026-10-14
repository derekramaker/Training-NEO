"""Build the Anki deck: seven core units in teaching order (with diagram cards) plus a suspended Reference unit.

Sources:
    data/anki/core/units.yaml        unit titles, descriptions and group lists
    data/anki/core/unit-NN.csv       core cards (columns in CORE_COLS)
    data/anki/diagrams/*.svg         diagrams, rendered by build/render_diagrams.cjs
    data/anki/0N-*.csv               the original decks; whatever the core set does not reuse becomes Reference

Card IDs (U01-G2-03) drive the note GUIDs, so rewording a card keeps the hires' review history.
"""

import csv
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import genanki
import yaml

CORE_COLS = ["id", "group", "priority", "track", "type", "front", "back", "front_image", "back_image",
             "extra", "source", "tags", "reuses"]
REF_COLS = ["front", "back", "tags", "source"]
TYPES = {"basic", "diagram", "cloze", "worked"}
TRACKS = {"both": "", "research": "Research track", "stdcost": "Standard Cost track"}
ID_RE = re.compile(r"^U0([1-7])-G([1-9])-(\d{2})$")
IMG_RE = re.compile(r"^([a-z0-9][a-z0-9-]*)(?:\?(hide|show)=([A-Za-z0-9_-]+))?$")
MAX_BACK_WORDS = 45
MAX_EXTRA_WORDS = 70

ROOT_DECK = "BSA Onboarding"
REF_DECKS = {"01": "Customs, classification and USMCA", "02": "Programs, exports and cost", "03": "BSA craft and data"}
MODEL_CARD_ID = 1730826421
MODEL_FILLIN_ID = 1730826422

CSS = """
.card { font-family: "Segoe UI", Calibri, Arial, sans-serif; font-size: 20px; line-height: 1.45; color: #262626;
        background: #FFFFFF; text-align: left; max-width: 680px; margin: 0 auto; padding: 4px 10px; }
.meta { font-size: 13px; color: #7F7F7F; margin-bottom: 10px; }
.meta .track { display: inline-block; margin-left: 8px; padding: 1px 8px; border-radius: 9px; background: #FBE5D6;
               color: #C55A11; font-weight: 600; }
.front { font-weight: 700; color: #1F3864; }
.img { margin: 14px 0 6px; }
.img img { max-width: 100%; height: auto; border-radius: 10px; border: 1px solid #D9DEE7; }
.extra { margin-top: 12px; font-size: 17px; color: #404040; background: #F7F9FC; border-left: 4px solid #2E75B6;
         padding: 8px 12px; border-radius: 4px; }
.src { margin-top: 14px; font-size: 13px; color: #7F7F7F; word-break: break-word; }
hr#answer { border: none; border-top: 1px solid #D9DEE7; margin: 16px 0; }
.nightMode .card, .night_mode .card { background: #1E1E1E; color: #E6E6E6; }
.nightMode .front, .night_mode .front { color: #9DC3E6; }
.nightMode .extra, .night_mode .extra { background: #2A2F36; color: #D0D0D0; }
.nightMode .img img, .night_mode .img img { border-color: #3A3F46; }
"""
META = '<div class="meta">{{Subdeck}}{{#Track}}<span class="track">{{Track}}</span>{{/Track}}</div>'
FRONT = '<div class="front">{{Front}}</div>'
TAIL = ('{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
        '{{#Source}}<div class="src">Source: {{Source}}</div>{{/Source}}')
FIELDS = ["ID", "Front", "FrontImage", "Back", "BackImage", "Extra", "Source", "Track", "Priority"]

CARD_MODEL = genanki.Model(
    MODEL_CARD_ID, "BSA Onboarding Card",
    fields=[{"name": f} for f in FIELDS],
    templates=[{
        "name": "Card",
        "qfmt": META + FRONT + '{{#FrontImage}}<div class="img">{{FrontImage}}</div>{{/FrontImage}}',
        "afmt": META + FRONT + '{{#FrontImage}}<div class="img">{{FrontImage}}</div>{{/FrontImage}}'
                '<hr id="answer"><div class="back">{{Back}}</div>'
                '{{#BackImage}}<div class="img">{{BackImage}}</div>{{/BackImage}}' + TAIL,
    }],
    css=CSS, sort_field_index=0,
)
# Fill-in-the-diagram: the back swaps the masked diagram for the revealed one instead of showing both.
FILLIN_MODEL = genanki.Model(
    MODEL_FILLIN_ID, "BSA Onboarding Diagram Fill-in",
    fields=[{"name": f} for f in FIELDS],
    templates=[{
        "name": "Fill-in",
        "qfmt": META + FRONT + '<div class="img">{{FrontImage}}</div>',
        "afmt": META + FRONT + '<div class="img">{{BackImage}}</div>'
                '<hr id="answer"><div class="back">{{Back}}</div>' + TAIL,
    }],
    css=CSS, sort_field_index=0,
)


class DeckError(Exception):
    pass


def deck_id(name):
    """Stable Anki deck ID derived from the deck name."""
    return int(hashlib.sha1(name.encode("utf-8")).hexdigest()[:12], 16) % (1 << 40) + (1 << 41)


def fmt(text):
    """Plain text from the CSV to card HTML: escaped, **bold**, newlines as <br>."""
    out = html.escape(text.strip())
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    return out.replace("\n", "<br>")


def fmt_source(src):
    src = src.strip()
    if src.lower() in ("", "general"):
        return ""
    if src.startswith("http"):
        return f'<a href="{html.escape(src)}">{html.escape(src)}</a>'
    return html.escape(src)


def read_rows(path, cols):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != cols:
            raise DeckError(f"{path.name}: columns are {reader.fieldnames}, expected {cols}")
        return [{k: (v or "").strip() for k, v in row.items()} for row in reader]


def parse_image(ref, where, diagrams_dir):
    m = IMG_RE.match(ref)
    if not m:
        raise DeckError(f"{where}: bad image reference {ref!r} (use name, name?hide=KEY or name?show=KEY)")
    name, mode, key = m.group(1), m.group(2) or "full", m.group(3) or ""
    svg = diagrams_dir / f"{name}.svg"
    if not svg.exists():
        raise DeckError(f"{where}: no diagram {svg.name}")
    media = f"bsa-{name}.png" if mode == "full" else f"bsa-{name}-{mode}-{key}.png"
    return {"svg": svg, "mode": mode, "key": key, "media": media}


def validate_core(units, core_dir, diagrams_dir, ref_fronts):
    """Read every unit CSV and check it against the rules. Returns (rows, image jobs)."""
    rows, ids, fronts, images, problems = [], set(), set(), {}, []
    for unit in units:
        n = unit["number"]
        path = core_dir / f"unit-{n:02d}.csv"
        if not path.exists():
            problems.append(f"missing {path.name}")
            continue
        group_keys = [g["key"] for g in unit["groups"]]
        for i, row in enumerate(read_rows(path, CORE_COLS), start=2):
            where = f"{path.name} line {i} ({row['id'] or 'no id'})"
            m = ID_RE.match(row["id"])
            if not m or int(m.group(1)) != n:
                problems.append(f"{where}: id must look like U{n:02d}-G1-01")
            if row["id"] in ids:
                problems.append(f"{where}: duplicate id")
            ids.add(row["id"])
            if row["group"] not in group_keys:
                problems.append(f"{where}: group {row['group']!r} is not one of {group_keys}")
            elif m and f"G{m.group(2)}" != row["group"]:
                problems.append(f"{where}: id group G{m.group(2)} does not match group column {row['group']}")
            if row["priority"] not in ("1", "2"):
                problems.append(f"{where}: priority must be 1 or 2")
            if row["track"] not in TRACKS:
                problems.append(f"{where}: track must be one of {sorted(TRACKS)}")
            if row["type"] not in TYPES:
                problems.append(f"{where}: type must be one of {sorted(TYPES)}")
            if not row["front"] or not row["back"]:
                problems.append(f"{where}: front and back are required")
            if len(row["back"].split()) > MAX_BACK_WORDS:
                problems.append(f"{where}: back has {len(row['back'].split())} words; max {MAX_BACK_WORDS} (move detail to extra)")
            if len(row["extra"].split()) > MAX_EXTRA_WORDS:
                problems.append(f"{where}: extra has {len(row['extra'].split())} words; max {MAX_EXTRA_WORDS}")
            if row["front"] in fronts:
                problems.append(f"{where}: duplicate front {row['front'][:60]!r}")
            fronts.add(row["front"])
            if row["reuses"] and row["reuses"] not in ref_fronts:
                problems.append(f"{where}: 'reuses' does not match any original card front exactly")
            fi = bi = None
            try:
                fi = parse_image(row["front_image"], where, diagrams_dir) if row["front_image"] else None
                bi = parse_image(row["back_image"], where, diagrams_dir) if row["back_image"] else None
            except DeckError as e:
                problems.append(str(e))
            t = row["type"]
            if t == "basic" and (row["front_image"] or row["back_image"]):
                problems.append(f"{where}: basic cards have no images (use type diagram or worked)")
            if t == "diagram" and not row["back_image"]:
                problems.append(f"{where}: diagram cards need a back_image")
            if t == "worked" and not (row["front_image"] or row["back_image"]):
                problems.append(f"{where}: worked cards need a front_image or back_image")
            if t == "cloze":
                if not (fi and bi and fi["mode"] == "hide" and bi["mode"] == "show"
                        and fi["svg"] == bi["svg"] and fi["key"] == bi["key"]):
                    problems.append(f"{where}: cloze cards need front_image NAME?hide=KEY and back_image NAME?show=KEY")
            for img in (fi, bi):
                if img:
                    images[img["media"]] = img
            row["_unit"], row["_front_img"], row["_back_img"] = unit, fi, bi
            rows.append(row)
    if problems:
        raise DeckError("core deck problems:\n  - " + "\n  - ".join(problems))
    return rows, images


def render_images(images, root, cache_dir):
    """Render every needed diagram variant, reusing cached PNGs whose inputs have not changed."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    css = (root / "data/anki/diagrams/_style.css").read_bytes()
    renderer = (root / "build/render_diagrams.cjs").read_bytes()
    todo = []
    for media, img in images.items():
        digest = hashlib.sha256(css + renderer + img["svg"].read_bytes() + f"{img['mode']}|{img['key']}".encode()).hexdigest()
        out, stamp = cache_dir / media, cache_dir / f"{media}.sha256"
        img["path"] = out
        if out.exists() and stamp.exists() and stamp.read_text() == digest:
            continue
        todo.append((img, digest))
    if todo:
        node = shutil.which("node")
        if not node:
            raise DeckError("node is needed to render diagrams")
        with tempfile.TemporaryDirectory() as tmp:
            jobs = [{"svg": str(img["svg"]), "mode": img["mode"], "key": img["key"],
                     "out": str(Path(tmp) / img["media"])} for img, _ in todo]
            jobs_file = Path(tmp) / "jobs.json"
            jobs_file.write_text(json.dumps(jobs))
            res = subprocess.run([node, str(root / "build/render_diagrams.cjs"), "--jobs", str(jobs_file)],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                raise DeckError(f"diagram renderer failed:\n{res.stderr[-3000:]}")
            report = json.loads(res.stdout)
            bad = [f"{Path(r['svg']).name} ({r['mode']} {r['key']}): {i}" for r in report for i in r["issues"]]
            if bad:
                raise DeckError("diagram problems:\n  - " + "\n  - ".join(sorted(set(bad))))
            for img, digest in todo:
                raw = Path(tmp) / img["media"]
                # Flat diagrams compress well to an 8-bit palette (about 40% of the size).
                subprocess.run(["convert", str(raw), "-strip", "-colors", "128", f"PNG8:{img['path']}"], check=True)
                (cache_dir / f"{img['media']}.sha256").write_text(digest)
    return len(todo)


def img_tag(img):
    return f'<img src="{img["media"]}">' if img else ""


def build_deck(root, dist, preview=False, only_units=None):
    data = root / "data/anki"
    units = yaml.safe_load((data / "core/units.yaml").read_text(encoding="utf-8"))["units"]
    if only_units:
        units = [u for u in units if u["number"] in only_units]

    ref_rows = []
    for path in sorted(data.glob("0*.csv")):
        for row in read_rows(path, REF_COLS):
            ref_rows.append({**row, "_file": path.name[:2]})
    ref_fronts = {r["front"] for r in ref_rows}

    core_rows, images = validate_core(units, data / "core", data / "diagrams", ref_fronts)
    rendered = render_images(images, root, root / "build/.cache/anki-media")

    decks = {}
    root_desc = ("<b>How to study (one-time setup, then 15 minutes a day):</b> in this top deck's Options, set New "
                 "cards/day to 10 on the preset and to 0 on the \"This deck\" tab. Each day, click the unit for the "
                 "current week to learn its new cards, then click this top deck to clear the remaining reviews. "
                 "Reference holds the rest of the original cards, suspended: browse it, or unsuspend cards you want. "
                 "Full steps: Anki card-writing guide.")
    decks[ROOT_DECK] = genanki.Deck(deck_id(ROOT_DECK), ROOT_DECK, description=root_desc)

    def deck(name, desc=""):
        if name not in decks:
            decks[name] = genanki.Deck(deck_id(name), name, description=desc)
        return decks[name]

    exported, reused = [], {r["reuses"] for r in core_rows if r["reuses"]}
    for unit in units:
        unit_name = f"{ROOT_DECK}::Unit {unit['number']:02d} · {unit['title']}"
        deck(unit_name, html.escape(unit["description"]))
    group_index = {(u["number"], g["key"]): (i, g["name"]) for u in units for i, g in enumerate(u["groups"], 1)}
    for seq, row in enumerate(core_rows):
        unit = row["_unit"]
        gi, gname = group_index[(unit["number"], row["group"])]
        name = f"{ROOT_DECK}::Unit {unit['number']:02d} · {unit['title']}::{gi} {gname}"
        model = FILLIN_MODEL if row["type"] == "cloze" else CARD_MODEL
        tags = (["core", f"unit::{unit['number']:02d}", f"priority::{row['priority']}", f"track::{row['track']}",
                 f"type::{row['type']}"] + row["tags"].split())
        note = genanki.Note(
            model=model,
            fields=[row["id"], fmt(row["front"]), img_tag(row["_front_img"]), fmt(row["back"]),
                    img_tag(row["_back_img"]), fmt(row["extra"]), fmt_source(row["source"]),
                    TRACKS[row["track"]], row["priority"]],
            tags=tags, guid=genanki.guid_for("bsa-core", row["id"]),
            due=unit["number"] * 10000 + gi * 1000 + seq,
        )
        deck(name).add_note(note)
        exported.append({"deck": name, "id": row["id"], "type": row["type"], "priority": row["priority"],
                         "track": row["track"], "front": row["front"], "back": row["back"],
                         "front_image": row["front_image"], "back_image": row["back_image"], "extra": row["extra"],
                         "source": row["source"], "tags": " ".join(tags), "suspended": "no"})

    ref_count = 0
    for i, row in enumerate(ref_rows):
        if row["front"] in reused:
            continue
        name = f"{ROOT_DECK}::Reference (browse only)::{REF_DECKS[row['_file']]}"
        ref_id = f"REF-{row['_file']}-{i:03d}"
        tags = ["reference"] + row["tags"].split()
        note = genanki.Note(model=CARD_MODEL,
                            fields=[ref_id, fmt(row["front"]), "", fmt(row["back"]), "", "", fmt_source(row["source"]), "", ""],
                            tags=tags, guid=genanki.guid_for("bsa-ref", row["front"]), due=900000 + i)
        for card in note.cards:
            card.suspend = True
        deck(name, "Suspended by default. Browse, or unsuspend the cards you want in your queue.").add_note(note)
        ref_count += 1
        exported.append({"deck": name, "id": ref_id, "type": "basic", "priority": "", "track": "",
                         "front": row["front"], "back": row["back"], "front_image": "", "back_image": "",
                         "extra": "", "source": row["source"], "tags": " ".join(tags), "suspended": "yes"})

    dist.mkdir(parents=True, exist_ok=True)
    out = dist / "BSA-Onboarding.apkg"
    media = [str(img["path"]) for img in images.values()]
    genanki.Package(list(decks.values()), media_files=media).write_to_file(str(out))
    (dist / "anki").mkdir(parents=True, exist_ok=True)
    with open(dist / "anki" / "BSA-Onboarding-cards.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(exported[0].keys()))
        w.writeheader()
        w.writerows(exported)
    if preview:
        write_previews(root, units, core_rows)
    size_mb = out.stat().st_size / 1e6
    return (f"anki: {len(core_rows)} core cards in {len(units)} units, {ref_count} reference cards (suspended), "
            f"{len(images)} images ({rendered} re-rendered), {size_mb:.1f} MB -> {out.relative_to(root)}")


def write_previews(root, units, core_rows):
    """Contact sheets (one PNG per unit) showing each card's front and back at phone width."""
    out_dir = root / "build/.cache/card-preview"
    out_dir.mkdir(parents=True, exist_ok=True)
    page_css = CSS + """
      body { background: #E9EDF3; margin: 0; padding: 18px; font-family: "Segoe UI", Arial, sans-serif; }
      h1 { font-size: 22px; color: #1F3864; margin: 0 0 14px; }
      .row { display: flex; gap: 14px; margin-bottom: 18px; align-items: flex-start; }
      .side { width: 380px; background: #fff; border-radius: 14px; box-shadow: 0 1px 4px rgba(0,0,0,.15); padding: 14px 4px; }
      .lbl { font-size: 12px; color: #888; margin: 0 10px 6px; }
    """
    for unit in units:
        rows = [r for r in core_rows if r["_unit"] is unit]
        cells = []
        for r in rows:
            meta = (f'<div class="meta">{html.escape(r["group"])} · {r["id"]} · P{r["priority"]}'
                    + (f'<span class="track">{TRACKS[r["track"]]}</span>' if TRACKS[r["track"]] else "") + "</div>")
            fimg = (f'<div class="img"><img src="{r["_front_img"]["path"].as_uri()}"></div>' if r["_front_img"] else "")
            bimg = (f'<div class="img"><img src="{r["_back_img"]["path"].as_uri()}"></div>' if r["_back_img"] else "")
            front = f'{meta}<div class="front">{fmt(r["front"])}</div>{fimg}'
            if r["type"] == "cloze":
                back = f'{meta}<div class="front">{fmt(r["front"])}</div>{bimg}<hr id="answer"><div>{fmt(r["back"])}</div>'
            else:
                back = f'{front}<hr id="answer"><div>{fmt(r["back"])}</div>{bimg}'
            if r["extra"]:
                back += f'<div class="extra">{fmt(r["extra"])}</div>'
            cells.append(f'<div class="row"><div class="side"><div class="lbl">FRONT</div><div class="card">{front}</div></div>'
                         f'<div class="side"><div class="lbl">BACK</div><div class="card">{back}</div></div></div>')
        page = (f'<!doctype html><html><head><meta charset="utf-8"><style>{page_css}</style></head><body>'
                f'<h1>Unit {unit["number"]:02d} · {html.escape(unit["title"])} — {len(rows)} cards</h1>{"".join(cells)}</body></html>')
        html_path = out_dir / f"unit-{unit['number']:02d}.html"
        html_path.write_text(page, encoding="utf-8")
        subprocess.run([shutil.which("node"), str(root / "build/render_diagrams.cjs"), "--screenshot", str(html_path),
                        str(out_dir / f"unit-{unit['number']:02d}.png")], check=True)
