---
topic: tara-01
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
revised_from: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-01/article.md (v1, method wiki-article-from-claims, dated 2026-08-10)
revision_date: 2026-08-21
context_packages:
  - 2-RAILS/Claims/tara-01.md
rails_status: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/yama-sonam.md
  - 2-RAILS/Claims/raw/tree-guided/dharmabhadra.md
  - 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-drub.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
  - 2-RAILS/Claims/raw/tree-guided/karma-maitri.md
  - 2-RAILS/Claims/raw/tree-guided/konchok-thabkhe.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/pema-namgyal.md
  - 2-RAILS/Claims/raw/tree-guided/sangye-nyentrul.md
  - 2-RAILS/Claims/raw/tree-guided/sungrab-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/taranatha.md
  - 2-RAILS/Claims/raw/tree-guided/tenga-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/tenzin-dhonzang.md
  - 2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md
date: 2026-08-10
status: draft
---

> [!note] Polished — gemini-article-polish, 2026-08-23, model gemini-3.1-pro-preview; claim usage unchanged from 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-01/article.md (pre-polish).

# Citations — tara-01

## Revision note (Mode B, v1 → v2)

This file and `article.md` were rewritten in place under `wiki-article-from-claims-v2`'s
**Mode B** procedure (register revision, not a redraft) on 2026-08-21. Per Mode B, no new
`2-RAILS/Claims/` or raw tree-guided lookup was performed and no claim ID was introduced
that was not already present in the v1 `citations.md`'s reference map (reproduced unchanged
below). Only these changed:

- **Register**: one-claim-one-sentence citation-dump sequences were merged into connected
  wikivoice prose (Rule 5, 8). Consensus material lost its inline commentator-name framing;
  attribution was kept only for unique claims and the three ⚑ divergences in
  `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`.
