---
name: 09-outline
description: "Pipeline step 9 — Outline. Builds the article outline from claims.md ONLY, weighting sections by breadth adjusted by reception, and producing a gap report. Use whenever the user says 'outline the article', 'structure <concept>', or when claims.md exists and outline.md does not. Never open passages.md during this step."
---

# Step 9 — Outline

Built from claims only. Sections weighted by breadth across independent commentaries, **adjusted by reception**: an outlier position that others argued against gets a section; an unengaged idiosyncrasy gets a sentence or footnote.

## Inputs
- `concepts/{{CONCEPT}}/claims.md` — and nothing else

## Outputs
- `concepts/{{CONCEPT}}/outline.md` — lead + body sections with the claim IDs each will use, sub-consensus markers, and a gap report

## Script
None.

## Invariants
- **Claims-only: do not open `passages.md`** (load-bearing invariant 1 — nothing downstream touches source wording after the claims stage).
- Divergent school positions are marked for in-text attribution when drafted.
- Weight = breadth adjusted by reception, not headcount.

## Canonical prompt

```
From claims.md ONLY (do not open passages.md), propose the article outline in
outline.md:
- Lead + body sections per bo.wikipedia conventions; under each section, the
  claim IDs it will use.
- Weight sections by breadth across independent commentaries, adjusted by
  reception: a refuted-and-defended position gets a section; an unengaged
  idiosyncrasy gets at most a sentence.
- Mark every section containing sub-consensus claims — these need in-text
  attribution when drafted.
- Gap report: sections resting on one source; reader questions (step 6
  taxonomy) with no claims; contested points needing "According to X…"
  treatment.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
