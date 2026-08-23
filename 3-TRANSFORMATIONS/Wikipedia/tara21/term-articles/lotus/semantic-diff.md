---
topic: lotus
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/lotus/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — lotus

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lede: pad+ma is the name applied to the water-born flower; a recurring symbol across the root verses and commentaries — Tārā's hand-attribute, sādhana seat-marks, and the goddess's birth story. | Same, restyled: "is the name of the water-born flower"; same three-item list, reformatted with clause breaks. | Yes | Cosmetic simplification of "name applied to" → "name of"; no referent change. |
| 2 | Root verse 3 quoted verbatim; explains Tārā's left hand adorned with the water-born lotus. | Same, quote untouched; "ཕྱག་གཡོན་ན" → "ཕྱག་གཡོན་པ" (both "left hand"). | Yes | — |
| 3 | ངེས་ཚིག: pad+ma and utpala treated as non-distinct; the pad+ma of verse 3 identified as the blue utpala; all 16 base commentaries agree. | Same content, reworded connectives (བཤད་དེ→བཤད་ཅིང་, མིན་པའི་...གཞན་→ལས་གཞན་པའི). | Yes | — |
| 4 | Gold-bodied Tārā's left hand adorned in detail by the blue utpala (per multiple commentators). | Same. | Yes | — |
| 5 | Gedün Drub: the mudrā also read as sign of the ten perfections; other base commentaries don't link it to the ten explicitly, but Tinpung's commentary treats the same mudrā as sign of the perfected/consummated perfections. | Same, only clause-break punctuation and བཤད→གསུངས (both "explained/stated"). | Yes | Verb synonym swap, see Flagged substitutions. |
| 6 | Birth-story: goddess born from the pistil of **a** water-born lotus that grew from Avalokiteśvara's tear. | Same, but "ཆུ་སྐྱེས་པདྨ་ཞིག" ("a [certain] lotus") loses the indefinite ཞིག → "ཆུ་སྐྱེས་པདྨ". | Yes (same referent) | Indefinite-marker drop, see Flagged substitutions. Note: the parallel sentence in the summary paragraph (§Sentence 15) still carries ཞིག unchanged. |
| 7 | Not stated explicitly in the individual root-verse contexts, but in the context of **additional/supplementary sādhana texts** (ལྷག་པའི་སྒྲུབ་ཐབས), the combined lotus-and-moon seat becomes a general feature across sādhana sequences (Palden Sherab, Sangye Nyentrul). | Qualifier ལྷག་པའི ("additional/supplementary") silently dropped — reads as a generic "in the context of sādhana" instead of "in the context of *additional* sādhana [texts, beyond the root verses]". | **NO — drift found and reverted** | See Reverted drift below. |
| 8 | Detail: colour of seat varies per verse's body-colour in individual sādhanas (each mudrā's utpala the common base; specifics of seat-colour agree between Palden Sherab and Sangye Nyentrul). | Same content, restructured into shorter clauses. | Yes | — |
| 9 | Yama Sönam's commentary: seat colours detailed per verse (yellow body → yellow lotus + moon seat; red body → red lotus + sun seat, etc.). | Same. | Yes | — |
| 10 | Palden Sherab alone gives two hidden/secret meanings of the lotus attribute in his commentary on verse 3: (a) completion-stage-with-signs reading via the quoted verse (lotus = ethics/asceticism etc., vajra = the six perfections through union); (b) completion-stage-without-signs reading — lotus as example of self-arisen wisdom whose subject-object stains are self-purified; unique to this khenchen among all consulted commentaries. | Same two meanings, same attribution to Palden Sherab alone, quotation verbatim identical; "རང་གིས་དག་པའི" → "རང་དག་ཏུ་གྱུར་པའི" (both "self-purified"); "ཡིན་ནོ" → "སུ་གྱུར་ཏོ" (both "is/has become [unique]"). | Yes | Grammar-variant/verb swap only. |
| 11 | Other markers: beyond hand/seat attribute (ཕྱག་མཚན), "lotus" also names the sole of Tārā's foot; her face likened to a fully-blossomed lotus, wrathful-browed. | Same; "ཕྱག་དང་གདན་གྱི་ཕྱག་མཚན" → "ཕྱག་དང་གདན་གྱི་མཚན་མ" (term swap, same referent: the identifying attribute of hand and seat). Face-simile sentence byte-identical. | Yes | See Flagged substitutions. |
| 12 | Tenzin Dhonzang: "Padma'i Lhamo" also named among the auspicious-**sign** (བཀྲ་ཤིས་བརྡའི) deity group (parasol, śrīvatsa, vase goddesses); benefits of eloquence and pleasing form; explicitly a different class of deity from Tārā's own lotus attribute. | Same content and attribution; "བཀྲ་ཤིས་བརྡའི" → "བཀྲ་ཤིས་རྟགས་ཀྱི" (both name the same auspicious-symbol category). Rest of paragraph byte-identical. | Yes | See Flagged substitutions. |
| 13 | Khenpo Tsültrim Namdak: in refuge-visualization, Tārā (embodiment of all refuges) sits on lotus-and-moon seat; White Tārā (via the Wish-Fulfilling Wheel praise) likewise on a lotus-and-moon seat, no different. | Same; "པདྨ་ཟླ་བའི་གདན" → "པདྨ་དང་ཟླ་བའི་གདན" (added དང་ conjunction) twice. | Yes | — |
| 14 | Divergence section: most commentaries state the goddess born from Avalokiteśvara's tear; Tāranātha and Karma Maitrī describe the lotus/pistil origin without explicitly mentioning the tear; five named commentators (Gendün Gyatso, Sungrab Tulku, Dharmabhadra, Tsültrim Namdak — tear-based; Sangye Nyentrul — tear stated but goddess emerges directly from it, no lotus-birth step). | Same five+ named commentators, same positions attributed to each, same divergence structure; only clause-break punctuation and grammar-particle swaps (ནས→ཡིས, ཏེ→པས, etc.). Verbatim Tāranātha quotation byte-identical. All personal names unchanged, no honorifics inserted. | Yes | — |
| 15 | Summary paragraph: pad+ma = utpala = blue lotus; became Tārā's hand-attribute per verse 3; recurs as lotus-and-moon seat / utpala hand-position across sādhanas; birth story also tied to "a" water-born lotus (ཞིག retained here). | Same four sentences; only sentence-final verb particles added (དོ/ཏོ/ངོ) and one དང་ conjunction added. | Yes | — |

