---
title: "Syncing the 21-Tārā root text to the WeBuddhist library — detailed report"
date: 2026-09-16
status: report
scope: "21-taras-rails root text vs Liturgy-rails copy vs live library.webuddhist.com"
companion: "[[backend-sync-tara-root-text-brief]]"
---

# Syncing the 21-Tārā root text to the WeBuddhist library — detailed report

Generated 2026-09-16 from three witnesses and the live API. Nothing was written to any vault source file or to the backend; every backend call was a `GET`.

| Witness | Where | State |
|---|---|---|
| **Live** | `https://library.webuddhist.com` — text `HyUbHGlzS9LsSrgiFQNYE`, edition `lEmYv8BrRQkOMPY9ymQpS`, segmentation `YxDH7GqdwYY3pTF1g2cvm` | 3 788 chars, 30 segments `0`–`29`, no table of contents, 6 aligned translations (en, hi, mn, ne, vi, zh) |
| **Liturgy source** | `Liturgy-rails/1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` | byte-identical to Live once block ids are stripped (verified: content and all 30 spans equal the upload payload) |
| **Liturgy inbox** | `Liturgy-rails/0-INBOX/སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` | expert edits not yet uploaded: title repeated as first body line, `## མཇུག་བྱང་།` + `### མཛད་བྱང་།` added before the colophon; no text change |
| **Rails** | `21-taras-rails/1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md` | 37 blocks (5 headings + 32 content blocks), hierarchical ids `I-*`, `1-*`, `2-*`, `a-*`; 13 lines read differently from Live |

Backend reference: OpenAPI `2.11.2` (live) and `openpecha-backend` branch `dev` at `cfec5ed` (2026-09-12; local clone was at `cd1c205`, four commits behind — none add an endpoint). The Liturgy vault's `4-SYSTEM/backend-update-plan.md` (2026-09-15) already documents the generic update path; this report applies it to this one text and adds what is specific to the rails scheme.

---

## 1. What differs — the complete inventory

### 1.1 Text readings (13 lines in 12 blocks + title)

Both witnesses have exactly 112 content lines, so every difference is in-place. The Rails frontmatter says the file was *copied from* the Liturgy critical edition on 2026-08-07, so every reading below is an edit made in the rails vault after the copy. Each should be confirmed as intentional by a domain specialist before it overwrites the live text — several are single-letter changes that alter the word.

| # | Live ref → Rails ref | Line | Live reads | Rails reads | Kind |
|---|---|---|---|---|---|
| 1 | `0` → `0` | H1 title | `༄༅།། སྒྲོལ་མ…` (two spaces after `#`, `།།`) | `༄༅། །སྒྲོལ་མ…` | punctuation / whitespace in the **title segment** |
| 2 | `1` → `I-1` | 1 | `…ཧི་ཏ་སཱ་ཀ།␠` (trailing space) | `…ཧི་ཏ་སཱ་ཀ །` (space before shad) | whitespace |
| 3 | `2` → `I-3` | 1 | `ཨོཾ་རྗེ་བཙུན་མ…` | `ཨོཾ། རྗེ་བཙུན་མ…` | punctuation (tsheg → shad + space) |
| 4 | `3` → `1-1` | 4 | `གེ་སར་བྱེ་བ་ལས་` | `གེ་སར་ཕྱེ་བ་ལས་` | **letter** (བ → ཕ) |
| 5 | `12` → `1-10` | 3 | `ཏུ་ཏྟཱར་ཡིས` | `ཏུ་ཏྟྭ་ར་ཡིས` | mantra orthography (ཱ → ྭ + tsheg) |
| 6 | `13` → `1-11` | 2 | `ནུས་པ་ཉིད་མ` | `ནུས་མ་ཉིད་མ` | **letter** (པ → མ) |
| 7 | `15` → `1-13` | 3 | `བརྐྱངས་གཡོན་བསྐུམས་…བསྐོར་དགའ` | `བརྐྱང་གཡོན་བསྐུམ་…བསྐོར་དགས` | **letters** (two ས dropped, འ → ས) |
| 8 | `16` → `1-14` | 3, 4 | `ཧཱུཾ` (U+0F7E) · `བགེམས་མ` | `ཧཱུྃ` (U+0F83) · `འགེམས་མ` | anusvāra sign + **letter** (བ → འ) |
| 9 | `18` → `1-16` | 4 | `ཧཱུཾ` | `ཧཱུྃ` | anusvāra sign |
| 10 | `19` → `1-17` | 2, 3 | `ཧཱུཾ` · `མན་དྷ་ར` | `ཧཱུྃ` · `མན་དཱ་ར` | anusvāra sign + Sanskrit orthography |
| 11 | `21` → `1-19` | 3 | `…བརྗིད་ཀྱིས། །ྃ` — stray U+0F83 after the shad | `…བརྗིད་ཀྱིས། །` | **defect on Live**; Rails is the repair |
| 12 | `22` → `1-20` | 3 | `ཏུཏྟཱ་ར་ཡིས` | `ཏུ་ཏྟྭ་ར་ཡིས` | mantra orthography |
| 13 | `24` → `2-1` | 2 | `རབ་དང་བརྗོད་པས` | `རབ་ཏུ་བརྗོད་པས` | **word** (དང → ཏུ) |
| 14 | `28` → `2-6` | last | `སོ་སོར་འཇོམས་འགྱུར། །` | `སོ་སོར་འཇོམས་འགྱུར་ཅིག །` | **word added** (ཅིག) |

