---
topic: vayu
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/vayu/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — vayu

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Vayu-deity appears in all 16 commentaries on the Twenty-One Praises as a worldly deity. | Same. | YES | verbatim, unchanged |
| 2 | Root verse quote (Indra, fire-god, Brahma, sna-tshogs-dbang-phyug, etc. worshipped alongside Tara); vayu is part of that group of deities; 15 commentaries also identify it as a NW guardian. | Same; verse quote character-for-character identical; same 4-deity list (order/particles reworded, count unchanged); same "15 commentaries → NW guardian" claim. | YES | style only (དང་ chain → བཅས་; བྱེད→མཛད honorific) |
| 3 | Two commentaries: via mantra's hidden meaning, vayu also symbolizes the wind element. | Same claim, same 2 commentaries (taranatha, palden-sherab refs unchanged). | YES | particle/verb rewording only |
| 4 | Three commentaries explain vayu's distinguishing features separately; did not converge on one identification. | Same. | YES | ངོས་འཛིན་གཅིག་ཏུ→གཅིག་མཐུན་དུ, same meaning |
| 5 | Yama Sonam names vayu "NW guardian vayu-of-various-kinds, having various mounts" (verbatim quote). | Same, quote identical, name unchanged (no honorific added). | YES | — |
| 6 | Taranatha identifies vayu as the one who fashions (གཟོ་བཀོད) the abodes/arrangement of the world. | Gemini's raw output silently changed གཟོ་བཀོད → བཟོ་བཀོད (a plausible-looking "correction" of the source spelling). **Flagged as drift and surgically reverted** — see § Reverted drift. Post-reversion: identical to source. | YES (after reversion) | see Reverted drift |
| 7 | Zurmang Khenpo Pema Namgyal: vayu has the power to shake the three realms of existence. | Identical, byte-for-byte. | YES | unchanged |
| 8 | Two commentaries place vayu not as a worshipper of Tara but as one of the ten directional guardians (of earth-protectors), drawn/summoned by light rays of the seed-syllable TAM at her heart, to be used as a servant for enacting activity. | Same claim; "TAM" → "the syllable TAM" (ཡིག་ added) — same referent (seed-syllable), flagged as lexical addition, not drift. | YES | flagged substitution: TAM → "syllable TAM" |
| 9 | Dorje Lobpön Tengatrul: vayu placed in NW among ten directional guardians, accomplishes all assigned tasks. | Same, name unchanged. | YES | — |
| 10 | Sermé Tsang Geshe Tenzin Dhonzang: also explained as similarly able to be summoned/employed as a servant for enacting activity. | Same claim (comparison to preceding servant-role description); "ནུས་པའི་མར་མཚུངས་པར" → "ནུས་པ་ཞིག་ཏུ་མཚུངས་པར" — grammar-particle rewording of same comparison. | YES | flagged substitution: particle/construction change |
| 11 | Chakrasamvara mandala notes: among eight directional guardians, vayu in NW likewise identified — same as other general guardian-tradition texts, not Tara-worship-based. | Same, name/attribution unchanged. | YES | particle changes only (ནས→དང་, གིས→དང་) |
| 12 | Taranatha and Palden Sherab: both explain vayu via mantra's hidden meaning, giving a matching identification. | Same claim ("matching" ↔ "unified/agreed" — same fact that the two agree). | YES | flagged substitution: མཚུངས་པའི་ངོས་འཛིན → ངོས་འཛིན་གཅིག་མཐུན་དུ |
| 13 | Taranatha's quote: "Indra=earth, fire-god=fire, Brahma=water, vayu=wind, sna-tshogs-dbang-phyug=space" (verbatim); vayu explained as the wind element. | Quote character-for-character identical; same claim. | YES | — |
| 14 | Palden Sherab also gives a similar five-element explanation. | Same. | YES | particle only |
| 15 | Summary: vayu identified by all 16 commentaries as a worldly deity; 15 commentaries, alongside Indra etc., identify it (via Tara-worship) as NW guardian; 3 commentaries explain individual distinguishing features; 2 commentaries place it among the ten directional earth-guardians; 2 commentaries explain it via mantra's hidden meaning as the wind element. | Same four summary claims, same ref sets attached to each clause, same commentary counts (16/15/3/2/2). | YES | style/honorific rewording only |

## Ref attachment walk

