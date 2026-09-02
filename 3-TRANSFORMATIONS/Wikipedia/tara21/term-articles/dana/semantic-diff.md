---
topic: dana
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/dana/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — dana

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Dāna is the first of the six pāramitās; per the verse-3 praise to the 21 Tārā "generosity, diligence, austerity, peace..." quote, dāna is placed first among her spheres of activity per all 16 commentaries (lit. or by implication). | Same — clause order shifted, "third stanza" phrase reordered, quote untouched. | Yes | Split into two sentences; reorders "gsum pa'i tshigs bcad" → "tshigs bcad gsum pa" (both = "third verse"). Verbatim quote character-identical. |
| 2 | Many commentaries also depict Tārā holding a lotus arisen from water, golden-blue in color, acting in the sphere of the six pāramitās including dāna. | Same, with added connective "gzhan yang" (moreover). | Yes | Connective added, no content change. |
| 3 (ངེས་ཚིག) | Drakpa Gyaltsen glosses the term itself as designating dāna-pāramitā. | Same. | Yes | Dropped the case particle ལ after དོན་ཉིད (minor grammar-particle change), no meaning change. |
| 4 (དབྱེ་བ) | Tenzin Dhonzang divides dāna into three types (material, protection-from-fear, Dharma) per quote; commentaries differ on the pāramitā count — most count six, but Khenchen Palden Sherab and Tenzin Dhonzang both count ten at the bhūmi stage by adding four (means, power, etc.); Könchok Tabkhé identifies wisdom-pāramitā itself as Tārā's essence with the five (incl. dāna) as her sphere; Khenpo Tsultrim Namdak also places this verse among the 37 bodhipakṣa dharmas. | Same facts, same order, same attributions. | Yes | Sentence-final particles changed (ལ→སོ།།, etc.), "སྣོན་ནས"→"བསྣན་ནས" (same verb, tense-form variant), "ངོས་འཛིན་བྱས་ནས"→"ངོས་འཛིན་མཛད་དེ" (honorific verb form — see Flagged substitutions). Verbatim quote character-identical. |
| 5 (སེར་སྣའི་གཉེན་པོར) | Three commentaries identify dāna as the antidote to miserliness, undefiled by its fault; Tenzin Dhonzang, citing the Abhidharmakośa, explains dāna's "enemy" is miserliness. | Same. | Yes | "ངོས་འཛིན་བྱེད་དེ"→"ངོས་འཛིན་མཛད་དེ" (honorific verb applied to a text-subject — see Flagged substitutions). Restructured clause "dāna's enemy" but same claim. |
| 6 (གཞུང་ལུགས་སོ་སོའི་བཤད་པ) | Tāranātha: hidden meaning is dāna as abandoning self-grasping. Khenchen Palden Sherab: two orders — completion-stage (freedom from self-grasping re: bliss) and ultimate (non-grasping, per the Brahmaviśeṣacintāparipṛcchā sūtra). | Same, both positions attributed to same two named authors. | Yes | Agent particles ནས→ཡིས/ཀྱིས swapped (same grammatical role); "དེ་བཞིན་དུ" (likewise) added as connective. |
| 7 (ལུང་གཞན་ལས་དྲངས་པའི་བཤད་པ) | Tenzin Dhonzang cites the Prātimokṣa-sūtra: dāna increases merit; and the Lam rim bsdus don: dāna is the wish-fulfilling jewel and the supreme weapon cutting the knot of miserliness. | Same. | Yes | "གཞན་ཡང" added as connective; particle ལ→ནི 삽입 style swap. |
| 8 (བསྡུས་དོན) | All 16 commentaries place dāna first among Tārā's pāramitā-spheres; some as antidote to miserliness; some as freedom from/non-grasping in the ultimate sense. | Same, same attributions and ref order. | Yes | "མདོར་ན" (in short) added, matching the "Summary" heading; no fact change. |

## Ref attachment walk

