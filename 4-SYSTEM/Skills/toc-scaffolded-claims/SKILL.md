---
name: toc-scaffolded-claims
description: Extract every distinct claim/fact a single commentary makes into ONE consolidated claims file at 2-RAILS/Claims/toc-scaffolded/<registered-id>.md, organised by that commentary's own decimal-numbered TOC tree (from toc-tree-extraction) instead of fixed A–I categories, with every claim anchored to the attested persons, figures, places, texts, events, and dates it concerns — so claims for several commentaries on the same root text can be read side by side, section by section, and every claim can be traced back to a concrete, verifiable referent.
---

# toc-scaffolded-claims

This skill produces a **TOC-scaffolded, referent-anchored claims inventory**: the same exhaustive, cited, one-claim-at-a-time extraction that `commentary-claims` performs, but grouped under the commentary's own ས་བཅད (sa bcad) structure instead of the fixed nine-category scheme, and with each claim **anchored to the specific referent it is about** whenever the source attests one. Where `commentary-claims` answers "what does this commentary assert, by topic?", this skill answers "what does this commentary assert, **in the order and hierarchy it itself imposes on the text — and about whom, where, and when, exactly?**"

It exists for two reasons. First, a category-scaffolded claims file (A. Framing, B. Word-gloss, …) is excellent for auditing one commentary in isolation, but it scatters a single section's material across nine categories, making it slow to compare *the same stretch of root text* across several commentaries. A TOC-scaffolded file keeps every claim under the heading of the actual section it belongs to, so opening several commentaries' files side by side and scrolling to the matching node shows what each commentator says about that same stretch, in one place.

Second, a claim floating free of its referent is not verifiable. "She acts swiftly to help" is unfalsifiable until the file records *which* figure, in *which* form or aspect, the commentary itself says this about — and commentaries usually do say: the deity's specific epithet, the form being praised in that section, the named speaker, the place, the lineage figure, the text being quoted, the date in the colophon. The commentary's own TOC is often where this disambiguation lives (a section titled "praise via the wrathful form" tells you the referent of every claim under it). This skill therefore harvests every such **grounding element** — person, figure/form, place, text, event, date — from the commentary, its TOC tree, and its frontmatter, registers each one verbatim with a citation, and ties claims to them. A claim that cannot be tied to any attested referent is explicitly marked, because that untethered-ness is itself a finding about the commentary.

Correct output looks like this: a reader who has never opened the commentary can scan the file top to bottom and see, node by node, everything the commentator states about that node — in his own vocabulary, each claim individually cited **and each claim's subject pinned to a registry entry that resolves to a verbatim source string** — matching the shape of the commentary's own TOC tree. Nothing in the file comes from the root text, from another commentary, or from the model's own knowledge.

---

## Inputs

| Input | Description | Path / format |
|---|---|---|
| **Commentary file** | Exactly one file from `1-SOURCES/Commentaries/`. Must carry frontmatter with `registered_id`, `title`, `author`, `lang_tag`. | `1-SOURCES/Commentaries/<filename>.md` |
| **`registered_id`** | The short ID from that file's frontmatter. Names the output file. | e.g. `karma-maitri` |
| **TOC tree** | The decimal-numbered ས་བཅད tree for this same commentary, built by `toc-tree-extraction` (Claude-native) or the Gemini `extract_toc_tree.py`. This is the scaffold every heading in the output is drawn from. | `0-INBOX/toc-tree-<id>.md`, or `0-INBOX/temp/TOC-<id>/toc-tree-<id>.md` |
| **Segment addressing** | How the commentary's blocks are addressed. Determined by inspection, same as `commentary-claims` Step 2. | numbered segments, or line numbers |

If the commentary file has no `registered_id`, **stop** and run `commentary-frontmatter` first. If no TOC tree exists for this `registered_id` under either path above, **stop** and run `toc-tree-extraction` (or the Gemini script) on this commentary first — do not invent a structure or fall back to the A–I categories.

If the human contributor supplies more than one commentary, run this skill once per commentary. Never merge two commentaries into one file.

## Output

One file per commentary at:

```
2-RAILS/Claims/toc-scaffolded/<registered-id>.md
```

