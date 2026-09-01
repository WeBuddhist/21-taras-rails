---
topic: vetala
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
source_article: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/vetala/article.md (v1, wiki-article-from-claims, dated 2026-08-12 — revised in place)
revision_date: 2026-08-21
context_packages:
  - 2-RAILS/Claims/vetala.md
rails_status: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/yama-sonam.md
  - 2-RAILS/Claims/raw/tree-guided/dharmabhadra.md
  - 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-drub.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
  - 2-RAILS/Claims/raw/tree-guided/karma-maitri.md
  - 2-RAILS/Claims/raw/tree-guided/konchok-thabkhe.md
  - 2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/pema-namgyal.md
  - 2-RAILS/Claims/raw/tree-guided/sangye-nyentrul.md
  - 2-RAILS/Claims/raw/tree-guided/sungrab-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/tenzin-dhonzang.md
  - 2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md
date: 2026-08-12
status: draft
---

> [!note] Polished — gemini-article-polish, 2026-08-23, model gemini-3.1-pro-preview; claim usage unchanged from 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/vetala/article.md (pre-polish).

# Citations — vetala (རོ་ལངས།)

> **Mode B revision (2026-08-21).** This `citations.md` is the v2 rewrite of the v1 audit
> trail (`wiki-article-from-claims`, 2026-08-12). Per Mode B, the claim-resolution work below —
> reference map, claims-used-but-not-quoted, unresolvable attestations, resolved-but-uncited
> list, and the 12-quotation verification table — is carried forward **unchanged** from the v1
> file as settled ground truth; no claim was re-derived and no `2-RAILS/` file was reopened.
> What changed is register only: the article prose was rewritten into wikivoice per Rules 5–9,
> the quotation count was cut from 12 to 2 (Rule 6), the citation cap of ≤3 refs/statement was
> applied (Rule 7, see *Full attestation beyond in-article refs* below for the three ref
> instances this displaced), the punctuation contract was applied (Rules 15–16), and in-prose
> commentator names were confirmed against `author_in_use` (Rule 17) — see *Author-naming check*
> below, including one correction to a `<ref>` tag's author string that Rule 17 required.

## Reference map

Every `<ref name="...">` in `article.md` is a hand-formatted `<AUTHOR>། <TITLE>།` citation
(no URLs, years, or page numbers exist for any of these 14 commentaries — see Warnings). The
table below maps each ref to every raw claim ID it backs in the article, whether or not that
claim was quoted verbatim. Unchanged from the v1 file except where noted.

