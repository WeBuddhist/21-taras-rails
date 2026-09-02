---
topic: obstacle
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/obstacle/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — obstacle

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Def.: bogegs = a class of beings hostile to sentient beings' virtue/happiness, causing obstruction | Same | YES | verb ending བརྗོད་པ་ཡིན། → བརྗོད་དོ།, stylistic only |
| 2 | Some prayer commentaries identify the term "འབྱུང་པོ" as a type of bogegs | Same | YES | agentive འགྲེལ་པ་...གིས...བྱེད་ → locative འགྲེལ་པ་...ཏུ...མཛད་ (honorific verb applied to commentaries' act, not a title before a personal name); referent and claim unchanged |
| 3 | In verse 14, some commentaries identify bogegs sub-types individually; others don't name "bogegs" directly but use nāga/rākṣasa (ཀླུ་སྲིན་) names instead | Same | YES | ཀླུ་སྲིན་ (compound abbrev.) expanded to ཀླུ་དང་སྲིན་པོ་ — same two categories, not a category swap |
| 4 (ངེས་ཚིག) | Many commentaries identify the "འབྱུང་པོ" section of a prayer verse as ཚོགས་ཀྱི་བདག་པོ་ etc., a class of bogegs/misleaders | Same | YES | restructured, no content change |
| 5 | Drakpa Gyaltsen names the harm-doer in the parallel verse with a deity-name (ལྷ་མིང་) rather than "bogegs" directly | Same | YES | ལྷ་མིང་ → ལྷའི་མིང་, particle only |
| 6 (དབྱེ་བ) | Verse 14's bogegs class divided into three (དམ་སྲི, འགོང་པོ་སྤུན་དགུ, སྡེ་བརྒྱད); named accordingly | Same | YES | stylistic verb/particle changes only |
| 7 | Sungrab Tulku names it དམ་སྲི but does not use "bogegs" | Same | YES | verb swap མི་སྦྱོར → སྦྱར་མེད, same meaning |
| 8 (གཞུང་ལུགས) | Commentaries disagree on naming the verse-14 harm-doer | Same | YES | stylistic only |
| 9 | Drakpa Gyaltsen and Taranatha both avoid "bogegs," name the seven-underworld nāga/asura/rākṣasa/piśāca group instead | Same | YES | no name/attribution change |
| 10 | Zurmang Khenpo Pema Namgyal and Khenpo Tsultrim Namdak agree with that naming | Same | YES | verb/particle only |
| 11 | Sungrab Tulku also names it དམ་སྲི but not "bogegs" — same camp | Same | YES | verb swap only |
| 12 | Khenchen Palden Sherab and Sangye Nyentrul Rinpoche both directly use "bogegs" (དམ་སྲི་བགེགས་རིགས) for the same verse | Same | YES | "གཉིས་ཀས" → "རྣམ་གཉིས་ཀྱིས", same meaning |
| 13 (ཕྲིན་ལས) | Serme Tsang Geshe Tenzin Dhonzang explains a ransom (གླུད) practice: offering a ransom for the lama's/all beings' misdeeds satisfies all harmful demons/bogegs | Same | YES | narrating verb བཤད → གསུངས (honorific verb describing his own act of teaching, not a title before his name); verbatim quotation unchanged character-for-character |
| 14 | He states the deity's main activity is repeatedly pacifying bogegs, without naming individual harm-doers per verse | Same | YES | "དེ་ཉིད" → "ཁོང་" (honorific 3rd-person pronoun, not a title attached to the name); claim content unchanged |
| 15 (བསྡུས་དོན) | Many commentaries use "bogegs" as a generic term alongside demons/māras; verse-14 commentaries split between those naming "bogegs" directly and those naming nāga/rākṣasa/other demon classes instead | Same | YES | restructured, no content change |

## Ref attachment walk

All 23 ref instances (8 unique names: taranatha, palden-sherab, tsultrim-namdak, drakpa-gyaltsen, sangye-nyentrul, sungrab-tulku, pema-namgyal, tenzin-dhonzang) remain attached to the identical clause/statement they supported before the polish — sentence and clause order was not altered, only verb forms and particles within each clause changed, so no ref crossed a clause boundary.

- taranatha: definition sentence, "some commentaries identify" sentence, ངེས་ཚིག paragraph, Drakpa Gyaltsen/Taranatha naming sentence in གཞུང་ལུགས, and the final summary — all same statements. YES
- palden-sherab: "some commentaries identify" sentence, ངེས་ཚིག paragraph, དབྱེ་བ naming sentence, direct-naming sentence in གཞུང་ལུགས, summary — same statements. YES
- tsultrim-namdak: ངེས་ཚིག paragraph and the Zurmang/Tsultrim agreement sentence in གཞུང་ལུགས — same statements. YES
- drakpa-gyaltsen: definition-context sentence, ངེས་ཚིག "avoids bogegs" sentence, the seven-underworld naming sentence, summary — same statements. YES
- sangye-nyentrul: དབྱེ་བ naming sentence, direct-naming sentence in གཞུང་ལུགས — same statements. YES
- sungrab-tulku: དབྱེ་བ Sungrab Tulku sentence, གཞུང་ལུགས Sungrab Tulku sentence — same statements. YES
- pema-namgyal: Zurmang/Tsultrim agreement sentence — same statement. YES
- tenzin-dhonzang: ransom-practice sentence (with verbatim quote) and the following "main activity" sentence — same statements. YES

## Flagged substitutions

| Before | After | Note |
|---|---|---|
| བྱེད་ / བཤད / མི་བཀོད etc. (plain verb register) | མཛད་ / གསུངས་ / མ་བཀོད (honorific verb register) applied throughout to commentators' and the cited teacher's own acts of explaining/naming | Register elevation only — does not attach an honorific title before any personal name (the known drift pattern from the 2026-08-21 pilot). Does not block PASS. |
| དེ་ཉིད་ (demonstrative, "that one/he himself") referring to Tenzin Dhonzang | ཁོང་ (honorific 3rd-person pronoun) referring to the same person | Same referent, honorific register only. Does not block PASS. |
| ཀླུ་སྲིན་ (compound abbreviation) | ཀླུ་དང་སྲིན་པོ་ (expanded) | Same two categories (nāga, rākṣasa), not a category swap. Does not block PASS. |
| ལྷ་མིང་ | ལྷའི་མིང་ | Particle only, same meaning ("a deity's name"). Does not block PASS. |

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator. Every verbatim quotation ("རང་ལ་གནོད་ཅིང་འཚེ་བའི་གདོན་བགེགས་ཀྱི་རིགས་ཡོད་ན། གདོན་བགེགས་ཐམས་ཅད་ཀྱང་དེས་ཚིམས་པ") is character-for-character identical. All 8 named refs remain attached to the same statements they supported before the polish. All personal and commentary names are unchanged, and no unattested honorific title was inserted before any personal name — only honorific verb/pronoun register shifts applied uniformly, which is a flaggable lexical/register substitution, not factual drift. Hard checks C1–C7 passed on the first attempt with 0 warnings.