## Ref attachment walk

Ref name sequence extracted from `body-before.txt` and `body-after.txt` and diffed: **identical order, identical names, same count (40 ref tags)**. Walking each ref against its paragraph:

- `sungrab-tulku`, `dharmabhadra`, `drakpa-gyaltsen` (lede) — same statement (verse-3 iconography) before/after. YES
- `gendun-gyatso`, `karma-maitri`, `taranatha`, `konchok-thabkhe`, `palden-sherab` (hand-attribute section) — same statement. YES
- `gendun-drub` (ten-perfections reading) — same statement. YES
- `gendun-gyatso`, `sungrab-tulku`, `dharmabhadra` (birth-story) — same statement. YES
- `palden-sherab`, `sangye-nyentrul` (sādhana seat section, both occurrences) — same statement (after the reverted-drift fix, see below); ref still attached to the claim about combined lotus-moon seat generalizing across sādhana sequences. YES
- `yama-sonam` (seat-colour detail) — same statement. YES
- `palden-sherab` ×2 (secret-meaning section) — same statement, same exclusive attribution. YES
- `pema-namgyal` ×2, `tsultrim-namdak`, `dharmabhadra` (foot-sole / face-simile) — same statement. YES
- `tenzin-dhonzang` (Padma Devi auspicious-sign group) — same statement. YES
- `tsultrim-namdak` (refuge visualization / White Tārā) — same statement. YES
- `taranatha`, `karma-maitri`, `gendun-gyatso`/`sungrab-tulku`/`dharmabhadra`, `tsultrim-namdak`, `sangye-nyentrul` (divergence section) — each ref stays attached to its named commentator's position, unchanged. YES
- `dharmabhadra`, `drakpa-gyaltsen`, `palden-sherab`, `karma-maitri` (summary) — same statements. YES

No ref migrated to a different clause anywhere in the article.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — do not block PASS:

| Location | Before | After | Note |
|---|---|---|---|
| Gedün Drub para (§5) | བཤད (explained) | གསུངས (stated/explained, honorific register) | Synonym verbs, same meaning. |
| Secret-meaning para (§10) | རང་གིས་དག་པའི (self-purified by itself) | རང་དག་ཏུ་གྱུར་པའི (become self-pure) | Same doctrinal content (self-purification of subject-object stains as example of self-arisen wisdom). |
| Secret-meaning para (§10) | ཡིན་ནོ (is [unique]) | སུ་གྱུར་ཏོ (has become [unique]) | Same claim of exclusivity to Palden Sherab. |
| Other-markers para (§11) | ཕྱག་དང་གདན་གྱི་ཕྱག་མཚན (hand-and-seat's "hand-attribute") | ཕྱག་དང་གདན་གྱི་མཚན་མ (hand-and-seat's "mark") | Same referent — the identifying attribute of both hand and seat; the lede already distinguishes ཕྱག་མཚན (hand) from གདན་མཚན་མ (seat), so the generic མཚན་མ arguably fits the dual referent better. No commentator or fact affected. |
| Padma Devi para (§12) | བཀྲ་ཤིས་བརྡའི་ལྷ་མོ (auspicious-**sign** goddess) | བཀྲ་ཤིས་རྟགས་ཀྱི་ལྷ་མོ (auspicious-**mark/token** goddess) | Both name the same class of deity (personifications of the auspicious symbols, alongside parasol/śrīvatsa/vase goddesses); no change to which deities are named or what is claimed of them. |
| Birth-story para (§6) | ཆུ་སྐྱེས་པདྨ་ཞིག (a [certain] lotus) | ཆུ་སྐྱེས་པདྨ (the/a lotus, indefinite marker dropped) | Same referent (the lotus from Avalokiteśvara's tear); the parallel sentence in the summary (§15) still carries ཞིག unchanged, so the drop is inconsistent stylistically but not fact-changing. |

## Reverted drift

**Location:** སྒྲུབ་ཐབས་ཀྱི་གདན་དང་ཕྱག་མཚན section, first sentence (refs `palden-sherab`, `sangye-nyentrul`).

**Before:** "...ལྷག་པའི་སྒྲུབ་ཐབས་ཀྱི་སྐབས་སུ་ཡང་པདྨ་ཟླ་བ་དང་སྦྲགས་པའི་གདན་ནི་..." — "in the context of **additional/supplementary sādhana [texts]** also, the seat combining lotus and moon has become a general feature..."

**Gemini's output (drift):** "...སྒྲུབ་ཐབས་ཀྱི་སྐབས་སུ་པདྨ་དང་ཟླ་བ་སྦྲགས་པའི་གདན་ནི་..." — the qualifier ལྷག་པའི ("additional/supplementary") was silently dropped, leaving a generic "in the context of sādhana," which broadens the claim from a specific subset of sādhana literature (supplementary to the root praise verses) to sādhana practice in general. Confirmed by grepping both body files: ལྷག་པ appears exactly once in `body-before.txt` and zero times in `body-after.txt` — a clean drop, not a paraphrase. This matches known drift pattern (e), a dropped scope-narrowing qualifier.

**Remedy applied (Rule 8a, surgical reversion):** restored the exact span in `article.md` — inserted ལྷག་པའི immediately before སྒྲུབ་ཐབས་ཀྱི་སྐབས་སུ so the sentence now reads "...ལྷག་པའི་སྒྲུབ་ཐབས་ཀྱི་སྐབས་སུ་པདྨ་དང་ཟླ་བ་སྦྲགས་པའི་གདན་ནི་...", matching the source's scope exactly. `body-after.txt` left untouched as the raw model record, per Rule 8(a).

## Verdict

**PASS-after-reversion.** One factual-scope drift was found (a dropped qualifier narrowing "sādhana" to "additional/supplementary sādhana") and surgically reverted in `article.md`; `body-after.txt` was left as the raw record of Gemini's output. No other fact was added, dropped, strengthened, weakened, or re-attributed to a different commentator anywhere in the article. Every `<ref>` remains attached to the exact statement it supported before polishing (40/40 refs, identical sequence). All verbatim quotations (root verse 3, the Tāranātha quotation, the Palden Sherab completion-stage-with-signs quotation) are character-for-character identical before and after. No unattested honorific was inserted before any personal name — all six named commentators in the divergence section (Tāranātha, Karma Maitrī, Gendün Gyatso, Sungrab Tulku, Dharmabhadra, Khenpo Tsültrim Namdak, Sangye Nyentrul) keep their exact source name forms. Six additional lexical-only substitutions were flagged above for the domain expert's awareness; none of them changes a referent, a fact, or an attribution.
