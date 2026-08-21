---
topic: tara-03
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-03/article.md
model: gemini-3.1-pro-preview
date: '2026-08-21'
verdict: FAIL
status: draft
---

# Semantic diff — tara-03

## W1 warning resolution

`gemini-report.md` flagged two W1 warnings (paragraph not ending `།།`):

- **paragraph 2** — ends `…བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ།"` — this is the root-verse quotation block (ref `yama-sonam`), a standalone verse-quote paragraph that ends on the verse's own internal punctuation followed by a closing straight quote mark, not on freestanding prose. **False positive** — type (b), a closing-quote-mark paragraph. Verbatim quotation is byte-identical to the source (confirmed by C3 pass and by direct comparison below).
- **paragraph 9** — ends `…བཅུའོ། ། ཞེས་གསུངས།"` — same pattern: the "ཉི་མ་སྦས་པ" verse citation block (ref `yama-sonam`), a standalone quote paragraph closing on `"` after the verse's own shad. **False positive**, same type (b).

Both resolved as false positives; no re-run needed for W1.

## Sentence-by-sentence comparison

| # | Paragraph (before, gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: Tara Serdokchen is the mchod-brjod of the 3rd [homage] in the Praise to 21 Taras (refs yama-sonam, gendun-gyatso, taranatha) | Same, "third" made explicit as "third ཕྱག་འཚལ" | Yes | Explicitation, not new info — document is titled ཕྱག་འཚལ་ཉེར་གཅིག |
| 2 | Root-verse quotation ("ཕྱག་འཚལ་སེར་སྔོ...") | Byte-identical quotation | Yes | Verbatim, C3-confirmed |
| 3 | Gloss: lotus adorns hand; deity is object/domain of the 6 perfections (refs dharmabhadra, palden-sherab) | Same gloss, added རྣམ་པར echoing the verse's own wording | Yes | Stylistic echo of P2's verse |
| 4 | **མཚན་གྱི་ངེས་ཚིག**: Tenzin Dhonzang glosses ཕྱག (clears obstacles to *dge-dbang*/virtue-power) and འཚལ (gathers favorable conditions); other commentaries read ཕྱག་འཚལ་བ as mere respectful bowing (refs tenzin-dhonzang, sungrab-tulku) | Same two positions, same terms | Yes | **Scrutinised specifically for the དགེ་དབང་→དགེ་སྦྱོར་ substitution flagged in the prior smoke test — does NOT recur here.** `དགེ་དབང་` is preserved unchanged in this fresh run; only `ཞེས`→`ཅེས` (particle allomorph) changed |
| 5 | Disagreement on "གསེར་སྔོ" spelling (ག-prefixed vs unprefixed); Konchok Thabkhe: uncertain on prefix, relies on Jowo/Drupchen's lung (refs dharmabhadra, palden-sherab, sungrab-tulku, yama-sonam, tenzin-dhonzang, tsultrim-namdak, konchok-thabkhe) | Same positions, same 7 refs, same order | Yes | Minor simplification of connective |
| 6 | Gendun Drub: "སྔོ་བ"=body color, "སེར"=clear color, hence "Serdokchen" epithet; Tenzin Dhonzang's commentary uses this as alt-name (refs gendun-drub, tenzin-dhonzang) | Same | Yes | Punctuation only |
| 7 | Body color: gold with slight blue tinge; hand-item (ཕྱག་གི་མཚོན་ཆ) = water-born lotus/blue utpala; ten [commentaries] say held in left hand, five say petals open toward the ear (refs yama-sonam, dharmabhadra, karma-maitri, drakpa-gyaltsen, gendun-drub, lobsang-dawa, palden-sherab, tenga-tulku, sungrab-tulku) | Same facts; `ཕྱག་གི་མཚོན་ཆ`→`ཕྱག་མཚན` (see flagged substitutions) | Yes | Term-choice flag, same referent |
| 8 | Yama Sonam's commentary gives an expanded 1-face-10-arm form: seated **on the multicolored lotus, which sits atop the sun-disc seat**; 5 right hands hold rosary/sword/arrow/vajra/hook-goad; 5 left hold streamer/lasso/lotus/bell/bow, vajra posture (ref yama-sonam) | Same form and implements, BUT seated **on the sun-disc seat, which sits atop the multicolored lotus** — the nesting of the two seat elements is reversed | **NO** | **FACTUAL DRIFT — see verdict** |
| 9 | "ཉི་མ་སྦས་པ" verse citation (ref yama-sonam) | Byte-identical | Yes | Verbatim, C3-confirmed |
| 10 | Other commentaries give no count for faces/arms; this expanded form is unique to Yama Sonam's commentary | Same, reworded ("ལུང་མི་སྟོན"→"ལུང་བསྟན་མེད"), "འདི" added for deixis | Yes | Paraphrase only |
| 11 | Deity arises from/is essence of the 6 perfections; Taranatha details how mastery of the 6 perfections makes them her domain (refs yama-sonam, dharmabhadra, taranatha) | Same | Yes | Punctuation only |
| 12 | "དཀའ་ཐུབ" glossed as ཚུལ་ཁྲིམས (discipline — hard-to-keep-but-kept); Drakpa Gyaltsen: དཀའ་ཐུབ = the 8 disciplines, in brief (refs yama-sonam, gendun-drub, tenzin-dhonzang, drakpa-gyaltsen) | Same | Yes | Added quotative ཅེས, no meaning change |
| 13 | Sungrab Tulku & Tenga Tulku: the 6 perfections pair 1-to-1 as antidotes to the 6 afflictions — generosity/miserliness, diligence/laziness, discipline/immorality, wisdom/delusion, patience/anger, concentration/distraction (refs sungrab-tulku, tenga-tulku) | Same 6 pairs, same order, same pairing; list re-punctuated with shad instead of དང (no-comma contract) | Yes | Verified pairing preserved exactly |
| 14 | Konchok Thabkhe: this ordering of the 6 perfections differs slightly from the well-known order — first 3 = merit accumulation, last = wisdom accumulation, diligence spans both hence placed first (ref konchok-thabkhe) | Same | Yes | Paraphrase only |
| 15 | 3 commentaries give secret-meaning readings that don't contradict each other, only differ in approach | Same | Yes | Punctuation only |
| 16 | Palden Sherab: 4-stage explanation — brief gloss + 6-pāramitā/10-power overview; generation-stage visualization; completion-stage (lotus/vajra union, signed); signless ultimate (6 pāramitās perfect simultaneously as Samantabhadrī); sūtra citation on non-observation (ref palden-sherab) | Same 4 stages, same content and order | Yes | `སྐད་ཅིག`→`ཅུང་ཟད` ("briefly"), `ཆིག་ཆར`→`ཅིག་ཅར` (spelling) |
| 17 | Taranatha: secret meaning via lotus/vajra union — discipline(austerity), bliss(meditation), wisdom(emptiness), diligence, patience, generosity accomplished separately, concluding with mantra conduct (ref taranatha) | Same list, same order | Yes | Punctuation/verb-form only |
| 18 | Sangye Nyentrul: generation-stage visualization on an utpala-borne wish-granting jewel radiating light; terminology matches Palden Sherab's generation-stage but independently worded (ref sangye-nyentrul) | Same | Yes | Punctuation only |
| 19 | Numbering: most commentaries count this as verse "3"; 4 commentaries count it "2" within a body-color/hand-attribute/cause sub-grouping, not counting within all 21 (refs yama-sonam, taranatha, palden-sherab, dharmabhadra, gendun-drub, lobsang-dawa) | Same | Yes | Spelling variant, added noun ཚུལ |
| 20 | Body color: Konchok Thabkhe, Palden Sherab, Sangye Nyentrul (3, bold) say body = gold[-colored], only the flower blue; Taranatha's [opening text / word-commentary] say gold+blue = stem-color+petal-color, doesn't differentiate body color; Tsultrim Namdak: mixed blue-gold = green body; Gendun Gyatso: body slightly reddish; Tenzin Dhonzang: body slightly blue-green (refs konchok-thabkhe, palden-sherab, sangye-nyentrul, taranatha, tsultrim-namdak, gendun-gyatso, tenzin-dhonzang) | Same 5 positions, same names (bold spans unchanged, C7-confirmed), same refs | Yes | See flagged substitutions (མཚོན་ཆ term unrelated here; two flagged items: `གསེར`→`གསེར་མདོག`, `སྡོང་མདོག...འདབ་མའི་མདོག`→`སྡོང་པོ...འདབ་མའི་མདོག`) |
| 21 | ཞི་བ ("pacification/peace") term: most read as wisdom or wisdom's pacifying action; Drakpa Gyaltsen & Gendun Gyatso: general "pacifies afflictions"; Gendun Drub: pacifies 6 specific opposites (miserliness, laziness, immorality, anger, distraction, wrong view — exact list); Tenga Tulku: undefiled-by-fault reading, 6 perfections each undefiled by their fault; Konchok Thabkhe: earlier commentaries link pacification+domain separately to wisdom; Yama Sonam: divergence exists even within his own text (refs yama-sonam, dharmabhadra, palden-sherab, drakpa-gyaltsen, gendun-gyatso, gendun-drub, tenga-tulku, konchok-thabkhe) | Same positions, same 6-item list in the same order, same names/refs | Yes | Spelling variants only (`ཞིག`→`ཤིག`, `འགྲེལ་བས`→`འགྲེལ་པས`) |
| 22 | Alternate substitution scheme: Gendun Gyatso: "or" — 6 perfections fulfilled via 4 factors (renunciation of affliction, patience, concentration, reality-domain wisdom); Konchok Thabkhe: this deity IS the wisdom-pāramitā itself, other 5 are her domain/basis; Tsultrim Namdak: elsewhere explains a metrically-matching line via the 37 factors, notes 2 systems exist even within his own text (refs gendun-gyatso, konchok-thabkhe, tsultrim-namdak) | Same | Yes | `འམ`→`ལམ` (disjunctive-particle allomorph, same meaning "or") |
| 23 | Summary: all commentaries agree deity = lotus-adorned, 6-pāramitā-domain goddess; divergence on gold/blue color-order, on whether "gold-blue" marks body-color or just the flower, and on whether "ཞི་བ" marks wisdom or a pacifying-action, "very clear" (refs dharmabhadra, palden-sherab, yama-sonam, konchok-thabkhe, taranatha, gendun-drub, tenga-tulku) | Same | Yes | `ཉིན་གསལ་ལོ`→`ཤིན་ཏུ་གསལ་ལོ` idiom swap (flagged) |

