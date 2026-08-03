"""Stage 1b — block parsing, block-ID stamping, and the reading view.

The property everything here rests on: the pipeline may add scaffolding to a
commentary and must never add, remove or alter a character of what the
commentary says. Each of these tests is a way for that to go wrong.
"""

from __future__ import annotations

import pytest

from kangyur_wiki.stages.commentary import (
    INTRO_PREFIX,
    Block,
    parse_blocks,
    reading_view,
    sanitise_sections,
    number_lines,
    split_front_matter,
    stamp_block_ids,
)
from kangyur_wiki.tibetan.normalize import collapse

FRONT = "---\nbook_id: TARAC02_DGT\nauthor: གྲགས་པ་རྒྱལ་མཚན\n---\n"

PLAIN = FRONT + (
    "༄༅།།ན་མོ་བུདྡྷ་ཡ།\n"
    "\n"
    "བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ།\n"
    "\n"
    "དང་པོ་ལ་གསུམ་སྟེ།\n"
)

TAGGED = FRONT + (
    "༄༅།།ན་མོ་བུདྡྷ་ཡ།\n"
    "\n"
    "## བསྟོད་པ་དངོས་ ^1-0\n"
    "### སྐུའི་རྣམ་པ་ ^1-1-0\n"
    "\n"
    "![[root#^1-1]]\n"
    "ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ།། ཞེས་པ་ནི།\n"
    "\n"
    "[[#^1-1-0|དང་པོ་]]ནི་འཁོར་བ་ལས་སྒྲོལ་བའོ།།\n"
    "\n"
    "## ཕན་ཡོན་ ^2-0\n"
    "\n"
    "ཕན་ཡོན་བཤད་པའོ།།\n"
)


# -- front matter ----------------------------------------------------------


def test_front_matter_is_split_off_whole():
    front, body = split_front_matter(PLAIN)
    assert front == FRONT
    assert body.startswith("༄༅།།ན་མོ")


def test_a_file_without_front_matter_is_all_body():
    front, body = split_front_matter("ཕྱག་འཚལ།\n")
    assert front == ""
    assert body == "ཕྱག་འཚལ།\n"


# -- block parsing ---------------------------------------------------------


def test_blocks_report_the_line_range_they_actually_occupy():
    lines = TAGGED.splitlines()
    for block in parse_blocks(TAGGED):
        assert lines[block.start_line - 1] == block.lines[0]
        assert lines[block.end_line - 1] == block.lines[-1]


def test_a_heading_is_its_own_block_and_does_not_swallow_what_follows():
    """The transclusion spacing convention glues a heading to the stanza below
    it with no blank line. That stanza is content and needs its own ID."""
    blocks = parse_blocks(TAGGED)
    kinds = [(b.kind, b.block_id) for b in blocks]
    assert ("heading", "1-0") in kinds
    assert ("heading", "1-1-0") in kinds
    # The anchor + stanza that sit directly under ^1-1-0 are a separate block.
    stanza = next(b for b in blocks if b.transclusions == ["1-1"])
    assert stanza.kind == "content"
    assert "ཕྱག་འཚལ་སྒྲོལ་མ" in stanza.text


def test_a_transclusion_only_block_carries_no_id():
    text = FRONT + "## ཕན་ཡོན་ ^2-0\n\n![[root#^1-1]]\n"
    stamped, report = stamp_block_ids(text)
    assert "![[root#^1-1]] ^" not in stamped
    assert report.stamped == 0


# -- block IDs -------------------------------------------------------------


def test_ids_are_derived_from_the_heading_above():
    stamped, _ = stamp_block_ids(TAGGED)
    assert "ཞེས་པ་ནི། ^1-1-1" in stamped
    assert "འཁོར་བ་ལས་སྒྲོལ་བའོ།། ^1-1-2" in stamped
    assert "ཕན་ཡོན་བཤད་པའོ།། ^2-1" in stamped


def test_content_before_the_first_heading_goes_to_the_intro_slot():
    stamped, report = stamp_block_ids(PLAIN)
    assert f"^{INTRO_PREFIX}-1" in stamped
    assert f"^{INTRO_PREFIX}-3" in stamped
    assert report.intro_blocks == 3


def test_stamping_is_idempotent():
    once, _ = stamp_block_ids(TAGGED)
    twice, report = stamp_block_ids(once)
    assert twice == once
    assert report.stamped == 0


def test_a_second_pass_does_not_reuse_an_id_already_handed_out():
    once, _ = stamp_block_ids(PLAIN)
    grown = once.rstrip("\n") + "\n\nགསུམ་པ་ནི།\n"
    twice, _ = stamp_block_ids(grown)
    ids = [line.rsplit("^", 1)[1] for line in twice.splitlines() if " ^" in line]
    assert len(ids) == len(set(ids)), ids
    assert f"{INTRO_PREFIX}-4" in ids


def test_headings_never_receive_an_id_here():
    """Heading IDs come from tag_inline_toc, derived from sa-bcad depth."""
    text = FRONT + "## ཕན་ཡོན།\n\nཕན་ཡོན་བཤད་པའོ།།\n"
    stamped, report = stamp_block_ids(text)
    assert "## ཕན་ཡོན།\n" in stamped
    assert report.untagged_headings == ["ཕན་ཡོན།"]


# -- the reading view ------------------------------------------------------


def test_stamping_changes_nothing_a_reader_would_see():
    stamped, _ = stamp_block_ids(TAGGED)
    assert reading_view(stamped) == reading_view(TAGGED)


