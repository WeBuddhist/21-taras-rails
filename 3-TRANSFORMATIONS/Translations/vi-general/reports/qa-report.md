---
title: QA report — Vietnamese (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-vi-general.md
skill: translation-qa (MQM, Webuddhist-Skills/rails/translation-qa/SKILL.md)
note: Runs are appended, dated. Never overwrite an earlier run.
---

# QA report — Vietnamese, general grade

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-vi-general.md (draft 4) — 2026-09-24

This is an LLM self-check (Claude). It is not a sign-off. A native Vietnamese reader and a domain specialist decide. The file stays `status: draft`.

**Score:** 98.2 / 100   **Gate:** PASS (0 critical, 0 major; 18 minor)
**Profile:** Accuracy/Mistranslation 3 · Accuracy/Addition 2 · Terminology 5 · Fluency 4 · Style/Register 2 · Audience 1 · LocaleConvention 1 · Markup/BlockID 0 · Neutral 9 (not scored)
**Word count:** 998 Vietnamese syllables (space-separated tokens in headings and blocks; transclusion lines and block IDs left out).
**Score formula:** 100 − (18 × 1 / 998) × 100 = 98.2.

**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy is scored against the Tibetan critical edition (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the Vietnamese consensus (`vi-general/reports/commentary-fact-check-consensus-vi-general.md`), the English consensus (`en-general/reports/commentary-fact-check-consensus-en-general.md`) and the fact-checked English (`en-general/bo-…-en-general.md`) as the meaning reference. The Hindi consensus (`hi-general/reports/commentary-fact-check-consensus-hi-general.md`) was compared for fixes that may carry over. Every accuracy judgement below cites one of these. Nothing is from memory.

**Requirements basis:** there is no `requirements.md` for this track. The contract is the **general** row for Vietnamese in `graded-translate/SKILL.md` § Registers: "Modern standard Vietnamese. Common Sino-Vietnamese Buddhist terms used freely (Phật, Pháp, Bồ Tát, từ bi, hồi hướng). Flowing prose."

**Stage 0 (mechanical):** clean. `$HOME/qa/stage0-vi.json` reports 0 critical, 0 major and 112 minor "latin characters in content". These are false positives: the check was written for Devanagari tracks, and Vietnamese is written in Latin script. They are not counted. A re-check here confirms: 37 block IDs (32 blocks + 5 headings) match the source one for one and in order; all 32 transclusions point to the right block; no CRLF.

**Terminology (mechanical):** `check_termbase_consistency.py --lang vi --strict-diacritics` → 137/137 locked renderings found, 0 loose, 0 drift. Mantras are Latin without diacritics as the word list says (Om, Hum, Tuttare, Trat, Phat, Ture, Soha, Tare, Hara); the Sanskrit title in I-1 stays IAST, as the word list says. Limit: the grade file has no locked words for 2-2 and 2-4, and no entry at all for 2-6, so the script cannot see those verses. Two drifts there were found by reading (see below).

**Diacritics:** all 427 distinct syllables were read. No missing or wrong tone marks. Tone placement is the older style throughout (hỏa, thủy, hủy, úy) and is consistent.

**Translator decisions respected (not errors):** 1-21 tam chân như; 1-11 thần hộ địa / nghèo khó; 1-14 bảy tầng; 1-8 đại uy mãnh; Nữ Thần; khởi thi; the English decisions on 1-3, 1-8, 1-17, 1-22, 2-6.

**Hindi carry-over check:**
- 1-19 — the kings serve her: already right. *được các vua của chúng trời phụng sự* ("served by the kings of the hosts of gods"; *các vua* is plural). Tibetan ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ། ལྷ་དང་མིའམ་ཅི་ཡིས་བསྟེན་མ.
- 2-2 / 2-4 — recollecting her, not "this": no error. *Nhờ nhớ nghĩ* ("through recollecting") names no object, like the Tibetan དྲན་པས. See Neutral.
- 1-20 — the simile belongs to her eyes: already right. *có đôi mắt rực rỡ, / Tỏa quang minh như mặt trời, mặt trăng tròn đầy* ("whose two eyes are brilliant, radiating light like the full sun and moon").
- 1-16 / 1-21 — བཀོད "set": already right. *được an bày* ("arranged, set") and *an lập* ("established, set").
- 1-9 — འཁྲུག and the locked word for འབར (Hindi fix #4): **applies**. See below.
- 1-10 — "all" added before the world (Hindi fix #8): **applies**. See below.
- 1-14 — "strikes" (Hindi fix #10): **applies**. See below.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| 1-9 | Accuracy/Mistranslation | Minor | *Tỏa ánh hào quang tự thân rực rỡ* ("radiates her own brilliant light"). The Tibetan says her masses of light *swirl* (འཁྲུག); "masses" and "swirl" are lost. *rực* is the locked word for འབར "blaze", not for འཁྲུག. The same fix was made in Hindi. | *Tỏa khối hào quang tự thân cuộn xoáy* ("radiates the swirling mass of her own light"; *cuộn xoáy* is already used for འཁྲུགས in 1-7) | Tibetan 1-9 རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ; English "Radiating a turbulent mass of her own light"; Hindi consensus #4 |
| 1-12 | Accuracy/Mistranslation | Minor | *vô lượng quang minh* ("immeasurable light"). The Tibetan says "intense light" (ཤིན་ཏུ་འོད). "Immeasurable" echoes Amitābha's name, not this line. | *Thường hằng phóng chiếu quang minh mãnh liệt* ("constantly radiates intense light") | Tibetan 1-12 རྟག་པར་ཤིན་ཏུ་འོད་ནི་མཛད་མ; English "Constantly radiates an intense light" |
| 1-14 | Accuracy/Mistranslation | Minor | *Vỗ mặt đất* ("pats / claps the ground"). *vỗ* is too soft for བསྣུན "strike". The same fix was made in Hindi. | *Đập xuống mặt đất* ("strikes the ground") | Tibetan 1-14 ཕྱག་གི་མཐིལ་གྱིས་བསྣུན; English "who strike the surface of the earth"; Hindi consensus #10 |
| 1-10 | Accuracy/Addition | Minor | *cùng toàn thế giới* ("and the whole world"). *toàn* ("whole") is not in the Tibetan. The Hindi removed the same addition. | *Nhiếp phục ác ma cùng thế giới* ("subdues the māras and the world") | Tibetan 1-10 བདུད་དང་འཇིག་རྟེན་དབང་དུ་མཛད་མ; English "Brings maras and the world under your power"; Hindi consensus #8 |
| 2-4 | Accuracy/Addition | Minor | *lỡ ăn vào hay lỡ uống vào* ("accidentally eaten or accidentally drunk"). *lỡ* ("by mistake") is not in the Tibetan. | *Dù đã ăn vào hay đã uống vào* ("whether eaten or drunk") | Tibetan 2-4 ཟོས་པ་དང་ནི་འཐུངས་པ་ཉིད་ཀྱང་; English "Even those that have been eaten or drunk" |
| 2-2 | Terminology | Minor | *Hủy diệt hoàn toàn* ("utterly annihilates") for འཇོམས. The word list locks འཇོམས to *tiêu diệt* ("destroy"), used in 1-7, 1-8, 1-13, 1-15, 1-21. The grade file has no locked words for 2-2, so the script cannot catch it. | *Tiêu diệt hoàn toàn tất thảy ác đạo* ("utterly destroys all lower realms") | Tibetan 2-2 ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ; word list `destroy`: འཇོམས → tiêu diệt |
| 2-6 | Terminology | Minor | *từng cái đều tận diệt* ("each one is wiped out") for འཇོམས་འགྱུར. Same drift from *tiêu diệt*. 2-6 has no entry in the grade file. | *từng thứ đều bị tiêu diệt* ("each one is destroyed") — see also the next row | Tibetan 2-6 སོ་སོར་འཇོམས་འགྱུར་ཅིག; word list `destroy` |
| 2-3 | Terminology | Minor | *Đấng Như Lai Tôn Thắng* ("the Tathāgata Victorious Ones"). The Tibetan has only རྒྱལ་བ "Victors". *Như Lai* is this file's word for དེ་བཞིན་གཤེགས་པ (1-4). *Tôn Thắng* is also the name of Uṣṇīṣavijayā (consensus note). | *bảy mươi triệu Đấng Chiến Thắng* ("seventy million Victorious Ones") | Tibetan 2-3 རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས; English "Seventy million Victorious Ones"; vi consensus, Leave table, 2-3 "Tôn Thắng" |
| 1-4 | Terminology | Minor | *Chư Bồ-tát* ("the bodhisattvas"). The general-grade contract spells it *Bồ Tát*. Meaning is right (vi consensus fix #1). The hyphen follows the file's style for transliterations. | *Chư Bồ Tát*, or record the hyphen style as a file-wide decision | graded-translate § Registers, vi general row and term table (bodhisattva → Bồ Tát) |
| 1-15 | Terminology | Minor | *Niết-bàn* ("nirvāṇa"). The contract's general spelling is *niết bàn*; *Niết-bàn* is the advanced-row form. | *niết bàn tịch diệt*, or decide the spelling once with 1-4 | graded-translate § Registers, term table (nirvana: general *niết bàn*, advanced *Niết-bàn*) |
| 1-1 | Fluency | Minor | *Độ Mẫu nhanh chóng* ("Tārā quickly / speedy"). *nhanh chóng* describes actions, not a person, so it reads oddly as her epithet. | *Kính lễ Độ Mẫu mau lẹ, dũng mãnh* ("Homage to Tārā, swift and heroic") | Tibetan 1-1 སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ; English "the swift and heroic" |
| 1-6 | Fluency | Minor | Capitals are uneven in one list of proper names: *Hỏa thần*, *Phong thần* ("Agni", "Vāyu") beside *Phạm Thiên*, *Đế Thích* ("Brahmā", "Indra"). | *Hỏa Thần*, *Phong Thần* | — |
| 1-18 | Fluency | Minor | *Tiêu trừ toàn bộ không sót mọi chất độc* ("removes entirely, without exception, every poison"). Three "all" words stacked for one མ་ལུས. | *Tiêu trừ mọi chất độc không sót* ("removes every poison without exception"; keeps the locked *không sót*) | Tibetan 1-18 དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ |
| 2-2 | Fluency | Minor | *tất thảy mọi ác nghiệp … tất thảy mọi ác đạo* ("all every misdeed … all every lower realm"). *tất thảy* and *mọi* both mean "all"; one ཐམས་ཅད each time. | *Tiêu trừ hoàn toàn tất thảy ác nghiệp, / Tiêu diệt hoàn toàn tất thảy ác đạo* ("thoroughly removes all misdeeds, / utterly destroys all lower realms") | Tibetan 2-2 སྡིག་པ་ཐམས་ཅད … ངན་འགྲོ་ཐམས་ཅད |
| 2-4 | Style/Register | Minor | *độc tố* ("toxin") is a modern scientific word. The same དུག is *chất độc* ("poison") in 1-18 and *độc* in 2-5. | *Dù là những chất độc rất hung hiểm* ("even very fierce poisons") | Tibetan 2-4 དུག་ནི་དྲག་པོ་ཆེན་པོ; 1-18 *chất độc* |
| 2-6 | Style/Register | Minor | *từng cái* ("each thing"): *cái* is the everyday classifier for objects and is a light register slip in a prayer line. | *từng thứ* or *mỗi mỗi* ("each one"), with the fix in the 2-6 Terminology row | contract: "Modern standard Vietnamese" |
| a-0 | Audience | Minor | *Lạc khoản* ("colophon") is mainly the signature on a painting or calligraphy. A general reader may not know it as a text's closing note (མཛད་བྱང). | *Lời kết* ("closing words") or *Hậu ký* ("afterword") | Tibetan a-0 མཛད་བྱང; English "Colophon" |
| 1-17 | LocaleConvention | Minor | *núi Tu-di, Mạn-đà, núi Vindhya* mixes Sino-Vietnamese spellings with a Latin name in one line. *Mạn-đà* also cuts the three-syllable མན་དཱ་ར short. | *núi Tu-di, núi Mandara, núi Vindhya* (or one system for all three) | Tibetan 1-17 རི་རབ་མན་དཱ་ར་དང་འབིགས་བྱེད; English "Mount Meru, Mandara, and Vindhya" |

### Neutral (logged, not scored)

| Verse | Note |
|---|---|
| 2-2, 2-4 | *Nhờ nhớ nghĩ* ("through recollecting") names no object, like དྲན་པས. Not the Hindi error ("this"). Optional for the reviewer: *nhờ nhớ nghĩ đến ngài* ("through recollecting her"). |
| 1-12 | *ngự trên búi tóc* ("seated on the topknot"); the Tibetan རལ་པའི་ཁྲོད་ན is "amid the matted locks". Optional: *ngự giữa búi tóc*. |
| 1-16 | *mọi kẻ thù* ("all enemies"): *mọi* is light; Tibetan དགྲ་ཡི་ལུས. |
| 2-4 | དེ་ཡི "their" (poisons) is not rendered; meaning holds. |
| 1-3 | *sen thủy sinh* ("water-born lotus"): literal for ཆུ་ནས་སྐྱེས; *thủy sinh* can read as the biology word "aquatic". |
| 2-2 | *thức dậy lúc chạng vạng* ("waking at dusk") follows ལངས literally; a reader may find waking at dusk odd. |
| 1-22 | Turned into a full sentence (*Đây là lời tán thán…*, "This is the praise…"); 2-1 *những lời tán thán này* ("these praises") links back. Meaning holds. |
| General | Audience: *khởi thi*, *đảnh kế*, *hành xứ*, *tam chân như* are technical for a general reader. They are decided or flagged in the frontmatter; the native reviewer should judge. |
| Tooling | The grade file `bo_vi_keyword_general.json` has no entry for 2-6. Add it so the termbase check covers every block. |

### Top fixes
1. 1-9: restore the swirling mass of light (*cuộn xoáy*) and stop using *rực* for འཁྲུག.
2. 1-10 and 2-4: drop the two additions, *toàn* ("whole") and *lỡ* ("by mistake").
3. 1-14: *vỗ* → *đập* ("strike"); 1-12: *vô lượng* → *mãnh liệt* ("intense").
4. 2-2 and 2-6: use the locked *tiêu diệt* for འཇོམས, and add 2-6 to the grade file.
5. Decide the spelling of *Bồ Tát* / *niết bàn* once for the whole file, and fix the stacked "all" words in 1-18 and 2-2.


## Re-check after fixes (draft 5) — 2026-09-24

16 of the 18 minor rows were applied (see `qa-fixes-log-vi-general.md`). Not applied: 1-4 *Bồ-tát* and 1-15 *Niết-bàn* — the word list has no entry for either, so the file keeps its current forms (1-4 is also the exact wording of vi consensus fix #1). Neutral rows were not applied.

**Stage 0 (mechanical):** `mqm_mechanical_checks.py <file> --source <root>` → 32 distinct verse IDs, 32 transclusions, 0 critical, 0 major, 112 minor. All 112 are "latin characters in content", false positives for Vietnamese (Latin script). Not counted. Gate: PASS-so-far.

**Alignment:** `check_translation_alignment.py` → OK (32 segments, 5 headings, every block mirrors the root). **Linter:** `lint_text_input.py` → OK.

**Terminology (mechanical):** `check_termbase_consistency.py --lang vi --strict-diacritics` → 137/137 locked renderings found, 0 loose, 0 drift. By reading: 2-2 and 2-6 now use *tiêu diệt* for འཇོམས (outside the lock's verse scope; scope question listed in the fixes log).

**Remaining errors:** 1-4 Terminology Minor (*Bồ-tát*), 1-15 Terminology Minor (*Niết-bàn*) — kept by rule, open to a word-list decision.

**Word count:** 992 Vietnamese syllables (998 − 6 from the fixes).

**Score:** 100 − (2 × 1 / 992) × 100 = **99.8 / 100**   **Gate:** PASS (0 critical, 0 major; 2 minor)
**Profile:** Accuracy 0 · Terminology 2 · Fluency 0 · Style/Register 0 · Audience 0 · LocaleConvention 0 · Markup/BlockID 0 · Neutral 9 (unchanged, not scored)

Still an LLM self-check, not a sign-off; the file stays `status: draft` for the native reviewer.
