---
title: Handoff — translate the Praise to the Twenty-One Tārās into a new language
file_type: guide
audience: anyone (with Claude) adding a new language
maintainer: Tenkal (DevOps lead, WeBuddhist)
updated: 2026-09-28
---

# How to translate the Twenty-One Tārās into a new language

This guide is for anyone who wants to add a language. You work **together with Claude**
(Claude Code or Claude Cowork, opened on this vault). Claude does most of the checking.
Your part is to make four decisions, run one script on your own computer, and check the
result with a native reader.

Seven languages have already been through this process, and you can copy from any of them:

| Language | Folder | Status |
|---|---|---|
| English | `Translations/en-general/` | draft 4, QA passed |
| Chinese (Traditional) | `Translations/zh-general/` | draft 5, QA passed |
| Vietnamese | `Translations/vi-general/` | draft 5, QA passed |
| Hindi | `Translations/hi-general/` | draft 5, QA passed |
| Nepali | `Translations/ne-general/` | draft 6, QA passed |
| Mongolian (Cyrillic) | `Translations/mn-general/` | draft 6, QA passed |
| Thai | `Translations/th-general/` | draft 6, QA passed; not yet a platform language |

See [[00-INDEX-current-translations]] for the current file in each language and which checks it has had.

---

## 1. The idea in one paragraph

We do not just ask an AI to translate. Plain AI translations of this praise all make the same
mistakes. The best-known one is in verse 1-1: the draft says the Lord has "a lotus face", but
the lotus actually grows *from* his face. So instead we:

1. fix a **word list** first (one agreed word for each key Buddhist term);
2. give that list to Gemini while it translates;
3. check every verse against **four Tibetan commentaries** and the checked English;
4. put the translation back into English to be sure the meaning came through;
5. score it with **QA** (the MQM method).

A native speaker then reads it before it is published.

---

## 2. Before you start

**You need:**

- This vault (`21-taras-rails`) and the skills repo (`Webuddhist-Skills`) **in the same parent
  folder**. The scripts look for `../Webuddhist-Skills`.
- Python 3 on your computer.
- Your **own Gemini API key** (from Google AI Studio). Two rules for it:
  - **Never** paste the key into any file, note, commit or chat you intend to share.
  - The run script asks for it with hidden input and never writes it down. If a key has been
    exposed, rotate it.
- Ideally, a **native reader** of your language who can review the result at the end.

**Check that the platform supports your language.** The WeBuddhist library currently accepts:
`bo, en, zh, lzh, hi, mr, ne, mn, vi, fr, ja, ru, pi, sa`. The list is cached in
`4-SYSTEM/scripts/linter-root-text/languages.py`. If your language is not on it (Thai, for
example), you can still translate, but it cannot be uploaded until the platform adds it. Ask
Tenkal.

**House rules:**

- Don't delete files. Move them to `_archive/` or a `_to_delete/` folder instead.
- Don't commit unless the project owner says so. Leave changes uncommitted and list what changed.
- When a change makes a note out of date (the index, `STATE.md`, frontmatter, an `about.md`),
  update that note in the same step.
- Every output keeps the Tibetan **block IDs** (`^1-1`, `^2-6`, …) and the same number of lines
  per verse. Nothing is added that the Tibetan does not say.

---

## 3. Four decisions only you can make

Write these down before anything else. Claude records them in the word list's `_meta.choices`.

1. **Script and spelling.** For example: Traditional or Simplified Chinese; Cyrillic or
   traditional Mongolian script.
2. **Style.** The usual choice is `general`: clear modern language for a general Buddhist
   reader, devotional but not archaic. A chantable, metrical version would be a different
   track.
3. **Mantra syllables.** Keep them as they are chanted, in your script or in Latin letters
   (OM, TĀRE, TUTTĀRE, TURE, SVĀHĀ, HŪṂ, PHAṬ). They are never translated.
4. **Who decides the unclear words.** Either you decide them one by one, or you tell Claude to
   "go with your picks", and Claude writes down its reason for each.

Also decide which established vocabulary your readers expect. For example: Pāli-derived words
for Thai, Sanskritised words for Hindi, liturgical words such as Дарь эх and мөргөмүй for
Mongolian.

---

## 4. The steps

`<tgt>` below means your language's ISO code (for example `fr`, `ja`, `ru`, `mr`).
`$KEYWORDS` means `0-INBOX/AI_translation/keyword-extraction-dharmamitra/`.
`$SK` means `../Webuddhist-Skills/rails/`.

### Step 0 — A plain first draft (only if nothing exists yet in your language)

Claude sets up `Translations/Gemini/<tgt>/`, with a `style.md` and a `run-<tgt>.sh` script
(copy `Gemini/th/`). You run the script on your computer:

```bash
bash 3-TRANSFORMATIONS/Translations/Gemini/<tgt>/run-<tgt>.sh
```