| Ref name | Commentary (registered_id) | Claim ID | Quoted in article (v2)? | Quotation (verbatim བོད་ཡིག, if quoted) | Source block |
|---|---|---|---|---|---|
| `yama-sonam` | yama-sonam | c-3-6-3 | Yes (lead) | རྒྱུད་ལས། ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། ། རླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱུག་མཆོད་མ། ། འབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། ། གནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། | `1-SOURCES/Commentaries/སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-66` |
| `yama-sonam` (reuse, bsdus-don) | yama-sonam | c-3-6-3 | No (summary support) | — | same as above |
| `dharmabhadra` | dharmabhadra | c-1-2-2-1-1-5-2 | No (lead support) | — | `1-SOURCES/Commentaries/སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-31` |
| `dharmabhadra` (reuse, lead2) | dharmabhadra | c-1-2-3-6-2 | No (paraphrased in v2 — quoted in v1) | — | `...ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-92` |
| `dharmabhadra` (reuse, position 2) | dharmabhadra | c-1-2-2-1-1-5-5 | No (paraphrased in v2 — quoted in v1) | — | `...ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-33` |
| `dharmabhadra` (reuse, ཕྲིན་ལས) | dharmabhadra | c-1-2-3-6-5 | No (paraphrased in v2 — quoted in v1) | — | `...ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-94` |
| `tenzin-dhonzang` | tenzin-dhonzang | c-4-6-2 | No (lead support) | — | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-150` |
| `tenzin-dhonzang` (reuse, lead2) | tenzin-dhonzang | c-4-21-2 | No (paraphrased in v2 — quoted in v1) | — | `...སྙིང་གི་ནོར་བུ.md#^0-282` |
| `tenzin-dhonzang` (reuse, ཕྲིན་ལས) | tenzin-dhonzang | c-4-21-7 | No (curse-sending support) | — | `...སྙིང་གི་ནོར་བུ.md#^0-287` |
| `palden-sherab` | palden-sherab | c-3-1-6-0-2 | No (lead support in v1; dropped from lead in v2, see below) | — | `1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་དད་བརྩོན་བྱང་ཆུབ་སེམས་མཆོག་གི་པདྨའི་གཞོན་ནུ་ཁ་འབྱེད་པའི་ཐབས་ཤེས་ཉི་ཟླའི་འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-63` |
| `palden-sherab` (reuse, position 4) | palden-sherab | c-3-1-6-1-2 | No (paraphrased in v2 — quoted in v1) | — | `...འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-66` |
| `palden-sherab` (reuse, ཕྲིན་ལས) | palden-sherab | c-3-1-21-1-3 | No (curse-sending support) | — | `...འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-207` |
| `palden-sherab` (reuse, རྫོགས་རིམ) | palden-sherab | c-3-1-6-3-2 | No (paraphrased in v2 — quoted in v1) | — | `...འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-70` |
| `palden-sherab` (reuse, རྫོགས་རིམ) | palden-sherab | c-3-1-21-4-2 | No (paraphrased in v2 — quoted in v1) | — | `...འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-213` |
| `gendun-drub` | gendun-drub | c-2-2-2-3-6-2 | No (lead2 support) | — | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-104` |
| `gendun-drub` (reuse, position 1) | gendun-drub | c-2-2-2-2-1-1-5-3 | No (position 1 support) | — | `...ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-37` |
| `tsultrim-namdak` | tsultrim-namdak | c-2-1-2-1-71 | No (lead2 support in v1; dropped from lead2 in v2, see below) | — | `1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-147` |
| `tsultrim-namdak` (reuse, position 1) | tsultrim-namdak | c-2-1-2-1-22 | No (position 1 support) | — | `...གྲུ་གཟིངས།.md#^0-96` |
| `pema-namgyal` | pema-namgyal | c-2-4-55 | No (paraphrased in v2 — quoted in v1) | — | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-69` |
| `pema-namgyal` (reuse, ཕན་ཡོན) | pema-namgyal | c-2-4-25 | No (paraphrased in v2 — quoted in v1) | — | `...བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-39` |
| `drakpa-gyaltsen` | drakpa-gyaltsen | c-1-41 | No (paraphrased in v2 — quoted in v1) | — | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-35` |
| `lobsang-dawa` | lobsang-dawa | c-1-2-2-1-1-5-3 | No (position 2 support) | — | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-12` |
| `lobsang-dawa` (v1 only, ཕྲིན་ལས — dropped in v2 cap) | lobsang-dawa | c-1-2-3-6-3 | No | — | `...མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-30` |
| `sungrab-tulku` | sungrab-tulku | c-9-7 | No (position 2 support) | — | `1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-51` |
| `karma-maitri` | karma-maitri | c-1-1-6-10 | No (paraphrased in v2 — quoted in v1) | — | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-16` |
| `gendun-gyatso` | gendun-gyatso | c-1-6-2 | No (position 3 support) | — | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-15` |
| `sangye-nyentrul` | sangye-nyentrul | c-7-0-2 | No (position 4 support) | — | `1-SOURCES/Commentaries/རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།།.md#^0-29` |
| `konchok-thabkhe` | konchok-thabkhe | c-2-6-3 | **Yes (position 5)** | རོ་ལངས་ཞོན་པའི་སྲིན་པོ | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-38` |

14 distinct commentaries cited (unchanged from v1); 22 claim-ID uses (unchanged); **2 direct
verbatim quotations in v2** (down from 12 in v1, per Rule 6's budget). `lobsang-dawa:c-1-2-3-6-3`
is resolved and attested but no longer holds a ref slot in the v2 article body (see *Full
attestation beyond in-article refs* — the ཕྲིན་ལས་དང་གནོད་པ statement was capped to 3 refs).

## Claims used but not quoted

Content entered the prose paraphrased (not verbatim), cited by ref only. Unchanged from v1
except that 10 claims formerly quoted verbatim in v1 are now paraphrased here too (listed with
their section, since v1 only tracked the always-paraphrased set):

- **Lead** — `dharmabhadra:c-1-2-2-1-1-5-2`, `tenzin-dhonzang:c-4-6-2` (fourfold-host support;
  `palden-sherab:c-3-1-6-0-2` also attests this but was capped out of the v2 lead's 3-ref limit —
  see overflow below); `dharmabhadra:c-1-2-3-6-2`, `gendun-drub:c-2-2-2-3-6-2` (destroyed-by-mantra
  support; `tsultrim-namdak:c-2-1-2-1-71` also attests this but was capped out — see overflow
  below); the verse itself (`yama-sonam:c-3-6-3`) is quoted, not paraphrased
- **དབྱེ་བ** — `pema-namgyal:c-2-4-55` (paraphrased in v2; quoted verbatim in v1)
- **གཞུང་ལུགས་སོ་སོའི་བཤད་པ** — `drakpa-gyaltsen:c-1-41` (paraphrased in v2; quoted in v1),
  `gendun-drub:c-2-2-2-2-1-1-5-3`, `tsultrim-namdak:c-2-1-2-1-22` (position 1, Maheśvara-headed);
  `dharmabhadra:c-1-2-2-1-1-5-5` (paraphrased in v2; quoted in v1), `lobsang-dawa:c-1-2-2-1-1-5-3`,
  `sungrab-tulku:c-9-7` (position 2, rākṣasa retinue); `karma-maitri:c-1-1-6-10` (paraphrased in v2;
  quoted in v1), `gendun-gyatso:c-1-6-2` (position 3, charnel-ground dweller);
  `palden-sherab:c-3-1-6-1-2` (paraphrased in v2; quoted in v1), `sangye-nyentrul:c-7-0-2`
  (position 4, directional/Legden); position 5 (`konchok-thabkhe:c-2-6-3`) remains quoted in v2
  — the one identity-position quotation retained, since its formulation is the article's most
  genuinely divergent claim (Rule 6)
- **ཕྲིན་ལས་དང་གནོད་པ** — `dharmabhadra:c-1-2-3-6-5` (paraphrased in v2; quoted in v1),
  `palden-sherab:c-3-1-21-1-3`, `tenzin-dhonzang:c-4-21-7` (curse-sending sorcery, now stated in
  wikivoice as consensus per Rule 5 — no inline attribution in v2, refs only);
  `lobsang-dawa:c-1-2-3-6-3` also attests this but was capped out of the 3-ref limit — see
  overflow below
- **ཕན་ཡོན** — `pema-namgyal:c-2-4-25` (paraphrased in v2; quoted in v1)
- **རྫོགས་རིམ་གྱི་བརྡ་དོན** — `palden-sherab:c-3-1-6-3-2`, `palden-sherab:c-3-1-21-4-2` (both
  paraphrased in v2 as "ཐིག་ལེ" / "ལས"; both quoted verbatim in v1)

## Full attestation beyond in-article refs

New in v2 (Rule 7 / the citation cap). Three ref instances that appeared in the v1 article were
displaced when a statement's ref count was capped to the v2 limit of 3. No attestation is lost —
each remains resolved in its raw tree-guided file and is listed here:

- **Lead, fourfold-host statement** — capped to `yama-sonam:c-3-6-3`, `dharmabhadra:c-1-2-2-1-1-5-2`,
  `tenzin-dhonzang:c-4-6-2` (3 refs). Displaced: `palden-sherab:c-3-1-6-0-2`.
- **Lead, destroyed-by-mantra statement** — capped to `tenzin-dhonzang:c-4-21-2`,
  `dharmabhadra:c-1-2-3-6-2`, `gendun-drub:c-2-2-2-3-6-2` (3 refs). Displaced:
  `tsultrim-namdak:c-2-1-2-1-71`.
- **ཕྲིན་ལས་དང་གནོད་པ, curse-sending statement** — capped to `dharmabhadra:c-1-2-3-6-5`,
  `palden-sherab:c-3-1-21-1-3`, `tenzin-dhonzang:c-4-21-7` (3 refs). Displaced:
  `lobsang-dawa:c-1-2-3-6-3`.

All five identity-position statements in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ` already carried ≤3 refs in v1
and needed no capping.

