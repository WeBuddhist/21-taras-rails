---
name: prepublication-review
version: 1
stage: 08-review
derived_from: [cowork-pipeline-step-16, chat-share-09ecaf85]
source_note: >
  The pre-publication review gate of 4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/16-wikipedia (claude.ai
  share 09ecaf85-57e5-4180-979b-b27912d0affa, 2026-08-01) — the canonical copy that gates
  the whole publication layer (steps 14–16): publish.py runs only after this returns
  "publish". In this repo it is run by the human (or by Claude on the human's behalf)
  inside /publish, before `kwiki publish --execute`; it never replaces the deterministic
  verify gate or the --execute confirmation. Check 4 (Wikidata QIDs) is kept from the
  canonical prompt but is advisory here until a Wikidata sync exists (see
  docs/reference/cowork-pipeline.md step 15).
model_tested: none
variables: [term, wikitext, sources_json]
---

Act as a skeptical reviewer of the final wikitext for "$term" before publication:

1. **Refs:** every ref resolves — public-domain sources to a Wikisource link whose anchor
   matches the pipeline's block ID; copyrighted sources to a BDRC/WeBuddhist link carrying
   the full locator in the ref text. No more than a short phrase quoted verbatim in refs to
   copyrighted texts. A ref with no URL at all is a gap the reader cannot check — list every
   one.
2. **Attribution:** scan for any sub-consensus position sitting in Wikipedia's neutral
   voice.
3. **Synthesis:** any sentence whose conclusion requires two sources combined.
4. **Wikidata:** concept QID present; cited works' and authors' QIDs exist. (Advisory until
   the Wikidata sync stage exists in this repo.)
5. **Restate the strongest independence case:** which sources establish the concept's
   weight beyond a single school.

Verdict: **publish / fix first** — with the list of what to fix.

---

**Wikitext under review:**

$wikitext

**Source registry:**

$sources_json