The Liturgy inbox makes none of these edits; on text it still equals Live.

### 1.2 Segmentation (block boundaries)

Same 112 lines, cut differently. Live has 29 content segments, Rails has 32.

| Region | Live | Rails | Change |
|---|---|---|---|
| Sanskrit + Tibetan title lines | one block `1` (2 lines) | `I-1` (Sanskrit), `I-2` (Tibetan) | **split** 1 → 2 |
| Homages 1–20 | `3`–`22`, 4 lines each | `1-1`–`1-20`, 4 lines each | boundaries identical, ids differ |
| Homage 21 + closing couplet | one block `23` (6 lines) | `1-21` (4 lines) + `1-22` (2 lines) | **split** 1 → 2 |
| Benefits section (22 lines) | `24`–`28` cut 4 / 4 / 4 / 4 / 6 | `2-1`–`2-6` cut 2 / 4 / 4 / 4 / 3 / 5 | **re-cut**: every boundary moves, 5 → 6 blocks |
| Colophon | `29` (1 line, `back_matter`) | `a-1` (1 line) | identical text, id differs |

Because the Liturgy translations are line-parallel to the source (checked: all six carry 6/4/4/4/4/6 lines in blocks `23`–`28` and 2/1 lines in `1`/`2`, exactly like the Tibetan), the same re-cut can be applied mechanically to each translation by line count. That is the precondition for keeping 1:1 alignments (see §3.3).

### 1.3 Segment references (block ids)

| | Live | Rails |
|---|---|---|
| Scheme | flat `0`…`29` | `0`; `I-0`…`I-3`; `1-0`…`1-22`; `2-0`…`2-6`; `a-0`, `a-1` |
| References in total | 30 | 37 (5 heading/title segments + 32 content) |
| References that survive unchanged | 1 (`0`, and even its content changes) | — |

The backend stores `reference` as any non-empty string, so `I-1` and `a-1` are legal there. They are **not** legal for the Liturgy tooling: `block_ids.py` (`ID_RE = \d+(-\d+)*`), `liturgy_payloads.py` and `translation_payloads.build_pairs` all assume digit-only ids. If the Liturgy inbox note were stamped with the rails headings it would get `^1-0/^1-1…`, `^2-0/^2-1…`, `^3-*`, `^4-*` — a third scheme. One scheme has to be chosen for the backend reference strings; see §4, decision 2.

Note also that the rails vault is not internally consistent on this: `4-SYSTEM/Guidelines/vault-annex.md` §2 documents the benefits section as `^a-0`, `^a-1`…`^a-7`, the rails English/Hindi/Chinese zero-shot translations use `^a-1`…`^a-7`, but the root text file now carries `^2-0`, `^2-1`…`^2-6` + `^a-0`/`^a-1`. Twelve rails files cite root-text ids (5 commentaries, 5 claims pages, 1 plan, 1 Wikipedia file), mostly `^1-1`…`^1-22` and `^2-1`…`^2-6`. Settle this before the ids are pushed anywhere.

### 1.4 Table of contents / headings

