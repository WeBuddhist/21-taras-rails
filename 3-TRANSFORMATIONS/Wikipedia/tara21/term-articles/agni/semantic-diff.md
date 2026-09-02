---
topic: agni
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/agni/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — agni

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Fire-god (me lha) appears in all sixteen commentaries on the Praises to the Twenty-One Taras, as a worldly deity. | Same. | YES | བཅུ་དྲུག་ཆར་ → བཅུ་དྲུག་ཀུན་ ("all sixteen" — synonym); added a sentence-break shad after ལྟར |
| 2 | Root-verse quote: "Praise to Indra, Agni, Brahmā... " | Identical quote, character-for-character. | YES | verbatim — unchanged |
| 3 | Per the verse, Agni is identified by all 16 commentaries as one of the worldly deities (with Indra, Brahmā, Vāyu, Īśvara) who worship/praise Tārā. | Same. | YES | list-of-four restyled from shad-separated to དང་-conjoined; བཅུ་དྲུག་ཀ་...བྱེད་དོ → བཅུ་དྲུག་པོས་...མཛད་དོ (honorific verb, same claim) |
| 4 | Agni is known by the epithet "sage" (drang srong); many commentaries treat him as chief of the sages. | Same. | YES | added ཀྱང particle; བྱེད་དོ → མཛད་དོ honorific |
| 5 | Some commentaries instead place him as the guardian of the southeast direction, calling him "sage of the southeast." | Same. | YES | ཁ་ཤས་ → འགྲེལ་པ་ཁ་ཅིག་ (explicit "some commentaries", same referent); གནས་སྐབས་སུ་ → གནས་སུ་ (same "position/role" sense); added ཀྱང |
| 6 | Tendhar Trulku and Serme Tsang Geshe Tenzin Dönzang: Agni is placed among the ten guardians of the earth (not as one who worships Tārā), drawn/summoned by the ray of light from Tārā's heart-syllable TĀṂ to perform whatever activity is commanded, like a servant. | Same — same two named commentators, same claim, same "not a worshipper / servant of activity" content. | YES | མེ་ལྷ་སྒྲོལ་མ་མཆོད་མཁན་གྱི་ཐོག་ནས་མིན་པར → མེ་ལྷ་སྒྲོལ་མ་ལ་མཆོད་པ་འབུལ་མཁན་གྱི་ཚུལ་དུ་མ་ཡིན་པར (same meaning); dropped redundant གཉིས་ཀས (subject already stated as the two masters at sentence start, so no information lost) |
| 7 | Tenzin Dönzang further draws on a Cakrasaṃvara maṇḍala note to identify Agni also among the eight guardians. | Same. | YES | བཤད་དོ → མཛད་དོ honorific; added དེ་དང for clarity |
| 8 | Jonang Tāranātha and Khenchen Palden Sherab both explain Agni also via the mantra's secret meaning, identifying him with the fire element. | Same — same two named commentators, same identification. | YES | བཤད་དེ...ངོས་འཛིན་བྱེད་དོ → བཀྲལ་ཏེ...ངོས་འཛིན་མཛད་དོ (synonyms/honorific); dropped ཀྱང particle |
| 9 | Tāranātha's quote: "Indra is earth, Agni is fire, Brahmā is water, Vāyu is wind, Īśvara is space" — sets the five-element order; Palden Sherab gives a matching explanation. | Same. Quote identical character-for-character. | YES | verbatim quote unchanged; གོ་རིམ་བཀོད་ལ → གོ་རིམ་དུ་བཀོད་ཅིང (same); བཤད་པ་གནང་ངོ → གསུང་བཤད་གནང་ངོ (honorific) |
| 10 | Summary: Agni is a worldly deity; all sixteen commentaries identify him as one who worships Tārā with Indra etc. | Same. | YES | ཀ་གིས...ངོས་འཛིན་བྱེད → པོས...ངོས་འཛིན་མཛད་དོ (honorific/synonym) |
| 11 | Summary: many commentaries call him "sage." | Same. | YES | clause-final particle change only |
| 12 | Summary: two commentaries place him among the ten earth-guardians. | Same. | YES | clause-final particle change only |
| 13 | Summary: two commentaries also identify him with the fire element via secret meaning. | Same. | YES | ནོ → པར་བཤད་དོ (same meaning, more explicit verb) |

## Ref attachment walk

