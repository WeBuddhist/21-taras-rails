---
topic: vetala
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/vetala/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — vetala

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 (lead) | Vetala (ro langs) is a class of named beings in many commentaries on the 21-praise; per the root verse it belongs to the fourfold retinue (bhūta, vetala, gandharva, yakṣa) praising Tārā from in front, per the "homage to Śakra, Agni, Brahmā... bhūta, vetala, gandharva... yakṣa" quote; many commentaries also cite another verse where Tārā's mantra-power destroys obstructing spirits together with gdon and yakṣa hordes. | Same facts, same quote, same ref set; internal shad-breaks inside the four-item list removed (fluid enumeration, not a punctuation-rule violation — these were mid-clause shads, not commas). | Yes | Verbatim quote character-identical. No name, ref, or claim change. |
| 2 (དབྱེ་བ) | Zurmang Khenpo Pema Namgyal lists six vetala subtypes (flesh-, blood-, skin-, mole-, vein-, bone-riser) linked to 18 great gdon and charnel-ground bhūta/yakṣa hordes; no other commentary gives this division. | Same six subtypes, same order, same attribution and exclusivity claim; list re-punctuated (repeated དང་ conjunctions condensed to one), verb ending མི་གསུང→མི་གསུངས (honorific consistency). | Yes | No content change. |
| 3 (གཞུང་ལུགས་སོ་སོའི་བཤད་པ, ¶1) | Five named commentators split into two groups: Drakpa Gyaltsen, Gendün Drub, Khenpo Tsultrim Namdak explain vetala as a class headed by Maheśvara; Dharmabhadra, Geshe Lobsang Dawa, Sungrab Tulku explain it as part of the rākṣasa retinue; Karma Maitri and Gendün Gyatso explain it by abode, dwelling in charnel grounds. | Same three groupings, same six names, same attributions. A missing དང་ between the 2nd/3rd name in each of the first two groups (a gap in the source's own bold-span formatting) is filled in — the name count and content are unchanged (still "three" in each group). | Yes | Benign formatting fix, not new content — same persons, same "three" count both before and after. |
| 4 (གཞུང་ལུགས་སོ་སོའི་བཤད་པ, ¶2) | Khenchen Palden Sherab and Sangye Nyentrul Rinpoche explain vetala as the rākṣasa class headed by Khorlha Lekden of the southwest maṇḍala; Könchok Tabkhé alone explains "vetala" not as an inherent class but merely as a name for the corpse a rākṣasa rides, per the phrase "the rākṣasa riding a vetala." | Same. | Yes | No change. |
| 5 (ཕྲིན་ལས་དང་གནོད་པ) | Harm associated with vetala is identified by many commentaries as not general/ordinary, but specifically the black-magic rite of rbod gtong. | Same claim, reworded ("སྤྱིར་བཏང་མིན་པར"→"སྤྱིར་བཏང་བ་ཞིག་མ་ཡིན་པར," same meaning "not general/ordinary"). | Yes | Paraphrase only. |
| 6 (ཕན་ཡོན) | Pema Namgyal: even the bhūta hordes including vetala tremble and praise Tārā before her; those who prostrate to her are freed from these beings' fear in this and all future lives. | Same. | Yes | Connective swap only (ཞིང→བཞིན་དུ). |
| 7 (རྫོགས་རིམ་གྱི་བརྡ་དོན) | Khenchen Palden Sherab gives vetala two distinct completion-stage symbolic referents: thig le (subtle drop) in one outline-section, karma/action in another; this same commentary shows both meanings, and no other commentary gives a matching referent. | Same two referents, same attribution, same exclusivity claim. | Yes | Sentence restructured, verb ending honorific-consistency fix (མི་གསུང→མི་གསུངས). |
| 8 (བསྡུས་དོན) | Many commentaries treat vetala within the root verse, but no unified view on its precise essence is clear. | Same. | Yes | Topic particle ནི added, no meaning change. |

## Ref attachment walk

| Ref | Statement supported before | Same after? |
|---|---|---|
| yama-sonam | lead quote/placement sentence; summary "no unified view" sentence | YES |
| dharmabhadra | lead sentence; rākṣasa-retinue grouping; harm/black-magic sentence | YES |
| tenzin-dhonzang | lead sentence; harm/black-magic sentence | YES |
| gendun-drub | lead sentence; Maheśvara-headed grouping | YES |
| pema-namgyal | 6-subtype division sentence; benefit sentence | YES |
| drakpa-gyaltsen | Maheśvara-headed grouping | YES |
| tsultrim-namdak | Maheśvara-headed grouping | YES |
| lobsang-dawa | rākṣasa-retinue grouping | YES |
| sungrab-tulku | rākṣasa-retinue grouping | YES |
| karma-maitri | abode/charnel-ground grouping | YES |
| gendun-gyatso | abode/charnel-ground grouping | YES |
| palden-sherab | southwest-maṇḍala grouping; harm/black-magic sentence; completion-stage referents | YES |
| sangye-nyentrul | southwest-maṇḍala grouping | YES |
| konchok-thabkhe | "name for a ridden corpse" explanation | YES |

Every ref token (24 total, C1-verified) remained attached to the same statement it supported before polishing; no ref migrated to a different clause.

## Flagged substitutions

Lexical/register-only swaps, same referent and meaning — listed for domain-expert acceptance, does not block PASS:

| Before | After | Note |
|---|---|---|
| ཤ་ལངས་དང་། ཁྲག་ལངས་དང་། ... (shad-separated list) | ཤ་ལངས་དང་ཁྲག་ལངས་... (single-connector list) | Punctuation re-flow of a name-list, not a comma; same six items, same order. |
| མི་གསུང (×2) | མི་གསུངས | Plain → honorific verb ending, consistent with the honorific register used throughout the article; no meaning change. |
| Missing དང་ between two bold-name spans (×2, glued `'''...''''''...'''`) | དང་ inserted | Fills a formatting gap in the source's own bold-span punctuation; same three-name groupings both before and after. |
| སྤྱིར་བཏང་མིན་པར | སྤྱིར་བཏང་བ་ཞིག་མ་ཡིན་པར | Paraphrase, identical meaning ("not general/ordinary"). |
| སྐྲག་ཅིང་འདར་ཞིང་...བཤད་ནས | སྐྲག་ཅིང་འདར་བཞིན་དུ་...བཤད་ཅིང | Connective-particle variant, same meaning. |
| ཐིག་ལེར་བཤད་ལ ... ལས་སུ་བཤད་དེ | ཐིག་ལེ་དང་ ... ལས་སུ་བཤད་པས | Clause restructured, same two referents named in the same order. |
| རོ་ལངས་རྩ་བའི་ | རོ་ལངས་ནི་རྩ་བའི་ | Topic particle ནི added, no meaning change. |

None of these touch a personal-name title (སློབ་དཔོན་/གྲུབ་ཆེན་/རྗེ་བཙུན་/མཁན་ཆེན་ etc.) — the known drift pattern from the 2026-08-21 pilot was specifically checked for and not found. Every personal name (རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་, རྒྱལ་བ་དགེ་འདུན་གྲུབ་, མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་, དངུལ་ཆུ་དྷརྨ་བྷ་དྲ་, དགེ་བཤེས་བློ་བཟང་ཟླ་བ་, འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ་, ཀརྨ་མཻ་ཏྲི་, རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ་, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་, སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ་, དཀོན་མཆོག་ཐབས་མཁས་, ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་) carries exactly the same title/epithet words in both versions.

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** No fact, name, number, doctrinal position, or position-attribution was added, dropped, weakened, strengthened, or re-attributed. The verbatim quote ("…") in the lead is character-for-character identical to the source. Every `<ref>` remains attached to the exact statement it supported before polishing. Only lexical/grammatical register substitutions were found (list punctuation, honorific verb endings, a benign fix of a missing དང་ in the source's own bold-span formatting), listed above under Flagged substitutions for the domain expert's discretion — none of them alter meaning. The tail-heading boundary before `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` is clean.
