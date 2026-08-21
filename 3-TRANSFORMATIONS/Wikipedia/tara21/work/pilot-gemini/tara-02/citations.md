---
topic: tara-02
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
revised_from: article.md (v1, method wiki-article-from-claims, dated 2026-08-10)
revision_date: 2026-08-20
context_packages:
  - 2-RAILS/Claims/tara-02.md
rails_status: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/yama-sonam.md
  - 2-RAILS/Claims/raw/tree-guided/dharmabhadra.md
  - 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-drub.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
  - 2-RAILS/Claims/raw/tree-guided/karma-maitri.md
  - 2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/pema-namgyal.md
  - 2-RAILS/Claims/raw/tree-guided/sangye-nyentrul.md
  - 2-RAILS/Claims/raw/tree-guided/sungrab-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/taranatha.md
  - 2-RAILS/Claims/raw/tree-guided/tenzin-dhonzang.md
  - 2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md
date: 2026-08-10
status: draft
---

> [!note] Polished — gemini-article-polish, 2026-08-21, model gemini-3.1-pro-preview; claim usage unchanged from 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-02/article.md.

# Citations — tara-02

## Post-audit fixes (2026-08-20)

A read-only audit of the Mode B revision (below) found two defects, both fixed in place; no
claim ID, quotation, or citation was added or removed.

1. **Rule 5 (wikivoice) — `མཚན་གྱི་ངེས་ཚིག`, "དབྱངས་ཅན་མ" naming sentence.** This statement is
   documented above (§"Full attestation beyond in-article refs") as a consensus statement capped
   to 3 representative refs (`palden-sherab`, `sangye-nyentrul`, `tsultrim-namdak`; `sungrab-tulku`
   dropped for the cap), yet the drafted prose named all three commentators in an attribution
   chain ("མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་ཀྱིས་...གདགས་ཤིང ... སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ ... དང་མཁན་པོ་ཚུལ་
   ཁྲིམས་རྣམ་དག་བཅས་ཀྱིས་ཀྱང་...གདགས་སོ།།"). Rewritten to a plain wikivoice assertion
   ("བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་མཚན་གྱིས་གདགས་སོ།།") with the same three `<ref>` tags, unchanged
   content, carrying the support silently — matching how the article already handles the
   body-colour consensus sentence in `སྐུ་ཡི་རྣམ་པ`. The section's opening sentence ("འདིའི་མཚན་ལ་
   གཞུང་ལུགས་སོ་སོས་མི་འདྲ་བར་གདགས་ཏེ་མཚན་གཅིག་ཏུ་མ་གྲུབ།") was left unchanged — it introduces the
   section's genuine cross-commentary naming divergence (this "Yangchenma" consensus among three
   commentators sits alongside the differently named "Karmo Dangden Drolma" and "Zhiwa Chenmo"
   documented later in the same section), not the capped consensus statement itself.
