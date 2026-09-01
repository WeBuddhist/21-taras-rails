"""The two deterministic checkers behind method 3 (tree-guided claims extraction).

Both scripts live under `4-SYSTEM/Skills/`, not under this pipeline's own `scripts/` —
they are skill-owned tooling, loaded here the same way `test_gemini_polish_script.py`
loads a script by path rather than importing it as an installed module, since neither
is part of the `kangyur_wiki` package.

`qc_tree_vs_source.py` checks a TOC tree against the commentary it was built from
(pointer bounds, title attestation near the pointer, document-order monotonicity,
repeated-pointer collisions, sibling-count congruence). `verify_claims.py` checks a
`tree-guided-claims` output file against its source (quote containment, `claim_count`
recomputation, claim-ID well-formedness, `stated`-referent validity). Both were smoke-
tested by hand against real vault data (the three shipped TOC trees and the documented
fabricated-mantra defect from `_comparison-report.md`) before this suite was written;
what is tested here is the same behaviour, held fixed so it cannot regress silently.
"""

from __future__ import annotations

import importlib.util
import sys
import textwrap
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parents[3] / "Skills"
QC_TREE_SCRIPT = SKILLS_DIR / "toc-tree-extraction" / "scripts" / "qc_tree_vs_source.py"
VERIFY_CLAIMS_SCRIPT = SKILLS_DIR / "tree-guided-claims" / "scripts" / "verify_claims.py"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    # Both scripts define dataclasses at module scope; Python 3.14's dataclass
    # machinery looks the defining module up in sys.modules by name (for its
    # ClassVar/InitVar detection), which only works if the module is registered
    # there before exec_module runs.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# qc_tree_vs_source.py
# ---------------------------------------------------------------------------

qc_tree_vs_source = _load(QC_TREE_SCRIPT, "qc_tree_vs_source")

# A tiny commentary; full-file line numbers (frontmatter included, matching
# chunk_file.py's convention — see qc_tree_vs_source.py's module docstring).
# Line 4 announces a two-way division ("... ལ་གཉིས་སྟེ ...") into "བསྟན་པ" and
# "བཤད་པ"; line 7 announces a three-way division ("... ལ་གསུམ་སྟེ ...") that the
# CLEAN tree below gives three children, so both divisions are self-consistent.
_SOURCE = textwrap.dedent(
    """\
    ---
    title: test
    ---
    འདི་ལ་གཉིས་སྟེ། བསྟན་པ་དང་བཤད་པའོ།། ^I-1
    བསྟན་པ་ནི་འདི་ལྟར་རོ།། ^I-2
    དེ་ནས་བཤད་པ་ནི། ^I-3
    གསུམ་པ་ལ་གསུམ་སྟེ། དང་པོ་དང་གཉིས་པ་དང་གསུམ་པའོ།། ^I-4
    དང་པོ་ནི་འདི་ལྟར་རོ།། ^I-5
    གཉིས་པ་ནི་འདི་ལྟར་རོ།། ^I-6
    གསུམ་པ་ནི་འདི་ལྟར་རོ།། ^I-7
    """
)


def _clean_tree() -> str:
    # "བསྟན་པ" is on full-file line 4, "བཤད་པ" on line 6 (within the ±3 near-
    # window of both), "གསུམ་པ"'s division announcement on line 7. Node 2 gets
    # three children (2.1/2.2/2.3) matching that announced three-way division,
    # each at its own distinct line so no repeated-pointer collision fires.
    return textwrap.dedent(
        """\
        * 1. འདི་ [[4]]
           * 1.1 བསྟན་པ་ [[4]]
           * 1.2 བཤད་པ་ [[6]]
        * 2. གསུམ་པ་ [[7]]
           * 2.1 དང་པོ་ [[8]]
           * 2.2 གཉིས་པ་ [[9]]
           * 2.3 གསུམ་པ་ [[10]]
        """
    )


def test_clean_tree_has_no_hard_issues():
    hard, info = qc_tree_vs_source.qc_tree_vs_source(_clean_tree(), _SOURCE)
    assert hard == []


