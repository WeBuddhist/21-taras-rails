---
name: gemini-translate
description: Produce a zero-shot, block-ID-aligned machine-baseline translation of a Tibetan source text into a display language DharmaMitra does not serve (Hindi, Nepali, Mongolian, Vietnamese, …) by calling Google Gemini on small batches of adjacent blocks under a JSON line schema, enforcing one target line per Tibetan line, translating section headings separately, and writing the result to its own track under 3-TRANSFORMATIONS/Translations/machine-drafts/zero-shot/gemini-<tag>/ — the same track shape as the DharmaMitra skill, so verification and upload work unchanged.
---

# gemini-translate

The sibling of `dharmamitra-translate` for languages DharmaMitra's `cat-translate` endpoint does not serve well or at all. It reuses that skill's parser, context builder and renderer (`dm_translate.py` is imported, not copied), keeps the same per-text append-only ledger and the same track layout. Two things are different, and both are the point:

- **Transport.** Gemini is asked for a JSON object holding one array of lines per block, under a response schema. No marker protocol: the response is split by block *and by line* without guessing.
- **Line parity is enforced, not hoped for.** Every block's line count is checked against its source before it is recorded. A wrong count triggers a solo re-run with the required count stated (up to `--parity-attempts`, default 3). Anything still divergent is recorded with `line_parity: false` and listed in the run report.

The output is a **machine baseline**: `track_type: machine-baseline`, `rails_used: none`, `status: draft`, never cited by any other `3-TRANSFORMATIONS/` output, never promoted past draft by an LLM.

This is the 21-taras-rails fork of the Liturgy-rails skill (imported 2026-09-17). The corpus drivers of the Liturgy version (`gm_corpus.py`, `gm_launch.py`, `gm_titles.py`, `gm_names.py`) were **not** imported — this vault serves one text and has no title registry; they remain in `Liturgy-rails/.claude/skills/gemini-translate/scripts/` if a corpus is ever needed here. Everything the DharmaMitra skill says under **This vault's conventions** (track layout, `<source stem>-<tag>.md`, transclusion layout, `--headings`, preserved frontmatter, no stamping pass, warning in the `note:` key, upload via `translation-upload`) applies here unchanged.

---

## Source language and provenance — read this first

**The source is always the Tibetan in `1-SOURCES/Text/`.** `root_text`, `translation_of_text_id` and the segment alignment always point at the Tibetan text, and block `^N` of the output renders block `^N` of the Tibetan.

An existing machine translation may be threaded into the prompt as **reference** with `--reference-track <folder>` (e.g. the DharmaMitra English track). It is recorded on every ledger record (`reference_used`) and in the frontmatter (`reference_translation`), but it is context, not source. **Default is no reference** — a true zero-shot from the Tibetan. The six imported tracks were all produced without a reference.

## Inputs

