---
name: Tara-Plan-Creator
description: Generates one daily practice-plan file for each requested day of the Tara practice cycle — the full Zabtig Drolchok sadhana, the day's Tara (image, name, praise stanza, introduction), a never-repeated story of Tara, the full 21-Praises recitation, and a YouTube-links placeholder — saved as "Day-<N> Tara Plan.md" in 3-TRANSFORMATIONS/Plans/21-Day-Plans-bo. Trigger only on an explicit user command to run this skill — e.g. "run this skill", "run Tara-Plan-Creator", or the `/Tara-Plan-Creator` command. Do not trigger on generic wording like "make a plan" or "create a Tara plan" alone.
creator: Tigerboy
---

# Tara-Plan-Creator

Produces the daily plan file for one or more days of the 21-day Tara practice cycle, entirely in Tibetan, by transcluding fixed source material rather than retyping it. It exists so every day's plan is assembled identically — same five task headings, same sadhana, same full recitation, correct Tara-of-the-day, and a story that is never repeated across the 21 days — without any human having to re-copy long liturgical text by hand (which is exactly where transcription errors creep in).

"Correct output" means: five `##` headings in a fixed order, four of which transclude untouched source blocks/files (never retyped text), the fifth (Task 5) left as a bare heading, and a story number that has not been used by any other day file in the output folder.

---

## Inputs

| Input                                         | Path                                                               | Notes                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Day number(s)                                 | user request                                                       | Entirely determined by what the user asks for at the time the skill is run — one day, several named days, a range, or a full 1–21 batch. Never assume a default; if the user's command to run this skill doesn't say which day(s), ask before generating anything. Whatever days are requested, each day N (1–21) maps 1:1 to Tara number N. |
| Sadhana (Task 1)                              | `1-SOURCES/Sadhana/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md`                         | One file, identical every day. Whole-file transclusion.                                                                                                                                                                                                                                                                                      |
| Tara images (Task 2)                          | `0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/`            | 21 PNGs, filenames prefixed `01_` … `21_`. See the reference table below.                                                                                                                                                                                                                                                                    |
| Drolma introductions (Task 2)                 | `0-INBOX/21-Drolma-Introductions/`                                 | 21 sets of three language versions per Tara (English, Chinese, and Tibetan files); this skill only ever uses the `(Tibetan)` file. Filenames prefixed `01 ` … `21 `. See the reference table below.                                                                                                                                                        |
| 21-Praises root text (Task 2 stanza + Task 4) | `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`                 | One file, identical every day for Task 4. Individual homage stanzas are block-referenced `^1-1` … `^1-21`, one per Tara, in order.                                                                                                                                                                                                           |
| Stories of Tara (Task 3)                      | `0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md` | 28 numbered stories as `###` headings under `## ལོ་རྒྱུས་དངོས།`. Each heading carries its own Obsidian block ID (`^1-N-0`), and its content sits in one or more separately block-ID'd paragraphs immediately below the heading. **Transclude by block ID only — never by heading text** (see Rule 3). See the story reference table below.   |
| Existing day files                            | `3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/*.md`                     | Read before assigning a story number, to avoid repeats.                                                                                                                                                                                                                                                                                      |

If any source file or the image/introduction pair for a Tara cannot be found exactly, stop and report the missing item — do not substitute or guess.

---

## Output

`3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/Day-<N> Tara Plan.md` — one file per requested day, `<N>` unpadded (`Day-1 Tara Plan.md`, `Day-2 Tara Plan.md`, … `Day-21 Tara Plan.md`).

Never write anywhere under `1-SOURCES/` or `0-INBOX/`. Never overwrite an existing `Day-<N> Tara Plan.md` — if it already exists, skip it, report the conflict, and ask before regenerating.

---

## Output file format

