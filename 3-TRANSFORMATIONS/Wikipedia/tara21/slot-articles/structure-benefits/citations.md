---
topic: structure-benefits
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
revised_from: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/structure-benefits/article.md (prior version, method wiki-article-from-claims / v1, dated 2026-08-11; preserved by git history, not kept as a side-copy)
revision_date: 2026-08-21
context_packages:
  - 2-RAILS/Claims/structure.md
  - 2-RAILS/Claims/benefits.md
rails_status:
  structure: draft
  benefits: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/dharmabhadra.md
  - 2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md
  - 2-RAILS/Claims/raw/tree-guided/tenga-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
  - 2-RAILS/Claims/raw/tree-guided/karma-maitri.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-drub.md
  - 2-RAILS/Claims/raw/tree-guided/taranatha.md
  - 2-RAILS/Claims/raw/tree-guided/konchok-thabkhe.md
  - 2-RAILS/Claims/raw/tree-guided/pema-namgyal.md
date: 2026-08-11
status: draft
---

# Citations — structure-benefits

This is a **multi-topic work article** (Inputs §1, `wiki-article-from-claims/SKILL.md`): the topic
pages `2-RAILS/Claims/structure.md` and `2-RAILS/Claims/benefits.md` are combined into one article
on the root text itself (a *work* article, not a deity article). Body sections: lead (identification),
`== ས་བཅད། ==` (structure, from `structure.md`), `== ཕན་ཡོན། ==` (benefits, from `benefits.md`),
`== ལོ་རྒྱུས། ==` (transmission/colophon, from `benefits.md`'s Colophon facet).

**This revision (Mode B, `wiki-article-from-claims-v2`, 2026-08-21)** rewrites the v1 draft's
register only — no claim was re-derived, re-resolved, or newly introduced. Per Mode B step 1, the
prior `article.md` + `citations.md` were treated as settled ground truth. Changes made:

1. **Quotation budget (Rule 6)**: cut from 15 verbatim commentary quotations to 2. The 13 cut
   quotations were converted to wikivoice/attributed paraphrase using the same claim content
   already on record in the prior citations.md's reference-map table — no new claim content was
   introduced. The 2 retained quotations are unchanged, character-for-character, from the prior
   PASS-verified text (see Verification below — this is a text diff against the prior record, not
   a fresh `1-SOURCES/` lookup, per Mode B step 6).
2. **Register (Rules 5, 8, 9)**: consensus statements (empowerment/buddhahood attainment, poison
   protection, protection from spirits/epidemics/manner-of-recitation, wishes for children/wealth
   fulfilled, the 21-count total) were converted to plain wikivoice — no "X says" framing, support
   carried by the `<ref>`s alone. The article's opening paragraph of `== ཕན་ཡོན། ==` in the v1 draft
   (a second, near-duplicate restatement of the four-part vs two-part benefits-structure divergence
   already stated at the end of `== ས་བཅད། ==`) was removed as redundant — the divergence itself is
   fully preserved, once, in `== ས་བཅད། ==`. All ⚑ divergences (2-part vs 3-part top-level
   structure; the two competing sub-classification systems within "the actual praise"; the
   "two/three/seven" recitation-count divergence with all four/five named traditions; the
   threefold allegorical reading of "poison") remain fully attributed, every position present,
   none flattened (Rule 10).
3. **Citation cap (Rule 7)**: no statement in the v1 draft actually required trimming — the
   original citation choices already stayed within 3 refs per statement (verified programmatically
   on the revised text: max 3 refs in any single consecutive ref-run). No refs were moved to a
   "Full attestation beyond in-article refs" overflow list because none were cut for cap reasons;
   see that section below for why it stays empty in this revision.
4. **Punctuation contract (Rules 15–16)**: every sentence closed with a single shad `།`; every
   paragraph's final sentence closed with a double shad `།།` before its trailing `<ref>` tag(s);
   no comma character (ASCII `,` or any variant) anywhere in the fence body — verified
   programmatically (see Completion check).
5. **Author naming (Rule 17)**: the two personal-name mentions in the v1 draft
   (`མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་` for palden-sherab, `ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ` for taranatha) were checked
   against each commentary's `author_in_use` frontmatter key (frontmatter-only lookup, per Rule 17
   and Mode B's stated exception) — both already matched exactly and needed no change. No other
   in-prose personal-name mentions exist in the article; all other attribution uses each
   commentary's title in the subject position (e.g. "མེ་ལོང་ལས་...བཤད"), which is not a commentator
   name and so is outside Rule 17's scope. No `author_in_use` fallback warning is needed.

## Reference map

Named refs are per-commentary (no page numbers exist in the raw files' frontmatter, so the
hand-formatted ref form `<AUTHOR>། <TITLE>།` is identical across all claims from one commentary —
per Rule 7, repeats use `<ref name="..." />`). Each row below is one claim actually used in the
article body, grouped by its ref name. The **Quoted?** column is updated for this revision; claim
IDs, source blocks, and `Cite:` targets are carried forward unchanged from the v1 draft.

| Ref name | Commentary (registered_id) | Claim ID | Quoted? (this revision) | Quotation (verbatim བོད་ཡིག, if retained) | Source block |
|---|---|---|---|---|---|
| utpala | dharmabhadra | c-1-1 | No (paraphrased in v2 rewrite) | — | 1-SOURCES/Commentaries/སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-4 |
| utpala | dharmabhadra | c-1-2-1-1 | No (paraphrased) | — | …#^0-7 |
| utpala | dharmabhadra | c-1-3-1…c-1-3-3 | No | — | (per structure.md/benefits.md Coverage table) |
| lobsang-dawa | lobsang-dawa | c-1-0-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-3 |
| tenga-tulku | tenga-tulku | c-1-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །།.md#^0-2 |
| tenga-tulku | tenga-tulku | c-1-2-3-6-7 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-184 |
| tenga-tulku | tenga-tulku | c-1-3-1-1…c-1-3-4-1 | No (paraphrased) | — | (per benefits.md Structural framing) |
| tenga-tulku | tenga-tulku | c-1-3-3-5 | No (paraphrased) | — | …#^0-208 |
| gendun-gyatso | gendun-gyatso | c-1-1-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-3 |
| gendun-gyatso | gendun-gyatso | c-1-1-2 | No (21-count agreement) | — | (per structure.md Coverage table) |
| gendun-gyatso | gendun-gyatso | c-2-6 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-37 |
| karma-maitri | karma-maitri | c-1-1-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-2 |
| karma-maitri | karma-maitri | c-1-1-2 | No (21-count agreement) | — | (per structure.md Coverage table) |
| karma-maitri | karma-maitri | c-1-2-3/c-1-2-4 | No (representative) | — | (per benefits.md Coverage table) |
| karma-maitri | karma-maitri | c-1-2-11 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-49 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-0-3 | **Yes (retained)** | "བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ། བསྟོད་པ་དངོས་དང་ཕན་ཡོན་ནོ།" | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-3 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-0-4, c-0-5, c-0-13, c-0-14 | No (paraphrased) | — | …#^0-3 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-1, c-2-2 | No (paraphrased in v2 rewrite — c-2-2 quoted in v1) | — | …#^0-87, #^0-88 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-3 | **Yes (retained)** | "དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར།" | …#^0-89 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-4 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-90 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-9, c-2-12 | No (paraphrased) | — | …#^0-95, #^0-98 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-16 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-102 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-20 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-103 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-21 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-103 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-22 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-103 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-2-23 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-103 |
| palden-sherab | palden-sherab | c-3-0-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་…#^0-10 |
| palden-sherab | palden-sherab | c-3-2-0-1 | No (paraphrased) | — | …#^0-217 |
| palden-sherab | palden-sherab | c-3-2-1-2 | No (paraphrased) | — | …#^0-218 |
| gendun-drub | gendun-drub | c-2-2-3-1-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-106 |
| gendun-drub | gendun-drub | c-2-2-3-2-1/2 | No (representative) | — | (per benefits.md Coverage table) |
| gendun-drub | gendun-drub | c-2-2-3-3-2 | No (paraphrased) | — | …#^0-108 |
| gendun-drub | gendun-drub | c-2-2-3-4-2, c-2-2-3-4-3 | No (paraphrased — three attributed traditions retained, none flattened) | — | …#^0-113, #^0-114, #^0-115, #^0-116 |
| taranatha | taranatha | c-22-1-1 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^22-1-0 |
| taranatha | taranatha | c-22-1-18 | No (paraphrased) | — | …#^0-89 |
| taranatha | taranatha | c-22-1-19 | No (paraphrased) | — | …#^0-89 |
| taranatha | taranatha | c-22-1-38 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-89 |
| taranatha | taranatha | c-22-1-39 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-89 |
| taranatha | taranatha | c-22-1-40 | No (paraphrased) | — | …#^0-89 |
| taranatha | taranatha | c-22-1-41 | No (paraphrased) | — | …#^0-89 |
| konchok-thabkhe | konchok-thabkhe | c-2-1, c-2-4 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-10, #^0-11 |
| konchok-thabkhe | konchok-thabkhe | c-3-6, c-3-7 | No (paraphrased) | — | …#^0-104 |
| konchok-thabkhe | konchok-thabkhe | c-3-9 | No (paraphrased in v2 rewrite — quoted in v1) | — | …#^0-104 |
| pema-namgyal | pema-namgyal | c-3-5 | No (paraphrased) | — | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-77 |

## Full attestation beyond in-article refs

Empty for this revision. No `<ref>` was dropped from any statement to satisfy the citation cap
(Rule 7) — every statement in the rewritten article already carries 3 or fewer refs (verified
programmatically: max refs in any single consecutive ref-run across the fence body is 3). The v1
draft's own Warning #3 (several consensus facets on `benefits.md` with 9–11 attesting commentaries
are represented by 2–3 representative refs, per Rule 5's due-weight guidance, not the full
attestation list) carries forward unchanged and is not restated as a new overflow list here, since
it was already the v1 citation choice, not something this revision newly capped.

