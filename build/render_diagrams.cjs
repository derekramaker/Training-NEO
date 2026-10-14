#!/usr/bin/env node
// Render flashcard diagrams (data/anki/diagrams/*.svg) to PNG with headless Chromium, and check them against the
// rules in data/anki/diagrams/README.md.
//
//   node build/render_diagrams.cjs --jobs jobs.json      # used by build/build.py
//   node build/render_diagrams.cjs --preview <file.svg>  # full image plus every hide/show variant, for authors
//   node build/render_diagrams.cjs --screenshot page.html out.png [width]  # card contact sheets
//
// A job is {svg, out, mode: "full" | "hide" | "show", key}. "hide" covers each [data-cloze=key] label with a "?" box;
// "show" highlights it. Prints a JSON report: one entry per job with any rule violations ("issues").

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

function loadPlaywright() {
  try {
    return require("playwright");
  } catch (e) {
    const root = execSync("npm root -g").toString().trim();
    return require(path.join(root, "playwright"));
  }
}

const ROOT = path.resolve(__dirname, "..");
const CSS = fs.readFileSync(path.join(ROOT, "data/anki/diagrams/_style.css"), "utf8");
const marker = (id, color) =>
  `<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" ` +
  `orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="${color}"/></marker>`;
const MARKERS =
  '<svg width="0" height="0" style="position:absolute"><defs>' +
  marker("arrow", "#1F3864") + marker("arrow-soft", "#8497B0") + marker("arrow-accent", "#C55A11") +
  "</defs></svg>";

function page_html(svg) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#fff}${CSS}</style>` +
    `</head><body>${MARKERS}<div id="wrap">${svg}</div></body></html>`;
}

// Runs in the page: check the rules, then apply the hide/show variant.
function inspect_and_apply([mode, key]) {
  const NS = "http://www.w3.org/2000/svg";
  const svg = document.querySelector("#wrap svg");
  const issues = [];
  if (!svg) return { issues: ["no <svg> element"], keys: [] };
  const vb = svg.viewBox.baseVal;
  if (!vb || vb.width !== 640) issues.push(`canvas width is ${vb ? vb.width : "unset"}, expected 640`);
  if (vb && (vb.height < 240 || vb.height > 480)) issues.push(`canvas height ${vb.height} is outside 240-480`);
  if (!svg.classList.contains("diagram")) issues.push('the <svg> needs class="diagram"');

  const label = (el) => (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 40);
  const texts = [...svg.querySelectorAll("text, tspan")];
  for (const t of texts) {
    if (!(t.textContent || "").trim()) continue;
    const size = parseFloat(getComputedStyle(t).fontSize);
    if (size < 17.99) issues.push(`text "${label(t)}" is ${size}px; minimum is 18px`);
  }
  const sr = svg.getBoundingClientRect();
  const boxes = [...svg.querySelectorAll("text")]
    .filter((t) => (t.textContent || "").trim())
    .map((t) => ({ t, r: t.getBoundingClientRect() }));
  for (const { t, r } of boxes) {
    if (r.left < sr.left - 1 || r.right > sr.right + 1 || r.top < sr.top - 1 || r.bottom > sr.bottom + 1)
      issues.push(`text "${label(t)}" runs off the canvas`);
  }
  for (let i = 0; i < boxes.length; i++) {
    for (let j = i + 1; j < boxes.length; j++) {
      const a = boxes[i], b = boxes[j];
      if (a.t.hasAttribute("data-allow-overlap") || b.t.hasAttribute("data-allow-overlap")) continue;
      const w = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
      const h = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
      if (w > 2 && h > 2) issues.push(`texts "${label(a.t)}" and "${label(b.t)}" overlap`);
    }
  }
  for (const fo of svg.querySelectorAll("foreignObject")) {
    const div = fo.firstElementChild;
    const foh = fo.height.baseVal.value, fow = fo.width.baseVal.value;
    if (div && (div.scrollHeight > foh + 1 || div.scrollWidth > fow + 1))
      issues.push(`table content (${div.scrollWidth}x${div.scrollHeight}) overflows its foreignObject (${fow}x${foh})`);
  }

  const keys = [...new Set([...svg.querySelectorAll("[data-cloze]")].map((e) => e.getAttribute("data-cloze")))];
  if (mode === "hide" || mode === "show") {
    const targets = [...svg.querySelectorAll(`[data-cloze="${key}"]`)];
    if (!targets.length) issues.push(`no element with data-cloze="${key}"`);
    for (const el of targets) {
      const bb = el.getBBox();
      const pad = 6;
      const w = Math.max(bb.width + 2 * pad, 64), h = Math.max(bb.height + 2 * pad, 36);
      const x = bb.x + bb.width / 2 - w / 2, y = bb.y + bb.height / 2 - h / 2;
      const rect = document.createElementNS(NS, "rect");
      Object.entries({ x, y, width: w, height: h, rx: 8 }).forEach(([k, v]) => rect.setAttribute(k, v));
      // The mask or highlight must not cover any other label.
      const vb2 = svg.viewBox.baseVal, scale = sr.width / vb2.width;
      const toPage = (bx, by, bw, bh) => {
        const m = el.getCTM();
        const p1 = new DOMPoint(bx, by).matrixTransform(m), p2 = new DOMPoint(bx + bw, by + bh).matrixTransform(m);
        return { left: sr.left + p1.x * scale, top: sr.top + p1.y * scale, right: sr.left + p2.x * scale, bottom: sr.top + p2.y * scale };
      };
      const mr = toPage(x, y, w, h);
      for (const { t, r } of boxes) {
        if (el.contains(t)) continue;
        const ow = Math.min(mr.right, r.right) - Math.max(mr.left, r.left);
        const oh = Math.min(mr.bottom, r.bottom) - Math.max(mr.top, r.top);
        if (ow > 1 && oh > 1) issues.push(`the ${mode} box for "${key}" covers "${label(t)}"; give that label more room`);
      }
      if (mode === "hide") {
        rect.setAttribute("class", "cloze-mask");
        const q = document.createElementNS(NS, "text");
        Object.entries({ x: x + w / 2, y: y + h / 2 + 1, class: "t-lg cloze-q mid" }).forEach(([k, v]) => q.setAttribute(k, v));
        q.textContent = "?";
        el.style.visibility = "hidden";
        el.parentNode.insertBefore(q, el.nextSibling);
        el.parentNode.insertBefore(rect, q);
      } else {
        rect.setAttribute("class", "cloze-hl");
        el.parentNode.insertBefore(rect, el);
      }
    }
  }
  return { issues, keys };
}