def test_unresolved_anchor_is_always_an_issue():
    tree = _clean_tree().replace("[[8]]", "[[?]]")
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(tree, _SOURCE)
    assert any("unresolved anchor" in x for x in hard)


def test_out_of_range_pointer_is_flagged():
    tree = _clean_tree().replace("[[7]]", "[[9999]]")
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(tree, _SOURCE)
    assert any("out of range" in x for x in hard)


def test_repeated_pointer_collision_flagged_at_three_or_more():
    # Three nodes sharing one pointer is the "lost cursor" signature; two sharing
    # one (a parent + its first child) is normal and must NOT be flagged.
    two_sharing = _clean_tree()  # "1" and "1.1" already share [[4]] — must be clean of collision noise
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(two_sharing, _SOURCE)
    assert not any("collision" in x for x in hard)

    three_sharing = _clean_tree().replace("[[6]]", "[[4]]")
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(three_sharing, _SOURCE)
    assert any("collision" in x and "[[4]]" in x for x in hard)


def test_monotonicity_violation_flagged():
    tree = textwrap.dedent(
        """\
        * 1. འདི་ [[4]]
        * 2. གསུམ་པ་ [[7]]
        * 3. དང་པོ་ [[4]]
        """
    )
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(tree, _SOURCE)
    assert any("runs backwards" in x for x in hard)


def test_title_not_in_source_is_flagged_as_possible_hallucination():
    tree = _clean_tree().replace("2.1 དང་པོ་", "2.1 མེད་པའི་ཚིག་")
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(tree, _SOURCE)
    assert any("not attested anywhere" in x for x in hard)


def test_bare_ordinal_titles_are_not_flagged_either_way():
    # "དང་པོ" (the first) is generic and appears constantly; the checker must not
    # penalise it for being unspecific, and must not silently count it as clean either.
    hard, info = qc_tree_vs_source.qc_tree_vs_source(_clean_tree(), _SOURCE)
    assert any("bare-ordinal-only" in x for x in info)


def test_sibling_count_mismatch_is_flagged():
    # Node "2" announces a three-way division at its own line but the tree gives
    # it only one child.
    tree = textwrap.dedent(
        """\
        * 1. འདི་ [[4]]
        * 2. གསུམ་པ་ [[7]]
           * 2.1 དང་པོ་ [[8]]
        """
    )
    hard, _ = qc_tree_vs_source.qc_tree_vs_source(tree, _SOURCE)
    assert any("division" in x and "1 child" in x for x in hard)


# ---------------------------------------------------------------------------
# verify_claims.py
# ---------------------------------------------------------------------------

verify_claims = _load(VERIFY_CLAIMS_SCRIPT, "verify_claims")

_CLAIMS_SOURCE = textwrap.dedent(
    """\
    ---
    title: test
    ---
    སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ།། ^I-1

    གཞན་ཡང་སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ།། ^I-2

    སྒྲོལ་མ་ནི་ཐུགས་རྗེ་ཆེའི་ཕྱིར་དང་། སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ།། ^I-3
    """
)


def _claims_file(*, claim_count=1, referent_basis="[unanchored]") -> str:
    return textwrap.dedent(
        f"""\
        ---
        registered_id: test
        source_file: source.md
        citation_form: block-id
        claim_count: {claim_count}
        status: draft
        ---

        ## 1. Test node

        ### c-1-1 a real claim
        **བོད་ཡིག:** སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ
        **English:** Tara liberates from suffering
        **Type:** doctrinal
        **Referent:** {referent_basis}
        **Cite:** (source.md#^I-1)
        """
    )


def test_clean_claims_file_has_no_hard_issues():
    hard, info = verify_claims.verify_claims(_claims_file(), _CLAIMS_SOURCE)
    assert hard == []
    assert any("of 3 source blocks" in x for x in info)


def test_fabricated_quote_is_caught():
    text = _claims_file().replace(
        "སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ", "སྒྲོལ་མ་ནི་ནམ་མཁའི་ལྷ་མོའོ"
    )
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert any("not found in block" in x for x in hard)