```markdown
---
plan: Tara-Plan-Creator
day: <N>
tara_number: <N>
tara_name_bo: "<Tara's name, copied verbatim from the introduction file's first line>"
story_number: <k>
generation_date: <YYYY-MM-DD>
status: draft
---

# ཉིན་<N>་པའི་སྒྲོལ་མའི་ལག་ལེན།

## ཟབ་ཏིག་སྒྲོལ་ཆོག

![[1-SOURCES/Sadhana/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md]]

## དེ་རིང་གི་སྒྲོལ་མ

### སྐུ་བརྙན

![[0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/<NN>_<image filename>.png]]

### མཚན

<Tara's name, copied verbatim from the introduction file's first line>

### བསྟོད་པའི་ཚིགས་བཅད

**![[1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md#^1-<N>]]** <praise citation, from the reference table>

### ངོ་སྤྲོད

![[0-INBOX/21-Drolma-Introductions/<NN> <English name> (Tibetan).md]]

## སྒྲོལ་མའི་ལོ་རྒྱུས

![[0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md#^<story's heading block ID, from the reference table>]]

![[0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md#^<story's content block ID, from the reference table>]]

## སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ་ཁ་ཏོན

![[1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md]]

## སྒྲོལ་མའི་སློབ་ཁྲིད་ཡུ་ཊུབ་སྦྲེལ་མཐུད
```

The last section (Task 5) ends the file with nothing after its heading — no link, no note, no placeholder text. `<N>` and `<NN>` are the same day/Tara number, unpadded and zero-padded respectively.

**Praise-stanza citation:** the transclusion for Task 2's stanza is wrapped directly in `**...**` (the double asterisks sit immediately against the `!` of the embed on one side and the closing `]]` on the other — no space inside them), and is followed by one space and a citation of the fixed form `སྒྲོལ་བསྟོད། ༡-<N in Tibetan numerals>`. This citation is generated by the skill, not copied from source text: `སྒྲོལ་བསྟོད།` and the leading `༡-` are fixed, and `<N in Tibetan numerals>` is the day/Tara number converted to Tibetan numerals. Use the exact citation string from the **Praise citation** column of the reference table below rather than converting N by hand.

**Stories with more than one content block:** two stories in the 28 — story 16 and story 21 — have a second content paragraph under its own block ID, immediately following the first. For those two stories only, add one more transclusion line — `![[0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md#^<second content block ID>]]` — directly after the first content line, in the order given in the reference table. Every other story has exactly one content transclusion line.

---

## Reference table — Tara images and introductions (Day = Tara number)