The script asks for your key, picks the best Gemini Pro model, and handles the usual macOS
certificate problem. This plain draft is the second opinion for the word list. In Thai, for
example, it showed that the model uses its word for Māra (བདུད) where the Tibetan means harmful
spirits (གདོན), so we locked a different word.

### Step 1 — The word list (skill: `keyword-standardize`)

Ask Claude: *"Build the `<tgt>` word list with keyword-standardize."*

- It starts from the English word list: **51 key Tibetan terms**, each tied to the verses where
  it is locked.
- For each term, it lays out the evidence (the meaning, related-language lists, the plain
  draft) in `$KEYWORDS/<tgt>/<tgt>-worksheet-general.md`.
- It chooses **one word per term**, with a source and a reason, in
  `$KEYWORDS/<tgt>/<tgt>-decisions-general.json`. This is the one file a person edits.
- It builds the termbase, the per-verse grade file, the review table
  (`termbase-<tgt>-general.md`, unclear picks first) and the glossary (`glossary-<tgt>-general.tsv`).

**Two lessons from earlier languages:**

- **Stems and hints.** If a word changes form in a sentence (vowels drop, words join), lock a
  short *stem* so the checker can find it. Add a `hint` holding the full word, so the model
  sees the full word and not the stem. Mongolian needed this for гэр/гэрэл, Thai for
  นุภาพ/พลานุภาพ, and Nepali for महा.
- **Clashes.** Check that no locked word also means something else in the text. The Thai
  zero-shot wrote the word for Māra where the Tibetan means afflicting spirits.

Then Claude takes a **baseline**: how many of the locked places (136 in most languages) the plain draft already
gets right.

```bash
python3 $SK/graded-translate/scripts/check_termbase_consistency.py --lang <tgt> \
    --grade-file $KEYWORDS/<tgt>/bo_<tgt>_keyword_general.json \
    --translation <draft .md>
```

### Step 2 — The primed Gemini run (you run it)

Claude sets up `Translations/Gemini/<tgt>-general/` with `style.md`, `glossary.tsv`,
`context-header.md` and `run-<tgt>-general.sh` (copy `Gemini/th-general/`). You run:

```bash
bash 3-TRANSFORMATIONS/Translations/Gemini/<tgt>-general/run-<tgt>-general.sh
```

Each verse is sent to Gemini together with the words locked for that verse. Then tell Claude
it has finished. Past results out of 136 locked places:

| Language | Plain draft | Primed run |
|---|---|---|
| Nepali | 126 | 128 |
| Mongolian | 117 | 121 |
| Thai | 122 | 132 |

### Step 3 — Swap in the missed words (skill: `graded-translate` Phase 2)

Claude copies the primed run into `Translations/<tgt>-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-<tgt>-general.md`,
puts the missed locked words into their verses (target: every locked place, e.g. **136/136**), fills in the frontmatter,
and logs every change in `reports/phase2-fixes-log-<tgt>-general.md`.

### Step 4 — Meaning check (back-translation)

Claude puts each verse back into literal English and compares it with the checked English
(`en-general`), its translator decisions and the English commentary consensus. Each verse is
marked match, minor or differs, and every difference is fixed. Output:
`reports/back-translation-check-<tgt>-general.md`.

### Step 5 — Four-commentary fact-check (skill: `commentary-fact-check`)

Four Claude agents run in parallel, one for each commentary in
`1-SOURCES/Commentaries/New raw data/`:

- Drakpa Gyaltsen — `bo-རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན།.md`
- Gendun Drub — `bo-རྒྱལ་བ་དགེ་འདུན་གྲུབ།.md`
- Tāranātha — `bo-ཏཱ་ར་ན་ཐ།.md`
- Tenga Tulku — `bo-བསྟན་དགའ་སྤྲུལ་སྐུ།.md`

Each agent writes `reports/commentary-fact-check-report-<commentary>-<tgt>-general.md`.
Claude then writes a **consensus** and applies the fixes. The rules:

- **Fix** when 3 or 4 commentaries agree, or when the change restores the root's wording or
  grammar.
- **Leave** it when only one commentary raises the point, or when a settled decision (below)
  covers it.

Outputs: `…-consensus-<tgt>-general.md` and `…-fixes-log-<tgt>-general.md`.

Steps 4 and 5 can run in either order. English, Nepali and Mongolian did the meaning check
first; Thai did the commentary check first.

### Step 6 — QA (skill: `translation-qa`)

This is an MQM score: 100 − (weighted errors ÷ words) × 100. The weights are:

- Minor: 1
- Major: 5
- Critical: 10

Any Major or Critical error means **FAIL**, whatever the score.

The QA writes `reports/qa-report.md` (runs are appended and never overwritten). Claude applies
the fixes and logs them in `reports/qa-fixes-log-<tgt>-general.md`. For languages without
spaces between words (Thai, Japanese, Chinese), the word count needs a word splitter; Thai used
PyThaiNLP.

