Bring a new text into the vault: clean, frontmatter, segment, structure, and annotate it — entirely in `1-SOURCES/`, entirely with vault skills. Arguments: $ARGUMENTS

Expected form: `<path-to-raw-root-text> [path-to-raw-commentary ...]`

**As of 2026-08-04 this command no longer touches the Wikipedia pipeline (`4-SYSTEM/Pipelines/wikipedia/`).** No `kwiki` command runs here, and nothing is written under `3-TRANSFORMATIONS/Wikipedia/`. Ingest is now a pure `1-SOURCES/` + `2-RAILS/` operation: raw text goes in, an annotated source file and its TOC-tree rail come out. `sources.yaml`/`terms.yaml`-style registries are not used by this chain — the citation and provenance data they used to hold (BDRC IDs, school, copyright) now lives directly in each file's own frontmatter, filled where it's easy and left blank for manual review where it isn't (see `raw-to-sources/SKILL.md` Rule 4). The Wikipedia pipeline's remaining role is article generation only (`/pipeline`, stages 4–7) — it reads finished `1-SOURCES/`/`2-RAILS/` files as inputs, same as any other transformation would.

Read each `SKILL.md` **in full** before executing it — do not improvise the format. Block-ID and heading conventions are pinned in `4-SYSTEM/CLAUDE.md` §5 and `4-SYSTEM/Guidelines/vault-annex.md`.

## Root text — one file, shorter path

| Step | Skill | Notes |
|---|---|---|
| 1. Clean + frontmatter | `4-SYSTEM/Skills/raw-to-sources/SKILL.md` `--type root` | Orchestrates `clean-raw-text` + `root-text-frontmatter`; writes `1-SOURCES/Text/<title>.md`, still unsegmented |
| 2. Segment + block IDs | `4-SYSTEM/Skills/format-tibetan-root-text/SKILL.md` | One stanza per paragraph, one verse-line per line, `^chapter-verse` IDs, `^N-0` chapter anchors — segmentation and block IDs happen together for root texts |
| 3. TOC *(optional)* | `4-SYSTEM/Skills/add-toc/SKILL.md` | Skip for a short text with no real internal division; use when the root has its own multi-chapter structure |
| 4. Lint | `4-SYSTEM/Skills/lint-annotations/SKILL.md` | Report-only pre-flight: verse structure, block IDs, heading anchors |

The root text must finish this path **before** any commentary's transclusion step (below) — commentaries anchor to the root's block IDs.

## Each commentary — full chain, in order

| Step | Skill | Notes |
|---|---|---|
| 1. Clean + frontmatter | `4-SYSTEM/Skills/raw-to-sources/SKILL.md` `--type commentary` | Orchestrates `clean-raw-text` + `commentary-frontmatter` (which assigns `registered_id`); writes `1-SOURCES/Commentaries/<title>.md`, still unsegmented |
| 2. Resegment by meaning | `4-SYSTEM/Skills/commentary-resegment/SKILL.md` | LLM groups clause-lines into sense-unit paragraphs **by meaning**, not by citation size or particle rules; byte-identity verified |
| 3. Build the TOC tree | `4-SYSTEM/Skills/toc-tree-extraction/SKILL.md` | Four-pass isolated-subagent pipeline (candidates → verbatim enumerations → nested tree → QC + repair). **Block IDs cannot be stamped before this step** — a block ID's prefix *is* its TOC path, so the structure has to exist first. Promotes the finished, QC-clean tree to `2-RAILS/TOC-Trees/<id>.md` |
| 4. Ingest headings | `4-SYSTEM/Skills/toc-tree-ingest/SKILL.md` | Inserts the tree's headings **in place** into the same `1-SOURCES/Commentaries/<id>.md` file — no side-copy. Takes a backup first as an undo path only |
| 5. Transclude root verses | `4-SYSTEM/Skills/Transclusion-rootext-into-commentaries/SKILL.md` | Places `![[1-SOURCES/Text/<root>.md#^N-V]]` anchors — this **is** the root↔commentary alignment; there is no separate alignment artifact in this chain (see note below) |
| 6. Stamp block IDs | `4-SYSTEM/Skills/commentary-verse-id/SKILL.md` | Runs only now that headings (step 4) and transclusions (step 5) both exist — chapter prefix is derived from the nearest preceding transclusion, and the heading path is what makes the ID meaningful |
| 7. Lint | `4-SYSTEM/Skills/lint-annotations/SKILL.md` | Report-only pre-flight: verse structure, block IDs, heading anchors |

Claims extraction (`/extract-claims <registered-id>`) is a separate command, run after this chain completes — it needs the TOC tree and block IDs this chain produces, but is not part of `/ingest` itself.

## On alignment — no separate coverage artifact in this chain

The Wikipedia pipeline used to compute `kwiki align`'s own coverage JSON + percentage,
stored under `3-TRANSFORMATIONS/Wikipedia/<corpus>/work/aligned.json`. This chain does not
reproduce that: step 5's `![[root#^N-V]]` anchors already place the alignment data directly
in the rails, as part of the commentary file itself — queryable by grep or by Obsidian's own
backlinks panel. If a numeric coverage percentage per commentary is ever needed again, that's
a small standalone script reading the anchors already in place, not a pipeline dependency.

## Report honestly

After each commentary's step 7, read the lint report and say plainly whether it's clean or
what remains open. For a **prose** commentary, zero verses transcluded in step 5 is a bug
worth chasing; for a **word-commentary** (`བསྡུས་འགྲེལ`, `མཆན་འགྲེལ`) that dissolves the
stanza into glosses, it can be legitimate — say which case applies, don't call a real gap a
non-issue or a real non-issue a failure.
