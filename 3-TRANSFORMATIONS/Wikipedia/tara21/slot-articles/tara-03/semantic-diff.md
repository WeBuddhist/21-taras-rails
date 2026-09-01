---
topic: tara-03
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-03/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-03

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | This deity is the 3rd homage-verse of the 21 praises (3 refs). | Same, word order reversed ("...is that 3rd homage-verse..."). | YES | reorder only |
| 2 | Root-verse quotation (4 lines, ref yama-sonam). | Identical quotation. | YES | verbatim, unchanged char-for-char |
| 3 | Per the verse: lotus-adorned, sphere of the 6 pāramitās (generosity...meditation), refs dharmabhadra/palden-sherab. | Same 6 items, same order, list punctuation only. | YES | — |
| 4 | Tenzin Dhonzang: etymology of "phyag 'tshal" — phyag = clearing obstacles; 'tshal = gathering favorable conditions. Most other commentaries: mere respectful bowing. | Same two positions, same attributions, refs unchanged. | YES | — |
| 5 | Commentaries disagree on "gser sngo" spelling (g-prefix or not); listed refs on each side. Konchok Thabkhe: certain of "gser" (gold), uncertain of prefix, relies on Jowo Chenpo/Drubchen's wording "gser mdog can gyi sgrol ma". | Same disagreement, same ref groups, same Konchok Thabkhe position. | YES | — |
| 6 | Gendun Drub: "sngo ba" = body color, "ser ni" = clear hue; hence also known "gser mdog can gyi sgrol ma" (ref gendun-drub). Tenzin Dhonzang's text also glosses this name (ref tenzin-dhonzang). | Same quotes, same attributions, same refs. | YES | verbatim quotes unchanged |
| 7 | Body: gold-yellow tinged slightly blue (3 refs). Hand implement (phyag gi mtshon cha): water-born lotus/blue utpala (3 refs). Ten [petals]: held in left hand (3 refs); five [petals]: open toward the ear (2 refs). | Same facts, same ref groups; "phyag gi mtshon cha" → "phyag mtshan" (synonym, flagged below); numbers "ten"/"five" preserved. | YES | 1 flagged substitution (see below) |
| 8 | Yama Sonam's commentary: elaborated form — 1 face, 10 arms, seated **atop a multicolored lotus which is atop a sun-disc seat** (explicit two-tier stacking), 5 right hands hold rosary/sword/arrow/vajra/hook, 5 left hold streamer/noose/lotus/bell/bow, vajra posture. Cites a verse of Nyima Sangwa. | Same enumeration, but stacking order was flattened to "seated upon lotus and sun-disc seat" (no longer specifies which is on top). **Reverted** — see below. | YES (after reversion) | ⚑ drift found and reverted, see "Reverted drift" |
| 9 | Nyima Sangwa verse quotation (4 lines). | Identical. | YES | verbatim, unchanged |
| 10 | Other commentaries cite no scripture for face/hand count here; this expanded body-form is unique to this one commentary. | Same claim, same exclusivity ("only this commentary"). | YES | — |
| 11 | Heading "Activity and power": deity arises from/is nature of the 6 pāramitās (3 refs); Taranatha explains in detail how mastery of the 6 pāramitās becomes her sphere. | Unchanged (punctuation only). | YES | — |
| 12 | "dka' thub" glossed as morality (3 refs); glossed as "hard to keep but able to keep" — also called dka' thub. Drakpa Gyaltsen: dka' thub = the eight moral precepts, summarized. | Unchanged content and ref. | YES | — |
| 13 | Sungrab Tulku & Tenga Tulku: 6 pāramitās paired 1:1 against 6 afflictions (generosity↔stinginess, diligence↔laziness, morality↔misconduct, wisdom↔delusion, patience↔anger, meditation↔distraction), agreed by both. | Same 6 pairs, same order, same ref (sungrab-tulku). | YES | — |
| 14 | Konchok Thabkhe: his ordering of the 6 pāramitās differs slightly from the well-known order; first 3 belong to merit-accumulation, last to wisdom-accumulation; diligence belongs to both, so placing it earlier is faultless. | Same claim; the doubled "brtson 'grus" (diligence) mention compressed to one, referent unchanged. | YES | redundancy removed, no fact lost |
| 15 | 3 commentaries explain the secret meaning differently, without contradicting each other, each in its own manner of elaboration. | Same claim; "sgro btab pa" → "sgro btags pa" spelling variant. | YES | 1 flagged substitution |
| 16 | Khenchen Palden Sherab: 4-stage explanation — literal meaning; generation-stage visualization as Serve Sönam-chok-ter; completion-stage-with-signs union of lotus/vajra applying the 6 pāramitās; signless ultimate meaning (6 pāramitās dissolve into self-arisen wisdom, become Samantabhadrī); cites Brahmaviśeṣacintā-paripṛcchā-sūtra on the non-observable ultimate nature of the 6 pāramitās. | Unchanged content, same 4 stages, same sūtra citation, same ref throughout. | YES | — |
| 17 | Taranatha: secret meaning via union of lotus/vajra — austerity's morality, meditation's bliss, wisdom realizing emptiness, diligence, patience, generosity — concludes tantric conduct. | Same 6 items, same order, same ref. | YES | — |
| 18 | Sangye Nyentrul Rinpoche: generation-stage visualization (wish-fulfilling jewel on utpala, granting all wishes, light pervading space) — terminologically consonant with Khenchen Palden Sherab's generation-stage but phrased independently. | Unchanged. | YES | — |
| 19 | Numbering: many commentaries count this verse as the 21-praises' "3rd"; 4 commentaries (by body-color/hand-attribute/cause) count it "2nd" within a sub-scheme; no commentary states which numbering is correct. | Same claim, same ref groups; "grangs pa" → "bgrangs pa" spelling variant. | YES | 1 flagged substitution |
| 20 | Body-color divergence: Konchok Thabkhe/Palden Sherab/Sangye Nyentrul — body gold only, flower blue; Taranatha's headnote/word-commentary — gold/blue both describe the flower's stem/petals, no body-color distinction; Tsultrim Namdak — green (blue+yellow mixed); Gendun Gyatso — slightly reddish; Tenzin Dhonzang — slightly blue-green. | Same 6 positions, same attributions (all bold names byte-identical, no honorific inserted), same refs. | YES | checked for honorific-insertion drift — none found |
| 21 | "zhi ba" divergence: most — wisdom, or wisdom's pacifying action (3 refs); Drakpa Gyaltsen/Gendun Gyatso — pacifying afflictions generally; Gendun Drub — pacifying the 6 specific opposites (stinginess/laziness/misconduct/anger/distraction/wrong-view); Tenga Tulku — "meditation's object" = wisdom, "zhi ba" = undefiled by the 6 corresponding faults; Konchok Thabkhe — earlier commentaries apply zhi ba/spyod yul to the wisdom-pāramitā specifically; Yama Sonam — notes the same internal split. | Same 6 positions, same attributions (all bold names unchanged), same refs; "'grel bas" → "'grel pas" spelling variant. | YES | 1 flagged substitution |
| 22 | Alternate 6-pāramitā substitution: Gendun Gyatso — "or": abandoning affliction/patience/meditation/wisdom-of-suchness (4 items) fulfill the 6; Konchok Thabkhe — deity herself = wisdom-pāramitā, other 5 = her sphere/basis; Tsultrim Namdak — elsewhere explains a metrically-matching line via the 37 bodhipakṣa-dharmas, showing 2 systems even within his own text. | Same content, same 3 attributions, same refs; "ngos 'dzin te" → "ngos bzung ste" synonym, "'am" → "lam" particle variant. | YES | 2 flagged substitutions |
| 23 | Summary: all commentaries agree lotus-adorned/6-pāramitā deity, but diverge on gser/sngo spelling, gser-sngo referring to body or flower, and "zhi ba" as wisdom vs. pacifying action — "very clear" that interpretations vary. | Same summary, same refs; "nyin gsal" → "shin tu gsal" idiom swap (both = "very clear"). | YES | 1 flagged substitution (idiom, matches Rule 8's known example) |

## Ref attachment walk

Every `<ref>` token was checked against the statement it sits on before vs. after. In every paragraph reviewed above, each ref remained attached to the same claim/attribution it supported in the source — no ref migrated to a different clause or a different commentator's position.

- yama-sonam, gendun-gyatso, taranatha (¶1) — same opening attribution — YES
- dharmabhadra, palden-sherab (¶3, ¶20 body-color, ¶23 summary) — same claims each time — YES
- tenzin-dhonzang (¶4, ¶6, ¶20) — same etymology / naming / body-color claims — YES
- sungrab-tulku (¶4, ¶13) — same "mere bowing" gloss and pāramitā-affliction pairing — YES
- dharmabhadra/palden-sherab/sungrab-tulku vs. yama-sonam/tenzin-dhonzang/tsultrim-namdak (¶5 g-prefix split) — same two groups — YES
- gendun-drub (¶6, ¶7, ¶21, ¶23) — same naming, ten-petal, "zhi ba" and summary claims — YES
- yama-sonam/dharmabhadra/karma-maitri (¶7 body color) — YES
- yama-sonam/dharmabhadra/drakpa-gyaltsen (¶7 hand implement) — YES
- gendun-drub/lobsang-dawa/palden-sherab (¶7 ten-petal) — YES
- tenga-tulku/sungrab-tulku (¶7 five-petal, ¶13, ¶21, ¶23) — YES
- yama-sonam (¶8–10 elaborated form and verse) — YES
- drakpa-gyaltsen (¶12, ¶20, ¶21) — same 8-precepts, body-color, "zhi ba" claims — YES
- konchok-thabkhe (¶5, ¶14, ¶19, ¶20, ¶21, ¶22, ¶23) — each instance still attached to its distinct Konchok Thabkhe claim — YES
- palden-sherab (¶16, ¶19, ¶20, ¶21, ¶23) — each attached to its distinct claim (4-stage explanation vs. numbering vs. body-color vs. "zhi ba") — YES
- taranatha (¶11, ¶17, ¶19, ¶20, ¶23) — same claims — YES
- sangye-nyentrul (¶18, ¶20) — YES
- tsultrim-namdak (¶20, ¶22) — YES
- gendun-gyatso (¶20, ¶21, ¶22) — YES
- tenzin-dhonzang (¶4, ¶6, ¶20) — YES

## Flagged substitutions

Lexical-only swaps — same referent/meaning, do not block PASS:

| Location | Before | After | Type |
|---|---|---|---|
| ¶1 | ནང་གསུམ་པའི་མཆོད་བརྗོད་ཡིན། | ནང་གི་མཆོད་བརྗོད་གསུམ་པ་དེ་ཡིན། | word-order reshuffle |
| ¶7 | ཕྱག་གི་མཚོན་ཆ (hand implement) | ཕྱག་མཚན (hand-attribute) | synonym |
| ¶9 / ¶21 | འགྲེལ་བ (commentary, ba-spelling) | འགྲེལ་པ (commentary, pa-spelling) | orthographic variant, both attested |
| ¶15 | སྒྲོ་བཏབ་པ | སྒྲོ་བཏགས་པ | orthographic variant |
| ¶16 | མི་དམིགས་པར་...དྲངས་སོ | མི་དམིགས་པའི་...དྲངས་སོ | grammar-particle change |
| ¶19 | གྲངས་པ | བགྲངས་པ | orthographic variant (with/without འ-prefix) |
| ¶22 | ངོས་འཛིན་ཏེ | ངོས་བཟུང་སྟེ | synonym ("identify/recognize") |
| ¶22 | ...འམ་བརྟེན་གནས་སུ | ...ལམ་བརྟེན་གནས་སུ | disjunctive-particle variant ("or") |
| ¶23 | ཉིན་གསལ་ལོ | ཤིན་ཏུ་གསལ་ལོ | idiom swap, both = "very clear" (the known false-positive pattern named in the skill's Rule 8 example) |

No honorific-title insertion before any personal name was found anywhere in the article — every bold `author_in_use` name and every inline mention of a commentator's name was walked and matches the source byte-for-byte (དཀོན་མཆོག་ཐབས་མཁས་, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་, སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ་, ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ, མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག་, རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ, རྒྱལ་བ་དགེ་འདུན་གྲུབ་, སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་, རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན་, རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ་, རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་, ཏཱ་ར་ནཱ་ཐ, ཇོ་བོ་ཆེན་པོ, གྲུབ་ཆེན, ཀརྨ་མཻ་ཏྲི, དངུལ་ཆུ་དྷརྨ་བྷ་དྲ, འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ).

## Reverted drift

**¶8/9 — throne-construction detail (surgical reversion applied, Rule 8a).**

- Source (Yama Sonam's commentary, elaborated body-form): `ཞལ་གཅིག་ཕྱག་བཅུ་མའི་ཚུལ་གྱིས་ཉི་མའི་གདན་གྱི་སྟེང་གི་སྣ་ཚོགས་པད་མའི་སྟེང་དུ་བཞུགས་ཤིང` — an explicit two-tier stack: the deity sits atop a multicolored lotus, which itself sits atop a sun-disc seat.
- Gemini's rewrite: `ཞལ་གཅིག་ཕྱག་བཅུ་མའི་ཚུལ་གྱིས་སྣ་ཚོགས་པདྨ་དང་ཉི་མའི་གདན་ལ་བཞུགས་ཤིང་` — flattened to "seated upon [a] multicolored lotus and sun-disc seat," losing the specific stacking order (which element is beneath which) that the commentary states.
- This is a dropped iconographic detail, not a paraphrase of the same fact, so it counts as factual drift under Rule 1/Rule 8.
- Remedy applied: surgical reversion (Rule 8a) — restored the source's exact clause verbatim in `article.md`, keeping the rest of the recomposed sentence (which was otherwise unaffected) intact:
  `ཞལ་གཅིག་ཕྱག་བཅུ་མའི་ཚུལ་གྱིས་ཉི་མའི་གདན་གྱི་སྟེང་གི་སྣ་ཚོགས་པད་མའི་སྟེང་དུ་བཞུགས་ཤིང་།`
- `body-after.txt` is left untouched as the raw model record (per Rule 8a); only `article.md` was corrected.

No other factual drift was found. No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator anywhere else in the article; no verbatim quotation was altered; no ref migrated to a different statement.

## W1 warnings (paragraph-final punctuation)

`gemini-report.md` flagged 4 paragraphs as not ending in the paragraph-final double shad `།།`. All 4 are false positives of the same two known patterns:

- Paragraph 1 ends `...པ་དེ་ཡིན། རྩ་ཚིག་ལས།` and paragraph 8 (¶8/9 in the table above) ends `...ལུང་དུ་དྲངས་ཏེ།` — both are the lead-in clause to a verbatim verse quotation ("...as follows:" / "...cites a verse, saying:"), ending in `ལས།`/`ཏེ།` rather than `།།`, because the sentence continues into the quoted block that follows. This matches the documented false-positive pattern for sentences ending in `ལས།`/`ཏེ།` before a quote.
- Paragraph 2 ends `...སྤྱོད་ཡུལ་ཉིད་མ།"` and paragraph 9 ends `...བཅུའོ། ། ཞེས་གསུངས།"` — both are the closing of a verbatim verse-quotation block (quotation marks after the verse's own internal shad), which is exempt from the prose paragraph-final-shad rule.

No re-run was needed; all 4 are accounted for.

## Verdict

**PASS-after-reversion.** One factual drift was found (the throne-stacking detail in ¶8/9, a dropped "lotus-on-top-of-sun-disc" spatial relation) and was surgically reverted in `article.md` to the source's exact wording. Every other change across the ~2,200-tsheg body is either (a) a pure restyling — punctuation-contract compliance (sentence/paragraph-final shad, list-splitting with shad instead of repeated "dang"), redundancy removal, or word-order/clause-structure improvement — with no change to content, or (b) a flagged lexical/orthographic substitution recorded above, none of which alters meaning, referent, or attribution. All refs remain attached to the same statements they supported in the source. All verbatim quotations are character-for-character identical. No honorific was inserted before any personal name. Length delta: −2.43% by tsheg count (2218 → 2164), consistent with the redundancy removed in ¶14 and the more economical phrasing elsewhere.
