---
name: 16-wikipedia
description: "Pipeline step 16 — Wikipedia publication. Runs the pre-publication review that gates steps 14–16, then publishes the audited article to bo.wikipedia with refs deep-linking to Wikisource anchors, and links/creates the concept's Wikidata item. Use whenever the user says 'publish the article', 'push to bo.wikipedia', 'pre-publication review', or when an article has audit verdict 'publish' and steps 14–15 are done."
---

# Step 16 — Wikipedia

Publish the article to bo.wikipedia with refs deep-linking to the Wikisource anchors. Link the article to its concept's Wikidata item (create one if needed, then backfill the QID from step 5) — interwiki links wire up automatically, and cited works can be connected to the concept item where a suitable property exists.

## Inputs
- Final wikitext (audited: `audit.md` verdict = publish)
- Concept QID (step 5, possibly empty → create here)
- `source_url` values (step 14) and work/author QIDs (step 15)

## Outputs
- Live bo.wikipedia article
- Concept Wikidata item created/linked; QID backfilled into the concept note

## Script
**`scripts/publish.py`** — MediaWiki Action API for bo.wikipedia + Wikidata API; resulting URLs/QIDs written back into vault frontmatter.

## Gate — pre-publication review (canonical copy; gates steps 14–16)
Must return **publish** before `publish.py` runs. Steps 14 and 15 reference this prompt.

```
Act as a skeptical reviewer of the final wikitext before publication:
1. Refs: every ref resolves — PD sources to a Wikisource anchor matching the
   vault ID; copyrighted sources to a BDRC/WeBuddhist link carrying the full
   folio/page locator in the ref text. No more than a short phrase quoted
   verbatim in refs to copyrighted texts.
2. Attribution: scan for any sub-consensus claim sitting in neutral voice.
3. Synthesis: any sentence whose conclusion requires two sources combined.
4. Wikidata: concept QID present; cited works' and authors' QIDs exist
   (step 15 complete).
5. Restate the strongest independence case: which sources establish the
   concept's weight beyond a single school.
Verdict: publish / fix first.
```

## Invariants
- Nothing is published that hasn't survived the step 12 audit **and** this review (load-bearing invariant 2).
- Refs must resolve to the stable anchors minted at step 2 — no manual re-anchoring.
- QIDs and URLs are written back to frontmatter so the vault and the wikis never diverge.

## Prompt maintenance
The pipeline document is the canonical home of the review prompt. Step 13 patches land there first, then sync here.
