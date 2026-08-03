Bring a new text into the pipeline: clean, segment, stamp block IDs, and align. Arguments: $ARGUMENTS

Expected form: `<corpus-id> <path-to-root-text> [path-to-commentary ...]`

This is stages 1–2. It uses the **vendored, production-proven skills** — prefer them over writing
new logic. In run order:

| Step | Skill | Notes |
|---|---|---|
| Clean OCR artifacts | `4-SYSTEM/Skills/clean-raw-text/SKILL.md` | Generates a targeted Python script per text; has worked examples for spyod-jug commentaries |
| Segment root + block IDs | `4-SYSTEM/Skills/format-tibetan-root-text/SKILL.md` | Root texts only. One stanza per paragraph, one verse-line per line, `^chapter-verse` IDs, `^N-0` chapter anchors |
| Segment commentaries | `4-SYSTEM/Skills/commentary-segmentation/SKILL.md` | Prose/word commentaries. Deterministic 3-stage scripts, no-loss gated. **Stages 0–1 only** — the rest is `kwiki commentaries`, below |
| Add TOC | `4-SYSTEM/Skills/add-toc/SKILL.md` | Optional, root texts. Prepends a nested `^toc-X-Y-Z` dkar-chag |
| Lint the annotations | `4-SYSTEM/Skills/lint-annotations/SKILL.md` | Report-only pre-flight: verse structure, block IDs, heading anchors |
| Align root↔commentary | `4-SYSTEM/Skills/Transclusion-rootext-into-commentaries/SKILL.md` | Driven by `kwiki commentaries`; read it to understand what the anchors mean |

Read each SKILL.md **in full** before executing it. They were ported from
`webuddhist-library-data-pipeline` and `bodhisattvacharyavatara-rails` where they are in production.
Block-ID and heading conventions are pinned in `4-SYSTEM/Pipelines/wikipedia/docs/reference/conventions.md`.

## Finishing the commentaries — do not stop at segmentation

`commentary-segmentation` leaves a file that is correctly broken into blocks and carries **nothing
else**: no headings, no block IDs, no anchors to the root. That is enough to align against badly and
not enough to cite at all — a footnote can name the commentary but not the passage. One command does
the rest:

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki commentaries <corpus-id>
```

Per file it runs: stage-2 refinement → sa-bcad headings (`tag-inline-toc` Phase 1 through Gemini,
Phase 2 through the vendored renderer) → root-verse transclusion anchors → a block ID on every
content block. Intermediates land in `work/ingest/commentaries/`, the summary in
`work/ingest/COMMENTARY_REPORT.md`, and the finished file is copied over `source/commentaries/`
(with a `.pre-toc` backup) only if every step held.

The invariant it enforces after each step: the file's **reading view** — its text with every layer
of scaffolding taken back off — must be byte-identical to what it was. A file that fails is left
alone and reported. Useful flags: `--only <substring>` for one file, `--skip-toc` for no model call,
`--no-promote` to review before overwriting `source/`.

**Read the report.** Three numbers matter per commentary: headings found, verses anchored, blocks
stamped. A word-commentary (`བསྡུས་འགྲེལ`, `མཆན་འགྲེལ`) legitimately anchors zero verses because it
dissolves the stanza into glosses — say so rather than calling it a failure. A *prose* commentary
anchoring zero is a bug worth chasing.

## If the corpus has no curated term list

`kwiki terms` seeds the ledger from `terms.yaml` (the team's sheet). For a corpus with no such
list, the proven route is translation-mediated: produce a block-ID-preserving English translation
(`4-SYSTEM/Skills/zeroshot-translator/SKILL.md`), extract ranked keywords from it and enrich them
with Tibetan equivalents (`4-SYSTEM/Skills/english-keyword-extraction/SKILL.md`), then put the
reviewed list in `terms.yaml`. A human approves the list before anything downstream runs.

## Layout to produce

```
4-SYSTEM/Pipelines/wikipedia/corpora/<corpus-id>/
  source/
    root.md                    segmented, ^chapter-verse IDs, NFC
    commentaries/<id>.md       sa-bcad headings, ^N-…-0 heading IDs, a block ID on every
                               content block, ![[root#^N-V]] anchors — see conventions.md §1a
  sources.yaml                 metadata + citation URLs (see below) — corpus root, not source/
  terms.yaml                   key-term registry (from the sheet, or seeded by the terms stage)
```

## sources.yaml is not optional

Every commentary needs an entry, because that is where citation URLs come from — the model is
never allowed to invent one. Use `4-SYSTEM/Pipelines/wikipedia/scripts/export_corpus_registry.py` if the corpus is one of the
17 tabs in the team's Google Sheet; otherwise write the entries by hand. Preference order for the
citation URL is Wikisource text → Wikisource index → BDRC → WeBuddhist → Commons.

Per the canonical pipeline's step 1 (`4-SYSTEM/Pipelines/wikipedia/docs/reference/cowork-pipeline.md`;
`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/01-ingest/`), each entry should also carry the metadata the
downstream stages read: `school` (feeds the claims stage's attribution rules), `author_dates`,
and `copyright` — a **router, not a gate**: `public-domain` texts are destined for Wikisource
with block-ID anchors; `copyrighted` ones get a stable BDRC/WeBuddhist link instead, and their
refs must carry the full locator. Derive `copyright` from the author's death date (70+ years →
public domain; uncertain → `copyrighted-assumed`, flagged for review). **Fetch, never recall:**

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python 4-SYSTEM/Pipelines/wikipedia/scripts/bdrc_fetch.py W22084
```

prints titles, author + life dates, and the derived copyright hint for any BDRC RID — use it to
fill the fields, and leave a `# TODO` on anything it could not resolve rather than guessing.

A source with no URL still works, but every citation from it will be flagged in the review report
as unlinked, which a reader cannot verify. Say so plainly when reporting.

## Finally

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki align <corpus-id>
```

**Read the coverage table and report it.** Low coverage on a commentary means either it does not
quote the root text (common for word-commentaries — expected) or the segmentation is wrong
(a real bug — investigate). Do not proceed to article generation while pretending an alignment
problem is not there.
