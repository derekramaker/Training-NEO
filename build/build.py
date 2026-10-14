#!/usr/bin/env python3
"""Build the OneNote-ready deliverables in dist/ from the Markdown and CSV sources.

Run from the repo root:

    python3 build/build.py                  # add --preview-cards for flashcard contact sheets

Needs: pandoc, python-docx, openpyxl, genanki, pyyaml, pandas (for the practice data), node with Playwright and
ImageMagick (for the flashcard diagrams).
Outputs:
    dist/docs/**.docx                    one Word file per Markdown page (paste into OneNote)
    dist/trainer-only/answer-key.docx    analytics answer key: Manager and Senior only
    dist/BSA-Onboarding-Handbook.docx    the core program docs in one printable file
    dist/BSA-Onboarding-Trackers.xlsx    skills tracker, knowledge tracker, tool inventory, glossary
    dist/BSA-Onboarding.apkg             Anki deck: 7 core units with diagrams + suspended Reference (File > Import)
    dist/anki/BSA-Onboarding-cards.csv   the same cards as one CSV
    dist/Tariff-Impact-Model-Template.xlsx, dist/Practice-Data.xlsx, dist/practice-data/*.csv
"""

import csv
import datetime as dt
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import anki_deck
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"
DIST = ROOT / "dist"
BUILD = ROOT / "build"

PROGRAM_START = dt.date(2026, 10, 19)
MILESTONES = [("Day 30", dt.date(2026, 11, 18)), ("Day 60", dt.date(2026, 12, 18)), ("Day 90", dt.date(2027, 1, 15))]
HIRES = [("Hire A", "Research", "M5R"), ("Hire B", "Standard Cost", "M5C")]

# Core program docs, in reading order, for the combined handbook.
HANDBOOK_ORDER = [
    "00-program-at-a-glance.md",
    "01-30-60-90-plan.md",
    "02-weeks-1-2-schedule.md",
    "03-check-ins-and-scorecards.md",
    "04-access-request-checklist.md",
    "05-time-management.md",
]

# Pages the hires must not see before the day-30 review; built to dist/trainer-only/.
TRAINER_ONLY = {"analytics/answer-key.md"}

NAVY = "1F3864"
FONT = "Calibri"


def fail(msg):
    sys.exit(f"build failed: {msg}")


def read_csv(path, expected_cols):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != expected_cols:
            fail(f"{path.relative_to(ROOT)} columns are {reader.fieldnames}, expected {expected_cols}")
        return list(reader)


# ---------------------------------------------------------------- Word ----

def make_reference_docx(path):
    """Pandoc's default reference.docx restyled to match OneNote's Calibri look."""
    subprocess.run(["pandoc", "-o", str(path), "--print-default-data-file", "reference.docx"], check=True)
    d = docx.Document(str(path))
    # Look styles up by display name: python-docx's d.styles[...] lowercases built-in names
    # ("heading 1"), which pandoc's reference.docx does not use.
    styles = {s.name: s for s in d.styles}
    for name in ["Normal", "Body Text", "First Paragraph", "Compact", "Block Text"]:
        st = styles[name]
        st.font.name = FONT
        st.font.size = Pt(11)
        st.font.color.rgb = RGBColor(0x26, 0x26, 0x26)
    for name, size in [("Title", 22), ("Heading 1", 18), ("Heading 2", 14), ("Heading 3", 12), ("Heading 4", 11)]:
        st = styles[name]
        st.font.name = FONT
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor.from_string(NAVY)
        rpr = st.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is None:
            fonts = OxmlElement("w:rFonts")
            rpr.append(fonts)
        for attr in ["w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"]:
            fonts.set(qn(attr), FONT)
        for attr in ["w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"]:
            if fonts.get(qn(attr)) is not None:
                del fonts.attrib[qn(attr)]
    # Pandoc writes every table with the "Table" style; give it visible grid borders.
    table_style = styles["Table"].element
    tbl_pr = table_style.find(qn("w:tblPr"))
    if tbl_pr is None:
        tbl_pr = OxmlElement("w:tblPr")
        table_style.append(tbl_pr)
    borders = OxmlElement("w:tblBorders")
    for edge in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        b = OxmlElement(f"w:{edge}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "4")
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), "A6A6A6")
        borders.append(b)
    tbl_pr.append(borders)
    # Bold, shaded header row (pandoc marks it with tblLook firstRow).
    first_row = OxmlElement("w:tblStylePr")
    first_row.set(qn("w:type"), "firstRow")
    rpr = OxmlElement("w:rPr")
    rpr.append(OxmlElement("w:b"))
    first_row.append(rpr)
    tcpr = OxmlElement("w:tcPr")
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "D9E2F3")
    tcpr.append(shd)
    first_row.append(tcpr)
    table_style.append(first_row)
    d.save(str(path))


