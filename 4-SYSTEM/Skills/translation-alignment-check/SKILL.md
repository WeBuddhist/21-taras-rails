---
name: translation-alignment-check
description: Report-only structural check that every translation note of this vault's root text mirrors the Tibetan exactly — same segment references in the same order, same line count per segment, same segment types, same heading ids and levels, the same table-of-contents tree, a transclusion pointing at the same id above every block, no numeral or heading text leaking into content — and, with --payloads, that the parser's edition / toc / alignment payloads say the same; with --live, that the library's root edition still matches the root note. Run it before any translation upload and after any re-cut, re-translation or heading change.
---

# translation-alignment-check

One deterministic script, no model calls: `4-SYSTEM/scripts/check_translation_alignment.py`. It reads the root note and every translation note with the **same parser the uploader uses** (`4-SYSTEM/scripts/parser-root-text/parser.py`), so what it compares is exactly what would be uploaded, and prints one table plus every failed check with the offending ids. Exit status 0 means every translation mirrors the root.

What it proves, per translation, against the root note:

| Check | Why it matters |
|---|---|
| segment references identical, in order | the alignment is identity by block id; one missing or renamed id breaks every later pair |
| line count per segment identical | the display is line-parallel; a 5-line stanza rendered in 4 lines misaligns the reader's eye and the linter |
| segment types identical (`front_matter`, `verse`, `back_matter`) | derived from the ids, so a mismatch means an id scheme drift |
| headings identical (level, id) and the same TOC tree | the translation's TOC must nest exactly like the root's, whatever the titles say |
| no heading title inside content, no `#` in content | headings are TOC annotations, never text — the parser drops them, but a stray copy in the body would leak |
| no heading title starting with a numeral | the `1.` in the root's `## 1. བསྟོད་པ་དངོས།` is an editorial artefact; translations drop it |
| a transclusion above every block pointing at the same id | that is where the vault parser reads the alignment from |
| no `*[not yet translated]*` placeholder, `file_type: translation`, `root_text` names the root | upload preconditions |

With `--payloads`, for each note's `<stem>.edition.json` / `.toc.json` / `.alignment.json` under `4-SYSTEM/scripts/parser-root-text/output/`: references equal the note's, content equals the note's parse and carries no `#` and no heading title, spans are contiguous and cover the whole content, the TOC has one root section (the H1) whose subsections are contiguous, cover the content, and carry the note's heading titles in the note's language, and the alignment is identity over every segment.

With `--live`, the root note is compared with the library (GET only): the live root edition's segment references and TOC subsection count.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| Root note | `--root`, default `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` | no |
| Translation notes | positional; default: every `3-TRANSFORMATIONS/Translations/*/*/<root stem>-*.md` | no |
| `--payloads` | check the parser outputs too (run the `translation-upload` dry run first so they exist) | no |
| `--live` | needs `WEBUDDHIST_API_KEY` in the environment | no |

## Output

A report on stdout only. Nothing is written or modified.

## Procedure

```bash
python3 4-SYSTEM/scripts/check_translation_alignment.py                     # notes only
python3 4-SYSTEM/scripts/check_translation_alignment.py --payloads           # after the dry-run uploads
set -a; source ../Liturgy-rails/4-SYSTEM/scripts/.env.local; set +a
python3 4-SYSTEM/scripts/check_translation_alignment.py --payloads --live    # before executing an upload
```

Read every `!!` line back to the user with the ids it names. A failure is fixed at its source — the ledger and a re-render for a translation (`--force --only <id>` in the translating skill, or `--render-only`), the root note for a root problem — never by editing a payload.

## Rules

1. Report-only. The script writes nothing.
2. The root note is the reference; the live library is checked against the root note, not the other way round.
3. A translation that fails is not uploaded until it passes.

## Completion check

- [ ] Ran on every translation that is about to be uploaded, with `--payloads`
- [ ] `RESULT: OK` or every `!!` line reported with its ids and fixed at the source
- [ ] `--live` run once before an execute
