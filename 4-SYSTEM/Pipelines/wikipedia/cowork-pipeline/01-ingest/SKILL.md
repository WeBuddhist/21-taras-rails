---
name: 01-ingest
description: "Pipeline step 1 — Ingest & provenance for the Tibetan Buddhist texts → Wikipedia pipeline. Creates the canonical text note (texts/<text-id>.md) with fully-filled YAML frontmatter from BDRC metadata. Use whenever a new root text, commentary, or e-text is added to the vault, whenever the user says 'ingest', 'add this text', 'create the text note', or mentions a BDRC work/scan ID that has no note yet."
---

# Step 1 — Ingest & provenance

Turn a source e-text into a vault note whose **YAML frontmatter is the canonical metadata record** for the whole pipeline. Every downstream stage reads from it; step 15 pushes it to Wikidata.

## Inputs
- Source e-text file (BDRC-sourced OCR): root text, commentary, subcommentary, or refutation
- BDRC work/scan ID

## Outputs
- `texts/{{TEXT_ID}}.md` — frontmatter per the canonical schema + a 3–5 line prose note

## Script
Run **`scripts/bdrc_fetch.py`** *first*. Given the BDRC work/scan ID, it queries the BDRC API and returns titles, author, author dates, and edition/scan provenance as JSON; use it to prefill the frontmatter. Claude then verifies, resolves ambiguities, and derives `copyright`. **Metadata is fetched, never recalled from model memory.**

## Frontmatter schema (canonical — copy exactly)

```yaml
---
id: derge-madhyamakavatara-comm-tsongkhapa   # stable ID prefix (edition–text)
title_bo: དབུ་མ་དགོངས་པ་རབ་གསལ།
title_wylie: dbu ma dgongs pa rab gsal
type: commentary            # root | commentary | subcommentary | refutation
comments_on: derge-madhyamakavatara   # stable ID of target text (commentaries/refutations)
author_bo: ཙོང་ཁ་པ་
author_wylie: tsong kha pa blo bzang grags pa
author_dates: 1357–1419
copyright: public-domain    # router: derived from author death date; decides step 14 target
school: gelug
edition: derge              # printing/edition of this e-text
bdrc_id: W00000             # BDRC work/scan ID (provenance + Wikidata property)
ocr_source: bdrc-ocr        # e-text provenance
language: bo
wikidata_work: ""           # QID — filled by step 15
wikidata_author: ""         # QID — filled by step 15
source_url: ""              # filled by step 14: Wikisource page (PD) or BDRC/WeBuddhist link
---
```

## Invariants
- Never invent metadata; every uncertain field gets a `# TODO:` comment, not a plausible guess.
- `copyright` is derived from the author's death date. Check death dates at ingest — 20th-century masters are typically still under copyright (life + 50–70 yrs); modern editorial apparatus can be too.
- `wikidata_work`, `wikidata_author`, `source_url` stay empty — the publication layer fills them so vault and wikis never diverge.
- OCR quality is covered by the BDRC collaboration; no separate spot-check stage.

## Canonical prompt

```
For the source text {{FILE}}, create texts/{{TEXT_ID}}.md using the frontmatter
schema exactly, fully filled.
- Derive `copyright` from the author's death date: public-domain if the author
  died 70+ years ago; otherwise `copyrighted`. If dates are uncertain, write
  `copyrighted-assumed` and flag for my review.
- Identify the edition from colophon/catalog data; if ambiguous, list the
  candidates instead of guessing.
- For commentaries, resolve `comments_on` to the root text's stable ID; if the
  root text isn't in the vault yet, flag it.
- Leave wikidata_* and source_url empty.
- Below the frontmatter, add a 3–5 line prose note: what the text is, its place
  in its school's curriculum, and known reception (who cited or refuted it).
Never invent metadata. Every uncertain field gets a `# TODO:` comment, not a
plausible guess.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