## Unresolvable attestations

None. Every attestation ID appearing anywhere on `2-RAILS/Claims/vetala.md` (44 total,
across the 14 sources listed in that page's `sources:` frontmatter) was located and resolved
in its raw tree-guided claims file. (Carried forward unchanged from v1 — Mode B did not reopen
`2-RAILS/Claims/`.)

## Resolved claims not cited in the final draft

Unchanged from v1 — these attestation IDs from `2-RAILS/Claims/vetala.md` were resolved but not
selected for citation in either version of `article.md`:

`yama-sonam:c-3-6-6`, `yama-sonam:c-3-21-3`, `drakpa-gyaltsen:c-1-99`,
`gendun-drub:c-2-2-2-3-6-1`, `gendun-gyatso:c-1-21-2`, `karma-maitri:c-1-1-21-3`,
`konchok-thabkhe:c-2-6-6`, `konchok-thabkhe:c-2-21-3`, `palden-sherab:c-3-1-21-0-2`,
`palden-sherab:c-3-1-21-2-2`, `palden-sherab:c-3-1-21-3-2`, `sangye-nyentrul:c-22-0-2`,
`sungrab-tulku:c-9-6`, `sungrab-tulku:c-24-4`, `tenzin-dhonzang:c-4-6-4`,
`tsultrim-namdak:c-2-1-2-1-74`, `tsultrim-namdak:c-3-24`.

No claim was dropped for failing resolution — all of the above resolved cleanly; they were
simply not needed once representative citations were selected. None of them contradict what
the article says.

## Author-naming check (Rule 17)

All 14 raw claims files carry their own `author_in_use` key (none predate the key, so the
`source_file` frontmatter fallback was never needed — no warnings to log for this rule):

| registered_id | `author_in_use` | Used in v2 prose? |
|---|---|---|
| yama-sonam | རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་ | No in-prose mention (wikivoice only; ref-only citation) |
| dharmabhadra | དངུལ་ཆུ་དྷརྨ་བྷ་དྲ་ | Yes — `གཞུང་ལུགས་སོ་སོའི་བཤད་པ`, position 2 |
| drakpa-gyaltsen | རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་ | Yes — position 1 |
| gendun-drub | རྒྱལ་བ་དགེ་འདུན་གྲུབ་ | Yes — position 1 |
| gendun-gyatso | རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ་ | Yes — position 3 |
| karma-maitri | ཀརྨ་མཻ་ཏྲི་ | Yes — position 3 |
| konchok-thabkhe | དཀོན་མཆོག་ཐབས་མཁས་ | Yes — position 5 |
| lobsang-dawa | དགེ་བཤེས་བློ་བཟང་ཟླ་བ་ | Yes — position 2 |
| palden-sherab | མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་ | Yes — position 4; also `རྫོགས་རིམ་གྱི་བརྡ་དོན` |
| pema-namgyal | ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་ | Yes — `དབྱེ་བ`; also `ཕན་ཡོན` |
| sangye-nyentrul | སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ་ | Yes — position 4 |
| sungrab-tulku | འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་ | Yes — position 2 |
| tenzin-dhonzang | སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་ | No in-prose mention (wikivoice only; ref-only citation) |
| tsultrim-namdak | མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་ | Yes — position 1 |

All 8 in-prose mentions in the v2 article already matched their `author_in_use` value exactly —
v1's drafter had, in fact, already used these forms for every named-commentator sentence (this
predates the skill's Rule 17, but the values happen to coincide). No name was invented,
translated, or upgraded. No fallback to bare `author` was needed anywhere.

**One correction made:** the `<ref name="pema-namgyal">` tag in v1 read
`ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ། [title]།` — i.e. it used the `author_in_use` form inside the `<ref>`
tag itself, inconsistent with the `དཔྱད་གཞིའི་ཡིག་ཆ` bibliography line for the same commentary,
which correctly used the formal `author` field (`ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ་`). Per Rule 17's last
sentence ("`<ref>` content and the `དཔྱད་གཞིའི་ཡིག་ཆ` bullets keep the formal `author` + title
unchanged — `author_in_use` is for prose mentions only"), the v2 `<ref name="pema-namgyal">` tag
was corrected to `ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ། ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ།`,
now matching the bibliography line and the raw claims file's `author` field exactly. This is the
only content change made to any `<ref>` tag's citation text in the v2 revision — every other ref
tag's `<AUTHOR>། <TITLE>།` string is byte-identical to v1.

## Warnings

1. **`rails_status: draft`.** The consolidated page `2-RAILS/Claims/vetala.md` is `status: draft`,
   not `complete` (unchanged since v1). A human contributor is accepting this risk by having this
   draft regenerated against a non-`complete` page.
2. **No URLs, years, or page numbers exist for any of the 14 cited commentaries** (unchanged).
3. **`yama-sonam`'s author is རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་** (unchanged from v1; carried forward).
4. **Article length.** The v2 body is shorter than v1's (12 quotations cut to 2, several
   attribution-heavy paragraphs merged into wikivoice); still well under the spec's non-blocking
   1,500-syllable threshold.
5. **Two commentaries in the consolidated page's own source list contributed nothing here**
   (`taranatha`, `tenga-tulku` — unchanged from v1).
6. **bo.wikipedia status (informational only, unchanged from v1).** Existing article རོ་ལངས་
   found at inventory time; this draft remains independently produced and unmerged.
7. **Position 5 (konchok-thabkhe) is preserved unharmonized** (unchanged from v1) — and is now
   the article's sole retained identity-position quotation, since Rule 6 favors spending the
   quotation budget on the position whose exact wording is most distinctively at odds with the
   other four.
8. **`palden-sherab`'s two rdzogs-rim glosses are internally inconsistent** (unchanged
   substantively from v1) — in v2 both are paraphrased ("ཐིག་ལེ" / "ལས") rather than quoted
   verbatim, since the inconsistency is fully legible from the paraphrase and the article's
   2-quote budget was better spent on the identity divergence (position 5) and the root-verse
   attestation (lead).

