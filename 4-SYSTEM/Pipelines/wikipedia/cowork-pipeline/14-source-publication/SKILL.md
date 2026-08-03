---
name: 14-source-publication
description: "Pipeline step 14 — Source publication, routed by the copyright frontmatter field. Publishes public-domain texts to multilingual Wikisource with section anchors matching vault stable IDs; copyrighted texts are cited via stable BDRC/WeBuddhist links instead. Use whenever the user says 'publish the sources', 'push to Wikisource', or when an audited article's cited texts have empty source_url fields. Gated by the pre-publication review in 16-wikipedia."
---

# Step 14 — Source publication (routed by `copyright`)

Publish or link every cited source text, routed by the `copyright` field in its note's frontmatter.

## Gate
The **pre-publication review** (canonical prompt in `skills/16-wikipedia/SKILL.md`) gates steps 14–16 as a unit and must return **publish** before `publish.py` runs. Also requires an `audit.md` verdict of publish (step 12).

## Inputs
- Text notes (`texts/*.md`) for every source cited by the article; their `copyright` field routes each text
- Vault stable IDs (step 2) — they become Wikisource section anchors
- Full locators from `claims.md` for refs to copyrighted texts

## Outputs
- **Public domain** → page on multilingual wikisource.org with section anchors matching the vault IDs; the edition stated on each text's page
- **Copyrighted** → no republication; a stable link to the text on BDRC or WeBuddhist
- Either way: the resulting URL written back into the text note's `source_url`

## Script
**`scripts/publish.py`** — MediaWiki Action API (bot account + edit tokens). After each successful call it writes `source_url` back into the vault frontmatter, keeping the round-trip invariant automatic rather than manual.

## Invariants
- Copyrighted texts (modern commentators, modern apparatus) are **never republished**. Prefer BDRC's persistent work/scan IDs where both BDRC and WeBuddhist exist.
- BDRC/WeBuddhist links have no verse-level anchors, so **the ref itself must carry the full locator** (folio/page/section) from the claims table.
- Keep any verbatim quotation in refs to copyrighted texts brief.
- Anchors must match vault stable IDs exactly — refs generated during drafting survive publication unchanged.
- Frontmatter is the single source of truth: `source_url` is written back so the vault and the wikis never diverge.

## Prompt maintenance
This step has no canonical drafting prompt; its gate prompt lives in `skills/16-wikipedia/SKILL.md`. Behavior patches land in the pipeline document first, then sync here.
