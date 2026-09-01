"""Offline tests for the bo.wikipedia Action API client.

``requests.Session`` is replaced wholesale by a ``MagicMock`` spec'd against the
real class, so a test that accidentally reaches the network fails on a missing
queued response instead of hitting a live encyclopedia.  No test needs an API
key, a bot password, or a socket.

The behaviours pinned here are the ones whose failure damages the wiki rather
than the run: the title-variant probe, the dry-run default, edit-conflict
detection, and the maxlag backoff.
"""

from __future__ import annotations

import unicodedata
from typing import Any, Iterable, Mapping
from unittest.mock import MagicMock

import pytest
import requests

from kangyur_wiki.wiki.client import (
    SHAD,
    TSHEG,
    EditConflict,
    NotAuthenticated,
    PageExists,
    PageInfo,
    WikiClient,
    WikiError,
    build_user_agent,
    sandbox_title,
    strip_terminal_punctuation,
    title_variants,
)

# Real bo.wikipedia titles: all three of these exist as separate pages.
BARE = "སངས་རྒྱས"
WITH_TSHEG = BARE + TSHEG
WITH_SHAD = BARE + SHAD


# --------------------------------------------------------------------------
# Test doubles
# --------------------------------------------------------------------------


class FakeResponse:
    """Minimal stand-in for ``requests.Response``.

    ``maxlag`` arrives as HTTP 200 with an error body and a ``Retry-After``
    header, so status code and headers both have to be controllable
    independently of the JSON payload.
    """

    def __init__(
        self,
        payload: Any = None,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        *,
        bad_json: bool = False,
    ) -> None:
        self._payload = payload
        self.status_code = status_code
        self.headers = dict(headers or {})
        self._bad_json = bad_json

    def json(self) -> Any:
        if self._bad_json:
            raise ValueError("Expecting value: line 1 column 1 (char 0)")
        return self._payload


def make_session(
    get: Iterable[Any] = (), post: Iterable[Any] = ()
) -> MagicMock:
    """A ``requests.Session`` double that replays queued responses in order."""
    session = MagicMock(spec=requests.Session)
    session.headers = {}
    session.get.side_effect = list(get)
    session.post.side_effect = list(post)
    return session


class SleepRecorder:
    """Captures backoff durations instead of spending them."""

    def __init__(self) -> None:
        self.calls: list[float] = []

    def __call__(self, seconds: float) -> None:
        self.calls.append(float(seconds))


def make_client(session: MagicMock, **kwargs: Any) -> tuple[WikiClient, SleepRecorder]:
    """Client wired to a fake session, no real sleeping, no edit throttle."""
    sleeper = SleepRecorder()
    kwargs.setdefault("dry_run", True)
    kwargs.setdefault("min_edit_interval", 0.0)
    client = WikiClient(session=session, sleep=sleeper, **kwargs)
    return client, sleeper


def token_response(kind: str, value: str) -> FakeResponse:
    return FakeResponse({"batchcomplete": True, "query": {"tokens": {kind: value}}})


def error_response(
    code: str, text: str = "boom", **kwargs: Any
) -> FakeResponse:
    """An ``errorformat=plaintext`` error body (HTTP 200, as the API sends it)."""
    return FakeResponse({"errors": [{"code": code, "text": text, "module": "edit"}]}, **kwargs)


def get_params(session: MagicMock, index: int = 0) -> dict[str, Any]:
    return session.get.call_args_list[index].kwargs["params"]


def post_data(session: MagicMock, index: int = 0) -> dict[str, Any]:
    return session.post.call_args_list[index].kwargs["data"]


def authenticated_client(
    get: Iterable[Any] = (), post: Iterable[Any] = (), **kwargs: Any
) -> tuple[WikiClient, MagicMock, SleepRecorder]:
    """A live-write client whose auth is taken on trust (injected session).

    An injected session is treated as carrying its own credentials, which is
    exactly how the OAuth path will work; it lets write tests skip the login
    round trip without poking at private attributes.
    """
    session = make_session(get=get, post=post)
    client, sleeper = make_client(session, dry_run=False, **kwargs)
    return client, session, sleeper


# --------------------------------------------------------------------------
# Pure helpers
# --------------------------------------------------------------------------


