# Slide plan — "Verification with a human hand on the gate"

**Talk:** 15–20 min, online conference. **Audience: ~50% humanities, ~50% technical.**
**Design rule:** minimum text, maximum image and chart. ≤ 12 words of body text per slide.

**26 slides · ~19 min · buffer 1 min.** Cut list, in order: **17 → 7 → 3 → 12b**.

---

## Writing for a 50/50 room

The mistake to avoid is picking one audience. The fix is **layering**, not averaging — each
slide carries one plain-language idea that everyone gets, and one precise mechanism the
technical half can chew on. The humanities half never feels lectured at; the technical half
never feels condescended to.

The pattern, used throughout the speaker notes:

> **Name it plainly → give the analogy → then state the mechanism precisely.**
> *"Every commentary numbers itself differently. Think Stephanus numbers for Plato. Concretely:
> a routing table per commentary, built once, and every claim gets exactly one disposition —
> never zero, never two."*

Three sentences. The first two are for everyone. The third is where the engineers lean in — and
the humanities half still follows it, because the analogy already did the work.

**Two things flip the room the other way**, and both are worth doing deliberately:
- Give the **technical half something they didn't expect from a Tibetan-studies talk** — the
  isolation architecture, the context-size finding, the same-model-audit result. They will
  remember those.
- Give the **humanities half something that is real philology** — the divergence the machine
  surfaced, the root-text variant. They will remember that.

In the notes, cues are marked **[HUM]** and **[TECH]**. Say both, in that order. Where a slide
is marked **[TECH-LED]**, the mechanism *is* the point and the analogy is the garnish.

---

## The running thread

One verse, one commentary, all the way through — introduced on slide 13, never abandoned:

> **Root verse 3** (`^1-3`) → **Gendün Drub's ṭīkā** (1st Dalai Lama), blocks `^0-23`–`^0-27`
> → **tree node 2.2.2.2.1.1.2** → **5 typed claims** → **spine slot `tara-03`** →
> **consolidated page `lotus.md`** → **the article པདྨ**

Every artifact is a real file. Paths in `03-facts-and-assets.md`.

---

# ACT I — The gap, and why it compounds (1–6, ~4 min)

### Slide 1 — Title

> Expanding the Digital Footprint of Tibetan
> *A semi-automatic pipeline for Wikipedia article generation*
> Tashi Tsering · OpenPecha

**Visual:** full-bleed darkened photograph of a Tibetan pecha, text overlaid.

---

### Slide 2 — The gap, in one number

> **7,000,000 speakers**
> **8,073 articles**

**Visual:** two numbers, enormous, stacked. Nothing else. Pause on it.

*(Re-run the live count the morning of the talk — see `03-facts-and-assets.md` §5.)*

---

### Slide 3 — Who does more with less **[CUT 3rd]**

> Welsh: **91,000 → 280,000+** *(government policy, 2017)*

**CHART — grouped horizontal bars, speakers vs articles.** Four languages. Every bar muted grey
except Tibetan in the accent colour. The visual argument is that the article bar has no
relationship to the speaker bar.

⚠ Welsh figures are sourced in the project bibliography. **Basque / Icelandic / Estonian counts
are not sourced in this vault** — pull them live from
`meta.wikimedia.org/wiki/List_of_Wikipedias` the morning of the talk.

**The line:** every one of these has *fewer speakers and a smaller classical corpus* than
Tibetan. The constraint was never the amount of material.

---

### Slide 4 — The models can't read us

**CHART — column chart with a threshold line.** A dashed horizontal rule at 25% labelled
"random guessing." Three columns:

| Series | Value |
|---|---|
| Qwen-2.5-72B — Chinese | 84.7% |
| Qwen-2.5-72B — Tibetan | 16.5% |
| GPT-4 — Tibetan | 17.5% |

Colour the two Tibetan columns in the accent colour. Both sit *below* the dashed line. That's
the whole graphic — the line above the bar.

> Below the coin-toss line.

**[TECH] add on the slide, small:** Tibetan costs ~**4×** the tokens of Chinese per unit of text
(Petrov et al. 2023). Worse service, higher price.

---

### Slide 5 — The loop has a sign