| Day | Image file (in `21-Surya-Gupta-Taras-Images/`) | Introduction file, Tibetan (in `21-Drolma-Introductions/`) | Praise block | Praise citation (skill-generated) |
|---|---|---|---|---|
| 1 | `01_DROLMA NYURMA PAMO སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། - Edited - Edited.png` | `01 Tara the Swift, the Heroine (Tibetan).md` | `^1-1` | `སྒྲོལ་བསྟོད། ༡-༡` |
| 2 | `02_DROLMA OKAR CHEN སྒྲོལ་མ་འོད་དཀར་ཅན། - Edited.png` | `02 Tara the Radiant, Treasury of Wisdom (Tibetan).md` | `^1-2` | `སྒྲོལ་བསྟོད། ༡-༢` |
| 3 | `03_DROLMA SERDOG CHEN སྒྲོལ་མ་གསེར་མདོག་ཅན། - Edited.png` | `03 Tara of Golden Light (Tibetan).md` | `^1-3` | `སྒྲོལ་བསྟོད། ༡-༣` |
| 4 | `04_DROLMA DESHIN SHEGPA TSUGTOR CHEN སྒྲོལ་མ་དེ་བཞིན་གཤེགས་པ་གཙུག་ཏོར་ཅན། - Edited.png` | `04 Tara Victorious, Crown of the Buddhas (Tibetan).md` | `^1-4` | `སྒྲོལ་བསྟོད། ༡-༤` |
| 5 | `05_DROLMA HUNGDRA DROKMA སྒྲོལ་མ་ཧཱུྃ་སྒྲ་སྒྲོག་མ། - Edited.png` | `05 Tara Who Roars with HUM (Tibetan).md` | `^1-5` | `སྒྲོལ་བསྟོད། ༡-༥` |
| 6 | `06_DROLMA JIGTEN SUMGYALMA སྒྲོལ་མ་འཇིག་རྟེན་གསུམ་རྒྱལ་མ། - Edited.png` | `06 Tara the Great Terror to Every Evil Force (Tibetan).md` | `^1-6` | `སྒྲོལ་བསྟོད། ༡-༦` |
| 7 | `07_DROLMA RABJOMA སྒྲོལ་མ་རབ་འཇོམས་མ། - Edited.png` | `07 Tara Whom None Can Overcome (Tibetan).md` | `^1-7` | `སྒྲོལ་བསྟོད། ༡-༧` |
| 8 | `08_DROLMA DUDJOM WANGCHUKMA སྒྲོལ་མ་བདུད་འཇོམས་དབང་ཕྱུག་མ། - Edited.png` | `08 Tara the Great Vanquisher of Fear (Tibetan).md` | `^1-8` | `སྒྲོལ་བསྟོད། ༡-༨` |
| 9 | `09_SENGDENG NAGKYI DROLMA སེང་ལྡེང་ནགས་ཀྱི་སྒྲོལ་མ། - Edited.png` | `09 Tara of the Khadira Forest (Tibetan).md` | `^1-9` | `སྒྲོལ་བསྟོད། ༡-༩` |
| 10 | `10_DROLMA NYANGEN SELCHEMA སྒྲོལ་མ་མྱ་ངན་སེལ་བྱེད་མ། - Edited.png` | `10 Tara Who Subdues Maras and the World (Tibetan).md` | `^1-10` | `སྒྲོལ་བསྟོད། ༡-༡༠` |
| 11 | `11_DROLMA JIGTEN WANGDUMA སྒྲོལ་མ་འཇིག་རྟེན་དབང་སྡུད་མ། - Edited.png` | `11 Tara Who Dispels All Poverty (Tibetan).md` | `^1-11` | `སྒྲོལ་བསྟོད། ༡-༡༡` |
| 12 | `12_DROLMA TASHI NANGWA སྒྲོལ་མ་བཀྲ་ཤིས་སྣང་བ། - Edited.png` | `12 Tara Who Grants Auspicious Accomplishment (Tibetan).md` | `^1-12` | `སྒྲོལ་བསྟོད། ༡-༡༢` |
| 13 | `13_DROLMA YONGSU MINCHEMA སྒྲོལ་མ་ཡོངས་སུ་སྨིན་བྱེད་མ། - Edited.png` | `13 Tara Blazing Like Fire (Tibetan).md` | `^1-13` | `སྒྲོལ་བསྟོད། ༡-༡༣` |
| 14 | `14_DROLMA TRONYER CHENMA སྒྲོལ་མ་ཁྲོ་གཉེར་ཅན་མ། - Edited.png` | `14 Tara Whose Frown Shakes the Earth (Tibetan).md` | `^1-14` | `སྒྲོལ་བསྟོད། ༡-༡༤` |
| 15 | `15_DROLMA ZHIWA CHENMO སྒྲོལ་མ་ཞི་བ་ཆེན་མོ། - Edited.png` | `15 Tara the Great Peace (Tibetan).md` | `^1-15` | `སྒྲོལ་བསྟོད། ༡-༡༥` |
| 16 | `16_DROLMA CHAKJOMA སྒྲོལ་མ་ཆགས་འཇོམས་མ། - Edited.png` | `16 Tara Who Destroys Attachment (Tibetan).md` | `^1-16` | `སྒྲོལ་བསྟོད། ༡-༡༦` |
| 17 | `17_DROLMA DRUPAY DROLMA སྒྲོལ་མ་སྒྲུབ་པའི་སྒྲོལ་མ། - Edited.png` | `17 Tara Who Subdues the Immeasurable (Tibetan).md` | `^1-17` | `སྒྲོལ་བསྟོད། ༡-༡༧` |
| 18 | `18_NAMPAR GYALWAY DROLMA རྣམ་པར་རྒྱལ་བའི་སྒྲོལ་མ། - Edited.png` | `18 Tara the Great Peacock (Tibetan).md` | `^1-18` | `སྒྲོལ་བསྟོད། ༡-༡༨` |
| 19 | `19_DROLMA DUKNGAL SELCHEMA སྒྲོལ་མ་སྡུག་བསྔལ་སེལ་བྱེད་མ། - Edited.png` | `19 Tara Unconquerable, Full of Splendor (Tibetan).md` | `^1-19` | `སྒྲོལ་བསྟོད། ༡-༡༩` |
| 20 | `20_DROLMA NGODRUP JUNGNAYMA སྒྲོལ་མ་དངོས་གྲུབ་འབྱུང་གནས་མ། - Edited.png` | `20 Tara Clad in Leaves of the Mountain Retreat (Tibetan).md` | `^1-20` | `སྒྲོལ་བསྟོད། ༡-༢༠` |
| 21 | `21_DROLMA YONGSU DZOGCHEMA སྒྲོལ་མ་ཡོངས་སུ་རྫོགས་བྱེད་མ། - Edited.png` | `21 Tara of Rays of Light (Tibetan).md` | `^1-21` | `སྒྲོལ་བསྟོད། ༡-༢༡` |

