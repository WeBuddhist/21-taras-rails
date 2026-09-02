---
topic: bhuta
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/bhuta/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — bhuta

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Bhuta is one member of the fourfold class of demigods (with rolangs, driza, nöjin) who worship Tārā from the front, per verse 6 of the praise; so explained by 15 commentaries. | Same claim, same verse (6th), same quote, same "15 commentaries" figure. | YES | "of the text" (gzhung gi) dropped before "sixth verse" — redundant given the verse is already anchored to the named praise text in the same clause; no referent change. |
| 2 | Many commentaries: verse 6 shows 5 great gods (Indra, fire-god, Brahmā, wind-god, Maheśvara) worshipping, and bhuta+rolangs+driza+nöjin praising from the front. | Same 5 gods, same 4-being group, same claim. | YES | Comma/shad-only list punctuation merged; "'di" → "'dis" case-marker shift on "this verse" (topic marker), no change to who does what. |
| 3 | Karma Maitri: identifies bhuta by name alone as a demigod class praising from the front. | Same. | YES | Verb tense byed→byas yod (present→"has done"), no fact change. |
| 4 | Könchok Thabkhé: gives spelling variant 'byung bo (one syllable different). | Identical sentence, byte-for-byte. | YES | No change. |
| 5 | Drakpa Gyaltsen: bhuta explained as a class exemplified by tsok-dak etc. | Same. | YES | nga → gyis nga (agentive made explicit); "bhuta" → "bhuta zhes pa" (quotative added); no fact change. |
| 6 | Gendün Drub, Gendün Gyatso, Zurmang Khenpo Pema Namgyal agree: tsok-kyi-dakpo is the chief of bhuta; prostration frees from all fear forever. | Same 3 names, same claim. | YES | byed→mdzad (honorific verb upgrade for the cited masters' action) — register shift only. |
| 7 | Tāranātha: different approach — tsok-kyi-dakpo is of the gek (obstructor) class. | Same. | YES | thabs lugs→lugs (dropped "means/method", "way" retained); bshad→bzhed (honorific). |
| 8 | Khenpo Tsultrim Namdak, Khenchen Palden Sherab, Sangye Nyentrul Rinpoche agree: the northeast-retinue bhuta is of the gek/misleading-spirit class. | Same 3 names, same claim. | YES | List punctuation merged only. |
| 9 | Ngulchu Dharmabhadra: bhuta explained as part of Wangden's retinue. | Same. | YES | Ergative particle added (na→yis ni); no fact change. |
| 10 | Geshe Lobsang Dawa, Drepa Rawa Trashö Sungrab Tulku, Könchok Thabkhe agree: bhuta is Wangden's retinue or synonymous with it. | Same 3 names, same claim. | YES | Punctuation only. |
| 11 | Dorje Lopön Tenga Tulku: different approach — bhuta is of the preta class, a sky-roaming being tormented by fear and suffering (verbatim quote). | Same, quote identical. | YES | thabs lugs→lugs, bshad→bzhed (honorific/register only); ཀྱིས→གྱིས spelling-rule correction after la-final name. |
| 12 | Dzogrim (completion-stage) reading: the 4 retinue members map to channel/drop/wind/thought — bhuta=channel, rolangs=drop, driza=wind, nöjin=thought. | Same 4-way mapping, same assignment. | YES | Case markers on the mapped terms changed (terminative→associative/absolutive) but each assignment (bhuta↔rtsa, rolangs↔thig le, driza↔rlung, nöjin↔rnam rtog) is unchanged. |
| 13 | Tenzin Dhönzang (Sera Mé): main activity is pacifying bhuta-caused harm/illness/mental suffering across the three realms; also counted among the 10 directional protectors, summoned as a servant of Tārā's activity. | Same claim, same two sub-claims. | YES | btsugs→bcug ("placed/included", causative synonym); grammatical restructuring only. |
| 14 | Sungrab Tulku: in verse 21, when the three hosts of gdön/rolangs/nöjin are destroyed, bhuta is appended as the 4th. | Same three named hosts + bhuta as 4th. | YES | ས→ཡིས agentive spelling correction; punctuation merged. |
| 15 | Tsultrim Namdak's historical anecdote: bhuta-caused misfortune at a bridge was pacified by placing a pile of Tārā-mantra-carved maṇi stones, cutting off the bhuta's path. | Same anecdote, same mechanism, same object (maṇi-stone pile). | YES | bshad→gsungs (honorific); "maṇ phung" expanded to "ma ṇi'i phung po" — orthographic expansion of the same referent, not a different object. |
| 16 | Summary: bhuta is one of the fourfold asura-class (with rolangs, driza, nöjin) per verse 6; commentaries variously identify it as tsok-kyi-dakpo, or gek class, or Wangden's retinue. | Same. | YES | Synonym swap bcas dang bcas pa→bcas dang lhan cig pa ("together with"); byed→mdzad + rephrase "so 'dra ba mdzad yod" (honorific + "have identified differently") — same 3-way divergence preserved. |
| 17 | Summary cont'd: Tenga Tulku identifies it as preta class. | Same. | YES | byed do→mdzad do (honorific only). |

## Ref attachment walk

All 30 ref tokens (16 distinct names) were checked against the sentence each is attached to in body-before.txt vs body-after.txt. Order and position of every `<ref>`/self-closing `<ref name=... />` is unchanged sentence-for-sentence:

- `drakpa-gyaltsen`, `taranatha`, `tenzin-dhonzang` — lede sentence (#1) — SAME
- `yama-sonam`, `dharmabhadra`, `palden-sherab` — ngestsig deity-list sentence (#2) — SAME
- `karma-maitri` — Karma Maitri sentence (#3) — SAME
- `konchok-thabkhe` — spelling-variant sentence (#4) — SAME
- `drakpa-gyaltsen` (self-closing) — Drakpa Gyaltsen sentence (#5) — SAME
- `gendun-drub`, `gendun-gyatso`, `pema-namgyal` — Gendün Drub/Gyatso/Pema Namgyal sentence (#6) — SAME
- `taranatha` (self-closing) — Tāranātha sentence (#7) — SAME
- `tsultrim-namdak`, `palden-sherab` (self-closing), `sangye-nyentrul` — sentence #8 — SAME
- `dharmabhadra` (self-closing) — sentence #9 — SAME
- `lobsang-dawa`, `sungrab-tulku`, `konchok-thabkhe` (self-closing) — sentence #10 — SAME
- `tenga-tulku` — sentence #11 — SAME
- `palden-sherab` (self-closing), `taranatha` (self-closing) — dzogrim mapping sentence (#12) — SAME
- `tenzin-dhonzang` (self-closing) — sentence #13 — SAME
- `sungrab-tulku` (self-closing) — sentence #14 — SAME
- `tsultrim-namdak` (self-closing) — sentence #15 — SAME
- `drakpa-gyaltsen`, `taranatha`, `dharmabhadra` (self-closing, ×3) — summary sentence #16 — SAME
- `tenga-tulku` (self-closing) — summary sentence #17 — SAME

No ref migrated to a different clause or statement. Every ref still supports the exact same assertion it supported before polishing.

## Flagged substitutions

Lexical/register-only swaps, same referent and meaning throughout — for the domain expert to accept or reject, none of which block PASS:

| Before | After | Where | Type |
|---|---|---|---|
| ངོས་འཛིན་བྱེད (byed, plain) | ངོས་འཛིན་མཛད (mdzad, honorific) | recurs ~6× across sentences #6, 7, 16, 17 (also བཤད→བཞེད/གསུངས in #7, 11, 15) | Systematic honorific-register upgrade applied to the actions of the named commentators. No new claim, no re-attribution — same masters, same positions. |
| ཐབས་ལུགས་ (method/means) | ལུགས་ (way/system) | sentences #7, #11 | "ཐབས" dropped; "ལུགས" alone still conveys "approach" — no narrowing or broadening of the claim. |
| མཎ་ཕུང (informal/abbreviated) | མ་ཎིའི་ཕུང་པོ (spelled out) | sentence #15 | Orthographic expansion of the same referent (pile of maṇi/mantra stones), not a different object. |
| ཀྱིས / ས (ergative, after la-/vowel-final names) | གྱིས / ཡིས (ergative) | sentences #11, #14 | Standard Tibetan ergative-allomorph corrections (grammar/spelling normalisation), no semantic change. |
| བཙུགས (btsugs) | བཅུག (bcug) | sentence #13 | Synonymous causative form of "place/include" — same claim (bhuta counted among the 10 directional protectors). |
| བཅས་དང་བཅས་པའི | བཅས་དང་ལྷན་ཅིག་པའི | sentence #16 | Both mean "together with" — synonym swap. |

## Reverted drift (if any)

None. No factual drift was found — all differences above are word-order, case-marking, punctuation, or honorific-register changes with no effect on facts, numbers, names, doctrinal positions, or which commentator holds which position. No surgical reversion was necessary.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened, or re-attributed. All 17 sentence-level units carry identical factual content before and after. All 3 verbatim quotations are character-for-character identical (re-confirmed by eye, consistent with the script's C3 pass). All 30 ref tokens remain attached to the exact same statement they supported before polishing, in the same order. The systematic byed→mdzad / bshad→bzhed/gsungs honorific-register upgrade applied to the cited commentators' actions is a consistent style choice, not a title inserted before a personal name (the known drift pattern in Rule 8 concerns unattested honorific titles prefixed to names, e.g. slob dpon before a name — not honorific verb conjugation for already-named masters), and is recorded above as a flagged substitution for the domain expert's discretion, not drift.
