---
name: tree-guided-claims
description: Extract every distinct claim/fact a single commentary makes into ONE consolidated claims file, doing the extraction itself node by node against the commentary's own decimal-numbered TOC tree (from toc-tree-extraction) — a fresh, independent extraction per node, never a re-bucketing of an existing category-scaffolded claims file. Output at 2-RAILS/Claims/raw/tree-guided/<registered-id>.md, with a namespaced claim-ID scheme, a recomputed claim count, and a stated-referent rule that resolves within the claim's own quoted text.
---

# tree-guided-claims

This is **method 3** in the vault's claims-extraction comparison: use the commentary's own
ས་བཅད (sa bcad) tree as the *scaffold for extraction itself* — read one tree node's own
source window, in isolation, and extract fresh claims from it — rather than extracting once
over the whole file (as `commentary-claims` and the `opus`/`sonnet` runs do) and only
afterward filing the result under the tree's headings.

## Why this skill exists, and what it is not

`toc-scaffolded-claims` was meant to be exactly this — a third, independent extraction
method — but the run that produced `3-TRANSFORMATIONS/Wikipedia/tara21/claims/toc-scaffolded/`
was not one: `_comparison-report.md`'s headline finding is that those files are the
`sonnet` category-scaffolded run's claims, re-bucketed under the tree with a Grounding index
and Referent tags added on top — 114 of 118 Tibetan strings in one file byte-identical to
sonnet's, sonnet's `claim_count` copied verbatim rather than recomputed, sonnet's
transcription errors inherited unchanged. Re-bucketing is a real and useful operation, but
it is not a second extraction, and the report is explicit that presenting it as one hid real
defects (a cross-document contamination, a fabricated mantra promoted to canonical status)
that a genuine independent extraction would very likely not have reproduced.

**This skill is what the report asked for instead:** re-run the tree-scaffolding as a true
extraction, with each node's claims drawn fresh from that node's own text — never copied,
paraphrased-from, or checked against `opus`, `sonnet`, or `toc-scaffolded`'s existing files.
The orchestrating agent must not open those files while running this skill, and per-node
subagents (see Procedure) are never given their paths at all — the same structural isolation
`toc-tree-extraction` uses to keep its four passes from contaminating one another applies
here to keep this extraction independent of the earlier ones.

The five guards the comparison report specifies for a trustworthy tree-scaffolded run are
load-bearing rules of this skill, not optional cleanup:

1. **Claim IDs are never node IDs.** A claim's ID and a node's decimal must be visibly
   different strings (Rule 3 below) — the `toc-scaffolded` files had `1.1` denoting both a
   claim and a section, five such collisions on one file alone.
2. **`claim_count` is computed by counting, at the end, never inherited or estimated**
   (Rule 9, Procedure Step 8b).
3. **A node-boundary check backs every claim's placement** — each node is read from its own
   line window alone (Procedure Step 5), never the whole file, so a claim cannot be extracted
   under the wrong node by construction rather than by discipline.
4. **`stated` means the referent's verbatim name occurs in *this claim's own* quoted
   Tibetan** — not merely somewhere in the node's segment (Rule 8).
5. **Every claim is independently re-derived**, never re-bucketed (this section, Rule 1).

`4-SYSTEM/Skills/tree-guided-claims/scripts/verify_claims.py` is the deterministic backstop
for guards 1, 2 and 4 (and a partial check on 3) — run it before considering any output file
final; see its own docstring for exactly what it checks.

---

## Inputs

