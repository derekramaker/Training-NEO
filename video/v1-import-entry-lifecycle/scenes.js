// v1-import-entry-lifecycle: what is on screen at time t (seconds into the scene).
// Each [data-step=n] element fades in at times[n], timed to the sentence that mentions it.

// Time at a fraction of the way through sentence i (for words in the middle of a long sentence).
const within = (sc, i, frac) => {
  const s = sc.sentences[Math.min(i, sc.sentences.length - 1)];
  return s.start - sc.start + frac * (s.end - s.start);
};

Stage.video({
  scenes: [
    {
      id: "title",
      render(el, t, sc, S) {
        S.steps(el, t, [S.at(sc, 1, 0)]);
      },
    },
    {
      id: "cast",
      render(el, t, sc, S) {
        S.steps(el, t, [
          S.at(sc, 0, 0.1),         // 0 importer of record
          S.at(sc, 1, 0),           // 1 broker (and its arrow)
          S.at(sc, 2, 0),           // 2 customs agency (and its arrow)
          within(sc, 2, 0.23),      // 3 CBP
          within(sc, 2, 0.4),       // 4 CBSA
          within(sc, 2, 0.54),      // 5 ANAM
        ]);
      },
    },
    {
      id: "us-entry",
      render(el, t, sc, S) {
        // The ring is the entry: it travels to each stop as the narration reaches it, then waits there.
        const X = [250, 590, 930, 1330, 1680];
        const go = [0.2, within(sc, 0, 0.2), S.at(sc, 1, 0), S.at(sc, 3, 0), S.at(sc, 4, 0)];
        const move = 0.9;
        S.steps(el, t, [
          0,                         // 0 the timeline
          go[0] + 0.1,               // 1 arrival
          go[1] + move * 0.7,        // 2 entry and release
          go[2] + move * 0.7,        // 3 entry summary
          S.at(sc, 2, 0.1),          // 4 post summary correction window
          go[3] + move * 0.7,        // 5 liquidation
          go[4] + move * 0.7,        // 6 protest
        ]);
        const ring = el.querySelector("#tl-ring");
        let x = X[0];
        for (let k = 1; k < X.length; k++) x += (X[k] - X[k - 1]) * S.prog(t, go[k], move);
        ring.setAttribute("cx", x.toFixed(1));
        ring.style.opacity = S.prog(t, go[0], 0.5);
      },
    },
    {
      id: "canada",
      render(el, t, sc, S) {
        S.steps(el, t, [
          within(sc, 0, 0.25),       // 0 release
          S.at(sc, 1, 0.2),          // 1 CAD
          S.at(sc, 2, 0),            // 2 monthly statement
          within(sc, 2, 0.64),       // 3 CARM Client Portal
        ]);
      },
    },
    {
      id: "mexico",
      render(el, t, sc, S) {
        S.steps(el, t, [
          within(sc, 0, 0.52),       // 0 pay first
          within(sc, 0, 0.76),       // 1 then release
          within(sc, 1, 0.35),       // 2 padrón de importadores
          within(sc, 2, 0.47),       // 3 "files the declaration: the pedimento"
          within(sc, 3, 0.18),       // 4 including IVA
          S.at(sc, 4, 0),            // 5 IMMEX follows other rules
        ]);
      },
    },
    {
      id: "audit",
      render(el, t, sc, S) {
        S.steps(el, t, [
          within(sc, 0, 0.25),       // 0 we send
          within(sc, 0, 0.5),        // 1 classification
          within(sc, 0, 0.74),       // 2 value
          within(sc, 0, 0.86),       // 3 origin
          S.at(sc, 1, 0),            // 4 the broker files; wrong data, wrong filing
          S.at(sc, 2, 0),            // 5 reasonable care
          S.at(sc, 3, 0),            // 6 we audit
        ]);
      },
    },
    {
      id: "remember",
      render(el, t, sc, S) {
        S.steps(el, t, [
          0.1,                       // 0 the one thing to remember
          within(sc, 1, 0.15),       // 1 customs primer
          within(sc, 1, 0.66),       // 2 Anki
        ]);
      },
    },
  ],
});
