---
name: toc-tree-ingest
description: >
  Ingest a pre-extracted TOC tree (toc-tree-*.md) into a commentary file
  in 1-SOURCES/Commentaries/ IN PLACE by inserting markdown headings with
  block IDs. All nodes are placed in a single pass using the tree's own
  [[N]] line-number pointers — no text search.

  Trigger this skill when the user says things like:
  "ingest the TOC tree", "insert headings from the toc-tree file",
  "add section headings to the commentary", "ingest toc tree".
---

# toc-tree-ingest

Inserts section headings derived from a pre-extracted TOC tree into a Tibetan
commentary file, **in place** — the canonical file in `1-SOURCES/Commentaries/`
is updated directly; no side-copy is left as the working artifact. (An earlier
version of this skill wrote to a `commentaries_with_toc/<id>.toc.md` copy; that
convention is retired — the vault's rule is one file, updated in place through
each ingest step, not forked variants. A timestamped backup is still taken
first, purely as an undo path, not as a second canonical file.) All nodes
across all depths are processed in a **single pass**.

---

## Anchor strategy — line-number pointers, not text search

Each TOC node carries a `[[N]]` (1-based source line number) or `[[?]]`
(unresolved) pointer — written by `toc-tree-extraction`'s Pass 3 and validated
by that skill's `qc_tree_vs_source.py` against the exact source file version
the pointers were computed against. This skill inserts each node's heading
directly before its pointed-to line; there is no text matching and no
disambiguation to perform, because the pointer already is the resolved
position.

**Nodes are processed in reverse document order** (highest line number
first), so each insertion never shifts the line numbers of not-yet-processed
nodes. Nodes whose pointer is `[[?]]` are flagged as **not-found** and must be
inserted manually (see Step 3).

**Retired 2026-08-04:** an earlier version of this skill searched for a
`[[context text]]` snippet instead, with document-order cursor
disambiguation for repeated phrases. That anchor scheme never actually
matched what `qc_tree_vs_source.py` validates (a `\d+|\?`-only pointer) — a
tree that QC'd clean under that checker could not be consumed correctly by
the old text-search logic. Line-number pointers are the one format both
tools agree on; do not reintroduce text-snippet anchors here.

---

## Architecture

```
toc-tree-*.md  (from 2-RAILS/Sections/Raw/toc-tree/<id>.md, once promoted — see toc-tree-extraction)
      │
      ▼  Step 0 — backup (safety only, not a second canonical file)
  0-INBOX/temp/TOC-<id>/pre-toc-ingest-backup.md
      │
      ▼  Step 1 — parse (once per commentary)
  /tmp/toc-tree-*.json
      │
      ▼  Step 2 — ingest (single pass, all depths)
  scripts/toc_tree_ingest.py ingest
      │
      ▼
  1-SOURCES/Commentaries/<id>.md
  (headings inserted IN PLACE in the canonical file; prose untouched)
```

Two script modes:
- **`parse`** — run once; produces the JSON tree cache.
- **`ingest`** — single run; inserts all nodes in document order using cursor disambiguation.

---

## Inputs

| Field | Description |
|---|---|
| `toc_file` | Path to the finished tree — `2-RAILS/Sections/Raw/toc-tree/<id>.md` once `toc-tree-extraction` has promoted it (or its `0-INBOX/toc-tree-<id>.md` working copy, pre-promotion) |
| `commentary_file` | Path to the canonical commentary file to update **in place** — `1-SOURCES/Commentaries/<id>.md` |

The commentary file must already exist in `1-SOURCES/Commentaries/` (from `raw-to-sources`,
already through `commentary-resegment`). No side-copy is created — the same file named here
is both the input and the output.

---

## Output

The **canonical** commentary file at `1-SOURCES/Commentaries/<id>.md` is updated **in
place** — not a `.toc.md` variant. Section heading lines of the form:

```
{heading_hashes} {label} ^{block-id}
```

are inserted immediately before the anchor line for each node. No existing
prose is deleted, reordered, or retyped.

### Heading level by depth

| Depth | Markdown heading |
|---|---|
| 1 | `##` |
| 2 | `###` |
| 3 | `####` |
| 4 | `#####` |
| 5+ | `######` |

### Block ID formula

Decimal path segments joined with `-`, then `-0` appended.

