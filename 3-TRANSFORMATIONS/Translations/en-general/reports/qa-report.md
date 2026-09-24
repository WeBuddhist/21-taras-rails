---
title: Praise to the Twenty-One Taras — MQM QA report (general grade)
file_type: report
translation: 3-TRANSFORMATIONS/Translations/en-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general.md
date: 2026-09-24
---

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en-general.md (draft 3) — 2026-09-24

**Score:** 96.0 / 100   **Gate:** FAIL (0 critical, 1 major present)
**Profile:** Fluency 12 (1 major) · Terminology 8 · Accuracy 4 (Mistranslation 3, Addition 1) · LocaleConvention 4 · Style/Register 2 · Audience 1 · Markup/BlockID 0
**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy is scored against the Tibetan critical edition (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`) and the commentary consensus (`reports/commentary-fact-check-consensus-en-general.md`), with the four per-commentary reports and the fixes log where needed.
**Requirements:** there is no `requirements.md`. The contract is the **general** row of `graded-translate/SKILL.md` § Registers (English): standard English prose; common Buddhist loanwords used freely without gloss.
**Termbase:** `en-bo-en-termbase-general.json`, checked with `check_termbase_consistency.py --strict-diacritics`: 131/131 locked renderings found, 0 misses. The 4 loose matches (1-7, 1-13 ×2, 1-15: "destroy", "blaze") are normal inflections — Neutral. The Terminology rows below are within-file consistency problems, not termbase misses.
**Stage 0:** clean. The script reported 112 minor "latin characters in content". These are false positives: that check is written for Devanagari tracks, and English is written in Latin script. Not counted.
**Word count:** 882 English words (translated content only; frontmatter, transclusion lines and block IDs excluded). 32 blocks + 5 headings checked; all block IDs and transclusions match the root.
**Method note:** this is an LLM self-check. It does not replace review. A domain specialist decides whether the file becomes `complete`.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| 1-8 | Fluency (wrong referent) | Major | The verse is in the third person ("Homage to ture… Who completely destroys…") but line 3 says "upon **your** lotus face". Nobody is addressed, so "your" reads as the reciter's face. The Tibetan means her own face. | "Whose lotus face is set in a wrathful frown," (and keep the verse in one person throughout) | root 1-8 ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད; termbase `lotus_face` note "Her own face… (1-8)"; DG report style note "1-8… switch between 'her / who' and 'your' mid-verse" |
| I-2 | Accuracy/Mistranslation | Minor | The head noun བསྟོད་པ "praise" is dropped, and ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག "twenty-one homages" becomes "Twenty-One Verses". The heading, 1-22 and the colophon all call it a praise. "its Benefits" is also mis-cased. | "The Praise to Tara in Twenty-One Homages, with Its Benefits." | root I-2 སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ཕན་ཡོན་དང་བཅས་པ |
| 1-1 | Fluency | Minor | "Tara, the swift and heroic," — two adjectives with no noun. | "Tara, the swift one, the heroine," | root 1-1 མྱུར་མ་དཔའ་མོ |
| 1-2 | Accuracy/Mistranslation | Minor | སྟོང་ཕྲག is "thousands", not "a thousand". | "Of thousands of gathered stars." | root 1-2 སྐར་མ་སྟོང་ཕྲག; DG report style note "1-2 སྟོང་ཕྲག = 'thousands'" |
| 1-2 | Fluency | Minor | "gathered" twice in four lines, for two different words (བརྩེགས "stacked", ཚོགས "gathered"). | "A hundred full autumn moons heaped together," | root 1-2 བརྩེགས / ཚོགས |
| 1-3 | Accuracy/Addition | Minor | After the fix, the list reads as seven qualities, not the six perfections. On the DG/GD/TT reading, སྤྱོད་ཡུལ is rendered twice ("sphere of activity" + "wisdom"); on TN's, "wisdom" doubles "peace". Line 3 is also twice the length of the others, and "She whose" does not agree with "to her". | e.g. "Who is generosity, diligence, discipline, peace, / Patience, concentration, and the very sphere of wisdom." — or add a translator note saying which six are meant. | root 1-3 སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ; consensus row 3 |
| 1-4 | Fluency | Minor | "every single perfection without exception" — two intensifiers for one word (མ་ལུས). | "Who have attained all the perfections without exception." | root 1-4 མ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི |
| 1-6 | Fluency | Minor | "Praised from before" reads as "praised previously". མདུན་ནས means "in front of her". "hosts of spirits" also adds a second "hosts" (only གནོད་སྦྱིན་ཚོགས has ཚོགས). | "Praised before her by spirits, / Vetālas, gandharvas, and hosts of yaksas." | root 1-6 མདུན་ནས; DG report style note "'from before' reads as time" |
| 1-6 | LocaleConvention | Minor | Mixed transliteration. "yaksas" is half-transliterated (neither "yakṣas" nor "yakshas") next to "vetālas". Across the file, Uṣṇīṣa, Tathāgatas, Brahmā, Vāyu, Īśvaras, nirvāṇa, Amitābha carry diacritics; Tara, Mara, maras, mudra, yaksas do not. Recurs at 1-21. | Pick one convention for the general grade and fix it in the termbase (e.g. "yakshas" with plain forms throughout, or full diacritics throughout). | termbase `yaksha` en "yaksas", `vetala` en "vetāla" |
| 1-8 | Terminology | Minor | "Homage to **ture**" is lower case. The translator decided ture here is her name ("consistent with 1-17 and 1-21"), and 1-17 and 1-21 write "Ture". | "Homage to Ture, the Great Terrifying One," — and update the termbase `ture` note. | fixes log, decisions table row 1-8; termbase `ture` note |
| 1-1 – 1-9 | Style/Register | Minor | The voice switches: 1-1 to 1-6 and 1-9 say "her"; 1-7 and 1-10 to 1-21 say "you"; 1-8 mixes both. The Tibetan uses the same form (…མ) in every homage. For a text recited aloud, the switch is noticeable. | Choose one voice for all 21 homages ("you" already covers 13). | root 1-1 to 1-21, each line 1 ཕྱག་འཚལ… / last line …མ |
| 1-9 | Fluency | Minor | "Her palm adorned…, / Radiating…" — dangling participle; it is unclear what radiates. | "Whose palm is adorned with the wheel…, / Who radiates a turbulent mass of her own light." | root 1-9 བརྒྱན་པའི། … འཁྲུག་མ |
| 1-10 | Fluency | Minor | Agreement: "Homage to you… Who… **Brings**". | "Bring maras and the world under your power." | — |
| 1-11 | Terminology | Minor | ཁྲོ་གཉེར is rendered three ways: "frowning expression" (1-8), "vibrating frown" (1-11), "wrathful frown" (1-14). ཁྲོ means wrath, so 1-8 and 1-11 lose it. "vibrating frown" is also odd English. | Use "wrathful frown" throughout; here "Who, with a quivering, wrathful frown and the syllable hum,". | root 1-8, 1-11, 1-14 ཁྲོ་གཉེར |
| 1-13 | Terminology | Minor | བསྐུམ is "drawn in" at 1-7 and "bent" at 1-13. The two verses are mirror postures, so the same verb helps the reader see it. | Use one verb in both (e.g. "drawn in"). | root 1-7 གཡས་བསྐུམ་གཡོན་བརྐྱང; 1-13 གཡས་བརྐྱང་གཡོན་བསྐུམ |
| 1-13 | Audience | Minor | "surrounded by joy" gives a general reader no image. GD and TT read ཀུན་ནས་བསྐོར as joyful disciples circling her; TN as encircling dance postures. Recurs at 1-16. | e.g. "joyfully encircled" — a translator call; a short note would also do. | consensus "Other findings": 1-13/1-16 *kun nas bskor*; GD, TN, TT style notes |
| 1-14 | Terminology | Minor | "trample it with your feet" renders བརྡུང ("pound, beat"). "trampling" is the locked word for a different verb, མནན (1-5, 1-7). | "And pound it with your feet;" | root 1-14 ཞབས་ཀྱིས་བརྡུང་མ; termbase `trampling` = མནན |
| 1-15 | Terminology | Minor | སྤྱོད་ཡུལ is "sphere of activity" at 1-3 but "sphere of experience" here. | Pick one (e.g. "domain") for both. | root 1-3, 1-15 སྤྱོད་ཡུལ |
| 1-15 | Terminology | Minor | སྡིག་པ is "negativity" here but "misdeeds" at 2-2. | "You destroy great misdeeds." | root 1-15 སྡིག་པ་ཆེན་པོ; 2-2 སྡིག་པ་ཐམས་ཅད |
| 1-15 | LocaleConvention | Minor | "OṂ and SVĀHĀ" use capitals and diacritics; the locked syllables (hum, phat, trat, tuttare, ture) are plain lower case. | Use one form for every mantra syllable (e.g. "om and svaha"). | termbase `hum`, `phat`, `trat`, `tuttare` |
| 1-16 | Fluency | Minor | Agreement: "Homage to you… Who utterly **shatters**". | "Who utterly shatter the bodies of enemies;" | — |
| 1-16 | Fluency | Minor | "With the ten-syllable mantra arranged," is an unclear absolute phrase. | "In whom the ten-syllable mantra is set," | root 1-16 ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི |
| 1-18 | LocaleConvention | Minor | "TĀRA" (capitals, macrons) next to plain "phat"; also easy to confuse with the name "Tara". | Same convention as 1-15 (e.g. "tara twice"). | as 1-15 |
| 1-20 | LocaleConvention | Minor | "HARA twice and tuttare" — two conventions in one line. | "hara twice and tuttare". | as 1-15 |
| 1-22 | Accuracy/Mistranslation | Minor | ཀྱིས is instrumental: a praise **by** the root mantra, not a praise **of** it. The full stop also ends a sentence that has no main verb; in the Tibetan it runs on into 2-1 and 2-2. | "With this praise by the root mantra / And these twenty-one homages," (comma, not full stop) | root 1-22 རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ; TN "the praise by the ten-syllable root mantra"; TT "the praise by the root mantra" |
| 2-1 | Fluency | Minor | "with supreme intent" is not idiomatic. GD glosses རབ་ཏུ་བརྗོད as "with great faith", TN "with diligence". | "Who recites it earnestly," | consensus "Other findings", 2-1 *rab tu brjod* |
| 2-2 | Fluency | Minor | "Having arisen" — "arise" means "come into being". The sense is "getting up". | "Rising at dusk and at dawn," | root 2-2 ལངས་པར་བྱས་ནས |
| 2-3 | Terminology | Minor | རྒྱལ་བ is "Victors" at 1-4 but "Victorious Ones" here. | "Seventy million Victors". | root 1-4 རྒྱལ་བའི་སྲས; 2-3 རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན |
| 2-4 | Fluency | Minor | "Their poisons" follows "one will attain…" (2-3): singular "one", then "their". The antecedent is unclear. | "For such a person, poisons that are extremely fierce," | root 2-4 དེ་ཡི་དུག |
| 2-5 | Style/Register | Minor | "This applies to other sentient beings as well." — flat, office-style prose in a verse. | "And so too for other beings." | root 2-5 སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ |
| a-1 | Terminology | Minor | "Tārā" here, "Tara" in the title, I-2, I-3 and 1-1. The termbase locks both ("Tara" and "the Blessed Tārā"), so it has to be fixed there. | "The praise to the Blessed Tara…"; change `blessed_tara` to match `tara`. | termbase `tara`, `blessed_tara` |

**Neutral (logged, not scored)**
- 1-3 "gold and blue" lotus; 1-8 "champions of Mara"; 1-14 "the seven levels"; 1-17 "Vindhya"; 1-22 "and"; 2-6 optative — settled translator decisions (fixes log).
- 1-15 OṂ/SVĀHĀ order and 1-6 "the various Īśvaras" — single-commentary flags, left by rule.
- 1-21 "the three suchnesses" — consensus wording. It is opaque to a general reader; a short translator note would help.
- 1-4 "Uṣṇīṣa" — an accepted loanword for this grade; still a hard word for a general reader.
- 1-18 "moon" for the kenning རི་དགས་རྟགས་ཅན — merged by termbase design.
- Frontmatter says `headings_translated: 4`; the body has 5 heading blocks (the title ^0 plus 4). Metadata only.

### Top fixes
1. 1-8: remove the stray "your" and keep the verse in one person (the only Major).
2. Pick one voice ("you") for all 21 homages; this also fixes the agreement slips at 1-10 and 1-16.
3. Pick one convention for mantra syllables and one for loanword diacritics, and fix it in the termbase (OṂ/SVĀHĀ, TĀRA, HARA vs hum/phat; yaksas; Tārā vs Tara).
4. Make repeated Tibetan words match: ཁྲོ་གཉེར "wrathful frown", སྤྱོད་ཡུལ, སྡིག་པ, རྒྱལ་བ, བསྐུམ; and do not use "trample" for བརྡུང (1-14).
5. Restore "praise" in the I-2 title and "by the root mantra" at 1-22.

## Re-check after fixes (draft 4) — 2026-09-24

Fixes applied per `qa-fixes-log-en-general.md` (approved by Tenkal): 30 of 31 rows — the 1-8 Major and 29 of 30 Minors; all 21 homages now in the second person.

**Stage 0** (`mqm_mechanical_checks.py <file> --source <root>`): 32 distinct verse IDs, 32 transclusions; 0 critical, 0 major, 112 minor — all 112 are "latin characters in content", false positives for an English track (the check is written for Devanagari). Stage-0 gate: PASS. Not counted.
**Alignment** (`check_translation_alignment.py`): OK — 32 segments, 5 headings, line counts and IDs unchanged. **Linter** (`lint_text_input.py`): OK.
**Terminology** (`check_termbase_consistency.py --strict-diacritics`): 131/131 locked renderings found, 0 misses (4 loose inflections, 3 covered) — unchanged from draft 3.
**Word count:** 878 (same method as the draft-3 run, 882).

**Remaining errors:** 0 critical · 0 major · 2 minor
| Verse | Dimension | Severity | Note |
|---|---|---|---|
| a-1 | Terminology | Minor | "the Blessed Tārā" vs "Tara" elsewhere — locked (`blessed_tara`); needs a word-list change |
| 1-6, 1-21 | LocaleConvention | Minor | "vetālas" keeps a macron in an otherwise plain-spelled file — locked (`vetala`); needs a word-list change |

**Score:** 100 − (2 × 1 / 878) × 100 = **99.8 / 100**   **Gate:** PASS (0 critical, 0 major). The file stays `status: draft`: only a domain specialist sets `complete`. The two remaining Minors clear once the word list is changed (see "For the word list" in the fixes log). This re-check is an LLM self-check of the applied fixes, not a fresh full QA run.
