---
topic: mudra
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/mudra/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — mudra

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: "mudra" refers to the hand gesture in the ninth-prostration verse (quote unchanged); all sixteen commentaries identify this mudra as symbolizing the Three Jewels. | Same two claims, same refs (sungrab-tulku, yama-sonam). | YES | བརྗོད་པ་ཡིན→བརྗོད་དོ, ངོས་འཛིན་བྱེད→ངོས་འཛིན་མཛད (honorific register only) |
| 2 | ངེས་ཚིག: hand arrangement per quoted passage (verbatim quote), refs yama-sonam/drakpa-gyaltsen/karma-maitri. | Identical quote, identical refs. | YES | ཡིན→རོ ending only |
| 3 | Sungrab Tulku's variant: thumb+middle finger hold the utpala stem (instead of thumb+ring finger), index/ring/little finger raised. | Same variant, same ref. | YES | ནི dropped, བཤད་དོ→གསུངས་སོ (register) |
| 4 | Right hand's supreme-giving mudra: wheel-of-a-thousand-spokes mark in the middle of the palm (ཕྱག་ལག་དཀྱིལ་མར), its light dispels the eight/sixteen fears; detail on the wheel deferred to [[འཁོར་ལོ་]]. | Same claim, same ref and wikilink; palm location worded ཕྱག་མཐིལ་དུ ("in the palm") instead of ཕྱག་ལག་དཀྱིལ་མར ("in the middle of the hand"). | YES | Flagged substitution — see below |
| 5 | དབྱེ་བ: the mudra pair is used beyond the ninth prostration, in other deities' sādhanas; Khenchen Palden Sherab composed (བརྩམས) generation-stage visualizations for each of the 21 emanations "by way of the basis of" (ཐོག་མའི་སྒོ་ནས) the 21 prostrations, reusing the same mudra-pair frame; Khenpo Tsultrim Namdak likewise reused the pair. | Same claims, same refs; "composed" → "taught/stated" (གསུངས), "ཐོག་མའི་སྒོ་ནས" → "སྒོ་ནས" (basis-marker trimmed). | YES | Flagged substitution — see below; referent (Palden Sherab's 21-emanation scheme, reusing the mudra pair) unchanged |
| 6 | Reasons for symbolizing the Three Jewels: Yama Sonam (Buddha+Dharma jewels produce it, Sangha sustains the activity); Tenzin Dhonzang (three fingers on own heart = all-three-times buddhas); Konchok Thabkhe (citing Gedun Drup's White Tara praise, mudra = all Three Jewels gathered). | Same three positions, same refs, same attributions. | YES | Particle/verb register only |
| 7 | Taranatha's distinct reading: quote (verbatim) identifying the mudra as Tara's own samaya-mudra; distinct hand arrangement (palms joined, etc. — full description); Bhagavati herself shown bound by this mudra as the karmic seed of blessing. | Identical quote, identical description, identical refs, epithet བཅོམ་ལྡན་འདས་མ unchanged. | YES | ལྷ་མོའི་ཉིད→ལྷ་མོ་ཉིད (deity epithet form) — flaggable, not drift |
| 8 | Yama Sonam notes commentators disagree on the light's source (palm-wheel vs. body-light); he himself holds the body-light position. | Same disagreement, same two positions, same final stance attributed to Yama Sonam. | YES | བཤད་དོ→བཞེད་དོ ("stated"→"holds/asserts", honorific register) |
| 9 | Taranatha and Palden Sherab agree on a completion-stage hidden meaning: Three Jewels = the three substances (semen/blood/wind), gathered by the three fingers at the heart-cakra hub. | Identical claim, identical refs. | YES | Grammar particles only |
| 10 | Armor function: mantra+mudra as protective armor — binds the three doors, blazes with power, dispels bad omens/harm/disputes day and night; same armor also used for White-Parasol-Tara; full detail deferred to [[སྔགས་]]. | Identical claims, identical refs and wikilink. | YES | Sentence-boundary/particle only |
| 11 | Summary: all sixteen commentaries say something about mudra; both ninth-prostration mudras are *definitely* (ངེས་པར) identified as Three-Jewels symbols, but commentaries differ on hand arrangement, reasons for the Three-Jewels symbolism, and hidden-meaning readings. | Same summary, same refs; "ངེས་པར" (definitely/certainly) dropped from the identification clause. | YES | Flagged substitution — see below |

## Ref attachment walk

Every `<ref>` was checked against the clause it sits on in both versions.

| ref name | Statement supported (before) | Statement supported (after) | Same? |
|---|---|---|---|
| sungrab-tulku | Root-verse quote; Sungrab Tulku's finger-variant; right-hand wheel-mark and its effect; DBYE-BA pair-reuse claim | Same four attachments | YES |
| yama-sonam | Sixteen-commentary identification; hand-arrangement quote; DBYE-BA pair-reuse; Three-Jewels cause/effect reasoning; light-source disagreement + own position; summary line | Same six attachments | YES |
| drakpa-gyaltsen | Hand-arrangement quote (co-cite) | Same | YES |
| karma-maitri | Hand-arrangement quote (co-cite) | Same | YES |
| palden-sherab | DBYE-BA 21-emanation scheme; completion-stage hidden meaning (co-cite); armor function (co-cite); armor/White-Parasol-Tara parallel | Same four attachments | YES |
| tsultrim-namdak | DBYE-BA pair-reuse (Tsultrim Namdak); armor function (co-cite) | Same | YES |
| tenzin-dhonzang | Three-fingers/three-times-buddhas reasoning | Same | YES |
| konchok-thabkhe | Gedun Drup citation / Three-Jewels-gathered reasoning | Same | YES |
| taranatha | Samaya-mudra reading + quote; hand-arrangement description; Bhagavati-bound-by-mudra claim; completion-stage hidden meaning (co-cite); armor function (co-cite); summary line | Same six attachments | YES |

No ref migrated to a different clause.

## Flagged substitutions

Lexical-only swaps — same referent/meaning, listed for domain-expert review; none block PASS.

| Location | Before | After | Note |
|---|---|---|---|
| Right-hand mudra location (ངེས་ཚིག §, sentence 4) | ཕྱག་ལག་དཀྱིལ་མར ("in the middle of the hand") | ཕྱག་མཐིལ་དུ ("in the palm") | Both denote the palm surface where the wheel-mark sits; no change to the iconographic claim itself |
| Palden Sherab's authorship verb (དབྱེ་བ §, sentence 5) | བརྩམས་ ("composed") | གསུངས་ ("taught/stated") | Register/verb shift; underlying claim (Palden Sherab built the 21-emanation generation-stage scheme reusing the mudra pair) is unchanged in both |
| Basis-marker (དབྱེ་བ §, sentence 5) | ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཐོག་མའི་སྒོ་ནས ("by way of the basis of the 21 prostrations") | ཕྱག་འཚལ་ཉེར་གཅིག་གི་སྒོ་ནས ("by way of the 21 prostrations") | Idiom trimmed; same referent (the 21-prostration framework) |
| Deity epithet (གཞུང་ལུགས་སོ་སོའི་བཤད་པ §, Taranatha paragraph) | ལྷ་མོའི་ཉིད་ཀྱི ("of the goddess's own") | ལྷ་མོ་ཉིད་ཀྱི ("of the goddess herself") | Epithet form of the deity herself — explicitly a flaggable substitution per Rule 8, not drift |
| Yama Sonam's own-position verb (གཞུང་ལུགས་སོ་སོའི་བཤད་པ §, sentence 8) | བཤད་དོ ("stated") | བཞེད་དོ ("holds/asserts") | Honorific register shift for expressing one's own view; same stance attributed to the same person |
| Certainty marker (བསྡུས་དོན §, sentence 11) | ངེས་པར ངོས་འཛིན་བྱེད་ ("*definitely* identify") | ངོས་འཛིན་མཛད ("identify") | Emphasis/intensifier dropped; the identification claim itself (both ninth-prostration mudras = Three-Jewels symbols) is asserted in both versions, only the added certainty adverb is gone |

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** Walked all eleven paragraph units and all nine distinct `<ref>` names: no fact was added, dropped, strengthened, weakened, or re-attributed to a different commentator; every ref remains attached to exactly the statement it supported before. All four verbatim quotations (root verse in the lead, hand-arrangement description in ངེས་ཚིག, Taranatha's samaya-mudra line, and the shared hand-arrangement quote) are character-for-character identical to the source. No unattested honorific was inserted before any personal name (Yama Sonam, Taranatha, Palden Sherab, Tsultrim Namdak, Tenzin Dhonzang, Konchok Thabkhe, Sungrab Tulku, Drakpa Gyaltsen, Karma Maitri, Gedun Drup all appear with the same title/name forms as the source). The six items in the Flagged substitutions table are lexical/register-only swaps that a domain expert may accept or reject but do not affect factual content. Hard checks C1–C7 passed on the first attempt with 0 warnings (see `gemini-report.md`). Body length dropped by 1.01% tsheg-count, consistent with tighter, more idiomatic prose rather than content loss.
