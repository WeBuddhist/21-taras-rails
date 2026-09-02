---
name: 02-alignment
description: "Pipeline step 2 — Verse alignment & stable IDs. Aligns a commentary to its root text verse by verse and mints edition-aware stable IDs used everywhere downstream. Use whenever the user says 'align', 'alignment table', 'verse mapping', or after ingesting a commentary/subcommentary/refutation whose alignment/<text-id>.md does not yet exist."
---

# Step 2 — Verse alignment & stable IDs

Align commentaries to the root text verse by verse and mint **edition-aware stable IDs** (`edition–text–chapter–verse`). These IDs are used by every downstream stage and later become Wikisource section anchors — so refs generated during drafting survive publication unchanged.

## Inputs
- `texts/{{COMMENTARY_ID}}.md` (its `comments_on` field names the root)
- `texts/{{ROOT_ID}}.md` and both e-texts

## Outputs
- `alignment/{{COMMENTARY_ID}}.md` — table: root verse stable ID | commentary locator (edition-aware) | confidence (high/medium/low) | note

## Script
None. This step is judgment work in Cowork.

## Invariants
- Stable IDs are **edition-aware** and never change after minting — they double as Wikisource anchors at step 14.
- Never force an alignment: mark low confidence instead; skipped verses are recorded as explicit gaps; unaligned sections are listed at the end.
- A section covering multiple verses maps to all of them.

## Canonical prompt

```
Align {{COMMENTARY_ID}} to its root text {{ROOT_ID}} verse by verse. Output
alignment/{{COMMENTARY_ID}}.md as a table:
root verse stable ID | commentary locator (edition-aware) | confidence
(high/medium/low) | note.
- Use the commentary's own structural markers (sa bcad, root-verse citations)
  as anchors.
- A section covering multiple verses maps to all of them; skipped verses are
  recorded as explicit gaps.
- Mark low confidence rather than forcing an alignment; list all unaligned
  sections at the end.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
