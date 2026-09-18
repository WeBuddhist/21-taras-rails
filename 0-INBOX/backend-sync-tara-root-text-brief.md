---
title: "Syncing the 21-Tārā root text to the WeBuddhist library — brief"
date: 2026-09-16
status: report
companion: "[[backend-sync-tara-root-text-detailed]]"
---

# 21-Tārā root text → WeBuddhist library — brief

Live text `HyUbHGlzS9LsSrgiFQNYE` · edition `lEmYv8BrRQkOMPY9ymQpS` · API 2.11.2 · read-only check on 2026-09-16.

## 1. Where the three copies stand

| Copy | Segments / ids | TOC | Text | Notes |
|---|---|---|---|---|
| Live backend | 30, flat `0`–`29` | none | = Liturgy source, byte for byte | 6 translations aligned 1:1 (en hi mn ne vi zh) |
| Liturgy inbox (expert edits) | would restamp to `0-*` / `1-*` | 2 colophon headings | = Live | title line repeated; not uploaded |
| Rails root text | 37 (5 headings + 32 blocks), `I-*` `1-*` `2-*` `a-*` | 4 section headings | 13 lines differ | only id `0` survives, and its content changes too |

## 2. What must change on the backend (Live → Rails)

| Area | Change | Count |
|---|---|---|
| Text readings | letter/word edits, mantra orthography (`ཏུ་ཏྟྭ་ར`, `ཧཱུྃ`), punctuation, one stray `ྃ` defect on Live | 14 lines (4 change a word: `ཕྱེ་བ`, `ནུས་མ`, `རབ་ཏུ`, `+ཅིག`) |
| Segmentation | split title block (`1` → `I-1`,`I-2`); split homage 21 (`23` → `1-21`,`1-22`); re-cut benefits 4/4/4/4/6 → 2/4/4/4/3/5 | 29 → 32 content segments |
| References | flat digits → hierarchical rails ids | 29 of 30 renamed |
| TOC | none → 4 sections (`མཚན་དོན་…`, `བསྟོད་པ་དངོས།`, `བསྟོད་པའི་ཕན་ཡོན།`, `མཛད་བྱང`) | +4 sections (+4 title segments if headings go into content) |
| Alignments | all 6 rebuilt with new references; translations re-cut by line (they are line-parallel, verified) | 6 × (re-seg + PUT) |
| Text metadata | English title, author, optional | `PATCH /v2/texts` |
| Edition metadata | nothing needed; no endpoint anyway | — |

## 3. Update cases vs. API support

| Case | In place? | Alignments | Endpoint |
|---|---|---|---|
| Character edit inside a segment | ✅ | kept | `PATCH …/content` (1 op per call) |
| Split / merge / move a boundary | ❌ | **dropped** | `DELETE` + `POST …/segmentation`, then `PUT` alignments |
| Rename block ids (references) | ❌ | **dropped** | same rebuild |
| Change a segment's type | ❌ | dropped | same rebuild |
| Add heading as a title segment in content | ❌ | dropped | content insert + rebuild |
| Add / replace TOC (annotation only) | ✅ | kept | `POST …/table-of-contents`; replace = `DELETE` + `POST` |
| Re-cut a translation | ❌ | dropped | `DELETE` + `POST` seg on the translation |
| Replace alignment pairs | ✅ | replaced | `PUT …/alignments/{tgt}` (n:1 allowed) |
| Text metadata | ✅ | n/a | `PATCH /v2/texts/{id}` |
| Edition metadata | ❌ | n/a | **no endpoint** |
| Whole-content replace | only after seg delete | dropped | `replace 0..len` |

**Missing endpoints:** `PUT …/segmentation` (replace keeping alignments by reference), `PATCH` a segment's reference/type, `PUT …/content`, `PATCH /v2/editions/{id}`, batched/atomic content ops, `PUT` TOC. `dev` (`cfec5ed`, 2026-09-12) adds none of these.

## 4. Effect on existing alignments

- **Yes, they are affected.** Every boundary or id change requires deleting the segmentation, and that query deletes every alignment on it. Nothing migrates automatically.
- **They are updated only by re-PUT** with pairs built from the new ids. Old→new map is deterministic: `1→I-1+I-2`, `2→I-3`, `3–22→1-1–1-20`, `23→1-21+1-22`, `24–28→2-1–2-6` (by line), `29→a-1`.
- Recommended: re-cut the 6 translations to the same 37 references → identity pairs, 1:1 display. Alternative: keep them and PUT n:1 pairs → benefits section misaligned by 2 lines per block.
- Window with no translations shown: from the segmentation delete to the last PUT (~25 calls).

## 5. Call order (per text)

```
GET snapshot → DELETE seg → PATCH content replace 0..3788 → POST seg (rails refs)
→ ×6: DELETE tr seg → POST tr seg → PUT alignments
→ POST table-of-contents → PATCH /v2/texts (optional) → GET verify
```

## 6. Decide first

| # | Decision | Recommendation |
|---|---|---|
| 1 | Which of the 14 readings are intentional (rails file was copied from Liturgy on 2026-08-07; all diffs are later rails edits) | specialist sign-off per line; the stray `ྃ` fix is safe |
| 2 | Reference scheme on the backend | rails ids — but first reconcile rails `2-*` (root file) vs `a-*` (annex + rails translations); make `block_ids.py` / `build_pairs` accept letters |
| 3 | Headings in `content` (Liturgy convention) or TOC spans only | pick one; fix `1.` numeral and `མཛད་བྱང` shad |
| 4 | Who owns the Liturgy copy afterwards | regenerate Liturgy `1-SOURCES`/`0-INBOX` from rails, or mark as rails-maintained |
| 5 | Re-cut translations vs n:1 pairs | re-cut |
| 6 | Re-translate the 4 word-changed lines in the zero-shot translations | optional follow-up |

## 7. Vault tooling still missing

No rebuild script, no TOC emitter, no translation re-cut / id-map builder, letter ids unsupported in `block_ids.py`. Rotate the API key in `Liturgy-rails/4-SYSTEM/scripts/.env.local` before the write run (its own comment says it was pasted into a chat).