def test_title_variants_from_bare_covers_all_three_live_forms():
    assert title_variants(BARE) == [BARE, WITH_TSHEG, WITH_SHAD]


def test_title_variants_puts_the_requested_form_first():
    # Ordering is load-bearing: resolve_title reports the first *existing*
    # variant, so the caller's own spelling must win ties.
    assert title_variants(WITH_TSHEG) == [WITH_TSHEG, BARE, WITH_SHAD]
    assert title_variants(WITH_SHAD) == [WITH_SHAD, BARE, WITH_TSHEG]


def test_title_variants_are_deduped():
    variants = title_variants(WITH_SHAD)
    assert len(variants) == len(set(variants)) == 3


def test_title_variants_strips_a_double_shad():
    assert title_variants(BARE + "༎")[1] == BARE


def test_title_variants_normalizes_to_nfc():
    # U+0F43 is a composition exclusion: NFC decomposes it to U+0F42 U+0FB7.
    # Probing the precomposed form against a wiki that stores NFC silently
    # misses the page.
    precomposed = "གྷ" + TSHEG
    assert title_variants(precomposed)[0] == unicodedata.normalize("NFC", precomposed)
    assert all(v == unicodedata.normalize("NFC", v) for v in title_variants(precomposed))


@pytest.mark.parametrize("bad", ["", "   ", TSHEG, SHAD, TSHEG + SHAD])
def test_title_variants_rejects_empty_or_punctuation_only(bad):
    with pytest.raises(ValueError):
        title_variants(bad)


def test_strip_terminal_punctuation_leaves_interior_marks_alone():
    # The tsheg between syllables is orthography, not trailing punctuation.
    assert strip_terminal_punctuation(WITH_TSHEG) == BARE
    assert TSHEG in strip_terminal_punctuation(WITH_TSHEG)


def test_sandbox_title():
    assert sandbox_title("OpenPechaBot", WITH_TSHEG) == (
        f"User:OpenPechaBot/sandbox/{WITH_TSHEG}"
    )


def test_sandbox_title_rejects_blank_inputs():
    with pytest.raises(ValueError):
        sandbox_title("", WITH_TSHEG)
    with pytest.raises(ValueError):
        sandbox_title("OpenPechaBot", "  ")


def test_build_user_agent_matches_wmf_policy_format():
    ua = build_user_agent("2.34.2")
    assert ua == (
        "IATS-2026-Pipeline/0.1 "
        "(https://github.com/OpenPecha; openpecha@gmail.com) "
        "python-requests/2.34.2"
    )


def test_user_agent_is_installed_on_the_session():
    session = make_session()
    make_client(session)
    assert "IATS-2026-Pipeline" in session.headers["User-Agent"]
    assert "openpecha@gmail.com" in session.headers["User-Agent"]


# --------------------------------------------------------------------------
# Dry run — the default
# --------------------------------------------------------------------------


def test_dry_run_is_the_default():
    assert WikiClient(session=make_session()).dry_run is True


def test_dry_run_create_returns_a_plan_and_sends_nothing():
    session = make_session()
    client, _ = make_client(session)

    plan = client.create_page(WITH_TSHEG, "'''ཚིག''' ...", "creating")

    assert plan["dry_run"] is True
    assert plan["operation"] == "create_page"
    assert plan["title"] == WITH_TSHEG
    assert plan["summary"] == "creating"
    assert plan["wikitext"] == "'''ཚིག''' ..."
    assert plan["params"]["createonly"] == 1
    assert plan["params"]["bot"] == 1
    assert plan["api_url"] == "https://bo.wikipedia.org/w/api.php"
    # The plan carries the byte size the wiki would see, not the char count.
    assert plan["bytes"] == len("'''ཚིག''' ...".encode("utf-8"))
    session.get.assert_not_called()
    session.post.assert_not_called()


def test_dry_run_edit_plan_carries_the_conflict_baseline():
    session = make_session()
    client, _ = make_client(session)

    plan = client.edit_page(
        WITH_TSHEG, "new", "updating", basetimestamp="2026-07-29T09:00:00Z"
    )

    assert plan["params"]["basetimestamp"] == "2026-07-29T09:00:00Z"
    assert plan["params"]["nocreate"] == 1
    assert plan["params"]["starttimestamp"].endswith("Z")
    session.post.assert_not_called()


