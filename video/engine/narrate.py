#!/usr/bin/env python3
"""Synthesize a video's narration sentence by sentence and record exact timings.

    python3 video/engine/narrate.py video/<id>

Reads video/<id>/script.yaml (scenes, each with a list of sentences), writes to video/<id>/build/:
    narration.wav   the full voice track
    timings.json    scene and sentence start/end times, used by the page and the captions
    captions.vtt    WebVTT captions, one cue per sentence (upload these to Stream)

Voice: Kokoro-82M (Apache-2.0), voice af_heart, run locally through kokoro-onnx. Model files are looked up in
$KOKORO_DIR or video/.models (model.onnx and voices.npz); see video/README.md.
"""

import json
import os
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

VOICE = "af_heart"
SPEED = 1.0
SENTENCE_GAP = 0.35   # seconds of silence between sentences
SCENE_GAP = 0.9       # extra silence between scenes
LEAD_IN = 0.8         # silence before the first sentence
TAIL = 1.5            # silence after the last sentence


def model_dir(root):
    for d in [os.environ.get("KOKORO_DIR"), root / "video/.models"]:
        if d and (Path(d) / "model.onnx").exists() and (Path(d) / "voices.npz").exists():
            return Path(d)
    sys.exit("Kokoro model not found: set KOKORO_DIR or put model.onnx and voices.npz in video/.models")


def vtt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def main():
    vdir = Path(sys.argv[1]).resolve()
    root = Path(__file__).resolve().parents[2]
    script = yaml.safe_load((vdir / "script.yaml").read_text(encoding="utf-8"))
    from kokoro_onnx import Kokoro  # imported late: slow to load

    mdir = model_dir(root)
    tts = Kokoro(str(mdir / "model.onnx"), str(mdir / "voices.npz"))
    out = vdir / "build"
    out.mkdir(parents=True, exist_ok=True)

    sr = 24000
    chunks = [np.zeros(int(LEAD_IN * sr), dtype=np.float32)]
    t = LEAD_IN
    scenes, cues = [], []
    for si, scene in enumerate(script["scenes"]):
        if si:
            chunks.append(np.zeros(int(SCENE_GAP * sr), dtype=np.float32))
            t += SCENE_GAP
        s_start, sentences = t, []
        for ti, text in enumerate(scene["say"]):
            if ti:
                chunks.append(np.zeros(int(SENTENCE_GAP * sr), dtype=np.float32))
                t += SENTENCE_GAP
            audio, rate = tts.create(text, voice=VOICE, speed=SPEED, lang="en-us")
            if rate != sr:
                sys.exit(f"unexpected sample rate {rate}")
            chunks.append(audio.astype(np.float32))
            dur = len(audio) / sr
            sentences.append({"text": text, "start": round(t, 3), "end": round(t + dur, 3)})
            cues.append((t, t + dur, text))
            t += dur
        hold = float(scene.get("hold", 0))  # extra visual time after the scene's last sentence
        if hold:
            chunks.append(np.zeros(int(hold * sr), dtype=np.float32))
            t += hold
        scenes.append({"id": scene["id"], "start": round(s_start, 3), "end": round(t, 3), "sentences": sentences})
    chunks.append(np.zeros(int(TAIL * sr), dtype=np.float32))
    t += TAIL

    audio = np.concatenate(chunks)
    peak = float(np.max(np.abs(audio))) or 1.0
    sf.write(out / "narration.wav", audio * (0.89 / peak), sr)
    timings = {"title": script["title"], "total": round(t, 3), "scenes": scenes}
    (out / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    lines = ["WEBVTT", ""]
    for i, (a, b, text) in enumerate(cues, 1):
        lines += [str(i), f"{vtt_time(a)} --> {vtt_time(b)}", text, ""]
    (out / "captions.vtt").write_text("\n".join(lines), encoding="utf-8")
    print(f"narration: {len(cues)} sentences, {t:.1f}s -> {out.relative_to(root)}")


if __name__ == "__main__":
    main()