Before using this table, confirm the two filenames it names still exist unchanged in the vault (a rename would break the transclusion silently). If a file has been renamed or added/removed, re-list the two source folders and update this table in the same edit rather than working around the mismatch.

---

## Reference table — the 28 stories (never reuse a number across the 21 days)

Heading text is given below **for human verification only** — do not build a transclusion link from it (heading-text transclusion has been observed to fail to resolve in this vault, even when copied verbatim; see Rule 3). Transclude using the block ID columns instead.

Content block IDs are **not** derivable from the story number by formula past story 15: stories 16 and 21 each contain a second content paragraph under its own block ID, which shifts every content block ID that follows out of step with the story number (e.g. story 17's content is `^1-18`, not `^1-17`). This table was built by reading every block ID directly from the source file. If the source file is ever edited — a story split, merged, added, or renumbered — re-derive this table by re-reading the file; do not patch it by formula.

| # | Heading text (verification only) | Heading block ID | Content block ID(s) |
|---|---|---|---|
| 1 | `༡. དགྲ་ཡི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-1-0` | `^1-1` |
| 2 | `༢. སེང་གེའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-2-0` | `^1-2` |
| 3 | `༣. གླང་པོའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-3-0` | `^1-3` |
| 4 | `༤. མེའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-4-0` | `^1-4` |
| 5 | `༥. དུག་སྦྲུལ་གྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-5-0` | `^1-5` |
| 6 | `༦. ཆོམ་རྐུན་གྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-6-0` | `^1-6` |
| 7 | `༧. བཙོན་རྭ་ལས་བསྐྱབས་པ།` | `^1-7-0` | `^1-7` |
| 8 | `༨. རྒྱ་མཚོའི་ཆུ་ཡི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-8-0` | `^1-8` |
| 9 | `༩. ཤ་ཟའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-9-0` | `^1-9` |
| 10 | `༡༠. མཛེ་ནད་ཀྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-10-0` | `^1-10` |
| 11 | `༡༡. དྲི་ཟའི་གདོན་གྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-11-0` | `^1-11` |
| 12 | `༡༢. དབུལ་བའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-12-0` | `^1-12` |
| 13 | `༡༣. གཉེན་དང་བྲལ་བའི་སྡུག་བསྔལ་ལས་བསྐྱབས་པ།` | `^1-13-0` | `^1-13` |
| 14 | `༡༤. རྒྱལ་པོའི་ཆད་པའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-14-0` | `^1-14` |
| 15 | `༡༥. ཐོག་གི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-15-0` | `^1-15` |
| 16 | `༡༦. དམག་གི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-16-0` | `^1-16`, `^1-17` |
| 17 | `༡༧. ཆུ་བོའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-17-0` | `^1-18` |
| 18 | `༡༨. ནད་ཡམས་ཀྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-18-0` | `^1-19` |
| 19 | `༡༩. ལྕགས་སྒྲོག་གི་བཙོན་ལས་ཐར་བ།` | `^1-19-0` | `^1-20` |
| 20 | `༢༠. འདྲེ་གདོན་གྱི་གནོད་པ་ཞི་བ།` | `^1-20-0` | `^1-21` |
| 21 | `༢༡. སྟག་གི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-21-0` | `^1-22`, `^1-23` |
| 22 | `༢༢. བྱ་ནེ་ཙོ་འོ་ལེའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-22-0` | `^1-24` |
| 23 | `༢༣. དར་ལྕོག་གི་ལོ་རྒྱུས།` | `^1-23-0` | `^1-25` |
| 24 | `༢༤. སྲས་མེད་པའི་སྡུག་བསྔལ་ལས་བསྐྱབས་པ།` | `^1-24-0` | `^1-26` |
| 25 | `༢༥. མེའི་འཇིགས་པ་ལས་བསྐྱབས་པ། (ཀོང་པོ)` | `^1-25-0` | `^1-27` |
| 26 | `༢༦. ནད་ཀྱི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-26-0` | `^1-28` |
| 27 | `༢༧. གྲོགས་མེད་པའི་སྡུག་བསྔལ་ལས་བསྐྱབས་པ།` | `^1-27-0` | `^1-29` |
| 28 | `༢༨. རུས་སྦལ་གྱིས་ཆུའི་འཇིགས་པ་ལས་བསྐྱབས་པ།` | `^1-28-0` | `^1-30` |

21 of these 28 will be used across one 21-day cycle; 7 will always remain unused, which is expected and not an error.

---

## Rules

1. **Trigger only on an explicit command to run this skill** — e.g. "run this skill", "run Tara-Plan-Creator", or the `/Tara-Plan-Creator` slash command. A generic request such as "make a plan" or "create a Tara plan" is not by itself a trigger; wait for the explicit command.
2. **How many plans to create, and for which day(s), depends entirely on the user's stated requirement at the time they run this skill — never on a default or an assumption.** Do not default to Day 1, to "the next unfilled day," or to all 21. If the run command doesn't say which day(s), stop and ask before generating anything.
3. **Never rewrite, retranslate, paraphrase, summarize, or re-key any source text.** Every task except the "Name" line uses Obsidian transclusion — whole-file `![[path.md]]` or block `![[path.md#^block-id]]` — so the plan file inherits the source's own bold/italic/small-text formatting exactly, with zero retyping. **Never transclude by heading text** (`![[path.md#Heading text]]`). This vault's own convention (`4-SYSTEM/CLAUDE.md` §5) makes block IDs the sole mechanism for cross-file references at this level, and heading-text transclusion has been observed to fail to resolve in this vault even when the heading text is copied verbatim from the source.
4. **The "Name" line is the one exception** — Obsidian has no line-level transclusion, so it is the only text copied by hand. Copy it character-for-character from the introduction file's first line; do not translate, shorten, or add honorifics.
5. **Task 1 (sadhana) and Task 4 (21-Praises recitation) are identical every day** — the same two whole-file transclusions, unabridged, for every day generated.
6. **Task 2's image, name, praise stanza, and introduction all correspond to Tara number = day number**, per the reference table. Day 1 → Tara 01 … Day 21 → Tara 21. Never skip, reorder, or repeat a Tara. The praise-stanza transclusion is wrapped in `**...**` with no inner space, followed by one space and the skill-generated citation `སྒྲོལ་བསྟོད། ༡-<N in Tibetan numerals>` — copy this citation string exactly from the **Praise citation** column of the reference table, never hand-converted (see the note under Output file format).
7. **Task 3's story number must never repeat across the 21 days.** Before assigning a story to day N, collect the `story_number:` frontmatter value from every existing `Day-*.md` file already in the output folder, and from every day already assigned earlier in the same run if generating a batch. Choose only from the 28 numbers not yet used.
8. **Task 3 is transcluded by block ID, never by heading text.** Look up the assigned story's heading block ID and content block ID(s) in the story reference table; for stories 16 and 21, transclude both content blocks in order (see the note under Output file format). Confirm each block ID exists at that exact spelling in the source file before writing — do not assume it from the table alone (see the Completion check).
9. **Task 5 gets only its heading.** No link, no text, no placeholder — content is added later by hand from YouTube.
10. **Exactly five `##` headings, one per task, in Task 1→5 order** (with the four `###` sub-headings under Task 2 for image / name / stanza / introduction). No other `##` heading appears anywhere in the file.
11. **Never write to any file under `1-SOURCES/` or `0-INBOX/`.** This skill only reads from them.
12. **Never overwrite an existing `Day-<N> Tara Plan.md`.** If the target already exists, skip that day, report the conflict, and ask before regenerating it.
13. **Run every item in the Completion check below and confirm each box before writing the file to disk** — not after. A plan is not saved until it has passed the checklist.

---

## Procedure

1. **Resolve scope from the user's command.** How many plans to create, and for which day(s), depends entirely on what the user asked for when they ran this skill — never on a default. Read their command for the specific day(s): a single day, a named list, a range, or all 21. If the command to run this skill doesn't specify which day(s), stop and ask rather than guessing (e.g. defaulting to Day 1 or to all 21 would both be wrong assumptions).
2. For each requested day N, in order:
   a. Zero-pad N to two digits as `NN`.
   b. Check `3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/` for an existing `Day-N Tara Plan.md`. If it exists, skip this day and note the conflict for the final report.
   c. Look up Day N's row in the **Tara reference table** above; confirm the named image file and `(Tibetan)` introduction file are both still present in their folders (Rule 4 / table footnote). If either is missing or renamed, stop and report — do not guess a substitute filename.
   d. Read the introduction file's first line and copy it verbatim as the Tara's name.
   e. Collect every `story_number:` already used — from existing files in the output folder and from any day already processed earlier in this same run — and pick an unused number 1–28. Look up its heading block ID and content block ID(s) in the **story reference table** above; confirm each ID exists at that exact spelling in the source file (do not transclude by heading text — Rule 3/8).
3. Assemble the file from the **Output file format** template, substituting N, NN, the image filename, the copied name, `^1-N`, the day's praise citation string (from the **Praise citation** column of the reference table), the introduction filename, and the chosen story's heading block ID and content block ID(s) (two content lines for stories 16 and 21, one for every other story).
4. Run the **Completion check** below in full for this day's content. Fix anything that fails before proceeding — do not save with an unchecked box.
5. Write the assembled content to `3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/Day-N Tara Plan.md`.
6. Re-read the file back from disk and confirm it matches what was written (this vault's file mount has shown intermittent write/sync glitches elsewhere; catch it here rather than leaving a silently-empty or stale plan). If the re-read does not match, write again and re-verify before moving on.
7. After all requested days are done, report to the user: which day files were created, which story number each one used, and any day that was skipped because its file already existed.

---

## Completion check

Run this checklist and confirm every box **before** writing the file (Rule 13) — it is the fact-check gate, not a post-hoc note.

- [ ] Day number N is within 1–21, and no `Day-N Tara Plan.md` already exists in the output folder (or the existing-file conflict has been reported and generation for that day stopped).
- [ ] The image file named in the plan is the exact, currently-existing filename from `21-Surya-Gupta-Taras-Images/` for Tara N (checked against the folder, not assumed from the table alone).
- [ ] The introduction file named in the plan is the exact, currently-existing `(Tibetan)` filename from `21-Drolma-Introductions/` for Tara N.
- [ ] The "Name" line was copied character-for-character from that introduction file's first line — no translation, no rewording, no added text.
- [ ] The praise-stanza transclusion targets `^1-N` in `bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`, and N matches the day/Tara number exactly.
- [ ] The praise-stanza transclusion is wrapped in `**...**` (asterisks immediately against `![[` and `]]`, no inner space) and is followed by one space and the exact citation string from the **Praise citation** column of the reference table for day N — never a hand-converted numeral.
- [ ] Task 1 and Task 4 transclude the complete, unmodified sadhana and 21-Praises source files — nothing abridged, nothing retyped.
- [ ] The assigned story number is not used by any other file currently in `3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/`, and not used by any other day already generated in this same run.
- [ ] The story is transcluded by block ID (never heading text): the heading block ID and every content block ID (two for stories 16 and 21, one otherwise) match the assigned story number in the reference table, and each block ID has been confirmed to exist at that exact spelling in the source file — not merely assumed from the table.
- [ ] All five task headings are `##`, appear exactly once each, in Task 1→5 order, with the exact Tibetan wording from the template; Task 2's four sub-items are `###`.
- [ ] Task 5's section contains only its heading — nothing else.
- [ ] Frontmatter (`day`, `tara_number`, `tara_name_bo`, `story_number`, `generation_date`, `status`) is present and correct.
- [ ] No file under `1-SOURCES/` or `0-INBOX/` was created, edited, or deleted.
- [ ] After writing, the file was re-read from `3-TRANSFORMATIONS/Plans/21-Day-Plans-bo/Day-N Tara Plan.md` and confirmed to match the assembled content.