def test_dry_run_section_plan_names_the_section():
    session = make_session()
    client, _ = make_client(session)

    plan = client.edit_section(
        WITH_TSHEG, 3, "text", "updating", basetimestamp="2026-07-29T09:00:00Z"
    )

    assert plan["section"] == "3"
    assert plan["params"]["section"] == "3"
    session.post.assert_not_called()


def test_dry_run_never_needs_a_login():
    session = make_session()
    client, _ = make_client(session)
    assert client.create_page(WITH_TSHEG, "x", "y")["dry_run"] is True


# --------------------------------------------------------------------------
# Write guards
# --------------------------------------------------------------------------


def test_edit_page_refuses_without_a_basetimestamp():
    client, _ = make_client(make_session())
    with pytest.raises(ValueError, match="basetimestamp"):
        client.edit_page(WITH_TSHEG, "text", "summary", basetimestamp="")


def test_edit_section_refuses_an_anchor_instead_of_an_index():
    # Anchors are for *finding* a section; only the numeric index addresses one.
    client, _ = make_client(make_session())
    with pytest.raises(ValueError, match="section_index"):
        client.edit_section(
            WITH_TSHEG, "ལུང་ཁུངས།", "text", "summary", basetimestamp="2026-01-01T00:00:00Z"
        )


def test_write_without_login_raises_before_any_request(monkeypatch):
    session = make_session()
    monkeypatch.setattr(requests, "Session", lambda: session)
    client = WikiClient(dry_run=False, sleep=SleepRecorder(), min_edit_interval=0.0)

    with pytest.raises(NotAuthenticated):
        client.create_page(WITH_TSHEG, "text", "summary")

    session.post.assert_not_called()


# --------------------------------------------------------------------------
# Auth and the CSRF token flow
# --------------------------------------------------------------------------


def test_login_then_edit_walks_the_documented_token_flow():
    session = make_session(
        get=[token_response("logintoken", "LOGIN+\\"), token_response("csrftoken", "CSRF+\\")],
        post=[
            FakeResponse({"login": {"result": "Success", "lgusername": "OpenPechaBot"}}),
            FakeResponse({"edit": {"result": "Success", "pageid": 42, "title": WITH_TSHEG}}),
        ],
    )
    client, _ = make_client(session, dry_run=False)

    assert client.login("OpenPechaBot@iats", "secret") is True
    assert client.username == "OpenPechaBot"

    result = client.create_page(WITH_TSHEG, "text", "summary")
    assert result["result"] == "Success"

    # GET tokens(login) -> POST login -> GET tokens(csrf) -> POST edit
    assert get_params(session, 0)["type"] == "login"
    assert get_params(session, 0)["meta"] == "tokens"
    login_body = post_data(session, 0)
    assert login_body["action"] == "login"
    assert login_body["lgname"] == "OpenPechaBot@iats"
    assert login_body["lgpassword"] == "secret"
    assert login_body["lgtoken"] == "LOGIN+\\"
    assert get_params(session, 1)["type"] == "csrf"

    edit_body = post_data(session, 1)
    assert edit_body["token"] == "CSRF+\\"
    assert edit_body["action"] == "edit"
    assert edit_body["createonly"] == 1
    assert edit_body["bot"] == 1
    assert edit_body["assert"] == "user"
    assert edit_body["assertuser"] == "OpenPechaBot"
    assert edit_body["maxlag"] == 5


def test_csrf_token_is_fetched_once_per_session():
    session = make_session(get=[token_response("csrftoken", "CSRF+\\")])
    client, _ = make_client(session)

    assert client.csrf_token() == "CSRF+\\"
    assert client.csrf_token() == "CSRF+\\"
    assert session.get.call_count == 1


def test_csrf_token_force_refetches():
    session = make_session(
        get=[token_response("csrftoken", "ONE+\\"), token_response("csrftoken", "TWO+\\")]
    )
    client, _ = make_client(session)

    assert client.csrf_token() == "ONE+\\"
    assert client.csrf_token(force=True) == "TWO+\\"
    assert session.get.call_count == 2


def test_anonymous_csrf_token_is_rejected():
    # "+\\" is what an unauthenticated session gets back; editing with it would
    # produce IP-attributed edits.
    session = make_session(get=[token_response("csrftoken", "+\\")])
    client, _ = make_client(session)
    with pytest.raises(NotAuthenticated):
        client.csrf_token()