`<registered-id>` is taken verbatim from the commentary's frontmatter. Create `2-RAILS/Claims/toc-scaffolded/` if it does not exist. This sits alongside any existing per-model category-scaffolded runs (e.g. `2-RAILS/Claims/sonnet/<id>.md`, `2-RAILS/Claims/opus/<id>.md`) without touching them.

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
language: bo
citation_form: segment | line
scaffold: toc-tree
claim_count: <integer — total claims in this file>
status: draft
---

# TOC-scaffolded claims — <title_in_english>

**Commentary:** `<registered-id>` · <author_in_english>
**Source:** [`<filename>.md`](../../../1-SOURCES/Commentaries/<filename>.md)
**TOC tree:** [`toc-tree-<registered-id>.md`](<relative path to toc_tree_source>)
**Citation form:** <one sentence stating how the `§`/`L` numbers in this file resolve to the source.>

> Every claim below is drawn from this commentary alone. Headings and their
> decimal numbers are drawn from the commentary's own TOC tree, not invented
> here. Every Referent tag resolves to an entry in the Grounding index, and
> every Grounding-index entry resolves to a verbatim string in this source.
> No claim originates in the root text, in another commentary, or outside
> `1-SOURCES/`.

---

## Grounding index

<The registry of every named referent the commentary, its TOC tree, or its
frontmatter attests. One entry per distinct referent, grouped by kind. Each
entry has a stable ID used by the Referent: lines below. Include ONLY kinds
that actually occur; keep the group heading with "None attested." for kinds
that do not — the absence is a finding.>

### Figures and forms (deities, aspects, emanations)
| ID | Name (verbatim) | What the source says it is | Attested at |
|---|---|---|---|
| FIG-1 | <Tibetan/original name or epithet exactly as written> | <one line, from the source only> | §<n>, §<n> |
| FIG-2 | … | | |

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

<Anything before the TOC tree's first node — opening formula, homage to the
deity, verse announcing intent — captured here as usual claim entries. Omit
this heading only if the tree's first node genuinely opens the document.>

### 0.1 <short label>
**བོད་ཡིག:** <the claim, commentator's own wording>
**English:** <one-line gloss>
**Type:** structural | word-gloss | etymology | iconography | identification | doctrinal | activity | practice | ritual | mantra | benefit | attribution
**Referent:** <ID(s) from the Grounding index this claim is about, with the
basis in parentheses: "(stated)" when the referent is named in the claim's
own passage, "(node)" when it is inherited from the enclosing TOC-node's
title, "(section-opener)" when the section's opening sentence fixes it. If
no attested referent applies, write exactly `[unanchored]`.>
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## 1. <node title, exactly as it reads in the TOC tree> [[<line>]]

<Claims found in this node's own text before its first child node begins —
i.e. the section's announcement / opening statement, if it makes assertions
of its own beyond dividing into parts.>

### 1.1 <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** <…>
**Referent:** <…>
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

---

## 1.1 <child node title> [[<line>]]

### 1.1.1 <short label>
**བོད་ཡིག:** <…>
**English:** <…>
**Type:** <…>
**Referent:** FIG-2 (node) <e.g. — a claim inside a section the TOC itself
titles "praise via the wrathful form" is *about* that form; the node title
is the source's own disambiguation and the claim inherits it>
**Cite:** (1-SOURCES/Commentaries/<filename>.md §<n>)

⚑ **1.1.2 <short label — internal tension>**
- **Position 1:** <Tibetan> — (…md §<n>)
- **Position 2:** <Tibetan> — (…md §<n>)
**English:** <one line stating what the tension is>

---

<... one heading per TOC-tree node, in the tree's own document order,
depth mirrored by heading level (## for depth 1, ### for depth 2, #### for
depth 3+, capped at #### — flatten anything deeper into the same heading
with a nested list) ...>

## Z. Back matter

<Anything after the TOC tree's last node — closing benefits, colophon,
dedication — if the tree does not extend that far. Omit if the tree's last
node genuinely closes the document.>

---

## Internal tensions (rollup)

<One line per ⚑ claim above, for fast scanning: node number, claim id, and
the one-line English gloss. If none, write "None observed." and keep the
heading.>

- ⚑ 1.1.2 — <one-line English gloss> (see node 1.1)

---

## Unanchored claims (rollup)

<One line per claim marked `[unanchored]` above: claim id + why no referent
could be attested (subject never named, pronoun with no antecedent in the
source, generic statement the commentary itself leaves generic). This list
is the file's honesty ledger — a reviewer reads it to see which claims
cannot yet be rooted back to anything concrete. If every claim is anchored,
write "None — all claims anchored." and keep the heading.>

