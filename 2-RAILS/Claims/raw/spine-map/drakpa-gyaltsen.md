---
registered_id: drakpa-gyaltsen
spine_scheme: tara21
source_tree: 2-RAILS/Sections/Raw/toc-tree/drakpa-gyaltsen.md
source_claims: 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
root_text: 1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md
claim_count: 142
mapped_claims: 24
extra_claims: 118
ambiguous_claims: 0
unmapped_claims: 0
date: 2026-08-08
status: draft
---

# Spine map — drakpa-gyaltsen

> Routing index only. This file records **which of this commentary's own TOC nodes hold
> which canonical spine slot's content** — nothing about what the claims say. It never
> quotes, interprets, or restates a claim; `assemble_packet.py` copies the claim text
> itself verbatim out of `2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md` at packet
> time. Every claim in that file has exactly one disposition below.

**Structure of this commentary.** The finished TOC tree has only two top-level nodes: `1.`
བསྟོད་པ་དངོས་ ("the actual praise") and `2.` ཕན་ཡོན་ ("the benefits") — no further
subdivision. Node `1` runs all twenty-one homages undivided, so it cannot be a Slot map
row; every one of its 102 claims is routed by claim ID instead, using the root-verse
quotation embedded in each claim's own བོད་ཡིག field as the boundary marker (e.g. `c-1-1`
opens with ^1-1's own first line, ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ།; `c-1-8` opens with ^1-2's
first line, ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ།; and so on through all 21 stanzas). Two of node 1's
own claims (`c-1-101`, `c-1-102`) quote not a homage but the closing benefits section's own
opening/count stanza (^a-1: རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག) — this
commentary's own node boundary splits ^a-1 mid-stanza, with its first two lines glossed at
the tail of node 1 and its last two lines (`c-2-1`, `c-2-2`) at the head of node 2; both
halves route to the single `benefits` slot. Node `2` corresponds cleanly to the rest of the
benefits section (recitation benefits through the colophon) and maps as a whole.
Before the tree's first node, a pseudo-node `0` (front matter, outside the sa-bcad tree —
per `verify_spine_map.py --counts`) carries the treatise's title, the commentator's own
homage to the Buddha, a long and detailed prose sa-bcad outline of the whole text (two-part
division, subdivided down to the six-fold division of activity and the four-fold division
of the benefits), an authorial attribution of that outline, and the commentator's own
opening homage to Tārā. The outline claims (`c-0-3`–`c-0-14`) are exactly the kind of
content the `structure` global slot exists for and are routed there by claim ID; the
remaining front-matter claims in the same pseudo-node (`c-0-1`, `c-0-2`, `c-0-15`,
`c-0-16`) are not spine content and have no registered slot. They cannot be placed in the
Unmapped nodes table under node `0`, because that table disposes of a whole node's subtree
and node `0` also holds the already-routed structure claims — doing so would double-cover
`c-0-3`–`c-0-14`. They are listed instead as a Claim-level routing row with an
intentionally blank Slot cell, so the routing decision (no slot applies) is still recorded
against those specific claim IDs.

## Slot map

| Slot | Root anchor | Node(s) | Node title(s) (verbatim) | Claims |
|---|---|---|---|---|
| `benefits` | `^a-1`–`^a-7` | `2` | ཕན་ཡོན་ | 24 |

## Claim-level routing

