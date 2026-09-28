---
title: QA report — Chinese (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md
skill: translation-qa (MQM)
---

# QA report — Chinese (Traditional), general grade

Runs are appended below, newest last. Never overwrite an earlier run.

## QA run — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md (draft 3) — 2026-09-24

This is an LLM self-check (Stages 0–2 of `translation-qa`). It is not a sign-off. A native Chinese reader and a specialist decide. The translation was not edited.

**Score:** 93.6 / 100   **Gate:** FAIL (0 critical, 3 major present)
**Counts:** Critical 0 · Major 3 · Minor 26 · Neutral 10
**Profile:** Accuracy/Mistranslation 8 (1 major) · Accuracy/Addition 5 · Accuracy/Omission 2 · Style/Register 7 (2 major) · Fluency 4 · Terminology 3 · Audience 0 · LocaleConvention 0 (1 neutral) · Markup/BlockID 0
**Rails basis:** `2-RAILS/Verses/` is empty for this text, so no verse rail exists. Accuracy is scored against the Tibetan critical edition (`1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`) and the English commentary consensus (`en-general/reports/commentary-fact-check-consensus-en-general.md`), with the fact-checked English (`en-general/bo-…-en-general.md`) as meaning reference and the Vietnamese and Hindi consensus files for issues already found in other languages. Chinese has had only the commentary LIGHT check, not the full four-commentary check. Every accuracy note cites a Tibetan line or a consensus row; nothing comes from memory.
**Contract:** there is no `requirements.md`. The contract is the **general** row for Chinese in `Webuddhist-Skills/rails/graded-translate/SKILL.md` § Registers: standard modern written Chinese, Traditional characters, clear sentences, no classical grammar, no lines forced to seven characters. The word list's own header says the same: "clear modern Chinese (general grade, not the chanting style)".
**Word count:** 956 Han characters in the translated content (title, headings, all verse blocks, colophon; frontmatter, block IDs and transclusion lines excluded) ÷ 1.5 = 637 words. This is a convention for Chinese, which has no spaces. Penalty 3×5 + 26×1 = 41. Score = 100 − 41/637.3×100 = 93.6.

### Stage 0 and mechanical checks

- Stage 0 (`$HOME/qa/stage0-zh.json`): 32/32 blocks, 32 transclusions, 0 critical, 0 major, 1 minor — Latin letters in I-1. That line is the Sanskrit title, kept in IAST on purpose (register rule: "A Sanskrit title line stays in IAST"). Logged as **Neutral**, no penalty.
- Terminology script (`check_termbase_consistency.py --lang zh`): **137/137 locked words found**, 0 loose, 0 misses, 1 covered by a longer locked phrase (I-1). Nothing to carry in as an error.
- Traditional characters: the whole text was run through OpenCC `s2t`. **No Simplified character found.** The only differences were 布施 → 佈施 and 布列 → 佈列, which are OpenCC's variant preference; 布施 is the standard Traditional Buddhist form. No fix needed.
- Punctuation: all full-width (，。、：). No half-width marks next to Han characters.
- Line count follows the Tibetan in every block (1-1 to 1-21: 4 lines; 1-22, 2-1: 2; 2-5: 3; 2-6: 5). Block IDs and headings are correct.
- Seven-character lines: 43 of 113 verse lines have exactly seven characters. Many are natural modern Chinese. The problem is where whole verses fall into chanting metre with classical compression (see 1-12, 2-3 and the Style/Register rows).

### Errors

| Verse | Dimension | Severity | Note | Suggested fix | Cite |
|---|---|---|---|---|---|
| 1-17 | Accuracy/Mistranslation | **Major** | Lines 3–4 須彌山、曼陀羅山與頻闍山，令三世界皆震動 ("Meru, Mandara and Vindhya make the three worlds tremble") make the mountains the subject. In the Tibetan she shakes the mountains *and* the three worlds. The same error was fixed in the Vietnamese. | 令須彌山、曼陀羅山、頻闍山 / 與三世界皆震動。 ("She makes Meru, Mandara, Vindhya / and the three worlds all tremble.") | ^1-17 རི་རབ་མན་དཱ་ར་དང་འབིགས་བྱེད། འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བ་ཉིད་མ། · en "You cause Mount Meru, Mandara, and Vindhya, / And all the three worlds to tremble" · vi consensus #6 |
| 1-12 | Style/Register | **Major** | The whole verse is four 7-character chanting lines with classical compression: 月牙冠頂飾 ("crescent-crown-top-ornament"), 阿彌陀 cut short for the metre (the register names the form 阿彌陀佛). A reader notices the switch from modern prose to chant. | 敬禮以月牙莊嚴頭頂者， / 身上一切飾物都極其熾燃， / 從她髮髻中的阿彌陀佛 / 恆常放出極其燦爛的光芒。 ("Homage to you whose head is adorned with a crescent moon, / every ornament on you blazes intensely, / from Amitābha in your locks / a brilliant light shines constantly.") | ^1-12 · graded-translate § Registers, zh general row ("no lines forced to seven characters") |
| 2-3 | Style/Register | **Major** | The whole verse is 7×4 chant style. 將速為其授灌頂 uses classical 為其; 由此獲得更殊勝 ("from this obtains more-excellent") has no noun and is not grammatical modern Chinese. | 七千萬尊佛 / 將迅速為此人授予灌頂， / 此人並獲得比這更殊勝的成就， / 最終抵達究竟的佛果。 ("Seventy million buddhas / will swiftly give this person empowerment; / this person also gains attainments greater than this, / and finally reaches ultimate buddhahood.") Keeps the locked 灌頂 and 更殊勝. | ^2-3 འདི་ལས་ཆེ་བ་ཉིད་ནི་འཐོབ་ཅིང་། སངས་རྒྱས་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ། · graded-translate § Registers, zh general row |
| 1-2 | Accuracy/Mistranslation | Minor | Lines 3–4 千顆星辰匯聚一處，放射極其熾燃的光芒 ("a thousand stars gather in one place and radiate light") become a new sentence about the stars. In the Tibetan *she* blazes with that light (-མ ending). | 她如千顆星辰匯聚， / 放射極其熾燃的光芒。 ("She, like a thousand gathered stars, / radiates an intensely blazing light.") | ^1-2 སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། · en "Blazing with the brilliant light / Of a thousand gathered stars" |
| 1-4 | Accuracy/Mistranslation | Minor | 佛子們 ("Buddha's children") is also used in modern Chinese for ordinary Buddhists. The Tibetan means bodhisattvas. The Vietnamese had the same problem (4/4 commentaries) and the Hindi chose "bodhisattva". The qualifier "who attained all perfections" softens the risk. | 諸菩薩所極力依止者。 ("deeply relied on by the bodhisattvas") | ^1-4 རྒྱལ་བའི་སྲས་ཀྱིས་ཤིན་ཏུ་བསྟེན་མ། · vi consensus #1 · hi consensus, translator's choice 1-4 |
| 1-4 | Fluency | Minor | Line 2 行持無邊、全然勝利 ("conduct boundless, completely victorious") is a loose fragment not tied to 者. | 以無邊的全然勝利而行持， ("who acts with infinite, complete victory") | ^1-4 མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། · en line 2 |
| 1-5 | Fluency | Minor | 能令無餘盡召集 ("able to cause without-remainder to fully summon"): 令 has no object, and 無餘 + 盡 say "all" twice. | 能將一切無餘召集而來。 ("able to summon all without exception") | ^1-5 ལུས་པ་མེད་པར་འགུགས་པར་ནུས་མ། |
| 1-7 | Accuracy/Mistranslation | Minor | 安住熾燃翻騰的火焰之中 ("dwells in the blazing, swirling fire") adds "dwells" and loses the predicate: *she* blazes intensely amid the fire. Fixed in the Vietnamese for the same reason. | 於翻騰的火焰中極其熾燃。 ("blazes intensely amid the swirling fire") | ^1-7 མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ། · en "Blazing amidst a swirling mass of fire" · vi consensus #7 |
| 1-8 | Accuracy/Mistranslation | Minor | 大怖畏 ("great fear") can read as her being afraid. The English fix (3 of 4 commentaries) was exactly this: she terrifies the māras. (大 is locked; 怖畏 is not.) | 敬禮都咧，令人大怖畏者， ("Homage to Ture, the one who causes great terror") | ^1-8 ཏུ་རེ་འཇིགས་པ་ཆེན་མོ། · en consensus Fix #4 |
| 1-8 | Terminology | Minor | ཁྲོ་གཉེར (wrathful frown) is 忿怒 ("wrath") here but 忿怒顰眉 ("wrathful frown") in 1-11 and 1-14. The frown is lost. | 蓮花面容現忿怒顰眉， ("shows a wrathful frown on her lotus face") | ^1-8 ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད། · en "a frowning expression" |
| 1-9 | Accuracy/Mistranslation | Minor | 熾盛 ("blazes intensely") for འཁྲུག ("stirs, swirls"). The Hindi was fixed for the same point. | 自身光聚翻騰四射者。 ("whose mass of her own light swirls and radiates") | ^1-9 རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ། · en "Radiating a turbulent mass of her own light" · hi consensus #4 |
| 1-10 | Accuracy/Addition | Minor | 光明花鬘 ("flower garlands of light") adds 花 "flower". The Tibetan is a garland of light. 1-13 uses 火鬘 correctly. | 頭冠散發光鬘， ("her crown ornament spreads garlands of light") | ^1-10 དབུ་རྒྱན་འོད་ཀྱི་ཕྲེང་བ་སྤེལ་མ། |
| 1-11 | Accuracy/Omission | Minor | 忿怒顰眉吽字中 ("wrathful frown, hūṃ-syllable, in") drops གཡོ་བ ("vibrating") and turns "with the hūṃ" into "in the hūṃ". | 以忿怒顰眉顫動中的吽字， ("with the hūṃ of the vibrating wrathful frown") | ^1-11 ཁྲོ་གཉེར་གཡོ་བའི་ཡི་གེ་ཧཱུཾ་གིས། · en "with a vibrating frown and the syllable hum" |
| 1-11 | Style/Register | Minor | 解脫一切諸貧困 ("liberate all the povertys") is chant compression: 一切 + 諸 doubled, and 解脫 takes "poverty" as its object. Three of four lines are 7-character. | 使人從一切貧困中解脫。 ("frees people from all destitution") | ^1-11 ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ་མ། · zh general row |
| 1-13 | Fluency | Minor | 周遭環繞喜悅 can read "the surroundings encircle joy". | 右伸左屈，為喜悅所環繞， ("right extended, left bent, surrounded by joy") | ^1-13 ཀུན་ནས་བསྐོར་དགས། · en "surrounded by joy" |
| 1-13 | Accuracy/Addition | Minor | 摧毀一切敵軍眾 adds 一切 ("all"); 軍 + 眾 double up. | 摧毀敵人的軍隊。 ("destroys the armies of enemies") | ^1-13 དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ། |
| 1-14 | Accuracy/Addition | Minor | 以足踏震動 ("treads with her feet, making it shake") adds 震動 "shake". The Tibetan is "pounds/tramples". | 並以雙足踐踏者， ("and tramples it with her feet") | ^1-14 ཞབས་ཀྱིས་བརྡུང་མ། · en "trample it with your feet" |
| 1-14 | Style/Register | Minor | Same chant line as 1-11: 忿怒顰眉吽字中 ("wrathful frown hūṃ-syllable in"); the instrumental "with" is lost. | 現忿怒顰眉，以吽字 ("making a wrathful frown, with the syllable hūṃ") | ^1-14 ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུྃ་གིས། |
| 1-15 | Accuracy/Addition | Minor | 摧毀一切大罪障 adds 一切 ("all"). | 摧毀大罪障。 ("destroys great negativity") | ^1-15 སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ཉིད་མ། |
| 1-16 | Accuracy/Addition | Minor | 莊嚴布列 ("adorned and arranged") adds 莊嚴 "adorned". བཀོད means "set, arranged". The Hindi was fixed for the same point. | 布列十字咒語， ("with the ten-syllable mantra arranged") | ^1-16 ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི། · hi consensus #5 |
| 1-18 | Style/Register | Minor | 誦二達咧呸字咒 ("recite two tāra phaṭ-syllable mantra") and 消除一切諸毒害 are classical compression (二 with no measure word; 一切 + 諸). 毒害 is also a different word for དུག than 毒 (2-4) and 毒物 (2-5). | 念誦兩遍達咧及呸字， / 消除所有毒物，無一遺漏。 ("reciting tāra twice and the syllable phaṭ, / you remove every poison, none left") | ^1-18 ཏཱ་ར་གཉིས་བརྗོད་ཕཊ་ཀྱི་ཡི་གེས། དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ། · vi consensus #2 (all poisons) |
| 1-19 | Accuracy/Omission | Minor | 具足喜樂鎧甲威 ("endowed with joy-armour majesty") drops ཀུན་ནས ("all-round, universal") and squeezes "majesty" into one character for the metre. | 以周遍喜樂鎧甲的威嚴， ("with the majesty of the all-round armour of joy") | ^1-19 ཀུན་ནས་གོ་ཆ་དགའ་བའི་བརྗིད་ཀྱིས། · en "your armor of universal joy" |
| 1-20 | Style/Register | Minor | 誦二喝囉 is copied from the classical canon line (termbase: "classical 1-20 誦二喝囉"). The register says not to copy classical lines. | 念誦兩遍喝囉及都達咧， / 消除極其猛烈的傳染病。 ("reciting hara twice and tuttare, / you remove the most violent infectious diseases") | ^1-20 ཧ་ར་གཉིས་བརྗོད་ཏུ་ཏྟྭ་ར་ཡིས། · zh general row ("Do not copy classical lines") |
| 2-2 | Accuracy/Mistranslation | Minor | 大無畏 ("great fearlessness") for ཐམས་ཅད ("all" fearlessness). The object of 憶念 is left out; the Hindi was fixed to say recollecting *her*. (Good: no added "always", and "dusk and dawn" is correct.) | 憶念她，即得賜予一切無畏， ("by recollecting her, one is granted every fearlessness") | ^2-2 དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར། · en "complete fearlessness through recollection" · hi consensus #1 |
| 2-3 | Terminology | Minor | 諸如來 renders རྒྱལ་བ ("Victors"), but 如來 is the file's word for དེ་བཞིན་གཤེགས་པ (1-4). Two Tibetan words merge. | 佛 or 諸佛 (see the 2-3 Major fix) | ^2-3 རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན · ^1-4 དེ་བཞིན་གཤེགས་པ · hi decision 2-3 बुद्धों |
| 2-4 | Accuracy/Mistranslation | Minor | 無論定住或遊走 ("whether staying put or wandering") can read as the person's situation. The Tibetan is stationary and moving poisons. | 無論是靜止的毒還是移動的毒， ("whether the poison is stationary or moving") | ^2-4 བརྟན་གནས་པའམ་གཞན་ཡང་འགྲོ་བ། · en "Whether stationary or moving" · vi consensus #2 |
| 2-5 | Style/Register | Minor | 此亦適用於其他眾生 ("this is also applicable to other beings"): 適用 is office/legal language in a liturgy. | 其他眾生也同樣如此。 ("it is the same for other beings too") | ^2-5 སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ་། |
| 2-5 | Terminology | Minor | རིམས is 瘟疫 ("plague") here but 傳染病 ("infectious disease") in 1-20. | 受邪魅、傳染病、毒物所苦， | ^2-5 གདོན་དང་རིམས་དང་དུག · ^1-20 རིམས |
| 2-6 | Fluency | Minor | 願無障礙，一一摧毀 can read as a command ("destroy them one by one"). | 願諸障礙皆無，一一摧毀。 ("may all obstacles be absent, each one destroyed") | ^2-6 བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག |
| I-1 | LocaleConvention | Neutral | Latin letters: the Sanskrit title in IAST, on purpose (Stage 0 minor, not penalised). | — | graded-translate § Registers ("A Sanskrit title line stays in IAST") |
| 1-3 | Accuracy | Neutral | 寂靜 and 智慧 both named, so the list has seven items. Follows the English consensus fix #3; settled. | — | en consensus Fix #3 |
| 1-9 | Accuracy | Neutral | 十方 ("ten directions") for ཕྱོགས ("directions"). 十方 is the normal Chinese for "all directions". | — | vi consensus, Leave 1-9 |
| 1-14 | Accuracy | Neutral | 七層 left open on purpose (translator note). Settled decision. | — | en consensus, Translator's choice 1-14 |
| 1-17 | Accuracy | Neutral | 頻闍山 (Vindhya) — settled translator decision with a note. | — | en consensus, Translator's choice 1-17 |
| 1-19 | Accuracy | Neutral | 天眾之王所侍奉 correctly makes her the one served (consensus #9). Chinese has no plural; 天眾諸王 ("the kings of the god-hosts") would make "kings" explicit. | optional: 天眾諸王所侍奉 | en consensus Fix #9 · hi consensus #3 |
| 1-21 | Fluency | Neutral | 它們 ("they", used for things) for the spirits; 他們 would also do. A style choice. | — | — |
| 2-1 | Terminology | Neutral | 天女 for ལྷ་མོ is flagged for the native reviewer (translator note). Settled. | — | termbase flagged pick ལྷ་མོ |
| 2-6 | Accuracy | Neutral | Optative 願… follows the root; settled translator decision. | — | en consensus, Translator's choice 2-6 |
| a-1 | Terminology (tool) | Neutral | The script counts 圓滿 as the lock for ཡང་དག་པར, but in a-1 圓滿 renders རྫོགས ("is complete"); ཡང་དག་པར sits inside 正等覺佛. The text is right; the match is a coincidence. | — | termbase ཡང་དག / ཡང་དག་པར note |

### Top fixes

1. **1-17:** make Tārā the one who shakes the mountains: 令須彌山、曼陀羅山、頻闍山 / 與三世界皆震動。
2. **1-12 and 2-3:** rewrite both verses in clear modern prose, not 7-character chant (fixes above). In 2-3, use 佛 for རྒྱལ་བ, not 如來.
3. **1-7:** she blazes amid the fire, not "dwells" in it: 於翻騰的火焰中極其熾燃。
4. **1-2:** tie the star-light back to her: 她如千顆星辰匯聚， / 放射極其熾燃的光芒。
5. **2-2:** 憶念她，即得賜予一切無畏 ("recollecting her, one is granted every fearlessness").
6. **1-4:** 佛子們 → 諸菩薩, so ordinary readers do not take it as "Buddhists".
7. Unify the words not locked in the termbase: ཁྲོ་གཉེར 忿怒顰眉 (1-8), རིམས 傳染病 (2-5), དུག 毒/毒物 (1-18). Consider locking them.

**Next step:** fix the 3 Majors, then re-run this check. The file stays `status: draft`. Because Chinese has had only the light commentary check, a full four-commentary check and a native Chinese reader are still needed before any promotion.

## Re-check after fixes (draft 4) — 2026-09-24

The fixes approved by Tenkal were applied to draft 3, giving draft 4: 3 Majors, all 26 Minors, and 6 more lines taken out of 7-character classical style (35 changes). No Neutral row was applied. See `reports/qa-fixes-log-zh-general.md`. This is still an LLM self-check, not a sign-off.

**Score:** 99.9 / 100   **Gate:** PASS (0 critical, 0 major)
**Counts:** Critical 0 · Major 0 · Minor 1 · Neutral 11
**Word count:** 1,050 Han characters in the translated content (same rule as above) ÷ 1.5 = 700 words. Penalty 0×5 + 1×1 = 1. Score = 100 − 1/700×100 = 99.9.

### Stage 0 and mechanical checks

- Stage 0 (`mqm_mechanical_checks.py <file> --source <root>`): 32 verse IDs, 32 transclusions, **0 critical, 0 major, 1 minor** — Latin letters in I-1, the Sanskrit title in IAST on purpose. Neutral, no penalty. Stage-0 gate PASS-so-far.
- Terminology (`check_termbase_consistency.py --lang zh`): **137/137 locked words found**, 0 loose, 0 misses, 1 covered by a longer locked phrase (I-1).
- Alignment (`check_translation_alignment.py`): OK — every block mirrors the root. Line count per block unchanged from draft 3 (32/32 blocks compared).
- Linter (`lint_text_input.py`): OK (WARN only for translator strings without BDRC/OP ids; INFO for optional fields).
- Traditional characters: OpenCC `s2t` finds no Simplified character. The only differences are variant preferences: 布 → 佈 (布施, 布列) and 吃 → 喫 (2-4 吃下). 吃 is the standard Traditional form in Taiwan and Hong Kong. No fix.
- Punctuation: all full-width; no half-width marks next to Han characters.
- Seven-character lines: 13 of 113 (was 43), scattered; no verse is left in chanting metre.

### Remaining items

| Verse | Dimension | Severity | Note | Cite |
|---|---|---|---|---|
| 2-3 | Accuracy/Addition | Minor | 比這更殊勝的成就 ("attainments greater than this"): 成就 is the head noun Chinese grammar needs, but the Tibetan has only ཆེ་བ་ཉིད ("greatness"). Supported by Gendun Drub (the common great siddhis, termbase note on ཆེ་བ); Taranatha reads "greater qualities". Check in the full fact-check. | ^2-3 འདི་ལས་ཆེ་བ་ཉིད་ནི་འཐོབ་ཅིང་། |
| I-1, 1-3, 1-9, 1-14, 1-17, 1-19, 1-21, 2-1, 2-6, a-1 | — | Neutral | The 10 Neutral rows of the draft-3 run stand as they were (not applied). | see run above |
| 2-4 | LocaleConvention | Neutral | OpenCC prefers 喫 to 吃; 吃 is standard Traditional. | — |

All 3 Majors and all other Minors of the draft-3 run are resolved.

**Next step:** the full four-commentary fact-check on draft 4, then a native Chinese reader. The file stays `status: draft`.
