---
title: QA report — Mongolian (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-mn-general.md
skill: translation-qa (MQM, Webuddhist-Skills/rails/translation-qa/SKILL.md)
note: Runs are appended, dated. Never overwrite an earlier run.
---

# QA report — Mongolian, general grade

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-mn-general.md (draft 5) — 2026-09-25

This is an LLM self-check (Claude). It is not a sign-off. A native Mongolian reader and a domain specialist decide. The file stays `status: draft`.

**Score:** 97.1 / 100   **Gate:** PASS (0 critical, 0 major; 17 minor)
**Profile:** Accuracy/Mistranslation 3 · Accuracy/Addition 1 · Terminology 2 · Fluency 4 · Style/Register 3 · Audience 0 · LocaleConvention 4 · Markup/BlockID 0 · Neutral 11 (not scored)
**Word count:** 581 Mongolian words (space-separated tokens in headings and blocks; transclusion lines and block IDs left out).
**Score formula:** 100 − (17 × 1 / 581) × 100 = 97.1.

**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy is scored against the Tibetan critical edition (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the Mongolian consensus (`mn-general/reports/commentary-fact-check-consensus-mn-general.md`), the English consensus (`en-general/reports/commentary-fact-check-consensus-en-general.md`) and the fact-checked English (`en-general/bo-…-en-general.md`) as the meaning reference. Every accuracy judgement below cites one of these. Nothing is from memory.

**Requirements basis:** there is no `requirements.md` for this track, and Mongolian has no row in `graded-translate/SKILL.md` § Registers. The contract is the track's style file `3-TRANSFORMATIONS/Translations/Gemini/mn-general/style.md`: Cyrillic (Khalkha), clear modern Mongolian for a general reader; keep the liturgical Buddhist words (Дарь эх, бурхан, хутагт, тарни, авшиг, the refrain мөргөмүй) but use modern grammar, no archaic particles (лугаа, хийгээд, болмуй); fixed terminology inflected as grammar needs; mantra syllables as recited in Mongolia, in Cyrillic, never translated; no glosses or notes.

**Stage 0 (mechanical):** clean. `mqm_mechanical_checks.py <file> --source <root>` (`$HOME/qa-mn/stage0-mn.json`) → 32 distinct verse IDs, 32 transclusions, 0 critical, 0 major, 0 minor. No Latin characters at all (the 1-18 Latin "a" was already fixed in draft 5). 37 block IDs (32 blocks + 5 headings) match the source in order; no CRLF.

**Terminology (mechanical):** `check_termbase_consistency.py --lang mn --grade-file bo_mn_keyword_general.json` → 136/136 locked renderings found (0 loose, 1 covered by a longer locked phrase at a-1, 0 drift). Limit: the grade file has no locked words for 2-2, 2-4 and 2-6, so the script cannot see them; they were read by hand.

**Archaic-particle scan:** no лугаа, хийгээд or болмуй. Classical forms found and flagged below: бөгөөс (2-1), -вээс (2-6), үргэлжид (1-12).

**Settled decisions respected (not errors):** the refrain мөргөмүй and the noun мөргөл (word list); 1-1 lotus from the face (consensus #1); 1-3 seven items incl. сахил / билиг; 1-5 three realms; 1-7 amid the fire (Tenkal); 1-8 дүрэ; 1-11 ядуурал (Tenkal); 1-14 seven levels; 1-17 Бигжид; 1-19 kings serve her; 1-21 three suchnesses set; 1-22 "and"; 2-1 охин тэнгэр (word list, flagged for the reviewer); 2-6 optative; the nine draft-5 consensus fixes.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| I-2 | Accuracy/Mistranslation | Minor | *мөргөх хорин нэгэн магтаал* ("twenty-one praises of homage"). The Tibetan is one praise made of twenty-one homages. | *Дарь эхэд хорин нэгэн мөргөлөөр магтсан магтаал, ач тусын хамт* ("the praise to Tārā in twenty-one homages, with its benefits") | Tibetan I-2 སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ; English "The Praise to Tara in Twenty-One Homages, with Its Benefits" |
| 1-2 | Accuracy/Mistranslation | Minor | *Үнэнхүү дэлгэрсэн* ("truly spread"). རབ་ཏུ is "fully, intensely", not "truly"; *үнэнхүү* is this file's word for ཡང་དག (2-1). | *Машид дэлгэрсэн гэрэл бадрагч танаа* ("blazing with fully opened light") | Tibetan 1-2 རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ |
| 1-17 | Accuracy/Mistranslation | Minor | *Хум-ын дүрт үр бүхий* ("having a seed in the form of HŪṂ"). ཉིད་མ says she *is* the seed, as 1-16 *зул болсон* ("who became / is the lamp"). | *Хумын дүрт үр болсон* ("you who are the seed in the form of HŪṂ"), with the hyphen fix below | Tibetan 1-17 ཧཱུྃ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ; English "Whose essence is the seed-syllable in the form of hum" |
| 1-21 | Accuracy/Addition | Minor | *дүрэ дээд хутагт* ("Ture, supreme noble one"). *хутагт* ("ārya, noble") is not in the Tibetan; རབ་མཆོག is "most supreme". | *Дарагч, дүрэ, дээдийн дээд танаа* ("Ture, highest of the high, who destroys") | Tibetan 1-21 འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ; English "You are the supreme Ture who destroys" |
| 1-6 | Terminology | Minor | *босоолой* for རོ་ལངས ("vetāla"). The lock is the stem *босоо*; the word list's form is *босоо үхдэл* ("risen corpse"). *босоолой* is neither the hint nor a draft form, and a reader may not know it. | *Чөтгөр, босоо үхдэл, үнэр идэгчид болон* ("spirits, vetālas, gandharvas and") | word list `vetala`: hint *босоо үхдэл*; Tibetan 1-6 རོ་ལངས |
| 1-21 | Terminology | Minor | Same *босоолой*. | *Ад, босоо үхдэл болон хорлогчдын чуулганыг* ("the hosts of demons, vetālas and yakṣas") | word list `vetala`; Tibetan 1-21 གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས |
| 1-6 | Fluency | Minor | *өмнөөс магтаал өргөгдсөн* — in modern Mongolian *өмнөөс* most often means "on behalf of", so the line can read "praised on (your) behalf". The Tibetan is "praised before you". | *Хорлогч чуулганаар өмнө тань магтаал өргөгдсөн танаа* ("you, praised before you by the hosts of yakṣas") | Tibetan 1-6 མདུན་ནས་བསྟོད་མ; English "Praised before you by spirits" |
| 1-16 | Fluency | Minor | *хум-ээс* ("from HŪṂ") breaks vowel harmony: *хум* is a back-vowel word, so the ablative is *-аас*. It is also hyphenated (see LocaleConvention rows). | *Увидас тарнийн хумаас зул болсон танаа* ("the lamp from the HŪṂ of the knowledge-mantra") | Khalkha vowel harmony; mn consensus fix 1-16 wording kept |
| 2-3 | Fluency | Minor | *Түргэнээ* ("quickly") — an odd reflexive-dative form for the adverb; 1-1 uses plain *түргэн*. | *Түргэн авшиг хүртэх болно* ("will quickly receive empowerment") | Tibetan 2-3 མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར |
| 2-4 | Fluency | Minor | *Бат орших ба эсвэл хөдлөх* ("stationary and or moving") — *ба* ("and") and *эсвэл* ("or") stacked for one འམ. | *Бат орших эсвэл хөдлөх* ("stationary or moving") | Tibetan 2-4 བརྟན་གནས་པའམ་གཞན་ཡང་འགྲོ་བ |
| 1-12 | Style/Register | Minor | *Үргэлжид* ("always") is the literary/classical form; the contract asks for modern grammar. | *Үргэлж машид гэрэл цацруулагч танаа* ("constantly radiates intense light") | style.md "modern grammar"; Tibetan 1-12 རྟག་པར; English "Constantly radiates" |
| 2-1 | Style/Register | Minor | *хэн бөгөөс* ("whoever") uses the classical conditional *бөгөөс*. | *Ухаан төгс хэн боловч сайтар өгүүлснээр* ("any wise one who recites it well") | style.md "no archaic particles"; Tibetan 2-1 བློ་ལྡན་གང་གིས |
| 2-6 | Style/Register | Minor | *өгүүлвээс* ("if one recites") — classical conditional *-вээс*; modern Khalkha after -л is *-бэл*. | *илт өгүүлбэл* ("if one recites clearly") | style.md "modern grammar"; Tibetan 2-6 མངོན་པར་བརྗོད་ན |
| 1-15 | LocaleConvention | Minor | *ум-тай* — suffixes on mantra syllables are hyphenated in 1-15, 1-16, 1-17, 1-18, 1-20 but attached directly in 1-7 (*падаар*) and 1-10 (*Дүдарэгийн*). Khalkha attaches case suffixes directly to Cyrillic words; the hyphen is for numerals and non-Cyrillic forms. | *умтай* ("with oṃ") | file-internal: 1-7 *падаар*, 1-10 *Дүдарэгийн* |
| 1-17 | LocaleConvention | Minor | *Хум-ын* (same). | *Хумын* ("of HŪṂ") | as above |
| 1-18 | LocaleConvention | Minor | *дарэ-г* (same). | *дарэг* ("tāra", accusative) | as above |
| 1-20 | LocaleConvention | Minor | *хара-г*, *дүдарэ-гээр* (same). | *хараг*, *дүдарэгээр* ("hara" accusative; "with tuttāre") | as above |

### Neutral (logged, not scored)

| Verse | Note |
|---|---|
| All | The line-final *танаа* ("to you") is a liturgical form, used in all 21 homages, like the refrain *мөргөмүй*. Not changed; the native reviewer may confirm. |
| 1-3 | *дияан* (dhyāna): the reviewer should confirm the spelling (also written *диян*). *уснаа ургасан* ("water-born") is the traditional epithet, kept by the Phase 2 fix. |
| 1-4 | *Түүнчлэн ирсэн* capitalised, mid-line; settled wording from the fact-check. |
| 1-9 | *чухаг дээд гурав* ("the three rare and supreme") and *мутарлага* ("mudrā") are old liturgical words; a general reader may know *Гурван эрдэнэ* better. For the reviewer. |
| 1-13 | ཕྲེང་བ is *хэлхээ* ("garland") in 1-10 and *хүрээ* ("ring") in 1-13; both read well for their images. |
| 1-14, 1-16 | *бутниргэгч* ("shatterer"): spelling (one word or *бут ниргэгч*) for the reviewer. |
| 1-22 | *билээ* (literary "it is") is mild and stays. |
| 2-2 | *бүх айдасгүйг хайрлана* ("grants all fearlessness") uses the adjective as a noun, as liturgical Mongolian does for abhaya. |
| 2-5 | *ч бас* ("also") doubles "also"; common in speech. |
| a-0 | *Зохиогчийн тэмдэглэл* ("author's note") for མཛད་བྱང ("colophon"); the reviewer may prefer *Цохолбор*. |
| Tooling | The grade file has no locked words for 2-2, 2-4, 2-6. |

### Top fixes
1. 1-6 / 1-21: use the word list's *босоо үхдэл* for the vetālas.
2. 1-17 and 1-21: *үр болсон* ("who is the seed"); drop the added *хутагт*.
3. I-2: one praise in twenty-one homages.
4. Remove the hyphens before case suffixes on mantra syllables, and fix the harmony of *хумаас*.
5. Modernise *үргэлжид*, *бөгөөс*, *-вээс*; smooth *Түргэнээ*, *ба эсвэл*, *өмнөөс*, *Үнэнхүү*.

## Re-check after fixes (draft 6) — 2026-09-25

All 17 minor rows were applied (see `qa-fixes-log-mn-general.md`); none was held back. Neutral rows were not applied.

**Stage 0 (mechanical):** `mqm_mechanical_checks.py <file> --source <root>` → 32 distinct verse IDs, 32 transclusions, 0 critical, 0 major, 0 minor. Gate: PASS-so-far.

**Alignment:** `check_translation_alignment.py` → OK (32 segments, 5 headings, every block mirrors the root; line counts unchanged). **Linter:** `lint_text_input.py` → OK (warnings only on the free-text translator field, no BDRC/OP id).

**Terminology (mechanical):** `check_termbase_consistency.py --lang mn` → 136/136 locked renderings found, 0 loose, 0 drift. By reading: *босоо үхдэл* now matches the word-list hint in 1-6 and 1-21; no hyphenated suffixes remain.

**Remaining errors:** none scored. The 11 Neutral rows stay for the native reviewer.

**Word count:** 584 Mongolian words (581 + 3 from the fixes).

**Score:** 100 − (0 / 584) × 100 = **100.0 / 100**   **Gate:** PASS (0 critical, 0 major, 0 minor)
**Profile:** all dimensions 0 · Neutral 11 (unchanged, not scored)

Still an LLM self-check, not a sign-off; the file stays `status: draft` for the native reviewer.
