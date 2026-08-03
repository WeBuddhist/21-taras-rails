#!/usr/bin/env python3
"""Run scripts/ingest_tara21.py against THIS repo's paths.

`ingest_tara21.py` was written in the 2026-08-01 cloud session with that sandbox's
paths hardcoded (RAW=/tmp/work/raw, REPO=/tmp/iats). Its logic is deterministic and
byte-reproducible; only the constants need repointing. This runner keeps the original
untouched (it is the provenance record of the cloud ingest) and rebinds its module
globals to the repo it lives in, with RAW = corpora/_raw_f — the renamed upload set.

Usage:
    ./.venv/bin/python scripts/ingest_tara21_local.py

Then complete the corpus (see corpora/tara21/INGEST_REPORT.md):
    kwiki commentaries tara21 --skip-toc    # deterministic; drop --skip-toc for headings
    kwiki align tara21
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "ingest_tara21", REPO / "scripts" / "ingest_tara21.py"
)
mod = importlib.util.module_from_spec(spec)
sys.modules["ingest_tara21"] = mod
spec.loader.exec_module(mod)

mod.RAW = REPO / "corpora" / "_raw_f"
mod.REPO = REPO
mod.CORPUS = REPO / "corpora" / "tara21"
mod.SRC = mod.CORPUS / "source"
mod.COMM = mod.SRC / "commentaries"
mod.WORK = mod.CORPUS / "work"
mod.SEG_SCRIPTS = REPO / "vendor" / "skills" / "commentary-segmentation" / "scripts"

if not mod.RAW.exists():
    sys.exit(f"raw upload set not found at {mod.RAW} — see corpora/tara21/INGEST_REPORT.md")

mod.main()
