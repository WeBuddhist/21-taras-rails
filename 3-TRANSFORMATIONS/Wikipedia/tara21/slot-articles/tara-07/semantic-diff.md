---
topic: tara-07
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-07/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-07

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: this verse is the chod-brjod of the 7th stanza of the 21-praise; root quote follows | unchanged | YES | ref set unchanged |
| 2 | Root verse quotation (tra/phat, right-bent/left-extended feet **treading**, amid blazing fire) | unchanged, character-for-character | YES | verbatim quote untouched |
| 3 | Paraphrase: by uttering tra/phat she instantly destroys curses/evil-mantra machinery; with right-bent/left-extended feet she abides amid blazing fire | same, minor word-order/punctuation only after reversion | YES | see "Reverted drift" — the paraphrase originally omitted the verb "treading/pressing" (མནན་ཏེ) that only the verse quote carries; Gemini's draft inserted it into the paraphrase, reverted |
| 4 | § Name gloss: no single fixed name across traditions; Yama Sönam/Tenzin Dhönzang → "gzhan mthu 'joms ma"; Palden Sherab → "gzhan gyis mi thub ma"; Sangye Nyentrul/Tsultrim Namdak → a closely similar name | same claims, same attributions | YES | "gdags"→"btags" spelling variant; "not established as a single name" → "various different ones occur" — same claim, flagged below |
| 5 | Drakpa Tulku → "gzhan 'joms ma", a short form of the above without "mthu"; Gendün Drub → different root name "rgol ba 'joms pa'i sgrol ma" | same | YES | punctuation reflow only |
| 6 | Dharmabhadra/Sangye Nyentrul on tra=tearing/destroying, phat=roar of exploding vidya-mantra; Tenzin Dhönzang glosses tra as "bsgral ba" | same | YES | ལ→དང particle swap, no meaning change |
| 7 | § Body form: right-bent/left-extended = emptiness+compassion sign (Dharmabhadra/Gendün Drub/Sangye Nyentrul); Gendün Drub: bent=realizing emptiness, extended=compassion | same | YES | punctuation only |
| 8 | Yama Sönam's expanded iconography: yellow body, lotus+sun seat, wrathful black face, yellow garment, jeweled crown, one face four arms (R: wheel+sword, L: noose+threat mudra) | same | YES | "so sor"→"zur du" synonym swap; list punctuation reflowed, same 4 items |
| 9 | Sangye Nyentrul/Palden Sherab: wrathful-tummo body, black, blazing pyre-of-embers-like wisdom fire, one face two arms | same | YES | genitive particle dropped in compound, same referent |
| 10 | § Activity: 11 commentaries: tra/phat merely uttered destroys enemy curse/evil-mantra apparatus instantly; Könchok Thabkhé: also destroys the evil vidya-mantra itself, not just the apparatus | same | YES | clause reordered, "bshad" added as explicit evidential — same claim |
| 11 | She pacifies epidemics/disease and protects beings (Taranatha/Drakpa Tulku/Tsultrim Namdak); Sangye Nyentrul: visualizing destruction of all enemies is a special meditation instruction | same | YES | unchanged |
| 12 | § Differing systems: 6 commentaries count this as the 7th of 21 praises; Dharmabhadra/Gendün Drub/Tenga Tulku count it under the 6th "praise-type" (mode) subdivision instead, per Dharmabhadra "praising by destroying the other" | same | YES | punctuation only |
| 13 | Hidden-meaning (channels/winds/drops): Palden Sherab & Taranatha agree — right channel roma bent = downward-looking, left channel kyangma extended = ... | same | YES | typo fix ("bshad pa ni" spacing), punctuation |
| 14 | Könchok Thabkhé: different hidden meaning per a mahasiddha's system — tra = mantra destroying lower rebirth (from a purification tantra), phat = syllable propelling consciousness upward, applied by the siddha to this practice; he considered another reading but did not write it, deferring to the siddha's intent | same | YES | "bsams kyang"→"bsams mod kyi" concessive-particle swap, same meaning |
| 15 | § Summary: she destroys curse/evil-mantra with tra/phat while abiding amid fire in bent/extended stance (Dharmabhadra/Drakpa Tulku); yet naming, numbering, and hidden-meaning traditions vary (Palden Sherab/Tenga Tulku/Könchok Thabkhé) | same after reversion | YES | see "Reverted drift"; idiom swap "nyin gsal"→"shin tu gsal lo", "yin yang"→"yin par bstan yang" (flagged) |