def test_ellipsis_fragments_checked_independently():
    # Block ^I-3 contains both phrases non-contiguously (connector text between
    # them): "སྒྲོལ་མ་ནི...ཐུགས་རྗེ་ཆེའི་ཕྱིར་དང་།...སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ".
    # Both halves real: legitimate.
    text = _claims_file().replace(
        "སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ",
        "སྒྲོལ་མ་ནི…སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ",
    ).replace("#^I-1)", "#^I-3)")
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert hard == []

    # One half fabricated: caught even though the other half is real and the
    # citation (^I-3) is otherwise correct.
    text_bad = _claims_file().replace(
        "སྒྲོལ་མ་ནི་སྡུག་བསྔལ་ལས་སྒྲོལ་བའོ",
        "སྒྲོལ་མ་ནི…མཁའ་འགྲོའི་གཙོ་མོའོ",
    ).replace("#^I-1)", "#^I-3)")
    hard, _ = verify_claims.verify_claims(text_bad, _CLAIMS_SOURCE)
    assert any("not found in block" in x for x in hard)


def test_claim_count_mismatch_is_caught():
    hard, _ = verify_claims.verify_claims(_claims_file(claim_count=2), _CLAIMS_SOURCE)
    assert any("claim_count declares 2 but 1" in x for x in hard)


def test_claim_count_correct_is_not_flagged():
    hard, _ = verify_claims.verify_claims(_claims_file(claim_count=1), _CLAIMS_SOURCE)
    assert not any("claim_count" in x for x in hard)


def test_duplicate_claim_id_is_caught():
    text = _claims_file() + textwrap.dedent(
        """
        ### c-1-1 a duplicate id
        **བོད་ཡིག:** གཞན་ཡང་སྙིང་རྗེ་ཆེན་པོའི་རྣམ་པར་གྱུར་པའོ
        **English:** and also compassionate
        **Type:** doctrinal
        **Referent:** [unanchored]
        **Cite:** (source.md#^I-2)
        """
    )
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert any("duplicates" in x for x in hard)


def test_malformed_claim_id_is_caught():
    text = _claims_file().replace("### c-1-1", "### c-oops")
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert any("does not match" in x for x in hard)


def test_stated_referent_must_occur_in_the_claims_own_quote():
    # The claim's own quotation never names "Tara" by the referent's Grounding-index
    # form, so tagging it (stated) is wrong even though the source elsewhere would
    # support it.
    text = _claims_file(referent_basis="FIG-1 (stated)")
    text = text.replace(
        "## 1. Test node",
        "## 1. Test node\n\n"
        "### Figures and forms (deities, aspects, emanations)\n"
        "| ID | Name (verbatim) | What the source says it is | Attested at |\n"
        "|---|---|---|---|\n"
        "| FIG-1 | མཁའ་འགྲོ་མ། | a dakini epithet never quoted in this claim | ^I-2 |",
    )
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert any("does not occur in this claim's own quoted Tibetan" in x for x in hard)


def test_stated_referent_present_in_quote_is_not_flagged():
    text = _claims_file(referent_basis="FIG-1 (stated)")
    text = text.replace(
        "## 1. Test node",
        "## 1. Test node\n\n"
        "### Figures and forms (deities, aspects, emanations)\n"
        "| ID | Name (verbatim) | What the source says it is | Attested at |\n"
        "|---|---|---|---|\n"
        "| FIG-1 | སྒྲོལ་མ | Tārā | ^I-1 |",
    )
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert not any("Referent" in x for x in hard)


def test_unanchored_referent_is_never_flagged():
    hard, _ = verify_claims.verify_claims(_claims_file(referent_basis="[unanchored]"), _CLAIMS_SOURCE)
    assert not any("Referent" in x for x in hard)


def test_citation_to_nonexistent_block_is_caught():
    text = _claims_file().replace("#^I-1)", "#^I-999)")
    hard, _ = verify_claims.verify_claims(text, _CLAIMS_SOURCE)
    assert any("does not exist in the source" in x for x in hard)
