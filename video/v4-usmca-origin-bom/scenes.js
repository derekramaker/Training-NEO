// v4-usmca-origin-bom: does pump PK-100 qualify under USMCA? The five-step strip (list non-originating, tariff shift,
// de minimis, RVC, document) sits on top of every scene from rule-bom on; the step being explained is navy, the others
// dimmed. The bill of materials sits on the left of scenes rule-bom to whatif and keeps its state: rows revealed,
// non-originating rows tinted, the failing housing flagged, and in the what-if its value swapped to 25.
// Every number comes from customs primer section 10.8 (fictional): TV 200, VNM 78, 14/200 = 7.0%; what-if TV 211,
// VNM 89, 25/211 = 11.8%, (211-89)/211 = 57.8%, (185-89)/185 = 51.9%.
(function () {
  // ---------- The step strip ----------
  const STEPS = [["List", "non-originating"], ["Test", "the tariff shift"], ["Apply", "de minimis"], ["Compute", "RVC"], ["Document", "the file"]];
  const SW = 300, SG = 57, SH = 120;
  const stepX = (i) => i * (SW + SG);

  function buildSteps(c) {
    let html = `<svg width="1728" height="${SH}" viewBox="0 0 1728 ${SH}">`;
    for (let i = 0; i < 4; i++) html += `<path class="s-arrow" d="M${stepX(i) + SW + 6} ${SH / 2} H${stepX(i + 1) - 8}"/>`;
    html += "</svg>";
    STEPS.forEach(([v, o], i) => {
      const lab = `<div class="sv">${v}</div><div class="so">${o}</div>`;
      html += `<div class="step" style="left:${stepX(i)}px"><div class="s-off">${lab}</div><div class="s-on">${lab}</div><div class="num">${i + 1}</div></div>`;
    });
    c.innerHTML = html;
  }

  // on: [[step, onTime, offTime?], ...] seconds into the scene.
  function strip(el, t, S, on) {
    const c = el.querySelector(".steps");
    if (!c) return;
    c.querySelectorAll(".step").forEach((n, i) => {
      let p = 0;
      on.forEach(([k, a, b]) => {
        if (k === i) p = Math.max(p, S.prog(t, a, 0.7) - (b !== undefined ? S.prog(t, b, 0.7) : 0));
      });
      n.querySelector(".s-on").style.opacity = p;
      n.style.opacity = 0.45 + 0.55 * p;
    });
  }

  // ---------- The bill of materials ----------
  // component, heading, origin, value (or [base, what-if]), originating
  const BOM = [
    ["Motor", "85.BB", "China", 60, "No"],
    ["Pump housing", "84.AA", "Germany", [14, 25], "No"],
    ["Impeller", "84.AA", "Mexico", 20, "Yes"],
    ["Fasteners", "73.CC", "China", 4, "No"],
    ["Seals", "40.DD", "US", 6, "Yes"],
    ["Labor, overhead, profit", "—", "Mexico", 96, "—"],
  ];
  const NONORIG = [0, 1, 3];
  const swap = (a, b) => `<span class="swap"><span class="va">${a}</span><span class="vb">${b}</span></span>`;

  function buildBom(c) {
    let html = `<div class="bhead"><span class="bt">Bill of materials</span><span class="bs">PK-100 · US$</span></div>` +
      `<div class="brow th"><span>Component</span><span>Heading</span><span>Origin</span><span>Originating</span><span class="num">US$</span></div>`;
    BOM.forEach(([n, h, o, v, y], i) => {
      const val = Array.isArray(v) ? swap(v[0], v[1]) : v;
      html += `<div class="brow" data-r="${i}"><div class="bg"></div><div class="bg flag"></div>` +
        `<span class="c${n.length > 14 ? " long" : ""}">${n}</span><span>${h}</span><span>${o}</span>` +
        `<span class="${y === "Yes" ? "yes" : ""}">${y}</span><span class="num">${val}</span></div>`;
    });
    html += `<div class="brow tot" data-r="tv"><span class="c">Transaction value (TV)</span><span class="sum">excl. international shipping</span>` +
      `<span class="num">${swap(200, 211)}</span></div>`;
    html += `<div class="brow vnm" data-r="vnm"><span class="c">Non-originating (VNM)</span><span class="sum">${swap("60 + 14 + 4", "60 + 25 + 4")}</span>` +
      `<span class="num">${swap(78, 89)}</span></div>`;
    html += `<div class="bnote">Yes = supplier certification on file</div>`;
    c.innerHTML = html;
  }

  // head: when the frame appears; rows: start of the row-by-row reveal (0.3 s apart); tv: the TV row;
  // nonorig: [t, t, t] tint for motor, housing, fasteners; vnm: the VNM row; flag: the housing is flagged;
  // swapAt: the what-if values (housing 25, TV 211, VNM 89) replace the base values.
  function bom(el, t, S, { head = -5, rows = -5, tv = -5, nonorig = null, vnm = null, flag = null, swapAt = null }) {
    const c = el.querySelector(".bom");
    if (!c) return;
    S.fadeIn(c, S.prog(t, head, 0.6));
    c.querySelectorAll(".brow[data-r]").forEach((r) => {
      const k = r.dataset.r;
      let start;
      if (k === "tv") start = tv;
      else if (k === "vnm") start = vnm === null ? Infinity : vnm;
      else start = rows + 0.3 * Number(k);
      S.fadeIn(r, S.prog(t, start, 0.5), 10);
      const j = NONORIG.indexOf(Number(k));
      const bg = r.querySelector(".bg:not(.flag)"), fl = r.querySelector(".bg.flag");
      if (bg) bg.style.opacity = nonorig && j >= 0 ? S.prog(t, nonorig[j], 0.5) : 0;
      if (fl) fl.style.opacity = flag !== null && k === "1" ? S.prog(t, flag, 0.5) : 0;
    });
    c.querySelectorAll(".swap").forEach((s) => {
      // old value lifts out, then the new one rises in (never both at once)
      const out = swapAt === null ? 0 : S.prog(t, swapAt, 0.45), inn = swapAt === null ? 0 : S.prog(t, swapAt + 0.4, 0.55);
      const a = s.querySelector(".va"), b = s.querySelector(".vb");
      a.style.opacity = 1 - out; a.style.transform = `translateY(${-22 * out}px)`;
      b.style.opacity = inn; b.style.transform = `translateY(${22 * (1 - inn)}px)`;
    });
  }

  // Time `frac` of the way through sentence i of the scene.
  const f = (S, sc, i, frac) => {
    const s = sc.sentences[i];
    return S.at(sc, i) + frac * (s.end - s.start);
  };

  Stage.video({
    init() {
      document.querySelectorAll(".steps").forEach(buildSteps);
      document.querySelectorAll(".bom").forEach(buildBom);
      // criterion B gets an "on" layer that the why scene fades in
      const b = document.getElementById("crit-b");
      if (b) b.insertAdjacentHTML("beforeend", `<div class="on"><div class="in"><div class="letter">B</div><div class="ct">Meets its product-specific rule</div></div></div>`);
    },
    scenes: [
      {
        id: "title",
        render(el, t, sc, S) {
          // "Does this pump qualify for USMCA? The answer is in its bill of materials."
          S.steps(el, t, [0, f(S, sc, 0, 0.42), f(S, sc, 0, 0.52), f(S, sc, 0, 0.66), f(S, sc, 0, 0.8), f(S, sc, 0, 0.92)]);
        },
      },
      {
        id: "why",
        render(el, t, sc, S) {
          const crit = S.at(sc, 2, 0.05);
          S.steps(el, t, [
            f(S, sc, 0, 0.08),                 // 0 valid claim
            S.at(sc, 1, 0.05),                 // 1 wrong claim
            f(S, sc, 1, 0.55),                 // 2 "so be ready to prove it"
            crit, crit + 0.1, crit + 0.25, crit + 0.4, crit + 0.55,   // 3 caption, 4-7 chips A to D
          ]);
          const on = el.querySelector("#crit-b .on");
          if (on) on.style.opacity = S.prog(t, f(S, sc, 2, 0.28), 0.6);   // "criterion B"
        },
      },
      {
        id: "rule-bom",
        render(el, t, sc, S) {
          strip(el, t, S, []);
          // "...made in Mexico from this bill of materials": the table fills row by row on those words
          const rows = f(S, sc, 0, 0.5);
          bom(el, t, S, { head: f(S, sc, 0, 0.3), rows, tv: rows + 1.7 });
          S.steps(el, t, [
            f(S, sc, 0, 0.05),                 // 0 the good
            S.at(sc, 1, 0.05),                 // 1 the rule card
            f(S, sc, 1, 0.1),                  // 2 change of heading
            f(S, sc, 1, 0.55),                 // 3 "or regional value content, RVC"
            S.at(sc, 2, 0.05),                 // 4 the thresholds: sixty / fifty percent
          ]);
        },
      },
      {
        id: "steps12",
        render(el, t, sc, S) {
          const step2 = S.at(sc, 1, 0.05);
          strip(el, t, S, [[0, 0.1, step2], [1, step2]]);
          bom(el, t, S, {
            nonorig: [f(S, sc, 0, 0.4), f(S, sc, 0, 0.52), f(S, sc, 0, 0.64)],   // motor, housing, fasteners
            vnm: f(S, sc, 0, 0.78),            // seventy-eight dollars
            flag: f(S, sc, 2, 0.45),           // "the housing shares heading 84.AA"
          });
          S.steps(el, t, [
            step2,                             // 0 caption
            f(S, sc, 1, 0.35),                 // 1 the three non-originating parts ("each")
            f(S, sc, 1, 0.62),                 // 2 the target: the pump's own heading
            S.at(sc, 2, 0.02), f(S, sc, 2, 0.14),   // 3 motor arrow, 4 fasteners arrow
            f(S, sc, 2, 0.3),                  // 5 "pass" marks
            f(S, sc, 2, 0.45),                 // 6 the housing: fail tint and its arrow
            f(S, sc, 2, 0.85),                 // 7 "so it fails": cross and "same heading: no shift"
          ]);
        },
      },
      {
        id: "deminimis",
        render(el, t, sc, S) {
          strip(el, t, S, [[2, 0.1]]);
          bom(el, t, S, { nonorig: [-5, -5, -5], vnm: -5, flag: -5 });
          const pct = f(S, sc, 1, 0.4);        // "is seven percent"
          S.steps(el, t, [
            0.1,                               // 0 caption
            f(S, sc, 0, 0.28),                 // 1 the meter ("failing parts are allowed")
            f(S, sc, 0, 0.62),                 // 2 the 10% limit ("up to ten percent")
            S.at(sc, 1, 0.05),                 // 3 "fourteen"
            f(S, sc, 1, 0.18),                 // 4 "over two hundred"
            pct,                               // 5 = 7.0%
            f(S, sc, 1, 0.58),                 // 6 "the pump qualifies"
            f(S, sc, 1, 0.82),                 // 7 "criterion B"
          ]);
          // The fill grows to 7% on a 0 to 20% scale as the result is said.
          const fill = el.querySelector("#dm-fill");
          if (fill) fill.style.width = `${(7 / 20) * 100 * S.prog(t, pct, 0.8)}%`;
        },
      },
      {
        id: "whatif",
        render(el, t, sc, S) {
          const step4 = S.at(sc, 1, 0.05);
          strip(el, t, S, [[2, -5, step4], [3, step4]]);
          bom(el, t, S, { nonorig: [-5, -5, -5], vnm: -5, flag: -5, swapAt: f(S, sc, 0, 0.25) });   // "twenty-five"
          S.steps(el, t, [
            f(S, sc, 0, 0.45), f(S, sc, 0, 0.85),   // 0 de minimis 11.8%, 1 fails
            f(S, sc, 1, 0.3), f(S, sc, 1, 0.9),     // 2 RVC transaction value, 3 fails
            S.at(sc, 2, 0.05), f(S, sc, 2, 0.85),   // 4 RVC net cost, 5 qualifies
            S.at(sc, 3, 0.05),                      // 6 who certifies
          ]);
        },
      },
      {
        id: "document",
        render(el, t, sc, S) {
          strip(el, t, S, [[4, 0.1]]);
          const cert = S.at(sc, 2, 0.05), flag = f(S, sc, 2, 0.6);
          S.steps(el, t, [
            0.1,                               // 0 the file
            f(S, sc, 0, 0.3), f(S, sc, 0, 0.6), f(S, sc, 0, 0.85),     // 1 BOM, 2 supplier certifications, 3 calculation
            f(S, sc, 1, 0.08), f(S, sc, 1, 0.4), f(S, sc, 1, 0.78),    // 4 rule text, 5 who prepared and checked, 6 date
            cert, cert + 0.5,                  // 7 arrow to the certification, 8 the certification
            flag, flag + 0.5,                  // 9 arrow to our system, 10 the flag
            S.at(sc, 3, 0.05),                 // 11 when customs verifies
          ]);
        },
      },
      {
        id: "remember",
        render(el, t, sc, S) {
          strip(el, t, S, [[0, 0.1], [1, 0.2], [2, 0.3], [3, 0.4], [4, 0.5]]);
          S.steps(el, t, [f(S, sc, 0, 0.1), f(S, sc, 0, 0.6), S.at(sc, 1, 0.05), f(S, sc, 1, 0.55)]);
        },
      },
    ],
  });
})();