**Visual:** one diagram, two rings.
- **Left (grey, inward spiral):** no articles → little training text → tools can't serve the
  language → fewer people write in it → no articles.
- **Right (accent, outward):** cited articles → digital footprint → better tools → faster
  articles.
- **Between them, one word:** **verification.**

**The point:** same loop, same machinery. Only the sign differs.

---

### Slide 6 — Three options. Two are measured failures.

> ✋ **By hand** — too slow
> 🤖 **Unsupervised** — Scots · Cebuano · **Greenlandic (closed, 2025)**
> ✅ **Supervised** — this talk

**Visual:** three panels; panel 2 carries a real screenshot (the Greenlandic closure notice or
the Scots controversy headline), not clip-art.

**The counterweight, small at the foot:** Content Translation — machine draft + *mandatory*
human edit — shows **lower** deletion rates than from-scratch articles across 2.4M+ creations.
The failure mode and the working mode differ in exactly one variable.

---

# ACT II — How the work is actually done (7–11, ~4 min)

### Slide 7 — The arithmetic of "by hand" **[CUT 2nd]**

**CHART — one horizontal bar running off the right edge of the slide.**

| Mode | Rate | 100,000 articles takes |
|---|---|---|
| bo.wikipedia, observed | ~350/yr | **~285 years** |
| Dzongkha program (manual, funded) | 80 articles / 5 months | — |
| This pipeline | review-bound | **24–48 person-years** |

Draw the 285-year bar so it physically leaves the slide. Running out of slide is the point.

**Say it out loud:** this is not a criticism of the editors. It's the measured capacity of the
mode.

---

### Slide 8 — Agent and harness

**Visual:** the workshop, drawn. Bench + racked tools + a rulebook pinned above + in-tray /
out-tray → labelled **"the harness."** The figure working at it → labelled **"the agent."**

> The model is the apprentice.
> The harness is the workshop.

**[TECH] add to the slide as a small stack diagram:**

```
model          judgement
  ├ tools      read · write · run · search
  ├ context    what it is allowed to see, per call
  └ rules      what it must do, loaded per task
```

An agent is that loop running unattended: read → judge → write → check → repeat.

---

### Slide 9 — Skills: the Matrix analogy **[the hinge slide]**

**Visual:** left — stylised green cascade resolving into a single document icon labelled
`SKILL.md`. *(Do not use a copyrighted film still in a recorded talk.)* Right — a real screenshot
of the vault's `4-SYSTEM/Skills/` folder listing.

> **62 skills** · **11,251 lines** of written-down method
> The model doesn't *know* the procedure. It **loads** it.

**[HUM]** Neo doesn't train for years. Someone loads a program: "I know kung fu."
**[TECH]** A skill is a markdown file injected into context immediately before the operation
that needs it. Not fine-tuning, not a plugin, not code — a *procedure*, versioned in git.

---

### Slide 10 — Anatomy of a skill **[TECH-LED]**

**Visual:** one `SKILL.md` on screen, collapsed to its section headings, with callouts. Use
`tree-guided-claims/SKILL.md` — it's the longest and the best-argued.

```
## Why this skill exists, and what it is not    ← the reasoning, and the failure it answers
## Inputs / Output / Output file format         ← the contract
## Rules            1 … 16                      ← numbered, each traceable to a real defect
## Procedure        Step 1 … Step 10            ← what to actually do
## Completion check                             ← how you know you're done
scripts/verify_*.py                             ← the deterministic backstop
```

> **62 skills · 21 carry scripts · 44 scripts total**

**The line that matters to both halves of the room:** a skill is a *text file*. A Buddhist
scholar can read it, disagree with it, and edit it. That is not true of a prompt buried in code,
and it is why the domain experts on this project can actually govern the system.

---

### Slide 11 — Why the rules exist: skills as institutional memory **[the slide to protect]**

**Visual:** three real rules, each with the failure that produced it. Two columns — **the rule**
on the left, **the scar** on the right.

