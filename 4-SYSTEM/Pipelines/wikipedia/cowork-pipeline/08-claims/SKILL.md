---
name: 08-claims
description: "Pipeline step 8 — Atomic claims table (in Tibetan). Converts passages.md + outliers.md into claims.md: one verifiable fact per row, own words, with claim type and reception columns. This file becomes the ONLY drafting input downstream. Use whenever the user says 'build the claims table', 'atomize', 'claims for <concept>', or when passages.md and outliers.md exist but claims.md does not. claims.md is immutable once written."
---

# Step 8 — Atomic claims (in Tibetan)

Convert passages → claims table, one verifiable fact per row. This is the pipeline's hinge: **the claims table is the only drafting input from here on** (load-bearing invariant 1). Source wording is left behind in `passages.md`, which remains only as verification material.

## Inputs
- `concepts/{{CONCEPT}}/passages.md` and `outliers.md`
- Locked glossary `{{GLOSSARY}}`

## Outputs
- `concepts/{{CONCEPT}}/claims.md` — **immutable once written**

| Field | Content |
|---|---|
| ID | C-number |
| Claim | one fact, own words, Tibetan, locked glossary terms preserved |
| Locator | edition-aware verse/section ID |
| Commentator / School | author + Nyingma / Gelug / Sakya / Kagyu / Jonang / … |
| Claim type | consensus · majority-with-dissent · school-position · single-commentator |
| Reception | cited by whom · refuted by whom (dgag lan and response literature) · unengaged |

## Script
None.

## Invariants
- **Weight by authority and response, not headcount.** One major figure outweighs several minor commentators. The corpus-internal proxy for authority is how often *other* commentators cite or refute the position — refutation literature is a reception record; a position that drew rebuttals has proven weight.
- **Normalize for corpus composition.** Tag each concept's coverage per school. In a skewed corpus, a sole representative of an entire school is a **school-position, never a fringe view** (Zhentong is a one-author outlier by headcount and a defining doctrine by reality).
- Nothing is dropped for being an outlier; claim type determines treatment downstream.
- No forbidden synthesis: no claim may require two sources combined to reach a conclusion neither states alone.
- Immutable once written.

## Canonical prompt

```
Read concepts/{{CONCEPT}}/passages.md and outliers.md. Produce claims.md: one
verifiable fact per row, written in Tibetan in your own words — never reuse a
source's sentence structure. These glossary terms must appear verbatim:
{{GLOSSARY}}.
Columns: ID | claim (bo) | locator | commentator/school | claim type |
reception.
- Claim type: consensus · majority-with-dissent · school-position ·
  single-commentator. Weight by authority and response, not headcount. A
  commentator who is the sole representative of his school in our corpus is a
  school-position, never single-commentator.
- Reception: cited by … / refuted by … (name the texts) / unengaged.
- One fact per row; split compound statements. Conflicting positions get one
  row each — never merge into a compromise no source states.
- Forbidden: any claim requiring two sources combined to reach a conclusion
  neither states alone. Record temptations in a "forbidden syntheses" list at
  the end instead.
- Flag rows resting only on a copyrighted source (verifiable only via the
  BDRC/WeBuddhist link).
This file is immutable once written.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