## Verification

Carried forward unchanged from v1 — every quotation retained through this Mode B revision was
already verified character-for-character against its `1-SOURCES/` file. Per Mode B step 6, the
two quotations kept in v2 were spot-checked as unchanged exact substrings of their v1 PASS
entries (rows 1 and 8 below), not re-verified from scratch:

| # | Commentary | Claim ID | Quotation (as used in v1) | Kept verbatim in v2? | v1 Result |
|---|---|---|---|---|---|
| 1 | yama-sonam | c-3-6-3 | རྒྱུད་ལས། ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ།...མདུན་ནས་བསྟོད་མ། | **Yes — spot-checked, exact substring match** | PASS |
| 2 | tenzin-dhonzang | c-4-21-2 | ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པས།...འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ། | No — cut, paraphrased in v2 lead | PASS (v1; not re-checked, quote removed) |
| 3 | pema-namgyal | c-2-4-55 | ནམ་གྲུ་ལ་སོགས་པའི་གདོན་ཆེན་བཅོ་བརྒྱད་...གདུག་རྩུབ་ཅན་ཐམས་ཅད | No — cut, paraphrased in v2 དབྱེ་བ | PASS (v1; not re-checked, quote removed) |
| 4 | drakpa-gyaltsen | c-1-41 | རོ་ལངས་ནི་དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའོ། | No — cut, paraphrased in v2 position 1 | PASS (v1; not re-checked, quote removed) |
| 5 | dharmabhadra | c-1-2-2-1-1-5-5 | སྲིན་པོའི་འཁོར་རོ་ལངས་རྣམས | No — cut, paraphrased in v2 position 2 | PASS (v1; not re-checked, quote removed) |
| 6 | karma-maitri | c-1-1-6-10 | དུར་ཁྲོད་ན་གནས་པའི་རོ་ལངས | No — cut, paraphrased in v2 position 3 | PASS (v1; not re-checked, quote removed) |
| 7 | palden-sherab | c-3-1-6-1-2 | རོ་ལངས་ནི་ལྷོ་ནུབ་བདེན་དང་བྲལ་བ་ལེགས་ལྡན་འཁོར་ལྷའི་སྲིན་པོ་རིག་སྔགས་མཐུ་གྲུབ་པ་ཅན | No — cut, paraphrased in v2 position 4 | PASS (v1; not re-checked, quote removed) |
| 8 | konchok-thabkhe | c-2-6-3 | རོ་ལངས་ཞོན་པའི་སྲིན་པོ | **Yes — spot-checked, exact substring match** | PASS |
| 9 | dharmabhadra | c-1-2-3-6-5 | རོ་ལངས་ཀྱི་ལས་རྦོད་གཏོང་ལ་སོགས་པའི་ངན་སྔགས་ | No — cut, paraphrased in v2 ཕྲིན་ལས | PASS (v1; not re-checked, quote removed) |
| 10 | pema-namgyal | c-2-4-25 | དེ་དག་གི་འཇིགས་པ་ལས་འདི་དང་ཚེ་རབས་ཀུན་ཏུ་བྲལ་ལོ། | No — cut, paraphrased in v2 ཕན་ཡོན | PASS (v1; not re-checked, quote removed) |
| 11 | palden-sherab | c-3-1-6-3-2 | རོ་ལངས་ཐིག་ལེ་དང་། | No — cut, paraphrased in v2 རྫོགས་རིམ | PASS (v1; not re-checked, quote removed) |
| 12 | palden-sherab | c-3-1-21-4-2 | རོ་ལངས་ནི་ལས་དང་། | No — cut, paraphrased in v2 རྫོགས་རིམ | PASS (v1; not re-checked, quote removed) |

