---
title: Machine drafts — what's here
file_type: index
updated: 2026-09-25
---

# Machine drafts — raw, not for use

Raw output of DharmaMitra and Gemini (`machine-translate`). Never edited by hand and never the translation
to use: the current translations are the `<lang>-general/` folders one level up
([[3-TRANSFORMATIONS/Translations/00-INDEX-current-translations|index]]). Each folder here is the starting
draft of one of them, or a reading aid.

## `zero-shot/` — no word list

The scripts write here by default (`<engine>-<tag>`).

| Folder | Language | Became | On the platform |
|---|---|---|---|
| `dharmamitra-en/` | English | draft 0 of en-general | yes (baseline) |
| `dharmamitra-zh/` | Chinese | draft 0 of zh-general | yes (baseline) |
| `gemini-vi/` | Vietnamese | draft 1 of vi-general | yes (baseline) |
| `gemini-hi/` | Hindi | draft 1 of hi-general | yes (baseline) |
| `gemini-ne/` | Nepali | draft 1 of ne-general | yes (baseline) |
| `gemini-mn/` | Mongolian | the starting point for Mongolian (not started) | yes (baseline) |

## `primed/` — run with the word list

Each request carried that language's locked words for its verses (`glossary.tsv`, built by
`keyword-standardize`). Written with `--out`.

| Folder | Language | Became | Locked words (zero-shot → primed) |
|---|---|---|---|
| `dharmamitra-en-general/` | English | draft 1 of en-general | — |
| `dharmamitra-zh-general/` | Chinese | draft 1 of zh-general | 63 → 122 of 137 |
| `gemini-ne-general/` | Nepali | draft 2 of ne-general; `run-ne-general.sh` re-runs it on the Mac | 126 → 128 of 136 |

## `commentaries/` — the commentaries, not the root

| Folder | Language | What it is | On the platform |
|---|---|---|---|
| `dharmamitra-en/` | English | DharmaMitra zero-shot of the eight Tibetan commentaries (reading aid) | yes (2026-09-24) |
| `dharmamitra-zh/` | Chinese (Traditional) | the same, in Chinese | yes (2026-09-24) |

Moved here on 2026-09-25 from `Dharmamitra/<tag>/` and `Gemini/<tag>/`; every path in the vault was updated.
The append-only ledgers in each `work/` keep the old paths, as a record of where each run wrote.
