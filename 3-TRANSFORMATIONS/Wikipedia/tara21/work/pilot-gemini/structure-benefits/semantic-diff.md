---
topic: structure-benefits
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/structure-benefits/article.md
model: gemini-3.1-pro-preview
date: 2026-08-21
verdict: PASS
status: draft
---

# Semantic diff — structure-benefits

Note on process: the script was run twice. Attempt 1 (temperature 0.3) passed hard checks
C1–C7 but raised one W1 warning (paragraph 4 in `== ས་བཅད། ==` ended in single shad
`ཞིག་གོ།` instead of `།།`). That paragraph is a plain declarative sentence — not a
lead-in ending ལས།/ཏེ། before a verse quote, and not a standalone verse-quote paragraph
closing on a quotation mark — so the warning was judged genuine, not a false positive,
per skill Rule 4 (paragraph-final double shad still binds) and Procedure step 3. The
script was re-run once (fresh sample); attempt 2 passed C1–C7 with 0 warnings, including
a correct `།།` close on that paragraph. All comparison below is attempt 2's
`body-after.txt` against `body-before.txt`. (For the record, attempt 1's draft also
contained two changes attempt 2 does not: a narrowed "བསྟོད་དོན་" → "བསྟོད་པ་དངོས་" in
the lead, and a dropped "དད་པ" head-noun in paragraph "ཉི་ཟླའི་འཛུམ་རླབས་ལས་ནི་...".
Neither survived into the accepted attempt 2, so neither is carried into the tables below.)

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: work = 21 homages to Tārā praising her, with a benefits section at the end; 3 commentaries cited for this framing | Same | YES | instrumental `གིས་` → `གི་སྒོ་ནས་` (by means of → through), same referent |
| 2 | Many commentaries say there are 21 verses in the topic of praise (བསྟོད་དོན་) | Same, same term `བསྟོད་དོན་` retained | YES | phrasing tightened, no scope change |
| 3 | Per the colophon, Vairocana Buddha spoke this praise to Tārā | Same | YES | `མཇུག་བྱང་ལས་བཤད་པ་ལྟར་` → `མཇུག་བྱང་ལྟར་`, same assertion, same directness (`གསུངས་པའོ།།` unchanged) |
| 4 | Some commentaries: 3-part sa bcad — brief teaching, detailed explanation, benefits (3 refs) | Same | YES | `སྤྱིའི་སྒྲུབ་ཚུལ` → `སྤྱིའི་འཆད་ཚུལ` — see Flagged substitutions |
| 5 | Other commentaries: 2-part sa bcad — actual praise + benefits, with verbatim quote from Drakpa Gyaltsen; Rinam Shed and Dusdrel agree; Palden Sherab: 4-part traditional structure reduces to the same 2-fold division | Same, quote verbatim | YES | ref attachments unchanged |
| 6 | Actual-praise subdivision differs by commentary: Utpala'i Chunpo = history/form/activity (3), form further split into 6 peaceful + 7 wrathful; Gsalwa'i Odzer = form/dharmakāya/activity (3), activity further split into 6 (mantra, empowerment, poison, obstacles, epidemic, discord) — a different system from Utpala's | Same | YES | W1 fixed: paragraph now ends `གོ།།` (double shad) |
| 7 | Melong: the fixed count of 21 homages explained via history(1)+peaceful form(6)+wrathful form(7)+dharmakāya(1)+activity-qualities(6)=21; Rnam bshad and Bsdus 'grel agree all 21 are homages | Same | YES | all six sub-counts and the total (21) unchanged |
| 8 | Benefits sa bcad: Gsalwa'i Odzer/Tikka Rinchen Trengwa = 4-fold (intent, timing, benefits detailed, benefits summarized); Nyida'i Dzumlab = 2-fold (chief cause, actual benefits) | Same | YES | — |
| 9 | Recitation manner: recall wrathful form at dusk, peaceful form at dawn, recite with reverence | Same | YES | — |
| 10 | Mere recollection grants fearlessness; quote: "དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར།" | Same, quote verbatim | YES | — |
| 11 | Purifies sin, protects from lower rebirth; Tāranātha: even one karmically destined to a lower rebirth is freed by the splendor of having recited the praise | Same | YES | — |
| 12 | Reciting swiftly empowers one by 700 million buddhas, culminating in buddhahood | Same | YES | — |
| 13 | Protects from poison (ingested/touched, still/moving); also pacifies spirit-harm, epidemic disease, and suffering of others, not only oneself | Same | YES | "རང་ཉིད་ལས་གཞན...ཡང" → "རང་ཉིད་ཙམ་དུ་མ་ཟད...ལའང" — see Flagged substitutions |
| 14 | Multiple traditions on repeating the closing "2, 3, 7": poet tradition (2/3/7 tied to practitioner faculties/time/session-count); Rinchen Bu Ton tradition (2/3/7 → 42/day-night); Rnam bshad (3+3=49); Tikka Zhallung (harmonizes both, 7×3 or 2+3+7 per watch) | Same | YES | all numbers (2,3,7,42,49) unchanged |
| 15 | Reciting with correct count grants sons/wealth per wish, removes obstacles | Same | YES | — |
| 16 | "Poison" interpreted variously: Tikka Rinchen Trengwa = wrong view obstructing buddhahood; Bsdus 'grel = self-view/thief/flesh-eater etc.; Melong = three afflictive obscurations; three systems don't conflict but use the term differently | Same | YES | — |
| 17 | Nyida'i Dzumlab: chief cause of benefits is heartfelt devoted-and-reverent faith (དད་པ) toward the goddess, established by citing Prajñāpāramitā, treasure-casket sūtra, etc. | Same | YES | noun `དད་པ` retained (not dropped, unlike attempt 1's draft) |
| 18 | Tāranātha explains each root-mantra syllable doctrinally; recitation yields siddhis (pacifying rites, pills, eye-medicine, sword, yakṣiṇī, great treasure, etc.) | Same | YES | verb `བཤད` retained (attempt 1 had swapped to `བཀྲལ`; not present in accepted attempt) |
| 19 | ལོ་རྒྱུས།: colophon says Vairocana spoke the praise to Tārā; Tikka Zhallung, Dud rtsi'i dga' tshal, Rnam par bshad pa all agree | Same | YES | — |
| 20 | Gsalwa'i Odzer: lineage from Nāgārjuna, translated by Nyen, finalized by Drakpa Gyaltsen | Same | YES | — |
| 21 | Tikka Zhallung: this tantra was spoken not only by Vairocana but also by our teacher [Śākyamuni]; citing Mañjuśrī-nāma-saṃgīti that past/future/present buddhas repeat it; many teachers hold this transmission | Same | YES | — |
| 22 | Tāranātha examined the colophon record: traditionally said to derive from the 700-chapter Tārā-tantrarāja; the various currently known "activity" tantras are composed by scholars and not its true source, but it may still be a fragment/condensation of the extended tantra | Same | YES | — |

