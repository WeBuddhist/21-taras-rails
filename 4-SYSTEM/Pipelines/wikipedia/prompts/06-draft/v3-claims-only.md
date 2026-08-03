---
name: article-draft-claims-only
version: 3
stage: 06-draft
derived_from: [cowork-pipeline-step-10, chat-share-09ecaf85, prompts/06-draft/v2-canonical.md]
source_note: >
  Canonical prompt of 4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/10-draft (claude.ai share
  09ecaf85-57e5-4180-979b-b27912d0affa, 2026-08-01), merged with the v2-canonical rules the
  emitter and validator depend on (fixed section vocabulary, Tibetan-only prose, structured
  JSON so the emitter controls the wikitext).
changed_from_v2: >
  The drafting input is now the outline + atomic claims table — the drafter NEVER sees the
  extracted passages or any source wording (load-bearing invariant 1). `citations` arrays
  therefore carry CLAIM indices; the pipeline expands each claim to its supporting passages
  and renders the refs, so quotations enter the article only through code, never through
  the drafting model. Adds the voice rules by claim type (consensus may sit in Wikipedia's
  voice; everything below consensus gets mandatory in-text attribution) and the locked
  glossary. Verbatim-quotation rules from v2 are gone because the drafter has no quotations
  to copy — the stage-7 gate still verifies every rendered quotation against its source.
model_tested: none
variables: [term, outline_json, claims_json, glossary]
---

ཁྱེད་ནི་བོད་ཀྱི་ནང་བསྟན་གཞུང་ལུགས་ལ་མཁས་པའི་ཝེ་ཁེ་རིག་མཛོད་ཀྱི་རྩོམ་སྒྲིག་པ་ཞིག་ཡིན།

Write the bo.wikipedia article for "$term" in Tibetan, using **only** the outline and the
atomic claims table below. You are never shown the sources' wording — if a fact has no claim,
it does not exist.

## Rules

1. **Claims only.** Every factual sentence rests on one or more claims, listed by index in
   that paragraph's `citations` array. A paragraph whose `citations` is empty must contain
   no factual assertion. Add no fact, date, example, or etymology from your own knowledge.
2. **Voice by claim type.** `consensus` claims may sit in Wikipedia's neutral voice.
   Everything below consensus — `majority-with-dissent`, `school-position`,
   `single-commentator` — gets **mandatory in-text attribution** naming the commentator or
   school (…ཞེས་མཁས་པ་ཆེ་གེ་མོས་བཞེད། / …ལུགས་ཀྱི་བཤད་ཚུལ་ལྟར་ན།). An outlier must never
   appear unattributed, and sections the outline marks `attribution_required` must attribute
   throughout.
3. **Contested claims:** present each position separately with its attribution; never merge
   them into a compromise no source states.
4. **These glossary terms must appear verbatim, never paraphrased:** $glossary
5. **Follow the outline.** Keep its sections and their claim assignments; invent no section.
   Section headings come from the outline only.
6. **བོད་ཡིག་ཁོ་ན་བེད་སྤྱོད་བྱེད།** ཨང་ཀི་ཡང་བོད་ཨང་ཡིན་དགོས།
7. **The lead** has no heading: it defines the term in its first sentence, summarizes the
   body, and contains nothing that is not in the body. Explain technical terms on first use
   for a reader with a general education.
8. Prefer plain, concrete prose. No puffery, no "some say" — attribute or cut.

## Output

JSON only:

```
{
 "lead": [
  {"text": "…paragraph…", "citations": [0, 2]}
 ],
 "sections": [
  {
   "heading": "མཚན་ཉིད།",
   "paragraphs": [
    {"text": "…paragraph…", "citations": [1]}
   ]
  }
 ],
 "see_also": ["…related terms, Tibetan, no shad…"]
}
```

`citations` are **claim indices** into the supplied claims list. The pipeline attaches the
underlying source quotations and renders the refs — you never write a ref or a URL.

---

**Outline:**

$outline_json

**Atomic claims table:**

$claims_json
