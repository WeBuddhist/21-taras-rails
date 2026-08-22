# Canva build brief — "Verification with a human hand on the gate"

**What this file is.** A self-contained build spec for the 26-slide deck (+5 backup slides).
Hand this single file to the builder (Claude Desktop → Canva). Everything needed is inside:
design system, per-slide text, chart data, and placeholder instructions. The builder should
not need — and must not invent — anything beyond it.

**What this file is not.** It contains no speaker guidance. Delivery notes and speaker notes
live in `02-speaker-notes.md` and stay off the slides entirely.

---

## A. Instructions to the builder — read first

1. **Build all 31 slides** (26 main + 5 backup). Slides marked `[CUT-CANDIDATE]` are still
   built — the cut decision happens at rehearsal, not at build time.
2. **On-slide text is verbatim.** Use exactly the text in each slide's **TEXT** block — do not
   paraphrase, expand, or "improve" it. If a slide's TEXT block is short, that is deliberate.
   Design rule for the whole deck: **≤ 12 words of body text per slide** (big display numbers
   and chart data labels are exempt).
3. **Never type Tibetan script into a text box.** Every piece of Tibetan appears only as an
   image. Wherever Tibetan is needed, insert a **placeholder frame** (see rule 4) — the
   author will drop in pre-made screenshots. The Tibetan strings themselves are in Appendix C
   for the author's use only.
