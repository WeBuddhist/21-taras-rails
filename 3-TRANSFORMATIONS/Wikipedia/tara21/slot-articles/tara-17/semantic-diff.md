---
topic: tara-17
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-17/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-17

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | This deity is the 17th prostration of the 21-praises; Ture = two feet strike ground fiercely; heart-HUM seed shakes the three worlds (Meru, Mandara, Vibhedaka) | Same, reworded/reordered | YES | verse quote character-for-character identical |
| 2 | Ture's word-meaning: "swift woman", explained via foot-stamping | Same | YES | quote "ཏུ་རེ་སྟེ་མྱུར་མའི་ཞབས་གཉིས་ནི་དྲག་ཏུ་བརྡབས་པས་སོ།" identical |
| 3 | Zurmang Khenpo Pema Namgyal: does not render as "swift", explains as displaying magical power instead; unattested elsewhere | Same | YES | |
| 4 | HUM seed explained as wrathful-deity nature (Dharmabhadra/Lobsang Dawa/Sungrab Tulku); Yama Sonam gives Nyima Bepa's alternate view (not wrathful nature, but cause of moving/subjugating Meru) and flags the conflict | Same | YES | "ཉི་མ་སྦས་པ" carries no honorific in either version |
| 5 | No single agreed name across commentaries for this Tara form | Same | YES | |
| 6 | Yama Sonam: "Sarva-sukha-sadhana"; Gendün Drub: "Tara who accomplishes happiness" (concordant); Yama Sonam also: "Bde ldan ma chom rkun bcing ba" | Same | YES | both named authorities and epithets unchanged |
| 7 | Palden Sherab: "Tara subduing the immeasurable, binder of enemy-bandits"; Sangye Nyentrul: abbreviated "subduing the immeasurable"; Tsultrim Namdak: same abbreviated name; all three concordant on that phrase | Same | YES | |
| 8 | Tenzin Dhonzang: "Tara who shakes the three worlds"; Sungrab Tulku: concordant epithet | Same | YES | |
| 9 | Konchok Thabkhe: no distinct name given, described functionally (protection from enemy-fear); Tenga Tulku: named functionally via wrathful activity, no actual name given | Same | YES | |
| 10 | Body color red-yellow/saffron, one face two arms, but major variance in hand-implements | Same | YES | |
| 11 | Yama Sonam: both hands hold moon-disc at heart, concordant with Nyima Bepa's verse per Yama Sonam himself; Sangye Nyentrul & Palden Sherab: right hand in boon-granting mudra, left holds stupa atop utpala | Same | YES | "atop utpala" spatial relation preserved, not flattened |
| 12 | Posture disagreement: Yama Sonam = bodhisattva cross-legged; Palden Sherab = "horse-mount" cross-legged; Sangye Nyentrul = half cross-legged; not settled as one | Same | YES | |
| 13 | Foot-stamping and light-rays from heart-HUM mostly explained as one and the same act (Tenga Tulku, Sangye Nyentrul); Yama Sonam identifies a conflict between two explanations: one holding light-rays cause the three-worlds shaking, Nyima Bepa holding the foot-stamping itself causes it | Same | YES | see Ref-attachment walk below — flagged lexical point |
| 14 | Commentaries disagree on "three worlds": some = netherworld/surface/above; Tenzin Dhonzang & Tenga Tulku = naga-world/human-world/deva-world (detailed); Yama Sonam rejects this, holds (from the tantra itself) the three worlds = Meru/Mandara/Vibhedaka; Drakpa Gyaltsen = desire/form/formless realms; Palden Sherab presents both without settling | Same | YES | |
| 15 | Mountain names: Meru & Mandara agreed; third name varies (Vibhedaka/Vibibhedaka spelling); some read as "snow mountain" or "Himalaya"; Taranatha: snow mountain where Maheshvara dwells; Tibetan texts mostly "Vibhedaka", Chinese sources "Kailasha" — Taranatha reconciles both as non-contradictory | Same | YES | |
| 16 | Taranatha & Palden Sherab both give a hidden-meaning (channel/wind/drop) reading, near word-for-word overlap; Taranatha's quote on Meru = Brahma's bone | Same | YES | quote "སྦས་དོན་ནི། རི་རབ་ནི་ཚངས་པའི་རུས་པ།" identical |
| 17 | Palden Sherab: Meru = central channel/spine; other two mountains = Yidzangma & Dungchenma (right/left channels); shaking = filled with bodhicitta; three worlds = 3 or 6 channels per both commentators, concordant | Same | YES | channel names unchanged |
| 18 | Palden Sherab also gives a 4th, "signless completion stage" reading beyond literal/generation/completion-with-signs: foot-stamping = guru-as-buddha devotion; HUM seed = self-arisen wisdom from guru's oral instruction; mountains/shaking = three-kaya essence dissolving in awareness — unattested in other commentaries (e.g. Taranatha) | Same | YES | list of 3 stages preserved (literal/generation/completion-with-signs), same 4th added on top |
| 19 | Tenzin Dhonzang: also gives detailed hidden meaning, differing from Taranatha/Palden Sherab's channel reading; HUM = bliss-wisdom arisen as Tara's form; explains via example-clear-light and 4th-stage wisdom, citing root tantra, Yeshe Gyaltsen, Chakrasamvara root tantra, Nama-sangiti, the inconceivable-secret sutra, and the omniscient scholar-siddha's works; unique to this commentary | Same | YES | all 6 cited items preserved, same order |
| 20 | Konchok Thabkhe: on practice — Panchen and a siddha both undertook this prostration as protection from robbers on the path | Same | YES | "ལག་ཏུ་བླངས་པར" → "ལག་ལེན་མཛད་པར" is a lexical swap only, see Flagged substitutions |
| 21 | Summary: this is the Tara form who stamps and shakes the three worlds via HUM; many differing views on her name, cause of the shaking, meaning of "three worlds", and hand-implements | Same | YES | |

