# Slide plan — "Verification with a human hand on the gate"

**Talk:** 15–20 min, online conference, humanities audience (Tibetology / Buddhist studies / DH).
**Design rule:** *minimum text on the slide, maximum image.* Nothing on a slide that the speaker
is going to say anyway. Target ≤ 12 words of body text per slide.

**22 slides · ~18 min speaking · 2 min buffer.** Four slides are marked **[CUT IF LONG]** — drop
them in order 16 → 7 → 3 → 19 if the clock runs away.

**The running thread.** One verse, one commentary, all the way through — introduced on slide 11
and never abandoned:

> **Root verse 3** (`^1-3`) → **Gendün Drub's ṭīkā** (1st Dalai Lama), blocks `^0-23`–`^0-27` →
> **tree node 2.2.2.2.1.1.2** → **5 typed claims** → **spine slot `tara-03`** →
> **consolidated page `lotus.md`** → **the article པདྨ**

Every artifact on those slides is a real file in the vault. Paths are in `03-facts-and-assets.md`.

---

## ACT I — The gap, and why it now compounds (slides 1–6, ~4 min)

---

### Slide 1 — Title

**On slide**
> Expanding the Digital Footprint of Tibetan
> *A semi-automatic pipeline for Wikipedia articles*
> Tashi Tsering · OpenPecha

**Visual:** full-bleed photograph of a Tibetan woodblock pecha or manuscript folio, darkened,
text overlaid. Nothing else. No logos crowding the corner.

**Image prompt (if generating):** *"A traditional Tibetan pecha — loose long-format folios of
handmade paper with black woodblock-printed Uchen script, stacked between wooden covers, warm
side lighting on a dark background, shallow depth of field, documentary photography."*

---

### Slide 2 — The gap, in one number

**On slide**
> **7,000,000 speakers**
> **8,073 articles**

**Visual:** those two numbers, enormous, stacked. Nothing else on the slide. Let the silence do
the work.

**Note:** 8,073 is a live API count from 19 Aug 2026 — **re-run it the morning of the talk** and
use the fresh number (see `03-facts-and-assets.md` §Verify).

---

### Slide 3 — Who does more with less **[CUT IF LONG]**

**On slide**
> Welsh: **91,000 → 280,000+**
> *(government policy, from 2017)*

**Visual:** a horizontal bar chart, speakers on one axis, article count as bar length. Four bars:
Welsh, Basque, Icelandic, Tibetan. Tibetan's bar is a stub. Colour every bar the same muted grey
except Tibetan, which is the one accent colour.

**Point of the chart:** these are all languages with *fewer speakers and a smaller classical
corpus* than Tibetan. The constraint was never the amount of material.

⚠ Verify all non-Welsh counts live before the talk (§Verify). Welsh figures are sourced in the
project bibliography.

---

### Slide 4 — Now it compounds: the models can't read us

**On slide**
> GPT-4 on Tibetan: **17.5%**
> Random guessing: **25%**

**Visual:** simple column chart. A dashed horizontal line labelled "random guessing (25%)". Two
columns: Qwen-2.5-72B in Chinese at 84.7% (tall, grey), the same model in Tibetan at 16.5%
(short, red), sitting *under* the dashed line. The visual gag is the line above the bar.

**Why it lands:** worse than a coin toss is not "needs improvement," it's *absent from the
training data*. And Wikipedia is, by Wikimedia's own account, almost always the largest
single source in a language model's corpus.

---

### Slide 5 — The loop has a sign

**Visual:** the whole slide is one diagram — two rings side by side, or one ring drawn twice.

- **Left ring (grey, arrows spiralling inward, labelled ↓):** no articles → no training text →
  models can't serve the language → nobody writes in it online → no articles.
- **Right ring (accent colour, arrows outward, labelled ↑):** cited articles → digital footprint
  → better tools → faster articles.
- **Between them, one word:** **verification.**

**On slide:** ring labels only. No prose.