| Decimal ID | Block ID |
|---|---|
| `1` | `^1-0` |
| `1.3` | `^1-3-0` |
| `1.3.2` | `^1-3-2-0` |
| `1.3.2.2.2.2.1.1.1` | `^1-3-2-2-2-2-1-1-1-0` |

No zero-padding. No segment cap — depth follows the tree exactly.

---

## Procedure

### Step 0 — Back up before writing into `1-SOURCES/`

This step edits the vault's canonical source file directly. Take an undo copy first —
this is a safety net, never treated as a second source of truth:

```bash
mkdir -p "0-INBOX/temp/TOC-BCAC14_GDR_bo"
cp "1-SOURCES/Commentaries/BCAC14_GDR_bo.md" \
   "0-INBOX/temp/TOC-BCAC14_GDR_bo/pre-toc-ingest-backup.md"
```

### Step 1 — Parse the TOC tree (run once per commentary)

```bash
python3 4-SYSTEM/Skills/toc-tree-ingest/scripts/toc_tree_ingest.py parse \
  --input "2-RAILS/Sections/Raw/toc-tree/BCAC14_GDR_bo.md" \
  --out "/tmp/toc-tree-BCAC14_GDR_bo.json"
```

Write the JSON to `/tmp/` to avoid NTFS ghost-file issues. Skip this step if
that JSON already exists and the toc-tree file has not changed. The script
reports how many nodes carry no pointer (`[[?]]`) — those will be not-found
at ingest.

### Step 2 — Ingest all nodes in one pass

```bash
python3 4-SYSTEM/Skills/toc-tree-ingest/scripts/toc_tree_ingest.py ingest \
  --tree "/tmp/toc-tree-BCAC14_GDR_bo.json" \
  --commentary "1-SOURCES/Commentaries/BCAC14_GDR_bo.md"
```

Inserts every node's heading directly before its `[[N]]` line, in reverse
document order (see Anchor strategy above). Prints a summary — inserted /
already-present / not-found counts — and exits non-zero if anything is
not-found.

### Step 3 — Resolve not-found nodes manually

Not-found nodes fall into two categories:

**`[[?]]` pointers** — `toc-tree-extraction` could not resolve this node to a
source line. Locate the section in the commentary by reading the surrounding
prose and understanding the structure, then insert the heading line manually
at the correct position.

**Out-of-range pointer** — a `[[N]]` where N exceeds the file's line count.
This means the tree was built against a different version of the file than
the one being ingested now (a resegmentation since, most likely) — go back
to `toc-tree-extraction` and rebuild the tree against the current file rather
than patching the pointer by hand.

**Manual insertion format:**
```
###### Label text ^block-id

```
(blank line after; inserted immediately before the section's opening prose)

After all manual insertions, re-run Step 2 — the already-present check will
skip the manually inserted headings and confirm zero not-found.

---

## Rules

1. **No pointer content in the output.** Only the label and block ID are
   written to the commentary file.
2. **No prose is altered.** Existing commentary lines are never deleted,
   reordered, or retyped.
3. **Block IDs follow the tree.** No segment cap. Use the full decimal path.
4. **Single pass, reverse document order.** All depths are ingested in one
   run; processing highest-line-number-first means an earlier insertion
   never invalidates a later (smaller-line-number) node's pointer.
5. **Idempotent.** The already-present check (looks for block_id in 1–3
   lines before the target) makes re-runs safe.
6. **Write to `/tmp/`** for JSON cache (avoids NTFS ghost-file issues).
7. **Trust the tree's pointers, don't re-derive them here.** If a pointer
   looks wrong, that is a `toc-tree-extraction` QC problem — fix it there
   (rebuild or re-run the checkers), not by hand-editing the JSON cache.

---

## Completion checklist

- [ ] Backup of the canonical commentary file taken to `0-INBOX/temp/TOC-<id>/pre-toc-ingest-backup.md`
- [ ] JSON cache produced at `/tmp/toc-tree-<id>.json`
- [ ] `ingest` run: summary shows 0 not-found (or all not-found resolved manually)
- [ ] `1-SOURCES/Commentaries/<id>.md` updated in place — no `.toc.md` side-copy left behind as a second canonical file
- [ ] Final file line count = source line count + (2 × headings inserted)
