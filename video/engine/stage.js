// Browser-side helpers for the training videos. Every frame is a pure function of time: the renderer calls
// window.renderAt(t) and screenshots, so a video renders identically every time (no CSS animations, no timers).
//
// A video page loads this file, then its own scenes.js, which calls Stage.video({...}).
(function () {
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const ease = (x) => { x = clamp(x); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  // Progress 0..1 of an animation that starts at `start` (seconds into the scene) and lasts `dur`.
  const prog = (t, start, dur = 0.6) => ease((t - start) / dur);

  const Stage = {
    clamp, ease, prog,
    timings: null,
    scenes: {},

    // Fade and slide an element in: y offset in px.
    fadeIn(el, p, y = 18) {
      if (!el) return;
      el.style.opacity = p;
      el.style.transform = `translateY(${(1 - p) * y}px)`;
    },
    // Draw an SVG path or line progressively (stroke-dashoffset). Call once with p in 0..1.
    draw(el, p) {
      if (!el) return;
      const len = el.getTotalLength ? el.getTotalLength() : 0;
      el.style.strokeDasharray = `${len}`;
      el.style.strokeDashoffset = `${len * (1 - p)}`;
      el.style.opacity = p > 0 ? 1 : 0;
    },
    // Time (seconds into the scene) at which sentence i of the scene starts; lets visuals land on the words.
    at(scene, i, offset = 0) {
      const s = scene.sentences[Math.min(i, scene.sentences.length - 1)];
      return s.start - scene.start + offset;
    },

    // Reveal elements marked data-step="n" in order: step n appears at times[n].
    steps(root, t, times, dur = 0.6) {
      root.querySelectorAll("[data-step]").forEach((el) => {
        const n = Number(el.getAttribute("data-step"));
        const start = times[n] !== undefined ? times[n] : Infinity;
        const tag = el.tagName.toLowerCase();
        if (el.classList.contains("draw") && (tag === "path" || tag === "line" || tag === "polyline")) {
          Stage.draw(el, prog(t, start, dur));
        } else {
          Stage.fadeIn(el, prog(t, start, dur), el.dataset.slide ? Number(el.dataset.slide) : 14);
        }
      });
    },

    // Burned-in captions: the current sentence, bottom of the frame.
    caption(t) {
      const box = document.getElementById("caption");
      if (!box || !Stage.timings) return;
      let text = "";
      for (const sc of Stage.timings.scenes)
        for (const s of sc.sentences)
          if (t >= s.start - 0.05 && t <= s.end + 0.25) text = s.text;
      if (box.textContent !== text) box.textContent = text;
      box.style.opacity = text ? 1 : 0;
    },

    video(def) {
      Stage.def = def;
      def.scenes.forEach((s) => (Stage.scenes[s.id] = s));
    },
  };

  // Scene i is on screen from the middle of the gap before it to the middle of the gap after it.
  function switchTimes(T) {
    return T.scenes.map((sc, i) => (i === 0 ? 0 : (T.scenes[i - 1].end + sc.start) / 2));
  }

  // Called by the renderer for every frame.
  window.renderAt = function (t) {
    const T = Stage.timings;
    const sw = switchTimes(T);
    let i = 0;
    while (i + 1 < sw.length && t >= sw[i + 1]) i++;
    const current = T.scenes[i];
    document.querySelectorAll(".scene").forEach((el) => { el.style.display = el.id === current.id ? "block" : "none"; });
    const def = Stage.scenes[current.id];
    if (def && def.render) def.render(document.getElementById(current.id), t - current.start, current, Stage);
    // Dip to dark for 0.25 s either side of each scene switch, and fade out at the very end.
    const fade = document.getElementById("fade");
    if (fade) {
      const d = 0.25;
      const toNext = i + 1 < sw.length ? sw[i + 1] - t : Infinity;
      const fromSwitch = i > 0 ? t - sw[i] : Infinity;
      const o = Math.max(clamp(1 - toNext / d), clamp(1 - fromSwitch / d), clamp((t - (T.total - 0.9)) / 0.9));
      fade.style.opacity = o;
    }
    Stage.caption(t);
    const bar = document.getElementById("progress");
    if (bar) bar.style.width = `${(t / T.total) * 100}%`;
    return true;
  };

  // Shared arrowheads for diagrams (same as the flashcard renderer) and the timings written by narrate.py.
  const marker = (id, color) => `<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="${color}"/></marker>`;
  document.addEventListener("DOMContentLoaded", () => {
    const holder = document.createElement("div");
    holder.innerHTML = `<svg width="0" height="0" style="position:absolute"><defs>${marker("arrow", "#1F3864")}${marker("arrow-soft", "#8497B0")}${marker("arrow-accent", "#C55A11")}</defs></svg>`;
    document.body.prepend(holder.firstChild);
    Stage.timings = window.TIMINGS;
    if (Stage.def && Stage.def.init) Stage.def.init(Stage);
  });

  window.Stage = Stage;
})();
