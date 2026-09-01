---
topic: tara-02
method: gemini-article-polish
source: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-02/article.md
model: gemini-3.1-pro-preview
date: 2026-08-23
verdict: PASS-after-reversion
status: draft
---

# Semantic diff — tara-02

## Sentence-by-sentence comparison

| # | Before (gist) | After (gist) | Facts identical? | Note |
|---|---|---|---|---|
| 1 | Lead: this deity is the second prostration of the 21-prostration praise. | Same, "ལྷ་མོ" (deity) made explicit: "...is the deity of the second prostration." | YES | Flagged substitution — see below; matches house style used in tara-01/03/04/05 openers. |
| 2 | Root verse quoted verbatim (autumn moon, hundred full moons, thousand stars, radiant light). | Identical, character-for-character. | YES | Verbatim quote unchanged. |
| 3 | Per the verse, her face — white, beautiful, brighter than a thousand stars — is how all recognize her. | Same claim, re-punctuated with more shad breaks. | YES | Style only. |
| 4 | Different textual traditions name her differently, so no single name is fixed; [she] is designated/named Lodrö Yangchenma. | Different traditions name her differently, name not fixed as one; **"popularly/commonly (ཡོངས་གྲགས་སུ) she is called"** Lodrö Yangchenma. | NO → reverted | **Factual drift found and reverted** — see Reverted drift below. |
| 5 | Gyalwa Gendün Drub's own commentary quoted verbatim ("འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ།"). | Identical, character-for-character. | YES | Verbatim quote unchanged. |
| 6 | So stated; Yama Sönam's commentary also identifies this as Gendün Drub's tradition. | Same claim, particle changes only (གིས་ནི...བྱེད་དོ → ཏུ་ཡང...བྱས་སོ). | YES | Style only. |
| 7 | Tenzin Dhonzang names her "Zhiwa Chenmo"; per Geshe Lobsang Dawa's annotation, no new name is given — the root verse's final words "Ödrap Barma" are taken as the name. | Same claim, verb synonyms only (གདགས/བཏགས/འདོགས — all "to name/designate"). | YES | Style only. |
| 8 | Body-form: face like stacked autumn moons [3 refs]; body color white [3 refs]; per Sangye Nyentrul & Palden Sherab: one face, two hands, peaceful form, half-vajra posture on lotus-moon, right hand boon-granting mudra, left hand holds utpala marked with mirror and seed-syllable [2 refs]. | Same iconography, same ref placement/count, minor particle additions (ཕྱག་གཡས་པས், མེ་ལོང་དང་ས་བོན་ཡིག་). | YES | Style only — no iconographic detail added/dropped. |
| 9 | In a commentary by Yama Sönam, relying on Nyima Bepa's statement, another body-form is also explained. | Same claim, particle change (གིས་ནི → ཏུ). | YES | Style only. |
| 10 | Three-faced, twelve-armed verse quoted verbatim. | Identical, character-for-character. | YES | Verbatim quote unchanged. |
| 11 | So stated; other commentaries give no scriptural indication of face/arm-count here — this expanded form is a feature unique to Yama Sönam's commentary alone. | Same claim, synonym/particle changes only (ལུང་མི་སྟོན་ཏེ → ལུང་བསྟན་མེད་པས; གཅིག་པུས → གཅིག་པུར). | YES | Style only — exclusivity attribution ("alone/unique to Yama Sönam") preserved. |
| 12 | Light rays from the mirror dispel beings' ignorance [3 refs]; per Sangye Nyentrul, this increases wisdom-strength and expands intelligence. | Same claim; "ཕྱག་གི་" (hand's) added before "mirror" — mirror already established (§ body-form) as held in her left hand. | YES | Flagged substitution — clarifying, no new referent. |
| 13 | Per Zurmang Khenpo Pema Namgyal: meditating on nectar-light dissolving into oneself grants long-life and wisdom siddhis. | Identical claim, particle/auxiliary additions only. | YES | Style only. |
| 14 | Per Geshe Tenzin Dhonzang: an uncommon ransom (lü) practice — offering one's misdeeds/obscurations with a guru-effigy ransom to the Lord of Death, satisfying karmic debts; love/compassion/bodhicitta explained as the supreme ransom from death; her chief activity is dispelling harm from obstructing spirits and bodily/mental afflictions. | Identical claim and attribution, restructured clause breaks only. | YES | Style only. |
| 15 | Per Taranatha & Palden Sherab (secret meaning, completion-stage): hundred-stacked moons = bodhicitta rising jewel-like from heart to crown uninterruptedly; thousand stars = pervading all subtle channels. | Identical claim and dual attribution. | YES | Style only. |
| 16 | Per Palden Sherab alone: bliss-emptiness wisdom pervades via the four chakras; generation-stage: white Vajra Yangchenma at Yeshe Tsogyal's heart; ultimate: introduced as Vajravarahi's own face, moon-stacked. | Identical claim; "དེ་ཉིད" (this very) added as anaphoric emphasis on "white [Vajra Yangchenma]." | YES | Style only — exclusivity marker ཁོ་ན (Palden Sherab alone) preserved. |
| 17 | On "rab tu phye": most traditions read it as light brighter than a thousand stars; Gyalwa Gendün Gyatso reads it as adorned by stars; Yama Sönam's commentary criticizes predecessors (starlight = faint light, an insult if applied to the deity's face) and reads "rab tu phye" as moonlight disclosed/revealed for meditation focus. | Identical claims and attributions; bold names (Gendün Gyatso, Yama Sönam) unchanged; verbatim quote "རབ་ཏུ་ཕྱེ" preserved twice. | YES | Style only — no honorific added to any name (checked both bold spans). |
| 18 | Traditions differ on what the light-rays are a sign of: Palden Sherab & Sangye Nyentrul explain via the four correct insights (meaning, dharma, definitive words, confidence); Tenzin Dhonzang via four types of wisdom (vast, clear, swift, deep). | Identical claims, attributions, and list items/order; bold names unchanged. | YES | Style only. |
| 19 | Conclusion: despite great differences among traditions on name/body-form/verse-meaning, all recognize her as the deity — whiter than the autumn moon, brighter than starlight — who displays wisdom-light. | Same claim; "ལྷ་མོ" made explicit (as in lead); "མཐུན་པར" (in concord) added before "all recognize." | YES | Flagged substitution — see below. |

