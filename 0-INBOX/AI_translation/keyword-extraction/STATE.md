# Keyword-extraction pipeline — run status

Handover note for the Tārā-21 keyword-extraction run. Read this before touching anything under
`0-INBOX/AI_translation/`. Method design lives in
[`4-SYSTEM/Guidelines/keyword-extraction-methodology.md`](../../../4-SYSTEM/Guidelines/keyword-extraction-methodology.md)
(the living doc — read it first for *why*; this file is the *what happened*). Started
2026-08-10.

---

## What this run is

Ranking the terms of the Tārā-21 root text + 16-commentary corpus to decide which subjects get
generated Wikipedia articles and in what order, per the methodology doc's 6-step pipeline:
detect candidates in English → map to Tibetan → count → score by attention → human review →
article queue. Nothing in this run writes to `2-RAILS/` or feeds the `kwiki` pipeline directly —
everything here is a working draft pending human approval (Step 6 gate).

---

## Status: pipeline complete through Step 5 — ranked list ready for human review (Step 6)

| Step | What | Output | State |
|---|---|---|---|
| 0 | Literal EN translation of the root text (Gemini zero-shot, pada-aligned, all 29 block IDs) | `../english/tara21-english-literal-keyword-zeroshot_split_chapters/` | done |
| 1 | YAKE candidate extraction, verse-scoped | `output/tara21-en-literal-*` (193 candidates) | done |
| 2 | TF-IDF vs. Reuters-21578 (secondary/complementary signal) | `output/tara21-english-literal-keyword-zeroshot-01_*`, `*-tfidf.md` (313 terms) | done |
| 3 | Per-occurrence en→bo mapping, 5 parallel agents (one per block-batch), all 29 root blocks | `output/mappings/batch1-5.json` | done |
| — | Regroup into Tibetan term registry (by Tibetan term, not English surface form) | `output/tibetan_term_registry.json` (370 unique terms) | done |
| 4 | Quote-excluded frequency count, root + 16 commentaries | `output/frequency_matrix.json` | done |
| 5B | Structural signal — TOC-tree node-title matches, all 16 commentaries | `output/signal_b_structure.json` | done |
| 5A | Claim-density tagging, 16 parallel agents (one per commentary's tree-guided claims file) | `output/signal_a/<id>.json` | done — all 16 landed (`palden-sherab`, 282 claims, needed one retry after a stall) |
| 5 | Composite score (A dominant 0.6, B secondary 0.25, C tie-breaker 0.15) | `output/ranked_keywords.json` (full, 367 terms), `output/ranked_keywords_top60.md` (review-friendly table) | **done** |
| 6 | Ranked list → human review | — | **awaiting you** — this is the stopping point; nothing downstream (terms.yaml, kwiki ledger) is touched without approval |

**Variant merge:** 370 → 367 terms after collapsing three orthographic-doublet clusters found by
scanning all terms for tsheg/whitespace-insensitive + anusvara-mark (U+0F83 ྃ ↔ U+0F7E ཾ)
equivalence: `ཧཱུྃ།`/`ཧཱུཾ།`, `ཡི་གེ་ཧཱུཾ།`/`ཡི་གེ་ཧཱུྃ།`, `ཏུ་ཏྟྭ་ར།`/`ཏུཏྟྭ་ར།` — the anusvara doublet is also
attested in the root text's own critical-edition witness apparatus (homages 5/14), so this is a
real, recognized spelling variation, not a typo.

**Result validates the design.** Before Signal A/B, raw presence-ranking put Tibetan
intensifier particles (རབ་ཏུ་, ཤིན་ཏུ་, ཉིད, མ་ལུས) in the top 20 — exactly the distortion §4.1
of the methodology doc predicts. None of them survive into the final top 60; the composite
ranking correctly promotes doctrinally substantive terms (སྒྲོལ་མ, disease/protection vocabulary
tied to the "sixteen fears" theme, iconographic details) instead. `ཕྱག་འཚལ།` ("homage" — present
in literally every stanza-opening) lands at rank 17, not rank 1, confirming attention correctly
discounts pure formula-word frequency.

---

## Decisions made / infra findings during this run

- **Frontmatter pollution caught and fixed.** The first YAKE pass ran over the translation
  file's own frontmatter (which I had added: title, purpose, skill fields) and pulled in noise
  like "zeroshot translator", "audience profile" as fake keywords. Fixed by stripping
  frontmatter before extraction (matches `keywords.py`'s own convention) and rerunning — 225 →
  193 clean candidates.
- **No transclusion anchors in the re-ingested commentaries.** All 16 files under
  `1-SOURCES/Commentaries/` carry `status: 0-raw` and zero `![[...]]` root-verse anchors — the
  `kwiki commentaries` promotion stage (headings + anchors + block IDs) has only partially run
  (headings exist via `tag-inline-toc`, anchors don't). This means Step 4's "quote-excluded"
  counting could not use the methodology doc's assumed transclusion-tag mechanism. Fallback
  implemented instead: a substring/similarity match (difflib, ≥0.8 ratio) against the actual
  root-text lines, excluding any commentary clause that closely reproduces a root pada from the
  prose count. Same purpose (kill quotation inflation), different mechanism — noted as a
  deviation from the doc's design, not a silent substitution.
- **Registry file location resolved** (doc's open question #3): the registry and all
  intermediate signal files live under `0-INBOX/AI_translation/keyword-extraction/output/` as
  working/draft output, not `2-RAILS/` — this pipeline's own product is a candidate list
  pending human review, and `2-RAILS/` requires per-claim `1-SOURCES/` citation status that a
  statistically-derived candidate list doesn't carry until approved. Once a human approves the
  top-N list, it graduates into the kwiki-consumed `3-TRANSFORMATIONS/Wikipedia/tara21/terms.yaml`.
- **Presence-signal noise confirmed as expected, not a bug.** Raw block-spread in the registry
  puts Tibetan intensifier/adverbial particles (རབ་ཏུ་, ཤིན་ཏུ་, ཉིད, མ་ལུས) near the top — exactly
  the distortion §4.1 of the methodology doc predicts (frequent everywhere, defined nowhere).
  This is why Step 5 exists; these are expected to drop once Signal A/B are folded in, not
  something Step 3 should have filtered.
- **Near-duplicate mantra-syllable spellings found in the registry**, flagged independently by
  two different Signal A agents: ཧཱུྃ vs ཧཱུཾ, ཏུཏྟྭ་ར vs ཏུ་ཏྟྭ་ར. These need merging during Step 5
  aggregation — not yet done.
- **Several claims files' own `claim_count` frontmatter undercounts** the claims actually
  present (gendun-drub: states 131, actual 136 — misses 5 ⚑ divergence entries; konchok-thabkhe:
  states 132, actual 135; anon-trinle-char: states 258, actual 260; tenzin-dhonzang: states 327,
  actual 328). Signal A agents used the real per-file count in every case; aggregation should
  too, not the frontmatter field.

---

## Known limitations, not yet addressed

- **Root-text prior not implemented.** The methodology doc calls for every content word of the
  root text to enter the registry regardless of English statistics — this would need Tibetan
  segmentation (no segmenter available/wired up here), so it wasn't done. Mitigated in part by
  the Step 0 translation being deliberately lexically complete, but not a substitute.
  Residual coverage gap unknown; not measured.
- **Local-Wiki sub-signal of Signal B skipped.** `2-RAILS/Local-Wiki/` is currently empty (wiped
  in the same Aug 4 backup that deleted the kwiki pipeline's derived artifacts — see the vault's
  main pipeline `STATE.md`), so Signal B is TOC-titles only, not TOC-titles + Local-Wiki
  definition tables as designed.
- **A/B/C composite weights are still undecided** — methodology doc's own open question, to be
  tuned on this run under human review once the ranked list exists.

---

## Next steps

1. **Human review of `output/ranked_keywords_top60.md`** — this is the Step 6 gate. Composite
   weights (0.6/0.25/0.15) are provisional per the methodology doc's own open question; sanity-
   check the ranking and adjust if a specific term's placement looks wrong before approving.
2. Once approved: promote the top-N into `3-TRANSFORMATIONS/Wikipedia/tara21/terms.yaml` with
   `status: candidate` (never auto-written by this pipeline — a deliberate human step).
3. Out of scope for this pipeline, but blocking actual article generation downstream: the kwiki
   `tara21` corpus's own `aligned.json`/`terms.yaml`/ledger were deleted in the 2026-08-04
   backup and need regenerating before any ranked term here can actually produce an article —
   see the wikipedia pipeline's own `STATE.md`.
