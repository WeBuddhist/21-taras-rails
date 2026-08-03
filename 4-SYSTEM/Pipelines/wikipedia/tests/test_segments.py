"""Segment-level provenance: which commentary block a citation came from.

An aligned span runs from one verse anchor to the next and is routinely
thousands of characters. Citing it names a book, not a passage. These tests pin
the narrowing — span → the blocks inside it that mention the term — and the
locator that narrowing produces.
"""

from __future__ import annotations

import pytest

from kangyur_wiki.stages.align import (
    AlignedSpan,
    AlignmentReport,
    segments_for_term,
    spans_for_term,
)
from kangyur_wiki.stages.pipeline import build_extract_context
from kangyur_wiki.wiki.wikitext import Citation

TERM = "སྒྲོལ་མ།"

BLOCK_HIT = "སྒྲོལ་མ་ནི་འཁོར་བའི་སྡུག་བསྔལ་ལས་སྒྲོལ་བར་མཛད་པས་ན་སྒྲོལ་མའོ།། ^1-1-1"
BLOCK_MISS = "འོད་ཟེར་གྱི་སྒོ་ནས་བསྟོད་པའོ།། ^1-1-2"
BLOCK_HIT_2 = "སྒྲོལ་མ་ལ་རིགས་ཉེར་གཅིག་ཡོད་དོ།། ^1-1-3"

COMMENTARY = (
    "---\nbook_id: TARAC02_DGT\n---\n"
    "## བསྟོད་པ་དངོས་ ^1-0\n"
    "### མཚན་གྱི་སྒོ་ནས་ ^1-1-0\n"
    "\n"
    "![[root#^1-1]]\n"
    f"{BLOCK_HIT}\n"
    "\n"
    f"{BLOCK_MISS}\n"
    "\n"
    f"{BLOCK_HIT_2}\n"
)


def _report():
    lines = COMMENTARY.splitlines()
    return AlignmentReport(
        corpus="tara21",
        total_verses=1,
        spans=[
            AlignedSpan(
                verse_id="1-1",
                source_id="TARAC02_DGT",
                start_line=6,
                end_line=len(lines),
                text="\n".join(lines[5:]),
                method="transclusion",
                confidence=1.0,
            )
        ],
    )


def _loader(source_id: str) -> str:
    assert source_id == "TARAC02_DGT"
    return COMMENTARY


def test_the_span_alone_is_one_undifferentiated_chunk():
    """What the pipeline sent before: everything from the anchor onward."""
    spans = spans_for_term(_report(), TERM)
    assert len(spans) == 1
    assert BLOCK_MISS.split(" ^")[0] in spans[0].text


def test_segments_narrow_a_span_to_the_blocks_that_mention_the_term():
    segments = segments_for_term(_report(), TERM, _loader)
    assert [s.block_id for s in segments] == ["1-1-1", "1-1-3"]
    assert all(TERM.rstrip("།") in s.text for s in segments)


def test_each_segment_keeps_the_root_verse_its_span_was_anchored_to():
    segments = segments_for_term(_report(), TERM, _loader)
    assert {s.verse_id for s in segments} == {"1-1"}


def test_a_segment_locator_names_the_source_and_the_block():
    segments = segments_for_term(_report(), TERM, _loader)
    assert segments[0].locator == "TARAC02_DGT#^1-1-1"


def test_headings_are_never_returned_as_segments():
    """A heading title is text the pipeline wrote; it is not citable material."""
    segments = segments_for_term(_report(), "བསྟོད་པ་དངོས་", _loader)
    assert all("##" not in s.text for s in segments)


def test_without_a_loader_it_degrades_to_whole_spans():
    """A corpus that has not been through stage 1b must still produce material,
    not an empty extract."""
    segments = segments_for_term(_report(), TERM, None)
    assert len(segments) == 1
    assert segments[0].block_id == ""
    assert segments[0].locator == "TARAC02_DGT"


def test_an_unreadable_source_falls_back_to_the_span_rather_than_vanishing():
    def broken(_source_id: str) -> str:
        raise FileNotFoundError("gone")

    segments = segments_for_term(_report(), TERM, broken)
    assert len(segments) == 1
    assert segments[0].block_id == ""


def test_a_term_absent_everywhere_yields_nothing():
    assert segments_for_term(_report(), "ཨ་མ་བྱམས་མ།", _loader) == []


# -- what the model is shown -----------------------------------------------


def test_the_context_header_carries_the_block_id_not_the_verse_id():
    context = build_extract_context(segments_for_term(_report(), TERM, _loader))
    assert "segment_id: 1-1-1" in context
    assert "root_verse: 1-1" in context


def test_the_context_falls_back_to_the_verse_id_without_block_ids():
    context = build_extract_context(segments_for_term(_report(), TERM, None))
    assert "segment_id: 1-1" in context


def test_the_context_is_bounded():
    segments = segments_for_term(_report(), TERM, _loader)
    assert build_extract_context(segments, max_chars=10) == ""


# -- what ends up on the citation ------------------------------------------


def test_a_citation_locator_degrades_cleanly_when_no_block_is_known():
    assert Citation(source_id="TARAC02_DGT").locator == "TARAC02_DGT"
    assert (
        Citation(source_id="TARAC02_DGT", segment_id="1-1-1").locator
        == "TARAC02_DGT#^1-1-1"
    )


def test_segment_id_is_not_rendered_into_the_ref():
    """The ref format is fixed by the wikitext spec; an Obsidian block ID means
    nothing to a Wikipedia reader and must not leak into the article."""
    from kangyur_wiki.wiki.wikitext import render_ref

    ref = render_ref(
        Citation(
            source_id="TARAC02_DGT",
            author="གྲགས་པ་རྒྱལ་མཚན",
            title="གསལ་བའི་འོད་ཟེར།",
            segment_id="1-1-1",
        )
    )
    assert "1-1-1" not in ref
