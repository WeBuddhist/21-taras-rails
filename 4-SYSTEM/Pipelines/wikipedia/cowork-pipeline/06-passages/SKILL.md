---
name: 06-passages
description: "Pipeline step 6 — Passage gathering. Pulls every passage relevant to a concept via the verse alignment tables into concepts/<concept>/passages.md, tagged with edition-aware locator, commentator, and school. Use whenever the user says 'gather passages', 'extract passages for <concept>', or starts the extraction layer for a new concept. passages.md is immutable once written — never invoke this to edit an existing one."
---

# Step 6 — Passage gathering

Per concept, pull relevant passages via the verse links into an **immutable** verification file. Passages stay in the vault as verification material — they are never published and are never seen again by the drafting stages.

## Inputs
- Alignment tables (`alignment/*.md`) for texts touching the concept
- Text notes' frontmatter (author/school)
- Concept + all variant forms

## Outputs
- `concepts/{{CONCEPT}}/passages.md` — **immutable once written**

## Script
None.

## Invariants
- **Immutability:** once written, `passages.md` is never edited. Corrections mean a new extraction run, not a patch.
- Passages are copied **verbatim** and stay private as verification material — never published (load-bearing invariant 1: nothing downstream touches source wording after the claims stage; passages exist only to verify claims).
- Extract disagreements aggressively — passages where a commentator names and refutes another position are the most valuable. Skip tangential mentions.

## Canonical prompt

```
You are preparing the bo.wikipedia article "{{CONCEPT}}". Your reader is an
educated Tibetan speaker who is not a scholastic specialist.
Using the alignment tables, gather every passage relevant to {{CONCEPT}} (all
variant forms) into concepts/{{CONCEPT}}/passages.md, grouped by source text.
For each passage record:
- LOCATOR: edition-aware stable ID (+ section within it)
- AUTHOR/SCHOOL: from the text note's frontmatter
- ANSWERS: which reader question it serves — definition · etymology/Sanskrit
  background · doctrinal context · positions & interpretations · disputes &
  refutations · practice relevance · history of the term
- NOTE: one line on why it matters or how it differs from other sources on the
  same point
Copy passages verbatim — they stay private as verification material and are
never published. Extract disagreements aggressively: passages where a
commentator names and refutes another position are the most valuable. Skip
tangential mentions. This file is immutable once written.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
