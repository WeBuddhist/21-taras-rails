---
topic: gandharva
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/gandharva/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — gandharva

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: gandharva (dri za) is a class of beings in root verse 21 of the Praise to Tara; many commentaries identify it as part of the fourfold retinue (with bhūtas, vetālas, yakṣas) praising before Tārā; quotes the root verse "ཕྱག་འཚལ་བརྒྱ་བྱིན..." verbatim. | Same content, reworded; quote reproduced verbatim. | YES | Verbatim quote checked character-for-character — identical. |
| 2 | ~12 commentaries mention the name "gandharva" within this verse's word-gloss/summary, but disagree on its exact nature. | Same. | YES | |
| 3 | Dharmabhadra: gandharva = retinue of Indra (brgya byin). | Same. | YES | |
| 4 | Lobsang Dawa and Sungrab Tulku concur with Dharmabhadra. | Same. | YES | |
| 5 | Palden Sherab and Sangye Nyentrul: explained in detail as belonging to the eastern maṇḍala wheel-deity Indra's "various-chariot" (sna tshogs shing rta) retinue. | Initial polish inserted the word དྲི་ཟ into this clause, producing the exact compound "དྲི་ཟ་སྣ་ཚོགས་ཤིང་རྟ" — contradicting sentence 6 below (Taranatha's name is unique). **Reverted** to the source's exact wording (see Reverted drift). | YES (after reversion) | See Reverted drift entry. |
| 6 | Taranatha alone uses the name "gandharva various-chariot" (dri za sna tshogs shing rta); no other commentary uses this name. | Same. | YES | This is the statement that made entry 5's drift detectable as a contradiction. |
| 7 | Konchok Thabkhe: gandharva is not an actual class-name but another name for Yama (gshin rje); quotes his reasoning from Abhidharma synonym lists verbatim. | Same content, reworded; quote reproduced verbatim. | YES | Verbatim quote checked character-for-character — identical. |
| 8 | Tenga Tulku: gandharvas are beings wandering the bardo of existence — similar position, but without the Abhidharma/Yama link. | Same. | YES | |
| 9 | Completion-stage hidden meaning: Palden Sherab and Taranatha both give the same reading, connecting gandharva to wind (rlung). | Same. | YES | |
| 10 | Benefits: Zurmang Khenpo Pema Namgyal — even the king of gandharvas (Ljon-pa rta-mgo-can) and the gandharva assembly, trembling in fear, praise Tārā; prostrating to Tārā frees one from their fear for all lifetimes. | Same. | YES | |
| 11 | Classification: Sermey Tsang Geshe Tenzin Dhonzang cites another text (Gdugs dkar) placing gandharva-affliction among the "28 dön"; no other commentary includes gandharva among the dön. | Same; source's "གདོན་གཉེར་བརྒྱད" (non-standard) rendered as "གདོན་ཉེར་བརྒྱད" (standard numeral form, 28). | YES | Spelling normalization, see Flagged substitutions. |
| 12 | Summary: no unified view of gandharva's nature — four positions: Indra's retinue / marked by five tufts / another name (for Yama) / bardo-being connected to Yama. | Same four positions, reworded as an explicit list. | YES | |

## Ref attachment walk

All 21 ref-token instances (15 unique ref names) were walked against the statement each supports, before and after polish, after the reversion above:

