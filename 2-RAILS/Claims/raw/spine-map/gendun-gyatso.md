---
registered_id: gendun-gyatso
spine_scheme: tara21
source_tree: 2-RAILS/Sections/Raw/toc-tree/gendun-gyatso.md
source_claims: 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
root_text: 1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md
claim_count: 64
mapped_claims: 54
extra_claims: 8
ambiguous_claims: 0
unmapped_claims: 2
date: 2026-08-08
status: draft
---

# Spine map — gendun-gyatso

> Routing index only. This file records **which of this commentary's own TOC nodes hold
> which canonical spine slot's content** — nothing about what the claims say. It never
> quotes, interprets, or restates a claim; `assemble_packet.py` copies the claim text
> itself verbatim out of `2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md` at packet time.
> Every claim in that file has exactly one disposition below.

**Structure of this commentary.** A flat tree: one top node (`1.` དང་པོ་ལ་ཕྱག་འཚལ་ཚིགས་སུ་བཅད་པ་ཉི་ཤུ་རྩ་གཅིག)
carries no content of its own (announcement only) and divides directly into twenty ordinal
child nodes `1.1`–`1.19`, `1.21` — the node titles are themselves bare ordinals (དང་པོ་ནི
"the first", གཉིས་པ་ནི "the second", … ཉེར་གཅིག་ནི "the twenty-first"), each corresponding one-to-one
with the root text's `^1-1`–`^1-21` homage stanzas, followed by top node `2.` གཉིས་པ་དེའི་ཕན་ཡོན
("its benefits") holding the closing benefits/colophon material. There is no `1.20` node: the
tree's own gap between `1.19` and `1.21` is a genuine source gap (no twentieth ordinal is
attested anywhere in the source between the nineteenth and twenty-first headings), confirmed
in the raw claims file's node-1.21 heading note and by `toc-tree-qc-gendun-gyatso.md` — not an
extraction error. One node, `1.1`, is not mapped wholesale: its eight direct claims mix a
general structural announcement (the exposition's two-part division into praise and benefit-
explanation; the count of homage verses) with homage-1's own content (etymology, iconography,
origin narrative), so the two groups are separated by claim-level routing instead (see below).

## Slot map

| Slot | Root anchor | Node(s) | Node title(s) (verbatim) | Claims |
|---|---|---|---|---|
| `tara-02` | `^1-2` | `1.2` | གཉིས་པ་ནི | 2 |
| `tara-03` | `^1-3` | `1.3` | གསུམ་པ་ནི | 3 |
| `tara-04` | `^1-4` | `1.4` | བཞི་པ་ནི | 3 |
| `tara-05` | `^1-5` | `1.5` | ལྔ་པ་ནི | 3 |
| `tara-06` | `^1-6` | `1.6` | དྲུག་པ་ནི | 2 |
| `tara-07` | `^1-7` | `1.7` | བདུན་པ་ནི | 2 |
| `tara-08` | `^1-8` | `1.8` | བརྒྱད་པ་ནི | 3 |
| `tara-09` | `^1-9` | `1.9` | དགུ་པ་ནི | 2 |
| `tara-10` | `^1-10` | `1.10` | བཅུ་པ་ནི | 2 |
| `tara-11` | `^1-11` | `1.11` | བཅུ་གཅིག་ནི | 2 |
| `tara-12` | `^1-12` | `1.12` | བཅུ་གཉིས་པ་ནི | 2 |
| `tara-13` | `^1-13` | `1.13` | བཅུ་གསུམ་པ | 1 |
| `tara-14` | `^1-14` | `1.14` | བཅུ་བཞི་པ་ནི | 2 |
| `tara-15` | `^1-15` | `1.15` | བཅོ་ལྔ་པ་ནི | 2 |
| `tara-16` | `^1-16` | `1.16` | བཅུ་དྲུག་པ་ནི | 3 |
| `tara-17` | `^1-17` | `1.17` | བཅུ་བདུན་པ་ནི | 1 |
| `tara-18` | `^1-18` | `1.18` | བཅོ་བརྒྱད་པ་ནི | 2 |
| `tara-19` | `^1-19` | `1.19` | བཅུ་དགུ་པ | 4 |
| `tara-21` | `^1-21` | `1.21` | ཉེར་གཅིག་ནི | 3 |
| `benefits` | `^a-1`–`^a-7` | `2` | གཉིས་པ་དེའི་ཕན་ཡོན | 10 |

## Claim-level routing

| Slot | Claim ID(s) | Why routed by claim rather than by node |
|---|---|---|
| `tara-01` | `c-1-1-3`–`c-1-1-8` | Node `1.1`'s eight direct claims mix general structural content (see next row) with homage-1-specific etymology, word-glosses, and origin narrative. Mapping node `1.1` wholesale would sweep the two structural claims into `tara-01`'s packet, so the homage-1 content is routed by claim instead. |
| `structure` | `c-1-1-1`–`c-1-1-2` | Node `1.1`'s own first two claims state the sa-bcad division of the exposition as a whole (two parts — the actual praise, and explaining its benefit — and that the praise proper has twenty-one verses). This is general structural content about the whole work, not specific to homage 1, so it cannot be left inside a `tara-01` node mapping. |

## Ambiguous claims

| Claim ID | Candidate slots | Why uncertain |
|---|---|---|
| (none) | | |

## Silent slots

| Slot | Why silent (where derivable) |
|---|---|
| `tara-20` | No twentieth node exists in this commentary's tree — a genuine source gap, not an extraction artifact. The tree jumps from `1.19` (nineteenth) directly to `1.21` (twenty-first); the raw claims file's node-1.21 heading and `toc-tree-qc-gendun-gyatso.md` both confirm no twentieth ordinal is attested anywhere in the source between them. |
| `origin` | This commentary carries no separate ལོ་རྒྱུས / origin-narrative section. Its account of Tārā's arising from Avalokiteśvara's tears (identifying him as protector of the three worlds, and the golden lotus-pollen origin) sits inside homage 1's own node (`1.1`, claims `c-1-1-7`–`c-1-1-8`) rather than in a section of its own. |

## Unmapped nodes

| Node | Title (verbatim) | Claims | Why not a spine slot |
|---|---|---|---|
| `0` | (Front matter — no tree node; the extraction's own `## 0. Front matter` bucket) | 2 | The commentator's own opening homage/invocation (`ན་མོ་ཨཱརྱཏཱར་ཡེ།`) and the announcement that the praise will be divided into twenty-one verses. Front matter of the commentary itself, not content on any homage of the root text. |