## Ref attachment walk

All 51 `<ref>` tokens (C1-verified for count) were walked individually against the statement each sits on in `body-before.txt` vs `body-after.txt`.

- Every ref remains on the same clause/sentence it supported before: e.g. `dharmabhadra`/`lobsang-dawa`/`drakpa-gyaltsen` after the opening 3-commentary list; `tenga-tulku`/`gendun-gyatso`/`karma-maitri` after the "21 verses" claim; `drakpa-gyaltsen` after the colophon sentence and again after the closing quote in the sa-bcad paragraph; `palden-sherab` after the Palden Sherab sentence and again after the Nyida'i Dzumlab 2-fold division; `taranatha` after each of its five claims (lower-rebirth liberation, 700-million-buddha empowerment, "poison" section not directly authored but cited, the mantra-syllable/siddhi passage, and the colophon-critique passage); `konchok-thabkhe` after each of its four claims (poison, extends-to-others, the harmonized recitation-count scheme, and the "self-view" vs "poison" triad, plus the ལོ་རྒྱུས། opening list).
- No ref migrated onto a different assertion than the one its source claim supports. Sequence and count of the placeholder tokens (⟦R1⟧…⟦R51⟧, restored by the script to their original `<ref>` forms) is identical between before and after — verified by direct diff of the extracted quote/ref token order (see Bash output in the session), confirming C1's token-conservation guarantee held.

## Flagged substitutions

Per Rule 8, these are lexical/phrasal substitutions judged same-referent and arguably same meaning — recorded for the domain expert to accept or reject, not treated as drift:

