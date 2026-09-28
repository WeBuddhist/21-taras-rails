---
name: translation-upload
description: Lint, parse and upload one translation note (file_type: translation) of this vault's root text to the WeBuddhist library as an edition of its own text, aligned segment-for-segment to the live root edition and carrying its own table of contents. Dry-run by default; reuses an existing translation text_id; never runs --execute without explicit human confirmation in the conversation.
---

# translation-upload

The translation-side counterpart of the root-text upload chain this vault already carries (`4-SYSTEM/scripts/linter-root-text` → `parser-root-text` → upload). One script, `4-SYSTEM/scripts/upload_translation.py`, chains the vault linter and parser and then talks to the live v2 API at `https://library.webuddhist.com`:

```
1. POST /v2/texts                                   <- <stem>.text.json      only when the note has no text_id
2. POST /v2/texts/{text_id}/editions                <- <stem>.edition.json   -> edition_id
3. PUT  /v2/editions/{root_edition}/alignments/{edition_id}
                                                    <- <stem>.alignment.json (root is the SOURCE side)
4. POST /v2/editions/{edition_id}/table-of-contents <- <stem>.toc.json       -> toc_id
```

Why the shape matters: a translation is its own **text** on the backend (`translation_of` = the root's `text_id`, settable only at creation), with its own **edition** (content + segmentation whose `reference`s are the block ids), an **alignment** from the root edition's segments to its own (identity pairs, because block `^N` here renders block `^N` of the Tibetan), and a **table of contents** whose spans mirror the root's (the `##` headings are not content; they are annotation spans over the translated blocks). Deleting a segmentation on the backend deletes every alignment hanging off it — that is what happened on 2026-09-16, and why the six translations of the Twenty-One Praises were re-cut and re-uploaded under their surviving text ids rather than re-created.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| **Translation note** | A `file_type: translation` note under `3-TRANSFORMATIONS/Translations/<Generator>/<tag>/` (or `1-SOURCES/Translations/`) whose body is block-ID aligned to the root and whose `root_text:` resolves to the root note. | yes |
| **Root note ids** | The root note's frontmatter must carry `text_id` and `edition_id` (the root is uploaded first). | yes |
| **Credentials** | `WEBUDDHIST_API_KEY` (and optionally `WEBUDDHIST_APP`) in the environment. They live in `Liturgy-rails/4-SYSTEM/scripts/.env.local`; load with `set -a; source ../Liturgy-rails/4-SYSTEM/scripts/.env.local; set +a`. Never print or commit them. | for `--execute` and the live checks |

## What the note must look like

- Frontmatter per `4-SYSTEM/Templates/FILE_YAML_PROPERTIES.md` §2: `title` (target language), `language`, `lang_tag`, `file_type: translation`, `root_text`, `category_id`, `license`, `source` (URL), `edition_type`. Optional: `translator`, `alt_titles`, `bdrc_work_id`. Do **not** set `translation_of` by hand — the linter resolves it from the root's `text_id`.
- `text_id` present when the translation text already exists on the backend (it is then reused); `edition_id` / `toc_id` empty until this skill fills them.
- Body: `# <title> ^0`, then the root's `##` headings with their `^N-0` ids, then per block a transclusion `![[<root stem>#^<id>]]`, a blank line, and the translation ending in ` ^<id>`. No other block may lack an id (the linter rejects a bare callout).
- The machine-baseline tracks produced by `dharmamitra-translate` / `gemini-translate` render exactly this shape.

## Output

- `4-SYSTEM/scripts/linter-root-text/output/<stem>.lint.json`
- `4-SYSTEM/scripts/parser-root-text/output/<stem>/<stem>.{text,edition,toc,alignment}.json`
- On `--execute`: `edition_id`, `aligned_to_edition_id`, `toc_id` patched into the note's frontmatter after each successful call, and a receipt appended to `4-SYSTEM/scripts/upload_ledger.json` after every call (so an interrupted run resumes; a step whose id is already in the note is skipped).

---

## Rules

1. **Dry-run is the default and is always run first.** It lints, parses, and checks — read-only — that the edition's references equal the live root's segment references one for one, that the live translation text points at the root and has no edition, and that the alignment is identity. Any problem aborts before a plan is printed.
2. **Never pass `--execute` without explicit human confirmation in the conversation.** A dry-run summary is not consent. Say what will be sent (host, text id, number of segments, pairs, TOC sections) and wait for a clear yes.
3. **Never re-create a text that exists.** A note with `text_id` reuses it. If the live text already has an edition, stop and report — the human decides whether to point the note at it or delete the stale one.
4. **The root's live segmentation is the truth.** If the note's block ids differ from the live root's references, fix the note (or the root upload), never the payload.
5. **Ids go back into the note.** After `--execute`, the note carries `edition_id`, `aligned_to_edition_id` and `toc_id`; the ledger has the receipts. Report both.
6. **Upload one translation per invocation**, and after all of them run `--verify` per note and read the results back.

---

## Procedure

All commands from the vault root.

### Step 0 — Structural check

```bash
python3 4-SYSTEM/scripts/check_translation_alignment.py
```

The `translation-alignment-check` skill must print `RESULT: OK` before anything below is run; after Step 1 run it again with `--payloads --live`.

### Step 1 — Dry run

```bash
set -a; source ../Liturgy-rails/4-SYSTEM/scripts/.env.local; set +a
python3 4-SYSTEM/scripts/upload_translation.py "3-TRANSFORMATIONS/Translations/<Generator>/<tag>/<stem>-<tag>.md"
```

Read the linter's `WARN` lines (an unresolved `translator` with no `[op:ID]` is expected for machine output and is skipped, not an error), the parser's counts (segments, headings, alignments), the `== checks ==` block (live root references identical, live text has no edition) and the plan. The linter patches `language`/`lang_tag` in the note if they disagree with the API's names; that is normal.

### Step 2 — Confirm with the human

State: host, `text_id` reused or created, edition size, pair count, TOC subsections, and that the note's frontmatter will be patched. Wait for a clear yes.

### Step 3 — Execute

```bash
python3 4-SYSTEM/scripts/upload_translation.py "<note>" --execute --skip-lint
```

Stops on the first error; the ids assigned so far are already in the note and the ledger — re-run the same command to resume.

### Step 4 — Verify

```bash
python3 4-SYSTEM/scripts/upload_translation.py "<note>" --verify
```

GETs the text, the edition's segments, the root→translation alignment and the TOC, and prints them. Compare against the note: same segment count, same reference order, one root TOC section with the `##` subsections in the target language.

### Step 5 — Report and record

Report per translation: text id, edition id, toc id, segments, pairs, TOC subsections. Commit the patched notes and the ledger.

---

## Completion check

- [ ] Dry run read back: lint OK, parse counts right, live checks ✓, plan as expected
- [ ] Human confirmed `--execute` in this conversation, naming the host
- [ ] `--execute` ran to `done.`; ids patched into the note; receipts in `upload_ledger.json`
- [ ] `--verify` read back and matches the note
- [ ] Nothing under `1-SOURCES/` changed except the linter's `language`/`lang_tag` normalisation on the note itself (which lives under `3-TRANSFORMATIONS/`)