- 1.2.4.b — <reason> 

---

## Coverage log

| Node | Source range | Claims extracted | Notes |
|---|---|---|---|
| 0 (front matter) | §1–§<n> | 0.1, … | |
| 1 | §<n>–§<n> | 1.1 | |
| 1.1 | §<n>–§<n> | 1.1.1, 1.1.2 | |
| … | | | |
| Z (back matter) | §<n>–§<n> | | |

**Nodes with no independently attested line (`[[?]]` in the tree):** <list
them and state which neighbouring node's range you folded their text into.>
**Segments yielding no claim:** <list ranges that are pure root-text
quotation, colophon, or scribal matter, so a reviewer can see nothing was
skipped silently.>
```

---

## Rules

1. **The TOC tree is the scaffold, never re-derived.** Use the node titles, decimal numbers, and document order exactly as they appear in the tree file. Do not renumber, reorder, merge, or split nodes — if the tree is wrong, that is a `toc-tree-extraction` problem, not something to silently fix here.
2. **One commentary per file, read in isolation.** Same as `commentary-claims` Rule 1: do not open a second commentary, do not consult the root text to decide what a passage means.
3. **Every claim carries a citation**, exactly as in `commentary-claims` Rule 4. A claim with no `(1-SOURCES/Commentaries/<filename>.md §<n>)` reference is not a claim — delete it.
4. **The commentator's own vocabulary, verbatim** — `commentary-claims` Rule 3, unchanged.
5. **English is a gloss, not a translation** — one line, for orientation only, never cited from.
6. **Exhaustive, not selective**, and **splitting preferred to merging** — `commentary-claims` Rule 6, unchanged. Every distinct assertion under a node gets its own numbered entry.
7. **No parametric knowledge.** Never add a fact this commentary does not itself state.
8. **Keep the `Type:` tag on every claim**, using the same vocabulary as `commentary-claims` (structural, word-gloss, etymology, iconography, identification, doctrinal, activity, practice, ritual, mantra, benefit, attribution). This is what still lets a reader filter by facet even though the top-level grouping is now structural, not topical.
9. **Never mark `status: complete`.** This skill writes `status: draft`. Only a domain specialist promotes a claims file.
10. **Do not modify `1-SOURCES/` or the TOC tree file.** This skill reads both and writes only to `2-RAILS/Claims/toc-scaffolded/`.
11. **Empty nodes are kept, not deleted.** If a node's own text yields no claim beyond dividing into children, write "None — announcement only." under its heading and move on; do not omit the heading.
12. **Front matter and back matter are never silently dropped.** If the tree's first node does not open the document, or its last node does not close it, the leftover text still gets claims extracted under `## 0. Front matter` / `## Z. Back matter`.
13. **Grounding is source-attested only.** A Grounding-index entry may be created from exactly three places: the commentary body, the TOC tree's node titles, and the commentary's own frontmatter (author, date, title). Never add an entry — or enrich one — from the model's general knowledge of the tradition, however standard the identification seems. If the commentary says only "the protector," the registry entry is "the protector," not the deity the tradition means by it.
14. **Every claim carries a `Referent:` line.** The line either names Grounding-index ID(s) with the basis — `(stated)` from the claim's own passage, `(node)` inherited from the enclosing TOC-node title, `(section-opener)` from the sentence that opens the section — or reads exactly `[unanchored]`. Node-title inheritance is legitimate grounding *because the title is the commentator's own words*: a claim under a section the author titled "praise via the wrathful form" is about that form on the author's authority, not the extractor's.
15. **`[unanchored]` is a verdict, not a failure to try.** Use it only after checking the claim's passage, its section opener, and its full node-path ancestry. Never resolve an unanchored claim by guessing; never delete a claim because it is unanchored. Every `[unanchored]` claim appears in the Unanchored claims rollup with the reason.
16. **Distinct referents get distinct entries — even when tradition equates them.** If the commentary praises a peaceful form in one section and a wrathful form in another, those are two registry entries; whether they are "the same deity" is the commentary's call to make, recorded only if it makes it. Conflating referents the source keeps apart destroys exactly the verifiability this skill exists to add.
17. **Text-generic, always.** The registry kinds (figures/forms, persons, places, texts, events/dates) and the anchoring mechanism are fixed; nothing in this skill's execution may hard-code a particular deity, text, or tradition. The skill must run unchanged on any commentary with a TOC tree.

