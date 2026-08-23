---
topic: tathagata
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/tathagata/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tathagata

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | "Tathāgata" is one of the epithets (grangs) for a buddha | same, "rnam grangs" instead of "grangs" | YES | lexical substitution (§Flagged) |
| 2 | All 16 commentaries gloss the 4th-homage verse's "gtsug tor" line via this term; Tārā herself is identified as uṣṇīṣa/mother of all tathāgatas | same | YES | verb honorific swap byed→mdzad (§Flagged) |
| 3 (ངེས་ཚིག) | Sermé Tsang Geshe glosses via emptiness/suchness; Tāranātha follows the same gloss | same | YES | added clarifying "de dang", no content change |
| 4 | Sermé Tsang Geshe also gives another etymology drawn from "ming brjod" (name-citation) | same, "mtshan brjod" + "lung drangs" | YES | ming→mtshan normalization (§Flagged); referent (his own further etymological remark) unchanged |
| 5 (དབྱེ་བ) | Usage divides into 3 contexts: uṣṇīṣa-linked, direct-name, tantric-class | same | YES | lag len → 'jug tshul/'jug pa, consistent global synonym swap (§Flagged) |
| 6 (§4th homage/uṣṇīṣa) | All 16 commentaries read the 4th-homage verse this way — most frequent usage; Tārā is mother/uṣṇīṣa-worthy of all tathāgatas | same | YES | honorific/particle changes only |
| 7 (§direct name) | Tsultrim Namdak: this 21-homage hymn is spoken by Vairocana himself | same | YES | bshad→bzhed honorific (§Flagged) |
| 8 | Tāranātha: 4th-homage uṣṇīṣa = Vairocana specifically; Yama Sönam's text agrees, ushnisha emanates wisdom of mantra-knowledge | same | YES | none material |
| 9 | Gelug scholars (Dülchu Dharmabhadra etc.): uṣṇīṣa refers to all tathāgatas generically | same | YES | bshad→bzhed honorific (§Flagged) |
| 10 | Tāranātha further: Amitābha resides in her topknot | same | YES | word-order + honorific swap |
| 11 (§tantric class) | Tāranātha: in generation-stage enumerations, "tathāgata uṣṇīṣa" denotes empowerment (dbang bskur) | same | YES | skor→skabs su lexical (§Flagged) |
| 12 | Sermé Tsang Geshe: "8 tathāgatas" subclass among tantric deity groups, same essence as buddhas despite differing form/name; cites the Guhyacintya-sūtra for tathāgata-wisdom pervading the 10 directions | same | YES | ming→mtshan (§Flagged), gsungs/lung drangs honorific additions |
| 13 | Tsultrim Namdak: on **one** Tārā (of the 21-Tārā group — verse 21's Tārā) crown/throat/heart, the body-speech-mind seed-syllables of all tathāgatas are placed | Gemini changed to **each** Tārā (re re'i) — a scope-widening drift from claim c-3-24 (verse 21's Sgrol-ma 'od-zer-can-ma specifically) to a universal claim about all 21 | **NO — REVERTED** | See §Reverted drift below |
| 14 (§history) | 3 commentaries: Buddha Tathāgata Dundubhisvara (Drumsound) appeared in a past age | same | YES | dropped agentive particle after "zhig" (grammar only) |
| 15 | Princess Yeshe Dawa's supreme devotion → bodhicitta | same | YES | bshad→gsungs honorific |
| 16 | Prophesied to hold the name "Tārā" until enlightenment | same | YES | ming...mtshan nyid → mtshan (simplification), same referent |
| 17 (§esoteric) | Khenchen Palden Sherab: two esoteric readings of the 4th homage — completion-stage-with-attributes: "tathāgata = fourth-joy wisdom"; completion-stage-without-attributes: uṣṇīṣa = Dzogchen Atiyoga view; both are asides, not literal-meaning-negating | same | YES | none material |
| 18 (§summary) | 16 commentaries gloss "tathāgata" via the 4th-homage uṣṇīṣa verse; some gave it as an etymological/defining-characteristic gloss (mtshan nyid nges tshig), others used it as Vairocana's proper name; also the Tārā-naming origin story | same | YES | "mtshan nyid nges tshig" → "mtshan gyi nges tshig" — drops the technical "defining-characteristic" qualifier but still points to the same section 2 content, not a different claim (§Flagged, borderline) |

## Ref attachment walk

All 34 ref tokens (per gemini-report.md) survived character-for-character (C1). Walked each `<ref>` against its governing clause:

- sungrab-tulku, dharmabhadra (lead) — same statement (uṣṇīṣa/mother identification). YES
- tenzin-dhonzang, taranatha (ངེས་ཚིག §) — same etymology statements. YES
- tenzin-dhonzang (§division), taranatha — same three-usage-context claim. YES
- sungrab-tulku, taranatha, tenzin-dhonzang (§4th-homage) — same "most frequent usage" claim. YES
- dharmabhadra, gendun-drub, konchok-thabkhe (§4th-homage, 2nd sentence) — still trail the same compound "mother/uṣṇīṣa-worthy" statement after the mid-sentence shad split; no re-attachment occurred. YES
- tsultrim-namdak (§direct name, 1st) — same "hymn spoken by Vairocana" claim. YES
- taranatha, yama-sonam (§direct name, 2nd) — same Jonang uṣṇīṣa=Vairocana + mantra-wisdom claim. YES
- yama-sonam (§direct name, 3rd) — same "Gelug generic" claim. YES
- taranatha (§direct name, 4th) — same "Amitābha in topknot" claim. YES
- taranatha (§tantric, 1st) — same "empowerment" claim. YES
- tenzin-dhonzang (§tantric, 2nd) — same "8 tathāgatas" + Guhyacintya-sūtra claim. YES
- tsultrim-namdak (§tantric, 3rd) — same seed-syllable claim, now restored to its correct scope (see below). YES after reversion
- sungrab-tulku, tenzin-dhonzang, tsultrim-namdak (§history, ×3) — same three history statements. YES
- palden-sherab (§esoteric, ×3) — same two-reading + caveat statements. YES
- sungrab-tulku, tenzin-dhonzang (§summary) — same closing paraphrase. YES

