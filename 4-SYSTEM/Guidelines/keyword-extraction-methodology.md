# Keyword-extraction methodology — selecting article subjects from the root text

**Status: living draft** — this document records the method as decided so far and is updated
as the discussion continues. Decisions made by the human contributor in discussion with the
agent, 2026-08-05 onward.

**Companions:** [`claims-methodology.md`](claims-methodology.md) (extraction + question-driven
consolidation — governs the topic space); the kwiki pipeline's key-term stage
(`../Pipelines/wikipedia/`) is the intended consumer of the ranked list.

---

## 1. Purpose and scope

Rank the terms of the root text and its commentary corpus by importance, to decide **which
subjects get generated articles and in what order**. Articles are generated from consolidated
claims pages (`2-RAILS/Claims/<topic>.md`), citation chain intact.

Boundary rule: **keywords select and order publication; they never define the consolidation
topic space.** Consolidation coverage comes from the spine grid + claim-derived questions
(claims-methodology §4). A keyword list must not narrow what gets consolidated — otherwise
claims answering unasked questions silently vanish. The reverse check is a finding: a
high-keyness term with no claims bucket means either extraction missed something or the term
is root-text poetic vocabulary better served by Local-Wiki/glossary than a claims article.

---

## 2. Core design: detect in English, measure in Tibetan

Tibetan has no word boundaries (tsheg separates syllables), so statistical keyword tools
cannot run on it directly without a segmenter (botok etc.). The workaround:

- **English side (Steps 1–2):** tokenization and candidate detection are free in English.
  TF-IDF/YAKE on a block-aligned English translation discovers *what the candidate terms
  are*. English scores are recall-oriented candidate generation only — never the ranking.
- **Mapping (Step 3):** block alignment converts English candidates into a **Tibetan term
  registry** — the term list that seemed to be missing is created by this step.
- **Tibetan side (Steps 4–5):** counting a *known* string needs no segmentation (plain
  string matching); all measuring and ranking happens on the Tibetan side, where the truth
  lives.

