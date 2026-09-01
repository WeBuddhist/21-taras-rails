---
registered_id: lobsang-dawa
spine_scheme: tara21
source_tree: 2-RAILS/Sections/Raw/toc-tree/lobsang-dawa.md
source_claims: 2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md
root_text: 1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md
claim_count: 87
mapped_claims: 54
extra_claims: 24
ambiguous_claims: 0
unmapped_claims: 9
date: 2026-08-08
status: draft
---

# Spine map — lobsang-dawa

> Routing index only. This file records **which of this commentary's own TOC nodes hold
> which canonical spine slot's content** — nothing about what the claims say. It never
> quotes, interprets, or restates a claim; `assemble_packet.py` copies the claim text
> itself verbatim out of `2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md` at packet time.
> Every claim in that file has exactly one disposition below.

**Structure of this commentary.** A six-level sa-bcad tree with six announcement-only
pass-through nodes (`1.2`, `1.2.2`, `1.2.2.1`, `1.2.2.1.1`, `1.2.2.1.2`, `1.2.3`) whose own
division statements the extraction physically attaches to the first content-bearing child's
window rather than to the parent's own, so five division claims (plus node `1`'s own opening
division statement, addressed `c-1-0-1`) are routed by claim ID rather than by node, per
Rule 4. Homage 1's content sits inside a dedicated "praise by way of history" node (`1.2.1`)
rather than a numbered homage node — its wording matches root `^1-1` term for term (etymologies
of "heroine," "all-seeing," and the lotus-face origin), so `tara-01` is silent and `1.2.1`
maps to `origin` instead. The body-form branch runs peaceful (`1.2.2.1.1.1`–`.6` → `tara-02`–
`tara-07`), then wrathful (`1.2.2.1.2.1`–`.7` → `tara-08`–`tara-14`), then dharmakāya
(`1.2.2.2` → `tara-15`); the activity branch (`1.2.3.1`–`.6` → `tara-16`–`tara-21`) follows
the same ordinal pattern. The commentary's in-text "Verse N" citations are its own continuous
count (5 … 47), not the root's `^1-N` numbering, so every node-to-slot correspondence below is
established by matching the claims' quoted wording against
`1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md`, never by the cited number. The tree contains
no exposition of the root's ཕན་ཡོན (benefits) section — the conclusion (`1.3`) only states the
praise's total stanza-count — so `benefits` is also silent.

## Slot map

| Slot | Root anchor | Node(s) | Node title(s) (verbatim) | Claims |
|---|---|---|---|---|
| `tara-03` | `^1-3` | `1.2.2.1.1.2` | གཉིས་པ་ | 3 |
| `tara-04` | `^1-4` | `1.2.2.1.1.3` | གསུམ་པ་ | 4 |
| `tara-05` | `^1-5` | `1.2.2.1.1.4` | བཞི་པ་ | 3 |
| `tara-06` | `^1-6` | `1.2.2.1.1.5` | ལྔ་པ་ | 3 |
| `tara-07` | `^1-7` | `1.2.2.1.1.6` | དྲུག་པ་ | 3 |
| `tara-09` | `^1-9` | `1.2.2.1.2.2` | ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ | 2 |
| `tara-10` | `^1-10` | `1.2.2.1.2.3` | གསུམ་པ་ | 3 |
| `tara-11` | `^1-11` | `1.2.2.1.2.4` | བཞི་པ་ | 3 |
| `tara-12` | `^1-12` | `1.2.2.1.2.5` | ལྔ་པ་ | 3 |
| `tara-13` | `^1-13` | `1.2.2.1.2.6` | དྲུག་པ་ | 3 |
| `tara-14` | `^1-14` | `1.2.2.1.2.7` | བདུན་པ་ | 3 |
| `tara-15` | `^1-15` | `1.2.2.2` | གཉིས་པ་ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ | 3 |
| `tara-17` | `^1-17` | `1.2.3.2` | གཉིས་པ་ | 4 |
| `tara-18` | `^1-18` | `1.2.3.3` | གསུམ་པ་ | 3 |
| `tara-19` | `^1-19` | `1.2.3.4` | བཞི་པ་ | 3 |
| `tara-20` | `^1-20` | `1.2.3.5` | ལྔ་པ་ | 3 |
| `tara-21` | `^1-21` | `1.2.3.6` | དྲུག་པ་ | 3 |
| `structure` | (none — global slot, no single root anchor) | `1.3` | གསུམ་པ་མཇུག་བསྡུ་བ | 2 |

