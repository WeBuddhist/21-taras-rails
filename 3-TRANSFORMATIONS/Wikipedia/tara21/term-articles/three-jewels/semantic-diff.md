---
topic: three-jewels
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/three-jewels/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — three-jewels

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: "three jewels" names the mark shown by Tara's left-hand mudra in verse 9 of the 21-praise homage stanzas. | Same, word order of "ninth prostration verse" rearranged. | YES | word-order only |
| 2 | The mudra symbolizes the three jewels, fingers adorn the heart, wheel of light adorns all directions; many commentaries similarly describe this. | Same content; clause connector "བཤད་དེ...འདྲེན" → "བཤད་ཅིང...འདྲེན" | YES | grammar particle only |
| 3 | Some commentaries name this 9th prostration "the praise symbolizing the three jewels." | Identical. | YES | — |
| 4 (མཚན་ཉིད) | Many commentaries: thumb+ring finger hold the utpala stem, index/middle/little finger raised **toward the sky** (གནམ་དུ). | Gemini's draft had raised **upward** (གྱེན་དུ) — a genericized iconographic descriptor. **Reverted** to source's གནམ་དུ (see below). | YES (after reversion) | iconographic detail — reverted |
| 5 | Sungrab Tulku describes the finger arrangement differently (verbatim quote of his description). | Identical, verbatim quote untouched. | YES | — |
| 6 | Palden Sherab: also a wheel of light blazing on the corolla held by the left-hand utpala, in the generation-stage visualization. | Same fact, subject fronted, genitive→instrumental particle. | YES | word order / particle |
| 7 (དབྱེ་བ) | Outer/inner division: outer = Buddha, Dharma, Sangha; inner secret meaning (dzogrim) = essence/seed/wind, per Taranatha's exact quote. | Identical facts; "སངས་རྒྱས་ཆོས་དགེ་འདུན" → "སངས་རྒྱས་དང་ཆོས་དགེ་འདུན" (added དང་, standard enumeration); verbatim Taranatha quote untouched. | YES | conjunction added |
| 8 | Palden Sherab agrees with that (Taranatha's inner-meaning reading) in the context of qualified dzogrim. | Same, with explicit anaphoric "དེ་དང་" added for clarity. | YES | — |
| 9 (Yama Sonam) | Splits cause (from Buddha+Dharma jewels) and function (indicates sustaining the Sangha); this reading matches no other commentary. | Same facts; "ནས་:" attribution format → "ཀྱིས་" instrumental clause (applies uniformly across this section — a restyling of the citation convention, not a content change). | YES | attribution-format restyle |
| 10 (Sungrab Tulku) | The prostration's meaning: Tara herself is the object of veneration of the three jewels via three-doors reverence. | Same. | YES | — |
| 11 (Tenzin Dhonzang) | Explains this **in contradiction to** (འགལ་བར) the prior view: Tara herself is the essence of the three jewels (body=Sangha, speech=Dharma, mind=Buddha). | Gemini's draft softened this to "differing from" (མི་མཐུན་པར) — a weakened characterization of the stated disagreement. **Reverted** to source's འགལ་བར (see below). | YES (after reversion) | strength of divergence — reverted |
| 12 (Taranatha) | Identifies this very mudra as Tara's own samaya-mudra; a distinctive identification no other commentary states. | Same facts; honorific verb elevation བྱེད→མཛད (register only, no unattested title before the name). | YES | honorific register only |
| 13 (Konchok Thabkhe) | Citing Gedun Drub's Tara praise verse: the utpala's petal symbolizes the buddhas of the three times; the mudra itself embodies all the jewels. | Same; verb/spelling normalization (འདྲེན→དྲངས, ཨུཏྤལ་གྱིས→ཨུཏྤ་ལས spacing/case). | YES | spelling/grammar normalization |
| 14 (Palden Sherab) | Ultimate meaning at the non-characteristic completion stage: three doors/appearance-sound-awareness/vajra triad; recurs in ~18 branch generation-stages, e.g. Ushnisha Vijaya and Sitatapatra hold distinct emblems on the utpala. | Same; idiom swap སླར་ཡང་སླར་ཡང→ཡང་ནས་ཡང་དུ ("again and again"), spelling normalization ཨུཏྤལ→ཨུཏྤ་ལ. | YES | idiom/spelling only |
| 15 (Tsultrim Namdak) | Third/fourth line of the 9th verse cited uniquely tied to the Tsenden Forest Tara legend; in sadhana context, three jewels = common refuge object, Tara = embodiment of all root-three/vajrayana deities as refuge; refuge brings protection by the three jewels. | Same facts; added དང་ conjunction, sentence-joining shad removed (longer compound sentence, no content change). | YES | punctuation/joining only |
| 16 (བསྡུས་དོན) | Summary: most commentaries = Buddha/Dharma/Sangha; some = inner secret triad; disagreement over Tara's relation to the three jewels (object of veneration vs. essence). | Identical facts; same added དང་/ལའང་ particle normalizations as elsewhere. | YES | particle normalization |

## Ref attachment walk

| ref name | Statement supported before | Statement supported after | Same? |
|---|---|---|---|
| yama-sonam (×2) | mudra symbolism claim (¶2); Yama Sonam's cause/function split (¶9) | same | YES |
| sungrab-tulku (×3) | finger-arrangement variant quote (¶5); prostration-as-veneration reading (¶10); summary divergence (¶16) | same | YES |
| tenzin-dhonzang (×2) | naming of 9th prostration (¶3); Tara-as-essence reading (¶11); summary divergence (¶16) | same | YES |
| palden-sherab (×4) | finger description (¶4); generation-stage wheel-of-light (¶6); dzogrim agreement (¶8); ultimate-meaning + branch-generation recurrence (¶14) | same | YES |
| taranatha (×2) | inner-meaning verbatim quote (¶7); mudra-as-samaya-mudra identification (¶12) | same | YES |
| konchok-thabkhe | Gedun Drub citation, utpala/buddhas-of-three-times claim (¶13) | same | YES |
| tsultrim-namdak (×2) | 3rd/4th line + Tsenden Forest legend link, sadhana refuge claim (¶15) | same | YES |

All 21 ref instances remain attached to the exact statement they supported before polishing (confirmed also by the script's C1 token-conservation check).

## Flagged substitutions

Lexical-only, same referent/meaning — recorded for the domain expert, does not block PASS:

| Before | After | Type |
|---|---|---|
| ནས་: [claim] (colon-attribution format) | X་ཀྱིས་/ཡིས་/གིས་ [claim] (instrumental-clause format) | citation-format restyle, applied uniformly across all "commentator explains" sentences |
| བྱེད་དེ (plain verb) | མཛད་དེ (honorific verb) — Taranatha's act of identifying the mudra | honorific register elevation (no title inserted before the name) |
| ཨུཏྤལ་ / ཨུཏྤལ་གྱིས | ཨུཏྤ་ལ་ / ཨུཏྤ་ལས | spacing/case normalization of "utpala," consistent with spacing used elsewhere in the same article |
| སླར་ཡང་སླར་ཡང་ | ཡང་ནས་ཡང་དུ་ | idiom swap, "again and again" |
| མི་གསུང་བའི | མ་གསུངས་པའི | negation tense form, "does/did not say" |
| various | various | scattered droppings/insertions of the connective དང་ in enumerations (Buddha, Dharma, Sangha lists) and clause-joining shad removed in favor of longer compound sentences |

## Reverted drift (Rule 8 surgical reversions)

1. **མཚན་ཉིད section, finger description.** Source: "...གུང་མོ་མཐེའུ་ཆུང་གསུམ་**གནམ་དུ**་བསྒྲེང་བའི་ཚུལ་དུ..." ("raised toward the sky"). Gemini's draft: "...**གྱེན་དུ**་བསྒྲེང་བའི་ཚུལ་དུ..." ("raised upward") — a genericized iconographic descriptor (known drift pattern (b), iconographic detail flattening). Reverted to the source's exact གནམ་དུ. `body-after.txt` left untouched as the raw model record; only `article.md` was edited.
2. **གཞུང་ལུགས་སོ་སོའི་བཤད་པ section, Tenzin Dhonzang's paragraph.** Source: "...**འགལ་བར**་སྒྲོལ་མ་ཉིད་དཀོན་མཆོག་གསུམ་གྱི་ངོ་བོར་བཤད་..." ("explains this **in contradiction to** [the prior view]"). Gemini's draft: "...**མི་མཐུན་པར**་..." ("explains this **differing from**...") — a softened characterization of a stated inter-commentary disagreement (known drift pattern (d)/(h), a qualifier weakening a claim's strength). Reverted to the source's exact འགལ་བར, keeping the surrounding subject-fronted restructuring (a non-factual stylistic change) intact. `body-after.txt` left untouched as the raw model record; only `article.md` was edited.

No other candidate drift was found. All verbatim `"..."` quotations (finger-position variant quote, "དཀོན་མཆོག་གསུམ་མཚོན" gloss, Taranatha's inner-meaning quote) are character-for-character identical between source and polished versions, both before and after the two reversions above. The task brief flagged a possible root-text verse quotation exempt from the usual quote budget in this article's lead — no such quotation (in `"..."` form or otherwise) appears in this article's lead; the lead is prose description of the ninth-prostration mudra, not a verbatim verse citation, so this caveat did not apply to this run.

## Verdict

**PASS-after-reversion.** Two factual-strength drifts were found and surgically reverted in `article.md` (iconographic descriptor genericized; a stated commentator contradiction softened to a mere difference). After reversion, no fact was added, dropped, changed, or re-attributed anywhere else in the article; every ref remains attached to the exact statement it supported before polishing; every verbatim quotation is character-for-character identical. The remaining changes are word-order, grammatical-particle, citation-format, spelling-normalization, and idiom substitutions with no effect on content, listed above under Flagged substitutions for the domain expert's awareness.