| Ref | Statement supported before | Statement supported after | Same? |
|---|---|---|---|
| yama-sonam | lead: all-16 identification as worshipper-deity | same | YES |
| karma-maitri | lead: all-16 identification as worshipper-deity | same | YES |
| gendun-gyatso | lead: all-16 identification as worshipper-deity | same | YES |
| taranatha | "sage" epithet (§2); secret-meaning fire-element claim (§4, both instances); summary (§5, both instances) | same, same positions | YES |
| tsultrim-namdak | "sage" epithet (§2); summary | same | YES |
| pema-namgyal | "sage" epithet (§2) | same | YES |
| sangye-nyentrul | southeast-guardian alternative (§2) | same | YES |
| sungrab-tulku | southeast-guardian alternative (§2) | same | YES |
| palden-sherab | southeast-guardian alternative (§2); secret-meaning fire-element claim (§4, both instances); summary (§5, both instances) | same, same positions | YES |
| tenga-tulku | ten-earth-guardians claim (§3); summary | same | YES |
| tenzin-dhonzang | ten-earth-guardians claim + Cakrasaṃvara maṇḍala note (§3, both instances); summary | same, same positions | YES |

All 24 ref tokens (per gemini-report.md) are attached to the identical statement they supported before recomposition; none migrated to a different clause.

## Flagged substitutions

Lexical-only swaps, same referent/meaning in every case — none block PASS:

| Before | After | Note |
|---|---|---|
| བཅུ་དྲུག་ཆར་ | བཅུ་དྲུག་ཀུན་ | "all sixteen" — synonym quantifier |
| བཅུ་དྲུག་ཀ་...བྱེད་དོ / ངོས་འཛིན་བྱེད་དོ (×4) | བཅུ་དྲུག་པོས་...མཛད་དོ / ངོས་འཛིན་མཛད་དོ | plain verb → honorific verb (མཛད་), applied throughout to actions of the commentators/masters already named in the sentence — not a title inserted before a personal name (checked: ཏཱ་ར་ནཱ་ཐ, མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ, རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ, སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང་ all appear unchanged, no honorific added before any of them) |
| ཁ་ཤས་ཀྱིས་ན்ི | འགྲེལ་པ་ཁ་ཅིག་གིས་ནི་ | "some" → "some commentaries" — same referent, made explicit |
| གནས་སྐབས་སུ་ | གནས་སུ་ | "position/status of" → "position of" — same sense in context |
| མེ་ལྷ་སྒྲོལ་མ་མཆོད་མཁན་གྱི་ཐོག་ནས་མིན་པར | མེ་ལྷ་སྒྲོལ་མ་ལ་མཆོད་པ་འབུལ་མཁན་གྱི་ཚུལ་དུ་མ་ཡིན་པར | "not as a worshipper of Tārā" — paraphrase, same meaning |
| བཤད་དེ / བཤད་དོ / བཤད་པ་གནང་ངོ (various) | བཀྲལ་ཏེ / མཛད་དོ / གསུང་བཤད་གནང་ངོ | synonyms of "explain" and honorific register upgrades |
| dropped: གཉིས་ཀས (§3, first sentence) | omitted | redundant with dual subject already named at sentence start (རྡོར་སློབ་... དང་... གཉིས་ཀྱིས་ནི); no information lost |
| discourse particles ཀྱང, དེ་དང added/dropped in several places | — | do not change claim content |

## Reverted drift (if any)

None. No factual drift was found; no reversion was necessary.

## Verdict

**PASS.** Every fact, every named commentator, every attributed position, the five-element correspondence, the two alternative classifications (worshipper-deity vs. earth-guardian vs. secondary Cakrasaṃvara-maṇḍala guardian), and the secret-meaning fire-element identification are preserved unchanged. Both verbatim quotations (the root-verse citation and Tāranātha's five-element quote) are character-for-character identical to the source. All 24 refs remain attached to the exact statement they supported before recomposition. The changes found are register/style only: synonym swaps, honorific-verb upgrades (བྱེད→མཛད, བཤད་པ→གསུང་བཤད), discourse-particle additions/drops, and list restyling (shad-separated → དང་-conjoined) — none of which alters, adds, drops, weakens, strengthens, or re-attributes any claim. No honorific title was inserted before any personal name (the one known drift pattern from the 2026-08-21 pilot was specifically checked for and not found).