## Claims used but not quoted

Unchanged in substance from the v1 draft, with the addition of every claim ID that was quoted in
v1 and is now paraphrased in this revision (listed above with "(paraphrased in v2 rewrite — quoted
in v1)"). The original breakdown by section:

- **Structure section**: `dharmabhadra:c-1-2-1-1`, `lobsang-dawa:c-1-0-1`, `tenga-tulku:c-1-1`,
  `gendun-gyatso:c-1-1-1`/`c-1-1-2`, `karma-maitri:c-1-1-1`/`c-1-1-2`, `palden-sherab:c-3-0-1`,
  `drakpa-gyaltsen:c-0-4`/`c-0-5`/`c-0-13`/`c-0-14`, `gendun-drub:c-2-2-3-1-1`.
- **Benefits section**: `tenga-tulku:c-1-3-1-1…c-1-3-4-1`, `gendun-drub:c-2-2-3-2-1/2`,
  `karma-maitri:c-1-2-3/4`, `taranatha:c-22-1-18/19/40/41`, `gendun-drub:c-2-2-3-3-2` and
  `tenga-tulku:c-1-3-3-5` and `karma-maitri:c-1-2-11` (allegorical "poison," three positions,
  attributed and not flattened), `gendun-drub:c-2-2-3-4-2/3` and `gendun-gyatso:c-2-6` and
  `konchok-thabkhe:c-3-7` ("two/three/seven," multiple positions, attributed and not flattened),
  `palden-sherab:c-3-2-1-2`, `taranatha:c-22-1-1`, `konchok-thabkhe:c-3-6`, `drakpa-gyaltsen:c-2-1`,
  `c-2-9`, `c-2-12`.