| The rule | Why it exists |
|---|---|
| *"`claim_count` is computed by counting, at the end — never inherited."* | A run that claimed to be an independent extraction had **114 of 118** Tibetan strings byte-identical to the earlier run. Counts had been copied, not recomputed. |
| *"Corroboration must be re-read, not remembered."* | The audit's one critical finding: a "three flaws" framing attributed to a second commentary whose cited claim contains no such framing. Right idea, wrong claim ID. |
| *"Counts are computed, never hand-tallied."* | **Five of five** "(N commentaries)" labels on the worst pilot page were wrong. |

> Every rule is a scar.

**The generalisable claim — say this one slowly, it's the most transferable idea in the talk:**
we don't fix a bad output by re-running with a better prompt. We find the *class* of error, write
it into the skill as a numbered rule, and where possible add a script that fails the build. The
fix outlives the person who found it.

**[TECH] the three standing design principles, small at the foot:**
> the model judges, the script verifies · isolation over context · nothing interpretive touches
> the source layer

---

### Slide 12 — Scripts: the machine

**Visual:** hopper → boxed mechanism with gears and a bolted rule-plate → chute.
Under it: *same input → same output, every time.*

> The model **judges**. The script **verifies**.
> The script has the **final say**.

**Two-column strip along the bottom:**

| Judgement (model) | Machine (script) |
|---|---|
| Is this line a structural announcement or prose? | Does this string appear character-for-character in the file it cites? |
| Does this gloss say *blue* or *clear-hued*? | Do the claim counts recompute? |
| Which commentaries actually disagree here? | Does every claim have exactly one disposition? |

**[TECH]** No bypass flag exists. An audit verdict of "publish" does not skip the gate. We
deliberately did not build an override.

---

### Slide 12b — The context-size finding **[CUT 4th · but strong for the technical half]**

**CHART — two paired columns. Same model, same prompt, different context size.**

| Context given | Passages returned | Characters returned |
|---|---|---|
| 93,000 chars | 10 | **873** |
| 12,000 chars | 20 | **5,224** |

> The model budgets its answer against the size of the question.

**The consequence:** you cannot fix this in the prompt. It's architectural — batch the question
smaller. It is exactly why claims extraction now runs **one isolated call per outline node**
instead of one call per commentary. Pilot capture rates before that change: 45%, 19%, **1.1%**.

---

# ACT III — The pipeline, through one verse (13–21, ~8 min)

### Slide 13 — The corpus, and the thread

**CHART — the corpus at a glance, as a stacked/proportional figure:**

> **16** commentaries · **582,332** Tibetan characters · **3,268** citable blocks
> **580** outline nodes · **2,975** claims
> Sakya · Geluk · Jonang · Nyingma · Kagyü · Sūryagupta

Beside it, the four lines of **root verse 3** in large Uchen with `^1-3` visible.

**The promise to state:** we will follow *this verse*, through *one commentary*, all the way to a
finished article. Every screen from here is a real file.

---

### Slide 14 — Getting the text in

**Visual:** four-panel strip, all real screenshots: BDRC scan → raw OCR (messy) → cleaned →
block-addressed with `^0-23` … `^0-27` visible.

> scan → OCR → clean → **address**

**[HUM]** A footnote pointing at a *file* is a promise. A footnote pointing at a *block* is an
address someone can open.
**[TECH]** Cleaning builds a **profile** of the mechanical debris first, shows it to a human, then
runs a cleaner limited to exactly those fixes. Segmentation runs behind a **no-loss gate**: if the
segmented text differs from the original by one non-whitespace character once whitespace is
squeezed out, the script aborts and writes nothing. Residue no rule can cut goes to a human under
a stated bias — *over-long is safer than wrong*.

---

### Slide 15 — The author's own outline (sa-bcad)

**Visual:** the real tree — Gendün Drub's, 37 nodes, 7 levels — with one branch highlighted all
the way down to **2.2.2.2.1.1.2**.

> **37 nodes · 7 levels**
> The 21 leaves under "extended explanation" come out at exactly **21**.

**[HUM]** The commentator announced his own structure. We recovered it; we didn't impose it.
**[TECH]** Extraction runs as **five isolated passes** — chunk, extract candidates, copy the
enumeration announcements verbatim, build, check. The finding: *a call that never sees the
tree-building instructions cannot drift into tree-building*, and a verbatim-copy call that never
sees "interpret and reconcile" stays literal. Merging the jobs measurably dropped precision. Tree
building treats the author's own enumerations as more authoritative than individual candidates —
if he declares six parts, six children must appear.