## Claim-level routing

| Slot | Claim ID(s) | Why routed by claim rather than by node |
|---|---|---|
| `structure` | `c-1-0-1` | Node `1`'s own direct claim (the commentary's own front-of-text three-part division of the whole explanation). The extraction addresses it with a `-0-` sentinel rather than a real node segment (see that file's Coverage log), so it is not swept by any node-based Slot map row. |
| `structure` | `c-1-2-1-1` | Node `1.2.1`'s first claim states the division of its *parent* node `1.2` into three, not `1.2.1`'s own history content; routing it separately keeps node `1.2.1` from being added to the Slot map (which would otherwise sweep this claim into `origin` along with the rest). |
| `structure` | `c-1-2-2-1-1-1-1`–`c-1-2-2-1-1-1-3` | These three claims state the divisions of ancestor nodes `1.2.2`, `1.2.2.1`, and `1.2.2.1.1` (each an "announcement only" pass-through with no content block of its own); the extraction's window boundaries place them inside leaf node `1.2.2.1.1.1` ahead of that leaf's own verse content. |
| `structure` | `c-1-2-2-1-2-1-1` | States the division of ancestor node `1.2.2.1.2` (seven-way, wrathful forms); placed inside leaf node `1.2.2.1.2.1`'s window ahead of that leaf's own verse content. |
| `structure` | `c-1-2-3-1-1` | States the division of ancestor node `1.2.3` (six-way, activity); placed inside leaf node `1.2.3.1`'s window ahead of that leaf's own verse content. |
| `origin` | `c-1-2-1-2`–`c-1-2-1-6` | Node `1.2.1`'s remaining five claims are its own history/origin content (etymologies and the lotus-face origin, matching root `^1-1` term for term); routed by claim rather than by node because the node's first claim (`c-1-2-1-1`) belongs to `structure` instead (see above). |
| `tara-02` | `c-1-2-2-1-1-1-4`–`c-1-2-2-1-1-1-6` | Node `1.2.2.1.1.1`'s own opener and two verse-quotation claims (matching root `^1-2`); the node's first three claims are ancestor-division statements routed to `structure` instead. |
| `tara-08` | `c-1-2-2-1-2-1-2`–`c-1-2-2-1-2-1-5` | Node `1.2.2.1.2.1`'s own opener and three verse-quotation claims (matching root `^1-8`); the node's first claim is an ancestor-division statement routed to `structure` instead. |
| `tara-16` | `c-1-2-3-1-2`–`c-1-2-3-1-6` | Node `1.2.3.1`'s own opener and four verse-quotation claims (matching root `^1-16`); the node's first claim is an ancestor-division statement routed to `structure` instead. |

## Ambiguous claims

| Claim ID | Candidate slots | Why uncertain |
|---|---|---|
| (none) | | |

## Silent slots

| Slot | Why silent (where derivable) |
|---|---|
| `tara-01` | This commentary gives verse 1's content — the etymologies matching "heroine," "all-seeing" (eyes like lightning), and the origin from Avalokiteśvara's lotus-face — inside its dedicated `1.2.1` history/origin node rather than a numbered homage node. That content is mapped to `origin` instead; no node or claim independently addresses `tara-01`. |
| `benefits` | The tree's final node (`1.3`, "the conclusion") states only the praise's total stanza-count via the peaceful and wrathful root mantras; no node or claim in this commentary's raw claims file quotes or comments on the root text's ཕན་ཡོན section (`^a-1`–`^a-7`). |

## Unmapped nodes

| Node | Title (verbatim) | Claims | Why not a spine slot |
|---|---|---|---|
| `0` | (Front matter — no tree node; the extraction's own `## 0. Front matter` bucket) | 3 | The containing anthology's title, the compiler credit, and this commentary's own title — front matter of the commentary, not content on any homage or the benefits section. |
| `1.1` | དང་པོ་མདོར་བསྟན་པ | 5 | Glosses OM and etymologizes "Venerable Lady," "Noble One," and "Tārā" from the root text's title/invocation line (`^I-1`), not from any homage stanza. The invocation is not a registered spine slot. |
| `z` | (Back matter — no tree node; the extraction's own `## Z. Back matter` bucket) | 1 | The compiler's own colophon (name and date of compilation) — back matter of the commentary, not content on the root text. |