Why not score in English: statistics on a translation measure the translator's vocabulary.
One Tibetan term splits across renderings (ཡེ་ཤེས་ → "wisdom" / "gnosis" / "pristine
awareness" — count divided, rank sinks) and different terms collapse into one English word
("wisdom" ← ཤེས་རབ་ and ཡེ་ཤེས་ — merged count belonging to no single term). Mapping per
occurrence, then regrouping by Tibetan term, fixes both.

A deliberately literal generated translation serves this purpose better than a published
poetic one — free translations paraphrase, and a keyword absent in English ≠ absent in
Tibetan.

---

## 3. The pipeline

```
English translation ──YAKE/TF-IDF──▶ English candidates ──block alignment──▶ Tibetan term
registry ──quote-excluded counts──▶ frequency matrix ──composite scoring──▶ ranked keywords
──human review──▶ article queue (kwiki key-term stage)
```

### Step 0 — Inputs (all existing vault artifacts)

- Tibetan root text with block IDs (`1-SOURCES/Text/`)
- Block-aligned English translation (its `^2` translates Tibetan `^2`)
- The 16 segmented commentaries, with root-text quotes transcluded/tagged
- Claims files (`2-RAILS/Claims/raw/tree-guided/`), TOC trees
  (`2-RAILS/Sections/Raw/toc-tree/`), Local-Wiki, bilingual glossaries

### Step 1 — English candidate extraction (recall, not ranking)

Run TF-IDF and YAKE over the English translation, treating **each verse as one document**
(this makes IDF punish words that recur in every verse — similes' "like", the "homage"
formula). Keep a generous pool (top ~100–200). A wrong candidate costs nothing (filtered in
Steps 3/5); a missed candidate is gone forever. Extend the stopword list with domain formula
words as they are noticed.

### Step 2 — Locate occurrences (English side)

Plain string search: for each candidate, record the block IDs where it occurs
(`"autumn moon" → ^2`; `"wisdom" → ^4, ^21`).

### Step 3 — Map each occurrence to its Tibetan term; build the registry

For each occurrence, open the same-numbered Tibetan block and identify the span the English
word translates (the `english-keyword-extraction` skill / interlinear-gloss rails do this
en↔bo pairing). Mapping is **per occurrence**, which is what resolves both distortions:

```
"autumn moon" in ^2  → སྟོན་ཀའི་ཟླ་བ་
"wisdom"      in ^4  → ཡེ་ཤེས་
"wisdom"      in ^21 → ཤེས་རབ་   ← same English word, different Tibetan term (split)
"gnosis"      in ^15 → ཡེ་ཤེས་   ← different English word, same Tibetan term (merge)
```

Regroup **by Tibetan term**. Drop candidates that resolve to grammatical particles
(ལྟ་བུ་, བཞིན་…) — first filter against function words. Add to each term's row: spelling
variants, attested synonyms (from Local-Wiki sense articles, bilingual glossaries, and the
claims themselves), and epithet forms. The result is the **Tibetan term registry** — the
keyword list plus its variant/synonym sets.

Root-text prior: every content word of the root text enters the registry regardless of
English statistics.

### Step 4 — Count on the Tibetan side (presence signal)

For each registry term (including its variants/synonyms), count occurrences by plain string
matching across the root text and each commentary — **in the commentary's own prose only,
excluding root-text quotes and transclusions** (machine-identifiable from the ingest
pipeline's transclusion/quote tagging). Output: a frequency matrix — rows = terms, columns =
root + 16 commentaries, plus a spread column (how many commentaries use the term at all).

### Step 5 — Composite scoring: attention beats presence

Three signal classes, in order of weight:

| Class | Signal | Source | Robust against |
|---|---|---|---|
| **A. Attention** (dominant) | claim density: how many claims are *about* the term, and across how many commentaries | `Claims/raw/tree-guided/` | paraphrase, synonyms, quotation inflation — extraction was semantic, per TOC node |
| **B. Structure** | term appears in TOC-tree node titles; commentaries explicitly define it | `Sections/Raw/toc-tree/`, Local-Wiki, term-definition tables | function words (present everywhere, defined nowhere) |
| **C. Presence** (weakest — sanity check / tie-breaker) | quote-excluded frequency × spread | Step 4 matrix | — (this is the signal the distortions attack; never the arbiter) |

Rationale: raw frequency + spread alone cannot separate ལྟ་བུ་ ("like", in every commentary)
from ཡེ་ཤེས་ — both are frequent and widespread. Only attention signals separate them: no
commentary defines ལྟ་བུ་, no TOC node is titled by it, no claim is about it. Weights of
A/B/C: to be tuned on the Tārā-21 run under human review.

### Step 6 — Ranked list → human review → article queue

Top-N terms pass a human review gate, then feed the kwiki key-term stage. Each article is
generated from its consolidated `Claims/<topic>.md` page, citing claim IDs, which cite
`1-SOURCES/` segments.

**The cutoff is mechanical, not judgmental (article-viability gate v1).** N is never chosen by
feel or per-run taste; a term enters the article queue iff the corpus demonstrably contains
enough claim-attention to support a cited article about it:

- **spread ≥ ⌈number of commentaries / 2⌉** — at least half the corpus's commentaries have
  claims substantively about the term. Anchors the queue in majority attention (an article
  needs due-weight structure across multiple independent secondary sources), and scales
  automatically to any corpus size.
- **claim count ≥ 20** (raw, corpus-wide) — the article-material floor. Claims-only drafting
  means the drafter has nothing but claims; consolidation collapses many raw claims into one
  cited statement (16 commentaries saying the same thing → one consensus sentence), so raw
  count must substantially exceed the final article's cited-statement count. 20 raw claims ≈ a
  lead plus two-to-three cited sections after shrinkage. This constant is *calibrated once and
  frozen* — the value of the rule is reproducibility, and sensitivity analysis on the Tārā-21
  run shows the neighborhood is stable (M=15 → 139 terms, M=20 → 114, M=30 → 63; spread ≥ 8
  vs ≥ 2 changes the count by under 6% at these M).

Selection is by the gate; *ordering* within the queue is by composite score. Terms failing the
gate are not deleted — they remain in the registry as Local-Wiki/glossary candidates per the
boundary rule (§1). The human review that remains is a *veto and reorder* pass over a
mechanically-produced queue, not a cutoff decision.

**Review point moved (2026-08-12):** there is no longer a human review between Step 6 and the
downstream stages. Steps 7–8 and article generation run without intermediate gates; the single
human review happens **at the end, over the finished articles**, before anything is published.
Consequence: every judgment step must leave a full audit trail (per-term verdicts with reasons,
merge mappings, citations) so the end review can reject selectively instead of rerunning the
pipeline.

### Step 7 — Subject filter and merge (article-worthiness) — decided, not yet implemented

The gate (Step 6) answers "is there enough claim material?"; Step 7 answers "is this an
encyclopedic *subject*?" A skill classifies every queue term three ways, with a one-line reason
per verdict — never a silent drop:

1. **Standalone subject** — gets its own article.
2. **Section material** — not a subject (body parts, directions: ཞལ, ཞབས, གཡས/གཡོན, མཐིལ…);
   its claims are routed to a named target article's section (mostly Tārā-article iconography).
3. **Glossary/Local-Wiki only** — stays in the registry per the boundary rule (§1).

The same pass performs **subject-normalization**: near-duplicate rows that string-level variant
merging cannot catch (དགྲ/དགྲ་བོ/དགྲ་ཡི; ཕྱག་འཚལ/ཕྱག་འཚལ་བ; ཧཱུྃ/ཡི་གེ་ཧཱུཾ; ཏཱ་ར/ཏུ་ཏྟྭ་ར/ཏཱ་ར་གཉིས་བརྗོད)
merge into one subject with pooled claims. Output is a new file alongside the queue
(`article_subjects`); all prior step outputs are preserved unchanged.

### Step 8 — Existing-article inventory (bo.wikipedia + Wikidata) — decided, not yet implemented

For each Step-7 standalone subject, a skill determines whether a bo.wikipedia article already
exists, via **two mechanisms**: (a) MediaWiki API search using the term *plus its registry
variant/synonym set*; (b) **Wikidata QID resolution** — find the subject's item and check its
bo.wikipedia sitelink, catching articles under unguessable titles. Saved per term: exists y/n,
title, URL, QID, length, section list, stub-or-substantial judgment, and a dated wikitext
snapshot. The snapshot is planning context only — at generation time the live article is
re-fetched. The per-subject `action: create | update` lives in `wiki-inventory.yaml`
(`terms.yaml` keeps the kwiki loader's minimal schema — `term`/`editor`/`status`/
`wikipedia_url` — where a null URL *is* the create signal, matching kwiki's own red-link
convention; merge routing is Step 7's `article_subjects` output, not a `terms.yaml` field).
Editorial rule (decided with the human contributor, 2026-08-12): one subject =
one article — existing articles are **updated/appended with cited sections**, never forked into
"X (according to the 21-Tārā commentaries)" pages; the 21 Tārās follow hub-and-spoke (main
Tārā article + text article as hubs, one article per Tārā as spokes).

---

## 4. Known distortions and their mitigations

### 4.1 English function/formula words ("like" in similes, the homage formula)

High raw frequency in both root and commentaries. Three nets, in order:
(1) verse-as-document IDF + stoplists (Step 1); (2) mapping filter — candidates resolving to
grammatical particles are dropped (Step 3); (3) decisive: attention signals (Step 5A/B) —
function words are *present* everywhere but *receive attention* nowhere.

### 4.2 Quotation inflation

Two shapes: the commentary quotes the verse then comments on only one word of it; or quotes
the verse (keyword included) but comments on the whole verse, not the word. Both inflate
every quoted word's count. Mitigation: Step 4 counts commentary **prose only** — quotes and
transclusions are excluded mechanically; and Step 5A measures what passages are *about*, not
which words they contain.

### 4.3 Paraphrase (concept discussed, word absent)

String counting undercounts by design and cannot be patched at the string level. Covered
because the tree-guided claims extraction read those passages with a model: a claim about
ཡེ་ཤེས་ phrased entirely in paraphrase still registers as attention to ཡེ་ཤེས་.

### 4.4 Synonyms (commentary uses a synonym for the root's keyword)

Partially fixed at the string level — attested synonym sets from Local-Wiki/glossaries are
counted into the term's row (Step 3) — and fully covered at the attention level (Step 5A),
which is surface-form-independent.

---

## 5. Open questions

- Reference corpus for proper cross-corpus keyness (matters more for larger corpora, e.g.
  Bodhicaryāvatāra; for Tārā-21 the commentary-spread signal substitutes).
- Document unit for TF-IDF when English translations of commentaries don't exist (current
  answer: verse-as-document over the root translation only; commentary evidence enters via
  signals A–C, not via English statistics).
- Where the term registry file lives (`2-RAILS/`? kwiki `corpora/tara21/`?) and its schema.
- Composite-score weights — tune on the Tārā-21 run, human-reviewed.

---

## Changelog

- **2026-08-12** — Post-queue design decided in discussion (not yet implemented): **Step 7**
  (subject filter: three-way verdict standalone/section-material/glossary + subject-normalization
  merge, reasons recorded per term) and **Step 8** (existing-article inventory via MediaWiki
  search + Wikidata QID sitelinks, feeding a per-term `action:` field). **Human review moved to
  the end** — one review over finished articles before publishing, no intermediate gates; audit
  trails at every judgment step replace them. Editorial rules fixed: one subject = one article
  (update, never fork); hub-and-spoke for the 21 Tārās. Artifact homes per rails docs: keyword
  working outputs stay in `0-INBOX/AI_translation/keyword-extraction/output/`; consolidated
  per-subject claims pages go to `2-RAILS/Claims/`; `terms.yaml`, wiki snapshots, drafts, and
  review records go to `3-TRANSFORMATIONS/Wikipedia/tara21/`. Publishing itself stays behind the
  explicit human gate (`kwiki publish --execute`).
- **2026-08-10 (second entry)** — **Article-viability gate v1 added to Step 6**: the cutoff is
  now a mechanical rule (spread ≥ ⌈commentaries/2⌉ AND raw claims ≥ 20; selection by gate,
  ordering by composite; gate-failures remain as Local-Wiki/glossary candidates), replacing
  per-run human N-picking after the human contributor asked for a reasoned, repeatable cutoff.
  Rationale: an article is drafted from claims only, so the only defensible cutoff is whether
  the corpus contains enough claim-attention to support a cited article. Applied to Tārā-21:
  114 of 367 terms pass; the gate agrees with the composite ordering (only 2 of the composite
  top-40 fail, both at 18–19 claims). Independent sanity checks: 114 ≈ the superseded
  translation-mediated route's human-era list (105 candidates / 96 distinct terms) and ≈ 4
  terms per root block. Output: `0-INBOX/AI_translation/keyword-extraction/output/article_queue.{json,md}`.
- **2026-08-10** — Full pipeline (Steps 1–5) run to completion for Tārā-21, using parallel
  subagents for the semantic steps (5 agents for Step 3 en→bo mapping, 16 agents — one per
  commentary — for Step 5A claim-density tagging) and deterministic scripts for the mechanical
  steps (YAKE/TF-IDF, Step 4 counting, Step 5B TOC matching). Run log and decisions:
  `0-INBOX/AI_translation/keyword-extraction/STATE.md`. Key resolutions to this doc's open
  questions:
  - **Registry location (open question, §5):** resolved as `0-INBOX/AI_translation/
    keyword-extraction/output/` — working/draft output pending human review, not `2-RAILS/`
    (which requires per-claim cited status this candidate list doesn't have yet). Promotes to
    `3-TRANSFORMATIONS/Wikipedia/<corpus>/terms.yaml` only after human approval.
  - **Composite weights (open question, §5):** used A 0.6 / B 0.25 / C 0.15 as a first pass
    (min-max normalized per signal, each signal itself an average of a count- and a
    spread-subcomponent) — provisional, pending human sanity-check of the resulting ranking.
  - **Transclusion-anchor assumption broken:** Step 4's design assumed root-verse quotes are
    machine-identifiable via ingest-pipeline transclusion tags. The commentaries in this vault
    (re-ingested 2026-08-05–08) don't have those yet (`status: 0-raw`, 0 anchors). Substituted a
    similarity-based quote detector (difflib, ≥0.8 ratio against actual root-text lines) —
    same purpose, different mechanism. Revisit once `kwiki commentaries` promotion actually runs.
  - **Result validates the attention-beats-presence design**: pre-Signal-A/B, raw presence
    ranking put Tibetan intensifier particles (རབ་ཏུ་, ཤིན་ཏུ་, ཉིད, མ་ལུས) in the top 20 —
    exactly the §4.1 distortion. None survive into the final top 60 once claim-density and
    structure are folded in; formula word ཕྱག་འཚལ་ ("homage," in every stanza) lands at rank 17,
    not rank 1. First empirical confirmation the design does what it was meant to.
  - **Orthographic-variant merging needed and not previously specified**: added a
    tsheg/whitespace-insensitive + Sanskrit-anusvara-mark (U+0F83 ↔ U+0F7E) equivalence pass
    before final ranking, catching 3 doublet clusters (e.g. ཧཱུྃ།/ཧཱུཾ།) that two independent
    Signal-A agents flagged independently. Should be folded into Step 3's registry-build going
    forward rather than left to a late merge pass.
- **2026-08-09** — Step 0 input generated: literal English translation of the root text
  (critical edition, post-2026-08-07 resegmentation) via `zeroshot-translator` on
  gemini-3.5-flash, pada-aligned, all 29 block IDs preserved. Lives at
  `0-INBOX/AI_translation/english/tara21-english-literal-keyword-zeroshot_split_chapters/`
  with purpose-built audience profile `literal-keyword`. Working aid for Steps 1–3 only —
  not a vault translation track.
- **2026-08-05** — Initial draft from discussion: detect-in-English / measure-in-Tibetan
  design, 6-step pipeline with worked example, the four commentary-distortion cases and the
  attention-beats-presence scoring reframe (claim density dominant, quote-excluded counts
  demoted to tie-breaker), root-text prior, boundary rule vs. consolidation coverage.
