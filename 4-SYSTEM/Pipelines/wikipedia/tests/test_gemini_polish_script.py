"""The `scripts/gemini_polish.py` entry point — the Gemini leg of the canonical pipeline.

`kwiki polish` and this script are two doors onto one `run_polish`, and the script is what
`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/11-polish/SKILL.md` declares. What is tested here is the part
that is *only* in the script: argument handling, the missing-artifact guard, and the
`--dry-run` path that renders the real handoff prompt without calling a model. The polish
behaviour itself (structure enforcement, re-rendering) is covered in `test_pipeline_e2e.py`.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "gemini_polish.py"


def _load_script():
    spec = importlib.util.spec_from_file_location("gemini_polish", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def corpus(tmp_path: Path, monkeypatch) -> Path:
    """A minimal corpus with the three artifacts the polish stage reads."""
    monkeypatch.setenv("KWIKI_CORPORA_DIR", str(tmp_path))
    monkeypatch.setenv("KWIKI_PROMPTS_DIR", str(REPO / "prompts"))
    monkeypatch.setenv("GEMINI_API_KEY", "test-key-not-used")

    art = tmp_path / "smoke" / "articles" / "X"
    art.mkdir(parents=True)
    (art / "draft.json").write_text(
        json.dumps(
            {
                "lead": [{"text": "ཚིག་དང་པོ།", "citations": [0]}],
                "sections": [{"heading": "མཚན་ཉིད།", "paragraphs": [
                    {"text": "གཉིས་པ།", "citations": [0]}]}],
                "see_also": [],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (art / "claims.json").write_text(
        json.dumps(
            {"term": "X", "claims": [{"id": "C1", "claim_bo": "དོན།",
                                      "passage_indices": [0], "claim_type": "consensus"}]},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (art / "extract.json").write_text(
        json.dumps({"term": "X", "passages": [{"source_id": "S", "quote": "ལུང་།"}]},
                   ensure_ascii=False),
        encoding="utf-8",
    )
    (tmp_path / "smoke" / "sources.yaml").write_text(
        "corpus_id: smoke\nsources:\n- source_id: S\n  title: T\n", encoding="utf-8"
    )
    return tmp_path


def test_missing_artifacts_exit_nonzero_without_calling_a_model(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("KWIKI_CORPORA_DIR", str(tmp_path))
    monkeypatch.setenv("KWIKI_PROMPTS_DIR", str(REPO / "prompts"))
    (tmp_path / "smoke" / "articles" / "X").mkdir(parents=True)

    assert _load_script().main(["smoke", "X"]) == 2
    assert "run the earlier stages first" in capsys.readouterr().err


def test_dry_run_renders_the_real_handoff_prompt_and_calls_nothing(corpus, capsys):
    assert _load_script().main(["smoke", "X", "--dry-run"]) == 0

    rendered = capsys.readouterr().out
    # The four hard constraints of the canonical handoff must reach the model.
    assert "[Cnn]" in rendered or "citations" in rendered
    assert "stylist, not an editor" in rendered
    assert "ཚིག་དང་པོ།" in rendered  # the draft itself was interpolated
    assert "$draft_json" not in rendered and "$glossary" not in rendered

    # Nothing was written: a dry run inspects, it does not advance the pipeline.
    art = corpus / "smoke" / "articles" / "X"
    assert not (art / "draft_polished.json").exists()
    assert not (art / "model.json").exists()