No ref migrated to a different clause.

## Flagged substitutions

Lexical-only swaps, same referent, both forms attributable to the same source claim — recorded for domain-expert review, not blocking PASS:

| Before | After | Location |
|---|---|---|
| མཚན་གྱི་གྲངས་ཤིག | མཚན་གྱི་རྣམ་གྲངས་ཤིག | lead sentence 1 |
| འགྲེལ་བཤད་བྱེད་ཅིང་ / ངོས་འཛིན་བྱེད། | འགྲེལ་བཤད་མཛད་ཅིང་ / ངོས་འཛིན་མཛད་དོ། | honorific verb throughout (byed→mdzad, bshad→gsungs/bzhed, systematic register elevation) |
| མིང་བརྗོད་ལས་དྲངས་ | མཚན་བརྗོད་ལས་ལུང་དྲངས་ | ངེས་ཚིག § |
| ལག་ལེན་ | འཇུག་ཚུལ་ / འཇུག་པ་ | དབྱེ་བ § (applied consistently) |
| བཤད། (Tsultrim Namdak's, Geluk scholars') | བཞེད། | §direct name, ×2 |
| ...ཞིག་གིས་མངོན་སུམ་དུ་བྱོན་ | ...ཞིག་མངོན་སུམ་དུ་བྱོན་ | §history (dropped stray agentive particle — grammar fix) |
| མིང་...མཚན་ཉིད་འཛིན་པར / མིང་ལྷ་མོ་སྒྲོལ་མའི་མཚན་ཉིད / མིང་སྒྲོལ་མར | ...མཚན་འཛིན་པར / ལྷ་མོ་སྒྲོལ་མ་ཞེས་པའི་མཚན་ / མཚན་སྒྲོལ་མར | ming→mtshan normalized throughout, incl. §history and §summary |
| མཚན་ཉིད་ངེས་ཚིག་ཏུ་གསུངས | མཚན་གྱི་ངེས་ཚིག་གསུངས | §summary — drops "mtshan nyid" (defining-characteristic) qualifier; still points to the same ངེས་ཚིག-section content, no different claim asserted, but the technical framing is weaker. Flagged for domain-expert attention as the most borderline item in this pass. |
| ནང་གསེས་སུ / སྐོར་ | ནང་ཚན་དུ / སྐབས་སུ | §tantric class, synonym swaps |

## Reverted drift

**§ "Tantric class" (3rd sentence, ref `tsultrim-namdak`).** Gemini's output changed "སྒྲོལ་མ་**གཅིག་**གི་སྐུའི་སྤྱི་བོ་མགྲིན་པ་སྙིང་ག་གསུམ་ལ" (on **one** Tārā's — of the 21-Tārā group — crown, throat, heart) to "སྒྲོལ་མ་**རེ་རེའི**་སྐུའི་སྤྱི་བོ་དང་མགྲིན་པ། སྙིང་ག་གསུམ་ལ" (on **each** Tārā's crown, throat, heart). The underlying claim (`2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md` c-3-24, cited to `1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-261–#^0-266`) is specific to **verse 21's** deity (Sgrol-ma 'od-zer-can-ma), not a claim that this happens for each of the 21 Tārās. "Each" universalizes a claim the source restricts to one specific figure — a dropped scope-narrowing qualifier (pattern e) plausibly read by the model as a "natural" tantric-visualization generalization, exactly the kind of plausible-looking "correction" Rule 8 warns against accepting.

**Fix applied:** surgical reversion in `article.md`, restoring "སྒྲོལ་མ་གཅིག་གི" in place of "སྒྲོལ་མ་རེ་རེའི" (Gemini's other, non-quantifier restructuring of this sentence — the added "དང་" and shad-split — was left as harmless stylistic recomposition since it does not affect the quantifier's scope). `body-after.txt` was left untouched as the raw model record, per Rule 8(a).

## Verdict

**PASS-after-reversion.** One factual drift was found and surgically corrected (see above): a quantifier ("one Tārā" → "each Tārā") that silently generalized claim c-3-24 beyond what the source commentary supports. Every other change across the article is a register/lexical substitution (honorific verb elevation, ming→mtshan terminology normalization, synonym swaps for "usage/application") with the same referent and no fact added, dropped, weakened, strengthened, or re-attributed. Both verbatim quotations are character-for-character identical to the source. All 34 refs remain attached to the same statements they supported before polishing, including after reversion. Headings, tail (`== འབྲེལ་ཡོད་ཤོག་ངོས། ==` onward), bold spans, and category are byte-identical to the source.