def pandoc_docx(sources, out, ref):
    out.parent.mkdir(parents=True, exist_ok=True)
    # gfm enables tex_math_dollars; turn it off so dollar amounts ("$1,234 ... $56") stay text.
    cmd = ["pandoc", "-f", "gfm-tex_math_dollars", "-t", "docx", f"--reference-doc={ref}",
           f"--lua-filter={BUILD / 'links.lua'}", "-o", str(out)]
    subprocess.run(cmd + [str(s) for s in sources], check=True)


def _text_width_twips(d):
    sect = d.sections[0]
    if None in (sect.page_width, sect.left_margin, sect.right_margin):
        return 9360  # pandoc leaves page size unset: Word's default Letter with 1-inch margins, 6.5 in
    return int((sect.page_width - sect.left_margin - sect.right_margin) / 635)  # EMU -> twips


def _set_width(el, tag, twips, kind="dxa"):
    w = el.find(qn(tag))
    if w is None:
        w = OxmlElement(tag)
        el.append(w)
    w.set(qn("w:w"), str(twips))
    w.set(qn("w:type"), kind)


def size_table_columns(path, page_breaks=False):
    """Give each table column a width proportional to its content.

    The gfm reader writes equal-width columns, so a 4-character "Week" column gets as much
    room as a sentence-long one and narrow text columns wrap a word per line.
    """
    d = docx.Document(str(path))
    total = _text_width_twips(d)
    min_col, max_share = 900, 0.6  # twips (about 0.6 in); no column wider than 60% of the line
    for table in d.tables:
        rows = [[c.text for c in r.cells] for r in table.rows]
        ncols = max((len(r) for r in rows), default=0)
        if ncols < 2:
            continue
        weights = []
        for c in range(ncols):
            cells = [r[c] for r in rows if c < len(r)]
            longest_word = max((len(w) for t in cells for w in t.split()), default=1)
            lengths = [len(t) for t in cells] or [1]
            mean_len = sum(lengths) / len(lengths)
            weights.append(max(longest_word, (mean_len * min(max(lengths), 90)) ** 0.5, 3))
        widths = [w / sum(weights) * total for w in weights]
        widths = [min(max(w, min_col), total * max_share) for w in widths]
        widths = [int(w * total / sum(widths)) for w in widths]
        tbl = table._tbl
        tbl_pr = tbl.tblPr
        _set_width(tbl_pr, "w:tblW", total)
        layout = tbl_pr.find(qn("w:tblLayout"))
        if layout is None:
            layout = OxmlElement("w:tblLayout")
            tbl_pr.append(layout)
        layout.set(qn("w:type"), "fixed")
        grid = tbl.tblGrid
        for gc in list(grid):
            grid.remove(gc)
        for w in widths:
            gc = OxmlElement("w:gridCol")
            gc.set(qn("w:w"), str(w))
            grid.append(gc)
        for row in table.rows:
            for c, cell in enumerate(row.cells[:ncols]):
                _set_width(cell._tc.get_or_add_tcPr(), "w:tcW", widths[c])
    if page_breaks:
        h1 = [p for p in d.paragraphs if p.style is not None and p.style.name == "Heading 1"]
        for para in h1[1:]:
            para.paragraph_format.page_break_before = True
    d.save(str(path))


def first_heading(md):
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md.stem


def build_docs():
    md_files = sorted(DOCS.rglob("*.md"))
    if not md_files:
        fail("no Markdown files under docs/")
    with tempfile.TemporaryDirectory() as tmp:
        ref = Path(tmp) / "reference.docx"
        make_reference_docx(ref)
        for md in md_files:
            rel = md.relative_to(DOCS)
            out_dir = DIST / "trainer-only" if rel.as_posix() in TRAINER_ONLY else DIST / "docs" / rel.parent
            out = out_dir / f"{md.stem}.docx"
            pandoc_docx([md], out, ref)
            size_table_columns(out)
        handbook = [DOCS / name for name in HANDBOOK_ORDER if (DOCS / name).exists()]
        if handbook:
            # A static contents list: a Word TOC field shows up empty in OneNote and Word Online.
            cover = Path(tmp) / "cover.md"
            cover.write_text(
                "# BSA Onboarding Handbook\n\n"
                f"Program start: {PROGRAM_START:%A, %B %-d, %Y}\n\n## Contents\n\n"
                + "".join(f"{i}. {first_heading(md)}\n" for i, md in enumerate(handbook, 1)),
                encoding="utf-8")
            out = DIST / "BSA-Onboarding-Handbook.docx"
            pandoc_docx([cover] + handbook, out, ref)
            size_table_columns(out, page_breaks=True)
    print(f"docs: {len(md_files)} Word files + handbook")