- **Colophon section**: `konchok-thabkhe:c-2-1`/`c-2-4` (mentioned only in passing — see v1
  Warning #4, unchanged), `pema-namgyal:c-3-5`.

## Unresolvable attestations

None. Unchanged from v1 — this revision did not re-resolve any claim ID (Mode B, step 1); no new
claim ID was introduced.

## Warnings

1. **Both source rails are `status: draft`, not `complete`.** Unchanged from v1: `2-RAILS/Claims/structure.md`
   and `2-RAILS/Claims/benefits.md` are both `status: draft`. This revision did not touch the rails
   and does not change this fact.
2. **No commentary source has a `bdrc_work_id`/public URL** — unchanged from v1; every `<ref>` is
   still the spec's hand-formatted `<AUTHOR>། <TITLE>།` form with no year or page.
3. **Due weight follows attestation counts (Rule 5/10, unchanged from v1's own Warning #3)**:
   several consensus facets with 9–11 attesting commentaries are represented by 2–3 representative
   commentaries, by design, not by omission.
4. **`structure.md`'s "Framing" facet** (contested kriyā/anuttarayoga classification) is only
   briefly touched via `konchok-thabkhe:c-2-1`/`c-2-4` in the colophon section, unchanged from v1's
   own Warning #4 and scope choice.
5. **Category choice**: `བསྟན་བཅོས།` retained unchanged from v1 — still the closest allowlisted fit.
6. **No `author_in_use` fallback was needed in this revision** — both personal names appearing in
   the article body (palden-sherab, taranatha) already matched their commentary's `author_in_use`
   frontmatter value exactly (verified by frontmatter-only lookup, Rule 17 / Mode B exception).
7. **This revision changes register and punctuation only** — no claim ID appears in the revised
   article that was not already cited in the v1 `citations.md`'s reference map above.
8. **Post-hoc audit fix (2026-08-21, not a new revision)**: `article.md` used the invalid ref name
   `utpala` (not a registered commentary ID) for all `dharmabhadra` citations; every occurrence
   (1 full definition + 3 self-closing reuses) was renamed to `ref name="dharmabhadra"`, matching
   the registered ID in `2-RAILS/Claims/raw/tree-guided/dharmabhadra.md`. Separately, the category
   line was changed from `[[རིགས་དབྱེ།:བསྟན་བཅོས།]]` to `[[རིགས་དབྱེ།:ནང་ཆོས།]]`, since `བསྟན་བཅོས།`
   is not in the pipeline's `DEFAULT_CATEGORIES` allowlist (`4-SYSTEM/Pipelines/wikipedia/src/kangyur_wiki/cli.py`);
   this supersedes Warning #5 above, which is now stale. Reference map row labels above (`utpala`)
   were left as-is for audit-trail continuity with the pre-fix ref name; they refer to the same
   `dharmabhadra` claims now cited under the corrected ref name in `article.md`.
9. **Post-hoc quote-count audit fix (2026-08-21, not a new revision)**: a readability review flagged
   that the article might carry more than Rule 6's cap of 2 verbatim quotations. Per an explicit
   decision on scope, the Rule 6 lead-quote exemption for root-text verse quotation applies only to
   the deity-profile articles (`tara-01`…`tara-21`) — this is a work-article about the text's
   structure and benefits, so no quote in it is exempt. A full re-scan of every `"..."`-wrapped span
   in the wikitext fence (excluding `ref name="..."` attribute quotes, which are markup syntax, not
   content quotation) found 4 spans, not the 2 already tracked as "retained": the 2 substantive
   quotes (drakpa-gyaltsen c-0-3, the two-part-division definition; drakpa-gyaltsen c-2-3, the
   fearlessness line) plus 2 short quoted technical terms ("གཉིས་གསུམ་བདུན་" in the recitation-count
   divergence; "དུག་" in the allegorical-poison divergence) that had not previously been counted
   against the budget. The 2 substantive quotes were kept (exact wording is the claim); the 2
   technical-term quotes were converted to unquoted mentions — the quote marks were simply removed,
   since each term already carried its own quotative particle (`ཞེས་པ`/`ཅེས་པ`) doing the naming
   work, so no rewording, claim content, or citation was affected. Full span-by-span accounting is
   in Verification below. Final count: 2 quoted spans in the article, matching Rule 6.

## Verification

**Quotations in v1 (15 total, all PASS)** — the full v1 verification table is preserved below for
audit continuity. **This revision (Mode B, step 6)** did not re-verify these against `1-SOURCES/`;
instead, the 2 quotations retained in the revised article were diffed as an exact substring against
the text already marked PASS below. Both matched byte-for-byte with no alteration.

**Post-hoc quote-count audit fix (2026-08-21, not a new revision — see Warning #9)**: a readability
review flagged that the article might carry more than the Rule 6 cap of 2 verbatim quotations. A
full re-scan of every `"..."`-wrapped span in the wikitext fence (excluding `ref name="..."`
attribute quotes, which are markup syntax, not content quotation) found **4 spans total**, not 2:

| # | Location | Span | Nature | Disposition |
|---|---|---|---|---|
| 1 | `== ས་བཅད། ==`, drakpa-gyaltsen c-0-3 | "བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ། བསྟོད་པ་དངོས་དང་ཕན་ཡོན་ནོ།" | Substantive quote — the two-part-division claim itself | **Kept** (already counted as retained #1) |
| 2 | `== ཕན་ཡོན། ==`, drakpa-gyaltsen c-2-3 | "དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར།" | Substantive quote — a specific line whose exact wording is the claim | **Kept** (already counted as retained #2) |
| 3 | `== ཕན་ཡོན། ==`, recitation-count divergence | "གཉིས་གསུམ་བདུན་" | Short quoted technical term (the colophon's numeral phrase being glossed) | **Converted** — quote marks removed; `ཞེས་པ` (already present) retained as the naming device: `མཇུག་གི་ཚིག་གཉིས་གསུམ་བདུན་ཞེས་པའི་དོན་ལ...` |
| 4 | `== ཕན་ཡོན། ==`, allegorical-"poison" divergence | "དུག་" | Short quoted technical term (the word being given divergent readings) | **Converted** — quote marks removed; `ཅེས་པ` (already present) retained as the naming device: `འདིར་དུག་ཅེས་པའི་དོན་ལ...` |

**Which 2 were kept and why**: spans #1 and #2 are quotations in the substantive sense Rule 6
targets — the commentator's exact phrasing *is* the claim (a definitional two-part division; a
specific promise-line whose precise wording matters). Spans #3 and #4 are single- or two-syllable
technical terms under discussion (a numeral phrase, a poison-word), not claims about exact wording;
each already carried its own quotative particle (`ཞེས་པ`/`ཅེས་པ`) doing the naming work, so dropping
the ASCII quote marks around them loses nothing — the terms are still clearly flagged as terms being
glossed, just without double-counting against the quotation budget. No claim content, citation, or
divergence attribution was altered by either conversion — only the `"` characters were removed.

**Tally after fix: 2 quoted spans in the article (down from 4 found), matching Rule 6's cap.**

| # | Commentary | Claim ID | Quotation (opening words) | Source file / block | v1 Result | This revision |
|---|---|---|---|---|---|---|
| 1 | dharmabhadra | c-1-1 | "དེ་ཡང་སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག..." | …ཨུཏྤལའི་ཆུན་པོ་...md#^0-4 | PASS | Cut — paraphrased |
| 2 | drakpa-gyaltsen | c-0-3 | "བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ..." | …གསལ་བའི་འོད་ཟེར...md#^0-3 | PASS | **Retained — diff-matched, unchanged** |
| 3 | tenga-tulku | c-1-2-3-6-7 | "ཕྱག་འཚལ་བ་ཉེར་གཅིག་ནི། དང་པོ་ལོ་རྒྱུས..." | …མེ་ལོང...md#^0-184 | PASS | Cut — paraphrased |
| 4 | drakpa-gyaltsen | c-2-2 | "སྲོད་ཁྲོ་མོའི་སྐུ་དྲན་པ..." | …གསལ་བའི་འོད་ཟེར...md#^0-88 | PASS | Cut — paraphrased |
| 5 | drakpa-gyaltsen | c-2-3 | "དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར།" | …གསལ་བའི་འོད་ཟེར...md#^0-89 | PASS | **Retained — diff-matched, unchanged** |
| 6 | drakpa-gyaltsen | c-2-4 | "སྡིག་པ་ཐམས་ཅད་རབ་དུ་ཞི་བ།" | …གསལ་བའི་འོད་ཟེར...md#^0-90 | PASS | Cut — paraphrased |
| 7 | drakpa-gyaltsen | c-2-16 | "བུ་འདོད་པས་ནི་བུ་ཐོབ་འགྱུར་ཞིང་།" | …གསལ་བའི་འོད་ཟེར...md#^0-102 | PASS | Cut — paraphrased |
| 8 | drakpa-gyaltsen | c-2-20 | "བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ..." | …གསལ་བའི་འོད་ཟེར...md#^0-103 | PASS | Cut — paraphrased |
| 9 | drakpa-gyaltsen | c-2-21 | "སློབ་དཔོན འཕགས་པ་ཀླུ་སྒྲུབ་ནས་བརྒྱུད་པ།" | …གསལ་བའི་འོད་ཟེར...md#^0-103 | PASS | Cut — paraphrased |
| 10 | drakpa-gyaltsen | c-2-22 | "ལོཙྪ་བ་གཉན་གྱིས་བསྒྱུར་བ།" | …གསལ་བའི་འོད་ཟེར...md#^0-103 | PASS | Cut — paraphrased |
| 11 | drakpa-gyaltsen | c-2-23 | "རྗེ་བཙུན་ཆེན་པོ་གྲགས་པ་རྒྱལ་མཚན..." | …གསལ་བའི་འོད་ཟེར...md#^0-103 | PASS | Cut — paraphrased |
| 12 | taranatha | c-22-1-38 | "གཞན་ཡང་ཞི་བ་ལ་སོགས་པའི་ལས..." | …བསྟོད་པའི་རྣམ་པར་བཤད་པ...md#^0-89 | PASS | Cut — paraphrased |
| 13 | taranatha | c-22-1-39 | "འཕགས་མ་སྒྲོལ་མ་ལ་བསྟོད་པ..." | …བསྟོད་པའི་རྣམ་པར་བཤད་པ...md#^0-89 | PASS | Cut — paraphrased |
| 14 | konchok-thabkhe | c-3-9 (a) | "བདག་ཅག་གི་སྟོན་པས་ཀྱང་གསུངས་པ" | …ཞལ་ལུང...md#^0-104 | PASS | Cut — paraphrased |
| 15 | konchok-thabkhe | c-3-9 (b) | "འདས་པའི་སངས་རྒྱས་རྣམས་ཀྱིས་གསུངས..." | …ཞལ་ལུང...md#^0-104 | PASS | Cut — paraphrased |

**Tally: 2 quotations in the revised article, both diff-matched exact against prior PASS text. 0 FAIL.**
(The above tally covered only the 2 spans this revision had already tracked as "retained." The
post-hoc audit above re-scanned the whole fence for every `"..."` span — including short quoted
technical terms not previously tracked as "quotations" — and found 2 more, both now converted to
unquoted mentions. Final count after the post-hoc fix: 2 quoted spans total in the article, per
Rule 6.)

## Completion check (per SKILL.md, this revision)

- [x] `article.md` and `citations.md` rewritten in place under
      `3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/structure-benefits/`; nothing else modified
- [x] No claim ID appears in the revised article that was not already in the v1 reference map
- [x] Quotation budget: 2 quotations in the whole article (down from 15), both diff-matched exact
      against text already marked PASS in v1 — no re-verification against `1-SOURCES/` performed
- [x] Citation cap: no statement carries more than 3 refs (verified programmatically: max 3)
- [x] Consensus material converted to wikivoice; all ⚑ divergences remain fully attributed, no
      position dropped or flattened (2-part/3-part top-level split; the two sub-classification
      systems within "the actual praise"; the "two/three/seven" divergence, all traditions
      preserved; the threefold allegorical "poison" reading)
- [x] Punctuation contract verified programmatically: 0 comma characters in the fence body; every
      one of the 17 prose paragraphs ends in a double shad `།།` immediately before its trailing
      `<ref>` tag(s); no punctuation found following any `<ref>` tag
- [x] Both in-prose personal-name mentions (palden-sherab, taranatha) already used the correct
      `author_in_use` form; no fallback warning needed
- [x] `== ལུང་ཁུངས། ==` + `<references />` present; no `{{Reflist}}`; fixed tail section order
      unchanged (`འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`); category unchanged
- [x] `citations.md` frontmatter records `context_packages`, `rails_status`, `status: draft`,
      `revision_mode: B`