**2/2 retained quotations spot-checked as unchanged exact substrings of their v1 PASS entries.**
No quotation text was altered; 10 of the original 12 were removed (not re-verified, per Mode B
step 6 — removed quotations need no re-check) and their content preserved as paraphrase, still
cited to the same claim IDs.

## Spec validator walk (V1–V12, informal self-check, v2)

- V1 — PASS: both retained quotations spot-checked as exact substrings of their v1 PASS entries (Verification table above)
- V2 — N/A in this skeleton: no `sources.yaml` mapping in play for this keyword-topic track; every ref is instead resolved through the reference map above
- V3 — PASS: `<references />` present, `<ref>` tags present
- V4 — PASS: no `{{Reflist}}` anywhere
- V5 — PASS: all 14 named refs have exactly one full definition (first occurrence), all reuses self-closing
- V6 — PASS: 9 `==` headings (unchanged from v1)
- V7 — PASS: 1 category, `ནང་ཆོས།`, from the allowlist
- V8 — PASS for all content sections (lead through བསྡུས་དོན, each ≥1 citation); the three fixed tail sections carry no citations by design, matching this vault's own prior `three-jewels` term-article and the spec's own skeleton exemplar
- V9 — PASS: Tibetan script only outside ref content, which is itself entirely Tibetan (no URLs exist)
- V10 — PASS: tsheg present at every `'''` and `[[` boundary
- V11 — PASS: tail order is `འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`
- V12 — PASS: no `dummy.com`, no placeholder text, no leftover model chatter