4. **Placeholder frames.** For every `[IMG-nn]` marker: insert a light-grey rectangle
   (#E5E0D8, 1 px #B8B2A8 border, slightly rounded corners) at the stated position, containing
   only the marker ID and its one-line label in small muted text (e.g. `IMG-07 — sa-bcad tree,
   37 nodes`). Do not fill placeholders with stock photos, AI images, or clip-art.
5. **`[LIVE-n]` numbers** are values that will be re-checked the morning of the talk. Build
   them with the number given, but style them normally — no visual marker on the slide. The
   author's checklist is Appendix B.
6. **Charts are built as native Canva elements** (or clean flat graphics), from the data
   tables given per slide. Chart style: flat, 2-D, no gridlines, no legends where colour
   already says it, data labels printed directly at the end of each bar/column. Every
   non-Tibetan data series is muted grey **#B8B2A8**; the Tibetan / pipeline datum is always
   the accent **#B03A1E**. Threshold lines are dashed, ink-coloured, labelled.
7. **No copyrighted film stills** (relevant to slide 9 — build the stylised cascade, not a
   Matrix frame). No watermarked stock. No decorative "oriental" fonts anywhere.
8. **Emoji** appear only where the TEXT block includes them (slide 6). Nowhere else.
9. If Canva supports a notes field, leave it empty — speaker notes are managed outside Canva.

---

## B. Design system

| Token | Value | Use |
|---|---|---|
| Canvas | 1920 × 1080 (16:9) | all slides |
| Background — light | `#FAF6F0` warm off-white | default, all content slides |
| Background — dark | `#201812` near-black brown | slides 1, 25 (closing line), 26 only |
| Ink | `#1A1A1A` | headlines, body |
| Muted | `#8A8378` | secondary text, captions, placeholder labels |
| Accent | `#B03A1E` deep maroon-red | the Tibetan/pipeline datum, key words, the ⚑ flag, big numbers |
| Support | `#D9A441` muted gold | sparingly: rules/dividers, the "verification" word on slide 5 |
| Grey data | `#B8B2A8` | all comparison bars/columns |
| Fail red | `#B03A1E` | reuse accent for FAIL states — do not add a second red |

**Type.** Headings + display numbers: **Archivo** (or Inter/Montserrat if unavailable), bold,
tight. Body/captions: **Inter** regular. Code/ID strings (`^1-3`, `SKILL.md`, file trees):
**JetBrains Mono** or any clean monospace. Display numbers may run 200–400 pt. Body never
below 24 pt.

**Layout defaults.** Generous margins (min 96 px). One idea per slide. Headline top-left or
centred; captions bottom. Act divider treatment: none — acts are invisible to the audience.

---

## C. The slides

### Slide 1 — Title  *(dark background)*

- **TEXT (centred, on top of image):**
  - Headline: `Expanding the Digital Footprint of Tibetan`
  - Subtitle: `A semi-automatic pipeline for Wikipedia article generation`
  - Byline: `Tashi Tsering · OpenPecha`
- **VISUAL:** full-bleed `[IMG-01 — darkened photograph of a Tibetan pecha]`, dark overlay
  ~60% so the text carries.

### Slide 2 — The gap, in one number

- **TEXT (two stacked display numbers, enormous, nothing else on the slide):**
  - `7,000,000 speakers` (ink)
  - `8,073 articles` (accent) `[LIVE-1]`
- **VISUAL:** typography only. No chart, no image, no logo.

### Slide 3 — Who does more with less  `[CUT-CANDIDATE — 3rd]`

- **TEXT:** headline `Welsh: 91,000 → 280,000+` · caption `government policy, 2017`
- **CHART — grouped horizontal bars, speakers vs articles, per language:**

  | Language | Speakers | Articles |
  |---|---|---|
  | Welsh | 850,000 | 280,000 |
  | Basque | 750,000 | `[LIVE-2]` |
  | Estonian | 1,100,000 | `[LIVE-2]` |
  | Tibetan | 7,000,000 | 8,073 `[LIVE-1]` |

  All bars grey; Tibetan pair in accent. `[LIVE-2]`/`[LIVE-3]` values are provisional —
  build with round placeholders (e.g. `~400,000`) sized so Tibetan's article bar is visibly,
  almost absurdly, the shortest. The visual argument: article count has no relationship to
  speaker count.

### Slide 4 — The models can't read us

- **TEXT:** headline `Below the coin-toss line.` · small footer note:
  `Tibetan ≈ 4× the tokens of Chinese per unit of text (Petrov et al. 2023)`
- **CHART — columns with a dashed threshold line at 25% labelled `random guessing`:**

  | Column | Value | Colour |
  |---|---|---|
  | Qwen-2.5-72B — Chinese | 84.7% | grey |
  | GPT-4 — Tibetan | 17.5% | accent |
  | Qwen-2.5-72B — Tibetan | 16.5% | accent |

  Both accent columns sit *below* the dashed line — that gap is the whole graphic.

### Slide 5 — The loop has a sign

- **TEXT:** between the two rings, one word in support-gold caps: `VERIFICATION`
- **VISUAL — one diagram, two circular arrow loops side by side (build as native shapes):**
  - Left loop, grey, arrows spiralling **inward**, four labels around it:
    `no articles → little training text → tools can't serve the language → fewer people write`
  - Right loop, accent, arrows flowing **outward**, four labels:
    `cited articles → digital footprint → better tools → faster articles`
- Caption (muted, bottom): `Same loop. Only the sign differs.`

### Slide 6 — Three options

- **TEXT — three vertical panels:**
  - Panel 1: `✋ By hand` — `too slow`
  - Panel 2: `🤖 Unsupervised` — `Scots · Cebuano · Greenlandic (closed, 2025)`
  - Panel 3: `✅ Supervised` — `this talk` (panel gets a thin accent border)
- **VISUAL:** panel 2 contains `[IMG-02 — screenshot: Greenlandic Wikipedia closure notice
  (or Scots controversy headline)]`.
- Small footer: `Content Translation — machine draft + mandatory human edit — shows lower
  deletion rates across 2.4M+ creations.`

### Slide 7 — The arithmetic of "by hand"  `[CUT-CANDIDATE — 2nd]`

- **TEXT:** headline `100,000 articles, at the observed rate:`
- **CHART — one horizontal bar that physically runs off the right edge of the slide,**
  labelled `~285 years` (grey). Below it, a short accent bar labelled
  `24–48 person-years — this pipeline, review-bound`. A small third row, text only:
  `Dzongkha program (manual, funded): 80 articles in 5 months`.
- Running off the slide is the point — do not shrink the long bar to fit.

### Slide 8 — Agent and harness

- **TEXT:**
  - `The model is the apprentice.`
  - `The harness is the workshop.`
- **VISUAL:** left two-thirds: `[IMG-03 — line illustration: workbench + racked tools +
  rulebook pinned above + in-tray/out-tray, labelled "the harness"; a figure at the bench
  labelled "the agent"]`. (Placeholder — the author supplies the drawing.)
- Right third, small monospace stack diagram (typed text, this is not Tibetan):

  ```
  model          judgement
    ├ tools      read · write · run · search
    ├ context    what it may see, per call
    └ rules      what it must do, per task
  ```

### Slide 9 — Skills: loaded, not known

- **TEXT:**
  - Display: `62 skills · 11,251 lines of written-down method`
  - Headline: `The model doesn't know the procedure. It loads it.`
- **VISUAL:** left — stylised green digital-rain cascade (build with shapes/text effects —
  **no film still**) resolving into a single white document icon labelled `SKILL.md`
  (monospace). Right — `[IMG-04 — screenshot: the vault's 4-SYSTEM/Skills/ folder listing]`.

### Slide 10 — Anatomy of a skill

- **TEXT:** display line at foot: `62 skills · 21 carry scripts · 44 scripts total`
- **VISUAL:** centre — `[IMG-05 — screenshot: tree-guided-claims/SKILL.md collapsed to its
  section headings]` with five small callout labels placed alongside, monospace, muted:
  - `the reasoning, and the failure it answers`
  - `the contract`
  - `rules 1…16 — each traceable to a real defect`
  - `the procedure`
  - `the deterministic backstop (scripts/verify_*.py)`
- Caption: `A skill is a text file. A scholar can read it, disagree, and edit it.`

### Slide 11 — Why the rules exist  *(protect — do not thin this slide)*

- **TEXT:** headline `Every rule is a scar.`
- **VISUAL — two-column table, three rows (typed text, keep it airy):**

  | The rule | The scar |
  |---|---|
  | `claim_count` is computed by counting — never inherited. | 114 of 118 strings byte-identical to the earlier "independent" run. |
  | Corroboration is re-read, not remembered. | Right idea, wrong claim ID — the audit's one critical finding. |
  | Counts are computed, never hand-tallied. | 5 of 5 "(N commentaries)" labels wrong on the worst pilot page. |

- Footer, small, three principles separated by `·`:
  `the model judges, the script verifies · isolation over context · nothing interpretive
  touches the source layer`

### Slide 12 — Scripts: the machine

- **TEXT:**
  - `The model judges. The script verifies.`
  - `The script has the final say.`
- **VISUAL:** top half — simple flat diagram: hopper → boxed mechanism (gears + a bolted
  rule-plate) → chute; caption under it `same input → same output, every time` (build with
  shapes; no placeholder needed).
- **Bottom strip — two-column table:**

  | Judgement (model) | Machine (script) |
  |---|---|
  | Structural announcement, or prose? | Does the string appear character-for-character? |
  | Does this gloss say *blue* or *clear-hued*? | Do the claim counts recompute? |
  | Which commentaries actually disagree? | Exactly one disposition per claim? |

- Footer, small: `No bypass flag exists. We deliberately did not build an override.`

### Slide 12b — The context-size finding  `[CUT-CANDIDATE — 4th]`

- **TEXT:** headline `The model budgets its answer against the size of the question.`
- **CHART — two paired column groups (same model, same prompt):**

  | Context given | Passages returned | Characters returned |
  |---|---|---|
  | 93,000 chars | 10 | 873 |
  | 12,000 chars | 20 | 5,224 |

  Grey for the 93k pair, accent for the 12k pair.
- Footer, small: `Pilot capture rates before the fix: 45% · 19% · 1.1%. The fix is
  architectural — one isolated call per outline node.`

### Slide 13 — The corpus, and the thread

- **TEXT — left column, stacked display figures:**
  - `16 commentaries`
  - `582,332 Tibetan characters`
  - `3,268 citable blocks`
  - `580 outline nodes`
  - `2,975 claims`
  - Small line beneath: `Sakya · Geluk · Jonang · Nyingma · Kagyü · Sūryagupta`
- **VISUAL — right column:** `[IMG-06 — root verse 3 in large Uchen, block ID ^1-3 visible]`
- Caption, bottom: `One verse, one commentary, all the way to a finished article.`

### Slide 14 — Getting the text in

- **TEXT:** headline strip under the panels: `scan → OCR → clean → address` (monospace,
  arrows in support-gold)
- **VISUAL — four equal panels, left to right:**
  - `[IMG-07a — BDRC scan page]`
  - `[IMG-07b — raw OCR output, visibly messy]`
  - `[IMG-07c — cleaned text]`
  - `[IMG-07d — block-addressed text with ^0-23 … ^0-27 visible]`
- Caption, small: `A footnote pointing at a file is a promise. Pointing at a block is an
  address.`

### Slide 15 — The author's own outline (sa-bcad)

- **TEXT:**
  - Display: `37 nodes · 7 levels`
  - Line: `The 21 leaves under "extended explanation" come out at exactly 21.`
- **VISUAL:** `[IMG-08 — Gendün Drub's full tree, one branch highlighted down to
  2.2.2.2.1.1.2]` — the highlight in accent.
- Caption: `Recovered, not imposed.`

### Slide 16 — Claims: index cards, not paraphrase

- **TEXT:**
  - Display: `2,975 claims · one fact · one type · one address`
  - Type chips (small rounded rectangles, grey with ink text, monospace):
    `etymology` `word-gloss` `iconography` `identification` `doctrinal` `structural`
- **VISUAL:** five overlapping index cards; front two full-size:
  `[IMG-09a — claim card: verbatim Tibetan + gloss + Type + Cite → ^0-26]`,
  `[IMG-09b — second claim card]`; three behind as blank card shapes.
- Footer, small: `One call per node. It cannot file under the wrong node, and cannot import
  from a commentary it was never shown.`

### Slide 17 — Sixteen commentaries are not sixteen of the same thing  `[CUT-CANDIDATE — 1st]`

- **TEXT:** headline `8× spread` · callout box (accent border):
  `outline nodes per commentary: 2 → 120`
- **CHART — horizontal bars, claims per 10,000 characters, sorted descending, all grey with
  the top and bottom bars in accent:**

  | Commentary | claims / 10k chars |
  |---|---|
  | karma-maitri | 181 |
  | taranatha | 116 |
  | drakpa-gyaltsen | 111 |
  | lobsang-dawa | 87 |
  | dharmabhadra | 81 |
  | gendun-drub | 65 |
  | sungrab-tulku | 59 |
  | gendun-gyatso | 56 |
  | pema-namgyal | 56 |
  | konchok-thabkhe | 54 |
  | yama-sonam | 54 |
  | tenga-tulku | 54 |
  | sangye-nyentrul | 51 |
  | tenzin-dhonzang | 46 |
  | palden-sherab | 34 |
  | tsultrim-namdak | 23 |

- Caption: `A word-commentary is dense. An expansive exegesis with ritual appendices is not.`

### Slide 18 — The spine map

- **TEXT:** headline `Every commentary numbered its own way. One shared coordinate system.`
- **VISUAL (build with shapes):** left — three small, visibly *different* abstract outline
  trees (grey). Right — one tall column of 24 numbered slots (accent outlines), labelled
  `tara-01 … tara-21 · benefits · structure · origin` (monospace, small). Thin arrows
  converging from the trees onto the column.
- Footer, small: `Every claim gets exactly one disposition — never zero, never two. A
  verifier recomputes every count.`

### Slide 19 — Consolidation is a viva, not a summary

- **TEXT:**
  - Headline: `We don't ask what they said. We ask all sixteen the same question.`
  - Four outcome labels in a row (chips): `Consensus` · `⚑ Divergence` · `Unique` ·
    `Silence — itself a finding` (⚑ in accent)
- **VISUAL (shapes):** sixteen small chair icons (or sixteen grey squares in a 4×4 grid)
  facing one board shape carrying a question mark.
- Footer, small italic, one real question:
  `"What narrative origin do commentaries give for Tārā's arising via a lotus connected to
  Avalokiteśvara — and do they agree the lotus grew specifically from his tears?"`

### Slide 20 — What consolidation finds  *(protect — best slide in the deck)*

- **TEXT:** headline across the bottom: `Divergence is recorded, never averaged.`
- **VISUAL — split slide:**
  - **Left panel, titled `Consensus`:** line `padma = utpala — four commentaries` +
    `[IMG-10 — two short Tibetan claim snippets with claim IDs]`
  - **Right panel, titled `⚑ Divergence` (⚑ accent):** two stacked groups, typed text:
    - `Tears stated: Gendün Gyatso · Dharmabhadra · Sungrab Tulku · Tsultrim Namdak`
    - `No tears: Tāranātha · Karma Maitri — pollen from the "water-born face"`
    - Beneath, accent line: `The word for "tears" does not occur anywhere in either
      commentary's file.`
- Footer strip: `[IMG-11 — the one-syllable variant: root text གསེར་སྔོ vs Gendün Drub
  སེར་སྔོ, side by side]` + caption `One syllable — two different etymologies licensed.`

### Slide 21 — The article

- **TEXT — the chain, monospace, arrows in support-gold:**
  `sentence → <ref> → claim ID → verbatim Tibetan → ^0-26 → source file`
- **VISUAL:** `[IMG-12 — the rendered article པདྨ with footnotes visible, one footnote's
  trail highlighted]` filling most of the slide; the chain text as a callout over it.
- Footer, small: `Of 44 standalone subjects, one was refused outright — for lack of citable
  claims. A system that always produces an article isn't following a rule.`

### Slide 22 — Two checks, checking different things

- **VISUAL — two deliberately unequal panels:**
  - **Left (larger), titled `The machine check — deterministic, blocking, no LLM`:**
    - Display: `861 / 882 quotations character-for-character (batch)`
    - Display: `81 / 81 in the audited pilot`
    - `[IMG-13 — two near-identical Tibetan strings, the changed punctuation circled]`
      + monospace label under it: `similarity 0.974 — FAIL` (FAIL in accent)
  - **Right (smaller), titled `The meaning check — adversarial, fresh model`:**
    - `same-model audit: "publish, no findings" × 3`
    - `cross-model audit: 5 blocking findings` (accent)
    - Small: `draft said "many scholars" — the claim said three.`
- **TEXT, bottom:** `A clean quote check is never, by itself, publication-ready.`
- Footer, tiny, the tiering: `exact → pass · whitespace-collapsed → pass ·
  punctuation-stripped fuzzy → FAIL · missing → fail. Found is not the gate. Passed is.`

### Slide 23 — What the audits actually measured

- **TEXT:** headline `Never report a same-model audit as independent.`
- **TABLE (typed, clean, generous row spacing):**

  | Check | Scope | Result |
  |---|---|---|
  | Deterministic gate — pilot | 81 quotations | 81/81 exact · 81/81 locators resolve |
  | Deterministic gate — batch | 882 quotations / 42 articles | 861/882 (97.6%) |
  | Consolidation audit | 418 citations / 3 pages | 0 fabricated IDs · 1 critical · 1 moderate · ~16 minor |
  | Same-model audit | 3 articles | "publish, no findings" × 3 |
  | Cross-model audit | same 3 articles | **5 blocking** · 4 genuine |
  | Auditor re-run variance | 3 rounds | 0.67 / 0.67 / 1.0 |

  The `5 blocking` cell in accent.

### Slide 24 — The humans, and the loop that matters

- **TEXT:** headline `A reader's objection became executable.`
- **VISUAL — three-part horizontal strip with arrows:**
  `reviewer's finding → new versioned skill → every future article`
  (three simple labelled boxes, middle one accent-bordered)
- **Below, the linguist's findings as six short chips, two rows:**
  - Row 1 (`register`): `too many citations per statement` · `reads as a literature review` ·
    `raw wikitext unreadable`
  - Row 2 (`orthography & respect`): `close every paragraph with the double shad` ·
    `the comma does not exist in Tibetan` · `names: copy the curated form — never invent an
    honorific`
- Footer, small: `Three revised articles are with the linguist. The corpus-wide redraft
  waits on that approval.`

### Slide 25 — Publication, and the economics  *(closing line on dark)*

- **TEXT, top:**
  - `create (19) · update (25) — one subject, one article, never forked`
  - `Manual now · bot later — the bot moves text, it never decides`
  - Display, accent: `Nothing published yet. On purpose.`
- **CHART — two horizontal bars:**

  | | |
  |---|---|
  | Writing, at the observed rate | ~285 years (grey, long) |
  | Reviewing, at 30–60 min/article | 24–48 person-years (accent, short) |

- Line under chart: `~$0.71 per article machine cost. Review is the constraint — by design.`
  `[LIVE-4]`
- **Bottom band — dark background strip, off-white italic display text:**
  `"The answer to the gap is neither refusal nor flood. It's verification, with a human hand
  on the gate."`

### Slide 26 — Thanks / links  *(dark background)*

- **TEXT (centred):** `Thank you` · `Tashi Tsering · OpenPecha`
- **Three labelled QR placeholders in a row:**
  `[IMG-14a — QR: the vault]` · `[IMG-14b — QR: the paper]` · `[IMG-14c — QR: a demo
  article]`
- Line, muted: `Reviewers welcome.`

---

## D. Backup slides (built, kept after slide 26, plain header `Backup — Bn`)

### B1 — Cost detail
- `$0.33 – $1.42 per article · 100,000 ≈ $35k–140k · prices falling` `[LIVE-4]`
- Line: `That is the marginal article — the pipeline itself is up-front engineering that
  amortizes.`
- Simple range bar, grey, with `$0.71` marked in accent.

### B2 — Full skills inventory
- Display: `62 skills · 21 with scripts · 44 scripts · 11,251 lines`
- `[IMG-15 — full Skills folder listing, two columns]`

### B3 — Isolation architecture
- Headline: `What each call receives — and what it is denied.`
- Two columns, monospace: **receives** `extraction rules · its own file path + line range ·
  its own node's decimal + title` / **denied** `every other node · every other commentary ·
  the tree-building instructions`
- Footer: `The guards are structural, not disciplinary.`

### B4 — Limitations, stated plainly
- Six short lines, no softening:
  - `Sectarian skew: 7 of 16 commentaries are Geluk`
  - `A praise genre yields zero reception-contested claims — due-weight machinery shown
    structurally, not adversarially`
  - `OCR quality bounds everything downstream`
  - `Articles are sic-faithful to their sources`
  - `No public citation URLs yet — no quotation is reader-checkable online`
  - `Claim-level judgements not yet human-validated`

### B5 — What generalises
- Headline: `Root text + commentaries + curated registry.`
- Line: `Bodhicaryāvatāra (10 commentaries) already prepared — and that corpus has real
  refutation exchanges.`
- Line: `Same shape: Sanskrit, Pāli, classical Chinese scholasticism.`

---

## E. Appendix A — asset manifest (for the author, after the build)

Placeholders to fill with screenshots. Source files per `03-facts-and-assets.md` §4.
Capture rules: raise the Tibetan font size first; crop to ≤ ~8 visible lines.

| ID | Content | Source |
|---|---|---|
| IMG-01 | darkened pecha photograph | author's photo library |
| IMG-02 | Greenlandic closure notice / Scots headline | live web |
| IMG-03 | agent-and-harness workshop drawing | author-commissioned / drawn |
| IMG-04 | `4-SYSTEM/Skills/` folder listing | Obsidian file pane |
| IMG-05 | `tree-guided-claims/SKILL.md` collapsed to headings | vault |
| IMG-06 | root verse 3 with `^1-3` | `1-SOURCES/Text/…བསྟོད་པ།.md` lines 43–46 |
| IMG-07a–d | scan / OCR / clean / addressed strip | BDRC + `0-INBOX/raw-data/` + `1-SOURCES/Commentaries/…ཕྲེང་བ།.md` lines 88–96 |
| IMG-08 | Gendün Drub tree, branch highlighted | `2-RAILS/Sections/Raw/toc-tree/gendun-drub.md` |
| IMG-09a–b | two claim cards | `2-RAILS/Claims/raw/tree-guided/gendun-drub.md` lines 396–432 |
| IMG-10 | consensus snippets with claim IDs | `2-RAILS/Claims/lotus.md` |
| IMG-11 | གསེར་སྔོ vs སེར་སྔོ side-by-side | root `^1-3` vs commentary `^0-24` |
| IMG-12 | rendered article + citation trail | `…/term-articles/lotus/article-preview.md`, `citations.md` |
| IMG-13 | tsheg/shad near-identical pair, FAIL | verifier report |
| IMG-14a–c | three QR codes | generate before the talk |
| IMG-15 | full skills listing (backup B2) | Obsidian file pane |

## F. Appendix B — `[LIVE-n]` morning-of-talk checklist (author only)

| ID | Value on slides | Re-check |
|---|---|---|
| LIVE-1 | 8,073 articles (19 Aug 2026) | bo.wikipedia siteinfo API |
| LIVE-2 | comparator article counts (slide 3) | meta.wikimedia.org / List of Wikipedias — not sourced in this vault; never quote from memory |
| LIVE-3 | speaker populations (slide 3) | one source for all four languages, not a mix |
| LIVE-4 | ~$0.71/article and derived totals | pricing note dated 2026-08-02; prices falling — round generously |

## G. Appendix C — verbatim Tibetan (author only; for making the IMG assets — never typed into Canva)

Root verse 3 (`^1-3`):

```
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། ། ^1-3
```

Claim `c-2-2-2-2-1-1-2-4` (*iconography*, cite `^0-26`):

```
དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ།
བཟུངས་ནས་སྙན་གྱི་ཐད་ཀར་ཁ་བྱེ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དག་པའི་རྟགས་སོ། །
```

The one-syllable variant (slide 20 footer, IMG-11):

```
root text     ^1-3   →   ཕྱག་འཚལ་གསེར་སྔོ་...
Gendün Drub   ^0-24  →   ཕྱག་འཚལ་སེར་སྔོ་...
```