| | Live | Liturgy inbox | Rails |
|---|---|---|---|
| Headings | none (H1 only) | `## མཇུག་བྱང་།` → `### མཛད་བྱང་།` before the colophon | `## མཚན་དོན་དང་འགྱུར་ཕྱག` (`I-0`) · `## 1. བསྟོད་པ་དངོས།` (`1-0`) · `## བསྟོད་པའི་ཕན་ཡོན།` (`2-0`) · `## མཛད་བྱང།` (`a-0`) |
| TOC annotation on backend | none (`GET …/table-of-contents` → `[]`) | would be 2 nested sections | would be 4 flat sections |

Two different TOC designs: the inbox marks only the colophon; Rails marks the four content divisions. They can be merged (`མཛད་བྱང` ≈ `མཛད་བྱང་།` — note the missing final shad in the rails heading, and the `1.` numeral in `1. བསྟོད་པ་དངོས།` that would otherwise land in the TOC title).

A heading can be represented on the backend in two ways, and the choice changes the content string:

- **Liturgy convention** — the heading text is inserted into `content` as a `title`-type segment (`^k-0`) and the TOC section points at it. Adding four headings therefore inserts four strings into the content and adds four segments: it is a content + segmentation change, not just an annotation.
- **Annotation-only** — the content stays verse-only; each TOC section is `{title: {bo: …}, span: {start, end}}` over the character range of that section. No new segments, no content change. The API supports this directly (`POST /v2/editions/{id}/table-of-contents`).

### 1.5 Text and edition metadata

| Field | Live | Rails frontmatter | Endpoint |
|---|---|---|---|
| `title.bo` | `སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།` | `title: སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།`, `title_in_source: …ལ་བསྟོད་པ།` | `PATCH /v2/texts/{id}` (`title`, `alt_titles`) |
| English title | none on backend (Liturgy note has `title_en: Praises to the Twenty-One Tārās`) | `Praise of the Twenty-One Taras` | `PATCH /v2/texts/{id}` (`alt_titles` or `title.en`) |
| author / contributions | `contributions: []` | `སངས་རྒྱས་བཅོམ་ལྡན་འདས (རྣམ་པར་སྣང་མཛད)` | `POST /v2/persons` then `PATCH /v2/texts/{id}` `contributions` |
| `bdrc` | `WA0XLF0FAD365454A` | same | — |
| `category_id` | `LCorCb2K98p3TICt3UCDm` | blank | — |
| edition `type` / `source` | `critical` / `https://webuddhist.com` | `critical` / long `source_description` | **no endpoint** (no `PATCH /v2/editions/{id}`) |

Side note: `Liturgy-rails/1-SOURCES/liturgy-catalog.json` still lists the pre-migration ids (`saXjClLpCGt5zM5yIkzLe` / `P4rtJBlE4hLKy6mgMmbqn`); the live ids are the ones in `upload_ledger.json` and in the note's frontmatter.

---

## 2. Endpoints that exist today (OpenAPI 2.11.2, confirmed against `dev`)

| Call | Used by the Liturgy pipeline? | Role in this update |
|---|---|---|
| `GET /v2/texts/{id}`, `GET /v2/editions/{id}`, `GET …/content`, `GET …/segmentation`, `GET …/segmentation/segments`, `GET …/alignments`, `GET …/alignments/{tgt}`, `GET …/table-of-contents` | yes (verification, `inbox_diff.py --live`) | snapshot before, verify after |
| `PATCH /v2/editions/{id}/content` — one `insert` / `delete` / `replace` per request | not yet (`content_patch_payloads.py` prepares payloads) | in-place character edits; also the whole-content replace once the segmentation is gone |
| `DELETE /v2/editions/{id}/segmentation` | not yet | required for any boundary or reference change; **cascades to every alignment** (`DETACH DELETE span, segment, segmentation`) |
| `POST /v2/editions/{id}/segmentation` | yes (inside edition creation) | re-post; `409` if one exists; `reference` is any non-empty string; types `paragraph / verse / title / back_matter / front_matter / top_segment` |
| `PUT /v2/editions/{src}/alignments/{tgt}` | yes (`upload_translations.py`) | replaces all pairs for that edition pair; validates each reference exists exactly once per side; n:1 pairs allowed |
| `DELETE /v2/editions/{src}/alignments/{tgt}` | one-off | — |
| `POST /v2/editions/{id}/table-of-contents`, `DELETE /v2/table-of-contents/{toc_id}` | no (`liturgy_payloads.py` never emits a TOC) | add the TOC; replace = delete + add |
| `PATCH /v2/texts/{id}` | one-off | title, alt_titles, contributions, license, category, bdrc, date |
| `POST /v2/persons` | no | author record, if wanted |
| `POST /v2/texts`, `POST /v2/texts/{id}/editions`, `DELETE /v2/texts/{id}`, `DELETE /v2/editions/{id}` | yes / one-off | **do not use** — the text id is referenced by six translations and by the rails vault |