| Input | Description | Path / format |
|---|---|---|
| **Commentary file** | Exactly one file from `1-SOURCES/Commentaries/`. Must carry frontmatter with `registered_id`, `title`, `author`, `lang_tag`. | `1-SOURCES/Commentaries/<filename>.md` |
| **`registered_id`** | The short ID from that file's frontmatter. Names the output file. | e.g. `karma-maitri` |
| **TOC tree** | The decimal-numbered ས་བཅད tree for this same commentary, built by `toc-tree-extraction`, **QC'd clean (or human-reviewed past its flags) by both `qc_check_tree.py` and `qc_tree_vs_source.py`** — see that skill's Pass 4. A tree that has not been checked against the source itself is not a scaffold, it is a guess. | `2-RAILS/Sections/Raw/toc-tree/<id>.md` (promoted, preferred), or its pre-promotion `0-INBOX/toc-tree-<id>.md` working copy |
| **Segment addressing** | How the commentary's blocks are addressed. Determined by inspection, same as `commentary-claims` Step 2 — this vault's post-migration commentaries carry `^I-n` block IDs throughout. | block ID (preferred when present), else line number |

If the commentary file has no `registered_id`, **stop** and run `commentary-frontmatter`
first. If no TOC tree exists for this `registered_id`, or the tree exists but has not been
run through `qc_tree_vs_source.py` against this exact file version, **stop** and run
`toc-tree-extraction`'s Pass 4 first — do not invent a structure and do not scaffold against
an unchecked tree.

If the human contributor supplies more than one commentary, run this skill once per
commentary. Never merge two commentaries into one file.

## Output

One file per commentary at:

```
2-RAILS/Claims/raw/tree-guided/<registered-id>.md
```

`<registered-id>` is taken verbatim from the commentary's frontmatter. Create
`2-RAILS/Claims/raw/tree-guided/` if it does not exist. This sits alongside `2-RAILS/Claims/<id>.md`
(`commentary-claims`, fixed categories) and `2-RAILS/Claims/raw/toc-scaffolded/<id>.md`
(`toc-scaffolded-claims`, re-bucketed under the tree) — three methods, three subfolders, never
overwriting one another. See `2-RAILS/About Rails.md` §6b.

**This moved here from `3-TRANSFORMATIONS/Wikipedia/<corpus>/claims/tree-guided/` on
2026-08-04.** Claims are descriptive rails — every claim cites `1-SOURCES/` only, same as any
other `2-RAILS/` file — not pipeline-owned experimental output; they belong in the rails any
transformation can draw on, not filed under one specific downstream pipeline. If the kwiki
Wikipedia pipeline's own claims stage (4b) later needs this file, it reads it from here like any
other rail. See `4-SYSTEM/Guidelines/vault-annex.md` §6 for the fuller history of this move.

---

## Output file format