## Ref attachment walk

All 81 ref occurrences were checked against the paragraph they close in both texts. Grouped by first appearance (a repeated `<ref name="x" />` always closes the same clause-final position in both versions unless noted):

| Ref | Statement it supports (before) | Statement it supports (after) | Same statement? |
|---|---|---|---|
| yama-sonam | P1 lead; P2 verse; P3 gloss; P5 spelling; P7 body/hand-item; **P8 expanded 10-arm form incl. seat-stacking**; P9 verse; P11 origin; P12 discipline gloss; P17(none)/P19 numbering; P21 own-text divergence; P23 summary | identical positions in every case | Yes, except **P8**: ref still closes the same sentence, but that sentence's seat-stacking claim has changed (see verdict) — a case of the supported *statement* drifting under a stationary ref, not ref migration |
| gendun-gyatso | P1 lead; P20 reddish-body; P21 general-pacification; P22 4-factor alt scheme | identical | Yes |
| taranatha | P1 lead; P11 mastery-of-6-perfections; P17 secret meaning; P19 numbering; P20 stem/petal color; P23 summary | identical | Yes |
| dharmabhadra | P3 gloss; P5 spelling; P7 body color; P11 origin; P21 general reading; P23 summary | identical | Yes |
| palden-sherab | P3 gloss; P5 spelling; P7 hand-item; P16 4-stage explanation (×4 uses); P19 numbering; P20 body=gold; P21 general reading; P23 summary | identical | Yes |
| tenzin-dhonzang | P4 ngestsig gloss; P5 spelling; P6 alt-name; P12 discipline gloss; P20 blue-green body | identical | Yes |
| sungrab-tulku | P4 alt gloss; P5 spelling; P7 petals-toward-ear; P13 antidote pairing (×2) | identical | Yes |
| konchok-thabkhe | P5 uncertain-prefix; P14 ordering; P20 body=gold; P22 wisdom-pāramitā; P23 summary | identical | Yes |
| gendun-drub | P6 epithet gloss; P7 held-in-left-hand; P12 discipline gloss; P19 numbering; P21 6-opposites list; P23 summary | identical | Yes |
| karma-maitri | P7 body color | identical | Yes |
| drakpa-gyaltsen | P7 hand-item; P12 8-disciplines; P21 general reading | identical | Yes |
| lobsang-dawa | P7 held-in-left-hand; P19 numbering | identical | Yes |
| tenga-tulku | P7 petals-toward-ear; P13 antidote pairing; P21 undefiled reading; P23 summary | identical | Yes |
| sangye-nyentrul | P18 generation-stage visualization; P20 body=gold | identical | Yes |
| tsultrim-namdak | P5 spelling; P20 mixed-color=green; P22 37-factors alt reading | identical | Yes |

