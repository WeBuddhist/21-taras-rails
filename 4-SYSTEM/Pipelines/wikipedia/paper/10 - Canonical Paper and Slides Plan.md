# IATS 2026 — Paper & Presentation Plan (canonical, from the lead's design session)

> **Provenance.** Designed in the team lead's claude.ai session on 2026-08-01
> (<https://claude.ai/share/dbdee4e9-5786-4672-9119-51ea1786cd05>) around the submitted abstract
> ([[abstract]]) and the canonical 17-step pipeline
> (`docs/reference/cowork-pipeline.md`). The share snapshot preserves the first version verbatim
> plus the full description of the one revision round (the Tibetan-Wikipedia revival story and
> the critical-mass argument, added as §3 and slides 3–4). This file is the reconstruction of
> the final state; the slide re-timing after the two inserted slides is this repo's editorial
> reconstruction and is marked as such. Where this plan and the earlier working notes
> ([[01 - Paper Argument and Structure]], [[08 - Presentation and Demo Plan]]) disagree, **this
> plan takes precedence** — it is the later design; the working notes keep their value for
> verified facts, policy detail, and the offline-demo logistics.

Audience assumption: IATS is philologists, historians, and buddhologists first, digital
humanists second, NLP people a distant third. They know the 21 Taras Praise intimately; they are
professionally skeptical of AI-generated text. The paper and talk should win them by showing
that the pipeline **encodes their own scholarly values** — attribution, editions, sectarian
balance, verifiability — as hard constraints.

---

## Part 1 — Paper structure (~8,000–10,000 words)

### 1. Introduction (~800 w)
The digital footprint gap with concrete numbers: bo.wikipedia article count vs. comparable
languages; Tibetan's share in LLM training corpora; the consequence (AI systems that cannot
answer basic questions about Tibetan culture from Tibetan sources). State the cyclical thesis
from the abstract. One paragraph announcing the case study: the Praise to the Twenty-One Taras
with 16 commentaries — a deliberately familiar text, so readers can judge output quality
themselves.

### 2. Related work (~900 w)
Three strands: (a) Tibetan digital infrastructure — BDRC, OpenPecha, ACIP, Adarsha, THL,
Lotsawa House; position the pipeline as consuming this infrastructure, not duplicating it.
(b) Wikipedia and under-resourced languages — small-wiki growth efforts and, honestly, the
failures: incidents of mass machine-generated content degrading small Wikipedias. Naming the
failure mode early buys credibility for your safeguards. (c) LLM-assisted encyclopedic writing
and its known risks (hallucination, citation fabrication, close paraphrase).

### 3. Reviving Tibetan Wikipedia: the critical-mass argument (~900 w) — added in revision
Our own revival campaigns as data, told in first person: workshops run, editors trained,
retention curves, articles per year (reconstruct from public bo.wiki edit histories where
internal records are thin). Then the argument, structured as a **trilemma, not an assertion**:

1. *Manual-only* — we tried it, we measured it, it does not scale;
2. *Unsupervised automation* — demonstrably degraded other small wikis;
3. *Supervised automation* — this pipeline.

That framing does double duty: it makes "automation is the only way" defensible, and it turns
the ethics safeguards from an apology into the third horn of the argument. In print, phrase the
claim as **"no demonstrated alternative reaches critical mass within a generation"** — save the
punchy version for the podium, backed by arithmetic. The one number that carries the whole
claim: **reviewer-hours per audit-passed article versus historical editor-hours per article,
projected to a target encyclopedia size** — "generations" collapsing to "years". Get it from
the Tara run before writing anything else; without it the argument is rhetoric, with it a
finding (reported in §8, shown on slide 13).

### 4. Corpus and case study (~800 w)
The root text; the 16 commentaries as a table: author, dates, school, edition, BDRC ID,
copyright status. Describe the verse-by-verse alignment and edition-aware stable IDs. Note the
corpus's school composition explicitly — this feeds §6.

### 5. Pipeline architecture (~2,000 w) — the core section
Present the four layers with the pipeline diagram. Give most space to the ideas that
distinguish this from naive LLM generation:
- **Atomic claims as the copyright/hallucination firewall**: sources → claims table (in
  Tibetan, one fact per row, locator, commentator/school) → drafting from claims only, passages
  closed. Two invariants stated as such.
