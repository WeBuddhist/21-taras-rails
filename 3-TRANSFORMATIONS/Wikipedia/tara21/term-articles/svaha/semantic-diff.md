---
topic: svaha
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/svaha/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS
status: draft
---

# Semantic diff — svaha

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Svaha is a term common to (thun-mong-ba'i) many mantras' endings; can be appended to any mantra. | Same, "thun-mong-gi" (grammatical particle variant of "common to"). | YES | Grammar-particle change only |
| 2 | It is glossed as meaning pacification, pacifying transgressions and increasing virtue, possessing (ldan-la) such potency — Sungrab Tulku, Tsultrim Namdak. | Same content; restructured as "...possessing such potency, is explained (ldan-par bshad)" — explicit attribution verb added, clause boundary shifted. | YES | Paraphrase/restructure, same claim, same two refs |
| 3 | Another commentary explains it also as meaning homage to you (source: Pema Namgyal). | Same. "'grel" (explains) → "bkral" (elucidates/explains); "zhig" (indefinite "a") dropped after "'grel pa gzhan". | YES | Synonym substitution |
| 4 | Explained (Sungrab Tulku, Tsultrim Namdak) as pacifying all transgressions and increasing all virtue. | Same; "zhi bar byed cing" → "zhi ba dang" (gerund → noun+conjunction). | YES | Grammar restructure only |
| 5 | Zurmang Khenpo Pema Namgyal (topic-marked "ni") appends another gloss and states quote: "svaha's letters are homage to you." | Same; "ni" → "gyis" (agentive particle). Quote identical. | YES | Grammar-particle change; quote verbatim preserved |
| 6 | Jonang Taranatha (topic-marked "ni") identifies ("ngos 'dzin byed do", plain verb) svaha as a mantra that transforms the activity of pacification. | Same; "ni" → "s" (agentive); "byed do" → "mdzad do" (honorific verb, same act, same agent). | YES | Register/honorific verb upgrade — flagged below |
| 7 | Taranatha, on top of ("thog tu") the above, also explains ("bshad de") a hidden meaning of svaha: reading om+svaha as the sound of indestructible speech, quote: "...the awareness-mantra of indestructible speech, symbolized by om and svaha, arises limitlessly." | Same; "thog tu" → "steng du" (synonym "on top of"); "bshad de" → "gsungs te" (honorific verb, same act). Quote identical. | YES | Synonym/register substitution; quote verbatim preserved |
| 8 | No other commentary shows (mi ston) a similar hidden meaning. | No other commentary has shown (bstan med do) a hidden meaning similar to that (de dang). Universal negation scope unchanged. | YES | Tense/verb-form variant, same scope-narrowing claim |
| 9 | Both ways of appending svaha appear in this text. Sungrab Tulku: in a closing verse of praise, the single term "svaha" stands for the entire ten-syllable mantra. | Unchanged sentence, byte-identical. | YES | No change |
| 10 | Tsultrim Namdak: in sadhana practice, both the offering mantra to Tara-with-retinue and another praise's mantra in this text have svaha attached (mtha'r btags) at the end (word order: "mantras-both svaha-instr at.end"); shows the practice of appending svaha even when unconnected to Tara's own ten-syllable root mantra. | Same content; word order changed to "mantras-both's end svaha attach" — same fact, same practice described, same two mantras, same conclusion. | YES | Word-order variant only |
| 11 | Svaha is a term common to many mantra endings, expressing both pacification and homage — both senses clear in this text (Sungrab Tulku, Pema Namgyal refs). | Same; "thun mong ba'i" → "thun mong gi"; "nang gsal" → "nang du gsal" (added locative particle). | YES | Grammar-particle change only |
| 12 | Also appended as a name for the entire ten-syllable mantra; practice of appending at the end even when unconnected to Tara's own root mantra is seen (Tsultrim Namdak ref). | Same; "yi ge bcu'i" → "yi ge bcu pa'i" (nominalizer added); "sbyar ba'i" → "sbyor ba'i" (verb-stem spelling normalization). | YES | Spelling/grammar normalization only |

## Ref attachment walk