1. **Line 4 (`== ས་བཅད། ==` opening sentence)** — describes what commentaries do when laying out the 3-part sa bcad.
   Before: `...བསྟོད་པ་འདིའི་སྤྱིའི་སྒྲུབ་ཚུལ་ལ་ས་བཅད་གསུམ་དུ་བཞག་སྟེ...` ("general method of *establishing/accomplishing*")
   After: `...བསྟོད་པ་འདིའི་སྤྱིའི་འཆད་ཚུལ་ས་བཅད་གསུམ་དུ་བཞག་སྟེ...` ("general manner of *explaining*")
   → `སྒྲུབ་ཚུལ` (accomplishing-method) vs `འཆད་ཚུལ` (explaining-method) are different verb roots. Both plausibly describe the same referent (how commentaries structure their exposition of the text), but a domain expert should confirm `སྒྲུབ` was not doing separate technical work (e.g. distinguishing textual composition from commentarial exposition) that `འཆད` collapses.

2. **Line 1 (lead sentence)** — how the work relates to its 21 homages.
   Before: `...ལ་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་གཞུང་...` ("a text that praises her *by/with* 21 homages")
   After: `...ལ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་སྒོ་ནས་བསྟོད་པའི་གཞུང་...` ("a text that praises her *through the gateway of* 21 homages")
   → Instrumental case swapped for a `སྒོ་ནས་` (by way of) construction; same referent and register, purely a syntactic idiom swap.

3. **Line 23 (poison-benefit paragraph, "extends to others" clause)**
   Before: `...ཕན་ཡོན་འདི་རང་ཉིད་ལས་གཞན་སེམས་ཅན་ལ་ཡང་ཁྱབ་པར་བཤད།` ("this benefit is explained to extend to sentient beings *other than* oneself")
   After: `...ཕན་ཡོན་འདི་རང་ཉིད་ཙམ་དུ་མ་ཟད་གཞན་སེམས་ཅན་ལ་ཡང་ཁྱབ་པར་བཤད།` ("...extends *not only to* oneself *but also* to other sentient beings")
   → Restructured from an exclusive "other than X" frame to an inclusive "not only X but also Y" frame. Same net claim (the benefit is not limited to the reciter), but the logical framing shifts from contrastive to additive — flagged so a domain expert can confirm this doesn't subtly change whether the benefit to oneself is being asserted as well as, vs. instead of, the benefit to others (before text is arguably ambiguous on whether the reciter is included; after text explicitly includes the reciter).

No other substitution rose above routine grammar-particle variation (ནས↔ལས, ལ↔ནི, ཀྱང↔ལས་ཀྱང, add/drop of བཅས/དང as list-bundling particles, add/drop of copula ཡིན) or sentence-boundary reflow (a single long clause split into two with an added shad, or two short clauses merged) — none of which alters what is claimed or who claims it.

## Frontmatter note

The bundled script carries the source frontmatter's `status:` field through unchanged (it only
appends `polished_by`/`polish_model`/`polish_date`/`polish_source`); the source here is
`status: published` (a live bo.wikipedia article). Per Rule 9 ("`status: draft` always... this
skill never publishes") and the Completion check's `status: draft` requirement, the pilot copy's
frontmatter was hand-corrected after the script ran: `status: published` → `status: draft`, with
the original value preserved as a new `polish_pilot_of_published_status: published` key so the
provenance (this is a pilot polish of a currently-published article) is not lost. This is the only
manual edit made to the script's output; no prose, ref, or wikitext content was touched by hand.

## Verdict

**PASS.** No fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator between `body-before.txt` and the accepted (attempt 2) `body-after.txt`. Both verbatim quotations survive character-for-character:
- `"བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ། བསྟོད་པ་དངོས་དང་ཕན་ཡོན་ནོ།"`
- `"དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར།"`

All 51 refs remain attached to the same statements they supported in the source. Three lexical substitutions are flagged above (§Flagged substitutions) for the domain expert's acceptance — none is factual drift. The one genuine W1 warning from attempt 1 (single-shad paragraph close) was resolved by re-running the script once, per Rule/step 3; attempt 2 closes that paragraph correctly with `།།` and also happens not to reproduce attempt 1's two more borderline rewordings (both noted above for the record, but not carried forward since they are not present in the accepted text).