def test_the_reading_view_strips_every_layer_of_scaffolding():
    view = reading_view(stamp_block_ids(TAGGED)[0])
    assert "^1-1-0" not in view
    assert "![[" not in view
    assert "[[" not in view
    assert "##" not in view
    # …and keeps the display text of a wikilinked sa-bcad term.
    assert "དང་པོ་ནི་འཁོར་བ་ལས་སྒྲོལ་བའོ།།" in view


def test_an_inserted_heading_is_removed_but_a_source_heading_is_kept():
    """A heading title the model wrote must not be quotable as the commentary's
    words; a heading that came in with the file is the commentary's own text."""
    text = FRONT + "# ༄༅། །རང་གི་མགོ་བྱང་།\n\n## མོདེལ་གྱིས་བྲིས་པ་ ^1-0\n\nནང་དོན།\n"
    view = reading_view(text)
    assert "རང་གི་མགོ་བྱང་།" in view
    assert "མོདེལ་གྱིས་བྲིས་པ་" not in view


def test_line_numbers_are_preserved_so_offsets_still_land():
    stamped, _ = stamp_block_ids(TAGGED)
    assert len(reading_view(stamped).splitlines()) == len(stamped.splitlines())


# -- the numbered listing the model reads ----------------------------------


def test_numbering_counts_from_the_top_of_the_file_and_skips_blanks():
    listing = number_lines(TAGGED)
    numbers = [int(line.split("\t", 1)[0]) for line in listing.splitlines()]
    lines = TAGGED.splitlines()
    for n in numbers:
        assert lines[n - 1].strip(), f"line {n} is blank"
    assert numbers == sorted(numbers)


# -- the annotation sanitiser ----------------------------------------------


def _sections(*specs):
    return [
        {"body_start_line": ln, "depth": d, "heading_title": t} for ln, d, t in specs
    ]


def test_a_line_outside_the_file_is_dropped():
    kept, notes = sanitise_sections(_sections((9999, 1, "ཕན་ཡོན།")), TAGGED)
    assert kept == []
    assert "outside the file" in notes[0]


def test_a_blank_line_anchor_is_dropped():
    blank = next(i for i, l in enumerate(TAGGED.splitlines(), 1) if not l.strip())
    kept, notes = sanitise_sections(_sections((blank, 1, "ཕན་ཡོན།")), TAGGED)
    assert kept == []
    assert "blank line" in notes[0]


def test_a_backwards_line_is_dropped_but_a_repeat_that_nests_is_kept():
    body = next(i for i, l in enumerate(TAGGED.splitlines(), 1) if "ཕྱག་འཚལ" in l)
    kept, _ = sanitise_sections(
        _sections((body, 1, "ཕ།"), (body, 2, "བུ།"), (body - 1, 1, "རྒྱབ།")), TAGGED
    )
    assert [s["heading_title"] for s in kept] == ["ཕ།", "བུ།"]


def test_a_skipped_depth_is_pulled_back_rather_than_dropped():
    body = next(i for i, l in enumerate(TAGGED.splitlines(), 1) if "ཕྱག་འཚལ" in l)
    kept, notes = sanitise_sections(_sections((body, 4, "ཕན་ཡོན།")), TAGGED)
    assert kept[0]["depth"] == 1
    assert "skips a level" in notes[0]


def test_the_verbatim_context_is_copied_from_the_file_not_the_model():
    body = next(i for i, l in enumerate(TAGGED.splitlines(), 1) if "ཕྱག་འཚལ" in l)
    kept, _ = sanitise_sections(_sections((body, 1, "ཕན་ཡོན།")), TAGGED)
    assert kept[0]["body_start_context"] == TAGGED.splitlines()[body - 1].strip()


# -- the property, over the real corpus ------------------------------------


def test_no_loss_over_every_shape_at_once():
    """Refine, headings, anchors and IDs together: still the same Tibetan."""
    stamped, _ = stamp_block_ids(TAGGED)
    assert collapse(reading_view(stamped)) == collapse(reading_view(TAGGED))


# -- the gate must read through the scaffolding ----------------------------
#
# The failure this guards against is nasty because it looks like the opposite of
# what it is: once a commentary carries block IDs, a perfectly faithful quotation
# spanning a block boundary fails verification on a caret the pipeline itself
# wrote — and that is indistinguishable, in the report, from a hallucinating
# model.


SPANNING_QUOTE = "བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ།\nདང་པོ་ལ་གསུམ་སྟེ།"


def test_a_quote_spanning_two_blocks_survives_stamping():
    from kangyur_wiki.tibetan.verify import check_quote

    stamped, _ = stamp_block_ids(PLAIN)
    assert not check_quote(SPANNING_QUOTE, stamped).passed, "precondition: raw text has the IDs"
    assert check_quote(SPANNING_QUOTE, reading_view(stamped)).passed


def test_a_quote_of_a_wikilinked_sa_bcad_term_survives_tagging():
    from kangyur_wiki.tibetan.verify import check_quote

    quote = "དང་པོ་ནི་འཁོར་བ་ལས་སྒྲོལ་བའོ།།"
    assert check_quote(quote, TAGGED).method == "fuzzy"  # the [[…|…]] wrapper defeats it
    assert check_quote(quote, reading_view(TAGGED)).passed


def test_the_gate_still_bites_through_the_reading_view():
    """Stripping scaffolding must not become a way to launder a paraphrase."""
    from kangyur_wiki.tibetan.verify import check_quote

    stamped, _ = stamp_block_ids(TAGGED)
    paraphrase = "དང་པོ་ནི། འཁོར་བ་ལས་སྒྲོལ་བའོ།།"  # one tsheg promoted to a shad
    check = check_quote(paraphrase, reading_view(stamped))
    assert check.method == "fuzzy"
    assert not check.passed
