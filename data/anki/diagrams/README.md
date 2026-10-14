# Flashcard diagrams

Every image in the core Anki deck is an SVG file in this folder, rendered to PNG by `python3 build/build.py`
(through `build/render_diagrams.cjs`, headless Chromium). Edit the SVG, rebuild, and the cards update.

## The rules

1. **Canvas:** `<svg class="diagram" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 H" width="640" height="H">`,
   with `H` between 240 and 480. Start with `<rect class="bg" width="640" height="H"/>`.
2. **Use the classes in `_style.css` only.** No inline colors, fonts or stroke widths. One accent (`box-accent`,
   `t-accent`, `arrow-accent`) per diagram, for the single thing to notice.
3. **Text is at least 18px** (`t-sm`); 20px (`t`) is the default. The card is about 360px wide on a phone, so a
   640-wide diagram is shown at roughly half size. If it does not fit at 18px, the diagram is too busy: split it.
4. **At most 7 boxes and about 6 words per label.** Wrap long labels with `<tspan x=".." dy="1.2em">`.
5. **Arrows:** `<path class="arrow" d="..."/>` (also `arrow-soft`, `arrow-accent`); arrowheads are supplied by the
   renderer. Leave 6px between an arrow tip and the box it points to.
6. **Fill-in-the-diagram cards:** wrap each label that a card hides in `<g data-cloze="KEY">...</g>` (KEY is short,
   for example `broker` or `s3`). A card asks for `diagram?hide=KEY` on the front and `diagram?show=KEY` on the
   back. The renderer covers the hidden label with a "?" box and, on the back, highlights it. Hide labels, not
   whole boxes, and give each hidden label a box at least 90 x 40 so the "?" reads.
7. **Worked examples:** a table goes in `<foreignObject x=".." y=".." width=".." height=".."><div xmlns="http://www.w3.org/1999/xhtml" class="wt"><table>...</table></div></foreignObject>`.
   Use `class="num"` on number cells, `tr.total` for the result row and `tr.hl` for the row to notice.
8. **Fictional and generic only.** Item numbers like `KIT-100`, origins like Country X, no company names, people,
   brokers or internal systems beyond the platform names the program already uses. No current tariff rates.
9. **File name = diagram ID:** lowercase, hyphens, prefixed by unit (`u02-hts-digits.svg`).

Check a diagram while you work:

```
node build/render_diagrams.cjs --preview data/anki/diagrams/u02-hts-digits.svg
```

That writes PNGs (full, plus every hide/show variant) next to the build cache and prints any rule violations
(text under 18px, missing cloze keys, wrong canvas width).
