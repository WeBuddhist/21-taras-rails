---
topic: tara-15
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-15/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-15

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | This is the 15th of the 21 praises; many commentaries ID it as the 15th | same, restyled word order | YES (after reversion) | quantifier "many" (མང་པོས) had been changed to "most" (མང་ཆེ་བས) — reverted, see below |
| 2 | Some commentaries instead count it as the 2nd of the dharmakāya-aspect subset | same | YES | "ཁ་ཤས"→"འགའ་ཞིག" both = "some/a few", synonymous |
| 3 | Root verse quoted verbatim | identical | YES | verbatim quote unchanged char-for-char |
| 4 | "ཞེས་གསུངས་སོ།།" closing | identical | YES | |
| 5 (heading) | Some commentaries give three different names for this deity | same, "all three" (སུམ་ཅར) softened to "about three" (གསུམ་ཙམ) | YES | count of 3 unaffected — 3 names are enumerated next; flagged as lexical substitution |
| 6 | 1st name: rje btsun ma zhi ba chen mo | same, reordered ("first, X is...") | YES | |
| 7 | 2nd name: sgrol ma rab zhi ma | same, reordered | YES | |
| 8 | 3rd name: dge legs zhi ba'i sgrol ma, per Gendun Drub | same | YES | |
| 9 | 3 commentaries: white, 2 arms, archer stance, right hand boon-granting mudrā, left hand holds long-necked vase of nectar atop utpala | same; "atop utpala" spatial relation preserved | YES | iconographic X-atop-Y relation intact |
| 10 | Trinlé Chardu Nyilwé Trinpung instead: white, 6 arms, vajra posture | same | YES | |
| 11 | Verse quoted verbatim | identical | YES | verbatim quote unchanged char-for-char |
| 12 | remaining 12 commentaries don't specify body form | same | YES | number 12 unchanged |
| 13 | all commentaries: mantra begins Oṃ, ends Svāhā; recitation destroys great sin | same; "adorned"→"concluded" for ending-verb, "said"→"asserted" | YES | synonym-level paraphrase, no fact change |
| 14 | Trinlé...Trinpung: specific mantra syllables Oṃ tāre tuttāre ture svāhā destroy great sin via blessing | identical mantra string | YES | mantra syllables unchanged char-for-char |
| 15 | Sungrab Tulku + Tenga Tulku: protects from 8 and 16 temporal fears | same | YES | names, numbers 8/16 unchanged |
| 16 | Palden Sherab + Sangye Nyentrul: generation-stage visualization — purifying goddesses emanate from heart, bathe practitioner in nectar, washing sins causing lower rebirth | same core visualization; "said to visualize" (བསྒོམ་པར་གསུངས) → "said one must visualize" (བསྒོམ་དགོས་ཚུལ་གསུངས) | YES | modal auxiliary added — flagged, not blocking (see below) |
| 17 | intro: 3 differing readings of bde ma/dge ma/zhi ma | same | YES | |
| 18 | reading 1 (majority of commentaries): as the deity's own qualities — bde ma=undefiled bliss, dge ma/zhi ma=virtuous/peaceful nature | identical | YES | this "མང་ཆེ་བས" (majority) was already the source wording, unchanged |
| 19 | reading 2 (3 commentaries): as states bestowed on other beings — bde ma=higher rebirth, dge ma=liberation, zhi ma=complete buddhahood; called the tantra's actual intent | same | YES | |
| 20 | Zurmang Khenpo Pema Namgyal: same 3-way correlation | same | YES | |
| 21 | reading 3: Gendun Drub's own commentary — via 4 paths; Drakpa Gyaltsen's system similar to reading 1; some scholars: 2 systems via 4 paths (accumulation/application/seeing/no-more-learning) | same | YES | numbers 4/2 unchanged |
| 22 | Jonang Taranatha + Khenchen Palden Sherab: ultimate meaning via 5 wisdoms | identical | YES | |
| 23 | Verse quoted verbatim (4 wisdoms enumerated) | identical | YES | verbatim quote unchanged char-for-char |
| 24 | Dorlop Tenga Tulku: this praise via 3 kāyas — bde ma etc.=dharmakāya qualities, mantra-protection=sambhogakāya, confession/purification=nirmāṇakāya; other commentaries don't use 3-kāya framing | same | YES | |
| 25 | Zurmang Khenpo Pema Namgyal: hidden-meaning reading via 4th-empowerment wisdoms, but this is part of a broader summary not specific to this praise alone, so hard to read in isolation | same | YES | |

