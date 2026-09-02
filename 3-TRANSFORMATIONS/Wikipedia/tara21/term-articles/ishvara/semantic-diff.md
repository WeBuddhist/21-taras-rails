---
topic: ishvara
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/ishvara/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — ishvara

Only the lead paragraph and the sections ངེས་ཚིག, རོ་ལངས་ཀྱི་གཙོ་བོ་དང་ཡབ་ཏུ་གྱུར་པའི་ཚུལ།, སྦས་དོན།, and the intro sentence of གཞུང་ལུགས་སོ་སོའི་བཤད་པ། were recomposed (git diff: one frontmatter hunk + one body hunk spanning original lines 12–41). Everything from == དཔེ་བརྗོད། == onward (དཔེ་བརྗོད་, བསྡུས་དོན་, འབྲེལ་ཡོད་ཤོག་ངོས་, ལུང་ཁུངས་, དཔྱད་གཞིའི་ཡིག་ཆ་, category) is byte-identical, confirmed against body-before.txt/body-after.txt and `git diff`.

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Ishvara = 5th of the great worldly gods (with Indra, Agni, Brahma, Vayu) who offer worship to Tārā in verse 6; also known as Vishvesvara | Same | YES | reworded, "who offer worship" made explicit (was implicit) |
| 2 | Some commentaries also denote it by the name Great Ishvara, treating the two names as one | Same | YES | synonym swap only |
| 3 (ངེས་ཚིག intro) | commentaries show many different "writing forms" (འབྲི་སྟངས) of the name | commentaries show several different "name-variants" (མཚན་གྱི་རྣམ་གྲངས) | YES (same referent: naming variation across commentaries) | category-word swap, flagged below |
| 4 | Vishvesvara most common, Great Ishvara also very well attested; Sungrab Tulku keeps the two names' referents separate | Same | YES | idiom swap ཆེས་གྲགས→ཤིན་ཏུ་གྲགས |
| 5 | Yama Sonam alone uses "Wrathful Great Ishvara"; no other commentary uses this name | Same | YES | — |
| 6 | Sangye Nyenpa's text has a different spelling but no difference in referent | Same | YES | འབྲི་སྟངས→འབྲི་ཚུལ, synonym |
| 7 | Taranatha's verbatim quote defining the term as a general name for many gods | Same, verbatim quote unchanged | YES | quote checked character-for-character identical |
| 8 | Tsultrim Namdak and Tenzin Dhonzang explain "in a manner matching the order" (གོ་རིམ་མཚུངས་པའི་ཚུལ) | explain "in agreement with that" (དེ་དང་མཐུན་པར) | YES (both assert the two commentators agree with Taranatha's account) | flagged: "matching order" vs "agreement" — narrower vs broader agreement claim, same conclusion (position not identified with a single deity) |
| 9 | The three commentaries treat the 5th deity as a category (Great Ishvara/wrathful deities etc.), not a single deity; this may explain why other commentaries do not specially identify the name | Same | YES | — |
| 10 (རོ་ལངས་...) | "རོ་ལངས" in the closing verse line is "definitely held" (ངེས་བཟུང) as an epithet of Great Ishvara; some place him specifically (ལྷག་པར) as chief of the zombies | "identified" (ངོས་བཟུང, the article's standard identification verb) as Great Ishvara; some commentaries explain him as chief of the zombies | YES (same identification, same "some vs others" split) | flagged: certainty-adverb ངེས་ and emphasis ལྷག་པར dropped |
| 11 | Here Great Ishvara, instead of Vishvesvara, reverts from worshipper to chief of the worshipped retinue | Same | YES | — |
| 12 | Drakpa Gyaltsen: at the text's start, gives "merely an understanding" (གོ་བ་ཙམ) that Great Ishvara became lord of the preceding four gods | gives an "explanation" (བཀྲལ) that Great Ishvara became lord of the preceding four gods | YES (same lord-of-four-gods claim) | flagged: "merely" (ཙམ, hedge on how much is said) dropped |
| 13 | Pema Namgyal: explains Great Ishvara as father of the various great gods (Indra etc.) | Same | YES | — |
| 14 | Both commentaries agree in according Great Ishvara "a distinctive status" (ཁྱད་པར་ཅན) with respect to the other four gods | Both agree he holds "a status distinctly superior to" (ཁྱད་པར་དུ་འཕགས་པའི་གོ་འཕང) the other four gods | YES — checked against sentences 12–13 immediately above (lord / father), which already establish a senior/superior relationship; "superior" is a paraphrase of "lord/father," not a new claim | flagged: strongest substitution in the diff, reviewed carefully, judged supported by adjacent sentences, not fabricated |
| 15 | Taranatha: Tara's blessed mantra can summon even great gods like Great Ishvara as servants | Same | YES | — |
| 16 | Sungrab Tulku: in another context, peaceful Tara subdues the pride of worldly great gods like Ishvara; here Ishvara reverts from worshipper to object-of-subduing | Same | YES | — |
| 17 (སྦས་དོན) | Taranatha and Palden Sherab: via completion-stage with signs, Vishvesvara is joined to the space element | Same | YES | — |
| 18 (གཞུང་ལུགས་ intro) | question framed as: "whether or not a specific deity definitely exists" (ངེས་པར་ཡོད་མེད) as Vishvesvara — three views follow | question framed as: "how [commentaries] identify which particular deity" it is — three views follow | YES, downstream content (lines 21, 23, 25, 27 — all unchanged in wording) still states the same three positions, including the "no single deity, just a category" position | flagged: intro-sentence framing shifted from existence-question to identification-question; verified the substantive three positions below are untouched |
| 19–23 (three named positions + summary) | Palden Sherab/Dharmabhadra/Sangye Nyenpa → Yama, south guardian; Tenzin Dhonzang → Ishvara, northeast guardian (with zin-bris quote); Konchok Thabkhe → water-deity + earth-deity compound; 12+ commentaries → no specific direction | Same, word order only | YES | quote (Chakrasamvara zin-bris) verified character-for-character identical |
| 24 (line 27, unchanged) | 12+ commentaries give only the generic sense "a great god," none states the three positions are mutually exclusive | identical text | YES | not touched by the polish at all |

## Ref attachment walk

All 14 distinct `<ref>` names checked against the statement each sits on, before vs after:

| ref name | statement it supports (before) | same statement (after)? |
|---|---|---|
| yama-sonam | (1) def. of Vishvesvara group; (2) sole use of "Wrathful Great Ishvara" | YES / YES |
| dharmabhadra | (1) def.; (2) identifies Ishvara with south-guardian Yama, also nāga-classes | YES / YES |
| sungrab-tulku | (1) def.; (2) keeps the two names' referents separate; (3) reused on རོ་ལངས identification; (4) peaceful-Tārā-subdues-pride passage | YES (×4) |
| gendun-gyatso | def. only, attached to "two names treated as one" sentence | YES |
| karma-maitri | def. only, same sentence as gendun-gyatso | YES |
| sangye-nyentrul | def.; different spelling, same referent | YES |
| taranatha | (1) def./quote on general-name meaning; (2) reused for Tsultrim Namdak/Tenzin Dhonzang agreement; (3) reused for mantra-summons-gods; (4) reused for completion-stage/space element; (5), (6) unchanged tail (mountain example, summary) | YES (×6) |
| tsultrim-namdak | def.; reused on རོ་ལངས identification group; reused unchanged in merchant story | YES (×3) |
| tenzin-dhonzang | def.; reused on Chakrasamvara zin-bris quote (northeast) | YES (×2) |
| drakpa-gyaltsen | def.; reused on "lord of the four gods" statement | YES (×2) |
| gendun-drub | def. only, same sentence as drakpa-gyaltsen | YES |
| pema-namgyal | def.; "father of the great gods" statement | YES |
| palden-sherab | def.; reused for south-guardian Yama identification; reused unchanged in summary | YES (×3) |
| konchok-thabkhe | def.; water/earth-deity compound explanation | YES |

No ref migrated to a different clause. No ref content altered (token-conservation check C1 already confirmed this mechanically; this is the manual re-confirmation).

## Flagged substitutions

Lexical/idiom-level swaps, same referent — recorded for the domain expert's review, do not block PASS:

| # | Before | After | Why flagged |
|---|---|---|---|
| 1 | མིང་གི་འབྲི་སྟངས་ ("writing-forms of the name") | མཚན་གྱི་རྣམ་གྲངས་ ("name-variants") | category word swapped; both describe the same phenomenon (naming variation across commentaries) discussed in the paragraph, but "writing-form" (orthographic) vs "variant name" (lexical) are not strict synonyms |
| 2 | ཆེས་གྲགས་ | ཤིན་ཏུ་གྲགས་ | idiom swap, "very well known" both ways |
| 3 | གོ་རིམ་མཚུངས་པའི་ཚུལ་གྱིས་བཤད ("explain matching the sequence") | དེ་དང་མཐུན་པར་བཤད ("explain in agreement with that") | narrower vs broader agreement claim; same conclusion downstream |
| 4 | ངེས་བཟུང ("definitely held") | ངོས་བཟུང ("identified") — the article's standard identification verb elsewhere | certainty-adverb ངེས་ dropped |
| 5 | ཁ་ཤས་ཤིག་གིས་ལྷག་པར་...བཀོད ("some place him specifically/further") | འགྲེལ་པ་འགའ་ཞིག་གིས་...བཤད ("some commentaries explain") | emphasis marker ལྷག་པར dropped |
| 6 | གོ་བ་ཙམ་ཞིག་སྤྲོད ("gives merely an understanding") | བཀྲལ ("explains") | hedge ཙམ ("merely") dropped |
| 7 | གོ་གནས་ཁྱད་པར་ཅན་ཞིག ("a distinctive status") | ཁྱད་པར་དུ་འཕགས་པའི་གོ་འཕང་ཅན ("a status distinctly superior to") | strongest substitution reviewed; judged supported by the immediately preceding lord/father statements, not a fabricated claim — see row 14 above |
| 8 | question framed as ངེས་པར་ཡོད་མེད ("whether a specific deity definitely exists") | question framed as ལྷ་བྱེ་བྲག་པ་གང་ཡིན་ངོས་འཛིན་ཚུལ ("how [commentaries] identify which deity it is") | intro-sentence reframing; the three positions detailed immediately below (including the "no single deity" position) are unchanged in wording, so the reframing does not suppress or misstate any position |

## Reverted drift (if any)

None. No factual drift requiring reversion was found — every item above is a same-referent lexical/register substitution, and item 7 (the closest call) was traced to content already stated two sentences earlier in the same paragraph.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened beyond what adjacent sentences already establish, or re-attributed to a different commentator. Every `<ref>` remains attached to the same statement it supported before. Both verbatim quotations (Taranatha's naming verse, Tenzin Dhonzang's Chakrasamvara zin-bris citation) are character-for-character identical. The frozen tail (དཔེ་བརྗོད་ onward: examples, summary, related-links, references, further-reading, category) is byte-identical, confirmed via `git diff`. Eight lexical-level substitutions are recorded above for the domain expert's discretion; none blocks the PASS verdict.