# --------------------------------------------------------------- Excel ----

HEADER_FILL = PatternFill("solid", fgColor=NAVY)
HEADER_FONT = Font(name=FONT, bold=True, color="FFFFFF")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
GREEN = PatternFill("solid", fgColor="C6EFCE")
AMBER = PatternFill("solid", fgColor="FFEB9C")
RED = PatternFill("solid", fgColor="FFC7CE")
THIN = Side(style="thin", color="BFBFBF")
GRID = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def title_rows(ws, title, subtitle):
    ws["A1"] = title
    ws["A1"].font = Font(name=FONT, size=16, bold=True, color=NAVY)
    ws["A2"] = subtitle
    ws["A2"].font = Font(name=FONT, italic=True, color="595959")


def write_table(ws, header_row, headers, rows, widths, input_cols=()):
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=header_row, column=c, value=h)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, GRID
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for r, row in enumerate(rows, header_row + 1):
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.border, cell.alignment = GRID, WRAP
            cell.font = Font(name=FONT, size=10)
            if c in input_cols:
                cell.fill = INPUT_FILL
    for c, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = ws.cell(row=header_row + 1, column=1)
    last = header_row + max(len(rows), 1)
    ws.auto_filter.ref = f"A{header_row}:{get_column_letter(len(headers))}{last}"
    return header_row + 1, last


def list_validation(ws, values, rng, prompt=None):
    dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
    if prompt:
        dv.prompt, dv.showInputMessage = prompt, True
    ws.add_data_validation(dv)
    dv.add(rng)


def start_here_sheet(wb):
    ws = wb.active
    ws.title = "Start Here"
    title_rows(ws, "BSA Onboarding Trackers", "Skills, knowledge, tool inventory and glossary for Hire A (Research) and Hire B (Standard Cost)")
    ws["A4"], ws["B4"] = "Program start (Day 1)", PROGRAM_START
    ws["B4"].number_format = "ddd mmm d, yyyy"
    ws["B4"].fill = INPUT_FILL
    wb.defined_names["ProgramStart"] = DefinedName("ProgramStart", attr_text="'Start Here'!$B$4")
    for i, (label, date) in enumerate(MILESTONES, 5):
        ws.cell(row=i, column=1, value=f"{label} review")
        ws.cell(row=i, column=2, value=date).number_format = "ddd mmm d, yyyy"
    ws["A9"] = "Proficiency scale"
    ws["A9"].font = Font(name=FONT, bold=True, color=NAVY, size=12)
    scale = [
        (0, "Not yet exposed"),
        (1, "Aware: can explain the basics"),
        (2, "Guided: does it with help"),
        (3, "Independent: does it alone; work is reviewed"),
        (4, "Owns/teaches: runs it, improves it, can train others"),
    ]
    for i, (lvl, desc) in enumerate(scale, 10):
        ws.cell(row=i, column=1, value=lvl).alignment = Alignment(horizontal="center")
        ws.cell(row=i, column=2, value=desc)
    ws["A16"] = "How to use"
    ws["A16"].font = Font(name=FONT, bold=True, color=NAVY, size=12)
    howto = [
        "Yellow cells are inputs. Everything else is reference data or formulas.",
        "Skills tabs: the hire updates 'Current self-rating' every Friday. At each milestone review the trainer enters the agreed rating in 'Rating @Dxx'. Green = at or above target, amber = one below, red = two or more below.",
        "Knowledge tabs: the hire updates Status, Date covered and Confidence as topics are taught. A Status cell turns red when its target week has passed and the topic is not yet Covered.",
        "Tool Inventory: the hires fill this in during week 2 (split the tools between them). It becomes the team's first catalog of custom tools.",
        "Dashboard: rolls up % of skills at target per milestone. Review it in the weekly 1:1.",
        "Generic-only: replace [COMPANY: ...] placeholders on company systems, not in the source repo.",
    ]
    for i, line in enumerate(howto, 17):
        ws.cell(row=i, column=1, value="•")
        c = ws.cell(row=i, column=2, value=line)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[i].height = 30
    ws.column_dimensions["A"].width = 24
    ws.column_dimensions["B"].width = 110