Content-patch behaviour (from `database/span_database.py`, `dev`): spans after the edit shift; a span entirely inside a deleted/replaced range is dropped; a replace that covers several segments keeps only the first; references are never touched, so alignments survive an in-place edit. The four `dev` commits since the live deploy (issue 442) fix a boundary case in replace and reindex content-search after segmentation changes; they add no endpoint.

### 2.1 Endpoints that do not exist (and what they would save)

| Missing | Consequence for this text |
|---|---|
| `PUT /v2/editions/{id}/segmentation` (replace, matching by reference, keeping alignments for surviving references) | every boundary/id change = delete + post + re-PUT six alignments |
| `PATCH` a single segment's `reference` or `type` | renaming `3` → `1-1` in place is impossible; same rebuild |
| `PUT /v2/editions/{id}/content` (whole document, with segmentation) | whole replace must be `replace 0..len` after deleting the segmentation |
| `PATCH /v2/editions/{id}` | edition `type` / `source` / `colophon` cannot be changed |
| batched / transactional content ops with a length precondition | 14 hunks = 14 sequential requests, no rollback |
| `PUT` table of contents | minor; delete + add works |

---

## 3. Update cases — what the API can and cannot absorb

| # | Case | Present in Tārā? | In place? | Alignments | How |
|---|---|---|---|---|---|
| 1 | Character edit inside a segment (letters, punctuation, whitespace) | yes — 14 lines (§1.1) | yes | kept | `PATCH …/content`, one op per hunk, highest offset first |
| 2 | Segment split / merge / boundary move | yes — 3 places (§1.2) | **no** | **dropped**, re-PUT | `DELETE` seg → `POST` seg → `PUT` alignments ×6 |
| 3 | Reference (block id) renumbering, boundaries unchanged | yes — 29 of 30 ids | **no** | **dropped**, re-PUT | same rebuild |
| 4 | Heading inserted into content as a `title` segment | yes if Liturgy convention — 4 headings | **no** | dropped, re-PUT | content insert + rebuild |
| 5 | TOC annotation added / replaced (annotation-only) | yes | yes | kept | `POST …/table-of-contents` (delete old one first if any) |
| 6 | Segment `type` change (`verse` ↔ `paragraph` ↔ `back_matter`) | possibly (`1-22` two-line block) | **no** | dropped | rebuild |
| 7 | Text metadata (title, alt titles, author, license, category) | yes (§1.5) | yes | n/a | `PATCH /v2/texts/{id}` |
| 8 | Edition metadata (`type`, `source`, colophon) | minor | **no endpoint** | n/a | — |
| 9 | Translation re-segmented to match the new source cut | needed for 1:1 pairs | no | dropped, re-PUT | per translation: `DELETE` seg → `POST` seg (content unchanged) |
| 10 | Alignment pairs rebuilt for new references | yes, ×6 | yes | replaced | `PUT …/alignments/{tgt}` with new pairs |
| 11 | Whole-content replace | alternative to 14 hunks | only after the segmentation is deleted | dropped | `replace 0..3788` |

### 3.1 Do these changes affect the existing alignments?

Yes. The six alignments hang off the `Segment` nodes of segmentation `YxDH7GqdwYY3pTF1g2cvm`. Cases 2, 3, 4 and 6 all require `DELETE /v2/editions/lEmYv8BrRQkOMPY9ymQpS/segmentation`, and that query deletes the segments and every `ALIGNED_TO` relationship on them. Nothing is updated automatically; there is no migration of alignments to new references. Between the delete and the last `PUT`, the library shows the Tibetan text with no translations.

Only the 14 character edits (case 1) could go through without touching alignments — but since the segmentation is being rebuilt anyway, it is simpler to fold them into one whole-content replace after the delete.

### 3.2 Will the alignments be "updated"?

Only if they are re-PUT with pairs built from the **new** references. The pair list is trivial to derive because the old→new map is deterministic (§1.2): `1 → I-1 + I-2`, `2 → I-3`, `3…22 → 1-1…1-20`, `23 → 1-21 + 1-22`, `24…28 → 2-1…2-6` (re-cut by line), `29 → a-1`. Two ways to express it:

- **Re-cut the translations too** (recommended). Each translation edition gets a new segmentation with the same 37 references, cut by line count. Then pairs are identity again (`I-1 ↔ I-1`, …), `translation_payloads.build_pairs` stays valid (once it accepts letter ids), and the reader sees 1:1 blocks. Cost: 6 × (delete + post segmentation).
- **Keep the translations as they are** and PUT many-to-one pairs (`I-1 → 1`, `I-2 → 1`, `1-21 → 23`, `1-22 → 23`, and for the benefits section 2-line-shifted pairs that no longer line up cleanly). The API accepts this, but the benefits section would be misaligned by two lines per block — a visible defect. Not recommended.

The translations are DharmaMitra zero-shot output; the four word-level edits (`ཕྱེ་བ`, `ནུས་མ`, `རབ་ཏུ`, `ཅིག`) may leave their lines stale. Re-translating those four lines is a separate, optional step.

### 3.3 Full call sequence for this text

```
GET    /v2/editions/{ed}/alignments                  snapshot (6 targets)
GET    …/content, …/segmentation/segments             snapshot
DELETE /v2/editions/{ed}/segmentation                 6 alignments go with it
PATCH  /v2/editions/{ed}/content  replace 0..3788     new content (with or without heading strings)
POST   /v2/editions/{ed}/segmentation                 37 (or 32) segments, rails references
for each of 6 translations:
  DELETE /v2/editions/{tr}/segmentation
  POST   /v2/editions/{tr}/segmentation               same references, cut by line
  PUT    /v2/editions/{ed}/alignments/{tr}            identity pairs
POST   /v2/editions/{ed}/table-of-contents            4 sections (bo titles, spans)
PATCH  /v2/texts/{text}                               title / alt_titles / contributions, if decided
GET    everything again                               verify content, 37 refs, 6 × pairs, TOC
```

About 25 mutating calls; ledger after every call, as `upload_liturgy.py` does. If the translations are not re-cut, 12 fewer calls.

---

## 4. Decisions needed before anything is sent

1. **Which readings win.** Confirm each of the 14 lines in §1.1 (especially rows 4, 6, 7, 8, 13, 14). Row 11 is an unambiguous defect on Live and should be fixed regardless.
2. **One reference scheme.** Backend references become the rails ids (`I-1`, `1-1`, `2-1`, `a-1`) — recommended, since the rails vault cites them — *or* stay digit-only for the Liturgy tooling. If rails ids: (a) reconcile the rails vault first (`2-*` in the root text vs `a-*` in the annex and the rails translations), (b) extend `block_ids.py` / `translation_payloads.build_pairs` to accept letters, or upload this text through the vendored parser path, which already accepts them.
3. **Headings in content or annotation-only.** Liturgy convention inserts heading text into `content` as `title` segments; the alternative keeps content verse-only and expresses sections purely as TOC spans. Also settle the heading titles (`1.` numeral, missing shad in `མཛད་བྱང`, whether to keep the inbox's `མཇུག་བྱང་།` level above `མཛད་བྱང་།`).
4. **Ownership of the Liturgy copy.** After the push, `Liturgy-rails/1-SOURCES/Text/…` and `0-INBOX/…` no longer describe the live state. Either regenerate them from the rails file (the Liturgy `inbox_diff` will then treat the rails text as the source) or mark the text as maintained from the rails vault.
5. **Re-cut the translations or accept n:1 pairs** (§3.2).
6. **Metadata**: keep `title.bo` as `…ལ་བསྟོད་པ།` (matches the text's own title line) and add the English title as `alt_titles`; whether to create a person record for the author.

## 5. Tooling gaps on the vault side

- No rebuild script exists yet; `upload_liturgy.py` / `upload_translations.py` only create, `content_patch_payloads.py` only handles boundary-preserving edits and will classify this text as *rebuild*.
- No TOC payload emitter (`liturgy_payloads.py` deliberately skips `build_toc`; the vendored parser has one that builds sections from `title` segments).
- No translation re-cut / old→new reference map builder.
- `.env.local` in `Liturgy-rails/4-SYSTEM/scripts/` carries a note that the API key was pasted into a chat on 2026-09-01 and should be rotated; rotate it before the write run.