def test_login_failure_returns_false_without_raising():
    session = make_session(
        get=[token_response("logintoken", "LOGIN+\\")],
        post=[
            FakeResponse(
                {"login": {"result": "Failed", "reason": {"text": "Incorrect password."}}}
            )
        ],
    )
    client, _ = make_client(session)

    assert client.login("OpenPechaBot@iats", "wrong") is False
    assert client.last_login_result == "Failed"


def test_login_without_a_token_raises():
    session = make_session(get=[FakeResponse({"query": {"tokens": {}}})])
    client, _ = make_client(session)
    with pytest.raises(WikiError, match="login token"):
        client.login("OpenPechaBot@iats", "secret")


def test_login_requires_both_credentials():
    client, _ = make_client(make_session())
    with pytest.raises(ValueError):
        client.login("OpenPechaBot@iats", "")


def test_badtoken_triggers_exactly_one_token_refresh():
    client, session, _ = authenticated_client(
        get=[
            token_response("csrftoken", "STALE+\\"),
            token_response("csrftoken", "FRESH+\\"),
        ],
        post=[
            error_response("badtoken", "Invalid CSRF token."),
            FakeResponse({"edit": {"result": "Success"}}),
        ],
    )

    assert client.create_page(WITH_TSHEG, "text", "summary")["result"] == "Success"
    assert session.get.call_count == 2  # exactly one refresh, not a loop
    assert post_data(session, 0)["token"] == "STALE+\\"
    assert post_data(session, 1)["token"] == "FRESH+\\"


# --------------------------------------------------------------------------
# maxlag / backoff
# --------------------------------------------------------------------------


def test_maxlag_error_is_retried_and_then_succeeds():
    # HTTP 200 with an error body: raise_for_status would never see this.
    session = make_session(
        get=[
            error_response("maxlag", "Waiting for db: 6 seconds lagged.", headers={"Retry-After": "5"}),
            FakeResponse({"query": {"search": []}}),
        ]
    )
    client, sleeper = make_client(session)

    assert client.search("སེམས་") == []
    assert session.get.call_count == 2
    assert sleeper.calls and sleeper.calls[0] >= 5.0


def test_backoff_honours_a_long_retry_after():
    session = make_session(
        get=[
            error_response("maxlag", "lagged", headers={"Retry-After": "30"}),
            FakeResponse({"query": {"search": []}}),
        ]
    )
    client, sleeper = make_client(session)

    client.search("སེམས་")
    assert sleeper.calls[0] >= 30.0


def test_retries_are_exhausted_into_a_wiki_error():
    session = make_session(get=[error_response("maxlag", "lagged") for _ in range(3)])
    client, sleeper = make_client(session, max_retries=3)

    with pytest.raises(WikiError, match="gave up after 3 attempts"):
        client.search("སེམས་")

    assert session.get.call_count == 3
    assert len(sleeper.calls) == 2  # no sleep after the final attempt


def test_backoff_grows_with_each_attempt():
    session = make_session(
        get=[error_response("ratelimited", "slow down") for _ in range(2)]
        + [FakeResponse({"query": {"search": []}})]
    )
    client, sleeper = make_client(session, max_retries=3)

    client.search("སེམས་")
    assert sleeper.calls[1] > sleeper.calls[0]


def test_transient_http_5xx_is_retried():
    session = make_session(
        get=[FakeResponse(status_code=503), FakeResponse({"query": {"search": []}})]
    )
    client, _ = make_client(session)

    assert client.search("སེམས་") == []
    assert session.get.call_count == 2


def test_hard_http_error_is_not_retried():
    session = make_session(get=[FakeResponse(status_code=403)])
    client, _ = make_client(session)

    with pytest.raises(WikiError, match="HTTP 403"):
        client.search("སེམས་")
    assert session.get.call_count == 1


def test_non_json_response_is_a_wiki_error():
    session = make_session(get=[FakeResponse(bad_json=True)])
    client, _ = make_client(session)
    with pytest.raises(WikiError, match="non-JSON"):
        client.search("སེམས་")


def test_transport_failure_is_retried_then_wrapped():
    session = make_session(
        get=[requests.ConnectionError("dns"), FakeResponse({"query": {"search": []}})]
    )
    client, _ = make_client(session)

    assert client.search("སེམས་") == []


