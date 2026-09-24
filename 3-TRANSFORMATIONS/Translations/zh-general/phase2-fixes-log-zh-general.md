---
title: Phase 2 fixes log — Chinese (general)
file_type: report
translation: bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh-general.md
base: 3-TRANSFORMATIONS/Translations/Dharmamitra/zh-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-zh.md
date: 2026-09-24
---

# Phase 2 fixes log — Chinese, general grade

Draft 1 is the glossary-primed DharmaMitra output. Draft 2 keeps its wording and changes only what is listed below.

- **locked-word**: a word from the Chinese word list was missing.
- **error**: the Chinese said something the Tibetan does not, checked against the Tibetan and the fact-checked English.
- **heading**: DharmaMitra leaves headings in Tibetan.

| Check | Draft 1 | Draft 2 |
|---|---|---|
| Locked words found (check_termbase_consistency.py --lang zh) | 122/137 (89%) | **137/137 (100%)** |
| Latin letters outside the Sanskrit title line | 0 | 0 |
| Line count per block = Tibetan | yes | yes |

| Block | Type | Draft 1 | Draft 2 | Why |
|---|---|---|---|---|
| 0 | heading | # སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ། — DharmaMitra zero-shot (modern chinese) | # 二十一度母禮讚文 | Title: the attested Chinese title (17th Karmapa office), as in the zero-shot zh track. |
| I-0 | heading | ## མཚན་དོན་དང་འགྱུར་ཕྱག | ## 釋題與譯者敬禮 | Heading translated (DharmaMitra left headings in Tibetan); homage → 敬禮 (locked). |
| I-2 | locked-word | 藏語：度母二十一禮讚文及其功德。 | 藏語：以二十一偈敬禮度母的讚頌及其功德。 | homage 敬禮 was missing (DharmaMitra 禮讚文); now says what the Tibetan says: a praise of Tara by twenty-one homages, with its benefits. |
| I-3 | locked-word | 唵，敬禮至尊聖度母。 | 嗡，敬禮至尊聖度母。 | om: 唵 → 嗡 (locked). |
| 1-0 | heading | ## བསྟོད་པ་དངོས། | ## 讚頌正文 | Heading translated; actual_praise → 讚頌正文 (locked). |
| 1-1 | error | 敬禮度母，迅捷勇猛者， / 雙目猶如剎那閃電光， / 三界怙主蓮花面容中， / 花蕊綻放之處所化生。 | 敬禮度母，迅捷勇猛者， / 雙目猶如剎那閃電光， / 三世界怙主面容所生蓮花， / 從其花蕊綻放之中化現者。 | world: 三界 → 三世界 (locked; 三界 is ཁམས་གསུམ). Also fixed the lotus: DharmaMitra put her in the Lord's "lotus face"; all four commentaries read 1-1 as the lotus that arose from the Lord's face (settled in the English fact-check), so 面容 (face) and 蓮花 (lotus) are now separate. |
| 1-5 | locked-word | 敬禮都達咧吽字， / 充滿欲界方隅空， / 踏碎七種世界者， / 能令無餘盡召集。 | 敬禮以都達咧與吽字， / 充滿欲界、十方與虛空， / 以足踏住七個世界， / 能令無餘盡召集。 | feet 足 was missing: 踏碎七種世界 ("crush") → 以足踏住七個世界 (ཞབས་ཀྱིས་མནན, press down with the feet). Line 1 made clear ("with the syllables…"); line 2 punctuated. |
| 1-6 | error | 敬禮帝釋火神梵， / 風神諸自在供養， / 鬼神羅剎乾闥婆， / 夜叉眾前讚頌者。 | 敬禮帝釋、火神、梵天， / 風神與諸自在天供養者， / 鬼神、起屍、乾闥婆， / 夜叉眾前讚頌者。 | vetala: DharmaMitra wrote 羅剎 (rākṣasa, a different being) for རོ་ལངས → 起屍 (locked). Names punctuated for clarity. |
| 1-8 | locked-word | 敬禮都咧大怖畏， / 摧毀魔軍勇猛者， / 蓮花面容現忿怒， / 殺盡一切諸怨敵。 | 敬禮都咧大怖畏， / 摧毀魔軍勇猛者， / 蓮花面容現忿怒， / 無餘誅殺一切怨敵。 | without_exception 無餘 was missing (མ་ལུས): 殺盡一切諸怨敵 → 無餘誅殺一切怨敵. |
| 1-11 | error | 敬禮能召諸眾生， / 守護大地諸神眾， / 忿怒顰眉吽字中， / 解脫一切諸貧困。 | 敬禮守護大地諸神眾， / 一切皆能召集者， / 忿怒顰眉吽字中， / 解脫一切諸貧困。 | DharmaMitra had "summon all beings / guardians of the earth" as two things; the Tibetan is one: she can summon all the hosts of earth-guardians (ས་གཞི་སྐྱོང་བའི་ཚོགས). Lines 1–2 rewritten; 眾 and 能 kept. |
| 1-14 | error | 敬禮以手擊大地， / 並以足踏震動者， / 忿怒顰眉吽字中， / 摧毀七界諸障礙。 | 敬禮以手擊大地， / 並以足踏震動者， / 忿怒顰眉吽字中， / 摧毀七層者。 | Line 4: 摧毀七界諸障礙 added 障礙 ("obstacles"), which is not in the Tibetan (རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་མ); now 摧毀七層, matching the English decision "the seven levels". |
| 1-16 | error | 敬禮周遍極喜者， / 摧毀一切敵軍身， / 安住十字咒語中， / 吽字覺性明燈者。 | 敬禮周遍極喜者， / 摧毀一切敵軍身， / 安住十字咒語中， / 從明咒吽字生起的明燈。 | Line 4: 吽字覺性明燈 read རིག་པ as 覺性 ("awareness"); here it is the knowledge-mantra (vidyā), as in the English and the classical 明呪吽聲 → 從明咒吽字生起的明燈. |
| 1-17 | error | 敬禮都咧足踏處， / 吽字種子形相者， / 須彌曼達與瓶山， / 震動三界一切處。 | 敬禮都咧頓足者， / 吽字種子形相者， / 須彌山、曼陀羅山與頻闍山， / 令三世界皆震動。 | world: 三界 → 三世界 (locked). Line 3: 瓶山 ("vase mountain") is wrong for འབིགས་བྱེད → 頻闍山 (Vindhya, the canon's name), as in the English translator note; 曼達 → 曼陀羅山. Line 1 clarified (stamping her feet). |
| 1-18 | error | 敬禮天海形相者， / 手中執持月亮印， / 誦二達咧呸字咒， / 消除一切諸毒害。 | 敬禮手持形如天湖、 / 帶有鹿紋的月亮者， / 誦二達咧呸字咒， / 消除一切諸毒害。 | Lines 1–2: DharmaMitra made her "the form of a celestial lake"; the Tibetan says the moon she holds has that form (as in the English). The "deer-marked" moon kenning is kept (鹿紋). |
| 1-19 | error | 敬禮天眾之尊者， / 諸天與緊那羅依， / 具足喜樂鎧甲威， / 消除爭鬥與惡夢。 | 敬禮天眾之王所侍奉， / 諸天與緊那羅所依止者， / 具足喜樂鎧甲威， / 消除爭鬥與惡夢。 | Line 1: DharmaMitra made her "lord of the gods"; the English (fact-checked) reads her as served by the kings of the hosts of gods → 天眾之王所侍奉. Line 2 completed (所依止者). |
| 1-20 | locked-word | 敬禮日月圓滿相， / 雙目放射極明光， / 誦二哈拉都達咧， / 消除極猛傳染病。 | 敬禮日月圓滿相， / 雙目放射極明光， / 誦二喝囉與都達咧， / 消除極猛傳染病。 | hara: 哈拉 → 喝囉 (locked). |
| 1-21 | error | 敬禮安住三真如， / 圓滿具足寂靜力， / 邪魅羅剎夜叉眾， / 摧毀都咧最勝者。 | 敬禮安住三真如， / 圓滿具足寂靜威力者， / 邪魅、起屍、夜叉眾， / 摧毀它們的最勝都咧。 | might: 寂靜力 → 寂靜威力 (locked). vetala: 羅剎 → 起屍 (locked; རོ་ལངས). Line 4 made clear: she is the supreme Ture who destroys them. |
| 2-0 | heading | ## བསྟོད་པའི་ཕན་ཡོན། | ## 讚頌的功德 | Heading translated; praise 讚頌 and benefits 功德 (locked). |
| 2-1 | error | 若有具足虔誠心， / 對此天女作讚頌， | 若有智者對此天女具足虔敬， / 以至誠之心念誦此讚， | DharmaMitra dropped བློ་ལྡན ("an intelligent person") and turned "recites" into "praises"; now 若有智者 … 念誦. 天女 and 具足 kept. |
| 2-6 | error | 若能誦持二、三、七遍， / 求子者即得子嗣， / 求財者即得財富， / 一切所願皆能圓滿， / 障礙消除並被各別摧毀。 | 若能誦持二、三、七遍， / 求子者即得子嗣， / 求財者即得財富， / 一切所願皆能圓滿， / 願無障礙，一一摧毀。 | Last line: 障礙消除並被各別摧毀 was awkward and missed the optative; the translator decision for the English (2-6) follows our root's འཇོམས་འགྱུར་ཅིག ("may…") → 願無障礙，一一摧毀. |
| a-0 | heading | ## མཛད་བྱང། | ## 題記 | Heading translated (colophon). |

## For the meaning check (next step)

These were **not** changed in Phase 2. They are left for the check against the commentary consensus:

- 1-5 line 2 (欲界、十方與虛空): the English, after the fact-check, reads "the desire, form, and formless realms". The Chinese keeps the literal Tibetan ("desire, the directions, and space").
- 1-7 line 2 (摧毀一切外道輪): 外道 ("non-Buddhists") for ཕ་རོལ ("adversaries"); the English reads "the magical wheels of adversaries".
- 1-2 line 1 (秋季百月齊聚時): 時 ("when") is not in the Tibetan.
- 1-3 line 3 (苦行): the English reads "discipline".