| Slot | Claim ID(s) | Why routed by claim rather than by node |
|---|---|---|
| `tara-01` | `c-1-1`–`c-1-7` | Node `1` runs all 21 homages undivided; `c-1-1` opens by quoting ^1-1's own first line. |
| `tara-02` | `c-1-8`–`c-1-11` | Same undivided node; `c-1-8` opens by quoting ^1-2's own first line. |
| `tara-03` | `c-1-12`–`c-1-22` | Same undivided node; `c-1-12` opens by quoting ^1-3's own first line. |
| `tara-04` | `c-1-23`–`c-1-27` | Same undivided node; `c-1-23` opens by quoting ^1-4's own first line. |
| `tara-05` | `c-1-28`–`c-1-33` | Same undivided node; `c-1-28` opens by quoting ^1-5's own first line. |
| `tara-06` | `c-1-34`–`c-1-44` | Same undivided node; `c-1-34` opens by quoting ^1-6's own first line. |
| `tara-07` | `c-1-45`–`c-1-48` | Same undivided node; `c-1-45` opens by quoting ^1-7's own first line. |
| `tara-08` | `c-1-49`–`c-1-54` | Same undivided node; `c-1-49` opens by quoting ^1-8's own first line. |
| `tara-09` | `c-1-55`–`c-1-58` | Same undivided node; `c-1-55` opens by quoting ^1-9's own first line. |
| `tara-10` | `c-1-59`–`c-1-63` | Same undivided node; `c-1-59` opens by quoting ^1-10's own first line. |
| `tara-11` | `c-1-64`–`c-1-67` | Same undivided node; `c-1-64` opens by quoting ^1-11's own first line. |
| `tara-12` | `c-1-68`–`c-1-71` | Same undivided node; `c-1-68` opens by quoting ^1-12's own first line. |
| `tara-13` | `c-1-72`–`c-1-74` | Same undivided node; `c-1-72` opens by quoting ^1-13's own first line. |
| `tara-14` | `c-1-75`–`c-1-77` | Same undivided node; `c-1-75` opens by quoting ^1-14's own first line. |
| `tara-15` | `c-1-78`–`c-1-82` | Same undivided node; `c-1-78` opens by quoting ^1-15's own first line. |
| `tara-16` | `c-1-83`–`c-1-84` | Same undivided node; `c-1-83` quotes ^1-16's third line (the ten-syllable-mantra line) and `c-1-84` its fourth. |
| `tara-17` | `c-1-85`–`c-1-87` | Same undivided node; `c-1-85` opens by quoting ^1-17's own first line. |
| `tara-18` | `c-1-88`–`c-1-90` | Same undivided node; `c-1-88` opens by quoting ^1-18's own first line. |
| `tara-19` | `c-1-91`–`c-1-93` | Same undivided node; `c-1-91` opens by quoting ^1-19's own first line. |
| `tara-20` | `c-1-94`–`c-1-96` | Same undivided node; `c-1-94` quotes ^1-20's full stanza before glossing it. |
| `tara-21` | `c-1-97`–`c-1-100` | Same undivided node; `c-1-97` opens by quoting ^1-21's own first line. |
| `benefits` | `c-1-101`–`c-1-102` | These two claims sit at the tail of node 1's flat bucket but quote ^a-1 (the benefits section's own opening/count stanza), not a homage; this commentary's node boundary splits ^a-1 mid-stanza (see `c-2-1`–`c-2-2` below for its other half). |
| `structure` | `c-0-3`–`c-0-14` | Pseudo-node `0` (front matter, outside the tree) mixes the commentator's own prose sa-bcad outline of the whole praise with unrelated front-matter material (title, homages, attribution); these twelve claims are the outline itself and cannot be mapped by node, so they are routed by claim ID. |
|  | `c-0-1`, `c-0-2`, `c-0-15`, `c-0-16` | (Slot cell intentionally blank — no registered slot applies.) Front matter proper: title of the treatise, the commentator's own homage to the Buddha, the authorial attribution of the outline, and the commentator's own opening homage to Tārā. Not spine content. Recorded here rather than in Unmapped nodes because node `0` also holds the structure claims above and Unmapped nodes disposes of whole nodes only; listing node `0` there would double-cover `c-0-3`–`c-0-14`. |

## Ambiguous claims

| Claim ID | Candidate slots | Why uncertain |
|---|---|---|
| (none) | | |

## Silent slots

| Slot | Why silent (where derivable) |
|---|---|
| `origin` | This commentary carries no separate ལོ་རྒྱུས / origin-narrative node; its account of Tārā's arising from the opened lotus's pollen sits inside homage 1's own exposition (`c-1-7`, routed to `tara-01`) rather than in a dedicated history section. |

## Unmapped nodes

| Node | Title (verbatim) | Claims | Why not a spine slot |
|---|---|---|---|
| none | | | |