SKILL_COLS = ["skill_id", "module", "category", "skill", "what_good_looks_like",
              "hire_a_d30", "hire_a_d60", "hire_a_d90", "hire_b_d30", "hire_b_d60", "hire_b_d90"]
TOPIC_COLS = ["topic_id", "module", "topic", "learning_objective", "primary_trainer",
              "suggested_resource", "target_week", "self_check_question"]
GLOSSARY_COLS = ["term", "definition", "country", "category"]


def skills_sheet(wb, hire, track, skills):
    ws = wb.create_sheet(f"Skills - {hire}")
    title_rows(ws, f"Skills tracker: {hire} ({track} track)", "Scale 0-4 (see Start Here). Targets come from the 30/60/90 plan.")
    key = "hire_a" if hire == "Hire A" else "hire_b"
    headers = ["Skill ID", "Module", "Category", "Skill", "What good looks like (level 3)",
               "Target D30", "Rating @D30", "Target D60", "Rating @D60", "Target D90", "Rating @D90",
               "Current self-rating", "Evidence / notes"]
    rows = [[s["skill_id"], s["module"], s["category"], s["skill"], s["what_good_looks_like"],
             int(s[f"{key}_d30"]), None, int(s[f"{key}_d60"]), None, int(s[f"{key}_d90"]), None, None, None]
            for s in skills]
    first, last = write_table(ws, 4, headers, rows, [10, 8, 18, 34, 46, 8, 9, 8, 9, 8, 9, 10, 36],
                              input_cols=(7, 9, 11, 12, 13))
    for col in "GIKL":
        list_validation(ws, ["0", "1", "2", "3", "4"], f"{col}{first}:{col}{last}", "Enter 0-4")
    for rating, target in [("G", "F"), ("I", "H"), ("K", "J"), ("L", "J")]:
        rng = f"{rating}{first}:{rating}{last}"
        r, t = f"${rating}{first}", f"${target}{first}"
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND({r}<>"",{r}>={t})'], fill=GREEN))
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND({r}<>"",{r}={t}-1)'], fill=AMBER))
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND({r}<>"",{r}<{t}-1)'], fill=RED))
    return ws.title, first, last


def knowledge_sheet(wb, hire, track, own_module, topics):
    ws = wb.create_sheet(f"Knowledge - {hire}")
    title_rows(ws, f"Knowledge tracker: {hire} ({track} track)", "Update Status, Date covered and Confidence as you go. Turn gaps into questions for your 1:1.")
    other = "M5C" if own_module == "M5R" else "M5R"
    headers = ["Topic ID", "Module", "Priority", "Topic", "Learning objective", "Trainer", "Resource",
               "Target week", "Week starts", "Status", "Date covered", "Confidence (1-5)",
               "Card / doc written?", "Self-check question", "Notes"]
    rows = []
    for i, t in enumerate(topics):
        priority = "Primary" if t["module"] == own_module else "Awareness" if t["module"] == other else "Core"
        r = 5 + i
        rows.append([t["topic_id"], t["module"], priority, t["topic"], t["learning_objective"], t["primary_trainer"],
                     t["suggested_resource"], int(t["target_week"]), f"=ProgramStart+(H{r}-1)*7",
                     "Not started", None, None, None, t["self_check_question"], None])
    first, last = write_table(ws, 4, headers, rows, [10, 8, 11, 32, 42, 11, 34, 8, 12, 15, 12, 10, 11, 42, 30],
                              input_cols=(10, 11, 12, 13, 15))
    for r in range(first, last + 1):
        ws[f"I{r}"].number_format = "mmm d"
        ws[f"K{r}"].number_format = "mmm d"
    list_validation(ws, ["Not started", "In progress", "Covered", "Teach-back done"], f"J{first}:J{last}")
    list_validation(ws, ["1", "2", "3", "4", "5"], f"L{first}:L{last}", "1 = lost, 5 = could teach it")
    list_validation(ws, ["Y", "N"], f"M{first}:M{last}")
    ws.conditional_formatting.add(
        f"J{first}:J{last}",
        FormulaRule(formula=[f'AND(TODAY()>$I{first}+4,$J{first}<>"Covered",$J{first}<>"Teach-back done")'], fill=RED))
    ws.conditional_formatting.add(f"J{first}:J{last}", FormulaRule(formula=[f'$J{first}="Teach-back done"'], fill=GREEN))
    return ws.title, first, last


