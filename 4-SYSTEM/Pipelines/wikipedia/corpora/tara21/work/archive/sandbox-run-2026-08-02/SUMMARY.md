# Kangyur Wiki — Tara-21 (སྒྲོལ་མ་ཉེར་གཅིག) pipeline run

Corpus: root praise text ("The Twenty-One Praises to Tara") + 16 Tibetan commentaries you added
under `corpora/སྒྲོལ་མ་ཉེར་གཅིག/`, ingested into the `kwiki` pipeline as corpus **`tara21`**.

## What ran

1. **Ingest** — root text + 16 commentaries parsed into `source/root.md` and
   `source/commentaries/*.md`, with a 17-source registry (`sources.yaml`).
2. **`kwiki commentaries`** — headings/anchors/block-IDs stamped on all 16 commentary files
   (deterministic sub-steps only; the TOC/heading-inference sub-step needs a live Gemini call,
   which is not reachable from this environment — see note below).
3. **`kwiki align`** — deterministic root↔commentary alignment (cluster + transclusion methods).
4. **`kwiki terms`** — 3 terms seeded via the corpus's own `keyness` frequency statistics.
5. **`kwiki article`** (extract → claims → organize → draft → audit → verify) — run to
   completion for all 3 terms. **Stage 7 (verify) is the pipeline's deterministic,
   non-bypassable, character-exact quote-matching gate — all three articles passed it.**

## The 3 keywords

Selected via the repo's own `kangyur_wiki.tibetan.keyness` module (frequency-only mode,
syllable-level fallback tokenizer — no live network call needed) against the ingested
commentaries, then cross-checked for genuine cross-commentary explanatory content:

| Term | Gloss | Citations | Distinct commentaries cited |
|---|---|---|---|
| **སྒྲོལ་མ** (Dolma / Tārā) | the deity herself | 18 | 5 |
| **འཇིག་རྟེན་གསུམ** | "the three worlds" (cosmology) | 34 | 16 |
| **སྡུག་བསྔལ** | "suffering" | 29 | 10 |

Dolma (སྒྲོལ་མ) was included as requested.

## Why Claude instead of Gemini

`generativelanguage.googleapis.com` is unreachable from this sandbox (confirmed: HTTP 000 /
403 at the egress proxy) — a known, documented limitation noted in the repo's own STATE.md.
The repo ships `scripts/claude_article.py` specifically as a Claude stand-in for this case. I
used that mechanism throughout (extended with a small batch-aware driver,
`scripts/claude_extract_batch.py`, to handle multi-batch extraction, which the shipped script
didn't support). All prompt templates, schemas, claim/section/draft data structures, and the
stage-7 verification code are the repo's own, unmodified — only the "model call" step was
substituted. Each article folder's `model.json` documents this.

## What's in this package

```
tara21_articles/
  སྒྲོལ་མ/            Dolma / Tārā
  འཇིག་རྟེན་གསུམ/     the three worlds
  སྡུག་བསྔལ/          suffering
    article.wiki      the final bo.wikipedia wikitext (NOT published — no --execute was run)
    report.md          verification report (PASS + advisory warnings only, per article)
    claims.json         the atomic, per-claim evidence table backing every sentence
    sections.json        the outline the draft was built from
    draft.json            the drafted article before wikitext rendering
    audit.json             the pre-verify self-audit result
    citations.json          the rendered reference list
    extract.json              the raw extracted passages per term
    model.json                 note on the Claude-stand-in substitution
terms.yaml / ledger.json / sources.yaml   corpus-level state
```

## Not done

Nothing was published to bo.wikipedia — that requires an explicit `--execute` flag on
`kwiki publish`, which I did not invoke and was not asked to. The `commentaries` stage's
TOC/heading sub-step (needs live Gemini) also did not run; it degraded gracefully and did not
block anything downstream, since the deterministic anchor/block-ID stamping still ran fully.