- `yama-sonam` — supports: (1) the 16-commentary appearance claim; (2) the root-verse-derived worship-group + 15-commentary NW-guardian claim; (3) the "vayu-of-various-kinds" name quote; (4) the summary's 16-commentary and 15-commentary/NW-guardian and 3-commentary distinguishing-features clauses. Same statements before and after. YES
- `dharmabhadra` — supports the 15-commentary NW-guardian claim (paired with yama-sonam) in lede and summary. Same statement before/after. YES
- `tenga-tulku` — supports the "ten directional guardians / servant-role" claim (§3) and the summary's 2-commentary directional-guardian clause. Same statement before/after. YES
- `taranatha` — supports the wind-element symbolism claim (lede + §4), the "fashions world's arrangement" claim (§2, corrected back to source wording), and the summary's wind-element clause. Same statements before/after. YES
- `palden-sherab` — supports the wind-element symbolism claim (lede), the five-element explanation (§4), and the summary's wind-element clause. Same statements before/after. YES
- `pema-namgyal` — supports the "power to shake the three realms" claim (§2) and summary's distinguishing-features clause. Identical sentence, unchanged. YES
- `tenzin-dhonzang` — supports the servant-role comparison (§3) and the Chakrasamvara-mandala general-guardian-tradition claim (§3), and summary's 2-commentary directional-guardian clause. Same statements before/after. YES

No ref migrated to a different clause; no ref dropped or duplicated. Token count 24 confirmed by gemini-report.md (C1 PASS).

## Flagged substitutions

| Location | Before | After | Note |
|---|---|---|---|
| Lede, deity list | བརྒྱ་བྱིན་དང་མེ་ལྷ་དང་ཚངས་པ་དང་སྣ་ཚོགས་དབང་ཕྱུག་བཅས་ | བརྒྱ་བྱིན་དང་མེ་ལྷ་ཚངས་པ་སྣ་ཚོགས་དབང་ཕྱུག་བཅས་ | དང་ chain reduced, same 4-item list, same referents |
| Lede, verb | ངོས་འཛིན་བྱེད། | ངོས་འཛིན་མཛད་དོ། | non-honorific → honorific verb (register only, no name involved) |
| §3, seed-syllable | ཏཱཾ་གྱི་འོད་ཟེར | ཏཱཾ་ཡིག་གི་འོད་ཟེར | "TAM" → "the syllable TAM"; same referent (seed-syllable TAM), idiomatic normalization |
| §3, comparison construction | ནུས་པའི་མར་མཚུངས་པར | ནུས་པ་ཞིག་ཏུ་མཚུངས་པར | grammar-particle rewording, same comparison target and meaning |
| §4, agreement phrase | མཚུངས་པའི་ངོས་འཛིན་གསུངས། | ངོས་འཛིན་གཅིག་མཐུན་དུ་གསུངས་སོ། | "matching identification" → "unified/agreed identification" — same fact (the two commentators agree) |
| Throughout | non-honorific verbs (བྱེད, བཤད) | honorific verbs (མཛད, གསུངས) where subject is a named commentator | register elevation; no personal name itself altered, no honorific inserted before a name |

None of these block PASS — each preserves the same referent, same commentator attribution, and same claim.

## Reverted drift

**Location:** § མཚན་ཉིད, Taranatha's claim about vayu fashioning the world's abodes/arrangement.

- **Source (git HEAD, pre-polish):** `...འཇིག་རྟེན་གྱི་གནས་དང་བཀོད་པ་གཟོ་བཀོད་མཛད་མཁན་གྱི་ལྷར...` (གཟོ་བཀོད)
- **Gemini's raw output (body-after.txt, unchanged as the raw record):** `...འཇིག་རྟེན་གྱི་གནས་དང་བཀོད་པ་བཟོ་བཀོད་མཛད་མཁན་གྱི་ལྷར...` (བཟོ་བཀོད — first syllable's initial changed ག→བ)

Confirmed by byte-level hexdump: source syllable starts with U+0F42 (ག, GA), Gemini's version starts with U+0F56 (བ, BA). This is exactly the kind of plausible-looking "typo correction" the task's safety rules require freezing as-is — even though བཟོ་བཀོད (bzo bkod, "form/construction") is the more common compound, the source's exact spelling གཟོ་བཀོད must be preserved verbatim; correcting it is not this pass's role.

**Remedy applied:** surgical reversion (Rule 8a) — edited the polished `article.md` to restore `གཟོ་བཀོད` exactly as in the source. `body-after.txt` was left untouched as the raw Gemini record. Verdict downgraded from PASS to **PASS-after-reversion**.

## Verdict

**PASS-after-reversion.** One factual/orthographic drift was found (a silent single-syllable "correction" of གཟོ་བཀོད → བཟོ་བཀོད) and surgically reverted in `article.md`. Apart from that one span, no fact was added, dropped, weakened, strengthened, or re-attributed to a different commentator; every `<ref>` remains attached to the exact same statement it supported before polishing; all verbatim quotations (the root-verse quote and Taranatha's five-element quote) are character-for-character identical to the source. Six lexical-only substitutions were flagged above (register/particle changes, one idiomatic addition) — none affect meaning, referent, or attribution, so none block PASS.