def tool_inventory_sheet(wb):
    ws = wb.create_sheet("Tool Inventory")
    title_rows(ws, "Custom tool inventory", "Built by the hires in week 2. One row per tool; one tool doc per row (docs/templates/knowledge/tool-doc.md).")
    headers = ["Tool ID", "Tool name", "Purpose / process supported", "Business users", "Stack",
               "Where code / file lives", "Data sources", "Run frequency", "Knowledge holder today", "Backup",
               "Documentation", "Known issues", "Risk if it breaks", "e2open impact", "Assigned learner",
               "Tool doc link", "Target doc date"]
    rows = [[f"T-{i:02d}", f"[COMPANY: tool {i}]"] + [None] * (len(headers) - 2) for i in range(1, 16)]
    first, last = write_table(ws, 4, headers, rows,
                              [8, 24, 34, 18, 14, 26, 22, 12, 18, 14, 13, 28, 12, 13, 13, 24, 12],
                              input_cols=tuple(range(2, 18)))
    list_validation(ws, ["Python", "Excel VBA", "Access", "Power Apps", "Power Automate", "Other"], f"E{first}:E{last}")
    list_validation(ws, ["None", "Partial", "Complete"], f"K{first}:K{last}")
    list_validation(ws, ["High", "Medium", "Low"], f"M{first}:M{last}")
    list_validation(ws, ["Replaced", "Integrates", "Unaffected", "TBD"], f"N{first}:N{last}")
    list_validation(ws, ["Hire A", "Hire B", "Senior", "Manager"], f"O{first}:O{last}")
    for r in range(first, last + 1):
        ws[f"Q{r}"].number_format = "mmm d"
    ws.conditional_formatting.add(f"M{first}:M{last}", FormulaRule(formula=[f'$M{first}="High"'], fill=RED))
    ws.conditional_formatting.add(f"K{first}:K{last}", FormulaRule(formula=[f'$K{first}="None"'], fill=AMBER))


def glossary_sheet(wb, terms):
    ws = wb.create_sheet("Glossary")
    title_rows(ws, "Glossary", "Filter by country or category. Add company-specific terms on the company copy only.")
    rows = [[t["term"], t["definition"], t["country"], t["category"]] for t in sorted(terms, key=lambda t: t["term"].lower())]
    write_table(ws, 4, ["Term", "Definition", "Country", "Category"], rows, [28, 90, 10, 14])


