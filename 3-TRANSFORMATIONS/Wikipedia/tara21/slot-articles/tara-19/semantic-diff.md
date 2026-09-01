---
topic: tara-19
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-19/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-19

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Opening: this is the 19th of the 21-praise; root-verse quote (verbatim); all commentaries agree the object relied on by gods/kinnaras eliminates disputes and bad dreams via armor-splendor | Same | YES | verb `བཤད`→`བཞེད` (register swap); verbatim root-verse quote untouched |
| 2a | 4 different naming traditions seen; **no consensus among them** | 4 traditions "about"; no-consensus clause dropped | NO → reverted | Dropped scope-narrowing "མཐུན་སྒྲིག་མེད་དོ" + added hedge "ཙམ" (about four) — **reverted** to source wording |
| 2b | Yama Sönam + Gendün Drub: name from "burns and eliminates all suffering" | Same | YES | phrasing only |
| 2c | Tenzin Dhönzang: agrees on term "suffering," differs on "burn" vs "eliminate" wording | Same | YES | phrasing only |
| 2d | 3 khenpos: took "Mipham" as the term, named "Mipham Ziji-chen Gyalmo" | Same | YES | `མཉམ་དུ་བཟུང`→`གཙོར་བཟུང` — flagged, same referent |
| 2e | 4th tradition: no new name, identified by activity; Könchok Tabkhé + Sungrab Tulku concur; Dharmabhadra + Tenga Tulku concur; Gendün Drub concurs | Same | YES | phrasing only |
| 3a | Body color: all agree white; 1 face 2 hands agreement; two systems for hand/leg position | Same | YES | phrasing only |
| 3b | System 1 (Yama Sönam): seated on lotus+sun, holds fire-vessel at heart, backed by Nyima Bepa verse | Same | YES | phrasing only |
| 3c | System 2 (Palden Sherab + Sangye Nyentrul): Mipham Tsuktor Dukarmo, varada mudra right, white parasol atop utpala left | Same | YES | spatial "atop utpala" relation preserved; verb swap only |
| 3d | Sangye Nyentrul adds: vajra-fire sparks from parasol | Same | YES | phrasing only |
| 3e | Tsultrim Namdak: agrees on parasol; **the vajra-fire-spark detail is unclear/ambiguous** (mi gsal) | Detail said to be "not stated" (ma gsungs) — a stronger, different claim | NO → reverted | Hedge-to-definite drift — **reverted** to source wording "མི་གསལ" |
| 3f | Palden Sherab adds unique detail: 8 ornaments as armor, eliminates channel/wind/drop-disturbance dreams | Same | YES | phrasing only |
| 3g | Gendün Gyatso's text includes epidemic-eliminating words tied to 20th verse; likely a mix-up since no other text places them in the 19th | Same | YES | `བསྒྲེས་ཤོར`→`འདྲེས་ཤོར` — spelling/term normalisation, flagged, same meaning ("mixed-up error") |
| 4a | 16 commentaries agree: object of veneration is a goddess relied on by Indra/Brahma, ordinary gods, kinnara king Drönpa Tago etc. | Same | YES | phrasing only |
| 4b | Taranatha: "king" extends to cakravartins | Same | YES | phrasing only |
| 4c | Taranatha + Palden Sherab add mountain/tree/water deities to the list of venerators | Same | YES | phrasing only |
| 4d | Sungrab Tulku adds four-element deities; Tenzin Dhönzang extends to all 6 desire-realm classes + 17 form-realm abodes | Same | YES | phrasing only |
| 4e | Pema Namgyal: even the smallest dust of her feet is relied on by desire/form-realm king-gods and their retinues | Same | YES | phrasing only |
| 4f | Pema Namgyal: this also eliminates religious disputes, worldly litigation, and bad omens/dreams | Same | YES | phrasing only |
| 4g | 9 commentaries: "universal armor" = practitioner's mantra-mudra-body meditation armor | Same | YES | phrasing only |
| 4h | Tenzin Dhönzang elaborates: deity as yidam, body/speech/mind visualization + mantra recitation (verbatim mantra) eliminates disputes/bad dreams | Same | YES | mantra string character-for-character identical |
| 4i | Most commentaries: armor-splendor eliminates disputes/bad dreams; Drakpa Gyaltsen alone specifies it as tīrthika disputes; no other commentary so specifies | Same | YES | phrasing only |
| 4j | Tenzin Dhönzang cites an extra verse (protection from untimely death, spirits, fear) not found in any other guidance text | Same | YES | phrasing only |
| 5a | 9 commentaries: universal armor = practitioner's mantra/mudra armor; Yama Sönam disagrees explicitly | Same | YES | phrasing only |
| 5b | Yama Sönam: "armor" = the joy from venerating the goddess herself, not meditation-practice; backed by a Nyima Bepa verse (3 realms' rulers venerate) | Same | YES | phrasing only |
| 5c | Könchok Tabkhé cites a near-identical verse but attributes it to an unnamed siddha, omitting Nyima Bepa's name; admits no other commentary explains these lines this way | Same | YES | phrasing only |
| 5d | Whether the two verses share the same name/author is unclear from any source | Same | YES | "མཚན" made explicit as "མཛད་པ་པོའི་མཚན" (author's name) — clarifying, same referent already established by context, flagged |
| 5e | Two traditions of profound-meaning explanation exist | Same | YES | phrasing only |
| 5f | Taranatha (verbatim quote on ལྷ etymology) breaks the verse into 5-fold meaning (host/king/armor/dispute-clearing/dream-clearing) | Same | YES | verbatim quote untouched; sentence restructured into parallel clauses, same 5-fold content |
| 5g | Palden Sherab: marked-completion-stage reading (verbatim channel quote) — armor = 4 joys' 4 concealments, clearing = channel/wind/drop obstacles; unmarked-completion-stage reading: king = guru-introduced awareness, armor = primordial liberation of the six-collection's appearances | Same | YES | verbatim quote untouched; phrasing only |
| 5h | Taranatha's and Palden Sherab's profound explanations do not agree on a single word — do not mutually support each other | Same | YES | phrasing only — this key divergence statement is fully preserved |

## Ref attachment walk

Every `<ref name="...">` / self-closing `<ref name="..." />` token was checked against the statement immediately preceding it in both before/after texts.

- `taranatha`, `sungrab-tulku`, `tenzin-dhonzang` (opening) — same statement (source/attribution of the 19th praise + root verse). YES
- `yama-sonam` (×6 occurrences) — each still attached to the same clause it supported before (naming tradition 1, body-system 1, veneration list, profound-meaning disagreement). YES
- `gendun-drub` (×2) — naming tradition 1 concurrence, and 4th-tradition concurrence. YES
- `dharmabhadra` (×2) — naming-tradition concurrence, 4th-tradition concurrence, universal-armor citation. YES
- `karma-maitri` — opening citation list. YES
- `palden-sherab` (×7) — naming tradition, body-system 2, vajra-fire detail, 8-ornament detail, veneration list, profound-meaning (marked/unmarked completion stage). YES
- `sangye-nyentrul` (×3) — body-system 2, vajra-fire-spark addition. YES
- `tsultrim-namdak` — parasol agreement / vajra-fire-spark unclear-detail sentence (reverted span). YES
- `konchok-thabkhe` (×2) — 4th naming tradition, "similar verse, no name given" sentence. YES
- `tenga-tulku` — 4th naming tradition concurrence. YES
- `gendun-gyatso` (×2) — the epidemic-verse / mix-up sentence. YES
- `taranatha` (later, ×3) — "king" extended to cakravartins, mountain/water deities, profound 5-fold breakdown quote. YES
- `sungrab-tulku` (later) — four-element deities. YES
- `tenzin-dhonzang` (later, ×4) — 6-class/17-abode extension, universal-armor elaboration + mantra, extra protection verse. YES
- `pema-namgyal` (×2) — smallest-dust veneration, dispute/omen elimination. YES
- `lobsang-dawa` — universal-armor citation list. YES
- `drakpa-gyaltsen` — tīrthika-dispute specification. YES

No ref migrated to a different clause; all refs support the identical statement before and after.

## Flagged substitutions

Lexical-only swaps, same referent/meaning — do not block PASS:

| Location | Before | After |
|---|---|---|
| Opening sentence | ...ཐམས་ཅད་ཀྱིས་མཐུན་པར་**བཤད**།། | ...ཐམས་ཅད་**མཐུན་པར་བཞེད་དོ**།། |
| §1 naming, 3 khenpos | ཐ་སྙད་**མཉམ་དུ་བཟུང་**སྟེ | ཐ་སྙད་**གཙོར་བཟུང་**སྟེ |
| §1 naming, 4th tradition | ལས་ཀྱི་ངོས་ནས་ཁ་གསལ་བ | ཕྲིན་ལས་ཀྱི་སྒོ་ནས་ངོས་འཛིན་པ |
| §2 body, verb register | འཛིན་པར་བཤད / སྐུར་བཤད་དེ | བསྣམས་པར་གསུངས / སྐུར་བཞེད་དེ |
| §2 body, Gendün Gyatso sentence | **བསྒྲེས་ཤོར** (likely OCR/spelling artifact) | **འདྲེས་ཤོར** ("mixing-up error" — coherent standard term, same intended meaning) |
| §3 profound-meaning, authorship line | ...གང་གཅིག་**ཡིན་མིན** | ...**མཛད་པ་པོའི་མཚན** གཅིག་ཡིན་མིན (made the already-contextually-clear referent — "the author's name" — explicit) |
| Throughout | verbs `བཤད་`/`བཀོད་` (says/posits) | honorific-register verbs `བཞེད་`/`གསུངས་`/`མཛད་` (holds/states — honorific register consistently applied to all commentators, not selectively to one name) |

None of these change which commentator holds which position, which fact is asserted, or the target of a citation.

## Reverted drift

Two spans reverted to the source article's exact wording (surgical reversion, Rule 8a). `body-after.txt` is left untouched as the raw model record; only `article.md` was restored.

1. **§ མཚན་གྱི་ངེས་ཚིག, opening clause.** Gemini's output dropped the source's explicit no-consensus statement and added an unsupported "about" hedge on the count of naming traditions:
   - Model output: `...བཤད་སྲོལ་མི་འདྲ་བ་བཞི་ཙམ་མཆིས་ཏེ།` (there exist about four different traditions)
   - Reverted to source: `...བཤད་སྲོལ་མི་འདྲ་བ་བཞི་མཐོང་སྟེ་མཐུན་སྒྲིག་མེད་དོ།` (four different traditions are seen, and there is no consensus among them)
   - This is drift pattern (e) — a dropped scope-narrowing qualifier — the explicit "no consensus" claim is a divergence-tracking statement this vault treats as load-bearing (CLAUDE.md §8, "no consensus flattening").

2. **§ སྐུ་ཡི་རྣམ་པ, Khenpo Tsultrim Namdak's vajra-fire-spark sentence.** Gemini's output turned a hedged/ambiguous claim into a definite negative claim:
   - Model output: `...རྡོ་རྗེའི་མེའི་ཚྭ་ཚྭ་འཕྲོ་བའི་ཞིབ་ཆ་ནི་མ་གསུངས་སོ།།` ("...the detail is not stated")
   - Reverted to source: `...རྡོ་རྗེའི་མེའི་ཚྭ་ཚྭའི་ཞིབ་ཆ་མི་གསལ།` ("...the detail is unclear")
   - This is drift pattern (d) — a qualifier that turns a plain (hedged/ambiguous) statement into a stronger, unsupported claim (definite absence).

## Verdict

**PASS-after-reversion.** No fact was added, dropped, changed, or re-attributed except the two spans above, both surgically reverted to the source article's exact wording. Every `<ref>` remains attached to the identical statement it supported before polishing. All verbatim quotations (root-verse praise, Taranatha's etymology quote, Palden Sherab's channel-verse quote, the mantra string) are character-for-character identical to the source. No unattested honorific was inserted before any personal name — the honorific-register verb shift (བཤད→བཞེད/གསུངས/མཛད) is applied uniformly across all named commentators, consistent with the source's own register, not selectively to one name. Length delta: tsheg count 1855 → 1932 (+4.15%).