No ref was found re-attached to a different claim than before. The one substantive issue is internal to the statement a stationary ref closes (P8), not a migration.

## Flagged substitutions

Per Rule 8, these are same-referent, arguably-same-meaning changes — recorded for the domain expert to accept or reject; none by itself changes a fact:

| # | Location | Before | After | Type |
|---|---|---|---|---|
| 1 | P1 lead | `ནང་གསུམ་པའི་མཆོད་བརྗོད` | `ནང་གི་ཕྱག་འཚལ་གསུམ་པའི་མཆོད་བརྗོད` | Explicitation — makes the elided noun (ཕྱག་འཚལ) explicit |
| 2 | P3 gloss | `ཕྱག་བརྒྱན་ཞིང` | `ཕྱག་རྣམ་པར་བརྒྱན་ཅིང` | Adverb addition + particle change, echoes the verse's own wording |
| 3 | P4 ངེས་ཚིག (the passage specifically flagged for scrutiny) | `ཕྱག་ཞེས་པས` | `ཕྱག་ཅེས་པས` | Particle allomorph (ཞེས/ཅེས) — **`དགེ་དབང་` itself is unchanged; the prior smoke test's དགེ་སྦྱོར་ substitution does NOT reproduce in this run** |
| 4 | P5 | `དཀོན་མཆོག་ཐབས་མཁས་ན་རེ` | `དཀོན་མཆོག་ཐབས་མཁས་ཀྱིས` | Quotative → agentive particle, same attribution |
| 5 | P7 | `ཕྱག་གི་མཚོན་ཆ` ("hand-weapon") | `ཕྱག་མཚན` ("hand-attribute/emblem") | Term generalization — same referent (the lotus/utpala), but the specific-to-generic register shift is worth a domain-expert glance since the object described is a flower, not a weapon |
| 6 | P16 | `སྐད་ཅིག་བཤད` | `ཅུང་ཟད་བཤད` | Near-synonym ("momentarily" vs "a little"), both = "briefly" |
| 7 | P16 | `ཆིག་ཆར` | `ཅིག་ཅར` | Spelling variant, same word "simultaneously" |
| 8 | P17 | `མཇུག་བསྡུའོ` | `མཇུག་བསྡུས་སོ` | Verb-form variant, same meaning "concludes" |
| 9 | P19 | `གྲངས་པ` | `བགྲངས་པ` | Spelling variant, "counted" |
| 10 | P20 | `སྐུ་ནི་གསེར་ཙམ་དུ` | `སྐུ་ནི་གསེར་མདོག་ཙམ་དུ` | Clarifying addition of མདོག ("-colored") — contextually redundant since paragraph topic is already སྐུ་མདོག (body color) |
| 11 | P20 | `འི་མགོ་གི་བཤད་པ` | `འི་ཐོག་མའི་བཤད་པ` | Synonym, "opening" vs "initial" exposition |
| 12 | P20 | `མེ་ཏོག་གི་སྡོང་མདོག་དང་འདབ་མའི་མདོག` | `མེ་ཏོག་གི་སྡོང་པོ་དང་འདབ་མའི་མདོག` | Ellipsis of the repeated head noun མདོག on the first coordinate — Tibetan distributes the trailing modifier across `དང`-joined nouns, so the two-color claim (stem-color, petal-color) is recoverable, but flagged since it is a technical claim worth a native-reader check |
| 13 | P21 | `ངེས་གྲངས་ཞིག` | `ངེས་གྲངས་ཤིག` | Spelling allomorph |
| 14 | P22 | `སྤྱོད་ཡུལ་འམ་བརྟེན་གནས་སུ` | `སྤྱོད་ཡུལ་ལམ་བརྟེན་གནས་སུ` | Disjunctive-particle allomorph (འམ/ལམ), same "or" |
| 15 | P23 | `ཉིན་གསལ་ལོ` | `ཤིན་ཏུ་གསལ་ལོ` | Idiom swap: "clear as day" → "extremely clear" |

