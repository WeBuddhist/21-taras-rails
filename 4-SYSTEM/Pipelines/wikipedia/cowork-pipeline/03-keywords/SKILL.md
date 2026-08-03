---
name: 03-keywords
description: "Pipeline step 3 — Keyword extraction & variant clustering. Clusters top TF-IDF terms into concepts, merging Wylie/Unicode/Sanskrit/orthographic variants so counts don't split. Use whenever the user says 'cluster the keywords', 'extract candidate concepts', 'variant clustering', or supplies a TF-IDF term list from the corpus."
---

# Step 3 — Keyword extraction (variant clustering)

TF-IDF over the corpus produces candidate terms; this skill covers the **judgment half**: clustering variants and abbreviations per concept so counts don't split.

## Inputs
- `{{TERM_LIST}}` — top TF-IDF terms for the corpus. The TF-IDF computation itself is deterministic and scripted outside this skill (the vault layout defines no script for it; the term list is supplied as input).

## Outputs
- Concept cluster table, one row per concept: canonical Tibetan form | all variants | Sanskrit equivalent if standard | one-line gloss. This table is the `{{CLUSTER_TABLE}}` input of step 4. (The pipeline doc defines no canonical vault path for it; store it alongside `pipeline/` working notes.)

## Script
None in the vault; TF-IDF is precomputed.

## Invariants
- Merge only true variants: orthographic variants, abbreviations, Wylie/Unicode duplicates, standard Sanskrit equivalents.
- **Never merge distinct technical terms that are merely related** — when unsure, keep separate and note the relation.

## Canonical prompt

```
Here are the top TF-IDF terms for the corpus: {{TERM_LIST}}. Cluster them into
concepts:
- Merge orthographic variants, abbreviations, Wylie/Unicode duplicates, and
  standard Sanskrit equivalents of the same concept.
- Do NOT merge distinct technical terms that are merely related — when unsure,
  keep separate and note the relation.
- Output one row per concept: canonical Tibetan form | all variants | Sanskrit
  equivalent if standard | one-line gloss.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
