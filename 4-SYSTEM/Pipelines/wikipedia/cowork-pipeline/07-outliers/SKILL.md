---
name: 07-outliers
description: "Pipeline step 7 — Outlier detection. Uses the verse alignment to diff commentaries on the same root verse and classify divergences as substantive doctrine, idiosyncratic phrasing, or OCR artifact. Use whenever the user says 'find outliers', 'diff the commentaries', 'divergence check', or after passages.md exists for a concept and outliers.md does not."
---

# Step 7 — Outlier detection (mechanical)

Using the verse alignment, diff commentaries on the same root verse. The alignment makes this nearly free — use it. Where one commentary diverges lexically or doctrinally from the others, classify the divergence.

## Inputs
- Alignment tables for the verses relevant to `{{CONCEPT}}`
- The commentaries themselves (for the flagged verses)

## Outputs
- `concepts/{{CONCEPT}}/outliers.md` — table: verse ID | diverging commentator | class | one-line description | for (a): who, if anyone, responds to this position elsewhere in the corpus

## Script
None.

## Invariants
- Three classes only: (a) substantive doctrinal divergence, (b) idiosyncratic phrasing of the same point, (c) probable OCR/e-text artifact.
- **Only (a) items feed the claims table as positions; (c) items are reported back to the corpus team.**

## Canonical prompt

```
Using the alignment tables for the verses relevant to {{CONCEPT}}, compare all
commentaries verse by verse. Where one commentary diverges from the others on
the same root verse, classify the divergence:
(a) substantive doctrinal divergence — a different position, not different
    wording
(b) idiosyncratic phrasing of the same point
(c) probable OCR/e-text artifact
Output concepts/{{CONCEPT}}/outliers.md:
verse ID | diverging commentator | class | one-line description | for (a):
who, if anyone, responds to this position elsewhere in the corpus.
Only (a) items feed the claims table as positions; (c) items are reported back
to the corpus team.
```

## Prompt maintenance
The pipeline document is the canonical home of this prompt. Step 13 patches land in the document first, then sync here.