**Diagram prompt:** *"Two circular feedback-loop diagrams side by side. Left: a downward
grey spiral with four nodes and inward arrows. Right: an upward-expanding loop in a single
accent colour with four nodes and outward arrows. Between them, one bold word: 'verification'.
Flat vector, thin strokes, generous white space, no decoration."*

---

### Slide 6 — Three options. Two are measured failures.

**On slide** — three columns, icon over one word each:
> ✋ **By hand** — too slow
> 🤖 **Bots** — Scots · Cebuano · Greenlandic
> ✅ **Supervised** — this talk

**Visual:** three panels. Panel 2 carries a small screenshot of the Greenlandic Wikipedia
closure notice, or the Scots Wikipedia controversy headline — a real artifact, not a clip-art
robot. Panel 3 is clean and empty, waiting.

---

## ACT II — How the work is actually done (slides 7–10, ~3 min)

---

### Slide 7 — The arithmetic of "by hand" **[CUT IF LONG]**

**On slide**
> Dzongkha: 5 months, dozens of people → **80 articles**
> Tibetan Wikipedia: **~350 articles / year**
> 100,000 articles → **~285 years**

**Visual:** a single timeline bar stretching off the right edge of the slide, with "today" at the
left and a tick at 285 years that is off-screen. Physically running out of slide is the point.

**Not a criticism of the editors** — say this out loud. It's the measured capacity of the mode.

---

### Slide 8 — What changed: agent + harness

**Visual:** the workshop analogy, drawn. A bench with tools racked on the wall, a rulebook
pinned above it, an in-tray and an out-tray, and a figure working at it.

- Label the **bench + tools + rulebook + trays** → "the harness"
- Label the **figure** → "the agent"

**On slide**
> The model is the apprentice.
> The harness is the workshop.

**Diagram prompt:** *"A clean flat-vector illustration of a craftsman's workbench: hand tools
racked on a pegboard wall, a pinned sheet of rules above the bench, an in-tray and out-tray
on the desk surface, and a seated figure working. Muted palette, thin outlines, two accent
colours, labelled callout lines pointing at the bench and the figure."*

---

### Slide 9 — Skills: the Matrix analogy

**Visual:** left half — a still or stylised frame evocative of the "I know kung fu" download
moment (do **not** use a copyrighted film still in a recorded talk; use a stylised
green-cascade graphic instead). Right half — a real screenshot of the vault's
`SKILLS-CATALOG.md` file list, showing the actual skill names in Obsidian.

**On slide**
> **63 skills** in this vault
> The model doesn't *know* the procedure. It loads it.

**Screenshot to take:** `4-SYSTEM/Skills/` folder listing in Obsidian's file pane, plus one
`SKILL.md` open beside it — `toc-tree-extraction/SKILL.md` reads well.

**Diagram prompt (safe alternative to a film still):** *"Stylised vertical cascade of
green glyphs on black, resolving at the centre into a single clean document icon labelled
'SKILL.md'. Minimal, high contrast."*

---

### Slide 10 — Scripts: the machine

**Visual:** a simple machine diagram. A hopper on the left (input), a boxed mechanism in the
middle with visible gears and a rule-plate bolted to its side, a chute on the right (output).
Under the box: "same input → same output, every time."

**On slide**
> The model **judges**.
> The script **verifies**.

**Speaker's contrast to draw on the slide, if it fits:** a small two-column strip along the
bottom — *judgement work* (is this sentence a structural division? does this gloss mean X?)
vs *machine work* (does this quotation appear character-for-character in the file it cites?).

**Diagram prompt:** *"Flat vector diagram of a simple industrial machine: a funnel-shaped input
hopper on the left, a rectangular mechanism in the centre with three visible gears and a small
bolted plate labelled 'rules', and an output chute on the right. Thin black outlines, one
accent colour, plenty of white space, no text baked in."*

---

## ACT III — The pipeline, followed through one verse (slides 11–19, ~8 min)

---

### Slide 11 — The corpus, and the thread we'll follow

**On slide**
> 1 root text · **16 commentaries** · ~540,000 characters
> Sakya · Geluk · Jonang · Nyingma · Kagyü