def test_maxlag_is_sent_on_every_call():
    session = make_session(get=[FakeResponse({"query": {"search": []}})])
    client, _ = make_client(session)
    client.search("སེམས་")
    assert get_params(session)["maxlag"] == 5


# --------------------------------------------------------------------------
# Edit-conflict and create-collision handling
# --------------------------------------------------------------------------


def test_edit_conflict_raises_and_is_never_retried():
    client, session, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[error_response("editconflict", f"Edit conflict: {WITH_SHAD}")],
    )

    with pytest.raises(EditConflict) as excinfo:
        client.edit_page(
            WITH_SHAD, "text", "summary", basetimestamp="2026-07-29T09:00:00Z"
        )

    assert excinfo.value.code == "editconflict"
    assert session.post.call_count == 1  # a retry would clobber the human edit


def test_create_on_an_existing_title_raises_page_exists():
    client, _, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[error_response("articleexists", "The page has been created already.")],
    )

    with pytest.raises(PageExists) as excinfo:
        client.create_page(WITH_TSHEG, "text", "summary")
    assert excinfo.value.code == "articleexists"


def test_permission_denied_raises_not_authenticated():
    client, _, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[error_response("assertuserfailed", "You are not logged in.")],
    )
    with pytest.raises(NotAuthenticated):
        client.create_page(WITH_TSHEG, "text", "summary")


def test_edit_page_sends_both_conflict_timestamps():
    client, session, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[FakeResponse({"edit": {"result": "Success"}})],
    )

    client.edit_page(
        WITH_SHAD,
        "text",
        "summary",
        basetimestamp="2026-07-29T09:00:00Z",
        starttimestamp="2026-07-29T09:05:00Z",
    )

    body = post_data(session, 0)
    assert body["basetimestamp"] == "2026-07-29T09:00:00Z"
    assert body["starttimestamp"] == "2026-07-29T09:05:00Z"
    assert body["nocreate"] == 1
    assert "createonly" not in body


def test_edit_section_targets_by_index():
    client, session, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[FakeResponse({"edit": {"result": "Success"}})],
    )

    client.edit_section(
        WITH_SHAD, 2, "text", "summary", basetimestamp="2026-07-29T09:00:00Z"
    )

    assert post_data(session, 0)["section"] == "2"


def test_edit_section_zero_edits_the_lead():
    # Section 0 is the unheaded lead, which the spec's article skeleton always
    # has; a falsy-index bug would silently rewrite the whole page instead.
    client, session, _ = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[FakeResponse({"edit": {"result": "Success"}})],
    )

    client.edit_section(
        WITH_SHAD, 0, "lead", "summary", basetimestamp="2026-07-29T09:00:00Z"
    )

    assert post_data(session, 0)["section"] == "0"


def test_bot_flag_can_be_turned_off():
    session = make_session()
    client, _ = make_client(session, mark_bot=False)
    assert "bot" not in client.create_page(WITH_TSHEG, "text", "summary")["params"]


def test_throttle_holds_the_policy_interval_between_writes():
    client, _, sleeper = authenticated_client(
        get=[token_response("csrftoken", "CSRF+\\")],
        post=[FakeResponse({"edit": {"result": "Success"}})] * 2,
        min_edit_interval=60.0,
    )

    client.create_page(WITH_TSHEG, "a", "s")  # first write goes straight out
    assert sleeper.calls == []
    client.create_page(WITH_SHAD, "b", "s")
    assert sleeper.calls and 58.0 < sleeper.calls[-1] <= 60.0


# --------------------------------------------------------------------------
# Title resolution — the variant probe
# --------------------------------------------------------------------------


def test_resolve_title_probes_all_variants_in_one_request():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "pages": [
                            {"ns": 0, "title": BARE, "missing": True},
                            {"ns": 0, "title": WITH_TSHEG, "pageid": 101, "length": 900},
                            {"ns": 0, "title": WITH_SHAD, "missing": True},
                        ]
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    resolution = client.resolve_title(BARE)

    assert session.get.call_count == 1
    assert set(get_params(session)["titles"].split("|")) == {BARE, WITH_TSHEG, WITH_SHAD}
    assert get_params(session)["redirects"] == 1
    assert resolution.exists is True
    assert resolution.matched_variant == WITH_TSHEG
    assert resolution.existing_variants == (WITH_TSHEG,)
    assert resolution.final_title == WITH_TSHEG
    assert resolution.page is not None and resolution.page.pageid == 101


