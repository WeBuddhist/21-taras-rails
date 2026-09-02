---
topic: pacification
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/pacification/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — pacification

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | ཞི་བ is the 4th of the six perfections in Tara's sphere of activity per the root verse; other commentaries cite the same verse; commentaries as a group explain ཞི་བ via wisdom-paramita, power to pacify afflictions, peaceful/wrathful activity division, nirvana, and the deity of homage's name | Same, reworded/list-formatted | YES | dharmabhadra ref stays on the verse quotation; yama-sonam/palden-sherab/tenzin-dhonzang stay on "cited similarly elsewhere" |
| 2 | Most commentaries define ཞི་བ as the wisdom-paramita (taranatha, dharmabhadra, palden-sherab); reasons differ slightly: Dharmabhadra = pacifies delusion's darkness; Yama Sönam = root of attaining nirvana's peace | Same | YES | refs unchanged |
| 3 | Some commentaries explain from the fruit side: pacifies all causes (negative karma) and effects (suffering) of lower rebirth (gendun-gyatso, palden-sherab); Könchok Thabkhé: victorious activity over saṃsāra/nirvāṇa, also = nirvāṇa; Khenpo Tsultrim Namdak: shows the path of peace, ends in nirvāṇa | Same | YES | all three ref attachments unchanged |
| 4 | Other commentaries: pacification of afflictions by the three-place light rays, of rabies/poison by mantra, of thoughts by touch (karma-maitri, pema-namgyal, tsultrim-namdak); Palden Sherab: pacifies all inner/outer/secret obstacles; Lobsang Dawa + Tsultrim Namdak: pacifies harms to the three doors / illness, poverty, conflict via aspiration | Same | YES | ref list unchanged |
| 5 | The 21 homages divide into peaceful-mode and wrathful-mode groups (gendun-drub, karma-maitri, tenzin-dhonzang); Karma Maitri: evening=wrathful, dawn=peaceful recitation; Tenzin Dhönzang: 21 verses arise from peaceful + wrathful root mantras, matching the division | Same | YES | ref attachments unchanged |
| 6 | Tenga Tulku uniquely places "Tara of Pacification" among the four-activity Taras, with a verbatim quoted verse describing her attributes, found in no other of the 14 digested commentaries; Dharmabhadra: Tara's peaceful stance amid flames looks slightly wrathful, exemplifying both peaceful and wrathful marks | Same | YES | verbatim quote character-for-character identical (confirmed by script); both refs on same statements |
| 7 | Drakpa Gyaltsen: pacification of the eight afflictions generally, without specifying wisdom | Same | YES | ref unchanged |
| 8 | Gendun Drub: without saying "wisdom," explains pacification of all discordant factors (miserliness, laziness, ...) as **Tara's** sphere of activity | Same after reversion | YES (after fix) | **See Reverted drift below — Gemini's draft said "the lamp's" (སྒྲོན་མ) instead of "Tara's" (སྒྲོལ་མ)** |
| 9 | Gendun Gyatso: equivalently, Tara pacifying afflictions | Same | YES | ref unchanged |
| 10 | Könchok Thabkhé: distinct division — pairs asceticism + pacification as "morality" alone; identifies Tara herself as the wisdom-paramita, sees 5 (not 6) perfections as her sphere, disagreeing with other commentaries on the count | Same | YES | ref unchanged |
| 11 | Tenga Tulku: also treats pacification as covering all six perfections without fault, rather than one alone — a reading not found in the other digested commentaries | Same | YES | ref unchanged |
| 12 | Könchok Thabkhé: notes some earlier, unnamed commentators disagree on applying "pacification"/"sphere of activity" to the wisdom-paramita; he himself, per Siddha Nyima Sewa, holds it completes all five perfections | Same | YES | ref unchanged |
| 13 | Yama Sönam: many commentaries gloss his source's "austerity" as morality pacifying afflictions; on "pacification" some link it to the wisdom-paramita, others to the tenth paramita's opposite pacified — a disagreement whose sourcing isn't clear | Same | YES | ref unchanged |
| 14 | Khenchen Palden Sherab, Sangye Nyentrul, and Sertreng Geshe Tenzin Dhönzang all name one homage in the 21 "pacification," but number it differently: 15th (Palden Sherab), 16th (Sangye Nyentrul); Tenzin Dhönzang uses the label twice, at 15th and 2nd; Gendun Drub separately calls one "Tara of virtuous pacification" | Same | YES | numbers 15/16/2 unchanged; all refs on same statements |
| 15 | Palden Sherab alone also reads pacification through completion-stage hidden meaning: at homage 14, tummo fire melts bodhicitta, pacifying the fire's burning; at homage 21, pacification = the clear-light of empty ground-attainment like an autumn sky, and self-liberation of the two obscurations' confused appearance — a reading not found elsewhere | Same | YES | ref unchanged |
| 16 | Könchok Thabkhé and Palden Sherab: per the Abhisamayālaṃkāra's 27 activities, the first is "pacification," placed as Tara's sphere of activity | Same | YES | both refs unchanged |
| 17 (summary) | Pacification arises in the root verse as one of the six perfections in Tara's sphere; most commentaries read it as the wisdom-paramita, but also explained via the fruit of pacifying afflictions, the peaceful/wrathful division, names of specific homages, the completion-stage hidden meaning, and nirvāṇa; commentaries diverge substantially on the division itself | Byte-for-byte identical to source (untouched by Gemini) | YES | all three refs unchanged |