### Step 7 — Final checks, notes, review, upload

Claude runs the three checks:

```bash
python3 4-SYSTEM/scripts/check_translation_alignment.py            # block IDs, TOC, line counts
python3 $SK/graded-translate/scripts/check_termbase_consistency.py --lang <tgt> \
    --grade-file $KEYWORDS/<tgt>/bo_<tgt>_keyword_general.json \
    --translation 3-TRANSFORMATIONS/Translations/<tgt>-general/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-<tgt>-general.md
python3 4-SYSTEM/Skills/translation-qa/mqm_mechanical_checks.py <translation .md> \
    --source 1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md
```

Claude updates these notes:

- the row in [[00-INDEX-current-translations]];
- `$KEYWORDS/STATE.md`;
- the translation's frontmatter (`draft`, `draft_history`, `fact_check_*`, `qa_*`, `note`);
- the language column in `$KEYWORDS/standardised-keywords-general.md` (`multilingual_table.py`).

Then:

- **Native review.** A native reader goes through it. Start them with the unclear words in
  `termbase-<tgt>-general.md` and the lines listed in the fixes logs. Ask them to read it aloud,
  because it is chanted. The file stays `status: draft` until then.
- **Upload.** Use the `translation-upload` skill. Always do a **dry run first**, and never use
  `--execute` without the owner's explicit OK. Before uploading, run the linter
  (`4-SYSTEM/scripts/linter-root-text/lint_text_input.py`).

---

## 5. Settled decisions — follow these, don't re-open them

The English translator and the project owner have already decided these. The commentary check
treats them as correct.

| Verse | Decision |
|---|---|
| 1-1 | The lotus grows **from the Lord's face** (not "the Lord's lotus face") |
| 1-3 | The colours (gold and blue) belong to the lotus; the list includes discipline and **wisdom** |
| 1-4 | The **bodhisattvas** attained the perfections |
| 1-5 | Desire, form and formless **realms** |
| 1-7 | She blazes **amid** fire (not "like" fire) |
| 1-8, 1-17, 1-21 | **Ture** is her name, not a syllable |
| 1-9 | Her **palm** bears the wheel |
| 1-11 | **Destitution** (poverty), not general hardship |
| 1-14 | The **seven levels** |
| 1-17 | Mount **Vindhya** |
| 1-19 | The kings of the gods **serve her** |
| 1-21 | The three suchnesses are **set upon her** |
| 1-22 | Root-mantra praise **and** the twenty-one homages (two items, "and") |
| 2-3 | **Seventy million** (seven koṭi) Victors |
| 2-6 | The last line is a wish: "**may** obstacles be absent, each one destroyed" |

**Mistakes the machine drafts keep making. Look for these:**

- **1-1:** the lotus face.
- **Homage wording.** In some languages the wording "homage with the syllables…" / "homage
  with the mudrā…" makes the syllables or gesture the *reciter's*. They are hers, so the line
  should read "homage to her who, with the syllables, …". Thai had this in 1-2, 1-5, 1-7 and 1-9.
- **Similes attached to the wrong thing.** Examples:
  - 1-13: the fire garland is like the aeon fire; she is not the fire.
  - 1-18: the moon is like a lake.
  - 1-20: her *eyes* are like the sun and moon.
- **1-3:** "austerity" is written where "discipline" belongs.
- **1-6:** "Śiva" is written where the Tibetan has many Īśvaras.
- **1-16:** the draft has her reciting the mantra; the mantra is set in her.
- **2-5:** "endure the suffering" is written where the suffering should be removed.
  Mongolian had this.

---

## 6. What you end up with

```
3-TRANSFORMATIONS/Translations/
├── Gemini/<tgt>/                  plain draft (if you made one)
├── Gemini/<tgt>-general/          primed run + run script, style, glossary
└── <tgt>-general/
    ├── bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-<tgt>-general.md    ← the translation
    └── reports/                   phase2 log, back-translation, 4 commentary reports,
                                   consensus, fixes logs, qa-report, qa fixes log
0-INBOX/AI_translation/keyword-extraction-dharmamitra/<tgt>/   the word list and its builds
```

---

## 7. A prompt to start with Claude

Copy this into Claude, opened on the vault. Fill in the brackets.

> I want to add **[language]** (`[code]`) to the Twenty-One Tārās translations. Please read
> `3-TRANSFORMATIONS/HANDOFF-translate-into-a-new-language.md` and follow it.
> My four choices:
> 1. script [ … ];
> 2. style `general`;
> 3. mantras [as chanted in … script];
> 4. unclear words: [I decide / go with your picks].
>
> Use the [Thai / Nepali / Mongolian] track as the model. I'll run the Gemini scripts myself on
> my computer, so never ask me to paste my API key into a file. Don't commit anything; list
> what changed at each step and keep the notes up to date.

Questions: Tenkal (tenzinkalden@webuddhist.com).