## Ref attachment walk

- `yama-sonam`, `palden-sherab`, `sungrab-tulku` (lead, opening chöd-brjod claim) — same statement before/after: YES
- `dharmabhadra` (root verse; the two paraphrase sentences it also tags) — same statement before/after: YES
- `yama-sonam`/`tenzin-dhonzang` ("gzhan mthu 'joms ma" naming) — same statement: YES
- `palden-sherab` ("gzhan gyis mi thub ma" naming) — same statement: YES
- `sangye-nyentrul`/`tsultrim-namdak` (closely-similar name) — same statement: YES
- `sungrab-tulku` (Drakpa Tulku's short-form name) — same statement: YES
- `gendun-drub` (different root name; bent/extended gloss) — same statement: YES
- `dharmabhadra`/`sangye-nyentrul` (tra/phat sound-meaning) — same statement: YES
- `tenzin-dhonzang` ("bsgral ba" gloss) — same statement: YES
- `yama-sonam` (expanded iconography) — same statement: YES
- `sangye-nyentrul`/`palden-sherab` (wrathful-tummo body) — same statement: YES
- `dharmabhadra`/`konchok-thabkhe`/`tsultrim-namdak` (11-commentary activity claim) — same statement: YES
- `konchok-thabkhe` (evil vidya-mantra itself destroyed) — same statement: YES
- `taranatha`/`sungrab-tulku`/`tsultrim-namdak` (epidemic-pacifying activity) — same statement: YES
- `sangye-nyentrul` (visualization instruction) — same statement: YES
- `yama-sonam`/`konchok-thabkhe`/`palden-sherab` (6-commentary count as 7th praise) — same statement: YES
- `dharmabhadra`/`gendun-drub`/`tenga-tulku` (count under 6th praise-type) — same statement: YES
- `palden-sherab`/`taranatha` (channel/wind hidden meaning) — same statement: YES
- `konchok-thabkhe` (siddha's-system hidden meaning) — same statement: YES
- Summary paragraph refs (`dharmabhadra`, `sungrab-tulku`, `palden-sherab`, `tenga-tulku`, `konchok-thabkhe`) — same statements as their first appearance: YES

No ref migrated to a different clause or statement. Token count (44) conserved per gemini-report.md C1.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — listed for domain-expert acceptance, does not block PASS:

| Before | After | Location |
|---|---|---|
| མཚན་གཅིག་ཏུ་མ་གྲུབ (not established as a single name) | མི་འདྲ་བ་སྣ་ཚོགས་ཤིག་འབྱུང་ (a variety occurs) | § མཚན་གྱི་ངེས་ཚིག, opening |
| གདགས / གདགས་ཤིང / གདགས་པ (designates) | བཏགས / བཏགས་ཤིང / བཏགས་པ (designated) | throughout § མཚན་གྱི་ངེས་ཚིག |
| དོན་གཅིག་པའི་མཚན་ཉེ་བར་མཚུངས་པ་ཞིག (a synonymous, closely-similar name) | དེ་དང་དོན་ཉེ་བར་མཚུངས་པའི་མཚན་ཞིག (a name close in meaning to that one) | § མཚན་གྱི་ངེས་ཚིག, Sangye Nyentrul/Tsultrim Namdak clause — flagged for closer expert read since "དོན་གཅིག་པ" (synonymous) is dropped in favour of a comparative "close to that [name]"; referent and overall claim (a near-equivalent name exists) unchanged |
| སོ་སོར (individually) | ཟུར་དུ (separately) | § སྐུ་ཡི་རྣམ་པ, Yama Sönam iconography clause |
| དོན་ལ་ཉེ (close to the meaning) | དོན་དང་ཉེ (close to the meaning) | § མཚན་གྱི་ངེས་ཚིག, tra/tearing gloss — grammatical particle only |
| བསམས་ཀྱང (though he thought) | བསམས་མོད་ཀྱི (he did think, but) | § གཞུང་ལུགས་སོ་སོའི་བཤད་པ, Könchok Thabkhé clause — concessive particle only |
| ཉིན་གསལ (clear as day) | ཤིན་ཏུ་གསལ་ལོ (very clear) | § བསྡུས་དོན், closing idiom |
| ཡིན་ཡང (although it is) | ཡིན་པར་བསྟན་ཡང་ (although it is shown/taught to be) | § བསྡུས་དོན், recap sentence — adds an explicit evidential frame ("taught by the cited sources") rather than a bare copula; the underlying iconographic/physical claim already established earlier in the article is not altered. Domain expert should confirm this reads as acceptable framing rather than an added claim. |

## Reverted drift

Gemini's draft inserted མནན་ཏེ ("pressing/treading with the feet") into two paraphrase sentences that, in the source article, describe the goddess's stance and location without that verb — the verb appears only inside the verbatim root-verse quotation two lines above ("...ཞབས་ཀྱིས་མནན་ཏེ།། མེ་འབར་..."), which Gemini apparently echoed into the surrounding prose. This is a factual addition (an action not asserted by the source's own paraphrase sentence), not a lexical substitution, so it is treated as drift per Rule 8 rather than logged as flagged.

- Location 1 — § opening paraphrase (dharmabhadra ref): reverted "...འཇོམས་ཤིང་གཡས་བསྐུམ་གཡོན་བརྐྱང་གི་ཞབས་ཀྱིས་མནན་ཏེ་མེ་འབར་..." back to the source's exact "...འཇོམས་ཤིང་། གཡས་བསྐུམ་གཡོན་བརྐྱང་གི་ཞབས་ཀྱིས་མེ་འབར་...".
- Location 2 — § བསྡུས་དོན (summary, dharmabhadra/sungrab-tulku refs): reverted "...འཇོམས་ཤིང་གཡས་བསྐུམ་གཡོན་བརྐྱང་གི་ཞབས་ཀྱིས་མནན་ཏེ་མེ་འབར་..." back to the source's exact "...འཇོམས་ཤིང་གཡས་བསྐུམ་གཡོན་བརྐྱང་གི་ཞབས་ཀྱིས་མེ་འབར་..." (this instance carried no shad after འཇོམས་ཤིང in the source, so only the inserted verb was removed).

Both reversions restore the exact source wording for the affected clause (delete-only, no fresh rephrasing). `body-after.txt` was left untouched as the raw, unedited model output for the record; only `article.md` was corrected.

**Mechanical formatting defect (not a fact issue, fixed alongside the drift):** the blank line separating the § བསྡུས་དོན paragraph from the following `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` heading was dropped by the polish pass, leaving `...ཤིན་ཏུ་གསལ་ལོ།།== འབྲེལ་ཡོད་ཤོག་ངོས། ==` glued onto one line — every other heading in the file kept its `\n\n` separation, only this one collapsed. Left as-is, MediaWiki would not parse this as a heading. Restored the `\n\n` to match the source's spacing convention (source had a blank line at every heading boundary); article-preview.md was regenerated afterward and now shows all eight `==...==` headings on their own line.

No honorific-before-personal-name drift (the known 2026-08-21 pattern) was found: every personal name (ཡ་མ་བསོད་ནམས་, བསྟན་འཛིན་དོན་བཟང་, དཔལ་ལྡན་ཤེས་རབ་, སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ, ཚུལ་ཁྲིམས་རྣམ་དག, ཏཱ་ར་ནཱ་ཐ, དགེ་འདུན་གྲུབ, དྷརྨ་བྷ་དྲ, དཀོན་མཆོག་ཐབས་མཁས, བསྟན་དགའ) appears with the exact same title/epithet before and after.

## Verdict

PASS-after-reversion. Two instances of factual drift (an unattested "pressing/treading" action pulled from the adjacent verbatim quotation into the paraphrase) were found and surgically reverted to the source's exact wording in `article.md`. After reversion: no fact added, dropped, weakened, strengthened, or re-attributed; every ref remains attached to the same statement it supported before; all verbatim quotations are character-for-character identical; no honorific drift on any personal name. Several lexical-only substitutions (idiom/spelling/particle swaps) remain and are listed above for the domain expert's acceptance — they do not change any claim and do not block PASS.
