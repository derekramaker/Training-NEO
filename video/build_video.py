#!/usr/bin/env python3
"""Build one training video from its source folder.

    python3 video/build_video.py <id> --storyboard   # narration + one still per scene (for review)
    python3 video/build_video.py <id>                # full render -> dist/videos/<id>.mp4 (+ .vtt, poster, script)

A video lives in video/<id>/:
    script.yaml   title and scenes; each scene has an id and the sentences to say (`say`), optional `hold` seconds
    scenes.html   one <section class="scene" id="..."> per scene; {{diagram:NAME}} inlines data/anki/diagrams/NAME.svg
    scenes.js     Stage.video({scenes: [{id, render(el, t, scene, S) {...}}]}): what is on screen at time t
    style.css     optional, video-specific styles
Every frame is a pure function of time, so a rebuild produces the same video.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / "video/engine"
DIAGRAMS = ROOT / "data/anki/diagrams"
FPS = 30


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def narrate(vdir, build):
    """Synthesize the narration unless script.yaml is unchanged since the last run."""
    digest = hashlib.sha256(b"".join(f.read_bytes() for f in
                                     [vdir / "script.yaml", ENGINE / "narrate.py", ENGINE / "lexicon.yaml"])).hexdigest()
    stamp = build / "script.sha256"
    if (build / "timings.json").exists() and stamp.exists() and stamp.read_text() == digest:
        return json.loads((build / "timings.json").read_text())
    run([sys.executable, str(ENGINE / "narrate.py"), str(vdir)])
    stamp.write_text(digest)
    return json.loads((build / "timings.json").read_text())


def assemble(vdir, build, timings):
    css = (DIAGRAMS / "_style.css").read_text() + (ENGINE / "base.css").read_text()
    if (vdir / "style.css").exists():
        css += (vdir / "style.css").read_text()
    body = (vdir / "scenes.html").read_text(encoding="utf-8")

    def inline(m):
        svg = DIAGRAMS / f"{m.group(1)}.svg"
        if not svg.exists():
            sys.exit(f"{vdir.name}: no diagram {svg.name}")
        return re.sub(r"<\?xml[^>]*\?>", "", svg.read_text(encoding="utf-8"))

    body = re.sub(r"\{\{diagram:([a-z0-9-]+)\}\}", inline, body)
    ids = set(re.findall(r'<section class="scene[^"]*" id="([^"]+)"', body))
    missing = [s["id"] for s in timings["scenes"] if s["id"] not in ids]
    if missing:
        sys.exit(f"{vdir.name}: scenes.html has no section for {missing}")
    page = ("<!doctype html><html><head><meta charset='utf-8'><style>" + css + "</style></head><body>" + body +
            "<div id='caption'></div><div id='progress'></div><div id='fade'></div>"
            f"<script>window.TIMINGS = {json.dumps(timings)};</script>"
            "<script>" + (ENGINE / "stage.js").read_text() + "</script>"
            "<script>" + (vdir / "scenes.js").read_text(encoding="utf-8") + "</script></body></html>")
    out = build / "index.html"
    out.write_text(page, encoding="utf-8")
    return out


def storyboard(build, page, timings):
    """One still per scene, just after its last sentence (everything built, before the switch), plus a contact sheet."""
    sb = build / "storyboard"
    if sb.exists():
        shutil.rmtree(sb)
    sb.mkdir(parents=True)
    shots = []
    for i, sc in enumerate(timings["scenes"], 1):
        t = sc["end"] + 0.1  # the dip to the next scene starts 0.2 s after the end
        shots.append(f"{t:.3f}:{sb / f'{i:02d}-{sc['id']}.png'}")
    run(["node", str(ENGINE / "render.cjs"), "--still", str(page)] + shots)
    from PIL import Image, ImageDraw
    files = sorted(sb.glob("*.png"))
    thumbs = [Image.open(f).resize((640, 360)) for f in files]
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 660 + 20, rows * 410 + 20), "#E9EDF3")
    draw = ImageDraw.Draw(sheet)
    for i, (th, f) in enumerate(zip(thumbs, files)):
        x, y = 20 + (i % cols) * 660, 20 + (i // cols) * 410
        sheet.paste(th, (x, y))
        draw.text((x, y + 364), f.stem, fill="#1F3864")
    sheet.save(build / "storyboard.png")
    return build / "storyboard.png"


def music(seconds, out, sr=44100):
    """A quiet, slow pad (Cmaj7 - Am7 - Fmaj7 - G6) synthesized here, so there is no licensing question."""
    chords = [[261.63, 329.63, 392.00, 493.88], [220.00, 261.63, 329.63, 392.00],
              [174.61, 220.00, 261.63, 329.63], [196.00, 246.94, 293.66, 329.63]]
    bar = 4.0
    n = int(seconds * sr)
    t = np.arange(n) / sr
    audio = np.zeros(n)
    for k in range(int(np.ceil(seconds / bar)) + 1):
        start = k * bar - 1.0
        idx = (t >= start) & (t < start + bar + 2.0)
        if not idx.any():
            continue
        local = t[idx] - start
        env = np.clip(local / 1.5, 0, 1) * np.clip((bar + 2.0 - local) / 1.5, 0, 1)
        for f in chords[k % 4]:
            audio[idx] += env * (np.sin(2 * np.pi * f * t[idx]) + 0.25 * np.sin(4 * np.pi * f * t[idx]))
        audio[idx] += env * 0.6 * np.sin(np.pi * chords[k % 4][0] * t[idx])  # soft root an octave down
    audio *= 0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * t)  # slow swell
    kernel = np.ones(24) / 24
    audio = np.convolve(audio, kernel, mode="same")  # take the edge off the highs
    fade = np.clip(t / 2.5, 0, 1) * np.clip((seconds - t) / 3.0, 0, 1)
    audio = audio * fade
    audio = 0.25 * audio / (np.max(np.abs(audio)) or 1)
    sf.write(out, np.stack([audio, audio], axis=1).astype(np.float32), sr)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    vid = sys.argv[1]
    vdir = ROOT / "video" / vid
    build = vdir / "build"
    build.mkdir(parents=True, exist_ok=True)
    timings = narrate(vdir, build)
    page = assemble(vdir, build, timings)
    if "--storyboard" in sys.argv:
        print(f"storyboard: {storyboard(build, page, timings).relative_to(ROOT)}")
        return
    total = timings["total"]
    silent = build / "video-silent.mp4"
    run(["node", str(ENGINE / "render.cjs"), str(page), str(silent), str(total), str(FPS)])
    music(total, build / "music.wav")
    dist = ROOT / "dist/videos"
    dist.mkdir(parents=True, exist_ok=True)
    out = dist / f"{vid}.mp4"
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(silent), "-i", str(build / "narration.wav"),
         "-i", str(build / "music.wav"), "-filter_complex",
         "[1:a]aresample=44100,pan=stereo|c0=c0|c1=c0[v];[2:a]volume=0.16[m];[v][m]amix=inputs=2:duration=first:normalize=0[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
         str(out)])
    shutil.copy(build / "captions.vtt", dist / f"{vid}.vtt")
    poster_t = timings["scenes"][0]["start"] + 0.7 * (timings["scenes"][0]["end"] - timings["scenes"][0]["start"])
    run(["node", str(ENGINE / "render.cjs"), "--still", str(page), f"{poster_t:.3f}:{dist / f'{vid}-poster.png'}"])
    script = yaml.safe_load((vdir / "script.yaml").read_text(encoding="utf-8"))
    lines = [f"# {script['title']}", "", f"Narration script ({total:.0f} s). Edit video/{vid}/script.yaml and rebuild.", ""]
    for sc in script["scenes"]:
        lines += [f"## {sc['id']}", ""] + [f"- {s}" for s in sc["say"]] + [""]
    (dist / f"{vid}-script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"video: {out.relative_to(ROOT)} ({total:.1f} s, {out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
