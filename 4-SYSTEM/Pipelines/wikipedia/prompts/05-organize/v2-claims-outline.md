---
name: claims-outline
version: 2
stage: 05-organize
derived_from: [cowork-pipeline-step-09, chat-share-09ecaf85, prompts/05-organize/v1.md]
source_note: >
  Canonical prompt of 4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/09-outline (claude.ai share
  09ecaf85-57e5-4180-979b-b27912d0affa, 2026-08-01), merged with v1's repo-specific
  constraints that the emitter and validator depend on: the fixed section vocabulary and
  the no-empty-sections rule.
changed_from_v1: >
  The input is now the atomic claims table (stage 4b), not raw passages — load-bearing
  invariant 1: nothing downstream touches source wording after the claims stage. Sections
  are weighted by breadth across independent commentaries ADJUSTED BY RECEPTION (a
  refuted-and-defended position gets a section; an unengaged idiosyncrasy a sentence), each
  section carrying sub-consensus claims is marked for in-text attribution, and the output
  gains a gap report. Indices are claim indices, not passage indices.
model_tested: none
variables: [term, claims_json]
---

You are structuring the bo.wikipedia article for the Tibetan term "$term" from its atomic
claims table — **and nothing else**. The passages behind these claims are closed to you.

## Rules

1. **Use only the claims supplied.** Invent no material; every section must be built from
   claim indices. A section with no claims must not appear.
2. **Section headings come from this vocabulary only** (never invent a heading):
   ངེས་ཚིག · མཚན་ཉིད། · དབྱེ་བ། · གཞུང་ལུགས་སོ་སོའི་བཤད་པ། · བསྡུས་དོན།
3. **Weight sections by breadth adjusted by reception.** A theme treated by many independent
   commentators can carry a long section. A position others argued against (see each claim's
   `reception`) earns space; an unengaged single-commentator idiosyncrasy gets at most a
   sentence inside a broader section — never its own section.
4. **Divergent positions belong in གཞུང་ལུགས་སོ་སོའི་བཤད་པ།** — one sub-grouping per
   position, never merged. Set `divergence: true` on that section.
5. **Mark every section containing sub-consensus claims** (`claim_type` below `consensus`)
   with `attribution_required: true` — the drafter must name the commentator or school in
   the text there.
6. **The lead** (`lead`) lists the claims that define the term for a first-time reader —
   consensus claims first.
7. Each claim is used at most once outside the lead.
8. **Gap report** (`gap_report`): sections resting on a single source; explanation kinds
   with no claims at all; contested points that will need "X holds that…" treatment in
   drafting.

## Output

JSON only:

```
{
 "term": "...",
 "lead": [0, 2],
 "sections": [
  {
   "heading": "མཚན་ཉིད།",
   "claim_indices": [1, 4, 5],
   "divergence": false,
   "attribution_required": true
  }
 ],
 "unused": [7],
 "unused_reason": "…why each unused claim was left out…",
 "gap_report": ["…one line per gap…"]
}
```

`claim_indices` are indices into the supplied claims list.

---

**Atomic claims table:**

$claims_json