## Ref attachment walk

Every `<ref>` token was checked against the clause immediately preceding it in both `body-before.txt` and `body-after.txt`. All 45 ref instances (across the reused named refs) remain attached to the same statement they supported before polishing — no ref migrated to a different clause or was re-attributed to a different commentator's position. Confirmed programmatically: the sequence of ref names extracted from before and after texts is identical, in identical order, with identical surrounding sentence content.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — accepted, verdict unaffected:

| Before | After | Where |
|---|---|---|
| མྱང་འདས་ (nirvāṇa, contracted spelling) | མྱ་ངན་ལས་འདས་པ (nirvāṇa, full spelling) | paragraphs 1, 2, 3, 17 — spelling normalization only, same referent |
| མྱང་འདས་སུ་འགོད་པར | མྱ་ངན་ལས་འདས་པའི་གོ་འཕང་ལ་འགོད་པར | paragraph 3 (Tsultrim Namdak) — "placed into nirvāṇa" vs "placed at the level/state of nirvāṇa," same claim |
| ཞི་བ་ལ་ཕྱག་འཚལ་བའི་འབྲས་བུའི་ཆ་ནས | ཞི་བ་ཞེས་པ་ཕྱག་འཚལ་བའི་འབྲས་བུའི་ཆ་ནས | paragraph 3 — grammar-particle rephrasing, same claim |
| སྒྲོལ་མ་ཉོན་མོངས་པ་ཞི་བར་མཛད་པ (Gendun Gyatso, unmarked subject) | སྒྲོལ་མས་ཉོན་མོངས་པ་ཞི་བར་མཛད་པ (agentive case marker added) | paragraph 7 — grammar only, same subject (Tara) and same claim |
| various ཏེ/ཅིང/ཞིང connective particles and sentence-final དོ/ནོ | swapped among each other | throughout | pure discourse-connective variation, no semantic change |

## Reverted drift

**Found:** In the Gendun Drub sentence (paragraph 7 / "གཞུང་ལུགས་སོ་སོའི་བཤད་པ", second sentence), the source (`body-before.txt`) reads:

> ...མི་མཐུན་ཕྱོགས་ཐམས་ཅད་ཞི་བ་ཉིད་**སྒྲོན་མའི**་སྤྱོད་ཡུལ་དུ་བཤད།

Gemini's draft (`body-after.txt`) silently changed this to:

> ...མི་མཐུན་པའི་ཕྱོགས་ཐམས་ཅད་ཞི་བ་ཉིད་**སྒྲོལ་མའི**་སྤྱོད་ཡུལ་དུ་བཤད་དོ།

This is a one-syllable near-homograph swap (སྒྲོན་མ "lamp" → སྒྲོལ་མ "Tara") — drift pattern (f) in the task instructions. Even though སྒྲོལ་མ is almost certainly the intended reading given the parallel phrase "སྒྲོལ་མའི་སྤྱོད་ཡུལ" recurs elsewhere in this same article and སྒྲོན་མ ("lamp") makes no sense as the referent of "sphere of activity" here, this skill's contract is to freeze the source's exact wording — including any pre-existing typo in the source article — rather than let the model silently "correct" it. Per Rule 8(a), applied surgical reversion: restored just this word in `article.md` (line 36) to the source's exact wording `སྒྲོན་མའི`, leaving the rest of Gemini's rewording of that sentence (grammar particles, sentence-final དོ) untouched. `body-after.txt` was left as the unmodified raw model record per Rule 8(a).

## Verdict

**PASS-after-reversion.** One factual/referential drift was found (a one-letter near-homograph swap changing "lamp's sphere of activity" to "Tara's sphere of activity" in the Gendun Drub attribution) and was surgically reverted in `article.md` to match the source's exact wording. No other fact was added, dropped, weakened, strengthened, or re-attributed; every `<ref>` remains attached to the same statement it supported before polishing; all verbatim quotations (including the Tenga Tulku block quote) are character-for-character identical to the source, confirmed programmatically. The remaining changes are pure prose recomposition — word order, clause structure, connective particles, list formatting, and a few lexical spelling normalizations (all logged above as flagged substitutions) — with no effect on content.
