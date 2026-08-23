---
topic: vindhya
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/vindhya/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — vindhya

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 (lead) | Vindhya (bigs byed) is the third mountain named after Meru and Mandara in verse 17's "homage, mover of the three worlds — Meru, Mandhara, and Vindhya" quote; Tārā's feet-stamping makes it shake together with Meru and Mandara. | Same facts, same quote (character-identical). | Yes | Verb "གྱུར་པའི" (became [shaking])→"མཛད་པའི" (honorific "made [to shake]") — subject is Tārā, consistent honorific register, no fact change. Shad inserted before the quote. |
| 2 (མིང་དོན་དང་མཚན་ཉིད) | Many commentaries identify Vindhya as the third mountain named after Meru/Mandara; these three kings of mountains shake the three worlds (below/surface/above) together with beings; the power to subdue bandit-hordes is also included here; Zurmang Khenpo Pema Namgyal further specifies it lies within the outer ocean where gods and great ṛṣis dwell. | Same, same attributions. | Yes | Particle/connective variants only (འདིས→འདི་དག་གིས, ཏེ→ཅིང). |
| 3 | Many commentaries agree with this reading; some also apply the descriptor "black mountain" (ri nag po) to Vindhya; spelling variants exist ('bigs byed vs 'big byed) with no difference in meaning. | Same. | Yes | Reworded, same claims, same refs. |
| 4 (གཞུང་ལུགས་སོ་སོའི་བཤད་པ) | Drakpa Gyaltsen identifies it as the single mountain "Meru-Mandarava" outside the trichiliocosm, struck by HUM-syllable light rays — not literally a third mountain name. Dorje Lobpön Tenga Tulku similarly applies "striker" to one mountain without listing three separately. Tāranātha (verbatim quote on Tibetan-text variants: possibly Kailash) explains variant readings of the name itself. Karma Maitri explains Vindhya as another name for Meru itself. Khenchen Palden Sherab states it is either Vindhya or any snow-mountain. | Same four positions, same four named commentators, quote character-identical. | Yes | Agent particles ནས→གྱིས (same role); verb ངོས་འཛིན་ཏེ→ངོས་འཛིན་མཛད་དེ (honorific, subject is the named teacher — not a title inserted before the name). |
| 5 (སྒྲུབ་ཐབས་ཀྱི་དམིགས་པ) | Khenchen Palden Sherab places Vindhya among the sādhana's visualization objects in the 17th-verse generation-stage instructions: visualizing Tārā as Amitāyus-suppressor, feet-stamping, HUM-light rays shaking the three mountains, pressed down by wrathful force. Sangye Nyentrul Rinpoche and Khenpo Tsultrim Namdak show a shared generation-stage teaching with the same three mountains via HUM-light; Tsultrim Namdak additionally includes the Himalaya (gangs can). | Same facts, same three named commentators, same attributions. | Yes | Reworded with added connectives; parenthetical "(ཧི་མ་ལ་ཡ)" → appositive "ཏེ་ཧི་མ་ལ་ཡའང" — same gloss, no content change. |
| 6 (བསྡུས་དོན) | Many commentaries explain Vindhya as the third mountain of verse 17, shaken by Tārā's feet-stamping with Meru/Mandara; commentaries disagree on whether "Vindhya" is a proper name or a descriptive phrase, and whether the mountain itself is Vindhya or the Himalaya; Khenchen Palden Sherab also places it in sādhana visualization. | Same. | Yes | Reworded, same refs and attributions. |

## Ref attachment walk

| Ref | Statement supported before | Same after? |
|---|---|---|
| yama-sonam | lead quote/placement sentence | YES |
| dharmabhadra | lead sentence; three-mountain-shaking sentence (×3 total incl. repeats); summary sentence | YES |
| palden-sherab | lead sentence; "gangs can" identification; sādhana visualization sentence (×2); summary sentence | YES |
| gendun-drub | three-mountain-shaking sentence | YES |
| konchok-thabkhe | bandit-subduing power sentence | YES |
| pema-namgyal | ocean-dwelling detail sentence | YES |
| lobsang-dawa | "many commentaries agree" sentence | YES |
| sungrab-tulku | "many commentaries agree" sentence | YES |
| tenzin-dhonzang | "many commentaries agree" sentence; "black mountain" sentence; summary sentence | YES |
| karma-maitri | "black mountain" sentence; spelling-variant sentence; "another name for Meru" sentence | YES |
| drakpa-gyaltsen | "Meru-Mandarava, single mountain" sentence; summary disagreement sentence | YES |
| tenga-tulku | "one mountain, no three listed" sentence | YES |
| taranatha | variant-reading quote sentence; summary disagreement sentence | YES |
| sangye-nyentrul | shared generation-stage teaching sentence | YES |
| tsultrim-namdak | shared generation-stage teaching + Himalaya-addition sentence | YES |

Every ref token (27 total, C1-verified) remained attached to the same statement it supported before polishing; no ref migrated to a different clause.

## Flagged substitutions

Lexical/register-only swaps, same referent and meaning — listed for domain-expert acceptance, does not block PASS:

| Before | After | Note |
|---|---|---|
| གྱུར་པའི (plain "became") | མཛད་པའི (honorific "made") | Subject is Tārā — honorific verb, consistent with the article's register; no fact change. |
| ངོས་འཛིན་ཏེ (plain, ×2, subject = named teacher) | ངོས་འཛིན་མཛད་དེ (honorific) | Same as above pattern — verb honorification of a named person's own action, not a title inserted before the name. |
| ནས (agent particle, ×2) | གྱིས | Grammatical particle variant, same syntactic role. |
| Various connective/final-particle reflows (ཏེ→ཅིང, ལ→ལ།, ཡང→འང) | — | Style-only, no meaning change. |
| "(ཧི་མ་ལ་ཡ)" parenthetical gloss | "ཏེ་ཧི་མ་ལ་ཡའང" appositive gloss | Same gloss content, different punctuation form. |

None of these touch a personal-name title (སློབ་དཔོན་/གྲུབ་ཆེན་/རྗེ་བཙུན་/མཁན་ཆེན་ etc.) — the known drift pattern from the 2026-08-21 pilot was specifically checked for and not found. Every personal name (རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་, རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་, ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ་, ཀརྨ་མཻ་ཏྲི་, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་, སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ་, མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་, ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་) carries exactly the same title/epithet words in both versions.

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** No fact, name, number, doctrinal position, or position-attribution was added, dropped, weakened, strengthened, or re-attributed. The verbatim Tāranātha quote is character-for-character identical to the source. Every `<ref>` remains attached to the exact statement it supported before polishing. Only lexical/grammatical register substitutions were found (particle variants, verb honorification, punctuation reflow), listed above under Flagged substitutions for the domain expert's discretion — none of them alter meaning. The tail-heading boundary before `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` is clean.