| ref name | statement supported (before = after) | Same? |
|---|---|---|
| yama-sonam | cites the root-verse quote / summary of 4 divergent positions | YES |
| dharmabhadra | Dharmabhadra's gandharva=Indra's-retinue claim (2 attachments: source ref + self-close) | YES |
| palden-sherab | Palden Sherab's eastern-maṇḍala claim; also completion-stage rlung claim (2 attachments) | YES |
| lobsang-dawa | Lobsang Dawa concurring with Dharmabhadra | YES |
| sungrab-tulku | Sungrab Tulku concurring with Dharmabhadra | YES |
| sangye-nyentrul | Sangye Nyentrul's eastern-maṇḍala claim (co-attached with palden-sherab) | YES |
| drakpa-gyaltsen | Drakpa Gyaltsen's five-tufts claim | YES |
| gendun-drub | Gendun Drub concurring on five-tufts / king-of-gandharvas | YES |
| karma-maitri | Karma Maitri concurring on five-tufts | YES |
| gendun-gyatso | Gendun Gyatso concurring on five-tufts | YES |
| taranatha | Taranatha's unique "gandharva various-chariot" name claim; also completion-stage rlung claim (2 attachments) | YES |
| konchok-thabkhe | Konchok Thabkhe's Yama-synonym claim (2 attachments: source ref + self-close after quote) | YES |
| tenga-tulku | Tenga Tulku's bardo-being claim | YES |
| pema-namgyal | Zurmang Khenpo Pema Namgyal's benefits claim | YES |
| tenzin-dhonzang | Tenzin Dhonzang's 28-dön classification claim | YES |

No ref migrated to a different statement. Count matches gemini-report.md ("refs frozen as tokens: 21").

## Flagged substitutions

Lexical-only swaps, same referent/meaning — do not block PASS:

| Location | Before | After | Note |
|---|---|---|---|
| Dbye ba paragraph | གདོན་གཉེར་བརྒྱད | གདོན་ཉེར་བརྒྱད | Numeral spelling normalization ("gnyer brgyad" → standard "nyer brgyad" = 28); same referent (the 28 dön class), no change in count or meaning. |
| Dbye ba paragraph | ...ལས་དྲངས་ཏེ | ...ལུང་དུ་དྲངས་ཏེ | Synonymous phrasing for "cited [from]"; same source-text reference (Gdugs dkar). |
| Throughout | བཤད / ངོས་འཛིན་བྱེད / འདྲེན | གསུངས / བཞེད / ངོས་འཛིན / དྲངས / མཛད | General register-level verb variation (bshad ↔ gsungs/bzhed, etc.) consistent with honorific register already used in the source article; no attribution or claim-strength change. |

## Reverted drift

**Location:** Palden Sherab / Sangye Nyentrul paragraph (== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==, second sentence).

**Drift found:** The first polish pass inserted the word དྲི་ཟ directly before སྣ་ཚོགས་ཤིང་རྟའི་འཁོར in this sentence, producing the exact compound "དྲི་ཟ་སྣ་ཚོགས་ཤིང་རྟ" (gandharva various-chariot). This string is byte-identical to the name that the article's very next sentence (ref: taranatha) explicitly states is used **only** by Taranatha, by no other commentary. The insertion silently created an internal contradiction not present in the source — the source's original clause did not contain the word དྲི་ཟ at all in this sentence (the topic "gandharva" was carried implicitly from the paragraph's established subject, referring only to a general "various-chariot retinue" category, not the specific named epithet). This matches known drift pattern (g) "a referent silently changed."

**Remedy applied:** Surgical reversion (Rule 8a) — restored the clause to the source's exact wording:
- Reverted: `ཤར་ཕྱོགས་ཀྱི་དཀྱིལ་འཁོར་གྱི་ལྷ་བརྒྱ་བྱིན་གྱི་འཁོར་དྲི་ཟ་སྣ་ཚོགས་ཤིང་རྟའི་འཁོར་ཡིན་པར་ཞིབ་ཏུ་གསུངས་སོ།།`
- To (source's exact text): `ཤར་ཕྱོགས་ཀྱི་དཀྱིལ་འཁོར་འཁོར་ལྷ་བརྒྱ་བྱིན་གྱི་སྣ་ཚོགས་ཤིང་རྟའི་འཁོར་དུ་ཞིབ་ཏུ་བཤད་དོ།།`

`body-after.txt` was left untouched as the raw model record, per Rule 8(a). The edit was applied directly to `article.md`.

## Verdict

**PASS-after-reversion.** One factual drift was found and surgically reverted (see above); no other fact was added, dropped, changed, or re-attributed. Every ref remains attached to the exact statement it supported in the source. Both verbatim quotations are character-for-character identical to the source. All remaining differences are lexical/register-level substitutions (flagged, non-blocking).