---

## Procedure

### Step 1 — Load the commentary

a. Read the full frontmatter of the target file in `1-SOURCES/Commentaries/`.
b. Record `registered_id`, `title`, `title_in_english`, `author`, `author_in_english`.
c. If `registered_id` is absent, stop and report; run `commentary-frontmatter` first.

### Step 2 — Load the TOC tree

a. Look for `0-INBOX/toc-tree-<registered-id>.md`; if absent, look for `0-INBOX/temp/TOC-<registered-id>/toc-tree-<registered-id>.md`.
b. If neither exists, stop and report: run `toc-tree-extraction` (or the Gemini `extract_toc_tree.py`) on this commentary first.
c. Record the path actually used as `toc_tree_source`.
d. Parse every tree line (`* <decimal> <title> [[<line>]]`) into an ordered list, in the exact document order the tree file lists them, keeping decimal, depth (number of decimal segments), title text, and the line number (or `?` if unattested).

### Step 3 — Determine the citation form

Same as `commentary-claims` Step 2: inspect the commentary body for leading segment numbers or Obsidian block IDs; set `citation_form` accordingly; state the resolved form in the output header.

### Step 4 — Compute each node's reading window

a. Flatten the parsed tree into document order (already true of the parse in Step 2d — every node, at any depth, in the order it appears in the tree file).
b. For each node in that order, its window starts at its own `[[line]]` and ends the line before the next node's `[[line]]` (any depth), or end-of-file for the last node. This means a parent node's window (before its first child) covers only its own opening/announcement text — correct, since the child's window then takes over.
c. For a node whose line is `?`, do not guess a line number. Fold its heading into the surrounding window of the nearest node (parent or preceding sibling) that does have a line number, and note this fold in the Coverage log's `Nodes with no independently attested line` row. The heading still appears in the output in its correct tree position; only its window boundary is approximate.
d. Anything before the first node's window is the `Front matter` window; anything after the last node's window is the `Back matter` window.

### Step 5 — Read the commentary in full, in order — and harvest grounding elements as you go

a. Read from the first line to the last. Do not sample or skip ahead to sections that look substantive.
b. Read in contiguous chunks sized so no chunk truncates mid-argument, same discipline as `commentary-claims` Step 3.
c. Track which node-window each chunk falls in as you go.
d. **While reading, collect every named referent into the Grounding index:** proper names and fixed epithets of figures and their forms/aspects, persons (author, teachers, lineage figures, the requester in the colophon), places, texts and mantras cited by name or incipit, and events or dates. Also harvest the TOC tree's own node titles (a title like "praise via the peaceful form" names a form) and the frontmatter (author, date). Record each entry's name verbatim, what the source itself says it is, and every location where it is attested. Assign stable IDs (`FIG-1`, `PER-1`, `PLC-1`, `TXT-1`, `EVT-1`, …).
e. Keep referents distinct exactly as the source keeps them distinct (Rule 16). Merge two mentions into one entry only when the source itself equates them (same name, or an explicit "that is, …" identification).

### Step 6 — Extract claims window by window, anchored

For each node window, in tree order:

a. Identify every distinct assertion the commentator makes within that window's lines.
b. For each assertion, write the Tibetan in the commentator's own wording, then the one-line English gloss, then the `Type:` tag.
c. **Anchor the claim (Rule 14):** determine what the claim is *about* and write the `Referent:` line. Search in this order and record the basis found: (1) the claim's own passage — is the subject named there? → `(stated)`; (2) the sentence that opens the section → `(section-opener)`; (3) the enclosing node's title and then each ancestor node's title up the tree → `(node)`. A claim may carry several referents (e.g. a figure and the text being quoted about it). If all three searches fail, write `[unanchored]` and log it in the Unanchored claims rollup with the reason.
d. Attach the segment or line citation.
e. Where the commentator marks an alternative view (འམ། / གཞན་དག་ན་རེ། / ཁ་ཅིག་ན་རེ།), mark it ⚑ inline under that node, and add a one-line entry to the Internal tensions rollup at the end. When the alternative view comes from a named source, that source is also a Grounding-index entry and the ⚑ claim's Referent line includes it.
f. If a window yields no claim of its own (pure announcement, or pure quotation), write "None — announcement only." (or the appropriate reason) under its heading rather than omitting the heading.

### Step 7 — Number the claims