---

### Slide 16 — Claims: index cards, not paraphrase

**Visual:** the five real claims from that one node, as index cards. Two shown full, three small
behind. Each card: verbatim Tibetan · English gloss · **Type** · **Cite → `^0-26`**.

> **2,975 claims** · one fact · one type · one address

Type chips: `etymology` · `word-gloss` · `iconography` · `identification` · `doctrinal` ·
`structural`

**[HUM]** A Zettelkasten slip. One card, one fact, one shelf-mark.
**[TECH]** Two invariants:
> **Extract first, merge later.** Each commentary is read in complete isolation — the first
> commentary you read otherwise silently defines the topic space for all the rest.
> **One model call per node.** Each call receives only the extraction rules, its own file path
> and line range, and its own node's decimal and title. **Nothing else.**

The consequence is the part worth stating precisely: a call that only ever sees one node
*cannot* file a claim under the wrong node, and *cannot* import from a commentary it was never
shown. **The guards are structural, not disciplinary.**

---

### Slide 17 — Sixteen commentaries are not sixteen of the same thing **[CUT 1st]**

**CHART — scatter or paired bars: claim density per 10,000 characters.** Real data, ordered:

| Commentary | chars | claims | claims / 10k chars |
|---|---|---|---|
| karma-maitri | 8,986 | 163 | **181** |
| taranatha | 31,741 | 368 | **116** |
| drakpa-gyaltsen | 12,805 | 142 | **111** |
| lobsang-dawa | 9,967 | 87 | 87 |
| dharmabhadra | 18,293 | 148 | 81 |
| gendun-drub | 20,060 | 131 | 65 |
| sungrab-tulku | 27,112 | 160 | 59 |
| gendun-gyatso | 11,004 | 62 | 56 |
| konchok-thabkhe | 24,535 | 132 | 54 |
| yama-sonam | 48,070 | 258 | 54 |
| sangye-nyentrul | 24,562 | 125 | 51 |
| tenzin-dhonzang | 71,628 | 327 | 46 |
| palden-sherab | 82,236 | 282 | 34 |
| tsultrim-namdak | 143,634 | 329 | **23** |

> **8× spread.** A word-commentary is dense. An expansive exegesis with ritual appendices is not.

**Why this slide earns its place with both halves:** for the humanities half it's a genre
observation the corpus produced by itself. For the technical half it's the reason a fixed
chunk size or a uniform per-commentary budget would have been wrong.

**Pair it with the structural spread** — outline nodes per commentary run from **2**
(drakpa-gyaltsen, a word-commentary with almost no sa-bcad) to **120** (palden-sherab). **60×.**
That is the slide that motivates the next one.

---

### Slide 18 — The spine map: Stephanus numbers for a commentarial corpus

**Visual:** left — three visibly different outline trees. Right — one column of 24 numbered
slots. Arrows converging.

> Every commentary numbered its own way. **One shared coordinate system.**

**[HUM]** Stephanus pagination for Plato. Bekker numbers for Aristotle.
**[TECH]** One routing table per commentary, built **once**, reused by every topic afterwards.
The problem it solves is a complexity problem: answering "which node holds slot N" inside every
topic run meant ~400 full-file reads over an unchanged multi-megabyte corpus. Sixteen judgements
instead of four hundred, because "which node is Tārā 5" and "which node is Tārā 12" are the same
act of reading the tree.

The invariant: **every claim gets exactly one disposition** — routed by subtree, routed by
claim-ID range, flagged ambiguous, or logged unmapped. Never zero (silent loss), never two
(silent duplication). A verifier recomputes every count and refuses to finish otherwise.

The hard case, worth naming: one commentary runs all 21 homages inside a single undivided node.
It's routed by **claim-ID range** instead, using its own "verse N quoted" claims as boundary
markers.

---

### Slide 19 — Consolidation is a viva, not a summary

**Visual:** sixteen chairs, one question on a board. Then four outcome labels.