- **Quotation budget (Rule 6)**: v1 carried **17 verbatim quotations** (see the v1
  verification table below — all still PASS, unchanged text). v2 keeps **2**: (1) the
  sungrab-tulku wisdom-eye gloss ("ཡེ་ཤེས་ཀྱི་སྤྱན་ནི་སྐད་ཅིག་གི་གློག་འཁྱུག་པ...ནུས་པ་ཡོད་པའོ།",
  `སྐུ་ཡི་རྣམ་པ།`) and (2) the dharmabhadra root-verse variant reading ("ཕྱག་འཚལ་སྒྲོལ་མ་
  མྱུར་མ་དཔལ་མོ།", `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`) — chosen because both are cases where the
  exact wording is itself the point (a technical definition and a contested textual
  variant). The other 15 quotations were converted to paraphrase, grounded in the same
  quoted Tibetan text already present and verified in the v1 article — no new `1-SOURCES/`
  lookup was performed for any of them, per Mode B step 4. Neither retained quote is a
  root-text verse quotation in the lead, so the Rule 6 lead exemption does not apply to
  either — both count against, and are within, the budget of 2.
- **Citation cap (Rule 7)**: v1 attached up to 14 refs to a single statement (the origin
  narrative's "attested by all 15 commentaries" sentence). Every statement in v2 carries
  at most 3 `<ref>`s (verified by scanning consecutive ref clusters in the fence body — see
  Completion check below). Every commentary dropped from a capped statement is listed
  under *Full attestation beyond in-article refs*.
- **Punctuation (Rules 15–16)**: the several ASCII commas present in v1's fence body
  (e.g. after homage-identification clauses and in the power-object enumeration in
  `མཚན་གྱི་ངེས་ཚིག`) were removed; every sentence now closes on a shad `།` and every
  paragraph closes on a double shad `།།`, placed before any trailing `<ref>` tag.
- **Author naming (Rule 17)**: all 15 raw tree-guided files' frontmatter already carry an
  `author_in_use` key (confirmed by a frontmatter-only grep, no claim content read — see
  table below); every in-prose commentator name in v2 already matched `author_in_use`
  in v1 too, so no name substitutions were needed. No fallback-to-`author` warning applies.

No claim ID appears anywhere in the v2 article that was not already cited in v1's
reference map below. `lobsang-dawa`'s status (listed in `tara-01.md`'s `sources:` but
contributing no claims to this slot — its verse-1 content routes to the `origin` global
slot per its own spine-map) is unchanged from v1 and still excluded from the 15 raw
sources actually cited.

### `author_in_use` frontmatter check (Rule 17, done for this revision)

| Commentary | `author_in_use` present? | Value |
|---|---|---|
| taranatha | yes | ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ་ |
| yama-sonam | yes | རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་ |
| palden-sherab | yes | མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་ |
| sangye-nyentrul | yes | སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ་ |
| sungrab-tulku | yes | འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་ |
| dharmabhadra | yes | དངུལ་ཆུ་དྷརྨ་བྷ་དྲ་ |
| drakpa-gyaltsen | yes | རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་ |
| gendun-gyatso | yes | རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ་ |
| karma-maitri | yes | ཀརྨ་མཻ་ཏྲི་ |
| tenzin-dhonzang | yes | སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་ |
| tenga-tulku | yes | རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་ |
| pema-namgyal | yes | ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་ (differs from formal `author` "ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ་"; bibliography keeps the formal form, prose uses `author_in_use`) |
| tsultrim-namdak | yes | མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་ |
| gendun-drub | yes | རྒྱལ་བ་དགེ་འདུན་གྲུབ་ (formal `author` also carries "(ཏཱ་ལའི་བླ་མ་སྐུ་ཕྲེང་དང་པོ)"; `author_in_use` correctly drops the parenthetical) |
| konchok-thabkhe | yes | དཀོན་མཆོག་ཐབས་མཁས་ |

No missing `author_in_use` fallback occurred — no warning line required for this rule.

## Full attestation beyond in-article refs

Every capped statement below is followed by the commentary:claim-id pairs of the
attesting commentaries dropped from the in-article citation (kept ≤3 reps per Rule 7),
so no attestation from v1's reference map is lost.

- **Lead, "identified as the activity-embodiment of all victors"** (kept: palden-sherab,
  sangye-nyentrul, sungrab-tulku) — dropped: tsultrim-namdak:c-2-1-2-1-3
- **མཚན་གྱི་ངེས་ཚིག, Tārā-etymology consensus** (kept: taranatha, dharmabhadra,
  drakpa-gyaltsen) — dropped: gendun-gyatso:c-1-1-3, tsultrim-namdak:c-2-1-2-1-4
- **མཚན་གྱི་ངེས་ཚིག, Swift (མྱུར་མ)-etymology consensus** (kept: drakpa-gyaltsen,
  gendun-gyatso, karma-maitri) — dropped: konchok-thabkhe:c-2-1-2, palden-sherab:c-3-1-1-1-1,
  sangye-nyentrul:c-2-0-2, sungrab-tulku:c-4-6, tenga-tulku:c-1-2-1-5,
  tsultrim-namdak:c-2-1-2-1-4, yama-sonam:c-3-1-8 (yama-sonam's elaborated version of this
  etymology is separately attributed to him by name in the following paragraph, per Rule 5)
- **མཚན་གྱི་ངེས་ཚིག, Heroine (དཔའ་མོ)-etymology / power-object variation** (kept:
  drakpa-gyaltsen, palden-sherab, sungrab-tulku) — dropped: konchok-thabkhe:c-2-1-3,
  tenzin-dhonzang:c-4-1-6, karma-maitri:c-1-1-1-6, gendun-gyatso:c-1-1-5,
  taranatha:c-1-1, tenga-tulku:c-1-2-1-5, sangye-nyentrul:c-2-0-3,
  tsultrim-namdak:c-2-1-2-1-4, pema-namgyal:c-2-4-11
- **སྐུ་ཡི་རྣམ་པ།, wisdom-eye-like-lightning consensus** (kept: yama-sonam, dharmabhadra,
  drakpa-gyaltsen) — dropped: palden-sherab:c-3-1-1-1-2, tsultrim-namdak:c-2-1-2-1-5,
  tenzin-dhonzang:c-4-1-6
- **ལོ་རྒྱུས།, origin-narrative consensus ("all 15 commentaries agree")** (kept: yama-sonam,
  sangye-nyentrul, palden-sherab, reused from elsewhere in the article for compactness;
  taranatha is cited separately in the same paragraph for his own fuller telling) —
  dropped: dharmabhadra:c-1-2-1-9, drakpa-gyaltsen:c-1-5–c-1-7, gendun-drub:c-2-2-2-1-3,
  gendun-gyatso:c-1-1-7/c-1-1-8, karma-maitri:c-1-1-1-9, konchok-thabkhe:c-2-1-4,
  pema-namgyal:c-2-4-14, sungrab-tulku:c-4-14, tenga-tulku:c-1-2-1-4,
  tenzin-dhonzang:c-4-1-7, tsultrim-namdak:c-2-1-2-1-6
- **གཞུང་ལུགས་སོ་སོའི་བཤད་པ།, dpa'-mo/dpal-mo reading — majority position** (kept:
  taranatha, drakpa-gyaltsen, palden-sherab) — dropped: gendun-gyatso:c-1-1-5,
  karma-maitri:c-1-1-1-6, konchok-thabkhe:c-2-1-2, pema-namgyal:c-2-4-11,
  sangye-nyentrul:c-2-0-3, sungrab-tulku:c-4-7, tenga-tulku:c-1-2-1-5,
  tenzin-dhonzang:c-4-1-6, tsultrim-namdak:c-2-1-2-1-4
