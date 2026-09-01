---
topic: asceticism
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/asceticism/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — asceticism

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | dka' thub is one of the six pāramitās taught in the third homage verse of the Twenty-one Praises | same | YES | ཡིན། → སྟེ clause-join; no meaning change |
| 2 | Of the six items listed (giving, effort, dka' thub, peace, patience, meditation), dka' thub is ascertained to mean śīla | same, same six items same order | YES | minor particle change only |
| 3 | Some commentaries also use dka' thub as a name for a vehicle-classification, an explanation of secret mantra's hidden meaning, and a name for a body-form | same three categories | YES | rephrased list syntax only |
| 4 | Twelve commentaries explain dka' thub (in the verse) as śīla-pāramitā | same, "twelve" unchanged | YES | none |
| 5 | Some commentaries explain it as śīla's power to pacify afflictions | same | YES | none |
| 6 | Gendun Drub also counts dka' thub among the ten signs of pure pāramitās | identical wording | YES | unchanged verbatim |
| 7 | In this text dka' thub also appears with three other particular meanings distinct from pāramitā śīla | same, "three" unchanged | YES | none |
| 8 | Khenchen Palden Sherab, per the nine-vehicle doctrine, posits dka' thub as a name for a subdivision of the nine vehicles, different from pāramitā śīla | same | YES | none |
| 9 | In secret-mantra hidden-meaning exegesis, Khenchen Palden Sherab and Jonang Taranatha explain non-emission in lotus-vajra union as equivalent to śīla-dka'-thub | same, same two authors, same claim | YES | none |
| 10 | Taranatha further glosses the mantra syllable tuttāre as dka' thub, quoting "ཏུཏྟཱ་རེ་ནི་གདུང་བ་སྟེ་དཀའ་ཐུབ་ཡིན་ལ", and explains this dka'-thub-in-avadhūti as curing the "bindu-transference" disease | same, quotation identical | YES | བཤད→བཀྲལ synonym swap (flagged below) |
| 11 | On the body-form reading, Taranatha and Palden Sherab explain Amitābha dwelling occasionally in an ascetic form amid Tārā's hair-locks | same | YES | "མཚུངས་པར" (similarly) dropped — see note |
| 12 | Konchok Thabkhe explains the third verse differently: most commentaries read dka' thub and zhi ba separately as śīla and prajñā, but he quotes "དཀའ་ཐུབ་ཞི་བ་སྟེ་ཚུལ་ཁྲིམས་དང" combining the two into one śīla, yielding ~5 pāramitās directly and identifying Tārā herself as prajñāpāramitā, unlike commentaries that map six terms to six pāramitās | same, quotation identical | YES | འགྲེལ་བར→བཀྲལ་བར, བྱེད་དེ→མཛད་པས register/verb swap (flagged below) |
| 13 | Khenpo Tsultrim Namdak also states dka' thub = śīla, matching other texts, but also counts the same verse among the 37 factors of enlightenment — differing from commentaries that read only six pāramitās | same, "37" unchanged | YES | none |
| 14 | Summary: dka' thub is another name for pāramitā-śīla; Konchok Thabkhe differs by combining it with zhi ba | same | YES | འགྲེལ་བར→བཀྲལ་བར synonym swap |
| 15 | Summary: the term is also explained as a subdivision of the nine vehicles and, in secret-mantra hidden meaning, as both śīla-dka'-thub and the mantra-syllable tuttāre's definitive meaning; Amitābha's form in Tārā's hair-locks is also occasionally called dka'-thub-can | same | YES | none |

## Ref attachment walk

| Ref | Statement it supports (before) | Same statement (after)? |
|---|---|---|
| karma-maitri | six-pāramitā list / dka' thub = śīla (lead); also śīla pacifies afflictions (མཚན་ཉིད) | YES / YES |
| drakpa-gyaltsen | six-pāramitā list / dka' thub = śīla (lead) | YES |
| taranatha | six-pāramitā list (lead); secret-mantra hidden-meaning equivalence (དབྱེ་བ); tuttāre gloss + quotation (དབྱེ་བ); Amitābha body-form (དབྱེ་བ); summary refs (བསྡུས་དོན) | YES throughout |
| gendun-drub | twelve-commentary śīla-pāramitā reading; ten-signs count (མཚན་ཉིད) | YES |
| gendun-gyatso | twelve-commentary śīla-pāramitā reading (མཚན་ཉིད) | YES |
| lobsang-dawa | twelve-commentary śīla-pāramitā reading (མཚན་ཉིད) | YES |
| tenzin-dhonzang | śīla pacifies afflictions (མཚན་ཉིད) | YES |
| palden-sherab | nine-vehicle subdivision (དབྱེ་བ); secret-mantra hidden-meaning equivalence (དབྱེ་བ); Amitābha body-form (དབྱེ་བ); summary refs (བསྡུས་དོན) | YES throughout |
| konchok-thabkhe | five-pāramitā combined reading + quotation (གཞུང་ལུགས་སོ་སོ); summary ref | YES |
| tsultrim-namdak | 37-bodhipakṣa reading (གཞུང་ལུགས་སོ་སོ) | YES |

All 10 distinct ref names (22 total ref tokens/instances including repeats, matching the script's "22 refs frozen" count) remain attached to the identical statement they supported before recomposition. No ref migrated to a different clause or claim.

## Flagged substitutions

Lexical-only swaps, same referent/meaning, do not block PASS:

| Location | Before | After | Note |
|---|---|---|---|
| Taranatha tuttāre-gloss sentence (དབྱེ་བ, 2nd para) | བཤད་ཅིང་ ("explained") | བཀྲལ་ཞིང་ ("explicated/elucidated") | synonym for "explain," same claim |
| Konchok Thabkhe paragraph (twice) | འགྲེལ་ / འགྲེལ་བར ("explain(ed)") | བཀྲལ་ / བཀྲལ་བར | same synonym swap, repeated pattern |
| Konchok Thabkhe paragraph | ངོས་འཛིན་བྱེད་དེ ("identifies," plain verb) | ངོས་འཛིན་མཛད་པས ("identifies," honorific verb མཛད་) | register elevation on the *verb*, not a title inserted before a personal name (Rule 8's named drift pattern concerns honorifics before proper names — this is an honorific auxiliary verb applied to the act of philosophical identification within a Buddhist-commentarial register). Referent, claim, and attribution to Konchok Thabkhe are unchanged. Flagged for domain-expert review as a register choice, not treated as drift. |
| Summary paragraph | འགྲེལ་བར ("explaining") | བཀྲལ་བར | same synonym swap |
| Amitābha body-form sentence (དབྱེ་བ, 3rd para) | ...སྐུར་བཞུགས་པར་**མཚུངས་པར་**བཤད་དོ།། ("...explained **similarly** that [Amitābha] dwells...") | ...སྐུར་བཞུགས་པར་བཤད་དོ།། (qualifier "similarly/concordantly" dropped) | The dropped qualifier described *how the two commentators explain* (in agreement with each other), not the content of the claim itself. Both refs (taranatha, palden-sherab) remain jointly attached to the same sentence, so the concordance is still implicit from the citation. No fact about Amitābha, Tārā's hair-locks, or the ascetic form was added, dropped, or altered. Flagged for completeness; not treated as factual drift since it does not change what is claimed, only how the joint-attribution was worded. |

## Reverted drift (if any)

None. No surgical reversion was necessary — every substitution found is a same-referent lexical/register swap or a non-substantive connective-word drop, not a changed, added, dropped, or re-attributed fact.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator. Every one of the 10 distinct `<ref>` names remains attached to exactly the statement it supported before recomposition (confirmed by the walk above). Both verbatim quotations — "ཏུཏྟཱ་རེ་ནི་གདུང་བ་སྟེ་དཀའ་ཐུབ་ཡིན་ལ" and "དཀའ་ཐུབ་ཞི་བ་སྟེ་ཚུལ་ཁྲིམས་དང" — are character-for-character identical before and after (also enforced mechanically by the script's C3 check). No unattested honorific was inserted before any personal name (checked ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ, དཀོན་མཆོག་ཐབས་མཁས, མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག, རྒྱལ་བ་དགེ་འདུན་གྲུབ — all unchanged). No numeral changed (six pāramitās, twelve commentaries, three particular meanings, ten signs, thirty-seven bodhipakṣa factors — all preserved). No technical/philosophical term was swapped for a different category. Headings, the "related pages" tail, the references section, the bibliography list, and the category tag are byte-identical to the source. The two flagged substitutions above are lexical/register-only and do not affect content.
