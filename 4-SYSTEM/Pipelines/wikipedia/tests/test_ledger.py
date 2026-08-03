"""Offline tests for the resumability ledger.

Timestamps are supplied by every test, never read from the clock — the same
property the production code depends on, exercised the same way.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from kangyur_wiki.ledger import (
    LEDGER_FILENAME,
    Ledger,
    LedgerEntry,
    TermStatus,
    atomic_write_text,
    ledger_path,
)

T0 = "2026-07-29T10:00:00+00:00"
T1 = "2026-07-29T11:30:00+00:00"

BDE = "བདེ་གཤེགས་"
SRAS = "སྲས་"


@pytest.fixture()
def ledger() -> Ledger:
    ledger = Ledger(corpus_id="spyodjug")
    ledger.seed([BDE, SRAS, "ཆོས་ཀྱི་སྐུ་"], updated_at=T0)
    return ledger


# --------------------------------------------------------------------------
# TermStatus
# --------------------------------------------------------------------------


def test_status_parse_accepts_value_name_and_member():
    assert TermStatus.parse("published") is TermStatus.PUBLISHED
    assert TermStatus.parse("PUBLISHED") is TermStatus.PUBLISHED
    assert TermStatus.parse(TermStatus.PUBLISHED) is TermStatus.PUBLISHED


def test_status_parse_rejects_nonsense():
    with pytest.raises(ValueError, match="unknown term status"):
        TermStatus.parse("nearly-done")


def test_status_declaration_order_is_pipeline_order():
    assert [status.value for status in TermStatus][:6] == [
        "pending",
        "extracted",
        "claimed",
        "organized",
        "drafted",
        "audited",
    ]


# --------------------------------------------------------------------------
# Entries
# --------------------------------------------------------------------------


def test_entry_normalises_its_term_and_status():
    entry = LedgerEntry(term=f"  {BDE} ", status="drafted", updated_at=T0)
    assert entry.term == BDE
    assert entry.status is TermStatus.DRAFTED


def test_entry_omits_empty_optionals_from_its_dict():
    entry = LedgerEntry(term=BDE, status=TermStatus.PENDING, updated_at=T0)
    assert entry.to_dict() == {"term": BDE, "status": "pending", "updated_at": T0}


def test_entry_round_trips_every_field():
    entry = LedgerEntry(
        term=BDE,
        status=TermStatus.PUBLISHED,
        updated_at=T1,
        error=None,
        artifacts={"draft": "articles/bde/draft.md"},
        wiki_title="བདེ་གཤེགས།",
        wiki_revid=98765,
        metrics={"tokens": 41230, "cost_usd": 0.0182, "review_seconds": 260},
    )
    assert LedgerEntry.from_dict(entry.to_dict()) == entry


def test_entry_from_dict_drops_unknown_keys():
    entry = LedgerEntry.from_dict(
        {"term": BDE, "status": "verified", "updated_at": T0, "reviewer_note": "looks fine"}
    )
    assert entry.status is TermStatus.VERIFIED


def test_entry_from_dict_needs_a_term():
    with pytest.raises(ValueError, match="no term"):
        LedgerEntry.from_dict({"status": "pending", "updated_at": T0})


# --------------------------------------------------------------------------
# Queries
# --------------------------------------------------------------------------


def test_seed_is_idempotent(ledger):
    added = ledger.seed([BDE, "ཕྱག་འོས་"], updated_at=T1)
    assert [entry.term for entry in added] == ["ཕྱག་འོས་"]
    assert ledger.get(BDE).updated_at == T0  # untouched


def test_get_matches_on_nfc_and_trimmed_whitespace(ledger):
    assert ledger.get(f"  {BDE}  ") is not None


def test_get_does_not_guess_about_tibetan_punctuation(ledger):
    """Term identity belongs to the registry — see the module docstring."""
    assert ledger.get("བདེ་གཤེགས།") is None


def test_entries_by_status(ledger):
    ledger.set_status(BDE, TermStatus.DRAFTED, T1)
    assert [entry.term for entry in ledger.entries_by_status(TermStatus.PENDING)] == [
        SRAS,
        "ཆོས་ཀྱི་སྐུ་",
    ]
    assert [entry.term for entry in ledger.entries_by_status("drafted")] == [BDE]


def test_summary_reports_every_status_even_at_zero(ledger):
    ledger.set_status(BDE, TermStatus.PUBLISHED, T1)
    summary = ledger.summary()
    assert summary["pending"] == 2
    assert summary["published"] == 1
    assert summary["failed"] == 0
    assert summary["total"] == 3
    assert list(summary) == [status.value for status in TermStatus] + ["total"]


# --------------------------------------------------------------------------
# Mutation
# --------------------------------------------------------------------------


def test_set_status_creates_a_missing_entry():
    ledger = Ledger(corpus_id="c")
    entry = ledger.set_status(BDE, TermStatus.EXTRACTED, T0)
    assert ledger.get(BDE) is entry
    assert entry.updated_at == T0


def test_set_status_merges_artifacts_and_metrics(ledger):
    ledger.set_status(
        BDE, TermStatus.EXTRACTED, T0, artifacts={"extract": "work/extracts/bde.json"},
        metrics={"tokens": 1000, "cost_usd": 0.01},
    )
    ledger.set_status(
        BDE, TermStatus.DRAFTED, T1, artifacts={"draft": "articles/bde/draft.md"},
        metrics={"review_seconds": 120},
    )
    entry = ledger.get(BDE)
    assert entry.artifacts == {
        "extract": "work/extracts/bde.json",
        "draft": "articles/bde/draft.md",
    }
    assert entry.metrics == {"tokens": 1000, "cost_usd": 0.01, "review_seconds": 120}
    assert entry.status is TermStatus.DRAFTED
    assert entry.updated_at == T1


def test_a_successful_retry_clears_the_previous_error(ledger):
    ledger.set_status(BDE, TermStatus.FAILED, T0, error="quote not verbatim in source")
    assert ledger.get(BDE).error
    ledger.set_status(BDE, TermStatus.VERIFIED, T1)
    assert ledger.get(BDE).error is None


def test_upsert_replaces_wholesale(ledger):
    ledger.upsert(LedgerEntry(term=BDE, status=TermStatus.APPROVED, updated_at=T1))
    assert ledger.get(BDE).status is TermStatus.APPROVED
    assert len(ledger.entries) == 3


def test_wiki_fields_are_recorded(ledger):
    ledger.set_status(
        BDE, TermStatus.PUBLISHED, T1, wiki_title="བདེ་གཤེགས།", wiki_revid=12345
    )
    entry = ledger.get(BDE)
    assert (entry.wiki_title, entry.wiki_revid) == ("བདེ་གཤེགས།", 12345)


# --------------------------------------------------------------------------
# Persistence
# --------------------------------------------------------------------------


def test_ledger_path():
    assert ledger_path("/corp", "spyodjug") == Path("/corp/spyodjug") / LEDGER_FILENAME


def test_load_of_a_missing_file_is_an_empty_ledger(tmp_path):
    """A first run has no ledger; that is not an error."""
    ledger = Ledger.load(tmp_path / "spyodjug" / "ledger.json")
    assert ledger.entries == {}
    assert ledger.path == tmp_path / "spyodjug" / "ledger.json"


def test_load_labels_a_fresh_ledger_with_the_given_corpus_id(tmp_path):
    ledger = Ledger.load(tmp_path / "ledger.json", corpus_id="spyodjug")
    ledger.seed([BDE], updated_at=T0)
    ledger.save()
    assert Ledger.load(tmp_path / "ledger.json").corpus_id == "spyodjug"


def test_load_never_overwrites_the_corpus_id_a_file_already_carries(tmp_path):
    Ledger(corpus_id="spyodjug").save(tmp_path / "ledger.json")
    assert Ledger.load(tmp_path / "ledger.json", corpus_id="typo").corpus_id == "spyodjug"


def test_save_then_load_round_trips(tmp_path, ledger):
    ledger.set_status(
        BDE, TermStatus.PUBLISHED, T1, wiki_title="བདེ་གཤེགས།", wiki_revid=7,
        artifacts={"article": "articles/bde/article.wiki"}, metrics={"cost_usd": 0.02},
    )
    target = ledger_path(tmp_path, "spyodjug")
    written = ledger.save(target)
    assert written == target

    restored = Ledger.load(target)
    assert restored.corpus_id == "spyodjug"
    assert restored.summary() == ledger.summary()
    assert restored.get(BDE) == ledger.get(BDE)


def test_save_remembers_its_path(tmp_path, ledger):
    ledger.save(tmp_path / "ledger.json")
    ledger.set_status(BDE, TermStatus.DRAFTED, T1)
    ledger.save()  # no argument
    assert Ledger.load(tmp_path / "ledger.json").get(BDE).status is TermStatus.DRAFTED


def test_save_without_any_path_is_an_error(ledger):
    with pytest.raises(ValueError, match="needs a path"):
        ledger.save()


def test_saved_file_is_readable_json_with_tibetan_intact(tmp_path, ledger):
    path = ledger.save(tmp_path / "ledger.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["version"] == 1
    assert payload["entries"][0]["term"] == BDE
    assert BDE in path.read_text(encoding="utf-8")  # not \\u escapes


def test_save_creates_the_corpus_directory(tmp_path, ledger):
    ledger.save(tmp_path / "deep" / "nested" / "ledger.json")
    assert (tmp_path / "deep" / "nested" / "ledger.json").exists()


# --------------------------------------------------------------------------
# Atomic write
# --------------------------------------------------------------------------


def test_atomic_write_replaces_the_whole_file(tmp_path):
    target = tmp_path / "f.txt"
    atomic_write_text(target, "old")
    atomic_write_text(target, "new")
    assert target.read_text(encoding="utf-8") == "new"


def test_atomic_write_gives_a_new_file_a_readable_mode(tmp_path):
    """``mkstemp`` creates at 0600; a committed corpus file must not inherit it."""
    target = tmp_path / "f.txt"
    atomic_write_text(target, "x")
    assert target.stat().st_mode & 0o777 == 0o644


def test_atomic_write_preserves_an_existing_mode(tmp_path):
    target = tmp_path / "f.txt"
    atomic_write_text(target, "x")
    target.chmod(0o600)
    atomic_write_text(target, "y")
    assert target.stat().st_mode & 0o777 == 0o600


def test_atomic_write_leaves_no_temp_files_behind(tmp_path, ledger):
    ledger.save(tmp_path / "ledger.json")
    ledger.save(tmp_path / "ledger.json")
    assert [p.name for p in tmp_path.iterdir()] == ["ledger.json"]


def test_a_failed_write_neither_clobbers_nor_litters(tmp_path, monkeypatch):
    """The whole point: an interrupted run must leave the old ledger intact."""
    target = tmp_path / "ledger.json"
    atomic_write_text(target, "original")

    def explode(src, dst):
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", explode)
    with pytest.raises(OSError):
        atomic_write_text(target, "replacement")

    assert target.read_text(encoding="utf-8") == "original"
    assert [p.name for p in tmp_path.iterdir()] == ["ledger.json"]