async function render(jobs) {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const context = await browser.newContext({ deviceScaleFactor: 2, viewport: { width: 700, height: 560 } });
  const page = await context.newPage();
  const report = [];
  for (const job of jobs) {
    const svg = fs.readFileSync(job.svg, "utf8").replace(/<\?xml[^>]*\?>/, "");
    await page.setContent(page_html(svg), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const result = await page.evaluate(inspect_and_apply, [job.mode || "full", job.key || ""]);
    if (job.out) {
      fs.mkdirSync(path.dirname(job.out), { recursive: true });
      const el = await page.$("#wrap svg");
      if (el) await el.screenshot({ path: job.out });
    }
    report.push({ ...job, ...result });
  }
  await browser.close();
  return report;
}

async function main() {
  const args = process.argv.slice(2);
  if (args[0] === "--jobs") {
    const jobs = JSON.parse(fs.readFileSync(args[1], "utf8"));
    process.stdout.write(JSON.stringify(await render(jobs)));
    return;
  }
  if (args[0] === "--preview") {
    const svg = path.resolve(args[1]);
    const id = path.basename(svg, ".svg");
    const outDir = path.join(ROOT, "build/.cache/preview", id);
    const [full] = await render([{ svg, out: path.join(outDir, `${id}.png`), mode: "full" }]);
    const variants = full.keys.flatMap((k) => ["hide", "show"].map((mode) => ({
      svg, mode, key: k, out: path.join(outDir, `${id}-${mode}-${k}.png`) })));
    const rest = variants.length ? await render(variants) : [];
    const all = [full, ...rest];
    for (const r of all) {
      console.log(`${r.issues.length ? "FAIL" : "ok  "} ${path.relative(ROOT, r.out)}`);
      for (const i of r.issues) console.log(`     - ${i}`);
    }
    console.log(`cloze keys: ${full.keys.join(", ") || "(none)"}`);
    process.exitCode = all.some((r) => r.issues.length) ? 1 : 0;
    return;
  }
  if (args[0] === "--screenshot") {
    // Full-page screenshot of a local HTML file (card contact sheets).
    const { chromium } = loadPlaywright();
    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width: Number(args[3] || 820), height: 900 } });
    await page.goto("file://" + path.resolve(args[1]), { waitUntil: "load" });
    await page.screenshot({ path: args[2], fullPage: true });
    await browser.close();
    return;
  }
  console.error("usage: render_diagrams.cjs --jobs jobs.json | --preview file.svg | --screenshot page.html out.png [width]");
  process.exitCode = 2;
}

main().catch((e) => { console.error(e); process.exitCode = 1; });
