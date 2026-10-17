# Training videos

Short (60–120 s) narrated explainers for stable concepts. Each video is code: a narration script, scene markup and
a render function of time. Change a sentence or a box, rebuild, and the MP4, captions and script update together.

| Video | Supports |
|---|---|
| `v1-import-entry-lifecycle` | Weeks 1–2, customs (M1) |
| `v2-trade-data-flow` | Weeks 1–2, trade systems and e2open (M2, M10) |
| `v3-research-to-std-cost` | Week 3 on, the Research → Standard Cost handoff (M5R, M5C, the boundary and control rules) |
| `v4-usmca-origin-bom` | Weeks 2–3, USMCA origin with a bill of materials (M1, customs primer §10) |

## Build

```
python3 video/build_video.py <id> --storyboard   # narration + one still per scene: video/<id>/build/storyboard.png
python3 video/build_video.py <id>                # dist/videos/<id>.mp4, .vtt captions, poster PNG, script
```

Needs ffmpeg, node with Playwright (headless Chromium), and Python with numpy, soundfile, pyyaml, pillow and
`kokoro-onnx`. The voice is Kokoro-82M (Apache-2.0), voice `af_heart`, run locally. Put `model.onnx` (from
huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX, `onnx/model.onnx`) and `voices.npz` in `video/.models/`, or set
`KOKORO_DIR`. `voices.npz` is built from the repo's `voices/af_heart.bin` (float32, shape 510 x 1 x 256) with numpy.
The music bed is synthesized by the build script, so nothing needs a license.

## Authoring rules

- **Frame:** 1920 x 1080. Keep content between y = 140 and y = 880: the caption bar sits below that.
- **Diagrams:** `{{diagram:NAME}}` inlines a flashcard diagram from `data/anki/diagrams/`. A 640 x 400 diagram at
  1100 px wide is 690 px tall: size the wrapper so the diagram fits inside the content area.
- **Text:** at least 30 px. One idea per scene; the narration says it, the screen shows it.
- **Timing:** reveal things when the narration mentions them: `S.at(scene, i, offset)` is the time sentence `i`
  starts. `S.steps(el, t, times)` fades in each `[data-step=n]` element at `times[n]`; paths with class `draw` draw on.
- **Pronunciation:** the voice misreads some acronyms and the Spanish terms ("CAD" as "cad", "AS400" as "as four
  hundred"). Write the term normally in `script.yaml` and add its phonemes to `video/engine/lexicon.yaml`; the captions
  keep the written form. Check a line with `python3 video/engine/narrate.py --phonemes "text"` and listen to it with
  `python3 video/engine/narrate.py --say "text" out.wav`.
- **Storyboard:** `--storyboard` takes one still just after each scene's last sentence, when everything is built.
- **Facts:** only what the verified primers, decks and plan say. No current tariff rates or status.
- **Generic only:** fictional items and countries, no company names, people or internal systems.

## Hosting

Upload the MP4 to Microsoft Stream (SharePoint) and add the `.vtt` file as its captions; use the poster PNG as the
thumbnail. Put the Stream link on the matching OneNote page (the docs carry `[COMPANY: Stream link]` placeholders).