**15 flagged substitutions total.** None independently alters a fact; #5 and #12 are the two worth the closest domain-expert look since they touch technical/iconographic wording (hand-item register; the two-color stem/petal claim).

## Verdict

**FAIL** — one factual drift found, isolated to paragraph 8 (== སྐུ་ཡི་རྣམ་པ། ==, Yama Sonam's expanded ten-arm form, ref `yama-sonam`):

- Before: `...ཉི་མའི་གདན་གྱི་སྟེང་གི་སྣ་ཚོགས་པད་མའི་སྟེང་དུ་བཞུགས་ཤིང...` — deity seated **atop the multicolored lotus, which itself rests atop the sun-disc seat** (stacking, bottom→top: sun-disc, lotus, deity).
- After: `...སྣ་ཚོགས་པད་མའི་སྟེང་གི་ཉི་མའི་གདན་ལ་བཞུགས་ཤིང...` — deity seated **atop the sun-disc seat, which itself rests atop the multicolored lotus** (stacking, bottom→top: lotus, sun-disc, deity).

The two seat elements (ཉི་མའི་གདན and སྣ་ཚོགས་པད་མ) have been swapped in their nesting relationship. This is not a wording variant — it changes which object the deity is described as sitting directly upon, and which object is below which, in a physical/iconographic description explicitly attributed to Yama Sonam's commentary (ref intact, same sentence position, but the claim itself is altered). Per Rule 8 this is factual drift, not a flaggable lexical substitution, regardless of whether the "after" phrasing happens to match the more conventional lotus-under-disc iconographic convention — the model was not authorized to correct content toward its own knowledge of standard iconography (explicitly prohibited by the prompt's constraints), only to restyle.

No other fact, name, number, doctrinal position, or quotation was added, dropped, weakened, strengthened, or re-attributed anywhere else in the article. All 15 headings unchanged (C2), all verbatim quotations byte-identical (C3, and independently re-confirmed above for both quote blocks), all bold author-name spans unchanged (C7), all 81 ref tokens preserved in position and count.

**Recommendation:** re-run the polish script once for a fresh sample (Rule 8) and re-diff paragraph 8 specifically before this pilot is considered for adoption; do not carry the current P8 wording into any in-place replacement without a fix. The rest of the polished article shows no drift and reads as a clean restyling pass.
