---
topic: deva
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/deva/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — deva

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Deva is a sentient-being class, a subtype of the 5-or-6 realms of rebirth; in the threefold-world scheme the upper realm is called the god-realm. | Same, split into two sentences. | YES | "ནང་གསེས་ཤིག་ཏུ་བཤད་པའི" → "ནང་གསེས་སུ་གཏོགས་པའི" (synonym: "explained as a subtype of" → "belonging to a subtype of"); no fact change. |
| 2 (མཚན་ཉིད, s1) | Deva is a subtype of the 5-, 6-, or 7-fold rebirth schemes: hell-being, hungry ghost, animal, human, god = the 5-fold desire-realm continuum. | Same list, same five terms, reworded with parallel "or" (གམ) instead of mixed ཅིང་/འམ. | YES | Same three enumeration options (5/6/7); no term added or dropped. |
| 3 (མཚན་ཉིད, s2) | 3 lower realms + human/god realms = 5; + form-realm + formless-realm = 7 (per Tenga Tulku). | Same enumeration, same ref. | YES | |
| 4 (མཚན་ཉིད, s3) | Sungrab Tulku: naga-realm (below), human-realm (surface), god-realm (above) = threefold world. | Same. | YES | |
| 5 (དབྱེ་བ, s1) | Taranatha: deva class has subtypes; desire-realm devas explained as six types. | Same. | YES | |
| 6 (དབྱེ་བ, s2) | Mountain/tree/lake devas etc. are a special class that help/harm in the world (Taranatha); Khenpo Tsultrim Namdak explains the same. | Same. | YES | "དེ་དང་" added as backreference; same claim, same two sources. |
| 7 (དབྱེ་བ, s3) | Some commentaries, without naming Indra etc. individually, group them under the general term "great worldly devas" as an object of praise (Sungrab Tulku). | Same. | YES | "ངོས་མ་བཟུང་བར" → "མིང་ནས་མ་སྨོས་པར" (synonym, "without naming"); "གོ་བཞག་སྟེ" → "ངོས་བཟུང་སྟེ" (synonym, "categorize/identify"). Same referent and claim. |
| 8 (དབྱེ་བ, s4) | Serme Tsang Geshe Tenzin Dhonzang: posits as the reason [for devotion] that if even the great devas worship and praise her, there is no need to even mention humans (a fortiori). | Same argument, same attribution. | YES | Word order/particles changed; the a fortiori logic and its attribution to this named commentator are unchanged. |
| 9 (གཞུང་ལུགས, s1) | One root verse reads "..." (verbatim quote); many commentaries explain it as a moon-metaphor (Dharmabhadra); Gedun Drub explains it via the moon-mandala/lake-of-gods simile. | Same. | YES | Root-verse quotation checked character-for-character identical (see below). "འདི་ཉིད" added for clarity only. |
| 10 (གཞུང་ལུགས, s2) | Jonang Taranatha shows another explanation: "lake of gods" also glossed as "lake of mind." | Same. | YES | ནས→ཡིས, སྟོན་ཏེ→བསྟན་ཏེ: synonymous particles/verbs, same claim, same attribution to Taranatha. |
| 11 (གཞུང་ལུགས, s3) | Konchok Thabkhe cites another commentarial lineage: the term's origin is tied to the Vedic story of Mount Meru churning the ocean, producing sun and moon. | Same. | YES | "བརྒྱུད་འགྲེལ་" → "འགྲེལ་རྒྱུན་" flagged below as a lexical substitution; underlying story, source (Vedic texts), and attribution unchanged. |
| 12 (གཞུང་ལུགས, s4) | Khenchen Palden Sherab, via the two "profound hidden meaning" outlines, adds two further explanations: (a) completion-stage-with-marks: "lake of gods" = body of the vajra-aggregate city; (b) completion-stage-without-marks: quoted line "..." = the great perfection of the true nature. | Same, same two explanations, same attribution. | YES | Both direct quotations checked character-for-character identical (see below). |
| 13 (བསྡུས་དོན, s1) | Deva is a subtype of the 5-or-6 rebirth realms and a division of the threefold world. | Same. | YES | "ནི" added, no fact change. |
| 14 (བསྡུས་དོན, s2) | There is also a special class of devas — mountain devas, tree devas, etc. | Same. | YES | "དེ་ལས་གཞན" added as a transition; same claim. |
| 15 (བསྡུས་དོན, s3) | "Lake of gods" is explained in many different ways, including as a moon-metaphor. | Same. | YES | Restructured, same content: moon-metaphor is named as one of several explanations, matching the body above. |

