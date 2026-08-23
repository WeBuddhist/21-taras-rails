---
topic: indra
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/indra/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — indra

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Indra is, from verse 6 onward, one of the great worldly gods (a "member/subtype" of that class) who, with fire-god/Brahma/wind-god/Vishnu, offer worship to Tara | Indra is, within verse 6, a great worldly god who offers worship with the same four | YES | ནང་གསེས་ (subset-of-class framing) dropped in favor of plain predication; same class membership implied. Flagged substitution. |
| 2 | Again appears with Brahma in verse 19 | Same | YES | ཡང་བསྐྱར/གསལ་བར་བྱེད → སླར་ཡང/གསལ་ཡོད, synonym swap |
| 3 | Two spellings of the name exist across commentaries | Same | YES | མིང→མཚན synonym |
| 4 | Most write brgya byin; Gendün Drub and Yama Sönam write brgya sbyin | Same | YES | — |
| 5 | No commentary treats the two spellings as two different deities; no difference in naming or philosophical position | Same | YES | connective དང→ལམ, logically equivalent under negation |
| 6 | Taranatha: "Indra is king of the gods" (verbatim quote) | Same verbatim quote | YES | quote character-for-character identical |
| 7 | All 16 commentaries commonly identify Indra as Lord of the gods | Same | YES | — |
| 8 | 8 commentaries assign Indra guardianship of the east | Same | YES | — |
| 9 | Tenga Tulku's commentary: ten-guardian scheme, Brahma=zenith, Indra=east | Same | YES | — |
| 10 | Sermey Geshe Tenzin Dhonzang cites a Chakrasamvara note for the eastern-guardian source, in an eight-guardian scheme | Same | YES | word order only |
| 11 | 5 commentaries: gandharvas (among yakshas) are Indra's retinue | Same | YES | — |
| 12 | Khenchen Palden Sherab & Sangye Nyentrul: Indra chief of ten-guardian retinue, summonable by Tara as a servant of activity | Same | YES | — |
| 13 | Taranatha & Palden Sherab: via completion-stage-with-signs, Indra + 4 others correlated to the five elements; Indra = earth | Same | YES | — |
| 14 | Verse-19 "king of the assembly of gods" explained as desire-realm Indra and form-realm great Brahma (2 deities) | Same | YES | — |
| 15 | 12 commentaries explain the same way | Same | YES | — |
| 16 | Khenpo Tsultrim Namdak: Brahma and Indra, with mountain/tree/water gods, among those who rely on [Tara's] feet | Same, but the possessor "Tara's" (སྒྲོལ་མའི) is spelled out explicitly | YES | Before elided the possessor grammatically; after names it. Referent (Tara) is the only one available from context — not a referent change. Flagged substitution. |
| 17 | Benefit of praying to Tara: merit like Indra/Brahma's, an intermediate example between universal monarch and buddhahood | Same | YES | — |
| 18 | Sermey Geshe Tenzin Dhonzang, point 1: in the past-life parallel, identifies Indra as a rebirth of Elder Lhepin | Same | YES | verb aspect ("has been born" → "is born") shift only |
| 19 | Point 2: at the request to turn the wheel of Dharma, Indra offers the white conch, Brahma the thousand-spoked golden wheel, requesting the turning of the wheel of Dharma of the **four blisses** (བདེ་བཞི); no other commentary states this account | Gemini's draft had substituted **བདེན་བཞི** ("four [noble] truths") for བདེ་བཞི ("four blisses") — a different doctrinal term/category | **NO (in Gemini's draft) — reverted, see below** | FACTUAL DRIFT, reverted per Rule 8(a); article.md now reads བདེ་བཞིའི again |
| 20 | Khenpo Tsultrim Namdak: bodily-gesture description of Indra et al. prostrating to Tara's feet, verbatim quote | Same verbatim quote | YES | ལུས་ཀྱི་བརྗོད་པ → ལུས་ཀྱི་རྣམ་འགྱུར་གྱི་སྒོ་ནས, synonym swap; quote identical |
| 21 | Colophon prayer verse: Brahma, Indra and Vishnu together, gods filling all realms with medicinal-cloud flowers — unique to this commentary | Same | YES | — |
| 22 | Summary: Indra = guardian of the east, retinue = gandharvas within yaksha class | Same | YES | — |
| 23 | Summary: appears in verses 6 and 19, both times with Brahma | Same | YES | — |