| Ref | Statement supported before | Statement supported after | Same? |
|---|---|---|---|
| tsultrim-namdak (1st, body 1) | "svaha is common-term appended to mantra endings" | same | YES |
| sungrab-tulku (body 1) | "pacifies transgressions, increases virtue, has such potency" | same | YES |
| tsultrim-namdak (2nd, body 1) | same statement (co-cited) | same | YES |
| pema-namgyal (body 1) | "another commentary: also means homage to you" | same | YES |
| sungrab-tulku + tsultrim-namdak (nges tshig, 1st sentence) | "pacifies all transgressions, increases all virtue" | same | YES |
| pema-namgyal (nges tshig, quote) | Zurmang Khenpo Pema Namgyal's quoted gloss | same, quote verbatim | YES |
| taranatha (nges tshig, 2nd sentence) | "Taranatha identifies svaha as a mantra transforming pacifying activity" | same | YES |
| taranatha (mtshan nyid, quote) | Taranatha's hidden-meaning quote (om+svaha = indestructible speech) | same, quote verbatim | YES |
| sungrab-tulku (dbye ba, 1st sentence) | "svaha stands for the whole ten-syllable mantra in a closing praise verse" | same — sentence untouched | YES |
| tsultrim-namdak (dbye ba, 2nd sentence) | "svaha attached to both the offering mantra and another praise's mantra, even unconnected to Tara's root mantra" | same, only word order changed | YES |
| sungrab-tulku + pema-namgyal (bsdus don, 1st sentence) | "both pacification and homage senses appear in this text" | same | YES |
| tsultrim-namdak (bsdus don, 2nd sentence) | "appended as name for ten-syllable mantra; practice of appending even when unconnected to root mantra" | same | YES |

No ref migrated to a different clause or statement. No verbatim quotation altered (checked character-for-character: the Pema Namgyal quote and the Taranatha hidden-meaning quote are identical in body-before.txt and body-after.txt).

## Flagged substitutions

Lexical/grammatical substitutions, same referent and meaning, listed for domain-expert awareness — none block PASS:

| Location | Before | After | Note |
|---|---|---|---|
| Body 1, opening | ཐུན་མོང་བའི་ | ཐུན་མོང་གི་ | grammar-particle variant of "common to" (also recurs in bsdus don) |
| Body 1, 3rd sentence | འགྲེལ (explains) | བཀྲལ (elucidates) | synonym |
| Nges tshig, Taranatha sentence | ངོས་འཛིན་བྱེད་དོ (plain verb "identifies") | ངོས་འཛིན་མཛད་དོ (honorific verb) | honorific register raised on the verb for Taranatha's own act — not a title inserted before his name (his name/epithet "Jonang Taranatha" is unchanged); the original article already uses honorific གསུངས་ for his and Pema Namgyal's speech elsewhere, so this is consistent with existing register, not a new pattern |
| Mtshan nyid, opening | བཤད་དེ (plain "explains") | གསུངས་ཏེ (honorific "states") | same register point as above |
| Mtshan nyid, opening | གོང་གི་...ཐོག་ཏུ (on top of the above) | གོང་དུ་...སྟེང་དུ | synonym phrase |
| Dbye ba, 2nd sentence | སྔགས་གཉིས་ཀ་སྭཱ་ཧཱས་མཐར་བཏགས་པར | སྔགས་གཉིས་ཀའི་མཐར་སྭཱ་ཧཱ་བཏགས་པར | word-order swap, same meaning |
| Bsdus don, 2nd sentence | ཡི་གེ་བཅུའི་ / སྦྱར་བའི་ | ཡི་གེ་བཅུ་པའི་ / སྦྱོར་བའི་ | nominalizer added / verb-stem spelling normalized |

## Reverted drift (if any)

None. No factual drift was found — no fact added, dropped, weakened, strengthened, or re-attributed; no personal name gained an unattested honorific title (the one honorific change found is on a verb, not a title before a name, and matches the source's own existing register for these commentators).

## Verdict

**PASS.** All changes are restyling: grammatical-particle variants, synonym substitutions, one word-order swap, spelling normalization, and honorific-register raising on two verbs (not names). Both verbatim quotations are character-for-character identical before and after. Every `<ref>` remains attached to the exact same statement it supported before. Headings, tail section (`== འབྲེལ་ཡོད་ཤོག་ངོས། ==` onward), bold span, and category are byte-identical to the source (confirmed via `git diff`). Tsheg-count delta: +0.67% (450 → 453), consistent with light restyling only.