| Input | Description | Required |
|---|---|---|
| **Source file** | A block-ID'd note under `1-SOURCES/Text/`. Blocks without ` ^<id>` are skipped; headings are handled by `--headings`. | yes |
| **Target language** | A language **label** (`hindi`, `nepali`, `mongolian`, `vietnamese`), not an ISO code. The tag comes from the label table or `--lang-tag`. | yes |
| **Model** | `--model`, default `gemini-3.1-pro-preview`. `--thinking low|medium|high` (default: the model's default). Temperature is left at the model default unless `--temperature` is given. | no |
| **Style instruction** | `<track>/style.md`, seeded per language on first run and read back **verbatim** thereafter as the system prompt, followed by the fixed output contract. Edit the file, never the script. | no |
| **Context header** | `<track>/context-header.md`, a work-neutral preamble; the per-text `Work:` line is derived from each source and appended at call time. | no |
| **Reference track** | `--reference-track`, see above. | no |
| **Glossary** | `<track>/glossary.tsv` (auto-loaded when present) or `--glossary`: `Tibetan term<TAB>rendering` lines; entries whose term occurs in the batch join that call's context as fixed terminology. The four imported tracks carry the name glossaries pinned in the Liturgy vault. | no |
| **Extra frontmatter** | `--extra-fm <file.json>`: keys to seed or override on render. | no |

## Output

```
3-TRANSFORMATIONS/Translations/machine-drafts/zero-shot/gemini-<tag>/
├── about.md                        # what this track is and is not (seeded)
├── style.md                        # system prompt, verbatim (seeded, editable)
├── context-header.md               # work-neutral preamble (seeded, editable)
├── glossary.tsv                    # optional fixed terminology, auto-loaded
├── <source stem>-<tag>.md          # rendered, block-ID aligned, transclusion above each block
└── work/
    └── <source stem>-<tag>.jsonl   # append-only ledger, one record per block / heading
```

Ledger records carry the DharmaMitra fields plus `model`, `model_version`, `thinking`, `temperature`, `line_parity`, `parity_attempts`, `reference_used` and token `usage`. The frontmatter adds `model`, `thinking`, `temperature`, `response_format`, `reference_translation`, `glossary` and `line_parity_failures`, and its `generator` is the model version that actually answered.

### Seeded style per language

| tag | Script and vocabulary the seed asks for | Mantras | Names |
|---|---|---|---|
| `hi` | Devanagari; Sanskrit-derived Hindi Buddhist vocabulary | Devanagari transliteration of the Sanskrit | Sanskrit names in Devanagari; Tibetan names transliterated |
| `ne` | Devanagari, standard Nepali (not Hindi); Nepal's Buddhist usage | Devanagari | as Hindi, plus forms current in Nepal (गुरु रिन्पोछे, लामा) |
| `mn` | Cyrillic, Khalkha; the Tibetan-derived Mongolian Buddhist lexicon | Cyrillic as recited (Ум мани бадмэ хум) | established Mongolian deity names (Дарь эх, Жанрайсиг, …) |
| `vi` | Vietnamese with diacritics; Sino-Vietnamese Buddhist vocabulary | romanized Sanskrit (Om Mani Padme Hum) | established Vietnamese forms (Quán Thế Âm, Văn Thù, Liên Hoa Sanh) |

---

## Rules

1. **Never write to `1-SOURCES/`.**
2. **Never write into a non-baseline track.** The script refuses a folder that holds a `file_type: translation` file without `track_type: machine-baseline`.
3. **Never guess a split.** A response whose ids or shape do not match the batch is discarded and the batch is re-run one block per call. A block whose line count is wrong is re-run alone. Parity failures are reported, never padded or trimmed by hand.
4. **Every source block ID appears exactly once in the output**, in source order, unaltered.
5. **Source is the Tibetan.** A reference track is context and is recorded as such.
6. **The ledger is append-only.** To change a rendering, edit `style.md` (or add a `glossary.tsv` line) and re-run the block with `--force --only <id>`; the newer record supersedes at render time.
7. **Rate limits are handled, quotas are not fought.** 429s back off; a per-day quota 429 aborts the run at once. The ledger makes any re-run a resume.
8. **Report a partial run as partial.**
9. **Wrathful and exorcistic texts are liturgy.** Safety thresholds are `BLOCK_NONE`; a `finishReason` other than `STOP` is a failed call, retried singly, and reported if it still fails.

---

## Procedure

Scripts live in `4-SYSTEM/Skills/gemini-translate/scripts/`. All commands run from the vault root with `GEMINI_API_KEY` in the environment (`source ~/.zshrc`).

### Step 1 — Confirm inputs, spend nothing

```bash
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --list
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --limit 3 --dry-run
```

`--dry-run` prints the exact request bodies so the style and the `Work:` line can be read before a call is made.

### Step 2 — Pilot, then run

```bash
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --limit 6
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label>
```

Read the pilot back block by block against the Tibetan: line parity, script, mantras transliterated, names consistent, register recitable, imperatives/optatives (`ཤོག`, `གྱུར་ཅིག`) rendered as aspirations. A **systematic** defect means editing `style.md`; a **recurring term-level** error means a line in `glossary.tsv`; then re-run the affected blocks with `--force --only <ids>`.

### Step 3 — Translate the section headings

```bash
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py --source "1-SOURCES/Text/<text>.md" --lang <label> --headings
```

All `##` headings go in one JSON call (each is a one-line block, so the parity check applies). A `HEADINGS:` clause narrows the track's `style.md` for the call; the records are `kind: heading` and the renderer puts them into the `##` lines. The H1 is never sent.

### Step 4 — Verify

```bash
python3 4-SYSTEM/Skills/gemini-translate/scripts/gm_verify.py --lang-tag <tag>
```

No API calls: every ledger's parity flags, every rendered file's counts and title, block ids against the Tibetan one for one, and a scan for Tibetan or CJK characters inside translation lines (transclusion lines are skipped). Exit 0 means the track is whole. Also confirm `headings_translated` equals the number of `##` headings.

### Step 5 — Upload (separate decision)

Never from here. The `translation-upload` skill lints, parses, checks the live root and asks for confirmation before sending. The backend must know the language first (`GET /v2/languages`; `hi`, `mn`, `ne`, `vi` are all registered as of 2026-09-17).

---

## Completion check

- [ ] Target language stated or confirmed; tag matches the backend's language code
- [ ] `--dry-run` request read once; `Work:` line names the text being translated
- [ ] Pilot read back block by block; `style.md` / `glossary.tsv` adjusted if needed
- [ ] Section headings translated with `--headings` and read back
- [ ] `gm_verify.py --lang-tag <tag>` exits 0; `about.md` carries the run history
- [ ] Every source block ID appears exactly once in the rendered file, in source order
- [ ] Frontmatter carries `track_type: machine-baseline`, `rails_used: none`, `status: draft`, and names the model version that answered
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or any other track was modified