- **གཞུང་ལུགས་སོ་སོའི་བཤད་པ།, "three worlds" reading — majority position** (kept:
  dharmabhadra, drakpa-gyaltsen, taranatha) — dropped: gendun-gyatso:c-1-1-8,
  karma-maitri:c-1-1-1-9, konchok-thabkhe:c-2-1-4, palden-sherab:c-3-1-1-1-3,
  pema-namgyal:c-2-4-14, sangye-nyentrul:c-2-0-5, sungrab-tulku:c-4-12,
  tenzin-dhonzang:c-4-1-7

Claim-ID pairings above are taken directly from the v1 reference map's own per-commentary
claim-ID listings (below), matched to the topical label already recorded there (e.g. "Tārā
etym.", "origin, quoted", "three-worlds id."). Where a commentary's contribution to a
specific merged sentence could not be pinned to one single claim ID more precisely than the
v1 map already resolves it, the nearest matching labeled ID from that commentary's own row
is used. This is bookkeeping over already-settled v1 data, not a new extraction.

## Reference map (v1, unchanged — reproduced verbatim as the settled resolution table)

| Ref | Commentary | Claim ID(s) drawn on | Quotation (verbatim བོད་ཡིག, if quoted) | Source block |
|---|---|---|---|---|
| 1 | taranatha | c-1-1 (structural, first homage), c-1-5 ("Mother" epithet, unique), c-1-6 (Swift tied to wisdom-eye, unique), c-1-7 (Tārā etymology, quoted in v1), c-1-8 (four-quality summary), c-1-9 (origin, quoted in v1) | v1 quoted c-1-7 and c-1-9; both now paraphrased in v2 (see Revision note) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^1-0, #^0-4, #^0-5, #^0-6` |
| 2 | yama-sonam | c-3-1-2 (structural), c-3-1-4 (three-greatnesses framing), c-3-1-5 (elaborated Tārā etymology, unique), c-3-1-8 (elaborated Swift etymology, unique), c-3-1-9 (refuge instruction, unique), c-3-1-10–13 (path-completion + vow-based Heroine etymology, unique, c-3-1-11 quoted in v1), c-3-1-14 (wisdom-eye consensus), c-3-1-15 (origin, quoted in v1), c-3-1-17 (three-quality mapping, unique), c-3-1-19 (three-worlds identity + alternate three-realms reading), c-3-1-21–24 (Nyisbepa 8-armed iconography, c-3-1-23/24 quoted in v1) | v1 quoted c-3-1-15, c-3-1-11, c-3-1-23, c-3-1-24; all four now paraphrased in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-6, #^0-14, #^0-15, #^0-16, #^0-18, #^0-19, #^0-21, #^0-22, #^0-23, #^0-24` |
| 3 | palden-sherab | c-3-1-1-0-1 (function phrase), c-3-1-1-1-1 (triad etymology, incl. Heroine/bdud sde), c-3-1-1-1-2 (wisdom-eye), c-3-1-1-1-3 (origin + White/Blue Tārā id.), c-3-1-1-2-1, c-3-1-1-2-3 (Mahāyoga iconography, paraphrased in v1 already) | (none in v1 or v2 — paraphrased only) | `1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་དད་བརྩོན་བྱང་ཆུབ་སེམས་མཆོག་གི་པདྨའི་གཞོན་ནུ་ཁ་འབྱེད་པའི་ཐབས་ཤེས་ཉི་ཟླའི་འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-12, #^0-14, #^0-15, #^0-16, #^0-17, #^0-18` |
| 4 | sangye-nyentrul | c-2-0-1 (identification), c-2-0-2 (Swift), c-2-0-3 (Heroine), c-2-0-4 (wisdom-eye), c-2-0-5 (origin), c-2-1-1 (function phrase, quoted in v1), c-2-1-2 (iconography, quoted in v1) | v1 quoted c-2-1-1 and c-2-1-2; both now paraphrased in v2 | `1-SOURCES/Commentaries/རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།།.md#^0-6, #^0-7, #^0-8, #^0-9` |
| 5 | sungrab-tulku | c-4-3, c-4-4 (unity framing, quoted in v1), c-4-5 (Tārā etym.), c-4-6 (Swift etym.), c-4-7 (Heroine etym.), c-4-9 (wisdom-eye, **quoted — retained in v2**), c-4-11, c-4-12 (three worlds), c-4-13, c-4-14 (origin) | v1 quoted c-4-4 and c-4-9; c-4-4 now paraphrased in v2, **c-4-9 is retained verbatim as one of v2's 2 budgeted quotations** | `1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-17, #^0-18, #^0-19, #^0-20, #^0-22, #^0-23, #^0-24` |
| 6 | tsultrim-namdak | c-2-1-2-1-3 (homage-as-template), c-2-1-2-1-4 (triad etymology), c-2-1-2-1-5 (wisdom-eye + three-realms reading), c-2-1-2-1-6 (origin), c-3-4 (iconography, paraphrased in v1 already) | (none — paraphrased only) | `1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-75, #^0-76, #^0-77, #^0-78, #^0-79` |
| 7 | dharmabhadra | c-1-2-1-1 (threefold division), c-1-2-1-2 (root-verse "dpal mo" variant, **quoted — retained in v2**), c-1-2-1-4 (Tārā etym.), c-1-2-1-5 (Swift, comparative, unique), c-1-2-1-6 ("dpal mo" etymology, quoted in v1), c-1-2-1-7 (wisdom-eye), c-1-2-1-8 (three-worlds id.), c-1-2-1-9 (origin) | v1 quoted c-1-2-1-2 and c-1-2-1-6; **c-1-2-1-2 is retained verbatim as one of v2's 2 budgeted quotations**, c-1-2-1-6 now paraphrased | `1-SOURCES/Commentaries/སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-7, #^0-8, #^0-9, #^0-10, #^0-11` |
| 8 | drakpa-gyaltsen | c-1-1 (Tārā etym.), c-1-2 (Swift etym.), c-1-3 (Heroine etym., quoted in v1), c-1-4 (wisdom-eye), c-1-5–c-1-7 (origin, three-worlds id.) | (none in v2 — v1's c-1-3 quote now paraphrased) | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-5, #^0-6, #^0-7, #^0-8, #^0-9` |
| 9 | gendun-gyatso | c-1-1-3 (Tārā etym.), c-1-1-4 (Swift etym.), c-1-1-5 (Heroine etym.), c-1-1-6 (wisdom-eye), c-1-1-7, c-1-1-8 (origin, three-worlds id.) | (none — paraphrased only) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-5, #^0-6, #^0-7` |
| 10 | karma-maitri | c-1-1-1-5 (Swift etym.), c-1-1-1-6 (Heroine etym.), c-1-1-1-7 (Tārā-from-eye-light etym., unique), c-1-1-1-8, c-1-1-1-9 (origin, three-worlds id.) | (none — paraphrased only) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-3, #^0-4, #^0-5` |
| 11 | konchok-thabkhe | c-2-1-2 (Swift+Heroine combined etym.), c-2-1-3, c-2-1-4 (origin, three-worlds id.), c-2-1-5 (⚑ divergence: whose tears, quoted in v1, both positions) | v1 quoted both positions of c-2-1-5; both now paraphrased in v2 | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-14, #^0-15, #^0-16, #^0-17` |
| 12 | gendun-drub | c-2-2-2-1-1 (threefold division), c-2-2-2-1-2 (root verse), c-2-2-2-1-3 (origin + three-realms reading, quoted in v1), c-2-2-2-1-4 (vow narrative, unique), c-2-2-2-1-5 (attribution) | v1 quoted c-2-2-2-1-3; now paraphrased in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-14, #^0-15, #^0-16, #^0-17` |
| 13 | tenga-tulku | c-1-2-1-1 (threefold division), c-1-2-1-4 (origin), c-1-2-1-5 (Swift/Heroine etym.), c-1-2-1-6 (unceasing compassionate watchfulness, unique) | (none — paraphrased only) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །།.md#^0-7, #^0-13, #^0-14` |
| 14 | tenzin-dhonzang | c-4-1-3 (elaborated ཕྱག/འཚལ gloss; its own quotation reads "མྱུར་མ་དཔལ་མོ", quoted in v1), c-4-1-5 (deity-emanation parallel schema, unique), c-4-1-6 (Heroine etym. + wisdom-eye), c-4-1-7 (origin) | (none in v2 — v1's c-4-1-3 quote now paraphrased) | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-111, #^0-113, #^0-114, #^0-115` |
| 15 | pema-namgyal | c-2-4-4, c-2-4-11 (Tārā/Heroine etym.), c-2-4-12 (wrathful-aspect wisdom-eye, unique), c-2-4-13, c-2-4-14 (origin + White/Blue Tārā id.), c-2-4-15 (homage-as-template) | (none — paraphrased only) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-25, #^0-27, #^0-28, #^0-29` |

## Claims used but not quoted

Unchanged from v1: nearly every claim ID listed above under "Claim ID(s) drawn on" that is
not marked quoted entered (and still enters, in v2) the article as paraphrased
consensus/unique/divergence content, cited via `<ref>` without quotation marks. v2 adds 15
more claims to this paraphrased set — every quotation v1 carried except the two retained
(sungrab-tulku c-4-9, dharmabhadra c-1-2-1-2) is now paraphrase-only, per the Rule 6 budget.

Facets from `tara-01.md` **not** incorporated into the article, unchanged from v1: §2 (the
grammatical "ma"-suffix note), §7 (textual attributions/translator-variant citations,
beyond the "dpal mo" root-verse variant used in the divergence section), §9
(palden-sherab's fourfold outer/inner/secret/ultimate hermeneutical scheme — §10's
path-completion etymology is used but its full four-layer structure from §9 is not
reproduced), and §12 (practice instructions, only glancingly present). These remain
legitimate editorial scope omissions, not unresolved attestations.

## Unresolvable attestations

None, unchanged from v1. All 149 distinct `commentary:claim-id` attestations cited anywhere
on `2-RAILS/Claims/tara-01.md` were located in their corresponding raw tree-guided file in
the v1 run. Mode B performed no new resolution work.

## Warnings

- **`rails_status` is `draft`, not `complete`.** Unchanged from v1: `2-RAILS/Claims/tara-01.md`
  still records `status: draft`. This revision, like the v1 draft it revises, is a risk the
  human reviewer accepts explicitly.
- **v1's two corrected quotations remain corrected.** v1's Warnings recorded that two
  initially-misattributed quotations (the iconography description and the "function"
  phrase, both eventually attributed to `sangye-nyentrul`) were fixed during v1's
  verification pass. Both are now paraphrased rather than quoted in v2, so the correction
  is moot for the final text but the underlying claim attribution (sangye-nyentrul, not
  palden-sherab) is preserved in the paraphrase.
- **No `sources.yaml` / URLs exist for this vault's commentaries** — unchanged from v1; all
  15 refs are hand-formatted `<AUTHOR>། <TITLE>།` with no year/page/URL, per this skill's
  Rule 11. V2 (of the wikitext spec) is treated as not-applicable to this hand-run skill's
  output, as in v1.
- **V8 judgment call, unchanged from v1**: the four tail sections
  (`བསྡུས་དོན།`, `འབྲེལ་ཡོད་ཤོག་ངོས།`, `ལུང་ཁུངས།`, `དཔྱད་གཞིའི་ཡིག་ཆ།`) carry no `<ref>`
  tags, matching the wikitext spec's own skeleton example. All five body sections
  (`མཚན་གྱི་ངེས་ཚིག`, `སྐུ་ཡི་རྣམ་པ།`, `ཕྲིན་ལས་དང་ནུས་མཐུ།`, `ལོ་རྒྱུས།`,
  `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`) carry multiple citations, satisfying V8.
- **Article length**: the v2 body (lead through the divergence section) is shorter than
  v1's ~2,150 syllables (the 15 dropped quotations and capped ref clusters removed
  considerable bulk) but still comfortably above the spec's 1,500-syllable
  non-blocking-warning threshold — no warning needed.
- **`ཕྲིན་ལས་དང་ནུས་མཐུ།`'s closing sentence** ("ཡོན་ཏན་གྱི་གྲངས་དང་སྦྱོར་ཚུལ་...") carries no
  ref of its own — connective content restating material already cited earlier in the same
  section, satisfying V8 at the section level per a reading a strict per-sentence pass would
  flag; noted for the reviewer's judgment, unchanged from v1's own note.
- **V8 fix (post-revision, 2026-08-21): `བསྡུས་དོན།` had zero `<ref>` tags**, failing V8 at
  the section level (not just the sentence level, unlike the `ཕྲིན་ལས་དང་ནུས་མཐུ།` case
  above). Fixed by attaching self-closing reuses of refs already defined earlier in the
  article — `palden-sherab`/`sangye-nyentrul`/`sungrab-tulku` (activity-embodiment claim,
  matching the lead's own citation set), `taranatha`/`yama-sonam`/`sangye-nyentrul`
  (origin-from-tears claim, matching `ལོ་རྒྱུས།`'s opening citation set), and
  `yama-sonam`/`dharmabhadra`/`drakpa-gyaltsen` (wisdom-eye-like-lightning claim, matching
  `སྐུ་ཡི་རྣམ་པ།`'s opening citation set) — no new claim, source, or ref name introduced.
- **`sangye-nyentrul`'s raw file frontmatter has an empty `title_in_english` field** —
  unchanged from v1; bibliography and refs use the Tibetan title only.

## Verification

### v1 quotation verification (unchanged — reproduced for audit continuity)

Every direct quotation in the v1 draft was located character-for-character
(whitespace-collapsed) in the `1-SOURCES/` file its claim's `Cite:` field names.

| # | Commentary | Quotation (first ~40 chars) | v1 Result | v2 status |
|---|---|---|---|---|
| 1 | sungrab-tulku | སྒྲོལ་མ་དང་མྱུར་མ་དཔའ་མོ་བཅས་གསུམ་ནི་མིང་འཇུག་ཚུལ་... | PASS | paraphrased |
| 2 | taranatha | སྒྲོལ་མ་སྟེ་སེམས་ཅན་ཐམས་ཅད་འཁོར་བ་ལས་སྒྲོལ་བའི་ཕྲིན་ལས་ཅན་ནོ། | PASS | paraphrased |
| 3 | drakpa-gyaltsen | དཔའ་མོ་ནི་ཉོན་མོངས་པ་འཇོམས་པས་དཔའ་མོ། | PASS | paraphrased |
| 4 | sungrab-tulku | ཡེ་ཤེས་ཀྱི་སྤྱན་ནི་སྐད་ཅིག་གི་གློག་འཁྱུག་པ... | PASS | **retained verbatim** (v2 quote 1/2) |
| 5 | sangye-nyentrul | སྐུ་མདོག་དམར་མོ་ཁྲོ་འཛུམ་ཆགས་པའི་ཉམས་ཅན...དུང་གཡས་འཁྱིལ | PASS | paraphrased |
| 6 | yama-sonam | མཁའ་དཀྱིལ་གསེར་མདོག་ཆུ་སྐྱེས་གདན...མེ་ཏོག་བརྒྱན། | PASS | paraphrased |
| 7 | yama-sonam | འཕགས་མ་སྒྲོལ་མ་མྱུར་ཞིང་རབ་ཏུ་དཔའ་བ | PASS | paraphrased |
| 8 | sangye-nyentrul | བྱང་ཆུབ་ཀྱི་སེམས་འཕེལ་ཞིང་སྣང་བ་དབང་དུ་སྡུད་པའི་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ་འདི་ཉིད | PASS | paraphrased |
| 9 | taranatha | འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་སྤྱན་རས་གཟིགས་ཀྱི་ཞལ་རས... | PASS | paraphrased |
| 10 | yama-sonam | དེ་བཞིན་འཇིག་རྟེན་གསུམ་མགོན་ཏེ...སྤྱན་ཆབ་ཤོར་བ་ལས། | PASS | paraphrased |
| 11 | yama-sonam | ཡང་ན་ཇི་སྲིད་འཁོར་བ་མ་སྟོང་གི་བར་དུ...དཔའ་མོ་སྟེ། | PASS | paraphrased |
| 12 | dharmabhadra | ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔལ་མོ། | PASS | **retained verbatim** (v2 quote 2/2) |
| 13 | dharmabhadra | བདུད་སྡེ་ལྷག་མེད་དུ་འཇོམས་པས་ན་དཔལ་མོ། | PASS | paraphrased |
| 14 | tenzin-dhonzang | མྱུར་མ་དཔལ་མོ | PASS | paraphrased |
| 15 | konchok-thabkhe | འདིར་གྲུབ་ཆེན་ཉི་མ་སྦས་བས...ཞེས་གསུངས་པ་ལྟར་བྲིས་སོ། | PASS | paraphrased |
| 16 | konchok-thabkhe | འགྲེལ་བ་སྔོན་མ་རྣམས | PASS | paraphrased |
| 17 | gendun-drub | འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པའི་ཁམས་གསུམ་གྱི་མགོན་སྐྱབས | PASS | paraphrased |

**17/17 quotations verified PASS in v1; that verification is treated as settled per Mode B.**

### v2 spot-verification (Mode B step 6 — text diff against the v1 PASS rows, not a fresh `1-SOURCES/` lookup)

| Retained quote | v1 PASS text (row above) | v2 fence-body text | Diff |
|---|---|---|---|
| sungrab-tulku wisdom-eye (row 4) | "ཡེ་ཤེས་ཀྱི་སྤྱན་ནི་སྐད་ཅིག་གི་གློག་འཁྱུག་པ་དང་འདྲ་བར་དུས་གསུམ་ཤེས་བྱ་མཐའ་དག་སྐད་ཅིག་ལ་གཟིགས་པའི་ནུས་པ་ཡོད་པའོ།" | "ཡེ་ཤེས་ཀྱི་སྤྱན་ནི་སྐད་ཅིག་གི་གློག་འཁྱུག་པ་དང་འདྲ་བར་དུས་གསུམ་ཤེས་བྱ་མཐའ་དག་སྐད་ཅིག་ལ་གཟིགས་པའི་ནུས་པ་ཡོད་པའོ།" | identical — exact substring match |
| dharmabhadra root-verse variant (row 12) | "ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔལ་མོ།" | "ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔལ་མོ།" | identical — exact substring match |

Both retained quotations are byte-identical to the text already marked PASS in v1. No new
`1-SOURCES/` lookup was performed, per Mode B step 6.

### v2 mechanical checks (performed on the fence body directly)

- **Comma scan**: no ASCII `,` or full-width `，`/`、` anywhere in the fence body.
- **Ref-cluster scan**: the longest consecutive `<ref>` run in the fence body is 3
  (occurs 8 times); no statement carries more than 3 refs.
- **Named-ref definitions**: exactly one full `<ref name="...">...</ref>` definition per
  each of the 15 names, all others self-closing `<ref name="..." />` — V5 satisfied.
- **Quotation count**: exactly 2 verbatim quotations in the fence body (confirmed by
  isolating `"..."` spans containing Tibetan script, excluding `<ref name="...">` attribute
  quotes) — Rule 6 satisfied. Neither is a lead root-text quotation, so no exemption was
  invoked.
- **Tail order**: `འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`, unchanged — V11
  satisfied.
- **Preview**: `article-preview.md` regenerated via `make_preview.py`; contains no `<ref>`
  tags and no leaked `[[...]]` wikitext links; all 15 named refs render as footnotes with
  author-slug labels.
