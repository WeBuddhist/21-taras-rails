---
topic: tara-02
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-02/article.md
model: gemini-3.1-pro-preview
date: 2026-08-21
verdict: PASS
status: draft
---

# Semantic diff — tara-02

## W1 warning resolution (all 6 judged false positives)

The script's C1–C7 checks all passed; W1 flags a paragraph not ending in `།།`. All six flagged paragraphs are pre-existing structural units in the *source* article (verified against `body-before.txt`, where the identical paragraph-break pattern already exists) — Gemini's recomposition did not introduce or alter this structure.

| Paragraph | Ending | Judgment |
|---|---|---|
| 1 | `…རྩ་བའི་ཚིགས་བཅད་ལས།` | False positive — lead-in line ending in `ལས།`, introducing the verse-quote block in paragraph 2. |
| 2 | `…རབ་འབར་མ།"` | False positive — standalone verse-quote paragraph ending in a closing quote mark. |
| 5 | `…རང་གི་འགྲེལ་པར།` | False positive — lead-in line ending in a single shad, introducing the quoted line "འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།" in the next paragraph (structurally identical to paragraph-1's `ལས།` lead-in). |
| 6 | `…ཞེས་བཤད་དོ།"` | False positive — standalone verse/citation-quote paragraph ending in a closing quote mark. |
| 10 | `…ཀྱང་བཤད་དེ།` | False positive — lead-in line ending in `ཏེ/དེ།`, introducing the quoted verse in the following paragraph. |
| 11 | `…པོ་ཏི་གཡོན།"` | False positive — standalone verse-quote paragraph ending in a closing quote mark. |

No re-run needed; all six match the two documented false-positive patterns.

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Opening: this deity is the 2nd prostration of the 21-praises to Tārā. | Same, word order changed (num.-noun inverted). | YES | Style only. |
| 2 | Root verse quote (autumn-moon face, thousand stars). | Character-for-character identical. | YES | Verbatim quote preserved. |
| 3 | "As stated, all recognize [her] as a goddess white/beautiful like a hundred stacked autumn moons, light surpassing a thousand stars." | Same content; མཐའ་དག → ཀུན (both "all"); ལྷ་མོར → ལྷ་མོ་ཞིག་ཏུ (indefinite marker added). | YES | Lexical substitution — see flagged list. |
| 4 | Heading: མཚན་གྱི་ངེས་ཚིག | Identical. | YES | — |
| 5 | Different traditions give different names; no single name settled. Named Lodter Yangchenma. | Same; མ་གྲུབ → མ་ངེས (synonym); adds སྤྱིར ("generally") before the naming clause. | YES | Lexical substitution — see flagged list. |
| 6 | "However, in Gyalwa Gendün Drub's own commentary…" | Same; རང་ཉིད་ཀྱི → རང་གི (both "own"); འགྲེལ་བར → འགྲེལ་པར (spelling variant). | YES | Style only. |
| 7 | Quote: "འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།" | Character-for-character identical. | YES | Verbatim quote preserved. |
| 8 | "…and in Yama Sönam's commentary too, this is identified as Gendün Drub's tradition." | Same; འགྲེལ་བ→འགྲེལ་པ (variant); ངོས་འཛིན་བྱེད→ངོས་བཟུང (synonym "recognize"). | YES | Style only. |
| 9 | Tenzin Dhönzang names her "Zhiwa Chenmo"; Geshe Lobsang Dawa's sub-commentary: no new name given, named from root verse's final words "Ö Rab Barma." | Same facts, restructured; གདགས→བཏགས (synonym "name/label"). | YES | Style only. |
| 10 | Heading: སྐུ་ཡི་རྣམ་པ། | Identical. | YES | — |
| 11 | Face white/beautiful like stacked autumn moons; body color also white; per Sangye Nyentrül & Palden Sherab: peaceful 1-face/2-arm form, half-vajra posture on lotus-moon seat, right hand boon-granting mudrā, left hand holds utpala marked by mirror+seed-syllable; "renowned as such" (གྲགས་སོ). | Same facts; "mirror AND seed-syllable letter" made explicit with དང; final verb གྲགས་སོ ("renowned") → བཞེད་དོ ("[they] assert/hold"). | YES | Lexical substitution — see flagged list (verb shift). |
| 12 | "In a commentary of Yama Sönam, based on the words of Nyima Bepa, another body-form is also explained." | Same; adds title སློབ་དཔོན் ("master/ācārya") before the name "Nyima Bepa." | YES | Lexical/honorific addition — see flagged list. |
| 13 | Quote: 3-face/12-hand verse (6 lines). | Character-for-character identical. | YES | Verbatim quote preserved. |
| 14 | "Thus, also explained with 3 faces/12 hands. Other commentaries give no scriptural basis for the count on this verse-line; this elaborated form is unique to Yama Sönam's commentary alone." | Same facts; only case-particle/connective changes (ཀྱིས་ནི→སུ, ཏེ→པས, ཡིན་ནོ→གོ). | YES | Style only. |
| 15 | Heading: ཕྲིན་ལས་དང་ནུས་མཐུ། | Identical. | YES | — |
| 16 | Light from the mirror dispels beings' ignorance-darkness; per Sangye Nyentrül, increases wisdom-power and expands intelligence. | Same; adds ཕྱག་གི ("of the hand") before "mirror" — clarifies which mirror (already established in para. 11), not a new fact. | YES | Minor clarifying addition — see flagged list. |
| 17 | Per Zurmang Khenpo Pema Namgyal: visualizing nectar-light dissolving into oneself grants siddhis of longevity and wisdom. | Same, spelling/particle variants only. | YES | Style only. |
| 18 | Per Geshe Tenzin Dhönzang: uncommon glud (ransom) practice — offering own downfalls/obscurations with the lama's body-effigy to the Lord of Death, satisfying all karmic debts; love/compassion/bodhicitta are the supreme "ransom from death"; main activity is dispelling harm from döns/obstructing spirits and physical/mental illness. | Same facts; བཅས→ལྷན་དུ, འབུལ→ཕུལ (synonyms); བྱམས་སྙིང་རྗེ expanded to བྱམས་པ་དང་སྙིང་རྗེ ("love AND compassion," same compound spelled out). | YES | Style only. |
| 19 | Heading: སྦས་དོན་གྱི་བཤད་པ། | Identical. | YES | — |
| 20 | Per Tāranātha and Palden Sherab (completion-stage secret meaning): hundred-stacked moon = bodhicitta rising unmoving from the jewel to the crown; thousand stars = pervading all subtle channels. | Same facts, particle additions only (བྱང་ཆུབ་སེམས→བྱང་ཆུབ་ཀྱི་སེམས; ཁྱབ་པའི→ལ་ཁྱབ་པའི). | YES | Style only. |
| 21 | Palden Sherab alone: also explained as pervading the 4 cakras via bliss-emptiness co-emergent wisdom; generation-stage focus: white Vajra-Sarasvatī at Yeshe Tsogyal's heart; ultimate: introduced as Vajravārāhī's own face, moon-stack manifestation. | Same facts; adds དེ་ཉིད ("that very one," anaphoric, no new referent); བྱེད་དོ→མཛད་དོ (honorific upgrade of "does/reveals"). | YES | Style only (honorific register). |
| 22 | Heading: གཞུང་ལུགས་སོ་སོའི་བཤད་པ། | Identical. | YES | — |
| 23 | Traditions differ on "rab tu phye": most say light surpasses stars; Gendün Gyatso (2nd Dalai Lama) says "adorned by stars"; Yama Sönam critiques predecessors (starlight = inferior simile, an insult if applied to the goddess), reads "rab tu phye" as "opening/revealing the moon's light to direct perception." | Same facts; བཤད་ན→བཤད་ཀྱང (connective swap, same contrastive sense: "if/when most explain X" → "although most explain X"); rest of the Yama Sönam clause is character-identical. | YES | Lexical substitution (connective) — noted, minor. |
| 24 | Traditions differ on what the light-rays signify: Palden Sherab & Sangye Nyentrül — 4 correct knowledges (meaning, dharma, expression, eloquence); Tenzin Dhönzang — 4 wisdoms (vast, clear, swift, profound). | Same facts, list-punctuation/connective restructuring only. | YES | Style only. |
| 25 | Heading: བསྡུས་དོན། | Identical. | YES | — |
| 26 | Conclusion: despite major doctrinal differences on name/body-form/verse-meaning, all agree she is recognized as the goddess showing wisdom-light, white and radiant like the autumn moon, surpassing the stars. | Same facts; adds མཐུན་པར ("in concord/agreement") to ངོས་འཛིན་བྱེད་དོ — redundant emphasis on the pre-existing མཐའ་དག ("all") consensus, not a new claim. | YES | Minor addition — see flagged list. |

## §Flagged substitutions

For domain-expert accept/reject. None of these change a fact, add a new claim, drop content, or re-attribute a position — all are same-referent lexical, grammatical, or register choices.

1. **Para. 12** — before: "…ཉི་མ་སྦས་པའི་གསུང་ལ…" / after: "…སློབ་དཔོན་ཉི་མ་སྦས་པའི་གསུང་ལ…". Gemini prefixed the honorific title སློབ་དཔོན (ācārya/master) to the name "Nyima Bepa" (Sūryagupta), which the source does not use at this point. Standard honorific, no fact added, but technically new text — flag for accept/reject.
2. **Para. 11** — before: "…ཨུཏྤལ་འཛིན་པར་**གྲགས་སོ**།།" (renowned as holding…) / after: "…ཨུཏྤལ་འཛིན་པར་**བཞེད་དོ**།།" (Sangye Nyentrül & Palden Sherab **assert/hold** [this]…). Shifts from a passive "is renowned/reputed" (གྲགས) to an active doctrinal-assertion verb (བཞེད) explicitly tied to the two named authorities. Same referent and same two sources cited by the adjacent refs, but a subtly different epistemic framing — flag for review.
3. **Para. 5** — before: "…མཚན་གྱིས་གདགས་སོ།།" / after: "…**སྤྱིར**་...མཚན་དུ་གདགས་སོ།།". Adds "སྤྱིར" ("generally") before the naming clause — arguably implicit in the preceding "no single name is settled" sentence, but not present in the source's own wording. Flag for review.
4. **Para. 16** — before: "…མེ་ལོང་ནས་འཕྲོས་པའི…" / after: "…**ཕྱག་གི**་མེ་ལོང་ནས་འཕྲོས་པའི…". Adds "ཕྱག་གི" ("of the hand") specifying which mirror — consistent with the hand-held mirror already described in paragraph 11, so not a new fact, but an added qualifier not in this sentence's own source wording. Flag for review.
5. **Para. 26** — before: "…མཐའ་དག་གིས་ངོས་འཛིན་བྱེད་དོ།།" / after: "…མཐའ་དག་གིས་ངོས་འཛིན་**མཐུན་པར**་བྱེད་དོ།།". Adds "མཐུན་པར" ("in concord/agreement") — redundant with "མཐའ་དག" (all) which already conveys unanimity; flag for review as a minor emphasis addition.
6. **Para. 23** — before: "…བཤད་**ན**…" / after: "…བཤད་**ཀྱང**…". Conditional connective ("if/when [most] explain…") replaced with a concessive one ("although [most] explain…") ahead of naming Gendün Gyatso's dissenting view. Same contrastive logical structure preserved; flag as a minor grammatical-register note only.

## Ref attachment walk

Script C1 (token conservation) confirms all 45 `<ref>` occurrences survive character-for-character. This walk confirms each ref still supports the *same statement* as in the source (no ref migrated to a different clause).

| Ref name | Statement it supports — before | Statement it supports — after | Same? |
|---|---|---|---|
| taranatha | Opening ID sentence; body-color statement (§Body); secret-meaning statement (§Hidden meaning); tradition-list + conclusion (§Traditions, §Summary) | Same four attachment points, same clauses | YES |
| sungrab-tulku | Opening ID sentence | Same | YES |
| tenzin-dhonzang | Opening ID sentence; "Zhiwa Chenmo" naming; glud-practice statement + activity statement (§Activity, ×2); four-wisdoms statement (§Traditions) | Same six attachment points | YES |
| yama-sonam | Root verse quote; Gendün Drub-tradition identification; 3-face/12-hand quote + explanation (×2); "rab tu phye" critique/re-reading; conclusion (§Summary) | Same attachment points, same clauses | YES |
| dharmabhadra | "recognized as autumn-moon goddess" sentence | Same clause | YES |
| palden-sherab | Naming section (3 refs); body-form statement (§Body, ×2); dispelling-ignorance statement; secret-meaning statements (§Hidden meaning, ×3); four-knowledges statement; conclusion | Same attachment points throughout | YES |
| sangye-nyentrul | Naming section; body-form statement (§Body, ×2); dispelling-ignorance + wisdom-power statement (§Activity, ×2); four-knowledges statement | Same attachment points | YES |
| tsultrim-namdak | Naming section | Same | YES |
| gendun-drub | 3-face quote's ref; "rab tu phye" tradition list; conclusion | Same | YES |
| lobsang-dawa | Sub-commentary naming statement (§Names) | Same | YES |
| karma-maitri | Body-form statement (§Body) | Same | YES |
| pema-namgyal | Nectar-visualization siddhi statement (§Activity) | Same | YES |
| drakpa-gyaltsen | "rab tu phye" tradition list (§Traditions) | Same | YES |
| gendun-gyatso | "adorned by stars" statement (§Traditions) | Same | YES |

No ref was moved onto a different assertion; no ref was dropped or duplicated beyond its original occurrences.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator across all 26 compared units. Every verbatim verse/citation quotation (paragraphs 2, 7, 13) is character-for-character identical to the source. Every `<ref>` remains attached to the same statement it supported before. Six W1 warnings are all false positives from pre-existing quote-block paragraph structure, none introduced by the recomposition. Six lexical/register-level substitutions are recorded above in §Flagged substitutions for the domain expert's accept/reject — none constitutes factual drift under Rule 8.