> **Consensus** · **⚑ Divergence** · **Unique** · **Silence** *(itself a finding)*
> We don't ask what they said. We ask **all sixteen the same question.**

One real question in small type at the foot:
> *"What narrative origin do commentaries give for Tārā's arising via a lotus connected to
> Avalokiteśvara — and do they agree the lotus grew specifically from his tears?"*

**[TECH]** The questions are **generated, not authored** — mechanically from the spine (21
homages × observed facets: name, colour, implements, stance, activity, mantra, benefit), and from
the extractions themselves, since every claim one commentary makes implies a question you can put
to the other fifteen. Free extraction first, generated questions second: consolidation becomes a
**derived completeness check** rather than a summary. Afterwards a script diffs the packet
manifest against every claim the page cites; anything in the gap is folded in or logged with a
reason. No third state. That check caught real gaps in **5–12%** of a topic's claims per page.

---

### Slide 20 — What consolidation finds **[PROTECT — best slide in the deck]**

**Visual:** split slide, one real finding each side.

**Left — consensus.** *padma = utpala.* Four commentaries gloss the verse's own word པདྨ as
specifically an utpala. Two short Tibetan snippets with claim IDs.

**Right — ⚑ divergence.** The origin narrative splits:
- **Tears stated:** Gendün Gyatso · Dharmabhadra · Sungrab Tulku · Tsultrim Namdak — tears →
  lotus → pollen → Tārā
- **No tears:** Tāranātha and Karma Maitri — the pollen issues from Avalokiteśvara's "water-born
  face," a standing epithet

> The word སྤྱན་ཆབ *(tears)* **does not occur anywhere in either commentary's file.**

**And the philological payoff:** the corpus reads གསེར་སྔོ at homage 3; Gendün Drub's text quotes
**སེར་སྔོ**. One syllable — two different etymologies licensed.

> Divergence is **recorded**, never averaged.

**[HUM]** This is the slide that says: it's an instrument, not an aggregator.
**[TECH]** Note the epistemics on the page itself — it records a difference in *what these
commentaries' captured claims state*, not a positive denial. That distinction is written into the
output, not left to the reader.

---

### Slide 21 — The article

**Visual:** the rendered article `པདྨ`, footnotes visible, with a callout tracing one footnote
down the chain:

> sentence → `<ref>` → claim ID → verbatim Tibetan → `^0-26` → source file

**[TECH] the two refusals that make it work:**
> **Claims-only drafting.** After the claims table is built, the drafting model **never sees
> source wording again.** It cites claim *indices*; code expands them and renders the references.
> Verified in code — the prompt constructor passes nothing else. The model cannot smudge a
> quotation it was never shown, which is what makes a character-exact check meaningful rather
> than decorative.
> **No parametric knowledge.** No date, no Sanskrit form, no iconographic detail that isn't in a
> claim — however standard it seems.

**The evidence the rule binds:** of 44 standalone subjects, **one was refused outright** for lack
of citable claims. A system that always produces an article isn't following a rule.

---

# ACT IV — Trust, and who publishes (22–25, ~3 min)

### Slide 22 — Two checks, checking different things

**Visual:** two deliberately unequal panels.

**Left — the machine check** (deterministic, blocking, no LLM):
> **861 / 882** quotations character-for-character (batch)
> **81 / 81** in the audited pilot, all locators resolving

Under it, the tsheg story: two near-identical Tibetan strings, the changed punctuation circled.
**"similarity 0.974 — FAIL."**

