"""A thin MediaWiki **Action API** client for bo.wikipedia.org.

Why the Action API and not the REST API: only ``action=edit`` offers
``createonly``, ``nocreate``, ``bot`` and ``minor``.  ``createonly=1`` is the
only real guard against creating a duplicate page at a Tibetan title variant,
which is the most likely way this pipeline damages the wiki
(``docs/reference/wikitext-spec.md`` §3).

Why not pywikibot: this module needs about six API calls, must import with no
config file, no credentials and no network, and must be testable entirely
offline.  pywikibot's family/config machinery buys none of that.

Why ``dry_run`` defaults to ``True``: every write method is a public,
irreversible act on a live encyclopedia with two administrators.  The default
has to be the safe one; ``--execute`` is the deliberate act (PLAN.md §3,
stage 8).
"""

from __future__ import annotations

import logging
import time
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Iterator, Mapping, Sequence

import requests

from kangyur_wiki import __version__ as _PIPELINE_VERSION

__all__ = [
    "TSHEG",
    "SHAD",
    "DOUBLE_SHAD",
    "DEFAULT_SITE",
    "USER_SANDBOX_PREFIX",
    "EDIT_INTERVAL_UNFLAGGED",
    "EDIT_INTERVAL_FLAGGED",
    "EDIT_INTERVAL_FLAGGED_PEAK",
    "WikiError",
    "EditConflict",
    "PageExists",
    "NotAuthenticated",
    "PageInfo",
    "TitleResolution",
    "Section",
    "Revision",
    "SearchResult",
    "WikiClient",
    "build_user_agent",
    "sandbox_title",
    "strip_terminal_punctuation",
    "title_variants",
]

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

#: Tibetan intersyllabic separator.  Never stripped from stored article text —
#: it is orthography, not whitespace.
TSHEG = "་"
#: Tibetan sentence terminator.
SHAD = "།"
#: Tibetan double shad (nyis shad).
DOUBLE_SHAD = "༎"

DEFAULT_SITE = "bo.wikipedia.org"

#: WMF User-Agent policy requires a client name, a version and *contact
#: information*; a browser UA or an empty one gets blocked without notice.
_UA_CLIENT = f"IATS-2026-Pipeline/{_PIPELINE_VERSION}"
_UA_CONTACT = "https://github.com/OpenPecha; openpecha@gmail.com"

#: Format string for the per-user staging namespace.  Human review happens in
#: userspace before anything reaches mainspace.
USER_SANDBOX_PREFIX = "User:{username}/sandbox"

#: meta:Bot policy edit throttle.  Unflagged bots must stay under one edit per
#: minute; this is 60x stricter than the technical rate limit, so it — not
#: ``maxlag`` — is the binding constraint on a run's wall-clock time.
EDIT_INTERVAL_UNFLAGGED = 60.0
EDIT_INTERVAL_FLAGGED = 5.0
EDIT_INTERVAL_FLAGGED_PEAK = 20.0

_DEFAULT_TIMEOUT = 30.0
_DEFAULT_MAXLAG = 5
_DEFAULT_MAX_RETRIES = 5

# API error codes that mean "the cluster is busy, come back later".
_RETRY_CODES = frozenset(
    {"maxlag", "ratelimited", "readonly", "internal_api_error_DBQueryError"}
)
# API error codes that mean "you are not who you think you are".
_AUTH_CODES = frozenset(
    {
        "assertuserfailed",
        "assertbotfailed",
        "assertnameduserfailed",
        "assertanonfailed",
        "notloggedin",
        "mustbeloggedin",
        "permissiondenied",
        "readapidenied",
        "writeapidenied",
        "badtoken",
    }
)
_CONFLICT_CODES = frozenset({"editconflict"})
_EXISTS_CODES = frozenset({"articleexists"})

_TRAILING_PUNCTUATION = (TSHEG, SHAD, DOUBLE_SHAD)


# --------------------------------------------------------------------------
# Exceptions
# --------------------------------------------------------------------------