```markdown
---
registered_id: <registered-id>
title: "<Tibetan title verbatim from the commentary frontmatter>"
title_in_english: "<English title verbatim from the commentary frontmatter>"
author: "<Tibetan author verbatim>"
author_in_english: "<English author verbatim>"
source_file: 1-SOURCES/Commentaries/<filename>.md
toc_tree_source: <path to the toc-tree file actually used>
tree_qc_reports: [<path to qc_check_tree.py's report>, <path to qc_tree_vs_source.py's report>]
language: bo
citation_form: block-id | segment | line
method: tree-guided-extraction
claim_id_scheme: "c-<decimal-with-dashes>-<n>, e.g. node 1.2.3's third claim is c-1-2-3-3 — never a bare decimal, never collides with a node heading number"
claim_count: <integer, computed by counting ### claim headings below — never copied from another file>
status: draft
---

# Tree-guided claims — <title_in_english>

**Commentary:** `<registered-id>` · <author_in_english>
**Source:** [`<filename>.md`](../../../1-SOURCES/Commentaries/<filename>.md)
**TOC tree:** [`toc-tree-<registered-id>.md`](<relative path to toc_tree_source>)
**Citation form:** <one sentence stating how the citations in this file resolve to the
source — block ID, segment number, or line number.>

> Every claim below was extracted fresh from this node's own text, in isolation, by a
> subagent that saw only this node's source window and never any other commentary's claims
> file. No claim is copied, paraphrased, or re-bucketed from `opus`, `sonnet`, or
> `toc-scaffolded`. Headings and their decimal numbers are drawn from the commentary's own
> TOC tree, not invented here. Claim IDs (`c-...`) are never node decimals.

---

## Grounding index

<Same structure and rules as `toc-scaffolded-claims`'s Grounding index: Figures/forms,
Persons, Places, Texts/mantras, Events/dates — one entry per distinct referent actually
named in the commentary body, its TOC-tree node titles, or its frontmatter. Keep every
kind-group heading even when empty ("None attested."). Populated cumulatively as each
node's subagent reports what it found in its own window (Procedure Step 6); the
orchestrating agent merges the reports, deduplicating only when the source itself equates
two mentions (same name, or an explicit "that is, …" identification) — never on the
orchestrator's own judgment that two named things are traditionally the same.>

### Figures and forms (deities, aspects, emanations)
| ID | Name (verbatim) | What the source says it is | Attested at |
|---|---|---|---|
| FIG-1 | … | | |

### Persons (authors, teachers, lineage figures, requesters)
| ID | Name (verbatim) | Role stated in the source | Attested at |
|---|---|---|---|
| PER-1 | … | | |

### Places
| ID | Name (verbatim) | Context | Attested at |
|---|---|---|---|
| PLC-1 | … | | |

### Texts and mantras cited
| ID | Name / incipit (verbatim) | How the source uses it | Attested at |
|---|---|---|---|
| TXT-1 | … | | |

### Events and dates
| ID | Event / date (verbatim) | Context | Attested at |
|---|---|---|---|
| EVT-1 | … | | |

---

## 0. Front matter

<Anything before the tree's first node's window — opening formula, homage, colophon
preamble — extracted as its own claims, same rules as every other node. Omit this heading
only if the tree's first node genuinely opens the document.>

### c-0-1 <short label>
**བོད་ཡིག:** <the claim, commentator's own wording, quoted from THIS node's window only>
**English:** <one-line gloss>
**Type:** structural | word-gloss | etymology | iconography | identification | doctrinal | activity | practice | ritual | mantra | benefit | attribution
**Referent:** <Grounding-index ID(s) with basis — `(stated)` only if the name is inside
*this claim's own* `**བོད་ཡིག:**` string, `(node)` from the enclosing node's title,
`(section-opener)` from the node's own opening sentence — or exactly `[unanchored]`.>
**Cite:** (1-SOURCES/Commentaries/<filename>.md#^<block-id>)

---

## 1. <node title, exactly as the tree gives it> [[<pointer, if the tree has one>]]

<Claims from this node's own window before its first child's window begins.>

### c-1-1 <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** <…>
**Referent:** <…>
**Cite:** (1-SOURCES/Commentaries/<filename>.md#^<block-id>)

---

### 1.1 <child node title> [[<pointer>]]

#### c-1-1-1 <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** <…>
**Referent:** <…>
**Cite:** (1-SOURCES/Commentaries/<filename>.md#^<block-id>)

⚑ **c-1-1-2 <short label — internal tension>**
- **Position 1:** <Tibetan> — (…md#^<block-id>)
- **Position 2:** <Tibetan> — (…md#^<block-id>)
**English:** <one line stating what the tension is>

---

<... one heading per TOC-tree node, in the tree's own document order, depth mirrored by
heading level (## depth 1, ### depth 2, #### depth 3+, capped at #### — flatten anything
deeper into a nested list under the #### heading) ...>

## Z. Back matter

<Anything after the tree's last node's window — closing benefits, colophon, dedication.
Omit if the tree's last node genuinely closes the document.>

---

## Internal tensions (rollup)

<One line per ⚑ claim above. If none, write "None observed." and keep the heading.>

- ⚑ c-1-1-2 — <one-line English gloss> (see node 1.1)

---

## Unanchored claims (rollup)

<One line per claim marked `[unanchored]`, with the reason. If every claim is anchored,
write "None — all claims anchored." and keep the heading.>

- c-1-2-4 — <reason>

---

## Coverage log

| Node | Source window | Claims extracted | Notes |
|---|---|---|---|
| 0 (front matter) | ^I-1–^I-<n> | c-0-1, … | |
| 1 | ^I-<n>–^1-<n> | c-1-1 | |
| 1.1 | ^1-<n>–^1-<n> | c-1-1-1, c-1-1-2 | |
| … | | | |
| Z (back matter) | | | |

**Nodes with no independently attested line (`[[?]]` in the tree):** <list them and which
neighbouring node's window you folded their extraction into — do not skip a node's claims
just because its own pointer is unresolved.>
**Segments yielding no claim:** <list ranges that are pure root-text quotation, colophon,
or scribal matter, so a reviewer can see nothing was skipped silently.>
```

