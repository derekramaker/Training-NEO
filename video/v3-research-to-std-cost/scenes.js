// v3-research-to-std-cost: a tariff action -> Research (the WHAT) -> Standard Cost (the $) -> the business, with the one
// shared Tariff-Impact Model under the two tracks. The same chain sits on top of every scene after the title; the step
// being explained is navy, the others are dimmed, and a link turns blue (arrowhead once it lands, then three packets)
// when the narration says something moves along it. The model bar lights when the narration points at the workbook.
(function () {
  const NODES = [
    ["Tariff action", "little warning"],
    ["Research", "the WHAT"],
    ["Standard Cost", "the $"],
    ["The business", "gets the answer"],
  ];
  const W = 342, GAP = 120, H = 112;
  const nodeX = (i) => i * (W + GAP);

  const lab = (t, s) => `<div class="lab"><div class="nt">${t}</div><div class="ns">${s}</div></div>`;

  // The arrowheads for the lit links and the return link. Defined ONCE, in a visible 0x0 svg on the body: a marker
  // inside a scene that is display:none does not render, and six chain strips would give six elements the same id.
  const marker = (id, color, size) =>
    `<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="${size}" markerHeight="${size}" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="${color}"/></marker>`;
  function defineMarkers() {
    const holder = document.createElement("div");
    holder.innerHTML = `<svg width="0" height="0" style="position:absolute"><defs>${marker("arrow-flow", "#2E75B6", 3.6)}${marker("arrow-back", "#C55A11", 4)}</defs></svg>`;
    document.body.prepend(holder.firstChild);
  }

  // Fill each <div class="chain">: nodes, grey base arrows, blue flow overlays, the accent return link (Standard Cost
  // back to Research) and the model bar.
  function buildChain(c) {
    let html = `<svg class="chain-lines" width="1728" height="190" viewBox="0 0 1728 190">`;
    for (let i = 0; i < 3; i++) {
      const x1 = nodeX(i) + W + 14, x2 = nodeX(i + 1) - 16;
      html += `<path class="base-arrow" d="M${x1} ${H / 2} H${x2}"/>`;
      html += `<path class="flowline" data-flow="${i}" d="M${x1} ${H / 2} H${x2 - 4}"/>`;
      for (let k = 0; k < 3; k++) html += `<circle class="pulse" data-pk="${i}" data-k="${k}" r="8" cx="${x1}" cy="${H / 2}"/>`;
    }
    // Return link in the Research -> Standard Cost gap, below the forward arrow: "a doubtful item goes back to Research"
    const bx1 = nodeX(2) - 16, bx2 = nodeX(1) + W + 14;
    html += `<path class="backline" data-back d="M${bx1} ${H / 2 + 30} H${bx2 + 4}"/>`;
    html += `<circle class="pulse" data-backpk r="8" cx="${bx1}" cy="${H / 2 + 30}"/>`;
    // Ticks from the two tracks down to the model bar
    html += `<path class="tick" d="M${nodeX(1) + W / 2} ${H} V134"/><path class="tick" d="M${nodeX(2) + W / 2} ${H} V134"/>`;
    html += "</svg>";
    NODES.forEach(([t, s], i) => {
      html += `<div class="node" data-n="${i}" style="left:${nodeX(i)}px">` +
        `<div class="n-off">${lab(t, s)}</div><div class="n-on">${lab(t, s)}</div></div>`;
    });
    html += `<div class="model">One shared Tariff-Impact Model<div class="m-on">One shared Tariff-Impact Model</div></div>`;
    c.innerHTML = html;
  }

  // hl: [[node, on, off?], ...] seconds into the scene; flows: [[link, at], ...]; back: when the return link draws;
  // model: [[on, off?], ...] when the model bar lights.
  function chain(el, t, S, { hl = [], flows = [], back = null, model = [] }) {
    const c = el.querySelector(".chain");
    if (!c) return;
    c.querySelectorAll(".node").forEach((n, i) => {
      let p = 0;
      hl.forEach(([k, on, off]) => {
        if (k === i) p = Math.max(p, S.prog(t, on, 0.7) - (off !== undefined ? S.prog(t, off, 0.7) : 0));
      });
      n.querySelector(".n-on").style.opacity = p;
      n.style.opacity = 0.45 + 0.55 * p;
    });
    let mp = 0;
    model.forEach(([on, off]) => { mp = Math.max(mp, S.prog(t, on, 0.7) - (off !== undefined ? S.prog(t, off, 0.7) : 0)); });
    const m = c.querySelector(".model");
    m.querySelector(".m-on").style.opacity = mp;
    m.style.opacity = 0.55 + 0.45 * mp;
    c.querySelectorAll("[data-flow]").forEach((path) => {
      const i = Number(path.dataset.flow);
      const f = flows.find(([k]) => k === i);
      const p = f ? S.prog(t, f[1], 0.9) : 0;
      S.draw(path, p);
      path.style.markerEnd = p > 0.97 ? "url(#arrow-flow)" : "none";
      // Once the link has landed, three packets run along it: the work moving. Then the line stays still.
      const len = path.getTotalLength();
      c.querySelectorAll(`[data-pk="${i}"]`).forEach((dot) => {
        const q = f ? S.clamp((t - (f[1] + 0.9 + 0.45 * Number(dot.dataset.k))) / 1.1) : 0;
        const pt = path.getPointAtLength(len * q);
        dot.setAttribute("cx", pt.x.toFixed(1));
        dot.style.opacity = q > 0 && q < 1 ? Math.min(1, Math.sin(Math.PI * q) * 1.5) : 0;
      });
    });
    const b = c.querySelector("[data-back]");
    const bp = back !== null ? S.prog(t, back, 0.8) : 0;
    S.draw(b, bp);
    b.style.markerEnd = bp > 0.97 ? "url(#arrow-back)" : "none";
    const dot = c.querySelector("[data-backpk]");
    const q = back !== null ? S.clamp((t - (back + 0.8)) / 1.0) : 0;
    const pt = b.getPointAtLength(b.getTotalLength() * q);
    dot.setAttribute("cx", pt.x.toFixed(1));
    dot.style.opacity = q > 0 && q < 1 ? Math.min(1, Math.sin(Math.PI * q) * 1.5) : 0;
  }

  // Time `frac` of the way through sentence i of the scene.
  const f = (S, sc, i, frac) => {
    const s = sc.sentences[i];
    return S.at(sc, i) + frac * (s.end - s.start);
  };

  Stage.video({
    init() {
      defineMarkers();
      document.querySelectorAll(".chain").forEach(buildChain);
    },
    scenes: [
      {
        id: "title",
        render(el, t, sc, S) {
          // "Research says what" / "Standard Cost says how much"
          S.steps(el, t, [0, f(S, sc, 1, 0.3), f(S, sc, 1, 0.62)]);
        },
      },
      {
        id: "action",
        render(el, t, sc, S) {
          // "It starts with a notice, sometimes with little warning." / "An authority, HTS tariff headings, countries, a rate, an effective date."
          chain(el, t, S, { hl: [[0, 0.1]] });
          S.steps(el, t, [
            f(S, sc, 0, 0.08),                                                                           // the notice
            f(S, sc, 1, 0.02), f(S, sc, 1, 0.2), f(S, sc, 1, 0.45), f(S, sc, 1, 0.6), f(S, sc, 1, 0.76),  // five fields
            f(S, sc, 0, 0.55),                                                                           // "little warning"
          ]);
        },
      },
      {
        id: "research",
        render(el, t, sc, S) {
          // The action lands on Research's desk as the scene opens; then the first pass, the brief's parts, the no-$ rule.
          chain(el, t, S, { hl: [[0, -5, 0.1], [1, 0.1]], flows: [[0, 0.05]] });
          S.steps(el, t, [
            0,
            S.at(sc, 1, 0.05),                                                           // first-pass card
            f(S, sc, 1, 0.4), f(S, sc, 1, 0.55), f(S, sc, 1, 0.7), f(S, sc, 1, 0.85),    // its four lines
            S.at(sc, 2, 0.05),                                                           // the brief
            // sources (3, 4) · timing · scope and exclusions · rates and how they stack · affected items · confidence + open questions
            f(S, sc, 2, 0.24), f(S, sc, 2, 0.32), f(S, sc, 2, 0.38), f(S, sc, 2, 0.52), f(S, sc, 2, 0.78), f(S, sc, 2, 0.9),
            S.at(sc, 3, 0.1),                                                            // what is in scope, no $
          ]);
        },
      },
      {
        id: "handoff",
        render(el, t, sc, S) {
          // "Then a fifteen-minute call": the brief and the Action tab move to Standard Cost.
          const call = S.at(sc, 3, 0.05);
          chain(el, t, S, {
            hl: [[1, 0.1], [2, call + 1.4]],
            flows: [[0, -5], [1, call]],
            model: [[f(S, sc, 1, 0.25)]],                                                // "the Action tab"
          });
          S.steps(el, t, [
            S.at(sc, 0, 0.3),
            S.at(sc, 1, 0.05), f(S, sc, 1, 0.25), f(S, sc, 1, 0.6),                     // brief v1.0 · Action tab · item list
            S.at(sc, 2, 0.02), f(S, sc, 2, 0.22), f(S, sc, 2, 0.75),
            call, f(S, sc, 3, 0.55),
          ]);
        },
      },
      {
        id: "stdcost",
        render(el, t, sc, S) {
          const back = f(S, sc, 4, 0.45);
          chain(el, t, S, {
            hl: [[2, 0.1]],
            flows: [[0, -5], [1, -5]],
            model: [[S.at(sc, 1, 0.05)]],
            back,
          });
          S.steps(el, t, [
            0,
            S.at(sc, 1, 0.05),                                                           // Items tab
            f(S, sc, 1, 0.3), f(S, sc, 1, 0.42), f(S, sc, 1, 0.55), f(S, sc, 1, 0.75),  // its rows
            S.at(sc, 2, 0.02),                                                           // Calc
            f(S, sc, 2, 0.3), f(S, sc, 2, 0.55), f(S, sc, 2, 0.8),                      // duty, landed cost, margin
            S.at(sc, 3, 0.02), f(S, sc, 3, 0.12), f(S, sc, 3, 0.42), f(S, sc, 3, 0.7),  // then: Oracle, with Finance, variance
            S.at(sc, 4, 0.05),                                                           // never changes the scope
          ]);
        },
      },
      {
        id: "controls",
        render(el, t, sc, S) {
          // Sentence 0 is maker-checker, 1 the urgency rule's first band, 2 the other two bands.
          // "signs off before release": the checked answer reaches the business.
          const release = f(S, sc, 0, 0.55);
          chain(el, t, S, {
            hl: [[1, 0.1], [2, 0.1], [3, release + 1.4]],
            flows: [[0, -5], [1, -5], [2, release]],
          });
          S.steps(el, t, [
            0,                                                                           // (unused)
            S.at(sc, 0, 0.02), f(S, sc, 0, 0.12), f(S, sc, 0, 0.2),                      // maker, arrow, checker
            f(S, sc, 0, 0.5), release, f(S, sc, 0, 0.8),                                 // arrow, release, after day 90
            S.at(sc, 1, 0.02), f(S, sc, 1, 0.25), f(S, sc, 1, 0.55), f(S, sc, 1, 0.8),  // caption, band 1, trainer, shadow
            S.at(sc, 2, 0.02), f(S, sc, 2, 0.2), f(S, sc, 2, 0.42),                     // band 2, you, same day
            f(S, sc, 2, 0.68), f(S, sc, 2, 0.82),                                        // band 3, normal cycle
          ]);
        },
      },
      {
        id: "remember",
        render(el, t, sc, S) {
          chain(el, t, S, {
            hl: [[0, 0.1], [1, 0.1], [2, 0.1], [3, 0.1]],
            flows: [[0, -5], [1, -5], [2, -5]],
            model: [[f(S, sc, 0, 0.62)]],
          });
          S.steps(el, t, [
            S.at(sc, 0, 0.2), f(S, sc, 0, 0.62), f(S, sc, 0, 0.8),   // what / how much; one model; two signatures
            S.at(sc, 1, 0.1), f(S, sc, 1, 0.55),                     // brief template; model guide
            S.at(sc, 2, 0.05), f(S, sc, 2, 0.42),                    // Unit 01 G5; "from week seven" Unit 06 G1-G3
          ]);
        },
      },
    ],
  });
})();
