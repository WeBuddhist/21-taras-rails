---
name: claims-consolidation-bo
description: Tibetan-language variant of claims-consolidation — same pipeline, gates, and rules, but the topic page's entire analytical content (synthesis, questions, divergence discussion, coverage notes) is written in Tibetan. Output files carry the -bo suffix alongside the English pages, enabling side-by-side comparison and direct review by Tibetan-literate domain specialists.
---

# claims-consolidation-bo

**This is a delta skill.** Read and follow
[`../claims-consolidation/SKILL.md`](../claims-consolidation/SKILL.md) **in full and
in force** — its Stage 1 (per-commentary mapping), Stage 2 (question-driven
consolidation), coverage check, Rules 1–16, and both verification gates all apply
unchanged. This file specifies *only* what differs when the consolidation is written
in Tibetan. Where this file is silent, the base skill governs.

**Why a Tibetan layer exists.** The claims' textual authority is Tibetan at every
step (source segment → raw claim བོད་ཡིག). An English topic page interposes an
analysis layer that Tibetan-generating transformations must not round-trip through
(Tibetan → English gloss → new Tibetan is exactly the drift the rails prevent). A
Tibetan topic page keeps the whole chain in one language and is directly reviewable
by the tradition's own readers. The `-en`/`-bo` pairs also serve as a methodological
comparison of consolidation quality by working language.

**Vault-rule note:** `4-SYSTEM/CLAUDE.md` §10 sets English as the analysis language
of `2-RAILS/`. This skill's Tibetan pages are a human-contributor-authorized
exception (2026-08-07), scoped to `2-RAILS/Claims/<topic>-bo.md` files only.

---

## Deltas from the base skill

### 1. Output file and frontmatter

- Path: `2-RAILS/Claims/<topic-slug>-bo.md` (the English page keeps the unsuffixed
  name; do not rename it).
- Frontmatter adds two fields and localizes one:

  ```yaml
  topic: <topic-slug>-bo
  lang_tag: bo
  counterpart: 2-RAILS/Claims/<topic-slug>.md   # the English page, if it exists
  consolidation_questions:                       # the questions, in Tibetan
    - "..."
  ```

  All other fields (`spine`, `method`, `sources`, `date`, `status: draft`) as in the
  base template.

### 2. Language of content

Everything analytical is Tibetan: the synthesis statements, divergence discussions,
unique-claim summaries, question list, review-section reasons, coverage-table notes.
Three things stay Latin-script for tooling:

- claim citations — always `registered_id:claim_id`, never translated or transliterated;
- frontmatter field names and values that are paths/slugs;
- the English anchor word in each structural heading (next section).

No English glosses are added to the Tibetan content — the raw claims files already
carry English per claim. (This is deliberate: it keeps the `-bo` page a clean test
of Tibetan-language consolidation, not a bilingual hybrid.)

### 3. Structural headings — bilingual anchors

The deterministic checker (gate 1) parses pages by English anchor words. Every
structural heading is Tibetan first with the English anchor in parentheses,
verbatim as follows:

| Base-skill heading | `-bo` page heading |
|---|---|
| `## Questions asked` | `## དྲི་བ་བཏོན་པ (Questions asked)` |
| `### Consensus` | `### མཐུན་སྣང (Consensus)` |
| `### ⚑ Divergences` | `### ⚑ མི་མཐུན་པ (Divergences)` |
| `### Unique` | `### ཐུན་མིན (Unique)` |
| `## Claims reviewed, not separately cited` | `## བསྐྱར་ཞིབ་བྱས་ཀྱང་ལུང་མ་དྲངས་པ (Claims reviewed, not separately cited)` |
| `## Coverage` | `## ཁྱབ་ཚད (Coverage)` |

Facet headings (`## …`) are free Tibetan — the checker does not key on them.
Attestation count labels use Arabic numerals in the form `(འགྲེལ་པ 13)` — the
checker recomputes these exactly as it does `(13 commentaries)`.

### 4. Rules — two become easier, none are waived

- Rule 12 (verbatim quotes) now covers *all* quoted content naturally: since the
  page is Tibetan, every attested claim — Consensus, ⚑, and Unique alike — quotes
  its བོད་ཡིག inline rather than paraphrasing in English. This is the norm on `-bo`
  pages, not an option.
- Rule 14 (epistemic strength): quote the marker itself (…སྙམ་མོ etc.) instead of
  characterizing it.

### 5. Independence for comparison

When an English counterpart page exists, the `-bo` consolidator **must not read
it**. Work only from the Stage-1 packet, exactly as the English consolidator did.
Reading the counterpart would contaminate the language comparison and copy its
errors. (The two pages are compared *after* both exist — by a human or a dedicated
comparison pass — never during writing.)

### 6. Gates

Both gates apply unchanged. Gate 1 (`verify_consolidation.py`) already parses the
bilingual anchors and `(འགྲེལ་པ N)` labels. Gate 2 (`claims-consolidation-audit`)
runs identically — the auditor checks the Tibetan synthesis against the raw བོད་ཡིག,
where quote fidelity is now a character-level comparison in one language.

---

## Completion check (in addition to the base skill's)

- [ ] File at `2-RAILS/Claims/<topic-slug>-bo.md`; English counterpart untouched
- [ ] `lang_tag: bo` and `counterpart:` in frontmatter; questions in Tibetan
- [ ] All structural headings carry the exact bilingual anchors of the table above
- [ ] Analytical content is Tibetan throughout; citations stay `registered_id:claim_id`
- [ ] Every attested claim quotes its བོད་ཡིག verbatim inline
- [ ] The English counterpart was never opened during consolidation