## Ref attachment walk

All 23 `<ref>` tokens survived C1 (token conservation). Walked each one against the statement it sits on:

| ref name | Statement it supports, before | Statement it supports, after | Same? |
|---|---|---|---|
| dharmabhadra (×3) | intro classification; 5-fold rebirth count; moon-metaphor gloss of root verse | same three attachment points, same statements | YES |
| sungrab-tulku (×3) | intro classification; threefold-world (naga/human/god) grouping; "great worldly devas" collective category | same three attachment points | YES |
| tenga-tulku | 7-fold rebirth count (3 lower + human/god + form + formless) | same | YES |
| taranatha (×4) | 6-fold desire-realm devas; special helping/harming deva class; "lake of mind" alternate gloss; summary line | same four attachment points | YES |
| tsultrim-namdak (×2) | special helping/harming deva class (concurring with Taranatha); summary line | same | YES |
| tenzin-dhonzang | a fortiori reasoning (great devas worship → humans need not be mentioned) | same | YES |
| gendun-drub | moon-mandala/lake-of-gods simile | same | YES |
| konchok-thabkhe (×2) | Vedic churning-of-the-ocean etymology; summary line | same | YES |
| palden-sherab (×3) | two profound-hidden-meaning explanations (vajra-aggregate city; great perfection quote); summary line | same | YES |

No ref migrated to a different clause or statement.

## Flagged substitutions

Lexical-only swaps, same referent/meaning, listed for domain-expert acceptance — none block PASS:

| Location | Before | After | Note |
|---|---|---|---|
| མཚན་ཉིད, s1 | ནང་གསེས་ཤིག་ཏུ་བཤད་པའི | ནང་གསེས་སུ་གཏོགས་པའི | "explained as a subtype of" → "belonging to a subtype of" |
| མཚན་ཉིད, s1 | ལྔའམ་དྲུག་ཅིང་བདུན (mixed འམ/ཅིང་) | ལྔའམ་དྲུག་གམ་བདུན (parallel འམ/གམ) | grammar normalization of the three-way enumeration, same three numbers |
| དབྱེ་བ, s3 | ངོས་མ་བཟུང་བར ... གོ་བཞག་སྟེ | མིང་ནས་མ་སྨོས་པར ... ངོས་བཟུང་སྟེ | "not identifying by name / posited as" → "not mentioning by name / identified as" |
| གཞུང་ལུགས, s3 | བརྒྱུད་འགྲེལ་ (a lineage commentary) | འགྲེལ་རྒྱུན་ (a commentarial tradition) | both denote a transmitted commentarial source; not a different category of source |
| throughout | verb-ending/particle variants (ནས→ཀྱིས/ཡིས, སྟོན་→བསྟན་, སྦྱོར་→སྦྱར་, གྲངས→བགྲང, གསུངས།།→གསུངས་སོ།།, འགྲེལ།།→འགྲེལ་ལོ།།) | — | routine style/register polish, no meaning change |

## Reverted drift (if any)

None. No factual drift was found; Rule 8 was not invoked.

## Verdict

**PASS.** No fact was added, dropped, changed, or re-attributed. Every one of the 23 refs remains attached to the exact statement it supported before. Both verbatim quotations — the root-verse couplet ("ཕྱག་འཚལ་ལྷ་ཡི་མཚོ་ཡི་རྣམ་པའི།། རི་དྭགས་རྟགས་ཅད་ཕྱག་ན་བསྣམས་མ།།") and the Palden Sherab completion-stage-without-marks quotation ("ལྷ་ཡི་མཚོ་ཡི་རྣམ་པ་ནི་གནས་ལུགས་རྫོགས་པ་ཆེན་པོའོ།") — are character-for-character identical to the source, confirmed by direct comparison. No unattested honorific was inserted before any personal name (all name forms — ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ, རྒྱལ་བ་དགེ་འདུན་གྲུབ་, དཀོན་མཆོག་ཐབས་མཁས་, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་, སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་ — are byte-identical before/after). No scope-narrowing qualifier was dropped, no hedge was strengthened, no referent was changed. Length delta: tsheg count 702 → 704 (+0.28%), consistent with a pure prose-flow polish.
