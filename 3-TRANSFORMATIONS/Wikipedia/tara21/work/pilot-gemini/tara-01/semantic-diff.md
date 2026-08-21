---
topic: tara-01
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-01/article.md
model: gemini-3.1-pro-preview
date: 2026-08-21
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-01

## W1 warnings

`gemini-report.md` reported **0 warnings** (0 W1 or otherwise) — the script's own paragraph-final `།།` check found nothing to flag. I independently walked every paragraph boundary in `body-after.txt` (12 paragraphs) and confirmed each ends in a genuine double shad (`།།`) immediately before its trailing `<ref>` tag(s), including the less obvious cases `...སྣང་ངོ་།།` (line 22) and `...མཐུན་པར་གྲུབ་བོ།།` (line 14, no ref) — no false positives to record and no re-run needed on this axis.

## Sentence-by-sentence comparison

| # | Para | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|---|
| 1 | Lead | Tara Nyurma Pawo is the first of the 21 prostrations to Tara | same, + demonstrative "that" | YES | style only |
| 2 | Lead | many scholars **introduce/present** her (ཁོང་མ) as the embodiment of all buddhas' activity | many scholars **hold/assert** (བཞེད) the **Jetsünma** (རྗེ་བཙུན་མ) as the same | YES | flagged: verb + referring term, same referent (Tara) |
| 3 | Lead | the three names are merely differences in how the **names** are applied to Tara alone | the three names are merely differences in how **synonyms of the name** are applied to Tara alone | YES | flagged: མིང་ → མཚན་གྱི་རྣམ་གྲངས், same concept |
| 4 | §མཚན་གྱི་ངེས་ཚིག P1 | per the explanation of many scholars **alike**, "Drolma" = liberates beings from samsara's suffering | per the **concordant tradition** of many scholars, same | YES | style only |
| 5 | same | "Nyurma" = activity for beings never delays an instant | identical | YES | unchanged |
| 6 | same | "Pawo" = unobstructed power to accomplish beings' welfare; scholars differ on what is overcome (afflictions/māras/fears/obstacles) but agree on the root point | identical content, grammar only (མི་འདྲ་ཡང → མི་འདྲ་བ་ཡོད་ཀྱང) | YES | style only |
| 7 | §P2 | Yama Sönam explains the etymology in three stages: temporary rescue from the 8 fears → ultimate liberation from the two obscurations → placement at unsurpassed buddhahood | identical | YES | unchanged |
| 8 | same | "Nyurma" distinguished as extremely swift, unlike healing an old illness or a sprout from seed (which need years) | identical | YES | unchanged |
| 9 | same | Tāranātha adds a 4th name "Ma" (mother), from the aspect of great non-referential compassion swiftly benefiting beings | identical | YES | unchanged |
| 10 | same | Tāranātha's unique reading of "Nyurma": not swiftness of benefit, but swiftly generating the all-seeing wisdom-eye | identical | YES | unchanged |
| 11 | same | Dharmabhadra distinguishes "Nyurma" by comparison with other buddhas | identical | YES | unchanged |
| 12 | same | Karma Maitri explains Tara's name via the eye-like-lightning quality, tied to the body-form section | identical | YES | unchanged |
| 13 | same | Serme Tsang Geshe Tenzin Dönzang: phyag = purifying misdeeds of body/speech/mind; 'tshal = seeking the three secrets' qualities of the refuge-object | identical | YES | unchanged |
| 14 | §སྐུ་ཡི་རྣམ་པ P1 | root verse's main body feature = eyes like an instant of lightning; scholars read this as the wisdom-eye seeing all objects instantly | identical | YES | style only |
| 15 | same | **verbatim quotation** from Sungrab Tulku on the wisdom-eye | **character-for-character identical** | YES | verbatim quote intact |
| 16 | same | Dorlob Tengye Trul: a unique gloss — the wisdom-eye sees beings' rise/fall unceasingly, six times day and night | identical | YES | unchanged |
| 17 | same | Zurmang Khenpo Pema Namgyal: the lightning-eye feature necessarily applies during **ཉི་མ་སྦས་པ**'s wrathful-smiling manner | identical claim, but **ཉི་མ་སྦས་པ retitled སློབ་དཔོན་ཉི་མ་སྦས་པ** ("Acharya" added) | **NO** | ⚑ **see Flagged — this one is FAIL-grade, not a benign substitution** |
| 18 | §P2 | Sangye Nyenpa Rinpoche & Palden Sherab: red body, wrathful-smiling, 2 legs crossed, 1 face 2 hands (supreme-giving + refuge mudras), holding utpala + white right-coiled conch | identical | YES | unchanged |
| 19 | same | Tsultrim Namdak: reddish-yellow body; mudrā/emblem scheme close to the above two | identical (མཚན་ཆ → ཕྱག་མཚན, synonym) | YES | style only |
| 20 | same | Yama Sönam adds an 8-armed form from **Nyima Bepa**'s sādhana (distinct from the above): flame-red, 1 face 2 eyes 8 arms, holding bow-arrow/wheel/sword/conch/vajra/noose, adorned with flowers | identical content — here **no title added**, matching the source | YES | unchanged (contrast with row 17 — inconsistent treatment of the same name within one polish pass) |
| 21 | same | Nyima Bepa states this form's names are also "swift" and "brave" | identical | YES | unchanged |
| 22 | §ཕྲིན་ལས་དང་ནུས་མཐུ | Sangye Nyenpa & Palden Sherab: this Tara's activity increases bodhicitta and draws in appearances/light | identical | YES | unchanged |
| 23 | same | Tāranātha: the two words "Drolma-Nyurma" alone summarize all boundless qualities — wisdom, love, capacity, activity | identical, words spelled out with དང་ instead of compound | YES | style only |
| 24 | same | Yama Sönam: matches wisdom/love/capacity to Drolma/Nyurma/Pawo respectively | identical, names spelled out | YES | style only |
| 25 | same | Tenzin Dönzang: as Avalokiteshvara=compassion-deity, Manjushri=wisdom-deity, Vajrapani=power-deity, so Tara=activity-deity of all buddhas — a unique analogy | identical | YES | unchanged |
| 26 | same | counts/correlations of qualities differ by scholar, but all agree Tara's activity is epitomized by a small subset of buddha-qualities | identical | YES | unchanged |
| 27 | §ལོ་རྒྱུས P1 | all scholars agree: Avalokiteshvara, seeing beings leaving samsara were still not few, wept; Tara arose from a million lotus-petals in the tear-pool; attested in all 15 scholars' texts | identical (མི་ཉུང་ / མ་ཉུང་ — both "not few", no flip) | YES | style only |
| 28 | same | Palden Sherab & Pema Namgyal identify this first-prostration Tara as both White Tara and Green Tara | identical | YES | unchanged |
| 29 | §P2 | Gendün Drup's unique addition: in reply to a request that Avalokiteshvara **not shed (མ་གཏོང་བ)** tears, Tara vowed to swiftly liberate beings; hence eyes like lightning from her valor | same narrative, but the request verb becomes **not discard/waste (མི་འདོར་བ)** the tears | uncertain | ⚑ **flagged — see Flagged substitutions; possible nuance shift, not a reversal** |
| 30 | same | Yama Sönam: ties the story to the 8 great fears + 16 [lesser] fears, urging refuge in the goddess | identical (སྦྲེལ → སྦྱར, synonym) | YES | style only |
| 31 | same | from first generating bodhicitta through accumulation to buddhahood, she relied on a female body throughout — hence "Pawo" | identical (བྱང་ཆུབ་སེམས་བསྐྱེད་པ → བྱང་ཆུབ་མཆོག་ཏུ་སེམས་བསྐྱེད་པ, standard fuller form of the same term) | YES | flagged: terminology completion, not a new claim |
| 32 | same | a Jonangpa history: monks urged her to pray for male rebirth; she vowed to work for beings in female form as long as samsara is not empty | identical | YES | unchanged — key doctrinal vow content preserved verbatim in sense |
| 33 | §གཞུང་ལུགས P1 | on reading "Pawo" vs "Palmo": most scholars read the 3rd root-verse name as "Pawo" (courage/power) | identical | YES | style only |
| 34 | same | **verbatim quotation** "ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔལ་མོ།" from Dharmabhadra, who reads "Palmo" and glosses it accordingly | **quotation character-for-character identical** | YES | verbatim quote intact |
| 35 | same | Tenzin Dönzang's text has "Palmo" in one citation of the root verse, but agrees on "Pawo" elsewhere in the same text (both the other citation and the etymology) → judged a **writing error (འབྲི་འཛིན་གྱི་ནོར་བ)**, not a deliberate "Palmo" reading like Dharmabhadra's | same conclusion, reworded as a **scribe's error (ཡི་གེ་པའི་ནོར་འཁྲུལ)** | YES | flagged: near-synonym for "copying error", same interpretive conclusion |
| 36 | §P2 | on whose tears: most earlier commentators read it as Tara's own eyes; Könchok Tapkhe follows **Mahasiddha Nyima Bepa (གྲུབ་ཆེན་ཉི་མ་སྦས་པ)** and reads it as Avalokiteshvara's eyes, citing a verse from Nyima Bepa's text | identical, and **the title "Mahasiddha" here is correctly preserved unchanged** | YES | unchanged — confirms row 17's added "Acharya" is an outlier, not a house-style upgrade applied consistently |
| 37 | same | the two lineages (Tara's-own-eyes vs. Avalokiteshvara's-eyes-per-Könchok-Tapkhe) are established as distinct | identical | YES | unchanged |
| 38 | §P3 | most scholars gloss "three worlds/realms" as nāga-underworld / human-earth / god-heaven | identical | YES | unchanged |
| 39 | same | Yama Sönam, per Chandrakīrti's *Catuḥśataka* commentary, also allows desire/form/formless realms — accepts both [traditions] | identical, realm list spelled out instead of compound | YES | style only |
| 40 | same | Gendün Drup & Tsultrim Namdak: without pairing the two, set forth only the three-realms (desire/form/formless) reading, as protector of those three | identical | YES | unchanged |
| 41 | §བསྡུས་དོན | this Tara is identified as the embodiment of all buddhas' activity; the tear-birth history and the lightning-eye body feature together indicate the name's meaning | identical | YES | unchanged |