- **Claim typing**: consensus / majority-with-dissent / school-position / single-commentator,
  and the voice rules each type triggers.
- **Dual-model division of labor**: Claude for extraction, claims, and audit (reading-strength
  tasks); Gemini for literary Tibetan generation; the sentence-level audit against the claims
  table as the loop-closer. Include one real audit-table excerpt.
- **Execution model**: Claude Cowork, one skill per step, immutable per-stage outputs, feedback
  loop patching the causal stage's prompt. Deterministic work in three scripts (BDRC metadata
  fetch, Gemini API, MediaWiki/Wikidata publishing). *(In this repo: `kwiki`'s deterministic
  verify gate additionally re-reads every quotation character-for-character — say so; it is the
  strongest trust card.)*

### 6. Weighting doctrine (~1,000 w) — the section this audience will cite
Breadth decides which concepts get articles; **reception decides the weight of positions**.
Argue that Tibetan polemical culture left a machine-readable reception record: citation and
refutation (dgag lan) patterns across commentaries. The pipeline reads that record — a position
that drew rebuttals has proven weight; an unengaged idiosyncrasy gets a sentence. Add the
normalization argument: a sole corpus representative of a school is a school-position, never
fringe (the Zhentong example). Frame this as **operationalizing traditional Tibetan
intellectual history as an editorial policy** — that framing turns an NLP paper into a Tibetan
studies paper.

### 7. Publication and data model (~700 w)
Frontmatter as canonical record; copyright routing (PD → Wikisource with verse anchors;
copyrighted → BDRC/WeBuddhist links); the Wikidata round-trip for works, authors, and concepts.
Point out the by-product: every article leaves behind structured, queryable metadata and a
verse-aligned corpus.

### 8. Evaluation (~1,200 w)
The abstract promises evaluation of early outputs — make it concrete from the 21 Taras run:
- **The lead metric** (from §3): reviewer-hours per audit-passed article vs. historical
  editor-hours per article, projected to a target encyclopedia size.
- **Pipeline statistics**: concepts selected (and rejected, with reasons), claims extracted,
  claim-type distribution, audit findings per stage and per severity, iterations to "publish"
  verdict.
- **Citation verifiability**: sample of refs checked end-to-end (ref → anchor → passage
  supports claim). Report the rate. *(This repo automates the strongest form: the deterministic
  gate's character-for-character quotation check — report its pass rate over repeated runs,
  never a single run.)*
- **Expert review**: 2–3 traditional scholars and/or academic Tibetologists rate a sample of
  articles on factual accuracy, attribution correctness, and register — this is the number the
  room will trust most.
- **Attribution integrity**: rate of sub-consensus claims correctly attributed in the final
  text (the audit's blocking category).
- **Community reception**: what happened on bo.wikipedia after paced publication (edits,
  talk-page response, deletions).
Report failures honestly — a table of representative audit catches (Gemini adding facts,
dropped qualifiers) *demonstrates* the safeguards working.

### 9. Discussion (~900 w)
Ethics of AI content on small wikis and your answer (disclosure, pacing, audit gate, human
editorial responsibility). Limitations: corpus sectarian skew, OCR dependence, model asymmetry
in Tibetan, evaluation scale. Generalization: hundreds of texts next; the architecture
transfers to any commentarial tradition (Sanskrit, Pali, classical Chinese) and to other
under-resourced languages with layered textual canons.

### 10. Conclusion (~400 w)
Return to the cycle: articles → footprint → training data → better tools → faster articles.
The deeper deliverable: not N articles but a **reusable editorial machine plus a growing claims
database** that is itself a research artifact for Tibetan studies.

---

## Part 2 — Slides (20 minutes; two revival slides inserted early; re-timing below is
editorial reconstruction — rebalance in rehearsal)