## Ref attachment walk

Every `<ref name="...">` / self-closing `<ref name="..." />` token in the polished body sits on the same clause it supported before polishing. Walked all 69 ref tokens paragraph by paragraph (matching gemini-report.md's token count); no ref migrated to a different statement. Notable checks:
- `yama-sonam` in paragraph 1 (lead sentence) — still attached to the "17th prostration" + "Ture/HUM/three-worlds" description, same as before.
- `dharmabhadra` self-refs in §Ngestsig — still attached to the same two sentences (word-etymology and Ngülchu's own quote).
- `yama-sonam` / `dharmabhadra` at the end of §Chorten (Activity/Power section) — still attached to the "conflict between two explanations" sentence, same referent.
- `tenzin-dhonzang` (three uses in the Gzhung-lugs section) — still attached to the same three clauses (name, hidden-meaning explanation, and the closing "unique to this commentary" remark).
- `palden-sherab` in the Summary — still attached to the same "many differing views" statement, same as before.

No ref was found reattached to a different fact or a different commentator's position.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — do not block PASS:

| Location | Before | After |
|---|---|---|
| §Practice, Konchok Thabkhe paragraph | ལག་ཏུ་བླངས་པར་བཤད (took up in hand) | ལག་ལེན་མཛད་པར་བཤད (practiced) |
| §Activity/Power, first sentence | ཕལ་ཆེར་གཅིག་ཏུ་བཤད (explained as [mostly] one/the same) | ཕལ་ཆེར་གཅིག་མཐུན་དུ་བཤད (explained as mostly concordant) |
| §Activity/Power, Yama Sonam's conflict statement | གཉིས་འགལ་བར་བཀོད (posited the two as contradictory) | གཉིས་ནང་འགལ་དུ་བཀོད་དོ (posited the two as mutually/internally conflicting) |

None of these change which commentator holds which position, add/drop a claim, or alter a name.

## Reverted drift

Not a factual/semantic drift, but a mechanical formatting defect was found and corrected: the script's tail-reattachment step concatenated the frozen tail heading `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` directly onto the same line as the last body paragraph's closing `<ref>` tags, with no blank-line separator (the source had one). This breaks MediaWiki heading parsing and violates the "frozen tail byte-identical" requirement, though it is a whitespace-only defect — no wording, ref, or heading text was altered. Fixed by inserting the single blank line back between the last `བསྡུས་དོན།` paragraph and the tail heading, restoring byte-identical tail content confirmed against the pre-polish HEAD version of the file. No prose fact was touched by this fix.

## Verdict

PASS-after-reversion. No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator between body-before.txt and body-after.txt; every `<ref>` remains attached to the same statement it supported before; every verbatim quotation is character-for-character identical (re-confirmed by eye for all four "..." spans); no honorific was inserted before any personal name (walked every name, including ཉི་མ་སྦས་པ which the skill's known-drift pattern specifically warns about). The one issue found — a missing blank line before the frozen tail heading — was a mechanical formatting defect from the script's tail-reattachment, not a content change, and has been surgically corrected so the tail section is now byte-identical to the pre-polish source. Length delta: +3.62% tsheg-count (well within the ±25% W2 threshold); no W1/W2 warnings were raised by the script.
