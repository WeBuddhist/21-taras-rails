// IATS 2026 — 16-slide deck per paper/10 - Canonical Paper and Slides Plan.md
// All pipeline numbers from the reviewed tara21 run (corpora/tara21/REVIEW-2026-08-02.md).
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const {
  FaBookOpen, FaUsers, FaSyncAlt, FaLayerGroup, FaAnchor, FaTable,
  FaBalanceScale, FaUserCheck, FaPlayCircle, FaChartBar, FaShieldAlt,
  FaExpandArrowsAlt, FaFlagCheckered, FaExclamationTriangle, FaRobot, FaSearch,
} = require("react-icons/fa");

// ---- palette -------------------------------------------------------------
const MAROON = "7A1E2D";      // dominant
const MAROON_DARK = "4E1220"; // title/close backgrounds
const GOLD = "C9A227";        // accent
const INK = "2B2B2B";         // body text
const MUTED = "6E6E6E";
const TINT = "F7EFE7";        // warm card tint (used sparingly on white)
const TINT2 = "EFE2D2";
const WHITE = "FFFFFF";
const RED = "A3261F";         // invariants / warnings

const SERIF = "Cambria";
const SANS = "Calibri";
const TIB = "Noto Serif Tibetan"; // per 08-plan; PDF backup expected

