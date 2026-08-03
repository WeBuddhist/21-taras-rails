---
name: english-keyword-extraction
description: >
  Extract ranked keywords per verse from an ENGLISH translation of a Tibetan
  root text (YAKE + spaCy, optional TF-IDF report against a general-English
  IDF corpus), then enrich each English keyword with its contextually correct
  Tibetan equivalent — producing a bilingual en↔bo key-term list keyed by
  verse block ID (^chapter-verse). This is the translation-mediated route to
  key terms: when the Tibetan-only prompt (prompts/03-terms) over-returns or
  fragments, run the extraction on an English translation instead, where
  keyword statistics are well-conditioned, and map the results back to
  Tibetan.

  Trigger this skill when the user wants key terms / keywords extracted via
  an English translation, a bilingual term list, or Tibetan equivalents for
  English keywords ("extract keywords from the translation", "enrich keywords
  with Tibetan", "build the en-bo term list").
---

# english-keyword-extraction

Keyword statistics behave badly on classical Tibetan directly: tokenization is
contested, no standard reference corpus exists (open-questions.md Q7), and the
team's Tibetan-only prompt (forum topic 289) is documented to over-return
phrase fragments. This skill routes around all three problems by extracting
keywords from an **English translation** — where YAKE/TF-IDF are
well-conditioned — and then mapping each keyword back to the Tibetan term it
renders, verse by verse.

If the corpus has no English translation yet, produce one first with
`4-SYSTEM/Skills/zeroshot-translator/` (block-ID-preserving), or use any
existing published translation whose verses carry `^chapter-verse` IDs.

## Pipeline

### Step 1 — extract keywords per verse (deterministic)

```bash
python3 scripts/keywords.py --input <en-translation>.md --output <out>/verse_keywords.json
```

`keywords.py` (YAKE + spaCy noun-phrase filtering) reads a block-ID'd English
translation and writes `{verse_id: {text, keywords: [{key, rank, score,
count}]}}`. Requires `pip install yake spacy` + the `en_core_web_sm` model
(see `scripts/requirements.txt`).

### Step 2 (optional) — corpus-level TF-IDF report

```bash
python3 scripts/generate_en_translation_idf.py
```

Ranks terms across the whole translation against the bundled Reuters-21578
general-English IDF table (`scripts/idf_corpus.py`, regenerable with
`scripts/generate_idf_corpus.py`). Use this to pick the corpus-level top-N
key terms rather than per-verse ones.

### Step 3 — enrich with Tibetan equivalents

Two routes; prefer (a) in a Claude session:

**(a) No API — Claude does it directly.** For each verse's keywords, add a
`"bo"` field with the Tibetan term that the English keyword *renders in that
verse* — the contextually correct term, not a dictionary lookup. Consult the
aligned Tibetan verse (same `^chapter-verse` ID in the root text) to see which
Tibetan word the translator was rendering. Write the enriched JSON alongside
the input with suffix `_en_bo_keyword_meaning_enriched.json`. Checkpoint
every 50 verses. Report totals and gaps when done.

**(b) Batch via Gemini** (reads `GEMINI_API_KEY` from the environment,
never hardcoded):

```bash
python3 scripts/enrich_en_bo_keyword_meaning.py --input <out>/verse_keywords.json
```

## Output contract

```json
{
  "1-1": {
    "text": "English verse text",
    "keywords": [
      {"key": "bodhisattva", "rank": 1, "score": 0.001, "count": 2, "bo": "བྱང་ཆུབ་སེམས་དཔའ།"}
    ]
  }
}
```

- Verse keys are the root text's `^chapter-verse` block IDs — the same IDs the
  aligner uses, so a keyword's commentary spans are one `spans_for_term` call
  away.
- Every `bo` value ends with a shad `།` (matching the team's term-list
  convention from forum topic 289).
- The Tibetan term must actually occur in the Tibetan verse (or be its
  standard citation form) — if uncertain, use the closest established term
  and note it in a `"note"` field rather than silently guessing.

## Feeding the article pipeline

The enriched list is a *candidate* term list. To use it for a corpus:

1. Aggregate `bo` terms across verses; rank by count and per-verse rank.
2. Intersect with the curated registry (`corpora/<id>/terms.yaml`) if one
   exists; otherwise propose the top terms for human review — the human
   approves the list before extraction runs (PLAN.md §3, stage 3).
3. Never auto-seed the ledger from this output without review.

## Provenance

Ported 2026-08-01 from
`bodhisattvacharyavatara-rails/4-SYSTEM/scripts/english_keyword/`
(scripts verbatim: `keywords.py`, `generate_en_translation_idf.py`,
`generate_idf_corpus.py`, `enrich_en_bo_keyword_meaning.py`, `idf_corpus.py`,
`requirements.txt`; the BCA-specific `output/` runs and the redundant
`idf_corpus.pkl` were not carried over). Step 3(a) is the API-free
`bo-keyword-enrich-simple.skill` bundled in the same directory, inlined here.
The source pipeline is documented end-to-end in that repo's
`4-SYSTEM/bca-translation-pipeline.md` and was run in production on the BCA
with the David Karma Choephel translation.