def dashboard_sheet(wb, skill_sheets, knowledge_sheets, modules):
    ws = wb.create_sheet("Dashboard", 1)
    title_rows(ws, "Dashboard", "Formulas only. Ratings come from the Skills tabs; status from the Knowledge tabs.")
    ws["A4"] = "Skills at or above target (skills with target > 0)"
    ws["A4"].font = Font(name=FONT, bold=True, color=NAVY, size=12)
    hdr = ["Hire", "Milestone", "Skills with target", "Rated", "At target", "% at target"]
    for c, h in enumerate(hdr, 1):
        cell = ws.cell(row=5, column=c, value=h)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, GRID
    r = 6
    for (hire, _, _), (sheet, first, last) in zip(HIRES, skill_sheets):
        for label, tcol, rcol in [("Day 30", "F", "G"), ("Day 60", "H", "I"), ("Day 90", "J", "K")]:
            q = f"'{sheet}'!"
            T, R = f"{q}${tcol}${first}:${tcol}${last}", f"{q}${rcol}${first}:${rcol}${last}"
            vals = [hire, label, f'=COUNTIF({T},">0")', f"=COUNT({R})",
                    f'=SUMPRODUCT(({R}<>"")*({T}>0)*({R}>={T}))', f'=IF(D{r}=0,"",E{r}/C{r})']
            for c, v in enumerate(vals, 1):
                cell = ws.cell(row=r, column=c, value=v)
                cell.border = GRID
            ws.cell(row=r, column=6).number_format = "0%"
            r += 1
    r += 1
    ws.cell(row=r, column=1, value="Average current self-rating vs Day 90 target, by module").font = Font(name=FONT, bold=True, color=NAVY, size=12)
    r += 1
    hdr2 = ["Module", "Hire A self-rating", "Hire A D90 target", "Hire B self-rating", "Hire B D90 target"]
    for c, h in enumerate(hdr2, 1):
        cell = ws.cell(row=r, column=c, value=h)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, GRID
    r += 1
    for m in modules:
        ws.cell(row=r, column=1, value=m).border = GRID
        for i, (sheet, first, last) in enumerate(skill_sheets):
            q = f"'{sheet}'!"
            M, L, J = (f"{q}$B${first}:$B${last}", f"{q}$L${first}:$L${last}", f"{q}$J${first}:$J${last}")
            ws.cell(row=r, column=2 + 2 * i, value=f'=IFERROR(AVERAGEIFS({L},{M},A{r}),"")').number_format = "0.0"
            ws.cell(row=r, column=3 + 2 * i, value=f'=IFERROR(AVERAGEIFS({J},{M},A{r}),"")').number_format = "0.0"
            for c in (2 + 2 * i, 3 + 2 * i):
                ws.cell(row=r, column=c).border = GRID
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Knowledge topics by status").font = Font(name=FONT, bold=True, color=NAVY, size=12)
    r += 1
    statuses = ["Not started", "In progress", "Covered", "Teach-back done"]
    for c, h in enumerate(["Hire"] + statuses + ["Overdue"], 1):
        cell = ws.cell(row=r, column=c, value=h)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, GRID
    r += 1
    for (hire, _, _), (sheet, first, last) in zip(HIRES, knowledge_sheets):
        q = f"'{sheet}'!"
        J, I = f"{q}$J${first}:$J${last}", f"{q}$I${first}:$I${last}"
        ws.cell(row=r, column=1, value=hire).border = GRID
        for c, s in enumerate(statuses, 2):
            ws.cell(row=r, column=c, value=f'=COUNTIF({J},"{s}")').border = GRID
        ws.cell(row=r, column=6, value=f'=SUMPRODUCT((TODAY()>{I}+4)*({J}<>"Covered")*({J}<>"Teach-back done"))').border = GRID
        r += 1
    for col, w in zip("ABCDEF", [22, 18, 18, 18, 18, 14]):
        ws.column_dimensions[col].width = w


def build_trackers():
    skills = read_csv(DATA / "trackers" / "skills.csv", SKILL_COLS)
    topics = read_csv(DATA / "trackers" / "knowledge-topics.csv", TOPIC_COLS)
    terms = read_csv(DATA / "trackers" / "glossary.csv", GLOSSARY_COLS)
    wb = Workbook()
    start_here_sheet(wb)
    skill_sheets = [skills_sheet(wb, h, t, skills) for h, t, _ in HIRES]
    knowledge_sheets = [knowledge_sheet(wb, h, t, m, topics) for h, t, m in HIRES]
    tool_inventory_sheet(wb)
    glossary_sheet(wb, terms)
    modules = list(dict.fromkeys(s["module"] for s in skills))
    dashboard_sheet(wb, skill_sheets, knowledge_sheets, modules)
    out = DIST / "BSA-Onboarding-Trackers.xlsx"
    wb.save(out)
    print(f"trackers: {len(skills)} skills, {len(topics)} topics, {len(terms)} glossary terms -> {out.relative_to(ROOT)}")


# ---------------------------------------------------------------- Anki ----

def build_anki(preview=False):
    try:
        print(anki_deck.build_deck(ROOT, DIST, preview=preview))
    except anki_deck.DeckError as e:
        fail(str(e))


# ----------------------------------------------------- generated helpers ----

def run_generators():
    for script in [BUILD / "make_tariff_model.py", DATA / "analytics" / "generate_practice_data.py"]:
        if script.exists():
            subprocess.run([sys.executable, str(script)], check=True, cwd=ROOT)
            print(f"ran {script.relative_to(ROOT)}")
        else:
            print(f"skipped {script.relative_to(ROOT)} (not found)")


def main():
    if shutil.which("pandoc") is None:
        fail("pandoc is not installed")
    DIST.mkdir(exist_ok=True)
    for sub in ("docs", "trainer-only"):
        if (DIST / sub).exists():
            shutil.rmtree(DIST / sub)
    build_docs()
    build_trackers()
    build_anki(preview="--preview-cards" in sys.argv)
    run_generators()


if __name__ == "__main__":
    main()