| # | Slide | Time | Content / speaker note |
|---|-------|------|------------------------|
| 1 | Title | 0:30 | Title, OpenPecha, one-line thesis. |
| 2 | The gap | 1:30 | Two or three stark numbers: bo.wiki vs. peer-language article counts; Tibetan share of LLM training data. "Ask an AI chatbot about a Tibetan topic in Tibetan — show what happens." |
| 3 | Our revival campaigns | 1:30 | **First person: "we ran these."** Workshops, editors trained, retention curves, articles per year. The standing matters: the claim lands differently coming from people who did the volunteer work. |
| 4 | The trilemma | 1:30 | Manual-only (measured, doesn't scale) / unsupervised automation (degraded other small wikis) / supervised automation (this pipeline). "No demonstrated alternative reaches critical mass within a generation." |
| 5 | The cycle | 0:45 | One circular diagram: content → footprint → NLP tools → faster content. This is the argument; everything after is mechanism. |
| 6 | Case study | 1:15 | 21 Taras Praise + 16 commentaries as a visual network (root text center, commentaries around it, colored by school). The room knows this text — that's the point: "you can check our output." |
| 7 | Pipeline overview | 2:00 | The four-layer diagram, one pass, no detail. Flag the two invariants in red: *no source wording past the claims stage; nothing publishes without surviving audit.* |
| 8 | Verse alignment & stable IDs | 1:00 | Screenshot of the alignment table; one ID anatomized (edition–text–chapter–verse) → same ID as a Wikisource anchor. |
| 9 | Atomic claims | 2:00 | One real row of the claims table (Tibetan claim, locator, school, type, reception). "The draft is written from *this*, with the sources closed." |
| 10 | Weighting: breadth vs. reception | 2:00 | **The slide for this room.** Two claims from the corpus: one held by many minor voices, one by a single major figure who drew a dgag lan — show the pipeline weighting the second higher. "Tibetan polemics as machine-readable due-weight policy." |
| 11 | Two models, one loop | 1:15 | Claude extracts & audits; Gemini writes literary Tibetan; the audit table catching a real Gemini-added fact. "The stylist is never trusted; the auditor never writes." |
| 12 | Demo | 2:30 | Pre-recorded 90-second screen capture (never live): concept → claims → draft → audit → published article with a ref resolving to a Wikisource verse anchor. End on the live bo.wiki URL + QR code. |
| 13 | Early results & the number | 2:00 | The §8 table compactly, **led by reviewer-hours vs. editor-hours projected to target size** — "generations" collapsing to "years". One honest failure example. |
| 14 | Ethics & limits | 1:00 | Small-wiki AI incidents in one line → your safeguards in three (disclosure, pacing, audit gate). Preempt the hardest question before it's asked. |
| 15 | Scaling | 0:45 | Hundreds of texts queued; per-step skills = the pipeline improves with every article; what the claims database becomes at scale. |
| 16 | Takeaway | 0:30 | The cycle diagram again + "the by-product is a research corpus" + QR to demo article, code, and paper. |

**Total: ~18:00**, leaving buffer. **Trim order if squeezed: slide 2, then 8 — never 3, 4, or
13**: they are an inseparable unit (claim, mechanism, proof).

---

## Part 3 — Preparation notes

- **Run the full pipeline on 3–5 concepts from the Tara corpus before writing anything.** The
  evaluation section and slides 9–13 all consume real artifacts from that run. The talk stands
  on one published, verifiable article more than on any diagram. *(Three verified Gemini
  articles exist as of 2026-08-01 — see `corpora/tara21/INGEST_REPORT.md` — but they predate
  the claims/audit stages; re-run them through the full chain for the artifacts.)*
- **Pick demo concepts the room can adjudicate**: e.g., a Tara-specific term treated
  differently across schools — it exercises the attribution machinery visibly.
- **Screenshots and recordings only; no live demo.** Conference wifi and login walls kill
  talks. (Logistics detail in [[08 - Presentation and Demo Plan]].)
- **Prepare for three predictable questions**: (1) "How do you know the LLM isn't
  hallucinating?" → claims-only drafting + audit table + the deterministic quotation gate +
  expert-review numbers. (2) "What does the bo.wiki community think?" → paced rollout +
  disclosure page + whatever reception data exists by then. (3) "Why should scholars trust
  machine-attributed positions?" → every claim carries a locator; verification is one click;
  show it.
- **Cite the by-products as contributions**: verse-aligned commentary corpus + claims database,
  citable datasets independent of Wikipedia. For IATS, that may be the headline.
- **Reconstruct the revival-campaign numbers early** — public bo.wiki edit histories if
  internal records are thin. Slides 3 and 13 both die without them.
- Check the panel's exact format: some IATS panels are 20 min + 10 Q&A, some 15+5. The trim
  order above protects the argument's spine.