---

## Rules

1. **Fresh extraction, node by node — never re-bucketing.** Each node's claims are derived
   by reading that node's own source window and asking "what does the commentator assert
   here", exactly as `commentary-claims` asks it of the whole file. Never open an existing
   `opus`/`sonnet`/`toc-scaffolded` claims file for this commentary while running this
   skill, and never give a per-node subagent their paths (Procedure Step 4). If a claim in
   this file happens to match one in an existing file, that is either a real, independently
   re-found claim or evidence this rule was violated — not something to reconcile by hand.
2. **The TOC tree is the scaffold, never re-derived.** Use node titles, decimal numbers,
   and document order exactly as the tree gives them. A wrong tree is a
   `toc-tree-extraction`/QC problem, not something to silently fix here — stop and say so.
3. **Claim IDs are `c-<decimal-with-dashes>-<n>`, never a bare decimal.** Node `1.2.3`'s
   third claim is `c-1-2-3-3`. This string can never be mistaken for a node heading
   (`## 1.2.3 …`) even out of context — the load-bearing property the `toc-scaffolded`
   files lacked (guard 1).
4. **One commentary per file, read window by window in isolation.** Do not consult the
   root text, another commentary, or a different node's already-written claims to decide
   what a passage means.
5. **Every claim carries a citation**, in the commentary's own block-ID or line form —
   `commentary-claims` Rule 4, unchanged. A claim with no citation is not a claim.
6. **The commentator's own vocabulary, verbatim** — `commentary-claims` Rule 3, unchanged.
7. **Exhaustive, not selective; splitting preferred to merging** — `commentary-claims`
   Rule 6, unchanged, applied within each node's window.
8. **`stated` means the name is in the claim's own quotation.** A `Referent:` tag of
   `(stated)` is valid only when the referent's verbatim name or epithet occurs inside that
   claim's own `**བོད་ཡིག:**` string — not merely somewhere in the node's window. If the
   name is absent from the claim's own quotation but present in the window or inherited
   from the node's title, use `(section-opener)` or `(node)` instead; if none apply, write
   `[unanchored]` (guard 4). This is the fix the comparison report names explicitly: on the
   original `toc-scaffolded` run, 7 of 14 claims tagged `FIG-1 (stated)` in one file
   contained no form of the referent's name at all.
9. **`claim_count` is counted, not carried.** After writing every claim, count the actual
   `###`-level claim headings (excluding ⚑ tension entries, which are their own count) and
   put that integer in the frontmatter. Never copy a count from another file, another
   node's running total, or an estimate (guard 2).
10. **A claim belongs to the node whose window contains its citation.** If a passage seems
    to discuss a neighbouring node's topic (a title-keyword coincidence — a node titled
    "overcoming what is discordant" pulling in a claim from a different section that
    happens to share a word with that title), the deciding fact is which node's window the
    *cited block* is actually inside, never which node's title the content sounds closer
    to. This is the guard against the exact failure the comparison report documents on
    `lobsang-dawa`'s tree (guard 3).