class WikiError(RuntimeError):
    """Any failure reported by, or while talking to, the MediaWiki API."""

    def __init__(
        self,
        message: str,
        *,
        code: str | None = None,
        payload: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.payload = dict(payload) if payload else {}


class EditConflict(WikiError):
    """The page changed under us since ``basetimestamp``.

    Never retried automatically: the correct response is to re-fetch, re-merge
    and let a human look at the diff.
    """


class PageExists(WikiError):
    """``createonly=1`` refused because the title is already taken.

    Raised rather than swallowed, because it means the title-variant probe
    disagreed with the wiki and the caller must switch to the update path.
    """


class NotAuthenticated(WikiError):
    """No usable login for an operation that requires one."""


# --------------------------------------------------------------------------
# Value objects
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class PageInfo:
    """What ``prop=info`` knows about one title."""

    title: str
    exists: bool
    pageid: int | None = None
    ns: int | None = None
    is_redirect: bool = False
    redirect_target: str | None = None
    length: int | None = None
    lastrevid: int | None = None
    touched: str | None = None
    fullurl: str | None = None
    contentmodel: str | None = None
    invalid: bool = False
    invalid_reason: str | None = None

    @classmethod
    def from_api(cls, page: Mapping[str, Any]) -> "PageInfo":
        """Build from one ``query.pages`` entry.

        A rejected title comes back as ``invalid: true`` with **no** ``missing``
        key, so testing ``missing`` alone reports an unusable title as existing —
        and the publisher would then take the update path against a page that
        cannot be written at all.
        """
        invalid = bool(page.get("invalid", False))
        missing = bool(page.get("missing", False))
        return cls(
            title=page.get("title", ""),
            exists=not missing and not invalid,
            pageid=page.get("pageid"),
            ns=page.get("ns"),
            is_redirect=bool(page.get("redirect", False)),
            length=page.get("length"),
            lastrevid=page.get("lastrevid"),
            touched=page.get("touched"),
            fullurl=page.get("fullurl"),
            contentmodel=page.get("contentmodel"),
            invalid=invalid,
            invalid_reason=page.get("invalidreason"),
        )


@dataclass(frozen=True)
class TitleResolution:
    """The outcome of probing every orthographic variant of one term.

    ``page`` describes the matched variant itself; ``target_page`` describes
    where it lands if it is a redirect.  Both are kept because bo.wikipedia has
    live *broken* redirects (``སངས་རྒྱས`` points at a page that does not
    exist), and "the redirect exists" and "the target exists" are different
    facts with different consequences for the publisher.
    """

    requested: str
    variants: tuple[str, ...]
    matched_variant: str | None = None
    page: PageInfo | None = None
    target_page: PageInfo | None = None
    existing_variants: tuple[str, ...] = ()

    @property
    def exists(self) -> bool:
        return self.matched_variant is not None

    @property
    def is_redirect(self) -> bool:
        return bool(self.page and self.page.is_redirect)

    @property
    def redirect_target(self) -> str | None:
        return self.page.redirect_target if self.page else None

    @property
    def broken_redirect(self) -> bool:
        """A redirect whose target does not exist — a real state on bo.wiki."""
        if not self.is_redirect:
            return False
        return self.target_page is None or not self.target_page.exists

    @property
    def final_title(self) -> str | None:
        """The title a reader ends up at, or ``None`` when nothing exists."""
        if not self.exists:
            return None
        if self.is_redirect and self.target_page and self.target_page.exists:
            return self.target_page.title
        return self.matched_variant


@dataclass(frozen=True)
class Section:
    """One entry of ``action=parse&prop=sections``.

    ``index`` and ``anchor`` are the only safe handles: heading *lines* are
    Tibetan text that differs by a shad or a tsheg between two renderings of
    the same section, so string-matching them silently targets the wrong
    section.  ``index`` may be an empty string for a transcluded section, which
    is exactly the case where it must not be edited.
    """

    index: str
    line: str
    anchor: str
    level: int
    number: str = ""
    toclevel: int | None = None
    byteoffset: int | None = None
    fromtitle: str | None = None

    @property
    def editable(self) -> bool:
        """False for template-transcluded sections, which have no index."""
        return self.index.isdigit()

    @classmethod
    def from_api(cls, section: Mapping[str, Any]) -> "Section":
        return cls(
            index=str(section.get("index", "")),
            line=section.get("line", ""),
            anchor=section.get("anchor", ""),
            level=_as_int(section.get("level"), default=0),
            number=str(section.get("number", "")),
            toclevel=_as_int(section.get("toclevel"), default=None),
            byteoffset=section.get("byteoffset"),
            fromtitle=section.get("fromtitle"),
        )


@dataclass(frozen=True)
class Revision:
    """Content plus the baseline needed for edit-conflict detection."""

    title: str
    content: str
    timestamp: str
    revid: int | None = None
    pageid: int | None = None


@dataclass(frozen=True)
class SearchResult:
    title: str
    pageid: int | None = None
    size: int | None = None
    wordcount: int | None = None
    snippet: str = ""
    timestamp: str | None = None

    @classmethod
    def from_api(cls, hit: Mapping[str, Any]) -> "SearchResult":
        return cls(
            title=hit.get("title", ""),
            pageid=hit.get("pageid"),
            size=hit.get("size"),
            wordcount=hit.get("wordcount"),
            snippet=hit.get("snippet", ""),
            timestamp=hit.get("timestamp"),
        )


# --------------------------------------------------------------------------
# Pure helpers
# --------------------------------------------------------------------------


def build_user_agent(requests_version: str | None = None) -> str:
    """Build the WMF-policy User-Agent.

    Format is mandated by the Wikimedia User-Agent policy:
    ``<client>/<version> (<contact>) <library>/<version>``.  Sending anything
    else risks a 403 without notice.
    """
    version = requests_version or getattr(requests, "__version__", "0")
    return f"{_UA_CLIENT} ({_UA_CONTACT}) python-requests/{version}"


def sandbox_title(username: str, term: str) -> str:
    """Userspace staging title for one term, e.g. ``User:Foo/sandbox/སེམས་``."""
    user = username.strip()
    if not user:
        raise ValueError("username must be a non-empty string")
    cleaned = unicodedata.normalize("NFC", term).strip()
    if not cleaned:
        raise ValueError("term must be a non-empty string")
    return f"{USER_SANDBOX_PREFIX.format(username=user)}/{cleaned}"


def strip_terminal_punctuation(title: str) -> str:
    """Drop trailing tsheg / shad / double shad from a *title*.

    Only ever applied to titles for probing.  Stored article text keeps its
    punctuation untouched — the tsheg is orthography, and removing it is a
    spelling error (wikitext-spec.md §4).
    """
    stripped = unicodedata.normalize("NFC", title).strip()
    changed = True
    while changed:
        changed = False
        for mark in _TRAILING_PUNCTUATION:
            if stripped.endswith(mark):
                stripped = stripped[: -len(mark)].rstrip()
                changed = True
    return stripped


def title_variants(title: str) -> list[str]:
    """Every title a term may live at on bo.wikipedia, original first.

    ``སངས་རྒྱས་`` (tsheg), ``སངས་རྒྱས།`` (shad) and bare ``སངས་རྒྱས`` are three
    unrelated pages on the live wiki right now.  Checking one form and creating
    on that basis produces a fourth, so every existence check probes all three.
    """
    normalized = unicodedata.normalize("NFC", title).strip()
    if not normalized:
        raise ValueError("title must be a non-empty string")
    bare = strip_terminal_punctuation(normalized)
    if not bare:
        raise ValueError(f"title {title!r} contains nothing but punctuation")

    ordered = [normalized, bare, bare + TSHEG, bare + SHAD]
    seen: set[str] = set()
    variants: list[str] = []
    for candidate in ordered:
        if candidate not in seen:
            seen.add(candidate)
            variants.append(candidate)
    return variants


def utc_now_iso() -> str:
    """MediaWiki timestamp for ``starttimestamp`` (``2026-07-29T09:00:00Z``)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _as_int(value: Any, default: int | None = None) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clean_params(params: Mapping[str, Any]) -> dict[str, Any]:
    """Drop ``None``/``False`` and render ``True`` as ``1`` for the API."""
    cleaned: dict[str, Any] = {}
    for key, value in params.items():
        if value is None or value is False:
            continue
        cleaned[key] = 1 if value is True else value
    return cleaned


def _api_error(payload: Any) -> dict[str, Any] | None:
    """Extract the error object from either error format.

    ``errorformat=plaintext`` returns ``errors: [...]``; older/global errors
    still arrive as ``error: {...}``.  Both shapes occur in practice.
    """
    if not isinstance(payload, Mapping):
        return None
    error = payload.get("error")
    if isinstance(error, Mapping):
        return dict(error)
    errors = payload.get("errors")
    if isinstance(errors, Sequence) and not isinstance(errors, (str, bytes)):
        for candidate in errors:
            if isinstance(candidate, Mapping):
                return dict(candidate)
    return None


def _error_message(error: Mapping[str, Any]) -> str:
    for key in ("text", "info", "*", "html"):
        value = error.get(key)
        if isinstance(value, str) and value:
            return value
        if isinstance(value, Mapping):
            nested = value.get("text") or value.get("*")
            if isinstance(nested, str) and nested:
                return nested
    return error.get("code", "unknown API error")


def _iter_pages(query: Mapping[str, Any]) -> Iterator[Mapping[str, Any]]:
    """Yield page objects from either formatversion (list or pageid-keyed)."""
    pages = query.get("pages")
    if isinstance(pages, Sequence) and not isinstance(pages, (str, bytes)):
        for page in pages:
            if isinstance(page, Mapping):
                yield page
    elif isinstance(pages, Mapping):
        for page in pages.values():
            if isinstance(page, Mapping):
                yield page


def _mapping_pairs(query: Mapping[str, Any], key: str) -> dict[str, str]:
    """Read ``query.normalized`` / ``query.redirects`` into a from->to dict."""
    entries = query.get(key)
    pairs: dict[str, str] = {}
    if isinstance(entries, Sequence) and not isinstance(entries, (str, bytes)):
        for entry in entries:
            if isinstance(entry, Mapping) and "from" in entry and "to" in entry:
                pairs[str(entry["from"])] = str(entry["to"])
    return pairs


# --------------------------------------------------------------------------
# Client
# --------------------------------------------------------------------------


class WikiClient:
    """One ``requests.Session`` against one wiki's ``api.php``.

    Session reuse is mandatory rather than stylistic: login cookies and the CDN
    rate-limit cookies must both persist for the process lifetime.
    """

    def __init__(
        self,
        site: str = DEFAULT_SITE,
        dry_run: bool = True,
        user_agent: str | None = None,
        session: requests.Session | None = None,
        *,
        maxlag: int = _DEFAULT_MAXLAG,
        max_retries: int = _DEFAULT_MAX_RETRIES,
        timeout: float = _DEFAULT_TIMEOUT,
        min_edit_interval: float = EDIT_INTERVAL_UNFLAGGED,
        mark_bot: bool = True,
        sleep: Any = time.sleep,
    ) -> None:
        self.site = site
        self.api_url = f"https://{site}/w/api.php"
        self.dry_run = dry_run
        self.user_agent = user_agent or build_user_agent()
        self.maxlag = maxlag
        self.max_retries = max(1, max_retries)
        self.timeout = timeout
        self.min_edit_interval = min_edit_interval
        self.mark_bot = mark_bot
        self.username: str | None = None
        self.last_login_result: str | None = None

        # An injected session is assumed to carry its own auth (OAuth bearer,
        # a test double, a pre-logged-in session); we do not police it.
        self._owns_session = session is None
        self.session = session if session is not None else requests.Session()
        try:
            self.session.headers["User-Agent"] = self.user_agent
        except (AttributeError, TypeError):  # pragma: no cover - exotic doubles
            logger.debug("session has no mutable headers mapping")

        self._sleep = sleep
        self._csrf_token: str | None = None
        self._authenticated = False
        self._last_edit_monotonic: float | None = None

    # -- plumbing ---------------------------------------------------------

    def __enter__(self) -> "WikiClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()

    def close(self) -> None:
        """Close the session only if we created it."""
        if self._owns_session:
            self.session.close()

    def _call(self, method: str, params: Mapping[str, Any]) -> dict[str, Any]:
        """One API round trip, with maxlag/ratelimit backoff.

        ``maxlag`` arrives as **HTTP 200 with an error body** plus a
        ``Retry-After`` header, so ``raise_for_status`` never sees it.
        """
        payload = _clean_params(params)
        payload.setdefault("format", "json")
        payload.setdefault("formatversion", "2")
        payload.setdefault("errorformat", "plaintext")
        payload.setdefault("maxlag", self.maxlag)

        last_error: dict[str, Any] | None = None
        for attempt in range(self.max_retries):
            try:
                if method == "POST":
                    response = self.session.post(
                        self.api_url, data=payload, timeout=self.timeout
                    )
                else:
                    response = self.session.get(
                        self.api_url, params=payload, timeout=self.timeout
                    )
            except requests.RequestException as exc:
                if attempt + 1 >= self.max_retries:
                    raise WikiError(f"transport failure: {exc}") from exc
                self._backoff(attempt, None)
                continue

            status = getattr(response, "status_code", 200)
            if status in (429, 502, 503, 504):
                if attempt + 1 >= self.max_retries:
                    raise WikiError(f"HTTP {status} from {self.api_url}")
                self._backoff(attempt, response)
                continue
            if status >= 400:
                raise WikiError(f"HTTP {status} from {self.api_url}")

            try:
                data = response.json()
            except ValueError as exc:
                raise WikiError(f"non-JSON response from {self.api_url}") from exc
            if not isinstance(data, Mapping):
                raise WikiError(f"unexpected response shape from {self.api_url}")

            error = _api_error(data)
            if error is None:
                return dict(data)

            last_error = error
            code = str(error.get("code", ""))
            if code in _RETRY_CODES:
                if attempt + 1 >= self.max_retries:
                    break  # exhausted; reported as "gave up", not as a bare maxlag
                logger.warning(
                    "%s from %s (attempt %d/%d): %s",
                    code,
                    self.api_url,
                    attempt + 1,
                    self.max_retries,
                    _error_message(error),
                )
                self._backoff(attempt, response)
                continue
            _raise_api_error(error)

        # Retries exhausted on a retryable code.
        message = _error_message(last_error) if last_error else "retries exhausted"
        raise WikiError(
            f"gave up after {self.max_retries} attempts: {message}",
            code=str(last_error.get("code")) if last_error else None,
            payload=last_error,
        )

    def _backoff(self, attempt: int, response: Any) -> None:
        """Honour ``Retry-After`` and add a linear penalty per attempt."""
        delay = float(self.maxlag)
        headers = getattr(response, "headers", None) or {}
        try:
            retry_after = headers.get("Retry-After")
        except AttributeError:  # pragma: no cover - exotic doubles
            retry_after = None
        if retry_after is not None:
            try:
                delay = max(delay, float(retry_after))
            except (TypeError, ValueError):
                pass
        self._sleep(delay + attempt * float(self.maxlag))

    def _get(self, **params: Any) -> dict[str, Any]:
        return self._call("GET", params)

    def _post(self, **params: Any) -> dict[str, Any]:
        return self._call("POST", params)

    # -- authentication ---------------------------------------------------

    def login(self, username: str, password: str) -> bool:
        """Log in with a ``Special:BotPasswords`` credential.

        Credentials are arguments, never module-level environment reads, so a
        test or a caller can never accidentally pick up ambient secrets.
        ``action=login`` is documented as bot-password-only; main-account use is
        deprecated and may fail without warning.
        """
        if not username or not password:
            raise ValueError("username and password are both required")

        token_payload = self._get(action="query", meta="tokens", type="login")
        login_token = (
            token_payload.get("query", {}).get("tokens", {}).get("logintoken")
        )
        if not login_token:
            raise WikiError("API returned no login token", payload=token_payload)

        payload = self._post(
            action="login",
            lgname=username,
            lgpassword=password,
            lgtoken=login_token,
        )
        result_block = payload.get("login", {})
        result = str(result_block.get("result", ""))
        self.last_login_result = result
        if result != "Success":
            reason = result_block.get("reason")
            if isinstance(reason, Mapping):
                reason = reason.get("text") or reason.get("code")
            logger.error("login failed for %s: %s (%s)", username, result, reason)
            self._authenticated = False
            return False

        self.username = result_block.get("lgusername") or username.split("@", 1)[0]
        self._authenticated = True
        self._csrf_token = None  # tokens are session-scoped; the session changed
        logger.info("logged in to %s as %s", self.site, self.username)
        return True

    def csrf_token(self, force: bool = False) -> str:
        """Fetch (and cache) the edit token; ``force`` refreshes after badtoken."""
        if self._csrf_token is None or force:
            payload = self._get(action="query", meta="tokens", type="csrf")
            token = payload.get("query", {}).get("tokens", {}).get("csrftoken")
            if not token:
                raise NotAuthenticated("API returned no CSRF token", payload=payload)
            if token == "+\\":
                raise NotAuthenticated(
                    "anonymous CSRF token (+\\) — call login() first"
                )
            self._csrf_token = str(token)
        return self._csrf_token

    # -- reads ------------------------------------------------------------

    @staticmethod
    def title_variants(title: str) -> list[str]:
        """See module-level :func:`title_variants`; exposed for convenience."""
        return title_variants(title)

    def resolve_title(self, title: str) -> TitleResolution:
        """Probe every variant of ``title`` in a single batched query.

        One call, because ``titles`` accepts a pipe-separated list — probing
        serially would triple the request count for every term in the run.
        """
        variants = title_variants(title)
        payload = self._get(
            action="query",
            titles="|".join(variants),
            prop="info",
            inprop="url",
            redirects=1,
        )
        query = payload.get("query", {}) or {}
        normalized = _mapping_pairs(query, "normalized")
        redirects = _mapping_pairs(query, "redirects")
        by_title = {
            page.get("title", ""): PageInfo.from_api(page)
            for page in _iter_pages(query)
        }

        matched_variant: str | None = None
        matched_page: PageInfo | None = None
        target_page: PageInfo | None = None
        existing: list[str] = []

        for variant in variants:
            canonical = normalized.get(variant, variant)
            if canonical in redirects:
                # The API followed the redirect, so no page entry exists for the
                # source itself; we know it exists because it was followed.
                destination = redirects[canonical]
                page = PageInfo(
                    title=canonical,
                    exists=True,
                    is_redirect=True,
                    redirect_target=destination,
                )
                landed = by_title.get(destination)
            else:
                page = by_title.get(canonical)
                landed = None
                if page is None or not page.exists:
                    continue

            existing.append(variant)
            if matched_variant is None:
                matched_variant = variant
                matched_page = page
                target_page = landed

        return TitleResolution(
            requested=variants[0],
            variants=tuple(variants),
            matched_variant=matched_variant,
            page=matched_page,
            target_page=target_page,
            existing_variants=tuple(existing),
        )

    def exists(self, title: str) -> PageInfo | None:
        """The first existing variant of ``title``, or ``None``.

        A redirect counts as existing — creating over one is still a duplicate.
        """
        resolution = self.resolve_title(title)
        return resolution.page if resolution.exists else None

    def get_revision(self, title: str, follow_redirects: bool = True) -> Revision | None:
        """Content *and* the conflict baseline in one call.

        The timestamp is the whole point: it is what goes back as
        ``basetimestamp``, and fetching content without it means the update path
        cannot detect an edit conflict.
        """
        payload = self._get(
            action="query",
            prop="revisions",
            titles=title,
            rvslots="main",
            rvprop="content|timestamp|ids",
            rvlimit=1,
            redirects=1 if follow_redirects else None,
        )
        query = payload.get("query", {}) or {}
        for page in _iter_pages(query):
            if page.get("missing"):
                continue
            revisions = page.get("revisions") or []
            if not revisions:
                continue
            revision = revisions[0]
            slots = revision.get("slots") or {}
            main = slots.get("main") or {}
            content = main.get("content")
            if content is None:
                content = revision.get("content", "")
            return Revision(
                title=page.get("title", title),
                content=unicodedata.normalize("NFC", str(content)),
                timestamp=str(revision.get("timestamp", "")),
                revid=revision.get("revid"),
                pageid=page.get("pageid"),
            )
        return None

    def get_wikitext(self, title: str, follow_redirects: bool = True) -> str | None:
        """Current wikitext, or ``None`` if the page does not exist.

        Use :meth:`get_revision` when you also need the timestamp for an edit.
        """
        revision = self.get_revision(title, follow_redirects=follow_redirects)
        return revision.content if revision else None

    def get_sections(self, title: str) -> list[Section]:
        """Section index for ``title``; empty list if the page does not exist.

        Reads are forgiving (missing page -> empty result) so callers can probe;
        writes are strict.  Target sections by ``index``/``anchor``, never by
        matching the heading line.
        """
        try:
            payload = self._get(action="parse", page=title, prop="sections")
        except WikiError as exc:
            if exc.code in ("missingtitle", "nosuchpageid", "invalidtitle"):
                logger.info("no sections: %s does not exist on %s", title, self.site)
                return []
            raise
        sections = payload.get("parse", {}).get("sections") or []
        return [Section.from_api(section) for section in sections if isinstance(section, Mapping)]

    def search(
        self,
        query: str,
        limit: int = 10,
        *,
        namespace: int = 0,
        what: str = "text",
    ) -> list[SearchResult]:
        """Full-text search.  ``what='nearmatch'`` is the precise existence probe."""
        payload = self._get(
            action="query",
            list="search",
            srsearch=query,
            srlimit=limit,
            srnamespace=namespace,
            srwhat=what,
            srprop="size|wordcount|snippet|timestamp",
        )
        hits = payload.get("query", {}).get("search") or []
        return [SearchResult.from_api(hit) for hit in hits if isinstance(hit, Mapping)]

    # -- writes -----------------------------------------------------------

    def create_page(
        self, title: str, wikitext: str, summary: str
    ) -> dict[str, Any]:
        """Create ``title``, refusing to touch it if it already exists.

        ``createonly=1`` closes the window between the variant probe and the
        write; without it a race (or a bug) creates a duplicate at a variant
        title, which is the failure mode this whole module exists to prevent.
        """
        params = {
            "action": "edit",
            "title": title,
            "text": wikitext,
            "summary": summary,
            "createonly": 1,
            "bot": 1 if self.mark_bot else None,
        }
        return self._write("create_page", title, wikitext, summary, params)

    def edit_page(
        self,
        title: str,
        wikitext: str,
        summary: str,
        basetimestamp: str,
        starttimestamp: str | None = None,
    ) -> dict[str, Any]:
        """Replace the whole page, aborting if it changed under us.

        ``basetimestamp`` detects a concurrent edit; ``starttimestamp`` detects
        a delete-and-recreate.  Omitting them silently clobbers human edits.
        """
        if not basetimestamp:
            raise ValueError("basetimestamp is required — refuse to clobber blind")
        params = {
            "action": "edit",
            "title": title,
            "text": wikitext,
            "summary": summary,
            "nocreate": 1,
            "basetimestamp": basetimestamp,
            "starttimestamp": starttimestamp or utc_now_iso(),
            "bot": 1 if self.mark_bot else None,
        }
        return self._write("edit_page", title, wikitext, summary, params)

    def edit_section(
        self,
        title: str,
        section_index: int | str,
        wikitext: str,
        summary: str,
        basetimestamp: str,
        starttimestamp: str | None = None,
    ) -> dict[str, Any]:
        """Replace one section — the update path's unit of change.

        Section-targeted edits keep diffs reviewable; a whole-page rewrite for a
        one-sentence addition is unreviewable on a wiki with two admins.
        """
        if not basetimestamp:
            raise ValueError("basetimestamp is required — refuse to clobber blind")
        index = str(section_index)
        if not index.isdigit():
            raise ValueError(
                f"section_index must be a numeric section index, got {section_index!r}"
            )
        params = {
            "action": "edit",
            "title": title,
            "section": index,
            "text": wikitext,
            "summary": summary,
            "nocreate": 1,
            "basetimestamp": basetimestamp,
            "starttimestamp": starttimestamp or utc_now_iso(),
            "bot": 1 if self.mark_bot else None,
        }
        return self._write(
            "edit_section", title, wikitext, summary, params, section=index
        )

    def _write(
        self,
        operation: str,
        title: str,
        wikitext: str,
        summary: str,
        params: Mapping[str, Any],
        **plan_extra: Any,
    ) -> dict[str, Any]:
        """Shared write path: dry-run gate, throttle, token, badtoken retry."""
        if self.dry_run:
            plan = self._plan(operation, title, wikitext, summary, params, **plan_extra)
            logger.info(
                "DRY RUN %s %s on %s (%d bytes) — no request sent",
                operation,
                title,
                self.site,
                plan["bytes"],
            )
            return plan

        if self._owns_session and not self._authenticated:
            raise NotAuthenticated(
                f"{operation} requires a login; call login() or inject an "
                "authenticated session"
            )

        self._throttle()
        request = dict(params)
        # assert=user turns a silently expired session into a hard failure
        # instead of a burst of IP-attributed edits.
        request["assert"] = "user"
        if self.username:
            request["assertuser"] = self.username

        try:
            payload = self._call("POST", {**request, "token": self.csrf_token()})
        except NotAuthenticated as exc:
            if exc.code != "badtoken":
                raise
            logger.warning("badtoken on %s; refreshing CSRF token once", operation)
            payload = self._call(
                "POST", {**request, "token": self.csrf_token(force=True)}
            )

        self._last_edit_monotonic = time.monotonic()
        result = payload.get("edit", payload)
        logger.info("%s %s on %s: %s", operation, title, self.site, result.get("result"))
        return dict(result)

    def _plan(
        self,
        operation: str,
        title: str,
        wikitext: str,
        summary: str,
        params: Mapping[str, Any],
        **extra: Any,
    ) -> dict[str, Any]:
        """The planned-action record returned instead of writing.

        It carries the exact parameters that would be POSTed (minus the token)
        so a reviewer can audit the write without trusting a prose summary.
        """
        planned = _clean_params(params)
        planned.pop("text", None)
        plan = {
            "dry_run": True,
            "operation": operation,
            "site": self.site,
            "api_url": self.api_url,
            "title": title,
            "summary": summary,
            "wikitext": wikitext,
            "bytes": len(wikitext.encode("utf-8")),
            "params": planned,
        }
        plan.update(extra)
        return plan

    def _throttle(self) -> None:
        """Hold the meta:Bot policy edit interval between real writes."""
        if self.min_edit_interval <= 0 or self._last_edit_monotonic is None:
            return
        elapsed = time.monotonic() - self._last_edit_monotonic
        remaining = self.min_edit_interval - elapsed
        if remaining > 0:
            logger.debug("throttling %.1fs before next edit", remaining)
            self._sleep(remaining)


def _raise_api_error(error: Mapping[str, Any]) -> None:
    """Map an API error code onto this module's exception vocabulary."""
    code = str(error.get("code", ""))
    message = _error_message(error)
    if code in _CONFLICT_CODES:
        raise EditConflict(message, code=code, payload=error)
    if code in _EXISTS_CODES:
        raise PageExists(message, code=code, payload=error)
    if code in _AUTH_CODES:
        raise NotAuthenticated(message, code=code, payload=error)
    raise WikiError(message, code=code, payload=error)