def test_resolve_title_reports_nothing_when_no_variant_exists():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "pages": [
                            {"title": BARE, "missing": True},
                            {"title": WITH_TSHEG, "missing": True},
                            {"title": WITH_SHAD, "missing": True},
                        ]
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    resolution = client.resolve_title(BARE)
    assert resolution.exists is False
    assert resolution.final_title is None
    assert resolution.existing_variants == ()


def test_resolve_title_follows_a_redirect():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "redirects": [{"from": BARE, "to": WITH_TSHEG}],
                        "pages": [
                            {"title": WITH_TSHEG, "pageid": 101},
                            {"title": WITH_SHAD, "missing": True},
                        ],
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    resolution = client.resolve_title(BARE)

    assert resolution.matched_variant == BARE
    assert resolution.is_redirect is True
    assert resolution.redirect_target == WITH_TSHEG
    assert resolution.broken_redirect is False
    assert resolution.final_title == WITH_TSHEG
    assert set(resolution.existing_variants) == {BARE, WITH_TSHEG}


def test_resolve_title_flags_a_broken_redirect():
    # bo.wikipedia has live redirects pointing at pages that do not exist;
    # "the redirect exists" and "the target exists" are different facts.
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "redirects": [{"from": BARE, "to": "ཡོད་མེད།"}],
                        "pages": [
                            {"title": "ཡོད་མེད།", "missing": True},
                            {"title": WITH_TSHEG, "missing": True},
                            {"title": WITH_SHAD, "missing": True},
                        ],
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    resolution = client.resolve_title(BARE)
    assert resolution.exists is True
    assert resolution.broken_redirect is True
    assert resolution.final_title == BARE


def test_resolve_title_maps_api_title_normalization():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "normalized": [{"from": BARE, "to": "Normalized"}],
                        "pages": [{"title": "Normalized", "pageid": 7}],
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    resolution = client.resolve_title(BARE)
    assert resolution.matched_variant == BARE
    assert resolution.page is not None and resolution.page.pageid == 7


def test_exists_returns_page_info_for_the_first_live_variant():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "pages": [
                            {"title": BARE, "missing": True},
                            {"title": WITH_TSHEG, "pageid": 101, "redirect": True},
                            {"title": WITH_SHAD, "missing": True},
                        ]
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    info = client.exists(BARE)
    assert isinstance(info, PageInfo)
    assert info.title == WITH_TSHEG
    assert info.is_redirect is True  # a redirect still blocks creation


def test_exists_returns_none_when_missing():
    session = make_session(
        get=[FakeResponse({"query": {"pages": [{"title": BARE, "missing": True}]}})]
    )
    client, _ = make_client(session)
    assert client.exists(BARE) is None


def test_an_invalid_title_does_not_count_as_existing():
    # `invalid` comes back *without* a `missing` key; treating it as existing
    # would send the publisher down the update path for an unwritable title.
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "pages": [
                            {
                                "title": BARE,
                                "invalid": True,
                                "invalidreason": "Invalid title",
                            }
                        ]
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    assert client.exists(BARE) is None
    assert PageInfo.from_api({"title": BARE, "invalid": True}).invalid is True


def test_client_exposes_title_variants():
    client, _ = make_client(make_session())
    assert client.title_variants(BARE) == title_variants(BARE)


# --------------------------------------------------------------------------
# Reads
# --------------------------------------------------------------------------


def _revision_payload(content: str, timestamp: str) -> FakeResponse:
    return FakeResponse(
        {
            "query": {
                "pages": [
                    {
                        "pageid": 101,
                        "title": WITH_TSHEG,
                        "revisions": [
                            {
                                "revid": 55,
                                "timestamp": timestamp,
                                "slots": {"main": {"content": content}},
                            }
                        ],
                    }
                ]
            }
        }
    )