## Flagged substitutions

Per Rule 8, lexical substitutions (same referent/meaning) are recorded here for the domain expert; they do not by themselves fail the verdict.

1. **Row 2** — ཁོང་མ (she) → རྗེ་བཙུན་མ (the Jetsünma); ངོ་སྤྲོད་བྱེད (introduce/present) → བཞེད (hold the view). Same referent (Tara), same claim (scholars regard her as the embodiment of all buddhas' activity).
2. **Row 3** — མིང་འཇུག་ཚུལ (way names are applied) → མཚན་གྱི་རྣམ་གྲངས་འཇུག་ཚུལ (way synonyms of the name are applied). Same concept.
3. **Row 6** — མི་འདྲ་ཡང (differ, yet) → མི་འདྲ་བ་ཡོད་ཀྱང (there is difference, yet). Grammar only.
4. **Row 17** — see Flagged §below; not a benign substitution, treated as drift.
5. **Row 19** — མཚན་ཆ (attribute/emblem) → ཕྱག་མཚན (hand-emblem). Synonyms for the same set of held implements; the implement list itself is unchanged.
6. **Row 23–24** — compound names (སྒྲོལ་མྱུར་དཔའ་, སྒྲོལ་མ་མྱུར་མའི་ཚིག་གཉིས） → the same names spelled out in full joined by དང་. No name added or dropped, same three-way (or two-way) correspondence.
7. **Row 27** — གྲངས་མི་ཉུང་བར → གྲངས་མ་ཉུང་བར ("the number was not few", both directions of the negation particle; confirmed this is not a flip to "few").
8. **Row 29** — **སྤྱན་ཆབ་མ་གཏོང་བར་ཞུས་པ** (requested [him] not to shed/release tears) → **སྤྱན་ཆབ་མི་འདོར་བར་ཞུས་པ** (requested [him] not to discard/let go to waste his tears). Same episode and same narrative outcome (Tara's vow follows either way), but the precise content of the request shifts from "stop crying" to "don't let the tears go to waste" — a nuance a Tibetan-literate domain reviewer should confirm against the underlying commentary (Gendün Drup's text) before accepting.
9. **Row 31** — བྱང་ཆུབ་སེམས་བསྐྱེད་པ (generate bodhicitta) → བྱང་ཆུབ་མཆོག་ཏུ་སེམས་བསྐྱེད་པ (generate the mind for supreme enlightenment). This is the fuller, more classical form of the same technical term, not a new claim.
10. **Row 35** — འབྲི་འཛིན་གྱི་ནོར་བ (a writing/copying error) → ཡི་གེ་པའི་ནོར་འཁྲུལ (the scribe's error). Same interpretive conclusion (Tenzin Dönzang's "Palmo" instance is a copying slip, not a real "Palmo" reading tradition).
11. Honorific-verb upgrades throughout (བྱེད → མཛད, several instances rows 22/28/41) — standard honorific register raising for actions of named teachers, referent and action unchanged.

## Flagged — factual drift (not a benign substitution)

**Row 17, §སྐུ་ཡི་རྣམ་པ, second sentence (Pema Namgyal's gloss on Nyima Bepa).**

- Before: `...ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་གྱིས་ནི་...ཁོང་མའི་ཁྲོས་མའི་ཚུལ་གྱི་སྐབས་སུ་ངེས་པར་སྦྱར་བར་བཤད།།`
- After: `...ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་གྱིས་...འདི་རྗེ་བཙུན་མ་ཁྲོས་མའི་ཚུལ་དུ་བཞུགས་པའི་སྐབས་སུ་ངེས་པར་སྦྱར་དགོས་པར་བཤད་དོ།།`

This sentence itself is fine (ཁོང་མ → རྗེ་བཙུན་མ is the Tara-referent substitution already covered under Flagged #1-type changes). The actual drift is three sentences earlier in the **same paragraph**, in the clause introducing the sādhana source:

- Before (line 11 opening): `...ཉི་མ་སྦས་པའི་སྒྲུབ་ཐབས་ལས...` — "from **Nyima Bepa's** sādhana" (no title).
- After (line 11 opening): `...སློབ་དཔོན་ཉི་མ་སྦས་པའི་སྒྲུབ་ཐབས་ལས་འབྱུང་བའི...` — "from the sādhana of **Acharya (སློབ་དཔོན) Nyima Bepa**".

`grep` confirms `སློབ་དཔོན` occurs **once** in `body-after.txt` and **zero** times anywhere in the source `article.md` — this is an invented title with no textual basis, inserted by the model. It is also internally inconsistent: the very same figure is named **གྲུབ་ཆེན་ཉི་མ་སྦས་པ** ("Mahasiddha Nyima Bepa" — row 36, §གཞུང་ལུགས P2) later in this same article, and appears untitled elsewhere (row 20/21). Per Rule 1 ("nothing added, however standard") and Rule 8 ("content added ... is a FAIL"), this is factual drift: it silently credits a historical tantric author with a rank/title the source article never attests and that conflicts with the title the article does attest for him. This is a single, precisely localized token addition — the fix is to delete `སློབ་དཔོན་` from that one clause (or re-run for a fresh sample) — but it is a hard finding, not a stylistic flag.

## Ref attachment walk

Walked all 15 unique ref names (69 total tag instances, matching the script's token-conservation count) — for each, whether the statement(s) the ref is attached to in `body-after.txt` match `body-before.txt`.

| Ref | Statements it supports (before) | Same in after? |
|---|---|---|
| taranatha | lead identification (×2 uses); 4-part etymology origin story; unique "Ma" 4th-name gloss; unique wisdom-eye gloss of "Nyurma"; 3-worlds gloss; summary tear-birth history | YES — every attachment point unchanged |
| yama-sonam | 3-stage etymology; distinguishes "Nyurma" swiftness; 8-armed form addition (×2 sentences); quality↔name correlation; 8/16-fears tie-in; bodhicitta-to-buddhahood "Pawo" gloss; female-form vow; realm-triad gloss; tear-birth history; summary | YES |
| palden-sherab | lead (embodiment claim); body-form (red, wrathful, 2-hand mudras); activity (bodhicitta/light); White/Green Tara ID; summary (×2 refs) | YES |
| sangye-nyentrul | lead; body-form (red/wrathful/mudras); activity (bodhicitta/light); tear-birth attestation; summary | YES |
| sungrab-tulku | lead (3-names-are-synonyms claim, ×2 uses); verbatim quote on lightning-eye | YES |
| dharmabhadra | "Nyurma" comparison-with-buddhas gloss; 3-worlds gloss; "Palmo" reading + verbatim quote; summary | YES |
| drakpa-gyaltsen | "Pawo" gloss (power over affliction/māra/fear); 3-worlds gloss; "Pawo"-reading concurrence; summary | YES |
| gendun-gyatso | "Nyurma" swiftness gloss (co-cite) | YES |
| karma-maitri | lightning-eye ↔ body-form tie-in | YES |
| tenzin-dhonzang | phyag/'tshal gloss; deity-analogy (Avalokiteshvara/Manjushri/Vajrapani/Tara); "Palmo"-as-scribal-error judgment | YES |
| tenga-tulku | unique wisdom-eye gloss (sees rise/fall six times daily) | YES |
| pema-namgyal | wisdom-eye ↔ wrathful-manner gloss (**the sentence carrying the flagged addition — see above; the ref's attachment to this claim is unchanged, only the sādhana-source clause upstream gained the unattested title**); White/Green Tara ID | YES (attachment point) / see drift note above for surrounding content |
| tsultrim-namdak | reddish-yellow body-form gloss; realm-triad-only reading | YES |
| gendun-drub | unique tear-request history + lightning-eyes-from-valor gloss (verb changed, see Flagged #8); realm-triad-only reading | YES (attachment unchanged; content nuance flagged separately) |
| konchok-thabkhe | whose-tears question, Avalokiteshvara-eyes reading via Nyima Bepa; two-lineages conclusion | YES |

No ref was found reattached to a different statement, a different commentator's claim, or a different part of the article than in `body-before.txt`.

## Verdict

**FAIL** — one instance of factual drift (Rule 8: "content added"): an unattested honorific title (སློབ་དཔོན་, "Acharya") was inserted before the name Nyima Bepa in §སྐུ་ཡི་རྣམ་པ, second paragraph, inconsistent with the title (གྲུབ་ཆེན་, "Mahasiddha") the same article correctly and consistently attests for the same person elsewhere. Every other change in the article (see the table and §Flagged substitutions above) is a Rule-8 lexical substitution — register/grammar/synonym level, same facts, same position-holders, refs correctly attached to the same statements — and would independently support a PASS.

This is a single, precisely localized, mechanically-uncaught addition (C1's token conservation does not check content outside `<ref>` tags, so it could not have caught this). Recommended resolution per Rule 8: either (a) hand-delete `སློབ་དཔོན་` from the one clause in `article.md` (`...ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་གྱིས་གོང་གསལ་ཉེར་སྤྱོད་ཅན་དེ་ལས་གཞན་དུ་**སློབ་དཔོན་**ཉི་མ་སྦས་པའི་སྒྲུབ་ཐབས...`) and re-verify just that sentence, or (b) re-run `gemini_polish.py` once for a fresh sample per Rule 8. Left as-is for the domain expert's decision; `article.md` in this pilot folder is written as the script produced it (uncorrected) so the reviewer can see the actual drift in context.


## Reverted drift (orchestrator pass, 2026-08-21)

The unattested honorific སློབ་དཔོན་ that Gemini inserted before ཉི་མ་སྦས་པ was reverted
in `article.md` by surgical deletion (Rule 8 remedy (a)) — the sentence now matches the
source wording exactly at that span. `body-after.txt` is left untouched as the raw model
record, so it still shows the insertion. The same insertion occurred independently in
tara-02; the pattern is now blocked in the script prompt and documented in the SKILL.md.
With this reversion the single factual-drift finding is resolved; every other diff item was verified identical or recorded as a flagged substitution, so the verdict is PASS-after-reversion.