---
topic: tara-12
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-12/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-12

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: this is the 12th prostration of the Twenty-One Praises; root verse quoted; crescent-moon-crowned, Amitābha-in-locks goddess | Same, word order of "twelfth prostration" rearranged, minor particles added | YES | pure reordering |
| 2 | Name not fixed across traditions; Yama Sönam names her Trashi Thamché Jinma; he also reports three masters (Chöne, Nyisapa, Gendün Drup) each giving a different name | Same three attributions, restructured into an explicit "namely: A, B, C" list | YES | clearer punctuation, same 3 name/author pairs |
| 3 | Sermey Tsang Geshe Tenzin Dhönzang names her Trashi Jungnema; Gyalwa Gendün Drup's commentary uses yet another name; Khenchen Palden Sherab names her Trashi Dönjé Drolma; Sangye Nyentrul Rinpoche and Khenpo Tsultrim Namdak use Trashi Döndrupma | Same four attributions, same names | YES | verb gdags→btags (synonym "to label") throughout |
| 4 | Tenzin Dhönzang's reading of "prostration" (unique, not found in other commentaries) explained as a prayer for cessation of the three-appearances' confused cognition and arising of unconfused cognition | Same claim, same attribution, recast as a "distinguishing feature" (ཁྱད་ཆོས) not found elsewhere | YES | same epistemic content (unique-to-this-commentator), different syntax |
| 5 | Crown = crescent moon (1st-day moon) per Dharmabhadra/Karma Maitri/Tenzin Dhönzang; Yama Sönam alone says 3rd-day moon (divergence flagged); Amitābha in locks, radiating light for beings | Identical claims and attributions, ན→དུ particle swap only | YES | |
| 6 | Taranatha & Palden Sherab: Amitābha sometimes shown as an ascetic. Palden Sherab & Sangye Nyentrul agree (generation-stage reading): yellow body, one face two hands, utpala with jewel-emblem atop it | Identical claims/attributions/spatial relation ("atop"); bshad→bzhed (reporting-verb synonym) | YES | |
| 7 | Yama Sönam alone: golden body, one face eight hands, holding trident/hook etc. (verbatim quote "ཞལ་གཅིག་ཕྱག་བརྒྱད་མ"); both iconographic forms left unreconciled | Identical, quote unchanged | YES | |
| 8 | This [deity's] activity destroys worldly/divine pride (Taranatha, Palden Sherab, Sangye Nyentrul); Palden Sherab & Tsultrim Namdak: light causes nectar-rain, medicinal plants/crops flourish | Same 3-ref pride-destruction claim, same 2-ref nectar-rain claim | YES (after 1 reversion — see below) | subject noun of the pride-destruction clause was drifted by the script, then reverted; see "Reverted drift" |
| 9 | Pema Namgyal: light brings all benefit to disciples (longevity, merit, realization); Tenzin Dhönzang: light causes bodily/mental sufferings, three sufferings, six faults, eight sufferings to leave the body as smoke, plus recitation — unique to him | Identical claims/attributions | YES | |
| 10 | Taranatha & Palden Sherab: secret meaning — crescent = bodhicitta fixed at the crown; Amitābha = essence of the red drop; united, they manifest the empty-form mahāmudrā maṇḍala | Identical claims/attributions | YES | |
| 11 | Könchök Thabkhé: a mahāsiddha's tradition reads crescent as syllable HAM at the crown, Amitābha as upward-moving fire-wind (verbatim quote on caṇḍālī); unreconciled with above | Identical, quote unchanged | YES | |
| 12 | Palden Sherab alone: fourth (formless completion-stage) reading — 4 ornaments mapped 1:1 to the 4 empowerments/signs | Identical 4 mappings, same attribution, list re-punctuated | YES | |
| 13 | Pema Namgyal: alternate secret-meaning terms — Amitābha=vase-empowerment, crescent=secret-empowerment; disagrees with Palden Sherab and with other prostrations' usage | Identical claims/attributions | YES | |
| 14 | Summary: despite many differences (name/form/secret-meaning) across traditions, she is the crescent-crowned, Amitābha-in-locks goddess | Identical claim, "སྤྱིར" (in general) hedge added before the closing consensus clause; སྐུ་འདིར→ལྷ་མོ་འདིའི (same single referent, body/image ↔ goddess) | YES | hedge softens rather than strengthens; referent unchanged (both denote the one deity the whole article is about) |

## Ref attachment walk

Every `<ref name="...">`/`<ref name="..." />` token in the after-text sits on the identical clause it supported before, in the identical order — confirmed by extracting the full ordered ref-tag sequence from both versions (`grep -o '<ref[^>]*>'`) and diffing: **zero differences**. Spot-checked the heavier-restructured paragraphs (name list, iconography, pride-destruction, four-empowerments mapping, closing summary) by hand as well — no ref migrated to a different statement.

## Flagged substitutions

Lexical-only swaps, same referent/meaning, do not block PASS:

| Before | After | Comment |
|---|---|---|
| རལ་པའི་ཁྲོད་ནས / ཁྲོད་ན | རལ་པའི་ཁྲོད་དུ | ablative/locative particle swap, "amid the locks", several places |
| གདགས (verb "to name/label") | བཏགས | synonym, same verb family, used consistently for every naming-attribution sentence |
| ...ལྷ་མོ་ཡིན།། | ...ལྷ་མོ་ཞིག་ཡིན།། | added indefinite marker ཞིག, x2 |
| ...མཐུན་པར་བཤད་དོ | ...མཐུན་པར་བཞེད་དོ | reporting-verb swap ("explained"→"held/asserted"), same reported content |
| འཆད་པ་ཞིག་ཡིན་ཏེ་...མ་བཤད། | བཀྲལ་བ་ནི་...མ་བཤད་པའི་ཁྱད་ཆོས་སོ། | "was not explained by others" recast as "a distinguishing feature not explained by others" — same epistemic claim (unique to Tenzin Dhönzang), not a stronger claim |
| སྐུ་འདིར (closing summary) | ལྷ་མོ་འདིའི | "regarding this body/image" → "this goddess's" — same single referent (the article's one deity), not a class change |
| འཇོམས་ཏེ | འཇོམས་པར་བྱེད་དེ | "destroys" → periphrastic "acts to destroy", same event |
| (implicit list) | སློབ་དཔོན་གསུམ་སྟེ། A་དང་། B། C ཞེས... | three-teachers naming sentence restructured into an explicit "namely" list — same 3 name/author pairs, clearer punctuation |
| ...གོང་འཕེལ་གྱི་སྣང་བ་དང་། ...ཕེབས་པ་དང་། ...སྣང་བར་སོ་སོར་སྦྱར་ཏེ | ...གོང་འཕེལ་གྱི་སྣང་བ། ...ཕེབས་པ། ...སྣང་བ་བཅས་ལ་སོ་སོར་སྦྱར་ཏེ | four-item correspondence list re-punctuated (དང་-chain → བཅས་ལ་ trailing conjunction); same four 1:1 mappings preserved |
| (closing clause) | added སྤྱིར ("in general") before the crown/Amitābha consensus statement | hedges rather than strengthens — appropriate given the Yama Sönam third-day-moon divergence noted two paragraphs earlier |

Personal-name honorific check (Rule 8 known drift pattern): walked every occurrence of every personal name (Yama Sönam, Könchök Thabkhé, Khenchen Palden Sherab, Sermey Tsang Geshe Tenzin Dhönzang, Zurmang Khenpo Pema Namgyal, Jonang Taranatha, Sangye Nyentrul Rinpoche, Khenpo Tsultrim Namdak, Gyalwa/Je Gendün Drup) — no honorific title was added or removed anywhere; every existing title (མཁན་ཆེན་, རྗེ་བཙུན་, ཇོ་ནང་, etc.) is carried over unchanged, in the same position, same number of times.

## Reverted drift

**Location:** `ཕྲིན་ལས་དང་ནུས་མཐུ` section, opening sentence (pride-destruction claim, refs taranatha/palden-sherab/sangye-nyentrul).

- **Before (source):** `འཁོར་འདིའི་ཕྲིན་ལས་སུ་...ང་རྒྱལ་འཇོམས་ཏེ` — subject "འཁོར་འདི" (**this retinue/circle**).
- **Gemini's output:** `ལྷ་མོ་འདིའི་ཕྲིན་ལས་ཀྱིས་...ང་རྒྱལ་འཇོམས་པར་བྱེད་དེ།` — subject silently changed to "ལྷ་མོ་འདི" (**this goddess**).

Unlike the སྐུ་འདིར→ལྷ་མོ་འདིའི swap in the closing summary (both denote the article's single deity via body/image metonymy — a flaggable substitution, not drift), འཁོར ("retinue/circle", a collective/plural notion) and ལྷ་མོ ("goddess", a singular deity) belong to different referential classes. Nothing in `citations.md` or elsewhere in the vault documents what "འཁོར" was meant to denote here (it does not appear as a quoted string anywhere in the citation trail, and no other tara-NN slot article uses "འཁོར་འདི" as the subject of this heading — they all use "ལྷ་མོ་འདི"). Because the actual intended referent of "འཁོར" in the pre-existing source text cannot be verified either way, and this skill's mandate is prose-only recomposition (not fact correction), the change could not be certified as meaning-preserving. Applied Rule 8(a): surgical reversion of the single noun in `article.md`, restoring "འཁོར་འདིའི་ཕྲིན་ལས" to match the source's exact wording, while keeping Gemini's improved verb periphrasis (འཇོམས་པར་བྱེད་དེ) and punctuation around it. Verified afterward against `body-before.txt` — the reverted clause now reads identically to source at the noun in question.

**Separately (mechanical, not Gemini's doing):** the script's reassembly glued the `== འབྲེལ་ཡོད་ཤོག་ངོས། ==` ("Related pages") heading directly onto the end of the preceding paragraph with no line break (`...tenzin-dhonzang" />== འབྲེལ་ཡོད་ཤོག་ངོས། ==`), which would have broken MediaWiki heading rendering (a `==` heading marker only parses at the start of a line). This heading and its three wikilinks were never sent to Gemini (they sit outside `body-before.txt`/`body-after.txt`, i.e., they are part of the script's "frozen tail"), so no content was actually lost or reworded — only the newline separator was missing. Restored the blank line before the heading. Confirmed via `diff` of `grep '^=='` output between the pre-polish commit and the current file: the heading list is now identical, and `diff` of all `[[wikilink]]` targets and all `<ref ...>` tokens (full ordered sequence) between pre-polish and current file both return zero differences.

## Verdict

**PASS-after-reversion.** No fact was added, dropped, or re-attributed in the final `article.md`; every ref supports the exact same statement it supported before; both budgeted verbatim quotations and the root-verse quotation are character-for-character identical; the "Related pages" section (3 wikilinks) and all 8 headings survive intact; no personal-name honorific drift found. One genuine drift (a subject-noun swap in the pride-destruction sentence, retinue→goddess) was caught and surgically reverted to the source's exact wording; one mechanical line-break defect in the script's tail splice (not a Gemini/meaning issue) was also fixed so the heading renders correctly. `body-after.txt` is left untouched as the raw model record per Rule 8(a); the two fixes above were applied only to `article.md`.