## Ref attachment walk

Every `⟦Rn⟧` / `<ref>` token was checked against the statement immediately preceding it in both before/after texts. All 45 ref tokens remain attached to the same statement they supported before the polish — confirmed by the paragraph-by-paragraph walk above (ref counts and ref-name sequences are identical in both `body-before.txt` and `body-after.txt`; C1 also enforced this mechanically). No ref migrated to a different clause. No honorific was inserted before any personal name — walked all bolded and non-bolded personal names (Taranatha, Yama Sönam, Gendün Drub, Palden Sherab, Sangye Nyentrul, Tenzin Dhonzang, Lobsang Dawa, Pema Namgyal, Gendün Gyatso, Dharmabhadra, Tsultrim Namdak, Karma Maitri, Drakpa Gyaltsen) — all identical wording before and after.

## Flagged substitutions

| Location | Before | After | Note |
|---|---|---|---|
| Lead sentence | "...ཕྱག་འཚལ་ཡིན" (is the [second] prostration) | "...ཕྱག་འཚལ་གཉིས་པའི་ལྷ་མོ་དེ་ཡིན" (is the deity of the second prostration) | Same referent; "ལྷ་མོ" (deity) made explicit. Matches the opener convention already used in tara-01, tara-03, tara-04, tara-05 (e.g. tara-04: "...ལྷ་མོ་ཞིག་ཡིན"). Does not block PASS. |
| § ཕྲིན་ལས་དང་ནུས་མཐུ | "མེ་ལོང་ནས" (from the mirror) | "ཕྱག་གི་མེ་ལོང་ནས" (from the hand's mirror) | The mirror was already established as hand-held in the preceding § སྐུ་ཡི་རྣམ་པ (left hand holds the mirror-marked utpala) — clarifying, no new object introduced. Does not block PASS. |
| Conclusion sentence | "མཐའ་དག་གིས་ངོས་འཛིན་བྱེད་དོ" (all recognize) | "མཐའ་དག་གིས་མཐུན་པར་ངོས་འཛིན་བྱེད་དོ" (all recognize in concord/unanimously) | Completes the concessive structure already begun by "ཁྱད་པར་ཆེན་པོ་ཡོད་ཀྱང" (though there are great differences...[yet they agree]); reads as a natural resolution of the same claim rather than a new consensus assertion. Does not block PASS. |

## Reverted drift (if any)

**§ མཚན་གྱི་ངེས་ཚིག (naming section).** Gemini's output changed the naming statement from an editorial designation to a claimed-popularity statement:

- Source: "...བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་མཚན་གྱིས་གདགས་སོ།།" — "[she] is designated by the name Lodrö Yangchenma."
- Gemini output: "...ཡོངས་གྲགས་སུ་བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་འབོད་དོ།།" — "[she] is **popularly/commonly known as** Lodrö Yangchenma."

This is factual drift, not a lexical substitution: it converts a plain editorial-naming statement into an unstated claim about the epithet's currency/consensus. Per the vault's tara21 publication registry, most of the 21 slot epithets are contested among traditions — the sentence itself says as much in its first clause (traditions name her differently; no single name is fixed) — so asserting the name is "commonly known" is an unsupported, and arguably contradictory, addition not present in the frozen source.

**Remedy applied:** surgical reversion (Rule 8a). Edited `article.md` to restore the drifted clause to the source's exact wording:

```
- ཡོངས་གྲགས་སུ་བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་འབོད་དོ།།
+ བློ་གཏེར་དབྱངས་ཅན་མ་ཞེས་མཚན་གྱིས་གདགས་སོ།།
```

The rest of the sentence's mechanical rephrasing (བཏགས་ཡོད་པས་...མ་ངེས་ཀྱང for the "traditions differ, no single name fixed" clause) was left as Gemini composed it — that portion carries no fact beyond the source. `body-after.txt` is left untouched as the raw model record per Rule 8a.

## W1 warnings — resolved

`gemini-report.md` lists 6 W1 warnings (paragraphs not ending `།།`). All 6 are false positives: comparison against `body-before.txt` shows every one of these paragraphs is byte-identical in structure to the source (paragraphs that end mid-sentence leading into a following verbatim verse-quote block, e.g. "...རྩ་བའི་ཚིགས་བཅད་ལས།", "...རང་ཉིད་ཀྱི་འགྲེལ་བར།", "...ཀྱང་བཤད་དེ།", or that end inside a quotation mark "...."). This paragraph-break pattern is inherent to the source article's own structure (root/commentary quotations set off as separate paragraphs) and was not introduced or altered by the polish. No re-run was needed.

## Verdict

**PASS-after-reversion.** One factual drift was found (an unsupported "commonly known as" claim inserted into the naming section) and surgically reverted to the source's exact wording. Every other fact, name, number, doctrinal position, and position-holder attribution is unchanged; every one of the 45 refs remains attached to the same statement it supported before; no honorific was added to any personal name; all four verbatim quotations are character-for-character identical; the punctuation contract holds (no commas, sentence-final shad, paragraph-final །།, no punctuation immediately after a ref); headings, bold spans, frozen tail, and category are byte-identical to the source.
