# tara21 ingest report — local rebuild, 2026-08-02

This corpus tree was rebuilt on this machine from the raw team upload, after the
original cloud-session tree (described by earlier STATE.md sessions) turned out to
exist only on that environment's disk. The rebuild is the evidence that the ingest is
deterministic: local `kwiki verify` over the sandbox run's articles produced reports
**byte-identical** to the sandbox's own (see `REVIEW-2026-08-02.md`).

## Inputs

- `corpora/_raw_f/` — the renamed upload set (`f001..f021.txt`; `f011/f012/f013` are
  the duplicate editions the dkar-chag itself flags, deliberately unread;
  `f000.xlsx` not needed — the dkar-chag rows are encoded in the ingest script).
  The Tibetan-named originals are alongside in `corpora/སྒྲོལ་མ་ཉེར་གཅིག/`.
- `scripts/ingest_tara21.py` — the reproducible ingest (cleaning: NFC, U+0F0C→U+0F0B,
  page-number lines; root rebuilt from f003 cross-checked against f017; commentaries
  through the vendored preclean + structural segmentation, no-loss gated).
  Run locally via `scripts/ingest_tara21_local.py` (repoints the script's
  cloud-sandbox paths).

## Results

- `source/root.md` — 22 stanzas (21 homages `^1-1..^1-21` + closing couplet `^1-22`,
  plus `^I-1`).
- 16 commentaries → `source/commentaries/<SIGLUM>_bo_segmented.md`:

| siglum | chars | blocks |
|---|---|---|
| TARAC02_DGT | 12,205 | 233 |
| TARAC03_GDD | 17,060 | 130 |
| TARAC04_GDG | 10,250 | 68 |
| TARAC05_TRN | 30,575 | 275 |
| TARAC06_NDB | 15,775 | 146 |
| TARAC07_KTK | 22,426 | 196 |
| TARAC08_DTG | 24,996 | 207 |
| TARAC09_ANON | 44,919 | 516 |
| TARAC10_DPN | 17,469 | 101 |
| TARAC11_KMT | 7,918 | 59 |
| TARAC12_PDS | 75,648 | 328 |
| TARAC13_TDZ | 68,537 | 636 |
| TARAC14_LZD | 8,557 | 64 |
| TARAC15_SNT | 22,404 | 152 |
| TARAC16_PSR | 25,021 | 185 |
| TARAC17_TSN | 138,854 | 639 |

- `sources.yaml` — 17 sources (root + 16), sigla = file stems, dkar-chag metadata,
  Google Drive scan URLs only (hence W2 on every citation until public URLs land).

## After ingest (stage 1b + alignment, same day)

- `kwiki commentaries tara21 --skip-toc` — deterministic sub-steps only (stage-2
  refinement, 22 root-verse transclusion anchors per file, block IDs on every content
  block; **no sa-bcad headings** — the TOC sub-step needs live Gemini and was
  deliberately skipped to mirror the sandbox run's source state). 16/16 promoted;
  reading-view invariant held on every file (`work/ingest/COMMENTARY_REPORT.md`).
- `kwiki align tara21` — **314 spans: 209 transclusion + 105 cluster**, 7/16
  commentaries at 100% coverage, lowest 52.2% (the condensed/interlinear genres).
  `work/aligned.json`.

To re-run the sa-bcad heading pass later (restores session 3's 581-heading state):
`kwiki commentaries tara21` without `--skip-toc` (needs GEMINI_API_KEY), then re-align.
