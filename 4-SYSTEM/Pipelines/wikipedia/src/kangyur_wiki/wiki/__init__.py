"""bo.wikipedia access layer: the Action API client, and (later) the emitter,
validator and merge logic that sit on top of it.

Only the client is re-exported here.  Submodules are imported lazily by
callers rather than eagerly at package import, so importing
``kangyur_wiki.wiki`` never pulls in a dependency a given stage does not need.
"""

from kangyur_wiki.wiki.client import (
    DEFAULT_SITE,
    DOUBLE_SHAD,
    EDIT_INTERVAL_FLAGGED,
    EDIT_INTERVAL_FLAGGED_PEAK,
    EDIT_INTERVAL_UNFLAGGED,
    SHAD,
    TSHEG,
    USER_SANDBOX_PREFIX,
    EditConflict,
    NotAuthenticated,
    PageExists,
    PageInfo,
    Revision,
    SearchResult,
    Section,
    TitleResolution,
    WikiClient,
    WikiError,
    build_user_agent,
    sandbox_title,
    strip_terminal_punctuation,
    title_variants,
)

__all__ = [
    "DEFAULT_SITE",
    "DOUBLE_SHAD",
    "EDIT_INTERVAL_FLAGGED",
    "EDIT_INTERVAL_FLAGGED_PEAK",
    "EDIT_INTERVAL_UNFLAGGED",
    "SHAD",
    "TSHEG",
    "USER_SANDBOX_PREFIX",
    "EditConflict",
    "NotAuthenticated",
    "PageExists",
    "PageInfo",
    "Revision",
    "SearchResult",
    "Section",
    "TitleResolution",
    "WikiClient",
    "WikiError",
    "build_user_agent",
    "sandbox_title",
    "strip_terminal_punctuation",
    "title_variants",
]
