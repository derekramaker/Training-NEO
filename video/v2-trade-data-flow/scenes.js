// v2-trade-data-flow: Oracle -> AS400 trade system -> brokers -> entry data back, and e2open replacing the AS400.
// The same four-step chain sits on top of every scene after the title; the step being explained is navy, the others
// are dimmed, and a link turns blue (with an arrowhead once it lands) when the narration says data moves along it.
(function () {
  const NODES = [
    ["Oracle", "items start here"],
    ["AS400", "adds trade data"],
    ["Brokers", "file with customs"],
    ["Entry data", "comes back to us"],
  ];
  const W = 342, GAP = 120, H = 136;
  const nodeX = (i) => i * (W + GAP);

  const lab = (t, s, cls) => `<div class="lab ${cls}"><div class="nt">${t}</div><div class="ns">${s}</div></div>`;

  // Fill each <div class="chain">: nodes, grey base arrows, blue flow overlays. data-n1 relabels node 1,
  // data-swap1 adds a second label for node 1 that the scene cross-fades to.
  function buildChain(c) {
    const labels = NODES.map((n) => n.slice());
    if (c.dataset.n1) labels[1] = c.dataset.n1.split("|");
    const swap = c.dataset.swap1 ? c.dataset.swap1.split("|") : null;
    let html = `<svg class="chain-lines" width="1728" height="${H}" viewBox="0 0 1728 ${H}">` +
      `<defs><marker id="arrow-flow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2E75B6"/></marker></defs>`;
    for (let i = 0; i < 3; i++) {
      const x1 = nodeX(i) + W + 14, x2 = nodeX(i + 1) - 16;
      html += `<path class="base-arrow" d="M${x1} ${H / 2} H${x2}"/>`;
      html += `<path class="flowline" data-flow="${i}" d="M${x1} ${H / 2} H${x2 - 4}"/>`;
    }
    html += "</svg>";
    labels.forEach(([t, s], i) => {
      const alt = i === 1 && swap;
      html += `<div class="node" data-n="${i}" style="left:${nodeX(i)}px">` +
        `<div class="n-off">${lab(t, s, "a")}${alt ? lab(swap[0], swap[1], "b") : ""}</div>` +
        `<div class="n-on">${lab(t, s, "a")}${alt ? lab(swap[0], swap[1], "b") : ""}</div></div>`;
    });
    c.innerHTML = html;
    c.querySelectorAll(".lab.b").forEach((b) => (b.style.opacity = 0));
  }

  // hl: [[node, on, off?], ...] seconds into the scene; flows: [[link, at], ...]; swapAt: when node 1 changes label.
  function chain(el, t, S, { hl = [], flows = [], swapAt = null }) {
    const c = el.querySelector(".chain");
    if (!c) return;
    c.querySelectorAll(".node").forEach((n, i) => {
      let p = 0;
      hl.forEach(([k, on, off]) => {
        if (k === i) p = Math.max(p, S.prog(t, on, 0.7) - (off !== undefined ? S.prog(t, off, 0.7) : 0));
      });
      n.querySelector(".n-on").style.opacity = p;
      n.style.opacity = 0.45 + 0.55 * p;
      if (swapAt !== null && n.querySelector(".lab.b")) {
        // old label lifts out, then the new one rises in (never both at once)
        const out = S.prog(t, swapAt, 0.45), inn = S.prog(t, swapAt + 0.4, 0.55);
        n.querySelectorAll(".lab.a").forEach((a) => { a.style.opacity = 1 - out; a.style.transform = `translateY(${-34 * out}px)`; });
        n.querySelectorAll(".lab.b").forEach((b) => { b.style.opacity = inn; b.style.transform = `translateY(${34 * (1 - inn)}px)`; });
      }
    });
    c.querySelectorAll("[data-flow]").forEach((path) => {
      const i = Number(path.dataset.flow);
      const f = flows.find(([k]) => k === i);
      const p = f ? S.prog(t, f[1], 0.9) : 0;
      S.draw(path, p);
      path.style.markerEnd = p > 0.97 ? "url(#arrow-flow)" : "none";
    });
  }

  // Time `frac` of the way through sentence i of the scene.
  const f = (S, sc, i, frac) => {
    const s = sc.sentences[i];
    return S.at(sc, i) + frac * (s.end - s.start);
  };

  Stage.video({
    init() {
      document.querySelectorAll(".chain").forEach(buildChain);
    },
    scenes: [
      {
        id: "title",
        render(el, t, sc, S) {
          // "a round trip: out to the brokers, and back to us as entries" / "and what e2open changes"
          S.steps(el, t, [0, f(S, sc, 0, 0.12), f(S, sc, 0, 0.3), f(S, sc, 0, 0.5), f(S, sc, 0, 0.78), f(S, sc, 1, 0.55)]);
        },
      },
      {
        id: "oracle",
        render(el, t, sc, S) {
          // "...our main business system for items, purchase orders and standard costs." / "New and changed items flow on"
          chain(el, t, S, { hl: [[0, 0.1]], flows: [[0, f(S, sc, 1, 0.45)]] });
          S.steps(el, t, [f(S, sc, 0, 0.42), f(S, sc, 0, 0.52), f(S, sc, 0, 0.63), f(S, sc, 0, 0.82), S.at(sc, 1, 0)]);
        },
      },
      {
        id: "as400",
        render(el, t, sc, S) {
          chain(el, t, S, { hl: [[1, 0.1]], flows: [[0, -5]] });
          S.steps(el, t, [
            S.at(sc, 0, 0.6),
            f(S, sc, 1, 0.14), f(S, sc, 1, 0.44), f(S, sc, 1, 0.62),
            f(S, sc, 2, 0.5), f(S, sc, 2, 0.66), f(S, sc, 2, 0.78),
          ]);
        },
      },
      {
        id: "product-file",
        render(el, t, sc, S) {
          const toBroker = S.at(sc, 1, 0.1);
          chain(el, t, S, { hl: [[1, 0.1, toBroker + 0.5], [2, toBroker + 0.5]], flows: [[0, -5], [1, toBroker]] });
          S.steps(el, t, [
            S.at(sc, 0, 0.3),
            f(S, sc, 0, 0.6), f(S, sc, 0, 0.7), f(S, sc, 0, 0.78), f(S, sc, 0, 0.86), f(S, sc, 0, 0.94),
            f(S, sc, 2, 0.2),
            S.at(sc, 3, 0.1),
          ]);
        },
      },
      {
        id: "entries",
        render(el, t, sc, S) {
          const back = S.at(sc, 0, 0.6);
          chain(el, t, S, { hl: [[2, 0.1, back + 0.5], [3, back + 0.5]], flows: [[0, -5], [1, -5], [2, back]] });
          S.steps(el, t, [
            f(S, sc, 0, 0.45),
            f(S, sc, 0, 0.72), f(S, sc, 0, 0.82), f(S, sc, 0, 0.92),
            S.at(sc, 1, 0.1), f(S, sc, 1, 0.45),
            S.at(sc, 2, 0), S.at(sc, 2, 0.1),
            f(S, sc, 2, 0.22), f(S, sc, 2, 0.46), f(S, sc, 2, 0.74),
          ], 0.7);
        },
      },
      {
        id: "e2open",
        render(el, t, sc, S) {
          chain(el, t, S, { hl: [[1, 0.1]], flows: [[0, -5], [1, -5], [2, -5]], swapAt: f(S, sc, 0, 0.6) });
          S.steps(el, t, [
            S.at(sc, 1, 0.1), f(S, sc, 1, 0.3), f(S, sc, 1, 0.4), f(S, sc, 1, 0.5), f(S, sc, 1, 0.6),
            S.at(sc, 2, 0.1), f(S, sc, 2, 0.45),   // "For your own process" / "the as-is doc"
            S.at(sc, 3, 0.1),                      // "And the data map"
            S.at(sc, 4, 0.1),                      // "Then you help clean the data and test"
            f(S, sc, 4, 0.62),                     // "so nothing is lost in the move"
          ]);
        },
      },
      {
        id: "remember",
        render(el, t, sc, S) {
          chain(el, t, S, { hl: [[0, 0.1], [1, 0.1], [2, 0.1], [3, 0.1]], flows: [[0, -5], [1, -5], [2, -5]] });
          S.steps(el, t, [S.at(sc, 0, 0.2), S.at(sc, 1, 0.3), S.at(sc, 2, 0.1), f(S, sc, 2, 0.56)]);
        },
      },
    ],
  });
})();