## Ref attachment walk

All 12 distinct `<ref>` names (`taranatha`, `gendun-drub`, `yama-sonam`, `drakpa-gyaltsen`, `gendun-gyatso`, `palden-sherab`, `dharmabhadra`, `konchok-thabkhe`, `lobsang-dawa`, `tenga-tulku`, `tenzin-dhonzang`, `sangye-nyentrul`, `sungrab-tulku`, `tsultrim-namdak` — 34 ref tags in total, matching the script's token count) were walked clause-by-clause between before/after. Every ref remains attached to the identical statement it supported before the polish — no ref migrated to a different clause or claim. YES for all.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — do not block PASS:

| Before | After | Context |
|---|---|---|
| འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོའི་ནང་གསེས་ཤིག་ཡིན (a member/subtype of the great worldly gods) | འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་ཞིག་ཡིན (a great worldly god) | opening sentence, class-membership framing dropped |
| མིང (name) | མཚན (name) | ངེས་ཚིག section, synonym |
| མང་ཆེ་བས...འབྲི་ཡང (though most write) | མང་ཆེ་བས...བྲིས་མོད (most write, though) | ངེස་ཚིག section |
| ཞབས་ལ་བརྟེན་མཁན (those who rely on [the] feet) | སྒྲོལ་མའི་ཞབས་ལ་བརྟེན་མཁན (those who rely on Tara's feet) | possessor made explicit; only referent available from context is Tara |
| ལུས་ཀྱི་བརྗོད་པས (via bodily description) | ལུས་ཀྱི་རྣམ་འགྱུར་གྱི་སྒོ་ནས (via bodily gesture) | Tsultrim Namdak paragraph |
| ངོས་འཛིན་བྱེད (identified as being born, past-tense-leaning) | ངོས་འཛིན་མཛད (identified as being born, present) | Tenzin Dhonzang paragraph, verb aspect only |
| Various connective particles (དང→ལམ; ནས→ནང; ཏེ→སྟེ etc.) | — | throughout, no meaning change |

## Reverted drift

**Drift found:** in the Sermey Geshe Tenzin Dhonzang paragraph (point 2, the "turning the wheel of Dharma" narrative), Gemini's polished draft changed **བདེ་བཞིའི་ཆོས་ཀྱི་འཁོར་ལོ** ("wheel of Dharma of the four blisses/joys" — a tantric technical term, `bde ba bzhi`) to **བདེན་བཞིའི་ཆོས་ཀྱི་འཁོར་ལོ** ("wheel of Dharma of the four [noble] truths" — the sutra-level doctrinal term for the First Turning at Sarnath). This is drift pattern (f) — a technical/philosophical term swapped for a genuinely different category — even though the two are one Tibetan letter (ན) apart and the substitution reads as a plausible "correction" of what might look like a typo. The source article's exact wording is the frozen factual contract (Rule 1), so this was not treated as a legitimate typo fix.

**Remedy applied:** surgical reversion (Rule 8a). `article.md` was edited to restore the exact source span `བདེ་བཞིའི་ཆོས་ཀྱི་འཁོར་ལོ`, character-for-character as it appeared before the polish. `body-after.txt` was left untouched as the raw model record of what Gemini actually produced. No other change was made to this sentence.

## Verdict

**PASS-after-reversion.** One factual/doctrinal-term drift was found (བདེ་བཞི → བདེན་བཞི, four blisses → four [noble] truths) and surgically reverted in `article.md` to the source's exact wording. Every other sentence carries identical facts before and after; every ref remains attached to the same statement; both verbatim quotations (Taranatha's etymology line and Tsultrim Namdak's verse) are character-for-character identical. Several lexical-only substitutions were found (synonym swaps, connective changes, one elided-possessor spelled out) — none change the referent or the claim, so none block PASS.