11. **No parametric knowledge, no cross-commentary content.** Never add a fact this
    commentary does not itself state, and never let a claim's content or citation
    originate in a different commentary file — the comparison report's karma-maitri
    finding (a claim whose Tibetan string and citation both belong to lobsang-dawa's file,
    not karma-maitri's) is exactly the failure this rule exists to prevent structurally:
    a per-node subagent is given only ITS OWN commentary's file, never another's.
12. **Grounding is source-attested only** — same three permitted sources as
    `toc-scaffolded-claims` Rule 13: the commentary body, the TOC tree's node titles, the
    commentary's own frontmatter. Never enrich from tradition or general knowledge.
13. **Distinct referents get distinct entries**, even when tradition equates them —
    `toc-scaffolded-claims` Rule 16, unchanged.
14. **Never mark `status: complete`.** This skill writes `status: draft`. Only a domain
    specialist promotes a claims file.
15. **Do not modify `1-SOURCES/` or the TOC tree file.** Read-only on both.
16. **Empty nodes are kept, not deleted.** Write "None — announcement only." under a node
    heading with no claims of its own rather than omitting the heading.
17. **Run `verify_claims.py` before considering the file final** (Procedure Step 9). A
    file that has not been run through it is a draft of a draft.

---

## Procedure

**This is an orchestrator skill, structured like `toc-tree-extraction`: you (the
orchestrating agent) do the bookkeeping — loading, windowing, merging, running the
verifier — and dispatch one ISOLATED subagent per node for the actual extraction. Do not
extract claims yourself in this context; a subagent that only ever sees one node's own
window is what makes guards 1, 3 and "fresh extraction, never re-bucketing" structural
rather than a matter of discipline.**

### Step 1 — Load the commentary and the tree

a. Read the commentary's frontmatter; record `registered_id`, `title`, `title_in_english`,
   `author`, `author_in_english`. Stop if `registered_id` is absent.
b. Load the TOC tree (`2-RAILS/Sections/Raw/toc-tree/<id>.md`, or its pre-promotion `0-INBOX/toc-tree-<id>.md` working copy). Record
   `toc_tree_source`.
c. Confirm both QC reports exist and are recent (`qc_check_tree.py`'s and
   `qc_tree_vs_source.py`'s, the latter checked against this *exact* file). If either is
   missing, stop and run `toc-tree-extraction` Pass 4 first. Record both report paths.
d. Parse every tree line into an ordered list: decimal, depth, title, pointer (`[[N]]`,
   `[[?]]`, or none).

### Step 2 — Determine the citation form

Same inspection as `commentary-claims` Step 2. This vault's post-migration commentaries
carry `^I-n` / `^<chapter>-<n>` block IDs on every content block — prefer `citation_form:
block-id` and cite `#^<block-id>` directly; fall back to `segment`/`line` only for a
commentary that has not been through the block-ID stamping stage.

### Step 3 — Compute each node's reading window

Identical definition to `toc-scaffolded-claims` Step 4: a node's window starts at its own
pointer and ends the line before the next node's pointer (any depth), or end-of-file for
the last node. A node whose pointer is `[[?]]` gets no window of its own — fold its
heading into the nearest neighbour with a real pointer and note the fold in the Coverage
log, exactly as `toc-scaffolded-claims` Step 4c prescribes. Anything before the first
node's window is `Front matter`; anything after the last is `Back matter`.

### Step 4 — Dispatch one ISOLATED subagent per node

For each node (front matter and back matter count as nodes here), dispatch a separate
subagent. Give it **only**:

- this skill's Rules 1, 3, 5–13 (not the whole file — the extraction rules, not the
  orchestration mechanics)
- the commentary's file path and the node's own line range (start–end, inclusive; tell it
  to read via `sed -n 'START,ENDp' <file>` or the Read tool with offset/limit — never the
  whole file)
- the node's decimal and title, so it can form claim IDs and know what to write under
- **nothing else.** Do not give it the paths of `opus`/`sonnet`/`toc-scaffolded`/any other
  node's output. Do not let it see the merged claims file being built.

Ask it to reply with: the claims it extracted (Tibetan quotation, English gloss, `Type:`,
`Referent:` with basis, citation) in this node's window only, plus any Grounding-index
candidates it noticed (referent name, kind, what the source says, its own citation).
Independent nodes have no dependencies — dispatch several in parallel, one message,
multiple subagent calls.

### Step 5 — Assemble, don't re-derive

Merge each subagent's reply into the output file at the node's position in tree order.
This is mechanical assembly (like `toc-tree-extraction`'s merge step) — do not re-read the
source yourself and second-guess a subagent's extraction; if a reply looks wrong, dispatch
a fresh subagent for that node rather than editing its claims in this context.

### Step 6 — Build the Grounding index

Collect every subagent's referent candidates into the five kind-groups. Deduplicate only
when the source itself equates two mentions (Rule 12/13). Assign stable IDs (`FIG-1`,
`PER-1`, …) in first-appearance order.

### Step 7 — Number the claims and write headings

a. Claim IDs per Rule 3, sequential within each node (`c-1-2-1`, `c-1-2-2`, …). Numbers
   are stable — never renumber existing entries when appending.
b. Heading depth mirrors tree depth (`##`/`###`/`####`, capped, deeper levels flattened
   into a nested list), reproducing the node's decimal and title exactly, with its
   pointer (or the line it was folded to) in `[[...]]`.

### Step 8 — Finalise

a. Write the Internal tensions and Unanchored claims rollups from what each node's
   subagent flagged.
b. **Count the actual `###`-level claim headings and set `claim_count` to that number** —
   never inherit it (Rule 9).
c. Build the Coverage log: one row per node (plus Front/Back matter), its window, the
   claim IDs drawn from it, and any fold note from Step 3.
d. Set `status: draft`.
e. Write to `2-RAILS/Claims/raw/tree-guided/<registered-id>.md`.

### Step 9 — Run the deterministic verifier

```bash
python 4-SYSTEM/Skills/tree-guided-claims/scripts/verify_claims.py \
  2-RAILS/Claims/raw/tree-guided/<registered-id>.md \
  --source 1-SOURCES/Commentaries/<filename>.md
```

It checks: every quoted Tibetan string is literally present (NFC + tsheg/shad-stripped) in
its cited block; `claim_count` matches the file's actual claim headings; no claim ID
collides with a node decimal or another claim ID; every `stated` tag's referent name
actually occurs in that claim's own quotation; the coverage log's claimed "no claim"
ranges are genuinely uncited elsewhere. Fix every issue it reports (dispatch a fresh
per-node subagent for the offending node rather than hand-editing) and re-run until clean,
or note remaining issues for human review — never suppress a finding to make the count
read zero.

### Step 10 — Self-verification

- [ ] Every node subagent saw only its own window and this commentary's own file
- [ ] Every claim heading has a `**Cite:**` and a `**Referent:**` (valid ID(s) with basis,
      or `[unanchored]`)
- [ ] No claim ID collides with any node decimal or any other claim ID
- [ ] `claim_count` equals a fresh count of the `###` headings present
- [ ] `verify_claims.py` has been run and its output reviewed (clean, or issues logged)
- [ ] `1-SOURCES/` and the TOC tree file unmodified

---

## Completion check

- [ ] Commentary and TOC tree loaded; both QC reports confirmed against this exact file
- [ ] Extraction ran node by node via isolated subagents, never re-bucketed from another
      claims file
- [ ] Output written to `2-RAILS/Claims/raw/tree-guided/<registered-id>.md`
- [ ] Frontmatter complete: `registered_id`, `title`, `author`, `source_file`,
      `toc_tree_source`, `tree_qc_reports`, `citation_form`, `method: tree-guided-extraction`,
      `claim_id_scheme`, `claim_count`, `status: draft`
- [ ] Every TOC-tree node has a heading in tree order, none skipped or renumbered
- [ ] Every claim ID matches `c-<decimal-with-dashes>-<n>` and collides with nothing
- [ ] Every claim has Tibetan, English gloss, `Type:`, `Referent:` (with basis, or
      `[unanchored]`), and a citation
- [ ] Grounding index present, all five kind-groups, every entry source-attested
- [ ] `verify_claims.py` run; issues fixed or explicitly logged for human review
- [ ] `claim_count` equals the actual number of claim headings
- [ ] `1-SOURCES/` and the TOC tree file unmodified
