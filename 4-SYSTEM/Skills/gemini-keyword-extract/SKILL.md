---
name: gemini-keyword-extract
description: >
  Extract key terms directly from Tibetan blocks by sending them to Gemini in batches,
  keeping a per-block provenance map, and verifying every returned term against the
  block it was claimed from (VERBATIM / NORMALIZED / ABSENT). Then compare the result
  against `keyword-extract`'s English-mediated registry: agreement, what each route
  finds alone, and whether the provenance matches.

  Trigger on "extract keywords from the Tibetan directly", "let Gemini find the key
  terms", "compare the two keyword routes", "how good is the English-mediated keyword
  extraction", "keyword extraction without translating first".

  This is a **comparison arm**, not a replacement for `keyword-extract`. Its output
  goes to `0-INBOX/temp/`, never to `2-RAILS/Keywords/`, unless a human decides
  otherwise after reading the comparison.
---

# gemini-keyword-extract

`keyword-extract` cannot run statistics on Tibetan — tokenization is contested and no
reference corpus exists — so it detects candidates in an English translation and maps
every occurrence back to the Tibetan term it renders. That detour is well-reasoned, and
it has one unmeasured cost: **a term the English translator paraphrased away never
becomes a candidate.** The registry can only be as complete as the pivot translation's
vocabulary.

This skill measures that cost. It asks a model to read the Tibetan itself, and then
compares the two routes. It exists to answer a question — *how much does the English
detour miss, and what does it miss?* — not to replace the pipeline that survives the
answer.

| | route A — `keyword-extract` | route B — this skill |
|---|---|---|
| Reads | an English translation | the Tibetan |
| Selection | YAKE/TF-IDF, then per-occurrence mapping back | a model's judgment of what a scholar would index |
| Ranking | claim density + structure + frequency, measured on the corpus | none — it returns a set, not a ranking |
| Verifiable | yes: every occurrence maps to a block | **only if checked** — hence the grading below |
| Fails by | missing what English paraphrased away | returning a term that is not in the block |

**Neither is ground truth.** `gk_compare.py` says where they agree and what each sees
alone; it does not score one against the other, because there is no key to score against.

---

## What the first comparison found (2026-09-22, Tārā-21 root text)

32 blocks, 7 calls, `gemini-3.1-pro-preview`. Full run:
`0-INBOX/temp/keyword-extraction/gemini-direct-2026-09-22/`.

| | count |
|---|---|
| A — registry terms occurring in this text | 345 |
| B — Gemini, distinct normalised terms | 208 |
| found by both | 154 |
| only A | 191 |
| only B | 54 |
| **A's top 50 by composite rank, independently found by B** | **46/50** |
| B verification | 282 VERBATIM · 5 NORMALIZED · **0 ABSENT** |

Four findings, in order of what they settle:

1. **A's ranking is independently corroborated.** 46 of A's top 50 were found by a
   model reading the Tibetan with no access to A's English pivot, its statistics or its
   claim-density scores. The composite ranking is picking up what a reader of the source
   picks up.
2. **The two routes differ in granularity, not mostly in coverage.** 66 of the 191
   "only A" terms (35%) are a *substring of a term B did return* — A splitting a compound
   B kept whole (A has `གསེར།` "golden" and `སྔོ།` "blue"; B has `གསེར་སྔོ་` "golden-blue").
   Neither is wrong, but for a translation termbase the whole unit is the useful one.
3. **The English detour's recall gap is real and is multi-word.** 43 of the 54 "only B"
   terms (80%) are 2+ syllables: `གནོད་སྦྱིན་ཚོགས་` (host of yakṣas), `གཡས་བརྐྱང་`/`གཡོན་བསྐུམ་`
   (the leg postures), `བདུད་ཀྱི་དཔའ་བོ་` (Māra's warriors), `དེ་ཉིད་` (suchness — a doctrinal
   term, simply missing from A). This is exactly the predicted failure: a phrase English
   renders idiomatically does not survive as an English keyword, so it never becomes a
   candidate and never maps back.
4. **Zero hallucination on this corpus.** 0 of 287 returned terms were ABSENT from the
   block they were attributed to. The verification tiers still run every time — this is
   one corpus, one model, one day — but the feared failure mode did not appear.

### The registry's `root_text_blocks` field is not a reliable occurrence index

On the 55 terms where the routes disagreed about provenance, checked against the actual
text: **A had 150 block-attribution errors, B had 57.** A commonly has the right *number*
of blocks and the wrong *blocks* — the signature of provenance inherited from where the
English keyword sat, through the per-occurrence mapping, rather than read off the Tibetan.

B's near-exactness is partly by construction (it was shown the block and asked to copy
from it), so its 57 are misses rather than misattributions. But A's 150 are real.

**This does not affect the translation pipeline**, because `build_lock_glossary.py` and
`check_locks.py` compute block membership mechanically from the text and never read
`root_text_blocks`. It does mean nothing else should treat that field as an occurrence
index without recomputing it.

---

## Verification is the whole design

A model reading the source language can return a term that is not there — a citation
form it normalised, a compound it conflated, a plausible word the passage never uses.
That failure is invisible unless checked, so every returned term is checked against the
block it was attributed to:

| Grade | Means | Trust |
|---|---|---|
| **VERBATIM** | the exact string occurs in that block | usable as-is |
| **NORMALIZED** | occurs after tsheg/shad/anusvāra normalisation — a citation form | usable; record the surface form |
| **ABSENT** | does not occur in that block | **do not use without a human read** |

ABSENT terms are kept in the output and flagged, never dropped. A dropped term is an
unmeasured error rate; a flagged one is a measured one.

---

## Inputs and output

| Input | Required | Description |
|---|---|---|
| **Source** | ✓ | A block-ID'd Tibetan file. Headings and transclusions are skipped. |
| **`GEMINI_API_KEY`** | ✓ | Environment, or `--env-file`. Falls back to `4-SYSTEM/Pipelines/wikipedia/.env` and `~/.zshrc`. Never hardcoded, never printed. |
| **`--batch`** | — | Blocks per call, default 5. |
| **`--model`** | — | Default `gemini-3.1-pro-preview`. |

```
0-INBOX/temp/keyword-extraction/<run>/
├── gemini-terms.json        per-block terms + verification grade + ledger
├── comparison.json          full route A vs B diff
└── comparison.md            the readable report
```

**Output stays in `0-INBOX/temp/`.** `2-RAILS/Keywords/` is written by `keyword-extract`
and by nothing else; promoting a Gemini run into the rails is a human decision taken
after reading the comparison, not a consequence of running this skill.

---

## Rules

1. **Never write to `2-RAILS/Keywords/`.** See above.
2. **Never report a term count without its verification breakdown.** "Gemini found 200
   terms" is not a result; "180 VERBATIM, 12 NORMALIZED, 8 ABSENT" is.
3. **Compare on normalised Tibetan, never raw strings.** Route A's lemmas carry a
   trailing shad, route B copies the running form. Raw comparison reports near-total
   disagreement and means nothing.
4. **Restrict route A to terms occurring in this text** before comparing. The registry
   covers the whole corpus including the commentaries; route B only ever saw the root
   text. Comparing the full registry against it manufactures a difference that is an
   artefact of scope.
5. **A block the model does not return is reported, never silently empty.** See the
   block-id trap below.
6. **This skill ranks nothing.** It returns a set. Ranking needs the corpus-wide
   attention signals that only `keyword-extract` Phases 4–5 compute.

---

## The block-id trap

Asked to label each block with its ID, Gemini has been observed **echoing the source's
own heading label back** — given `### BLOCK 1-3` it returned `block_id: "BLOCK 1-3"` —
and the formatting is not stable run to run. In the first run of this skill, two of seven
batches returned bare IDs and five returned the prefixed form; the five were silently
recorded as empty, and the run reported 53 terms from 32 blocks while looking like it had
succeeded.

Two guards, both needed:

- The prompt delimits blocks as `<<ID>>` and states that `block_id` is the identifier
  between the brackets, with no prefix.
- `resolve_block_id()` strips decoration and then matches, **longest candidate first**,
  so `1-2` can never claim a row belonging to `1-22`. Anything still unresolvable is
  reported as `UNRESOLVED IDS`, not dropped.

The general lesson, worth carrying to any structured-output call: **a response that
parses is not a response that matched.** Schema compliance says nothing about whether
the keys mean what you asked them to mean.

---

## Procedure

```bash
# 1 — parse check, no calls
python3 4-SYSTEM/Skills/gemini-keyword-extract/scripts/gk_extract.py \
  --source "1-SOURCES/Text/<file>.md" --out /dev/null --list

# 2 — extract
python3 4-SYSTEM/Skills/gemini-keyword-extract/scripts/gk_extract.py \
  --source "1-SOURCES/Text/<file>.md" \
  --out 0-INBOX/temp/keyword-extraction/<run>/gemini-terms.json --batch 5

# 3 — compare against the English-mediated registry
python3 4-SYSTEM/Skills/gemini-keyword-extract/scripts/gk_compare.py \
  --gemini 0-INBOX/temp/keyword-extraction/<run>/gemini-terms.json \
  --source "1-SOURCES/Text/<file>.md" \
  --out 0-INBOX/temp/keyword-extraction/<run>/comparison.json \
  --md  0-INBOX/temp/keyword-extraction/<run>/comparison.md
```

Read step 2's summary before step 3. Any `MISSING BLOCKS` or `UNRESOLVED IDS` line means
the run is incomplete and the comparison will understate route B — re-run those blocks
with `--only` before comparing.

### Reading the comparison

Three numbers carry the decision, in this order:

1. **Route A's top-ranked terms that B did not find.** A miss at rank 5 matters; a miss
   at rank 300 is noise. This is the direct test of whether the composite ranking is
   picking up what a reader of the Tibetan would.
2. **Terms B found that A does not have, filtered to VERBATIM.** These are the candidate
   evidence of the English detour's recall gap. Check them by hand: a real term here is
   a finding; a particle or a fragment is route B's own noise.
3. **Provenance agreement** on the terms both found. Disagreement means one route
   attributed a term to the wrong block — check which, since A's provenance is what
   downstream lock-matching relies on.

---

## Completion check

- [ ] `--list` block count matches the source
- [ ] No `MISSING BLOCKS` / `UNRESOLVED IDS` left unresolved
- [ ] Verification breakdown reported alongside every term count
- [ ] Comparison restricted to registry terms occurring in this text
- [ ] Terms-only-in-B reviewed by hand before being called a recall gap
- [ ] Nothing written to `2-RAILS/`