**Visual:** left — a photograph of the Praise text. Right — the four lines of **root verse 3** in
large Uchen, with the block ID `^1-3` visible in a muted colour beside it:

```
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། ། ^1-3
```

**This is the promise slide.** Say explicitly: "we will follow *this verse*, through *one
commentary*, all the way to a published article."

---

### Slide 12 — Getting the text in

**Visual:** a left-to-right strip of four panels, each one a real screenshot:
1. A BDRC scan page (Gendün Drub's ṭīkā if available)
2. Raw OCR output — messy, page numbers, running headers, junk
3. The cleaned file
4. The same text carrying block IDs, `^0-23` … `^0-27` visible

**On slide**
> scan → OCR → clean → **address**

**The one idea to plant:** block IDs. Every discrete block of every text in the corpus gets a
permanent address. That address is what makes every later citation checkable. It is the whole
foundation — a footnote that points at a *file* is a promise; a footnote that points at a
*block* is an address you can open.

**Also mention here (30 seconds, no slide of its own):** *segmentation* — cutting the commentary
into citation-sized blocks — runs behind a **no-loss gate**: if the segmented text differs from
the original by a single non-whitespace character, the script aborts and writes nothing.

---

### Slide 13 — The author's own outline (sa-bcad)

**Visual:** the real tree, on screen, as a screenshot of the vault file — Gendün Drub's, nested
to seven levels. Highlight one branch in the accent colour, all the way down to
**2.2.2.2.1.1.2** ("praise by body colour, hand-emblem, and cause"). That node is where verse 3
lives.

**On slide**
> **37 nodes · 7 levels**
> The commentator's own architecture, recovered.

**Screenshot:** `2-RAILS/Sections/Raw/toc-tree/gendun-drub.md`

**Worth saying:** the 21 leaf nodes under "extended explanation" come out at exactly 21. The
tree recovers the praise's own structure *as the commentator declared it* — the machine didn't
impose an outline, it found the one that was already there.

---

### Slide 14 — Claims: index cards, not paraphrase

**Visual:** the five real claims from that one node, laid out as five index cards. Show **two**
in full (c-...-2-3 and c-...-2-4) and let the other three be visible-but-small behind them.
Each card shows: verbatim Tibetan · English gloss · **Type** · **Cite → `^0-26`**.

**On slide**
> **2,975 claims** · 16 commentaries
> one fact · one type · one address

**Card content (verbatim, from the vault):**

> **c-2-2-2-2-1-1-2-3** — *word-gloss*
> སྔོ་བ་ནི། སྐུ་མདོག །སེར་ནི། ཁ་དོག་དྭངས་པ་མཚོན་པ་སྟེ།
> "Blue" refers to her body colour; "gold" indicates a clear hue.
> → `^0-25`

> **c-2-2-2-2-1-1-2-4** — *iconography*
> དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ།
> Her left ring-finger holds a water-born lotus (utpala) at her heart — the sign of the ten
> pure perfections.
> → `^0-26`

**Type labels to show as a row of chips somewhere on the slide:** `etymology` · `word-gloss` ·
`iconography` · `identification` · `doctrinal` · `structural`

---

### Slide 15 — Two ways to choose what gets an article

**Visual:** a fork diagram. One input at the top ("2,975 claims"), two branches:

- **Left — by structure.** The root text's own shape: 21 homages + benefits + 2 global slots =
  **24 slots.** One article per slot.
- **Right — by keyword.** What the corpus actually talks about, most. One article per subject.

**On slide**
> by **structure** ↔ by **keyword**

Both branches converge again three slides later at "consolidation." Say so.

---

### Slide 16 — The keyword chain **[CUT IF LONG]**

**Visual:** a funnel, four stages, numbers shrinking down it:

> **193 + 313** English candidates
> ↓
> **367** Tibetan terms
> ↓ *viability gate: ≥ half the commentaries, ≥ 20 claims*
> **114** pass
> ↓ *subject filter*
> **44** standalone subjects — 25 update / 19 create

**On slide, one line only**
> Detect in **English**. Measure in **Tibetan**.

**The two-line explanation (say it, don't slide it):** Tibetan has no word boundaries, so
keyword statistics can't run on it directly — but *counting a string you already know* needs no
word segmentation at all. So candidates are found in a deliberately literal English translation,
each occurrence is mapped back to the exact Tibetan span it translates, and all the *measuring*
happens on the Tibetan side.

**The validation worth one sentence:** before the "attention" signal was added, Tibetan
intensifier particles sat in the top 20. After it, none survives into the top 60.

---

### Slide 17 — The spine map: Stephanus numbers for a commentarial corpus

**Visual:** left — three small, obviously *different* outline trees (one nests a homage at
`1.1.N`, one at top-level `N`, one runs all 21 inside a single undivided node). Right — a single
vertical column of 24 numbered slots, `tara-01` … `tara-21`, `benefits`, `structure`, `origin`.
Arrows from all three trees converging onto the same slots.

**On slide**
> Every commentary numbered its own way.
> One shared coordinate system.

**The analogy to say:** this is Stephanus pagination for Plato, or Bekker numbers for Aristotle —
except built once per commentary, by machine, and every claim gets **exactly one** disposition:
routed, flagged ambiguous, or logged unmapped. Never zero (silent loss), never two (silent
duplication).

**Screenshot:** the slot table in `2-RAILS/Claims/raw/spine-map/karma-maitri.md`

---

### Slide 18 — Consolidation is a viva, not a summary

**Visual:** the seminar table. Sixteen chairs around a table, one question on a board. Then, as
a build or a second panel, the four possible outcomes as coloured labels:

> **Consensus** · **⚑ Divergence** · **Unique** · **Silence** *(itself a finding)*

**On slide**
> We don't ask *what they said.*
> We ask **all sixteen the same question.**

**Show one real question** from `lotus.md`, at the bottom of the slide in small type:

> *"What narrative origin do commentaries give for Tārā's arising via a lotus connected to
> Avalokiteśvara — and do they agree the lotus grew specifically from his tears?"*

**Where the questions come from (say it):** they're *generated*, not authored — mechanically from
the spine (21 homages × observed facets: name, colour, implement, stance, activity, mantra,
benefit), and from the extractions themselves, since every claim one commentary makes implies a
question you can put to the other fifteen. Free reading first; generated questions then catch
what free reading missed.

---

### Slide 19 — What consolidation finds **[CUT IF LONG, but it's the best slide in the deck]**

**Visual:** split slide, one real finding on each side.

**Left — consensus:** *padma = utpala.* Four commentaries gloss the verse's own word པདྨ as
specifically an utpala. Show two short Tibetan snippets with their claim IDs.

**Right — ⚑ divergence:** the origin narrative splits.
- **Tears stated:** Gendün Gyatso, Dharmabhadra, Sungrab Tulku, Tsultrim Namdak — tears → lotus
  → pollen → Tārā.
- **No tears:** Tāranātha and Karma Maitri say the pollen issues from Avalokiteśvara's
  "water-born face" — a standing epithet. *The word* སྤྱན་ཆབ *(tears) does not occur anywhere in
  either commentary's file.*

**On slide**
> Divergence is **recorded**, never averaged.

**The line that lands with this audience:** the machine also surfaced a *root-text variant* — the
corpus reads གསེར་སྔོ where Gendün Drub's text quotes སེར་སྔོ. One syllable, two different
etymologies licensed. This is a philological instrument, not just an aggregator.

---

### Slide 20 — The article

**Visual:** the finished article, rendered. Screenshot of
`3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/lotus/article-preview.md` in Obsidian, with
the footnote superscripts visible. Beside or below it, a callout arrow tracing one footnote back
down the chain:

> sentence → `<ref>` → claim ID → verbatim Tibetan → `^0-26` → the source file

**On slide**
> **པདྨ**
> every sentence traceable to a block

**The invariant to state plainly:** *claims-only drafting.* After the claims table is built, the
drafting model **never sees source wording again**. It cites claim indices; code expands them
back into quotations and renders the references. That is what keeps a character-for-character
check meaningful — the model literally cannot smudge a quotation it was never shown.

**Also on this slide:** *no parametric knowledge.* No date, no Sanskrit form, no iconographic
detail that isn't in a claim, however standard it seems. Of 44 standalone subjects, **one was
refused outright** for lack of citable claims — the refusal is the evidence the rule binds.

---

## ACT IV — Why you can trust it, and who publishes (slides 21–22, ~3 min)

---

### Slide 21 — Two things check the work, and they check different things

**Visual:** two panels, deliberately unequal in character.

**Left — the machine check (deterministic, blocking, no LLM):**
> **861 / 882** quotations character-for-character
> **81 / 81** in the audited pilot

Under it, the tsheg story as a tiny visual: two nearly identical Tibetan strings, with the one
changed punctuation mark circled in red, and the label **"string similarity 0.974 — FAIL."**
A tsheg silently promoted to a shad. Invisible to a human skimming. Not a quotation any more.

**Right — the meaning check (adversarial, a fresh model that did not write the page):**
> same-model audit: *"publish, no findings"* ×3
> cross-model audit: **5 blocking findings**

Show one real finding: the draft said **"many scholars"** where the claim said **three**.

**On slide**
> A clean quote check is never, by itself, publication-ready.

**The design lesson to say out loud:** never report a same-model audit as independent. An agent
auditing its own work re-reads its own intentions, not the text.

---

### Slide 22 — The humans, and the gate

**Visual:** three-part strip.

1. **The reviewer's findings become code.** The project's Tibetan linguist read the batch and
   returned six findings — three about register (too many citations per sentence; reads like a
   literature review, not an encyclopedia; raw wikitext unreadable) and three about orthography
   and respect (every paragraph must close with the double shad །།; the comma does not exist in
   Tibetan; commentators must be named by a respectful, human-curated form of their name).
   Every one became a rule in a **new versioned skill** — never an in-place edit of the shipped
   one.
2. **Two paths at publication.** *Create* (19 subjects) vs *update* an existing article with
   cited sections (25). One subject, one article — never forked.
3. **The gate.** Manual now, bot later. Dry-run is the default on every publish path. And:
   **nothing has been published yet.** Community consultation comes first; the absence of a
   local policy on machine-assisted content is read as *stop*, not as permission.

**On slide**
> Nothing published yet — **on purpose.**

**Closing numbers, small, at the foot of the slide:**
> ~$0.71 / article machine cost · **review is the constraint**
> 285 years of writing → 24–48 person-years of reviewing

**The last sentence of the talk:** *"The answer to the gap is neither refusal nor flood. It's
verification, with a human hand on the gate."*

---

## Backup slides (hold in reserve for Q&A)

- **B1 — Cost table.** $0.33–1.42/article; 100k articles ≈ $35k–140k; one project grant.
- **B2 — The extraction-capture cliff.** The same model on the same prompt returned 10 passages
  / 873 characters when given 93,000 characters of context, and 20 passages / 5,224 characters
  when given 12,000. *The model budgets its answer against the size of the question.* The fix is
  architectural — batch smaller — not a better prompt. This is the single most useful practical
  finding in the project for anyone building something similar.
- **B3 — Isolation as a structural guard.** One model call per tree node, each seeing only its
  own window. A call that only ever sees one node *cannot* file a claim under the wrong node,
  *cannot* import from another commentary. Guards made structural instead of disciplinary.
- **B4 — Limitations, stated plainly.** Sectarian skew (7 of 16 Geluk); the praise genre yields
  zero contested claims so the reception machinery is demonstrated structurally, not
  adversarially; OCR quality bounds everything; no citation yet carries a public URL; claim-level
  judgements are not yet human-validated.
- **B5 — What generalises.** Root text + commentaries + a curated registry. Already prepared over
  the Bodhicaryāvatāra (10 commentaries, with real refutation exchanges). Nothing in the
  architecture is specific to 21 homages.
