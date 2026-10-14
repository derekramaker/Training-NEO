#!/usr/bin/env node
// Render a video page frame by frame: for each frame call window.renderAt(t), screenshot, pipe to ffmpeg.
//
//   node video/engine/render.cjs <page.html> <out.mp4> <seconds> [fps]
//   node video/engine/render.cjs --still <page.html> <out.png> <t>      # one frame (storyboards, posters)

const fs = require("fs");
const path = require("path");
const { spawn, execSync } = require("child_process");

function loadPlaywright() {
  try { return require("playwright"); } catch (e) {
    return require(path.join(execSync("npm root -g").toString().trim(), "playwright"));
  }
}

async function open(page_html) {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto("file://" + path.resolve(page_html), { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  return { browser, page };
}

async function stills(page_html, shots) {
  const { browser, page } = await open(page_html);
  for (const [t, out] of shots) {
    await page.evaluate((x) => window.renderAt(x), t);
    await page.screenshot({ path: out });
  }
  await browser.close();
}

async function video(page_html, out, seconds, fps) {
  const { browser, page } = await open(page_html);
  const frames = Math.ceil(seconds * fps);
  const ff = spawn("ffmpeg", ["-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
    { stdio: ["pipe", "inherit", "inherit"] });
  const done = new Promise((res, rej) => ff.on("close", (c) => (c === 0 ? res() : rej(new Error(`ffmpeg exited ${c}`)))));
  for (let i = 0; i < frames; i++) {
    await page.evaluate((x) => window.renderAt(x), i / fps);
    const buf = await page.screenshot({ type: "jpeg", quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
    if (i % (fps * 10) === 0) process.stderr.write(`  frame ${i}/${frames}\n`);
  }
  ff.stdin.end();
  await done;
  await browser.close();
}

(async () => {
  const a = process.argv.slice(2);
  if (a[0] === "--still") {
    // --still page.html t1:out1.png [t2:out2.png ...]
    const shots = a.slice(2).map((s) => { const i = s.indexOf(":"); return [Number(s.slice(0, i)), s.slice(i + 1)]; });
    await stills(a[1], shots);
  } else {
    await video(a[0], a[1], Number(a[2]), Number(a[3] || 30));
  }
})().catch((e) => { console.error(e); process.exitCode = 1; });
