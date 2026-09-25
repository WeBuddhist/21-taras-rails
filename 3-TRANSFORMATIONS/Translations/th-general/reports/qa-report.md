---
title: QA report — Thai (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-th-general.md
skill: translation-qa (MQM, Webuddhist-Skills/rails/translation-qa/SKILL.md)
note: Runs are appended, dated. Never overwrite an earlier run.
---

# QA report — Thai, general grade

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-th-general.md (draft 5) — 2026-09-25

This is an LLM self-check (Claude). It is not a sign-off. A native Thai reader and a domain specialist decide. The file stays `status: draft`.

**Score:** 98.7 / 100   **Gate:** PASS (0 critical, 0 major; 13 minor)
**Profile:** Accuracy/Mistranslation 2 · Accuracy/Addition 1 · Terminology 3 · Fluency 7 · Style/Register 0 · Audience 0 · LocaleConvention 0 · Markup/BlockID 0 · Neutral 5 (not scored)
**Word count:** 973 Thai words (Thai has no spaces between words: headings and blocks tokenised with PyThaiNLP `newmm`; transclusion lines and block IDs left out).
**Score formula:** 100 − (13 × 1 / 973) × 100 = 98.7.

**Rails basis:** `2-RAILS/Verses/` is empty for this text. Accuracy is scored against the Tibetan critical edition (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`), the Thai consensus and back-translation reports (`th-general/reports/`), the English consensus and the fact-checked English as the meaning reference.

**Requirements basis:** no `requirements.md`; Thai has no row in `graded-translate/SKILL.md` § Registers. The contract is the track's style file `Gemini/th-general/style.md`: clear modern Thai for a general Thai Buddhist reader, devotional but not archaic; Pāli-derived Buddhist words; Sanskrit names in Thai script; royal/religious vocabulary for Tārā's body; mantras in Thai script as chanted; ผีร้าย for གདོན; no glosses.

**Stage 0 (mechanical):** clean. `mqm_mechanical_checks.py <file> --source <root>` → 32 distinct verse IDs, 32 transclusions, 0 critical, 0 major, 0 minor.
**Terminology (mechanical):** `check_termbase_consistency.py --lang th --grade-file bo_th_keyword_general.json` → 136/136 (1 loose, 1 covered at a-1, 0 drift). The grade file has no locked words for 2-2, 2-4 and 2-6; read by hand.

**Settled decisions respected (not errors):** the word list (นอบน้อม, พระแม่ตารา, อารย, สงบ, ผีร้าย …); the draft-4 consensus fixes and draft-5 meaning-check fixes; 1-3 colours on the lotus; 1-5 three realms; 1-7 amid fire and 1-11 ความยากไร้ (Tenkal); 1-8 and 1-17 Ture as her name; 1-14 seven levels; 1-17 Vindhya (เขาพินธัย); 1-19 kings serve her; 1-21 suchnesses set on her; 1-22 'and'; 2-6 optative.

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| I-2 | Accuracy/Mistranslation | Minor | ขอนอบน้อม…ทั้งยี่สิบเอ็ดประการ reads 'praise of homage to Tārā, all twenty-one kinds'. The Tibetan is one praise made by twenty-one homages (…ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ). | บทสรรเสริญพระแม่ตาราด้วยการขอนอบน้อมยี่สิบเอ็ดบท พร้อมด้วยอานิสงส์ ('the praise to Tārā by twenty-one homages, with its benefits') | Tibetan I-2; English 'The Praise to Tara in Twenty-One Homages, with Its Benefits' |
| 1-1 | Fluency | Minor | ในฉับพลัน ('suddenly') is an odd tail for a simile; the Tibetan is simply 'eyes like a flash of lightning' (གློག་ལྟར). | พระเนตรดุจฟ้าแลบแปลบปลาบ ('eyes like flashing lightning') | Tibetan 1-1 སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ; English 'like a flash of lightning' |
| 1-3 | Fluency | Minor | สีน้ำเงินทอง can read as one colour ('golden-blue'); the lotus is gold and blue (སེར་སྔོན). | ดอกบัวสีทองและสีน้ำเงินที่เกิดจากน้ำ ('a gold and blue water-born lotus') | Tibetan 1-3 སེར་སྔོན་ཆུ་ནས་སྐྱེས་པའི་པདྨ; English 'gold and blue' |
| 1-4 | Fluency | Minor | กระทำชัยชนะ ('do victory') is not idiomatic Thai; 'complete' (རྣམ་པར) is missing. | ผู้ทรงดำเนินด้วยชัยชนะโดยสิ้นเชิงอันไม่มีที่สิ้นสุด ('who act with infinite, complete victory') | Tibetan 1-4 མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ; English |
| 1-7 | Fluency | Minor | ปั่นป่วน is 'churning, upset' (stomach, mind); fire is not described this way in Thai. | ท่ามกลางกองเพลิงที่โหมกระหน่ำ ('amid a raging, swirling mass of fire') | Tibetan 1-7 མེ་འབར་འཁྲུགས་པ; English 'swirling mass of fire' |
| 1-12 | Terminology | Minor | พระเมาลี is a crown or topknot; རལ་པ is matted locks (ชฎา in Thai). | พระอมิตาภพุทธะท่ามกลางพระชฎา ('Amitābha amid her matted locks') | Tibetan 1-12 རལ་པའི་ཁྲོད་ན་འོད་དཔག་མེད; English 'From whose matted locks Amitabha' |
| 1-12 | Fluency | Minor | Line 4 had no subject after 'there is Amitābha' (มี…), so the light hung loose. | เปล่งแสงอันเจิดจ้าอย่างยิ่งอยู่เสมอ ('constantly radiates intense light' (the same fix; line 3 is now the subject)) | Tibetan 1-12 རྟག་པར་ཤིན་ཏུ་འོད་ནི་མཛད་མ |
| 1-15 | Accuracy/Addition | Minor | ทั้งปวง ('all') is added; the Tibetan is 'great misdeeds' (སྡིག་པ་ཆེན་པོ). | ผู้ทรงทำลายบาปอันยิ่งใหญ่ ('who destroy great misdeeds') | Tibetan 1-15; English 'You completely destroy great misdeeds' |
| 1-17 | Accuracy/Mistranslation | Minor | ทรงมีพยางค์พืช ('has a seed syllable'); ཉིད་མ says she is the seed, as in 1-16 'she is the lamp'. | พระองค์คือพยางค์พืชในรูปแห่ง ฮูม ('you are the seed-syllable in the form of hūṃ') | Tibetan 1-17 ཧཱུྃ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ; English 'Whose essence is the seed-syllable in the form of hum' |
| 1-21 | Fluency | Minor | ตุเร ผู้ประเสริฐสุดทรงทำลาย puts the object first and the verb last; it reads as a fragment. | ทรงทำลายผีร้าย เวตาล และหมู่ยักษ์ / พระองค์คือพระตุเรผู้ประเสริฐสุด ('you destroy demons, vetālas and hosts of yakṣas; you are the supreme Ture') | Tibetan 1-21 lines 3–4; English 'You are the supreme Ture who destroys' |
| 2-1 | Terminology | Minor | ความเคารพ is 'respect'; དད་པ is faith/devotion (ศรัทธา), and རབ་ is strong. | ผู้กอปรด้วยศรัทธาอันแรงกล้าต่อเทวี ('endowed with strong devotion to the goddess') | Tibetan 2-1 ལྷ་མོ་ལ་ནི་རབ་དད་ལྡན་པས; English 'perfect devotion' |
| 2-1 | Fluency | Minor | line 2 said 'recites the praise well'; བརྗོད་པ is to recite, and the praise is already named in 1-22; 'earnestly' reads better than 'well'. | ผู้มีปัญญาใดที่สวดสาธยายอย่างตั้งใจ ('any wise one who recites it earnestly') | Tibetan 2-1 བློ་ལྡན་གང་གིས་རབ་ཏུ་བརྗོད་པས; English 'Who recites this earnestly' |
| 2-3 | Fluency | Minor | opens with โดย ('by …'), a passive fragment; Victors (རྒྱལ་བ) is ชินเจ้า as in 1-4. | พระชินเจ้าเจ็ดโกฏิพระองค์ ('seventy million Victors') | Tibetan 2-3 རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་གྱིས; English 'Seventy million Victors' |

### Neutral (logged, not scored)

| Verse | Note |
|---|---|
| I-3 | พระอารยาผู้ประเสริฐพระแม่ตารา — the epithets come before the name; word-list wording (TT style note). Reviewer may prefer พระแม่ตาราผู้เป็นอารยาผู้ประเสริฐ. |
| 1-6 | Line 3 ends with และ, carried into line 4; forced by keeping the Tibetan line order. |
| 1-15 | โซฮา before โอม follows the root order; the English reorders. |
| 1-16 | ดวงประทีปแห่งวิทยามนตร์จากพยางค์ ฮูม follows the English 'lamp' reading of སྒྲོན་མ. |
| All | มนตรา and มนตร์ both appear (the lock is มนตร์); both are standard Thai. |