async function iconPng(Comp, colorHex, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(Comp, { color: `#${colorHex}`, size: String(size) })
  );
  const buf = await sharp(Buffer.from(svg)).resize(size, size).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const icons = {};
  const defs = {
    book: FaBookOpen, users: FaUsers, cycle: FaSyncAlt, layers: FaLayerGroup,
    anchor: FaAnchor, table: FaTable, scale: FaBalanceScale, check: FaUserCheck,
    play: FaPlayCircle, chart: FaChartBar, shield: FaShieldAlt,
    expand: FaExpandArrowsAlt, flag: FaFlagCheckered, warn: FaExclamationTriangle,
    robot: FaRobot, search: FaSearch,
  };
  for (const [k, C] of Object.entries(defs)) icons[k] = await iconPng(C, WHITE);
  const iconsGold = {};
  for (const [k, C] of Object.entries(defs)) iconsGold[k] = await iconPng(C, GOLD);

  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  const W = 13.33, H = 7.5;

  // helpers ---------------------------------------------------------------
  const headIcon = (slide, key, x, y, d = 0.62) => {
    slide.addShape("ellipse", { x, y, w: d, h: d, fill: { color: MAROON }, line: { color: MAROON } });
    slide.addImage({ data: icons[key], x: x + d * 0.22, y: y + d * 0.22, w: d * 0.56, h: d * 0.56 });
  };
  const title = (slide, txt, iconKey) => {
    if (iconKey) headIcon(slide, iconKey, 0.55, 0.42);
    slide.addText(txt, {
      x: iconKey ? 1.35 : 0.55, y: 0.32, w: W - 1.9, h: 0.85,
      fontFace: SERIF, fontSize: 30, bold: true, color: INK, margin: 0, valign: "middle",
    });
  };

  // ---- 1 · TITLE ---------------------------------------------------------
  let s = pres.addSlide();
  s.background = { color: MAROON_DARK };
  s.addText("ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ།", {
    x: 0.8, y: 0.5, w: W - 1.6, h: 0.5, fontFace: TIB, fontSize: 16, color: GOLD, align: "center",
  });
  s.addText("Homage to the Noble Lady Tara — the run's case-study text", {
    x: 0.8, y: 1.0, w: W - 1.6, h: 0.35, fontFace: SANS, fontSize: 10.5, italic: true, color: MUTED, align: "center",
  });
  s.addText("Expanding the Digital Footprint of Tibetan", {
    x: 0.8, y: 1.7, w: W - 1.6, h: 1.0, fontFace: SERIF, fontSize: 40, bold: true, color: WHITE, align: "center",
  });
  s.addText("A Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs", {
    x: 0.8, y: 2.7, w: W - 1.6, h: 0.6, fontFace: SERIF, fontSize: 20, italic: true, color: TINT2, align: "center",
  });
  s.addShape("line", { x: W / 2 - 1.1, y: 3.62, w: 2.2, h: 0, line: { color: GOLD, width: 1.5 } });
  s.addText("Machine-drafted. Human-published. Verification flips the sign of the AI-content loop.", {
    x: 1.6, y: 3.85, w: W - 3.2, h: 0.55, fontFace: SANS, fontSize: 17, color: WHITE, align: "center",
  });
  s.addText([
    { text: "Tashi Tsering · The OpenPecha Project", options: { fontSize: 16, color: TINT2, breakLine: true } },
    { text: "17th IATS Seminar · The Soaltee Kathmandu · 23–29 August 2026", options: { fontSize: 13, color: MUTED } },
  ], { x: 0.8, y: 5.6, w: W - 1.6, h: 1.0, fontFace: SANS, align: "center", color: TINT2 });
  s.addNotes("Thirty seconds. One-line thesis: the same feedback loop that is destroying small-language Wikipedias becomes a virtuous cycle under one condition — human verification. Everything in this talk is that condition made concrete.");

  // ---- 2 · THE GAP -------------------------------------------------------
  s = pres.addSlide();
  title(s, "The gap, in three numbers", "book");
  const stat = (x, big, label, sub) => {
    s.addShape("roundRect", { x, y: 1.55, w: 3.9, h: 3.3, rectRadius: 0.12, fill: { color: TINT }, line: { color: TINT2, width: 1 } });
    s.addText(big, { x, y: 1.85, w: 3.9, h: 1.4, fontFace: SERIF, fontSize: 54, bold: true, color: MAROON, align: "center" });
    s.addText(label, { x: x + 0.25, y: 3.25, w: 3.4, h: 0.6, fontFace: SANS, fontSize: 15, bold: true, color: INK, align: "center" });
    s.addText(sub, { x: x + 0.25, y: 3.85, w: 3.4, h: 0.85, fontFace: SANS, fontSize: 11.5, color: MUTED, align: "center" });
  };
  stat(0.55, "8,072", "bo.wikipedia articles — for 7M+ speakers", "31 active editors/month · 2 admins · ~350 new articles/yr (Jul 2026)");
  stat(4.72, "17.5%", "GPT-4 on Tibetan (TLUE) — below the 25% random baseline", "Qwen-2.5-72B: 84.7% in Chinese → 16.5% in Tibetan (EMNLP 2025)");
  stat(8.89, "4×", "tokenizer cost of Tibetan vs Chinese", "byte-level premium — Tibetan pays more for less (NeurIPS 2023)");
  s.addText("Ask an AI assistant a basic question about Tibetan culture, in Tibetan — it fails. Not because the knowledge is obscure: because the open digital text isn't there.", {
    x: 0.85, y: 5.35, w: W - 1.7, h: 0.9, fontFace: SERIF, fontSize: 16, italic: true, color: INK, align: "center",
  });
  s.addText("Kornai: “digital language death” · Khanna & Li 2025: “invisible giants”", {
    x: 0.85, y: 6.45, w: W - 1.7, h: 0.4, fontFace: SANS, fontSize: 11, color: MUTED, align: "center",
  });
  s.addNotes("Trim-order note: this slide is first to cut if time runs short. Live demo of the chatbot failure is in the recorded video, not live.");

  // ---- 3 · OUR REVIVAL CAMPAIGNS ----------------------------------------
  s = pres.addSlide();
  title(s, "We ran the manual revival — here is what it yields", "users");
  s.addText("First person: OpenPecha and collaborators have trained editors and run bo.wikipedia workshops. The public record shows what manual-only effort achieves.", {
    x: 0.6, y: 1.35, w: W - 1.2, h: 0.6, fontFace: SANS, fontSize: 14.5, color: INK });
  const row = (y, k, v) => {
    s.addText(k, { x: 0.9, y, w: 5.6, h: 0.5, fontFace: SANS, fontSize: 15, bold: true, color: MAROON, margin: 0 });
    s.addText(v, { x: 6.6, y, w: 6.1, h: 0.5, fontFace: SANS, fontSize: 15, color: INK, margin: 0 });
  };
  row(2.15, "bo.wikipedia, founded 2008", "≈ 8,072 articles after 18 years");
  row(2.75, "Sustained output since 2020", "≈ 350 new articles per year");
  row(3.35, "Community", "31 active editors/month · 2 administrators");
  row(3.95, "Dzongkha Education Program (closest Tibetic effort)", "dozens of participants · 5 months · ≈ 80 articles");
  s.addShape("roundRect", { x: 0.9, y: 4.75, w: 11.5, h: 1.0, rectRadius: 0.1, fill: { color: TINT }, line: { color: GOLD, width: 1 } });
  s.addText([
    { text: "[TO FILL — campaign records] ", options: { bold: true, color: RED } },
    { text: "workshops run, cohort sizes, retention curves — the first-person numbers that make this land.", options: { color: INK } },
  ], { x: 1.1, y: 4.9, w: 11.1, h: 0.7, fontFace: SANS, fontSize: 13.5 });
  s.addText("At ~350 articles/year, a 100,000-article encyclopedia is two centuries away. That is the measured capacity of manual-only.", {
    x: 0.9, y: 6.1, w: 11.5, h: 0.7, fontFace: SERIF, fontSize: 16.5, italic: true, color: MAROON });
  s.addNotes("The standing matters: this claim lands differently coming from the people who did the volunteer work. Never cut this slide (canonical trim order protects 3, 4, 13).");

  // ---- 4 · THE TRILEMMA --------------------------------------------------
  s = pres.addSlide();
  title(s, "The trilemma", "scale");
  const col = (x, head, lines, dark) => {
    s.addShape("roundRect", { x, y: 1.5, w: 3.95, h: 4.55, rectRadius: 0.12,
      fill: { color: dark ? MAROON : TINT }, line: { color: dark ? MAROON_DARK : TINT2, width: 1 } });
    s.addText(head, { x: x + 0.25, y: 1.75, w: 3.45, h: 0.85, fontFace: SERIF, fontSize: 19, bold: true,
      color: dark ? WHITE : MAROON });
    s.addText(lines.map((t, i) => ({ text: t, options: { bullet: { code: "2022" }, breakLine: i < lines.length - 1, paraSpaceAfter: 8 } })), {
      x: x + 0.25, y: 2.7, w: 3.45, h: 3.1, fontFace: SANS, fontSize: 13.5, color: dark ? TINT2 : INK });
  };
  col(0.55, "1 · Manual-only", ["We tried it; we measured it", "~350 articles/year, 31 editors", "Does not reach critical mass within a generation"]);
  col(4.69, "2 · Unsupervised automation", ["Scots: credibility destroyed", "Cebuano: 6M stubs, closure votes", "Greenlandic: closed by LangCom, 2025", "Poisons the training corpus downstream"]);
  col(8.83, "3 · Supervised automation", ["Machine drafts under hard verification", "Throughput bounded by review capacity", "A named human is the publisher", "This pipeline"], true);
  s.addText("“No demonstrated alternative reaches critical mass within a generation.”", {
    x: 0.9, y: 6.35, w: 11.5, h: 0.6, fontFace: SERIF, fontSize: 18, italic: true, color: INK, align: "center" });
  s.addNotes("Phrase in print as 'no demonstrated alternative…'; the punchy version is for the podium, backed by the slide-13 arithmetic. The ethics section later is the third horn, not an apology.");

  // ---- 5 · THE CYCLE -----------------------------------------------------
  s = pres.addSlide();
  title(s, "The cycle — the whole argument on one slide", "cycle");
  const nodes = [
    { t: "Cited Tibetan\narticles", x: 5.47, y: 1.45 },
    { t: "Digital\nfootprint", x: 9.2, y: 2.9 },
    { t: "Training data →\nTibetan-capable AI", x: 5.47, y: 4.5 },
    { t: "Visibility, tools,\nreaders, editors", x: 1.8, y: 2.9 },
  ];
  nodes.forEach(n => {
    s.addShape("roundRect", { x: n.x, y: n.y, w: 2.4, h: 1.1, rectRadius: 0.55, fill: { color: MAROON }, line: { color: MAROON_DARK } });
    s.addText(n.t, { x: n.x, y: n.y, w: 2.4, h: 1.1, fontFace: SANS, fontSize: 12.5, bold: true, color: WHITE, align: "center", valign: "middle", margin: 0 });
  });
  const arrow = (x1, y1, x2, y2) => s.addShape("line", { x: x1, y: y1, w: x2 - x1, h: y2 - y1, line: { color: GOLD, width: 2.5, endArrowType: "triangle" }, flipV: y2 < y1 ? true : false });
  // clockwise arrows (drawn as straight segments between node edges)
  s.addShape("line", { x: 7.95, y: 2.35, w: 1.45, h: 0.55, line: { color: GOLD, width: 2.5, endArrowType: "triangle" } });
  s.addShape("line", { x: 9.35, y: 4.0, w: -1.4, h: 0.7, line: { color: GOLD, width: 2.5, endArrowType: "triangle" } });
  s.addShape("line", { x: 5.4, y: 4.7, w: -1.4, h: -0.7, line: { color: GOLD, width: 2.5, endArrowType: "triangle" } });
  s.addShape("line", { x: 3.35, y: 2.9, w: 1.35, h: -0.55, line: { color: GOLD, width: 2.5, endArrowType: "triangle" } });
  s.addText("verification\nflips the sign", { x: 5.47, y: 2.85, w: 2.4, h: 1.35, fontFace: SERIF, fontSize: 15, bold: true, italic: true, color: MAROON, align: "center", valign: "middle" });
  s.addShape("roundRect", { x: 0.7, y: 6.0, w: 5.9, h: 0.95, rectRadius: 0.1, fill: { color: "F5E3E0" }, line: { color: RED, width: 1 } });
  s.addText("Unverified: MT junk → corpus rot → model collapse — the doom spiral (Greenlandic, 2025)", { x: 0.9, y: 6.1, w: 5.5, h: 0.75, fontFace: SANS, fontSize: 11.5, color: RED });
  s.addShape("roundRect", { x: 6.85, y: 6.0, w: 5.9, h: 0.95, rectRadius: 0.1, fill: { color: "E9EFE4" }, line: { color: "3F6B3F", width: 1 } });
  s.addText("Verified: CX-style human-gated content shows lower deletion rates than from-scratch articles", { x: 7.05, y: 6.1, w: 5.5, h: 0.75, fontFace: SANS, fontSize: 11.5, color: "2F5230" });
  s.addNotes("45 seconds. This is the argument; everything after is mechanism. Wikipedia is almost always the largest source in LLM training mixes; per-language capability tracks pretraining share; Welsh entered the loop deliberately as policy.");

  // ---- 6 · CASE STUDY ----------------------------------------------------
  s = pres.addSlide();
  title(s, "A text this room can check", "anchor");
  s.addText([
    { text: "སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ།", options: { fontFace: TIB, fontSize: 18, color: MAROON, breakLine: true } },
    { text: "\u201CPraise to Tara with Twenty-One Homages\u201D", options: { fontFace: SANS, fontSize: 12, italic: true, color: MUTED, breakLine: true } },
    { text: "Praise to the Twenty-One Tārās (Tōh. 438) + 16 commentaries · Drakpa Gyaltsen to 2023 · ~540,000 characters", options: { fontFace: SANS, fontSize: 13.5, color: INK } },
  ], { x: 0.6, y: 1.3, w: 7.3, h: 1.15 });
  // network: root center + 16 school-colored dots
  const cx = 3.6, cy = 4.35, R = 1.75;
  const schools = [
    ["Geluk", "7A1E2D", 7], ["Sakya", "C9A227", 1], ["Jonang", "3E5C76", 1],
    ["Nyingma", "8C5A2B", 1], ["Kagyü", "4A7A6F", 1], ["Sūryagupta lineage", "A3261F", 2], ["unattributed", "9A9A9A", 3],
  ];
  const dots = [];
  schools.forEach(([name, colr, n]) => { for (let i = 0; i < n; i++) dots.push(colr); });
  dots.forEach((colr, i) => {
    const a = (2 * Math.PI * i) / dots.length - Math.PI / 2;
    const x = cx + R * Math.cos(a), y = cy + R * Math.sin(a) * 0.82;
    s.addShape("line", { x: cx + 0.0, y: cy + 0.0, w: x - cx, h: y - cy, line: { color: "D9CDBB", width: 1 } });
  });
  dots.forEach((colr, i) => {
    const a = (2 * Math.PI * i) / dots.length - Math.PI / 2;
    const x = cx + R * Math.cos(a), y = cy + R * Math.sin(a) * 0.82;
    s.addShape("ellipse", { x: x - 0.14, y: y - 0.14, w: 0.28, h: 0.28, fill: { color: colr }, line: { color: WHITE, width: 1 } });
  });
  s.addShape("ellipse", { x: cx - 0.62, y: cy - 0.62, w: 1.24, h: 1.24, fill: { color: WHITE }, line: { color: MAROON, width: 2 } });
  s.addText("root\ntext", { x: cx - 0.62, y: cy - 0.62, w: 1.24, h: 1.24, fontFace: SERIF, fontSize: 13, bold: true, color: MAROON, align: "center", valign: "middle", margin: 0 });
  // legend
  let ly = 2.75;
  s.addText("16 commentaries by school", { x: 7.6, y: ly - 0.5, w: 5.1, h: 0.4, fontFace: SANS, fontSize: 13, bold: true, color: INK, margin: 0 });
  schools.forEach(([name, colr, n]) => {
    s.addShape("ellipse", { x: 7.65, y: ly + 0.05, w: 0.22, h: 0.22, fill: { color: colr }, line: { color: colr } });
    s.addText(`${name} — ${n}`, { x: 8.0, y: ly - 0.05, w: 4.6, h: 0.4, fontFace: SANS, fontSize: 12.5, color: INK, margin: 0 });
    ly += 0.42;
  });
  s.addText("Deliberately familiar: the room can judge output quality itself. School skew is data the pipeline must respect (slide 10).", {
    x: 7.6, y: ly + 0.15, w: 5.15, h: 1.0, fontFace: SANS, fontSize: 12, italic: true, color: MUTED, margin: 0 });
  s.addNotes("22 stanzas rebuilt with stable per-stanza IDs, cross-checked against an annotated edition. Ingest is deterministic: re-running reproduces every source file byte-for-byte — verified on a second machine this week.");

  // ---- 7 · PIPELINE OVERVIEW --------------------------------------------
  s = pres.addSlide();
  title(s, "The pipeline in one pass", "layers");
  const stagesInfo = [
    ["INGEST", "clean · segment · headings\nanchors · block IDs"],
    ["ARTICLES", "extract → claims → outline\n→ draft → audit → verify"],
    ["PUBLISH", "review gate · dry-run default\nsandbox first · disclosure"],
    ["MAINTAIN", "update path: insert-only\nconflicts flagged ⚑ for humans"],
  ];
  stagesInfo.forEach(([h, b], i) => {
    const x = 0.55 + i * 3.25;
    s.addShape("roundRect", { x, y: 1.55, w: 2.9, h: 1.7, rectRadius: 0.1, fill: { color: i === 1 ? MAROON : TINT }, line: { color: i === 1 ? MAROON_DARK : TINT2 } });
    s.addText(h, { x: x + 0.15, y: 1.66, w: 2.6, h: 0.42, fontFace: SANS, fontSize: 14.5, bold: true, color: i === 1 ? GOLD : MAROON, margin: 0 });
    s.addText(b, { x: x + 0.15, y: 2.1, w: 2.65, h: 1.1, fontFace: SANS, fontSize: 11.5, color: i === 1 ? WHITE : INK, margin: 0 });
    if (i < 3) s.addShape("line", { x: x + 2.92, y: 2.4, w: 0.31, h: 0, line: { color: GOLD, width: 2.5, endArrowType: "triangle" } });
  });
  s.addText("Two invariants — stated as invariants, not aspirations", { x: 0.55, y: 3.6, w: 12.2, h: 0.5, fontFace: SERIF, fontSize: 17, bold: true, color: RED });
  const inv = (y, n, txt) => {
    s.addShape("roundRect", { x: 0.55, y, w: 12.25, h: 1.05, rectRadius: 0.1, fill: { color: "F5E3E0" }, line: { color: RED, width: 1.25 } });
    s.addText([{ text: `Invariant ${n}.  `, options: { bold: true, color: RED } }, { text: txt, options: { color: INK } }],
      { x: 0.8, y: y + 0.12, w: 11.8, h: 0.8, fontFace: SANS, fontSize: 13.5, margin: 0 });
  };
  inv(4.2, 1, "No source wording ever reaches the drafting model. It cites claim indices; code expands them to passages and renders the references. Quotations enter articles only from the extraction record.");
  inv(5.45, 2, "Nothing publishes without the audit AND a deterministic, LLM-free verification gate. Added facts and attribution loss block regardless of any model's verdict. There is no bypass flag.");
  s.addText("17 steps · 4 layers · one skill per step · versioned prompts · 546 passing tests", { x: 0.55, y: 6.7, w: 12.2, h: 0.4, fontFace: SANS, fontSize: 11.5, color: MUTED });
  s.addNotes("Two minutes, one pass, no detail. The red boxes are the talk's spine: everything distinctive follows from these two constraints.");

  // ---- 8 · ALIGNMENT & IDs ----------------------------------------------
  s = pres.addSlide();
  title(s, "Verse alignment and stable IDs", "search");
  const arow = (y, k, v, bold) => {
    s.addText(k, { x: 0.9, y, w: 6.6, h: 0.45, fontFace: SANS, fontSize: 14, bold: !!bold, color: INK, margin: 0 });
    s.addText(v, { x: 7.7, y, w: 4.9, h: 0.45, fontFace: SANS, fontSize: 14, bold: true, color: MAROON, margin: 0 });
  };
  arow(1.55, "Aligned spans over the 23 root units", "314");
  arow(2.1, "…anchored by explicit verse transclusion in the commentary", "209");
  arow(2.65, "…by lexical clustering (precision-first)", "105");
  arow(3.2, "Commentaries at 100% coverage", "7 of 16");
  arow(3.75, "Lowest coverage — the condensed & interlinear genres, as predicted", "52%");
  s.addShape("roundRect", { x: 0.9, y: 4.55, w: 11.5, h: 1.9, rectRadius: 0.1, fill: { color: TINT }, line: { color: TINT2 } });
  s.addText("One ID, anatomized", { x: 1.15, y: 4.7, w: 11.0, h: 0.4, fontFace: SANS, fontSize: 13, bold: true, color: MAROON, margin: 0 });
  s.addText([
    { text: "TARAC03_GDD", options: { color: MAROON, bold: true } },
    { text: "  ·  ", options: { color: MUTED } },
    { text: "^1-9", options: { color: RED, bold: true } },
    { text: "   →   Gendün Drub's ṭīkkā, its block on stanza 9 — the same ID is the citation's locator and, for public-domain texts, a Wikisource verse anchor.", options: { color: INK } },
  ], { x: 1.15, y: 5.15, w: 11.0, h: 1.1, fontFace: "Courier New", fontSize: 14, margin: 0 });
  s.addText("Alignment decides what the extractor is shown; anchors make every citation traceable to the verse being explained.", {
    x: 0.9, y: 6.6, w: 11.5, h: 0.5, fontFace: SANS, fontSize: 12, italic: true, color: MUTED });
  s.addNotes("Second slide in the trim order if squeezed. The reading-view invariant: every added scaffold layer strips back to a byte-identical text, so verification can never fail on the pipeline's own marginalia.");

  // ---- 9 · ATOMIC CLAIMS -------------------------------------------------
  s = pres.addSlide();
  title(s, "Atomic claims — the firewall", "table");
  s.addText("One real row (སྒྲོལ་མ, claim 0):", { x: 0.6, y: 1.32, w: 11, h: 0.4, fontFace: SANS, fontSize: 13.5, bold: true, color: INK, margin: 0 });
  s.addShape("roundRect", { x: 0.6, y: 1.75, w: 12.15, h: 2.35, rectRadius: 0.1, fill: { color: TINT }, line: { color: GOLD, width: 1 } });
  s.addText("མཁས་པ་མི་འདྲ་བ་གསུམ་གྱིས་མིང་སྒྲོལ་མའི་སྒྲ་བཤད་མཚུངས་པའི་དོན་དུ་བྱས་ཏེ། སྡུག་བསྔལ་གྱི་རྒྱ་མཚོ་ལས་སྒྲོལ་བ་འམ། སེམས་ཅན་སངས་རྒྱས་ཀྱི་ས་ལས་སྒྲོལ་བར་མཛད་པ་འམ། འཁོར་བའི་སྡུག་བསྔལ་ལས་སྐྱོབ་པ་ཞེས་བཤད་དེ། མིང་གི་དོན་ལ་མཐུན་པའོ།", {
    x: 0.85, y: 1.88, w: 11.6, h: 0.85, fontFace: TIB, fontSize: 12, color: INK });
  s.addText("\u201CThree different scholars gloss the name Tara alike: she who delivers from the ocean of suffering, brings beings to the level of buddhahood, or protects from samsara's suffering — the name's meaning is agreed.\u201D", {
    x: 0.85, y: 2.72, w: 11.6, h: 0.62, fontFace: SANS, fontSize: 10.5, italic: true, color: MUTED });
  s.addText([
    { text: "type: ", options: { color: MUTED } }, { text: "consensus", options: { bold: true, color: MAROON } },
    { text: "   passages: ", options: { color: MUTED } }, { text: "[0, 1, 9] — Sakya · Geluk · Geluk, block-located", options: { bold: true, color: INK } },
    { text: "   reception: ", options: { color: MUTED } }, { text: "uncontested", options: { bold: true, color: INK } },
  ], { x: 0.85, y: 3.42, w: 11.6, h: 0.5, fontFace: "Courier New", fontSize: 12.5, margin: 0 });
  s.addText("“The draft is written from this — with the sources closed.”", {
    x: 0.6, y: 4.5, w: 12.15, h: 0.5, fontFace: SERIF, fontSize: 17, italic: true, color: MAROON, align: "center" });
  const cstat = (x, big, lab) => {
    s.addText(big, { x, y: 5.25, w: 2.9, h: 0.8, fontFace: SERIF, fontSize: 34, bold: true, color: MAROON, align: "center" });
    s.addText(lab, { x, y: 6.05, w: 2.9, h: 0.75, fontFace: SANS, fontSize: 11.5, color: MUTED, align: "center" });
  };
  cstat(0.7, "81 → 47", "verbatim passages compressed to atomic claims (3 articles)");
  cstat(3.75, "13 / 13 / 21", "consensus / school-position / single-commentator");
  cstat(6.8, "0", "majority-with-dissent — praise commentary isn't polemical (slide 10)");
  cstat(9.85, "100%", "claims carry passage indices, school, and reception tags");
  s.addNotes("Two minutes. The claim type triggers voice rules: consensus speaks plainly; a school position names its school; a single commentator is attributed. All types are corpus-relative — consensus means these sixteen commentaries agree, not the tradition at large. Facts aren't copyrightable — this is also the licensing posture: cite, don't copy (it narrows copyright risk; the review still checks quote length and paraphrase).");

  // ---- 10 · WEIGHTING ----------------------------------------------------
  s = pres.addSlide();
  title(s, "Breadth decides existence; reception decides weight", "scale");
  s.addText([
    { text: "Tibetan polemical culture left a machine-readable due-weight record: ", options: { color: INK } },
    { text: "commentaries cite, endorse, and refute one another (dgag lan).", options: { bold: true, color: MAROON } },
  ], { x: 0.6, y: 1.4, w: 12.1, h: 0.6, fontFace: SANS, fontSize: 15.5 });
  const wcard = (x, head, body, tint) => {
    s.addShape("roundRect", { x, y: 2.2, w: 5.95, h: 2.4, rectRadius: 0.12, fill: { color: tint }, line: { color: TINT2 } });
    s.addText(head, { x: x + 0.25, y: 2.4, w: 5.45, h: 0.5, fontFace: SERIF, fontSize: 16, bold: true, color: MAROON, margin: 0 });
    s.addText(body, { x: x + 0.25, y: 2.95, w: 5.45, h: 1.5, fontFace: SANS, fontSize: 13, color: INK, margin: 0 });
  };
  wcard(0.6, "A position that drew rebuttals", "…has proven historical weight even without breadth — it gets a named, weighted treatment. Refutation is engagement.", TINT);
  wcard(6.8, "An unengaged idiosyncrasy", "…gets a sentence. And a school's sole corpus representative is a school-position, never “fringe” — sole representation is a fact about the corpus, not the tradition.", TINT);
  s.addShape("roundRect", { x: 0.6, y: 4.95, w: 12.15, h: 1.55, rectRadius: 0.1, fill: { color: "EFEAE2" }, line: { color: GOLD, width: 1 } });
  s.addText([
    { text: "Honest limit of this case study: ", options: { bold: true, color: RED } },
    { text: "0 of 47 claims drew dissent — praise commentary explains, it doesn't refute. The contested demonstration comes from the Bodhicaryāvatāra corpus already aligned behind this pipeline (10 commentaries, 7,279 spans — the Mipham exchanges).", options: { color: INK } },
  ], { x: 0.85, y: 5.12, w: 11.6, h: 1.25, fontFace: SANS, fontSize: 13.5 });
  s.addText("Traditional Tibetan intellectual history, operationalized as editorial policy.", {
    x: 0.6, y: 6.7, w: 12.1, h: 0.45, fontFace: SERIF, fontSize: 15, italic: true, color: MAROON, align: "center" });
  s.addNotes("The slide for this room. Frame: the pipeline reads the tradition's own reception record — citation and refutation patterns — as due-weight policy, the way Wikipedia reads secondary literature.");

  // ---- 11 · TWO MODELS, ONE LOOP ----------------------------------------
  s = pres.addSlide();
  title(s, "The auditor never writes — and it matters, measurably", "robot");
  const mcard = (x, head, lines, dark) => {
    s.addShape("roundRect", { x, y: 1.5, w: 5.95, h: 2.15, rectRadius: 0.12, fill: { color: dark ? MAROON : TINT }, line: { color: dark ? MAROON_DARK : TINT2 } });
    s.addText(head, { x: x + 0.25, y: 1.66, w: 5.45, h: 0.5, fontFace: SERIF, fontSize: 15.5, bold: true, color: dark ? GOLD : MAROON, margin: 0 });
    s.addText(lines, { x: x + 0.25, y: 2.2, w: 5.45, h: 1.35, fontFace: SANS, fontSize: 13, color: dark ? WHITE : INK, margin: 0 });
  };
  mcard(0.6, "Same-model audit (writer judges its own prose)", "“publish, no findings” — three articles out of three.\nEvery real defect sailed through.");
  mcard(6.8, "Cross-model audit (independent model)", "5 blocking findings on 2 articles.\nHand-adjudication against the claims table: 4 genuine, 1 borderline.", true);
  s.addText("One real catch, from the run:", { x: 0.6, y: 3.95, w: 12, h: 0.4, fontFace: SANS, fontSize: 13, bold: true, color: INK, margin: 0 });
  s.addShape("roundRect", { x: 0.6, y: 4.35, w: 12.15, h: 1.5, rectRadius: 0.1, fill: { color: "F5E3E0" }, line: { color: RED, width: 1.25 } });
  s.addText([
    { text: "⛔ dropped-qualifier  ", options: { bold: true, color: RED } },
    { text: "draft lead: ", options: { color: MUTED } },
    { text: "མཁས་པ་མི་འདྲ་བ་མང་པོས་ ", options: { fontFace: TIB, color: RED, bold: true } },
    { text: "(“many scholars agree”) — claim 0: ", options: { color: MUTED } },
    { text: "མཁས་པ་མི་འདྲ་བ་གསུམ་གྱིས་ ", options: { fontFace: TIB, color: "2F5230", bold: true } },
    { text: "(“three”). A consensus exaggeration: caught, fixed, re-audited to zero findings.", options: { color: INK } },
  ], { x: 0.85, y: 4.55, w: 11.6, h: 1.15, fontFace: SANS, fontSize: 13.5 });
  s.addText("Beneath both: the deterministic gate — every quotation re-read character-for-character from its source. It once caught a single tsheg silently promoted to a shad (similarity 0.974). No model, no bypass.", {
    x: 0.6, y: 6.1, w: 12.15, h: 0.85, fontFace: SANS, fontSize: 13, italic: true, color: INK });
  s.addNotes("The layers catch disjoint failure classes: audit reads meaning (paraphrase drift, weight inflation); the gate reads characters (quotation integrity). The auditor also twice misquoted the draft in its own findings — model text is untrusted everywhere, which is why the blocking decision keys on categories and the gate is LLM-free.");

  // ---- 12 · DEMO ---------------------------------------------------------
  s = pres.addSlide();
  title(s, "Demo — pre-recorded, offline-first", "play");
  s.addShape("roundRect", { x: 0.9, y: 1.5, w: 7.4, h: 4.4, rectRadius: 0.12, fill: { color: MAROON_DARK }, line: { color: MAROON } });
  s.addImage({ data: iconsGold.play, x: 3.9, y: 3.0, w: 1.3, h: 1.3 });
  s.addText("[ 90-second screen capture — slot ]", { x: 0.9, y: 4.55, w: 7.4, h: 0.5, fontFace: SANS, fontSize: 13, color: TINT2, align: "center" });
  const step = (y, n, t) => {
    s.addShape("ellipse", { x: 8.75, y, w: 0.4, h: 0.4, fill: { color: GOLD }, line: { color: GOLD } });
    s.addText(String(n), { x: 8.75, y: y - 0.008, w: 0.4, h: 0.4, fontFace: SANS, fontSize: 13, bold: true, color: MAROON_DARK, align: "center", valign: "middle", margin: 0 });
    s.addText(t, { x: 9.3, y: y - 0.05, w: 3.4, h: 0.55, fontFace: SANS, fontSize: 13, color: INK, margin: 0 });
  };
  step(1.7, 1, "a term, from the aligned corpus");
  step(2.35, 2, "its claims table forms");
  step(3.0, 3, "draft cites claim indices");
  step(3.65, 4, "audit + character gate");
  step(4.3, 5, "the article, every ref block-located");
  step(4.95, 6, "an answer-engine finds it — in Tibetan");
  s.addText("Never live: venue wifi unconfirmed; every intermediate file local; PDF sequence as video fallback. End on the live URL + QR.", {
    x: 0.9, y: 6.25, w: 11.8, h: 0.7, fontFace: SANS, fontSize: 12, italic: true, color: MUTED });
  s.addNotes("2:30. The recording exists before travel; cached at three redundancies (USB, cloud, email). If video fails, the PDF slide sequence of the same frames.");

  // ---- 13 · EARLY RESULTS ------------------------------------------------
  s = pres.addSlide();
  title(s, "Early results — and the number that carries the claim", "chart");
  const rows = [
    [{ text: "What ran", options: { bold: true, color: WHITE, fill: { color: MAROON } } }, { text: "Result", options: { bold: true, color: WHITE, fill: { color: MAROON } } }],
    ["3 articles, full chain (claims → draft → audit → verify)", "all three ledger-verified"],
    ["Quotations re-read from source, character-for-character", "81 / 81 exact — reproduced byte-identically on a 2nd machine"],
    ["Block locators (citation → commentary block)", "81 / 81 resolve, none wrong"],
    ["Cross-model audit findings on first drafts", "5 blocking → 6 logged edits → 0 findings, re-verified"],
    ["Wall-clock per article (machine side)", "≈ 10–20 min · ≈ $0.33–1.42 at current Flash prices"],
    ["Audit stability, final articles (3 runs each)", "pass rates 0.67 / 0.67 / 1.0 — rates, not verdicts"],
    ["Reviewer-hours per audit-passed article", "[TO FILL — August evaluation batch]"],
  ];
  s.addTable(rows.map(r => r.map(c => typeof c === "string" ? { text: c, options: { color: INK } } : c)), {
    x: 0.6, y: 1.45, w: 12.15, colW: [7.3, 4.85], fontFace: SANS, fontSize: 12,
    border: { type: "solid", color: "D9CDBB", pt: 0.75 }, fill: { color: WHITE },
    rowH: 0.43, valign: "middle", margin: 0.05,
  });
  s.addText([
    { text: "The honest failure: ", options: { bold: true, color: RED } },
    { text: "the drafts were not clean — the same-model audit called them perfect, the independent audit did not, and every finding is in the paper. The safeguards are the result.", options: { color: INK } },
  ], { x: 0.6, y: 5.6, w: 12.15, h: 0.75, fontFace: SANS, fontSize: 13 });
  s.addText("Reviewer-hours vs ~350 articles/year manual: the “generations collapse to years” arithmetic — completed when the review logs land.", {
    x: 0.6, y: 6.5, w: 12.15, h: 0.6, fontFace: SERIF, fontSize: 14.5, italic: true, color: MAROON });
  s.addNotes("Never cut this slide. Single run, reported as such; pass rates over repeated runs are the evaluation-batch metric. WikiCrow anchors for context: 86.1% rater-judged citation precision vs 71.2% human baseline — ours is a stricter, byte-level property.");

  // ---- 14 · ETHICS & LIMITS ---------------------------------------------
  s = pres.addSlide();
  title(s, "Ethics and limits — the hardest question, pre-empted", "shield");
  s.addText("Small-wiki AI content has a body count: Greenlandic closed (2025) · Inuktitut ⅔ MT-contaminated · African wikis 40–60% uncorrected MT.", {
    x: 0.6, y: 1.4, w: 12.1, h: 0.6, fontFace: SANS, fontSize: 14, color: RED });
  const gcard = (x, iconKey, head, body) => {
    s.addShape("roundRect", { x, y: 2.25, w: 3.95, h: 2.3, rectRadius: 0.12, fill: { color: TINT }, line: { color: TINT2 } });
    s.addShape("ellipse", { x: x + 0.25, y: 2.5, w: 0.55, h: 0.55, fill: { color: MAROON }, line: { color: MAROON } });
    s.addImage({ data: icons[iconKey], x: x + 0.38, y: 2.63, w: 0.29, h: 0.29 });
    s.addText(head, { x: x + 0.95, y: 2.5, w: 2.85, h: 0.55, fontFace: SANS, fontSize: 14.5, bold: true, color: MAROON, valign: "middle", margin: 0 });
    s.addText(body, { x: x + 0.25, y: 3.2, w: 3.45, h: 1.25, fontFace: SANS, fontSize: 12, color: INK, margin: 0 });
  };
  gcard(0.55, "flag", "Disclosure", "On-wiki edit summaries + project page; machine-drafted, human-published — the Content Translation model, adopted voluntarily.");
  gcard(4.69, "users", "Pacing", "Throughput bounded by review capacity, not model capacity. No mass creation. A named human is the sole publishing agent.");
  gcard(8.83, "check", "Verification", "Cross-model audit blocks added facts & attribution loss; the character gate has no bypass; every sentence traces to block-located passages.");
  s.addText([
    { text: "Limits, stated: ", options: { bold: true, color: MAROON } },
    { text: "corpus school-skew (7/16 Geluk); articles still short of the 1,500-syllable bar; citations await public URLs (BDRC/Wikisource) before any mainspace publish; three articles is a case study, not a distribution; drafting and auditing Tibetan still rides on models trained mostly on other languages — the §1 gap felt from inside.", options: { color: INK } },
  ], { x: 0.6, y: 5.0, w: 12.15, h: 1.5, fontFace: SANS, fontSize: 13 });
  s.addNotes("One minute. The residual risk stays named: a fluent reviewer can still wave through a subtly wrong article. The pipeline shrinks what a reviewer must distrust; it does not abolish editorial responsibility — and is not meant to.");

  // ---- 15 · SCALING ------------------------------------------------------
  s = pres.addSlide();
  title(s, "What scale looks like", "expand");
  const scard = (x, big, lab) => {
    s.addShape("roundRect", { x, y: 1.6, w: 3.95, h: 2.5, rectRadius: 0.12, fill: { color: TINT }, line: { color: TINT2 } });
    s.addText(big, { x, y: 1.85, w: 3.95, h: 1.0, fontFace: SERIF, fontSize: 30, bold: true, color: MAROON, align: "center" });
    s.addText(lab, { x: x + 0.25, y: 2.9, w: 3.45, h: 1.1, fontFace: SANS, fontSize: 12, color: INK, align: "center" });
  };
  scard(0.55, "7,279 spans", "Bodhicaryāvatāra already aligned: 10 commentaries, 545 terms — 520 of them existing articles → the insert-only update path");
  scard(4.69, "1 skill / step", "the pipeline improves with every article: prompt patches are versioned, never in-place; every output traces to the prompt that made it");
  scard(8.83, "claims DB", "typed, school-tagged, reception-tagged, block-located rows over a verse-aligned corpus — a research object independent of Wikipedia");
  s.addText("The architecture is not Tārā-specific: root text + commentaries + registry. Sanskrit, Pali, and classical Chinese scholasticism have the same shape.", {
    x: 0.6, y: 4.55, w: 12.15, h: 0.7, fontFace: SANS, fontSize: 14, color: INK, align: "center" });
  s.addText("For Class-0/1 languages generally: machine volume, human authority, verification as the hinge.", {
    x: 0.6, y: 5.5, w: 12.15, h: 0.6, fontFace: SERIF, fontSize: 16, italic: true, color: MAROON, align: "center" });
  s.addNotes("45 seconds. Hundreds of texts queued behind the same contract. The durable asset is the claims database, not the article count.");

  // ---- 16 · TAKEAWAY -----------------------------------------------------
  s = pres.addSlide();
  s.background = { color: MAROON_DARK };
  s.addText("The loop is running either way.", { x: 0.8, y: 0.9, w: W - 1.6, h: 0.8, fontFace: SERIF, fontSize: 32, bold: true, color: WHITE, align: "center" });
  s.addText("Unverified, it is the doom spiral. Verified — with a human hand on the gate — it is how a language re-enters the digital world.", {
    x: 1.4, y: 1.8, w: W - 2.8, h: 0.8, fontFace: SERIF, fontSize: 17, italic: true, color: TINT2, align: "center" });
  const tk = (x, t) => {
    s.addShape("roundRect", { x, y: 3.0, w: 3.75, h: 1.7, rectRadius: 0.12, fill: { color: MAROON }, line: { color: GOLD, width: 1 } });
    s.addText(t, { x: x + 0.2, y: 3.15, w: 3.35, h: 1.4, fontFace: SANS, fontSize: 13.5, color: WHITE, align: "center", valign: "middle", margin: 0 });
  };
  tk(0.75, "Machine-drafted,\nhuman-published — with 81/81 quotations character-verified");
  tk(4.79, "The by-product is a research corpus: claims, citations, alignments — citable datasets for Tibetan studies");
  tk(8.83, "Reusable for any commentarial tradition — and any small language with a layered canon");
  s.addText("paper · code · demo article — QR here", { x: 0.8, y: 5.3, w: W - 1.6, h: 0.5, fontFace: SANS, fontSize: 13, color: GOLD, align: "center" });
  s.addShape("roundRect", { x: W / 2 - 0.85, y: 5.9, w: 1.7, h: 1.0, rectRadius: 0.08, fill: { color: WHITE }, line: { color: GOLD } });
  s.addText("[QR]", { x: W / 2 - 0.85, y: 5.9, w: 1.7, h: 1.0, fontFace: SANS, fontSize: 13, color: MUTED, align: "center", valign: "middle" });
  s.addText("Tashi Tsering · OpenPecha · tashitsering@dharmaduta.in", { x: 0.8, y: 7.0, w: W - 1.6, h: 0.4, fontFace: SANS, fontSize: 11, color: TINT2, align: "center" });
  s.addNotes("30 seconds. The cycle diagram in words; end on the QR to the demo article, code, and paper.");

  await pres.writeFile({ fileName: require("path").join(__dirname, "IATS-2026-slides.pptx") });
  console.log("deck written");
})();