**[TECH] the tiering is the policy, and it's deliberately unequal:**
> exact → **pass** · whitespace-collapsed → **pass** (line wrapping isn't text) ·
> punctuation-stripped fuzzy → **FAIL** (letters agree, punctuation doesn't — you're not quoting
> what the file says) · missing → fail
> *Found is not the gate. Passed is the gate.*

**Right — the meaning check** (adversarial, fresh model that did not write the page):
> same-model audit: *"publish, no findings"* × 3
> cross-model audit: **5 blocking findings**

One real finding: draft said **"many scholars"**; the claim said **three**.

> A clean quote check is never, by itself, publication-ready.

---

### Slide 23 — What the audits actually measured **[numbers slide]**

**CHART — a small table or dot plot, honest about what's measured vs pending:**

| Check | Scope | Result |
|---|---|---|
| Deterministic gate, pilot | 81 quotations | **81/81** exact · 81/81 locators resolve |
| Deterministic gate, batch | 882 quotations, 42 articles | **861/882 (97.6%)** |
| Consolidation audit | **418** citations, 3 pages | **0** fabricated IDs · 1 critical · 1 moderate · ~16 minor |
| Same-model audit | 3 articles | "publish, no findings" × 3 |
| Cross-model audit | same 3 articles | **5 blocking**, 4 genuine on adjudication |
| Auditor re-run variance | 3 rounds | pass rates **0.67 / 0.67 / 1.0** |

**Two honesty notes to say, not slide:** of 293 validator findings, **269** are a single
reference-format mismatch between the two drafting routes — mechanical, not fabricated citations.
And twice the auditor **misquoted the draft inside its own finding**, inventing typos that weren't
there. Model-written finding text is itself untrusted — which is exactly why the deterministic
check, which cannot hallucinate, sits *beneath* the audit rather than beside it.

> **Never report a same-model audit as independent.**

---

### Slide 24 — The humans, and the loop that matters

**Visual:** three-part strip — *reviewer's finding* → *new versioned skill* → *every future
article*.

The linguist's six findings, real:
- **Register:** too many citations per statement · reads as a literature review, not an
  encyclopedia · raw wikitext unreadable
- **Orthography and respect:** every paragraph closes with the double shad །། · **the comma does
  not exist in Tibetan** · commentators named by a respectful, human-curated form of their name

Every one became a rule in a **new versioned drafting skill** — never an in-place edit of the
shipped one.

> A reader's objection became **executable**.

**The respect rule is the one to dwell on:** a human-curated name field the model may only
**copy** — never invent, translate, or upgrade an honorific.

**And the gating:** three revised articles are with the linguist; the corpus-wide redraft waits on
that approval. We don't batch-redraft ahead of the human.

---

### Slide 25 — Publication, and the economics

> **create** (19) · **update** (25) — one subject, one article, never forked
> Manual now · bot later — the bot moves text, it never decides
> **Nothing published yet. On purpose.**

**CHART — the closing comparison, two bars:**

| | |
|---|---|
| Writing, at the observed rate | **~285 years** |
| Reviewing, at 30–60 min/article | **24–48 person-years** |

> ~**$0.71** per article machine cost. **Review is the constraint — by design.**

**Say:** the wiki has no local policy on machine-assisted content, and we read that vacuum as
*stop*, not permission. Public bilingual proposal first, on-wiki project page listing every
assisted article with its reviewer and sources, disclosure on every edit. And a debt I'll name:
no citation yet carries a public URL, so no quotation is reader-checkable online. That's the
single largest pre-publication task.

**Last line:** *"The answer to the gap is neither refusal nor flood. It's verification, with a
human hand on the gate."*

---

### Slide 26 — Thanks / links

Contact · the vault · the paper · an invitation for reviewers.

---

## Backup slides (Q&A)

- **B1 — Cost detail.** $0.33–1.42/article; 100k ≈ $35k–140k; prices falling. That's the
  *marginal* article — the pipeline itself is up-front engineering that amortizes.
- **B2 — Full skills inventory.** 62 skills, 21 with scripts, 44 scripts, 11,251 lines.
- **B3 — Isolation architecture in full.** One call per node; what each call receives and what it
  is denied; why guards become structural.
- **B4 — Limitations, stated plainly.** Sectarian skew (7 of 16 Geluk); praise genre yields **zero**
  reception-contested claims so the due-weight machinery is demonstrated structurally, not
  adversarially; OCR bounds everything; articles are *sic*-faithful; no public citation URLs yet;
  claim-level judgements not yet human-validated; corpus exists in two annotated copies.
- **B5 — What generalises.** Root text + commentaries + curated registry. Bodhicaryāvatāra (10
  commentaries) already prepared — and that corpus *has* real refutation exchanges, which is where
  the reception machinery gets tested properly. Same shape as Sanskrit, Pāli, classical Chinese
  scholasticism.