2. **Rule 17 (author naming) — four `<ref>` tag definitions carried the wrong author form.**
   `<ref>` content must use the formal `author` frontmatter value (never `author_in_use`, which is
   reserved for in-prose mentions per Rule 17's last sentence). Fixed against each raw claims
   file's frontmatter in `2-RAILS/Claims/raw/tree-guided/`:
   - `taranatha`: `ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ།` (that commentary's `author_in_use`, wrongly used in the ref) →
     `ཏཱ་ར་ནཱ་ཐ` (its `author`).
   - `pema-namgyal`: `ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ།` (`author_in_use`) → `ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ`
     (`author`).
   - `gendun-drub`: `རྒྱལ་བ་དགེ་འདུན་གྲུབ།` (missing the frontmatter's Dalai Lama parenthetical) →
     `རྒྱལ་བ་དགེ་འདུན་གྲུབ (ཏཱ་ལའི་བླ་མ་སྐུ་ཕྲེང་དང་པོ)` (full `author`).
   - `gendun-gyatso`: `རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ།` (missing the parenthetical) →
     `རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ (ཏཱ་ལའི་བླ་མ་སྐུ་ཕྲེང་གཉིས་པ)` (full `author`).

   Only each name's first/full `<ref>` definition was touched; later bare `<ref name="..." />`
   reuses need no change since they carry no author text. The same wrong forms were also found
   and fixed in the `དཔྱད་གཞིའི་ཡིག་ཆ།` bibliography for `gendun-drub` and `gendun-gyatso` (which
   were missing the parenthetical); the bibliography entries for `taranatha` and `pema-namgyal`
   were already in the correct formal form and were not touched. All in-prose commentator mentions
   (e.g. `ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ་དང་...` in `སྦས་དོན་གྱི་བཤད་པ།`, `ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་གྱི་...` in
   `ཕྲིན་ལས་དང་ནུས་མཐུ།`, `རྒྱལ་བ་དགེ་འདུན་གྲུབ་...` in `མཚན་གྱི་ངེས་ཚིག`) already correctly used
   `author_in_use` and were left untouched.

The preview (`article-preview.md`) was regenerated after these fixes.

## Mode B revision note (2026-08-20)

Rewritten in place from the v1 `wiki-article-from-claims` draft to the v2 register (wikivoice
consensus, ≤2 commentary quotations, ≤3 refs/statement, sentence-final shad / paragraph-final
ཉིས་ཤད, no commas, `author_in_use` names). No claim ID was introduced that was not already in the
v1 reference map below; the reference map, "claims used but not quoted," and verification table
below are carried forward from the v1 audit and are still accurate for every claim ID cited in the
revised `article.md`. Three quotations that appeared verbatim in v1 were converted to paraphrase
under the Rule 6 budget (see "Quotation budget" below); the root-verse quotation in the lead is
unchanged and is exempt from the budget.

## Reference map

| Ref (named) | Commentary | Claim ID(s) used in article | Quotation (verbatim བོད་ཡིག, if quoted) | Source block |
|---|---|---|---|---|
| taranatha | taranatha | c-2-1, c-2-3, c-2-4, c-2-5, c-2-6, c-2-7 | — (paraphrased throughout) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-19–^0-31 (per claim) |
| sungrab-tulku | sungrab-tulku | c-5-1, c-5-3 | — (paraphrased) | 1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-25, ^0-27 |
| tenzin-dhonzang | tenzin-dhonzang | c-4-2-1, c-4-2-4, c-4-2-5, c-4-2-6, c-4-2-7 | "ཞི་བ་ཆེན་མོ" (unquoted-in-prose but verbatim, from c-4-2-1) | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-116 (and ^0-119–^0-122 for other claims) |
| yama-sonam | yama-sonam | c-3-2-3, c-3-2-4, c-3-2-5, c-3-2-6, c-3-2-7, c-3-2-8, c-3-2-9, c-3-2-10, c-3-2-11 | "ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། ། གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། ། སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས།། རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ།" (c-3-2-3); "ཞལ་གསུམ་དཀར་སྔོ་གསེར་མདོག་ཅན། ། བཅུ་གཉིས་ཕྱག་མངའ་མཉམ་གཞག་དང་། ། ཁ་ཊཱཾ་འཁོར་ལོ་རིན་ཆེན་ཉིད། ། རྡོ་རྗེ་མེ་ཏོག་ཕྲེང་འཛིན་གཡས། ། རིལ་བ་ཨཏྤལ་དྲིལ་བུ་དང་། ། བུམ་པ་དང་ནི་པོ་ཏི་གཡོན།" (c-3-2-11); "འགྲེལ་མཛད་མཁན་དག" (c-3-2-5) | 1-SOURCES/Commentaries/སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-26 (c-3-2-3); #^0-31 (c-3-2-11); #^0-28 (c-3-2-5) |
| dharmabhadra | dharmabhadra | c-1-2-2-1-1-1-5, c-1-2-2-1-1-1-6 | — (paraphrased) | 1-SOURCES/Commentaries/སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-15, ^0-16 |
| palden-sherab | palden-sherab | c-3-1-2-0-1, c-3-1-2-1-2, c-3-1-2-2-1, c-3-1-2-2-2, c-3-1-2-3-1, c-3-1-2-4-1, c-3-1-2-4-2 | "གཉིས་པ་བློ་གཏེར་དབྱངས་ཅན་མ་ནི།" (c-3-1-2-0-1) | 1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ་དད་བརྩོན་བྱང་ཆུབ་སེམས་མཆོག་གི་པདྨའི་གཞོན་ནུ་ཁ་འབྱེད་པའི་ཐབས་ཤེས་ཉི་ཟླའི་འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-25 (c-3-1-2-0-1); #^0-28–^0-32 (other claims) |
| sangye-nyentrul | sangye-nyentrul | c-3-0-2, c-3-1-1, c-3-1-2, c-3-1-3 | — (paraphrased) | 1-SOURCES/Commentaries/རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།།.md#^0-12, ^0-13 |
| tsultrim-namdak | tsultrim-namdak | c-3-5 | — (paraphrased) | 1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-183–^0-185 |
| gendun-drub | gendun-drub | c-2-2-2-2-1-1-1-5, c-2-2-2-2-1-1-1-3 | "འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།" (c-2-2-2-2-1-1-1-5) | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-22 |
| lobsang-dawa | lobsang-dawa | c-1-2-2-1-1-1-6 | "འོད་རབ་འབར་མ" (unquoted-in-prose but verbatim, part of the verse's own closing words) | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-8 |
| karma-maitri | karma-maitri | c-1-1-2-2 | — (paraphrased) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-6 |
| pema-namgyal | pema-namgyal | c-2-4-17 | — (paraphrased) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-31 |
| drakpa-gyaltsen | drakpa-gyaltsen | c-1-11 | — (paraphrased) | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-13 |
| gendun-gyatso | gendun-gyatso | c-1-2-2 | "དེ་ལ་ཡང་སྐར་མ་སྟོང་གུས་པ་རྣམས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་སྟེ་བརྒྱན་པ་ལྟ་བུའི་འོད་དཀར་པོ་རབ་ཏུ་འབར་བའི་སྒྲོལ་མ་ལའོ།" (c-1-2-2) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-9 |

## Claims used but not quoted (paraphrased content, per section)

- **Lead:** taranatha:c-2-1, sungrab-tulku:c-5-1, tenzin-dhonzang:c-4-2-1 (second-of-21 identification); dharmabhadra:c-1-2-2-1-1-1-5/-6 (radiance description)
- **མཚན་གྱི་ངེས་ཚིག:** sangye-nyentrul:c-3-0-2, sungrab-tulku:c-5-3, tsultrim-namdak:c-3-5 (Dbyangs-can-ma naming); yama-sonam:c-3-2-7 (naming survey / confirmation of Gendun Drub's tradition); lobsang-dawa:c-1-2-2-1-1-1-6 (epithet from verse's own words)
- **སྐུ་ཡི་རྣམ་པ:** yama-sonam:c-3-2-4 (basic simile), karma-maitri:c-1-1-2-2, taranatha:c-2-3/c-2-5 (white body); sangye-nyentrul:c-3-1-2, palden-sherab:c-3-1-2-2-1, tsultrim-namdak:c-3-5 (simple one-face-two-hand form); yama-sonam:c-3-2-8, c-3-2-9, c-3-2-10 (elaborate three-face-twelve-arm form, hand-implement list)
- **ཕྲིན་ལས་དང་ནུས་མཐུ:** palden-sherab:c-3-1-2-2-2, sangye-nyentrul:c-3-1-3, tenzin-dhonzang:c-4-2-4 (dispels ignorance); sangye-nyentrul:c-3-1-1 (increases insight); tenzin-dhonzang:c-4-2-6, c-4-2-7 (ransom practice, chief activity)
- **སྦས་དོན་གྱི་བཤད་པ:** taranatha:c-2-6/c-2-7, palden-sherab:c-3-1-2-3-1 (completion-stage-with-marks); palden-sherab:c-3-1-2-2-1 (generation-stage identity, reused), c-3-1-2-4-1 (ultimate-tier identity)
- **གཞུང་ལུགས་སོ་སོའི་བཤད་པ:** gendun-drub:c-2-2-2-2-1-1-1-3, drakpa-gyaltsen:c-1-11, taranatha:c-2-4 (Position A, light surpasses stars); yama-sonam:c-3-2-6 (own "vividly manifest" reading); palden-sherab:c-3-1-2-1-2, sangye-nyentrul:c-3-0-2 (four correct discernments); tenzin-dhonzang:c-4-2-5 (four kinds of wisdom)
- **བསྡུས་དོན:** yama-sonam:c-3-2-4/c-3-2-7, gendun-drub:c-2-2-2-2-1-1-1-5, taranatha, palden-sherab (summary reuse of already-cited facts)

## Quotation budget (Rule 6)

The revised article carries exactly 2 commentary quotations (plus the exempt root-verse
quotation in the lead, unchanged):

1. **Retained** — `gendun-drub:c-2-2-2-2-1-1-1-5` ("འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།"),
   in `མཚན་གྱི་ངེས་ཚིག` — a unique alternate name, exact wording is the point.
2. **Retained** — `yama-sonam:c-3-2-11` (the three-face/twelve-arm iconography verse), in
   `སྐུ་ཡི་རྣམ་པ` — a unique, fully enumerated alternate iconographic form; exact wording of the
   implement list is the point.

Converted from verbatim quotation to attributed paraphrase (content unchanged, no new claim
content added):

- `palden-sherab:c-3-1-2-0-1` ("གཉིས་པ་བློ་གཏེར་དབྱངས་ཅན་མ་ནི།") — a bare structural/ordinal
  marker; paraphrased into wikivoice "བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་མཚན་གྱིས་གདགས་སོ།" (see the 2026-08-20
  post-audit fix note below — this was briefly an attributed paraphrase naming Palden Sherab and
  was corrected to plain wikivoice per Rule 5, since citations.md itself treats this as a
  consensus statement capped to 3 representative refs).
- `gendun-gyatso:c-1-2-2` ("དེ་ལ་ཡང་སྐར་མ་སྟོང་གུས་པ་...འོད་དཀར་པོ་རབ་ཏུ་འབར་བའི་སྒྲོལ་མ་ལའོ།") —
  paraphrased into "རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོས་ནི་སྐར་མས་བརྒྱན་པའི་དོན་དུ་བཤད་དོ།".
- `yama-sonam:c-3-2-5` ("འགྲེལ་མཛད་མཁན་དག") — a two-word fragment naming unspecified prior
  commentators; paraphrased into "སྔ་མའི་འགྲེལ་མཛད་རྣམས་ལ་སྐྱོན་དུ་བརྗོད་དེ" without quotation marks.

## Full attestation beyond in-article refs (Rule 7 citation-cap overflow)

Two consensus statements in the revised article were capped to 3 representative refs; the
remaining resolved attestations for the same statement are preserved here so nothing already
resolved is lost:

- **`མཚན་གྱི་ངེས་ཚིག`, "དབྱངས་ཅན་མ" naming (sentence 1):** cited to `palden-sherab`, `sangye-nyentrul`,
  `tsultrim-namdak` in-article; `sungrab-tulku:c-5-3` also attests this same naming (resolved,
  paraphrase-equivalent to the cited three) but was dropped from the in-article ref list to hold
  the cap at 3.
- **`སྐུ་ཡི་རྣམ་པ`, body-colour consensus ("སྐུ་མདོག་ཡང་དཀར་པོར་མཐུན་པར་བཤད"):** cited to
  `sangye-nyentrul`, `palden-sherab`, `taranatha` in-article; `tsultrim-namdak:c-3-5` also attests
  the same white-body-colour consensus (resolved) but was dropped from this statement's ref list
  to hold the cap at 3 — it remains cited elsewhere in the article for other content.

## Resolved claims not used in the article (due-weight / space selection — not unresolvable)

These attestations from `2-RAILS/Claims/tara-02.md` were successfully resolved to their raw tree-guided files (བོད་ཡིག, English gloss, and `Cite:` all located) but were not incorporated into the drafted prose, mainly to keep the article to a manageable length and to avoid restating near-duplicate consensus points already covered by the representative citations used:

- **Structural placement (the whole facet):** yama-sonam:c-3-2-1, karma-maitri:c-1-1-2-1, konchok-thabkhe:c-2-2-1, gendun-drub:c-2-2-2-2-1-1-1-1, tenga-tulku:c-1-2-2-1-1-1-1, lobsang-dawa:c-1-2-2-1-1-1-4 — the nested nested-taxonomy vs. simple-ordinal divergence documented on the consolidated page concerns the source text's own organizational scheme rather than the deity's own attributes, so it was judged out of scope for a deity profile and dropped rather than force-fitted into a section.
- Root-verse verbatim duplicates beyond the one quoted: dharmabhadra:c-1-2-2-1-1-1-4, palden-sherab:c-3-1-2-0-2, sungrab-tulku:c-5-2, tenzin-dhonzang:c-4-2-2, tenga-tulku:c-1-2-2-1-1-1-2, tsultrim-namdak:c-2-1-2-1-7.
- Redundant "hundred stacked moons" consensus attestations beyond the representative set used: drakpa-gyaltsen:c-1-10, gendun-gyatso:c-1-2-1, konchok-thabkhe:c-2-2-2, lobsang-dawa:c-1-2-2-1-1-1-5, palden-sherab:c-3-1-2-1-1, pema-namgyal:c-2-4-16, sangye-nyentrul:c-3-0-1, sungrab-tulku:c-5-5, tenzin-dhonzang:c-4-2-3, tsultrim-namdak:c-2-1-2-1-8.
- "Why autumn" facet (entire): sungrab-tulku:c-5-4, tenga-tulku:c-1-2-2-1-1-1-3.
- Redundant "radiance surpasses stars" attestations beyond the representative set: karma-maitri:c-1-1-2-3, konchok-thabkhe:c-2-2-3, sungrab-tulku:c-5-6, tenga-tulku:c-1-2-2-1-1-1-4.
- Gendun Drub's internal textual-variant tension ("hundred stacked" vs. "sixteen teeth / thirty-two marks"): gendun-drub:c-2-2-2-2-1-1-1-4 (⚑, in the raw file). Tsultrim Namdak's related teeth/garland-smile image: tsultrim-namdak:c-2-1-2-1-9. Both omitted for space; a fuller revision of this article should add them under either སྐུ་ཡི་རྣམ་པ or གཞུང་ལུགས་སོ་སོའི་བཤད་པ.
- Tenzin Dhonzang's external "Legdrima" comparative citation on Khadiravaṇī Tārā's beauty: tenzin-dhonzang:c-4-2-8 — omitted because the consolidated page itself notes this describes a different tantric form of Tārā, not this homage's own figure, and including it risked implying an identity the sources do not assert.
- Konchok Thabkhe's unique "homage by way of ornament and light rays" structural characterization: konchok-thabkhe:c-2-2-1 (the same claim also carries the plain "second" ordinal, which was likewise not used — see above).

## Unresolvable attestations

None. Every attestation cited on `2-RAILS/Claims/tara-02.md` that this draft attempted to draw on was located in its named raw tree-guided file under `2-RAILS/Claims/raw/tree-guided/`.

## Warnings

- **`rails_status` is `draft`, not `complete`.** Per the vault rule that transformations generate from `status: complete` rails, this article was drafted from a consolidated claims page still marked `draft`. A human contributor is accepting that risk explicitly by running this skill against it; the article's own `status` is set to `draft` below and should not be treated as publishable until `2-RAILS/Claims/tara-02.md` itself is promoted to `complete` (or the discrepancy is otherwise resolved).
- **No public URLs exist for any of the fourteen cited commentaries.** Every `<ref>` in `article.md` uses the skill's hand-formatted `<AUTHOR>། <TITLE>།` form with no `[<URL> ...]` wrapper, per Rule 7 (no `sources.yaml` entries exist yet for this corpus). This means validator rule V2 ("every `<ref>` resolves to a source declared in `sources.yaml`") cannot be satisfied by this draft and is not applicable until the corpus gets a `sources.yaml`.
- **`yama-sonam`'s author is unrecorded.** Its raw claims file's own frontmatter records `author: "རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་"` and `author_in_english: "unknown"`. The bibliography and in-text refs cite it as "རྗེ་བཙུན་ཡ་མ་བསོད་ནམས" (Jetsün Yama Sonam) rather than inventing a name — this is itself attested by the frontmatter, not fabricated, but a reviewer should confirm this is the vault's preferred convention for anonymous commentaries.
- **Several refs lack year and page** (no publication year or page number is recorded in any of the fourteen raw files' frontmatter for this corpus), so none of the fourteen `<ref>`s in this article carry a year or page, per the spec's own allowance ("may be omitted when genuinely unknown — but the review report lists every ref missing them").
- **Article length is short of the spec's 1,500-Tibetan-syllable guidance.** The prose body (lead through the last content section, excluding the reference list, bibliography, and the citation text embedded in `<ref>` tags) runs to roughly 460–470 Tibetan syllables (tsheg-separated units); counting everything including ref/bibliography text, the whole file is roughly 1,450 tsheg. This is a non-blocking warning per the spec (§7), not a validator failure.
- **Two genuine divergences were deliberately left out of the drafted prose** to keep the article at a manageable length for this test run (see "Resolved claims not used" above): Gendün Drub's internal "hundred stacked moons" vs. "sixteen teeth / thirty-two marks" textual-variant tension, and Tenzin Dhonzang's external Legdrima citation on Khadiravaṇī Tārā. Neither is contradicted by anything drafted; both are candidates for a follow-up expansion pass.
- **`konchok-thabkhe` was fully resolved (3 claims) but not cited anywhere in the final article** — its content (structural placement + basic "hundred moons/thousand stars" gloss) duplicated points already carried by the representative citations chosen for those facets (Rule 5's "2–4 representative commentaries" guidance), so it was dropped rather than force-included.

## Verification

The v1 audit (below) verified all 8 quotations that existed in the v1 draft, character-for-character
against their cited `1-SOURCES/` files. Per Mode B step 6, the revised `article.md` was spot-checked
by text diff against this same table rather than re-verified from scratch: the two quotations
retained in the revision (#1 the root verse, exempt from the budget, and #3, #4 the two in-budget
commentary quotations) are unchanged, unaltered substrings of the same PASS rows below. Quotations
#2, #5, #6 were removed from quotation-mark status and converted to paraphrase (see "Quotation
budget" above) and so no longer require character-level verification; #7 and #8 were short
unquoted-in-prose phrases in v1 that remain unquoted content in v2 (folded into the naming
paragraphs), also not subject to character verification since they never carried quotation marks.

| # | Quotation | Claim | Source file (block) | v1 Result | Status in v2 |
|---|---|---|---|---|---|
| 1 | "ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། ། གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། ། སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས།། རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ།" | yama-sonam:c-3-2-3 | སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-26 | PASS | retained, root verse, exempt (lead) |
| 2 | "གཉིས་པ་བློ་གཏེར་དབྱངས་ཅན་མ་ནི།" | palden-sherab:c-3-1-2-0-1 | (long-titled Palden Sherab commentary).md#^0-25 | PASS | converted to paraphrase |
| 3 | "འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།" | gendun-drub:c-2-2-2-2-1-1-1-5 | སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-22 | PASS | retained, quotation #1 of 2 |
| 4 | "ཞལ་གསུམ་དཀར་སྔོ་གསེར་མདོག་ཅན། ། བཅུ་གཉིས་ཕྱག་མངའ་མཉམ་གཞག་དང་། ། ཁ་ཊཱཾ་འཁོར་ལོ་རིན་ཆེན་ཉིད། ། རྡོ་རྗེ་མེ་ཏོག་ཕྲེང་འཛིན་གཡས། ། རིལ་བ་ཨཏྤལ་དྲིལ་བུ་དང་། ། བུམ་པ་དང་ནི་པོ་ཏི་གཡོན།" | yama-sonam:c-3-2-11 | སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-31 | PASS | retained, quotation #2 of 2 |
| 5 | "དེ་ལ་ཡང་སྐར་མ་སྟོང་གུས་པ་རྣམས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་སྟེ་བརྒྱན་པ་ལྟ་བུའི་འོད་དཀར་པོ་རབ་ཏུ་འབར་བའི་སྒྲོལ་མ་ལའོ།" | gendun-gyatso:c-1-2-2 | ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-9 | PASS | converted to paraphrase |
| 6 | "འགྲེལ་མཛད་མཁན་དག" | yama-sonam:c-3-2-5 | སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-28 | PASS | converted to paraphrase |
| 7 | "ཞི་བ་ཆེན་མོ" (unquoted in prose) | tenzin-dhonzang:c-4-2-1 | སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-116 | PASS | unchanged, unquoted content |
| 8 | "འོད་རབ་འབར་མ" (unquoted in prose) | lobsang-dawa:c-1-2-2-1-1-1-6 / yama-sonam:c-3-2-3 | སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-8 / སྒྲོལ་མའི་འགྲེལ་བ་...སྤྲིན་ཕུང་།.md#^0-26 | PASS | unchanged, unquoted content |

**8/8 v1 quotations PASS; v2 carries forward 2 in-budget commentary quotations (rows 3, 4) plus the
exempt root-verse quotation (row 1), all unaltered substrings of PASS rows. No new quotation was
introduced.**
