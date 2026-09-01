"""Tibetan text layer: normalisation, quotation verification, key-term stats.

``normalize`` and ``verify`` are re-exported here — pure stdlib, cheap to
import, and used by nearly every stage.

``keyness`` is deliberately **not** re-exported.  Importing it pulls in botok
when botok is installed, and only stage 3 needs word segmentation; a publish
run should not pay for a trie it will never touch.  Import it explicitly::

    from kangyur_wiki.tibetan import keyness
"""

from kangyur_wiki.tibetan.normalize import (
    DOUBLE_SHAD,
    FUZZY_DROP,
    SHAD,
    TSHEG,
    TSHEG_NB,
    collapse,
    collapse_with_map,
    fuzzy_key,
    fuzzy_key_with_map,
    nfc,
    strip_markup,
    syllables,
)
from kangyur_wiki.tibetan.verify import (
    METHOD_COLLAPSED,
    METHOD_EXACT,
    METHOD_FUZZY,
    METHOD_MISSING,
    MIN_FUZZY_KEY_LEN,
    PASSING_METHODS,
    SHORT_QUOTE_CHARS,
    QuoteCheck,
    SourceLoader,
    check_quote,
    check_quotes,
)

__all__ = [
    "DOUBLE_SHAD",
    "FUZZY_DROP",
    "SHAD",
    "TSHEG",
    "TSHEG_NB",
    "collapse",
    "collapse_with_map",
    "fuzzy_key",
    "fuzzy_key_with_map",
    "nfc",
    "strip_markup",
    "syllables",
    "METHOD_COLLAPSED",
    "METHOD_EXACT",
    "METHOD_FUZZY",
    "METHOD_MISSING",
    "MIN_FUZZY_KEY_LEN",
    "PASSING_METHODS",
    "SHORT_QUOTE_CHARS",
    "QuoteCheck",
    "SourceLoader",
    "check_quote",
    "check_quotes",
]
