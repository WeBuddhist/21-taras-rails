"""Kangyur → Tibetan Wikipedia pipeline.

Deliberately empty of imports.  Every stage of this pipeline has a different
dependency footprint (botok, google-genai, requests), and a stage must be
importable — and testable offline — without dragging in the others.  Import
``kangyur_wiki.wiki.client`` and friends directly.

``__version__`` is the single source of the version reported in the Wikimedia
User-Agent header (``kangyur_wiki.wiki.client.build_user_agent``).  WMF policy
requires a real client name and version there, so this string is operational,
not decorative.
"""

__version__ = "0.1"

__all__ = ["__version__"]