## v2 style self-check (Rules 5–9, 15–17)

- **Quotation budget (Rule 6):** 2/2 — verified by direct count of Tibetan-content quote-mark
  pairs inside the fence (script-checked; the fence's other 24 `"` characters are all `name="..."`
  ref-tag attribute delimiters, not content quotations).
- **Citation cap (Rule 7):** every statement in the article carries ≤3 refs — verified by
  enumerating each sentence's ref cluster (lead: 3+3; དབྱེ་བ: 1; positions 1–5: 3/3/2/2/1;
  ཕྲིན་ལས: 3; ཕན་ཡོན: 1; རྫོགས་རིམ: 1; བསྡུས་དོན: 1).
- **Wikivoice for consensus (Rule 5):** the ཕྲིན་ལས་དང་གནོད་པ statement (curse-sending sorcery,
  attested by 4 commentaries with no dissent) was converted from v1's attributed framing
  ("... ཞེས་བཤད་ལ། ... ཀྱིས་ཀྱང་མཐུན་པར་བཤད།") to a single wikivoice sentence carrying no
  commentator names, refs only. The five-way identity divergence in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ`
  keeps full inline attribution for every position, per Rule 5's ⚑-divergence carve-out — never
  flattened, never adjudicated.
- **Prose before fragments (Rule 8):** the five identity positions, formerly five separate
  one-claim paragraphs in v1, are merged into two connected paragraphs of flowing attributed
  prose in v2.
- **Punctuation contract (Rules 15–16):** no comma character appears anywhere inside the
  ` ```wikitext ` fence (the three commas present in the file are all in the English Obsidian
  note callout above the fence, outside its scope); all 8 body paragraphs end with a double
  shad `།།`; no punctuation character follows any `<ref>` tag anywhere in the fence.
- **Author-naming (Rule 17):** see *Author-naming check* above — all 8 in-prose mentions use
  `author_in_use`; one `<ref>`-tag correction made (pema-namgyal, see above); no warnings to log.