| Ref | Statement supported before | Same after? |
|---|---|---|
| tenzin-dhonzang (full, x1) + repeats (x5) | verse-3 quote/placement sentence; dāna's threefold division; ten-pāramitā count; Abhidharmakośa "enemy=miserliness"; Prātimokṣa-sūtra merit citation; Lam rim bsdus don citation; summary sentence 1 | YES — all six occurrences attached to the identical statements, same order |
| palden-sherab (full, x1) + repeats (x4) | verse-3 quote/placement sentence; ten-pāramitā count; two-order (completion-stage/ultimate) statements (x2); summary sentence 1 | YES |
| yama-sonam (full) | verse-3 quote/placement sentence | YES |
| dharmabhadra (full) | lotus-imagery sentence | YES |
| sungrab-tulku (full, x1) + repeat (x1) | lotus-imagery sentence; "antidote to miserliness" sentence; summary "some say antidote" clause | YES |
| gendun-drub (full) | lotus-imagery sentence | YES |
| drakpa-gyaltsen (full) | ངེས་ཚིག gloss sentence | YES |
| konchok-thabkhe (full) | wisdom-pāramitā-as-Tārā's-essence sentence | YES |
| tsultrim-namdak (full) | 37-bodhipakṣa-dharmas sentence | YES |
| tenga-tulku (full) | "antidote to miserliness, undefiled" sentence | YES |
| taranatha (full, x1) + repeat (x1) | hidden-meaning/self-grasping sentence; summary "some say ultimate/non-grasping" clause | YES |

Every ref token (25 total, C1-verified) remained attached to the same statement it supported before polishing; no ref migrated to a different clause.

## Flagged substitutions

Lexical/register-only swaps, same referent and meaning — listed for domain-expert acceptance, does not block PASS:

| Before | After | Note |
|---|---|---|
| གསུམ་པའི་ཚིགས་བཅད (verse-3, genitive-first) | ཚིགས་བཅད་གསུམ་པ (verse-3, noun-first) | Word-order swap, identical meaning ("the third verse"). |
| དོན་ཉིད་ལ (with ལ particle) | དོན་ཉིད (particle dropped) | Minor case-particle omission, no meaning change. |
| སྣོན་ནས | བསྣན་ནས | Same verb "to add", different tense/aspect form. |
| ནས / ལ (agent/topic particles, several places) | ཡིས / ཀྱིས / ནི (agent/topic particles) | Grammatical particle variants, same syntactic role. |
| དཀོན་མཆོག་ཐབས་མཁས་...ངོས་འཛིན་བྱས་ནས | ...ངོས་འཛིན་མཛད་དེ | Plain verb → honorific verb form, subject is a named person — stylistically elevated register, not a title before the name, no fact change. |
| འགྲེལ་པ་གསུམ་...ངོས་འཛིན་བྱེད་དེ | ...ངོས་འཛིན་མཛད་དེ | Plain verb → honorific verb form, but here the grammatical subject is "three commentaries" (a text), not a person — an unusual honorific-register choice worth a human editor's attention, though it does not add/change any claim or attribution. |

None of these touch a personal-name title (སློབ་དཔོན་/གྲུབ་ཆེན་/རྗེ་བཙུན་/མཁན་ཆེན་ etc.) — the known drift pattern from the 2026-08-21 pilot was specifically checked for and not found. Every personal name (རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་, ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ་, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་, སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་, དཀོན་མཆོག་ཐབས་མཁས་, མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག) carries exactly the same title/epithet words in both versions.

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** No fact, name, number, doctrinal position, or position-attribution was added, dropped, weakened, strengthened, or re-attributed. All verbatim quotations ("…") are character-for-character identical to the source. Every `<ref>` remains attached to the exact statement it supported before polishing, in the same order. Only lexical/grammatical register substitutions were found (word order, particle variants, verb-honorification), listed above under Flagged substitutions for the domain expert's discretion — none of them alter meaning. The tail-heading boundary before `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` is clean (blank line present, no reassembly-bug artifact). Length delta: +1.1% by tsheg count (well within the ±25% soft-check tolerance).