## Ref attachment walk

All 14 distinct `<ref>` names (36 token instances) checked against the statement they support in body-before.txt vs body-after.txt:

- taranatha — 15th-praise ID / mantra section / 5-wisdoms reading / 4-wisdoms verse: same statements in both. YES
- yama-sonam — 15th-praise ID / root verse / name-1 / body-verse / mantra / name-3-corroboration: same in both. YES
- dharmabhadra — 2nd dharmakāya-subset count: same. YES
- gendun-drub — 15th-count / name-1 / name-3 / 4-paths system: same. YES
- sungrab-tulku — name-1 gloss / 8-16 fears: same. YES
- tenzin-dhonzang — name-1 gloss: same. YES
- palden-sherab — iconography / mantra-recitation / reading-2 correlation / 5-wisdoms verse / 3-kāya section: same. YES
- sangye-nyentrul — iconography / reading-2 correlation: same. YES
- tsultrim-namdak — iconography / mantra-recitation: same. YES
- drakpa-gyaltsen — reading-1: same. YES
- gendun-gyatso — reading-1: same. YES
- konchok-thabkhe — reading-2: same. YES
- pema-namgyal — reading-2 (Zurmang) / hidden-meaning reading: same. YES
- tenga-tulku — 8-16 fears / 3-kāya section: same. YES

No ref migrated to a different statement.

## Flagged substitutions

(lexical-only swaps, same referent/meaning — do not block PASS)

| Location | Before | After |
|---|---|---|
| heading intro (§ Definitive term of the name) | སུམ་ཅར ("all three together") | གསུམ་ཙམ ("about three") |
| para 2 | འགྲེལ་པ་ཁ་ཤས་ ("a few commentaries") | འགྲེལ་པ་འགའ་ཞིག་ ("some commentaries") |
| mantra section | མགོ་བརྒྱན...མཇུག་བརྒྱན ("headed/tailed by") | མགོ་བརྒྱན...མཇུག་བསྡུས ("headed/concluded by") |
| mantra section | མཐུན་པར་བཤད་དོ ("said in agreement") | མཐུན་པར་བཞེད་དོ ("held/asserted in agreement") |
| generation-stage visualization (§ Activity and power) | བཀྲུས་པར་བསྒོམ་པར་གསུངས ("said to visualize [it] washing") | དག་པར་བསྒོམ་དགོས་ཚུལ་གསུངས ("said one must visualize [it] purifying") — modal "must" (དགོས) added; reviewed and judged non-blocking since the passage describes a sādhana instruction (inherently prescriptive genre) and no position-holder, correlation, or content changed |

## Reverted drift

- **Location:** paragraph 1 (15th-praise identification sentence).
- **Drift:** Gemini changed འགྲེལ་པ་**མང་པོས** ("many commentaries [ID it as the 15th]") to འགྲེལ་པ་**མང་ཆེ་བས** ("the majority/most commentaries..."). This upgrades an indefinite-plural consensus claim ("many") into a majority claim ("most") — the same stronger-unsupported-claim pattern flagged in the skill's known-drift guidance (cf. "designated as" → "popularly known as"). Confirmed as a genuine change (not source wording) by checking body-before.txt line 1, which reads མང་པོས.
- **Remedy applied:** surgical reversion (Rule 8a) — restored མང་པོས in `article.md`, leaving the rest of Gemini's restyled clause (word order, ཅིང་ ending) untouched. `body-after.txt` left as the unmodified raw model record per the rule.
- Note: a second, unrelated occurrence of མང་ཆེ་བས appears later in the article (§ གཞུང་ལུགས་སོ་སོའི་བཤད་པ།, "reading 1"); checked against body-before.txt line 35 and confirmed this was already the source's own wording (not introduced by Gemini) — left untouched.

## Verdict

PASS-after-reversion. One factual drift (a quantifier upgrade from "many" to "most" commentaries) was found and surgically reverted in `article.md`; no other fact, name, number, doctrinal position, position-holder, or verbatim quotation was added, dropped, weakened, strengthened, or re-attached to a different ref. Every ref supports the same statement before and after polishing. Two lexical-only substitutions and one modal-auxiliary addition are recorded above for the domain expert's awareness but do not block PASS.
