# Claims → library edition remap

Status: draft, 2026-11-04. The library addresses are written into the 8 claims files in
`2-RAILS/Claims/raw/tree-guided/`, as a `**Library:**` line under each claim's `**Cite:**`
line, and as `library_*` fields in the frontmatter. The old `**Cite:**` lines are not changed,
and nothing in `1-SOURCES/` is changed.

## The problem

The tree-guided claims in `2-RAILS/Claims/raw/tree-guided/` were extracted in August 2026.
They cite the commentary files in `1-SOURCES/Commentaries/used for wiki/`, which use the old
blocks `^0-N`. Those blocks were not proofread or segmented by a person.

The proofread and resegmented commentaries are in `1-SOURCES/Commentaries/New raw data/`.
These are the files that are uploaded to the WeBuddhist library. Each file's frontmatter has its
`text_id`, `edition_id` and `toc_id`. Each block ID in these files (for example `^2-5`) is the
`reference` of a segment in the library edition.

So the claims point to text that the library does not have.

## What the script does

`remap_claims.py` finds each claim in the new file in two ways that do not depend on each other:

1. **Cite map.** It splits the old file and the new file into syllables and aligns them. Then it
   follows the claim's old block (`^0-12`) to the new block that holds the same syllables.
2. **Quote.** It searches the new file for the claim's verbatim `བོད་ཡིག` quote.

Then it compares the two results.

| Verdict | Meaning | New address taken from |
|---|---|---|
| `confirmed` | The quote is in the new file exactly, and it is in the block that the cite map gives | either (they agree) |
| `confirmed-fuzzy` | The quote matches at 60% or more because the proofreading changed some spellings, and it agrees with the cite map | either |
| `quote-wins` | The quote is in the new file exactly, but not in the block that the cite map gives | quote |
| `absent-from-edition` | The old block's text is not in the library edition | — |

There are two reasons for `quote-wins`. Both are correct behaviour:

- **Tenga Tulku.** The old file included the root verse by transclusion. The new file writes the
  verse inline as its own segment, so the claim's quote is now one block earlier than the
  "ཞེས་པ་སྟེ།" block that the old cite pointed to.
- **Tāranātha.** The old machine TOC had headings such as "གཉིས་པ་ཕྱག་འཚལ་…". The human TOC
  changed these to body text in the homage segment.

## Results (8 commentaries that are in the library)

| Commentary | Claims | Syllables aligned | confirmed | confirmed-fuzzy | quote-wins | cite-only | absent |
|---|---:|---:|---:|---:|---:|---:|---:|
| karma-maitri | 163 | 95.3% | 151 | 12 | | | |
| taranatha | 368 | 97.1% | 293 | 55 | 20 | | |
| dharmabhadra | 148 | 98.3% | 140 | 8 | | | |
| pema-namgyal | 104 | 97.1% | 96 | 8 | | | |
| tenga-tulku | 157 | 93.1% | 100 | 15 | 22 | | 20 |
| gendun-drub | 136 | 98.7% | 124 | 11 | 1 | | |
| drakpa-gyaltsen | 142 | 97.0% | 59 | 82 | | 1 | |
| sangye-nyentrul | 125 | 95.7% | 104 | 21 | | | |
| **total** | **1,343** | | **1,067** | **212** | **43** | **1** | **20** |

The total includes the 5 tension entries (`⚑ **c-…**`) in gendun-drub. Each fragment of a quote
that has an ellipsis (`…`) is searched separately. A fuzzy match is tried first in the blocks
that the old cite maps to, and then in a wider part of the file.

The 20 `absent` claims are all of Tenga Tulku's back-matter (`c-z-1`–`c-z-20`, the list of the
twenty retinue deities). This list is not in the library edition. A person must decide one of these:

- add the list to the edition, or
- keep these claims without a library address.

For drakpa-gyaltsen, 82 matches are fuzzy. A spot check found the cause: the old text had page
numbers ("15", "20") inside the lines, and the proofreading removed them. The sampled matches
are the correct homage stanzas.

## Not covered yet: 8 commentaries, 1,637 claims

These commentaries have no resegmented or uploaded version yet:

| Commentary | Claims |
|---|---:|
| gendun-gyatso | 62 |
| konchok-thabkhe | 132 |
| lobsang-dawa | 87 |
| palden-sherab | 282 |
| sungrab-tulku | 160 |
| tenzin-dhonzang | 327 |
| tsultrim-namdak | 329 |
| yama-sonam | 258 |

When one of them is resegmented and uploaded, add a row for it to `NEW_FILES` in the script.
Then run the script again.

The two `bo-མཁན་པོ་ཚུལ་རྣམ།_*` files in `New raw data/` are different raw works. They have no
frontmatter, so the script does not use them.

## Library side

The `text_id` and `edition_id` values in each output file come from the new file's frontmatter.
All 8 are listed as commentaries of the root text `HyUbHGlzS9LsSrgiFQNYE`.

The library does not give a segment's own ID yet. On 2026-11-04, every content, segment and TOC
endpoint on library.webuddhist.com returned this error:

> Edition '…' requires the content-state migration

The deployed backend expects the `content_key`, `content_length` and `revision` fields on each
edition, and the migration that sets them has not been run. The migration is
`scripts/migrate.py` in the Webuddhist-library repo (dry run first, then `--apply`). After it is
run, each `reference` can be resolved to its segment ID with
`GET /v2/editions/{edition_id}/segmentation/segments`.

## Run

From the vault root:

```bash
python3 0-INBOX/claims-remap/remap_claims.py
```

To run one commentary only:

```bash
python3 0-INBOX/claims-remap/remap_claims.py dharmabhadra
```

The script writes `out/<registered_id>.json`, one row per claim, and `out/summary.json`.

To write the results into the claims files (a dry run unless you add `--write`; you can run it
again safely):

```bash
python3 0-INBOX/claims-remap/write_library_refs.py --write
```

Before and after the write, `tree-guided-claims/scripts/verify_claims.py` gives the same exit
code and the same findings. Only the line numbers change.
