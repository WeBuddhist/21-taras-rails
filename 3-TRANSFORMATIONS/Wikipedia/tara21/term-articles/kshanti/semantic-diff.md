---
topic: kshanti
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/kshanti/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — kshanti

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Opening: kshanti is one of the six paramitas taught as Tara's conduct, per verse 3 of the Praise to the Twenty-One Taras ("gold-blue lotus-born...") | Same, verse quote verbatim unchanged; one clause break added before "rje btsun ma'i spyod yul du" | Yes | Punctuation only |
| 2 | Etymology: kshanti = the paramita of patience itself | Same, copula ཡིན།། → དོ།། | Yes | Grammar-particle swap |
| 3 | Definition: Khenchen Palden Sherab cites the Brahmaviśeṣacintī-paripṛcchā sutra for the six paramitas' ultimate definitions; verbatim quote "mi 'dzin pa ni sbyin pa'o..." unchanged | Same commentator, same sutra, same verbatim quote; "mdo drangs nas...bshad" → "mdo lung du drangs nas...bstan pa" (both mean "cited from/as sutra citation...taught/explained") | Yes | Synonym substitution ("drangs"→"lung du drangs", "bshad"→"bstan pa") |
| 4a | Threefold division of kshanti: patience of enduring suffering, patience of not minding harm, patience of certain attainment re dharma | Same three types, same order | Yes | Punctuation/connective restructuring only |
| 4b | Ten-paramita counting system (6 + thabs/stobs/smon lam/ye shes); kshanti placed 3rd, linked to the ten bhumi qualities; Gendun Drub: heart-lotus mudra as sign of the ten pure paramitas | Same facts, same attribution (Gendun Drub), same mudra detail | Yes | "sbrel te"→"sbyar nas" (synonym "link/connect"); "rtags su bshad"→"mtshon rtags su gsungs" (synonym "sign") |
| 5 | Kshanti explained as the antidote to hatred/anger, defined by being unstained by the fault of anger | Same fact, same attribution | Yes | Grammar-particle swap only |
| 6 | Hidden-meaning (completion-stage) reading: kshanti = the patience of equalizing all happiness and suffering | Same fact, same attribution (Palden Sherab, Taranatha) | Yes | "la go" → "la go bar bya'o" (both = "is to be understood as"; common commentarial gloss form, not a new obligation imposed on the reader — see note below) |
| 7 | Gendun Gyatso's alternate reading of the six-paramita phrase: identifies renunciation-through-shila and wisdom-of-suchness as the "extra" two members in place of dana/virya/shila as usually explained by other commentators; no other commentary offers this second reading | Same fact set, same commentator, same three substituted paramitas (dana, virya, shila) named identically | Yes | Word-order/connective restyling; bold author name `'''རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ་'''` byte-identical |
| 8 | "Patience toward the unborn nature of phenomena" (anutpattika-dharma-kṣānti): term also appears in the text's narrative (Tara as a princess practicing meditation amid the five sense-pleasures, thereby attaining this patience and the samadhi that liberates all beings); distinct, uncommon usage from the paramita sense | Same narrative, same attainment, same three refs, same conclusion that this is a distinct usage | Yes | "sgra" → "tha snyad" (synonym "word/term"); "thob nas...bshad" → "thob ste...gsungs so" (synonym reporting verbs); "thun mong min pa" → "thun mong ma yin pa" (same meaning, uncontracted spelling) |
| 9 | Summary: kshanti as a paramita of Tara's conduct and as antidote to anger; threefold division repeated; also glossed as "ultimate non-abiding" | Same three summary facts, same three refs (sungrab-tulku, tenzin-dhonzang, palden-sherab) in the same order | Yes | "gnod pa la mi snyam pa" → "gnod pa la ji mi snyam pa" restores the idiomatic "ji" already used in the § དབྱེ་བ paragraph's phrasing of the same division — brings the summary in line with the fuller idiom used earlier, not a new claim; "bshad yod" → "gsungs so" synonym |

## Ref attachment walk

| Ref | Statement it supports (before) | Statement it supports (after) | Same? |
|---|---|---|---|
| sungrab-tulku (×3) | 1: kshanti as 6th-paramita conduct of Tara; 5: antidote-to-anger definition; 8: unborn-dharma-patience narrative | identical three attachments | YES |
| tenzin-dhonzang (×5) | 2 (none — not used there); 4a: threefold division; 4b: ten-paramita/10-bhumi link; 5: antidote-to-anger; 8: narrative; 9: threefold division in summary | identical attachments, same count and positions | YES |
| drakpa-gyaltsen | 2: etymology = paramita of patience | same | YES |
| palden-sherab (×3) | 3: sutra-citation definition; 4b: ten-paramita/10-bhumi link; 6: hidden-meaning gloss; 9: "ultimate non-abiding" gloss | identical attachments | YES |
| tenga-tulku | 5: antidote-to-anger | same | YES |
| taranatha | 6: hidden-meaning gloss | same | YES |
| gendun-drub | 4b: heart-lotus mudra as sign of ten paramitas | same | YES |
| gendun-gyatso | 7: alternate six-paramita reading | same | YES |
| tsultrim-namdak | 8: narrative | same | YES |

All 20 ref tokens (per gemini-report.md) survived with identical attachment to the same statements; none migrated to a different clause.

## Flagged substitutions

Lexical/grammatical swaps, same referent and meaning, listed for domain-expert review (do not block PASS):

| # | Before | After | Note |
|---|---|---|---|
| 1 | ཡིན།། | དོ།། | copula ending swap (§ ངེས་ཚིག) |
| 2 | མདོ་དྲངས་ནས...བཤད་དེ | མདོ་ལུང་དུ་དྲངས་ནས...བསྟན་པ་སྟེ | "cited from sutra...explained" → "cited as sutra-passage...taught"; synonym pair, no new source or fact (§ མཚན་ཉིད) |
| 3 | སྦྲེལ་ཏེ་བཤད | སྦྱར་ནས་བཤད་དོ | "linked/connected...explained" synonym (§ དབྱེ་བ) |
| 4 | རྟགས་སུ་བཤད | མཚོན་རྟགས་སུ་གསུངས་སོ | "sign" → "symbolic sign/indicator"; same referent (§ དབྱེ་བ) |
| 5 | ལ་གོ།། | ལ་གོ་བར་བྱའོ།། | "means/refers to" → "is to be understood as"; standard commentarial gloss idiom, reviewed against Rule 8(d) — does not convert a descriptive claim into a prescriptive obligation on the reader/practitioner, only a conventional interpretive-gloss formula (§ སྦས་དོན) |
| 6 | བཀོད་དེ | མཛད་དེ | "posited" → "did/composed" (honorific verb registering the commentator's own authorial act, already implicit; name form unaffected) (§ གཞུང་ལུགས་སོ་སོའི) |
| 7 | སྒྲ | ཐ་སྙད | "word" → "term", synonym (§ མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ) |
| 8 | ཐུན་མོང་མིན་པ | ཐུན་མོང་མ་ཡིན་པ | contracted vs. uncontracted negative, identical meaning |
| 9 | གནོད་པ་ལ་མི་སྙམ་པ | གནོད་པ་ལ་ཇི་མི་སྙམ་པ | restores idiomatic "ཇི" already present in the fuller statement of the same threefold division earlier in the article (§ དབྱེ་བ); brings the summary's wording closer to, not further from, the article's own definition (§ བསྡུས་དོན) |
| 10 | བཤད / བཤད་ཡོད | གསུངས་སོ | reporting-verb synonym, same evidentiary weight, not weakened or strengthened |

## Reverted drift (if any)

None. No factual drift was found requiring reversion.

## Verdict

**PASS.** Sentence-by-sentence comparison of `body-before.txt` and `body-after.txt` found no fact added, dropped, weakened, strengthened, or re-attributed to a different commentator. All personal names (Khenchen Palden Sherab, Gendun Drub, Gendun Gyatso, Taranatha, etc.) appear with the same titles/forms as the source, no unattested honorifics inserted. The heart-lotus-mudra iconographic detail, the sutra citation, and all three verbatim quotations are preserved character-for-character. All 20 refs remain attached to the identical statements they supported before polishing. Tsheg count is unchanged (830 → 830, 0.0% delta), consistent with the script's C1 token-conservation check. Ten flaggable lexical/grammatical substitutions are listed above for domain-expert acceptance but none affect content.