def test_get_revision_returns_content_and_the_conflict_baseline():
    wikitext = "'''སངས་རྒྱས་'''ནི།\n\n== ལུང་ཁུངས། ==\n<references />"
    session = make_session(get=[_revision_payload(wikitext, "2026-07-29T09:00:00Z")])
    client, _ = make_client(session)

    revision = client.get_revision(WITH_TSHEG)

    assert revision is not None
    assert revision.content == wikitext
    assert revision.timestamp == "2026-07-29T09:00:00Z"
    assert revision.revid == 55
    params = get_params(session)
    assert params["rvslots"] == "main"
    assert "content" in params["rvprop"] and "timestamp" in params["rvprop"]


def test_get_revision_preserves_tibetan_punctuation():
    wikitext = f"{WITH_TSHEG}{SHAD}"
    session = make_session(get=[_revision_payload(wikitext, "2026-07-29T09:00:00Z")])
    client, _ = make_client(session)

    content = client.get_revision(WITH_TSHEG).content
    assert content.endswith(SHAD)
    assert TSHEG in content
    assert content == unicodedata.normalize("NFC", wikitext)


def test_get_wikitext_returns_the_string_only():
    session = make_session(get=[_revision_payload("hello", "2026-07-29T09:00:00Z")])
    client, _ = make_client(session)
    assert client.get_wikitext(WITH_TSHEG) == "hello"


def test_get_wikitext_returns_none_for_a_missing_page():
    session = make_session(
        get=[FakeResponse({"query": {"pages": [{"title": WITH_TSHEG, "missing": True}]}})]
    )
    client, _ = make_client(session)
    assert client.get_wikitext(WITH_TSHEG) is None


def test_get_sections_parses_index_anchor_and_level():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "parse": {
                        "title": WITH_TSHEG,
                        "sections": [
                            {
                                "toclevel": 1,
                                "level": "2",
                                "line": "ངེས་ཚིག",
                                "number": "1",
                                "index": "1",
                                "anchor": "ངེས་ཚིག",
                                "byteoffset": 120,
                            },
                            {
                                "toclevel": 1,
                                "level": "2",
                                "line": "ལུང་ཁུངས།",
                                "number": "2",
                                "index": "",
                                "anchor": "ལུང་ཁུངས།",
                                "fromtitle": "Template:Refs",
                            },
                        ],
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    sections = client.get_sections(WITH_TSHEG)

    assert [s.index for s in sections] == ["1", ""]
    assert sections[0].level == 2
    assert sections[0].anchor == "ངེས་ཚིག"
    assert sections[0].editable is True
    # A transcluded section has no index and must never be edited in place.
    assert sections[1].editable is False


def test_get_sections_returns_empty_for_a_missing_page():
    session = make_session(get=[error_response("missingtitle", "does not exist")])
    client, _ = make_client(session)
    assert client.get_sections(WITH_TSHEG) == []


def test_get_sections_propagates_other_errors():
    session = make_session(get=[error_response("permissiondenied", "nope")])
    client, _ = make_client(session)
    with pytest.raises(NotAuthenticated):
        client.get_sections(WITH_TSHEG)


def test_search_returns_results_and_respects_limit():
    session = make_session(
        get=[
            FakeResponse(
                {
                    "query": {
                        "search": [
                            {
                                "ns": 0,
                                "title": WITH_SHAD,
                                "pageid": 12,
                                "size": 4096,
                                "wordcount": 300,
                                "snippet": "…",
                                "timestamp": "2026-01-01T00:00:00Z",
                            }
                        ]
                    }
                }
            )
        ]
    )
    client, _ = make_client(session)

    results = client.search("སངས་རྒྱས", limit=3)

    assert [r.title for r in results] == [WITH_SHAD]
    assert results[0].wordcount == 300
    params = get_params(session)
    assert params["srsearch"] == "སངས་རྒྱས"
    assert params["srlimit"] == 3
    assert params["list"] == "search"


def test_search_empty_result_is_an_empty_list():
    session = make_session(get=[FakeResponse({"query": {"search": []}})])
    client, _ = make_client(session)
    assert client.search("nothing") == []


# --------------------------------------------------------------------------
# Session ownership
# --------------------------------------------------------------------------


def test_injected_session_is_not_closed_by_the_client():
    session = make_session()
    with make_client(session)[0]:
        pass
    session.close.assert_not_called()


def test_owned_session_is_closed(monkeypatch):
    session = make_session()
    monkeypatch.setattr(requests, "Session", lambda: session)
    with WikiClient(sleep=SleepRecorder()):
        pass
    session.close.assert_called_once()