a. Number sequentially within each node: `<decimal>.1`, `<decimal>.2`, … (e.g. node `1.1` → claims `1.1.1`, `1.1.2`). Front matter uses `0.1, 0.2, …`; back matter uses `Z.1, Z.2, …`.
b. Numbers are stable identifiers — never renumber an existing file when appending.

### Step 8 — Write headings at the right depth

a. Depth-1 tree nodes get `##`, depth-2 get `###`, depth-3+ all get `####` (flatten deeper levels into a nested bullet list under the `####` heading rather than inventing `#####`).
b. Each heading reproduces the node's decimal number and title exactly as the tree gives it, followed by its `[[line]]` (or the line it was folded to, if originally `?`).

### Step 9 — Finalise the Grounding index, rollups, and Coverage log

a. Write the Grounding index tables (all five kind-groups, "None attested." where empty), placing them before the first claims section so a reader meets the referents before the claims that use them.
b. Sweep every `Referent:` line and confirm each ID it names exists in the index; sweep every index entry and confirm at least one claim or ⚑ position references it — an entry nothing points to is either a missed anchoring opportunity (fix the claims) or noise (delete the entry).
c. List every ⚑ claim from Step 6e as a one-line entry: node number, claim id, English gloss.
d. List every `[unanchored]` claim in the Unanchored claims rollup with its reason.
e. Build the Coverage log table: one row per node (plus Front matter / Back matter), its source range, and the claim IDs drawn from it.
f. List any node whose line was folded (from Step 4c) and which neighbour it was folded into.
g. List any source ranges that yielded no claim at all, with the reason.

### Step 10 — Write the file

a. Write to `2-RAILS/Claims/toc-scaffolded/<registered-id>.md`, creating the directory if needed.
b. Fill `claim_count` with the total across all nodes plus front/back matter.
c. Set `status: draft` and `scaffold: toc-tree`.

### Step 11 — Self-verification

a. Confirm every numbered claim heading has a `**Cite:**` line (except ⚑ tension entries, which cite inline per position) **and a `**Referent:**` line that is either valid index ID(s) or exactly `[unanchored]`**.
b. Confirm every Grounding-index entry's "Attested at" locations actually contain the verbatim name — an entry whose name cannot be found at its cited location is invented; delete it and re-anchor its dependants.
c. Confirm no claim text or index entry mentions another commentary, the root text file, or a fact from outside this source (Rule 13).
d. Confirm every tree node has a corresponding heading, in the tree's own order, with no node skipped.
e. Confirm the Coverage log's ranges span the whole source file with no unexplained gap.
f. Confirm `claim_count` equals the number of claim entries actually present, and the Unanchored rollup lists exactly the claims marked `[unanchored]`.

---

## Completion check

- [ ] Commentary read in isolation, from first line to last
- [ ] TOC tree loaded from an existing `toc-tree-extraction` (or Gemini) output; skill stopped and reported if none was found — no structure was invented
- [ ] Output written to `2-RAILS/Claims/toc-scaffolded/<registered-id>.md` with `<registered-id>` matching the source frontmatter
- [ ] Frontmatter complete: `registered_id`, `title`, `author`, `source_file`, `toc_tree_source`, `citation_form`, `scaffold: toc-tree`, `claim_count`, `status: draft`
- [ ] Every TOC-tree node has a heading, in the tree's own document order and decimal numbering, none skipped or renumbered
- [ ] Every claim has a Tibetan statement, an English gloss, a `**Type:**`, a `**Referent:**` (valid index IDs with basis, or `[unanchored]`), and a `**Cite:**`
- [ ] Grounding index present with all five kind-groups (empty ones carry "None attested."), every entry verbatim-attested at its cited locations, no entry unreferenced by any claim
- [ ] No Grounding-index entry or referent identification drawn from parametric knowledge — only from the commentary body, its TOC-node titles, or its frontmatter
- [ ] Unanchored claims rollup lists exactly the `[unanchored]` claims, each with a reason
- [ ] Nodes with no independently attested line are listed in the Coverage log with the neighbour they were folded into
- [ ] Front matter and back matter (if any) captured, not dropped
- [ ] Alternative or conflicting positions marked ⚑ inline and listed in the Internal tensions rollup
- [ ] Coverage log accounts for the entire source file, including ranges that yielded nothing
- [ ] `claim_count` equals the number of claim entries actually present
- [ ] `1-SOURCES/` and the TOC tree file unmodified
