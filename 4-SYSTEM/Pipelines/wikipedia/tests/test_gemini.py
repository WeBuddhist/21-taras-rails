"""Offline tests for the Gemini wrapper and the prompt library.

No network, no API key, no ``google.genai`` client is ever constructed against
a real endpoint: every test either injects a ``unittest.mock`` double or
patches ``genai.Client``.  Responses are built as *real*
``types.GenerateContentResponse`` objects rather than bare mocks, so the
extraction code is exercised against the shapes the SDK actually produces —
a MagicMock would happily answer any attribute and prove nothing.
"""

from __future__ import annotations

import json
import os
import random
import subprocess
import sys
import textwrap
import unicodedata
from pathlib import Path
from unittest import mock

import pytest
from google.genai import errors as genai_errors
from google.genai import types

from kangyur_wiki.llm import gemini as G

TSHEG = "་"
SHAD = "།"
TIBETAN_TERM = "བྱང་ཆུབ་སེམས" + TSHEG


# --------------------------------------------------------------------------
# Fixtures and builders
# --------------------------------------------------------------------------


def make_response(
    *,
    text: str | None = "ok",
    thought: str | None = None,
    finish_reason: str | None = "STOP",
    usage: dict | None = None,
    block_reason: str | None = None,
    safety_ratings: list[dict] | None = None,
    model_version: str = "gemini-3.5-flash",
    parsed: object | None = None,
) -> types.GenerateContentResponse:
    """A real SDK response object, populated the way the API populates one."""
    parts: list[dict] = []
    if thought is not None:
        parts.append({"text": thought, "thought": True})
    if text is not None:
        parts.append({"text": text})

    candidate: dict = {"content": {"role": "model", "parts": parts}}
    if finish_reason is not None:
        candidate["finish_reason"] = finish_reason
    if safety_ratings is not None:
        candidate["safety_ratings"] = safety_ratings

    payload: dict = {
        "candidates": [candidate],
        "model_version": model_version,
        "usage_metadata": usage
        or {
            "prompt_token_count": 120,
            "candidates_token_count": 40,
            "cached_content_token_count": 0,
            "thoughts_token_count": 0,
            "total_token_count": 160,
        },
    }
    if block_reason is not None:
        payload["prompt_feedback"] = {"block_reason": block_reason}

    response = types.GenerateContentResponse.model_validate(payload)
    if parsed is not None:
        response.parsed = parsed
    return response


def api_error(status: int, message: str = "boom") -> genai_errors.APIError:
    """A genai error with a realistic error body."""
    body = {"error": {"code": status, "message": message, "status": "ERROR"}}
    return (
        genai_errors.ClientError(status, body)
        if status < 500
        else genai_errors.ServerError(status, body)
    )


class Recorder:
    """A drop-in ``sleep`` that records instead of sleeping."""

    def __init__(self) -> None:
        self.delays: list[float] = []

    def __call__(self, seconds: float) -> None:
        self.delays.append(seconds)


@pytest.fixture
def fake_client() -> mock.MagicMock:
    client = mock.MagicMock(name="genai.Client")
    client.models.generate_content.return_value = make_response()
    client.models.count_tokens.return_value = types.CountTokensResponse(total_tokens=8192)
    client.caches.create.return_value = types.CachedContent(name="cachedContents/abc123")
    return client


@pytest.fixture
def sleeper() -> Recorder:
    return Recorder()


@pytest.fixture
def client(fake_client: mock.MagicMock, sleeper: Recorder) -> G.GeminiClient:
    return G.GeminiClient(
        client=fake_client,
        sleep=sleeper,
        rng=random.Random(0),  # deterministic jitter
    )


def last_config(fake_client: mock.MagicMock) -> types.GenerateContentConfig:
    return fake_client.models.generate_content.call_args.kwargs["config"]


# --------------------------------------------------------------------------
# Construction
# --------------------------------------------------------------------------


def test_missing_api_key_raises_and_names_the_env_var(monkeypatch):
    monkeypatch.delenv(G.ENV_API_KEY, raising=False)
    monkeypatch.delenv(G.ENV_API_KEY_FALLBACK, raising=False)

    with pytest.raises(G.MissingAPIKey) as excinfo:
        G.GeminiClient()

    assert "GEMINI_API_KEY" in str(excinfo.value)


def test_api_key_read_from_environment(monkeypatch):
    monkeypatch.setenv(G.ENV_API_KEY, "env-key")
    with mock.patch.object(G.genai, "Client") as constructor:
        G.GeminiClient()
    assert constructor.call_args.kwargs["api_key"] == "env-key"


def test_explicit_api_key_beats_the_environment(monkeypatch):
    monkeypatch.setenv(G.ENV_API_KEY, "env-key")
    with mock.patch.object(G.genai, "Client") as constructor:
        G.GeminiClient(api_key="explicit-key")
    assert constructor.call_args.kwargs["api_key"] == "explicit-key"


def test_timeout_is_seconds_here_and_milliseconds_on_the_wire(monkeypatch):
    monkeypatch.setenv(G.ENV_API_KEY, "env-key")
    with mock.patch.object(G.genai, "Client") as constructor:
        G.GeminiClient(timeout=30.0)
    assert constructor.call_args.kwargs["http_options"].timeout == 30_000


def test_injected_client_needs_no_key(monkeypatch, fake_client):
    monkeypatch.delenv(G.ENV_API_KEY, raising=False)
    monkeypatch.delenv(G.ENV_API_KEY_FALLBACK, raising=False)
    instance = G.GeminiClient(client=fake_client)
    assert instance.client is fake_client


def test_default_model_is_pinned_and_not_a_preview(client):
    assert client.model == "gemini-3.5-flash"
    assert "-preview" not in G.DEFAULT_MODEL


@pytest.mark.parametrize(
    "model", ["gemini-3.1-pro-preview", "gemini-2.5-flash", "gemini-3.1-flash-lite", ""]
)
def test_forbidden_models_rejected_at_construction(fake_client, model):
    with pytest.raises(ValueError):
        G.GeminiClient(client=fake_client, model=model)


# --------------------------------------------------------------------------
# generate()
# --------------------------------------------------------------------------


def test_generate_returns_text_usage_model_and_finish_reason(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        text=TIBETAN_TERM,
        usage={
            "prompt_token_count": 1000,
            "candidates_token_count": 200,
            "cached_content_token_count": 900,
            "thoughts_token_count": 50,
            "total_token_count": 1250,
        },
    )

    result = client.generate("hello")

    assert result.text == TIBETAN_TERM
    assert result.parsed is None
    assert result.model == "gemini-3.5-flash"
    assert result.finish_reason == "STOP"
    assert result.usage.input_tokens == 1000
    assert result.usage.output_tokens == 200
    assert result.usage.cached_tokens == 900
    assert result.usage.thought_tokens == 50
    assert result.usage.uncached_input_tokens == 100
    assert result.used_cache is True
    assert not result.blocked


def test_generate_sets_all_safety_categories_to_block_none_and_no_tools(client, fake_client):
    client.generate("hello")

    config = last_config(fake_client)
    categories = {setting.category for setting in config.safety_settings}
    assert categories == set(G.ADJUSTABLE_HARM_CATEGORIES)
    assert all(
        setting.threshold == types.HarmBlockThreshold.BLOCK_NONE
        for setting in config.safety_settings
    )
    # Google Search grounding activates purely by the presence of a tool.
    assert not config.tools


def test_safety_settings_can_be_overridden_per_call(client, fake_client):
    strict = G.default_safety_settings(types.HarmBlockThreshold.BLOCK_ONLY_HIGH)
    client.generate("hello", safety_settings=strict)
    thresholds = {s.threshold for s in last_config(fake_client).safety_settings}
    assert thresholds == {types.HarmBlockThreshold.BLOCK_ONLY_HIGH}


def test_system_instruction_and_temperature_are_passed(client, fake_client):
    client.generate("hello", system="be terse", temperature=0.7)
    config = last_config(fake_client)
    assert config.system_instruction == "be terse"
    assert config.temperature == 0.7


def test_temperature_none_omits_the_field(client, fake_client):
    client.generate("hello", temperature=None)
    assert last_config(fake_client).temperature is None


def test_prompt_is_nfc_normalised_before_sending(client, fake_client):
    # U+0F77 is a composition exclusion: NFC decomposes it.
    client.generate("ཷ" + TSHEG)
    sent = fake_client.models.generate_content.call_args.kwargs["contents"]
    assert sent == unicodedata.normalize("NFC", "ཷ" + TSHEG)
    assert sent.endswith(TSHEG)  # punctuation survives normalisation


def test_empty_prompt_rejected(client):
    with pytest.raises(ValueError):
        client.generate("   ")


def test_thought_parts_are_not_returned_as_article_text(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        thought="let me reason about this", text="final answer"
    )
    assert client.generate("hello").text == "final answer"


def test_max_tokens_is_reported_as_truncated(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        finish_reason="MAX_TOKENS"
    )
    result = client.generate("hello")
    assert result.truncated is True
    assert not result.blocked


# --------------------------------------------------------------------------
# Structured output
# --------------------------------------------------------------------------


def test_schema_sets_json_mime_type_and_schema(client, fake_client):
    schema = {"type": "object", "properties": {"term": {"type": "string"}}}
    fake_client.models.generate_content.return_value = make_response(
        text=json.dumps({"term": TIBETAN_TERM}, ensure_ascii=False)
    )

    result = client.generate("hello", schema=schema)

    config = last_config(fake_client)
    assert config.response_mime_type == "application/json"
    assert config.response_schema == schema
    assert result.parsed == {"term": TIBETAN_TERM}


def test_no_schema_leaves_json_config_unset(client, fake_client):
    client.generate("hello")
    assert last_config(fake_client).response_mime_type is None


def test_schema_prefers_the_sdk_parsed_object(client, fake_client):
    sentinel = {"already": "parsed"}
    fake_client.models.generate_content.return_value = make_response(
        text="{}", parsed=sentinel
    )
    assert client.generate("hello", schema={"type": "object"}).parsed == sentinel


def test_schema_tolerates_a_json_code_fence(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        text='```json\n{"term": "a"}\n```'
    )
    assert client.generate("hello", schema={"type": "object"}).parsed == {"term": "a"}


def test_schema_with_unparseable_json_raises(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(text="not json at all")
    with pytest.raises(G.StructuredOutputError):
        client.generate("hello", schema={"type": "object"})


def test_truncated_json_error_says_so(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        text='{"term": "unfin', finish_reason="MAX_TOKENS"
    )
    with pytest.raises(G.StructuredOutputError, match="MAX_TOKENS"):
        client.generate("hello", schema={"type": "object"})


def test_schema_with_empty_response_raises(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(text=None)
    with pytest.raises(G.StructuredOutputError):
        client.generate("hello", schema={"type": "object"})


# --------------------------------------------------------------------------
# Safety blocks
# --------------------------------------------------------------------------


def test_safety_finish_reason_raises_and_carries_the_ratings(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        text=None,
        finish_reason="SAFETY",
        safety_ratings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "probability": "HIGH", "blocked": True}
        ],
    )

    with pytest.raises(G.ResponseBlocked) as excinfo:
        client.generate("wrathful deity iconography")

    result = excinfo.value.result
    assert result.blocked is True
    assert result.finish_reason == "SAFETY"
    assert result.safety_ratings[0]["category"] == "HARM_CATEGORY_HARASSMENT"


def test_blocked_prompt_raises(client, fake_client):
    fake_client.models.generate_content.return_value = make_response(
        text=None, finish_reason=None, block_reason="SAFETY"
    )
    with pytest.raises(G.ResponseBlocked) as excinfo:
        client.generate("hello")
    assert excinfo.value.result.block_reason == "SAFETY"


# --------------------------------------------------------------------------
# Caching
# --------------------------------------------------------------------------


def test_cache_name_is_passed_as_cached_content(client, fake_client):
    client.generate("hello", cache="cachedContents/abc123")
    assert last_config(fake_client).cached_content == "cachedContents/abc123"


def test_system_with_cache_is_refused(client):
    with pytest.raises(ValueError, match="create_cache"):
        client.generate("hello", system="be terse", cache="cachedContents/abc123")


def test_create_cache_returns_the_cache_name(client, fake_client):
    name = client.create_cache(["corpus"], "bca-commentaries-v1", ttl_seconds=21600)

    assert name == "cachedContents/abc123"
    config = fake_client.caches.create.call_args.kwargs["config"]
    assert fake_client.caches.create.call_args.kwargs["model"] == "gemini-3.5-flash"
    assert config.display_name == "bca-commentaries-v1"
    assert config.ttl == "21600s"


def test_create_cache_carries_the_system_instruction(client, fake_client):
    client.create_cache("corpus", "d", system_instruction="cite every claim")
    config = fake_client.caches.create.call_args.kwargs["config"]
    assert config.system_instruction == "cite every claim"


def test_create_cache_skips_the_api_when_corpus_is_below_the_minimum(client, fake_client):
    fake_client.models.count_tokens.return_value = types.CountTokensResponse(total_tokens=10)

    assert client.create_cache("tiny", "tiny-corpus") is None
    fake_client.caches.create.assert_not_called()


def test_create_cache_degrades_when_the_api_calls_it_too_small(client, fake_client):
    fake_client.caches.create.side_effect = api_error(
        400, "Cached content is too small. total_token_count=99, min_total_token_count=4096"
    )

    assert client.create_cache("corpus", "small-corpus") is None


def test_create_cache_reraises_other_400s(client, fake_client):
    fake_client.caches.create.side_effect = api_error(400, "Invalid model name")

    with pytest.raises(G.GeminiAPIError):
        client.create_cache("corpus", "broken")


def test_create_cache_requires_a_display_name(client):
    with pytest.raises(ValueError):
        client.create_cache("corpus", "  ")


def test_create_cache_requires_content(client):
    with pytest.raises(ValueError):
        client.create_cache([], "empty")


def test_delete_cache(client, fake_client):
    assert client.delete_cache("cachedContents/abc123") is True
    fake_client.caches.delete.assert_called_once_with(name="cachedContents/abc123")


def test_delete_cache_of_none_is_a_no_op(client, fake_client):
    assert client.delete_cache(None) is False
    fake_client.caches.delete.assert_not_called()


def test_delete_cache_never_raises_from_a_finally_block(client, fake_client):
    fake_client.caches.delete.side_effect = api_error(404, "not found")
    assert client.delete_cache("cachedContents/gone") is False


# --------------------------------------------------------------------------
# Retries
# --------------------------------------------------------------------------


def test_retry_on_429_then_success(client, fake_client, sleeper):
    fake_client.models.generate_content.side_effect = [
        api_error(429, "rate limited"),
        make_response(text="second time lucky"),
    ]

    result = client.generate("hello")

    assert result.text == "second time lucky"
    assert fake_client.models.generate_content.call_count == 2
    assert len(sleeper.delays) == 1
    assert 0.5 <= sleeper.delays[0] <= 1.0


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
def test_all_retryable_statuses_are_retried(fake_client, sleeper, status):
    instance = G.GeminiClient(client=fake_client, sleep=sleeper, rng=random.Random(0))
    fake_client.models.generate_content.side_effect = [api_error(status), make_response()]

    instance.generate("hello")

    assert fake_client.models.generate_content.call_count == 2


def test_400_is_never_retried(client, fake_client, sleeper):
    fake_client.models.generate_content.side_effect = api_error(400, "bad request")

    with pytest.raises(G.GeminiAPIError) as excinfo:
        client.generate("hello")

    assert excinfo.value.status_code == 400
    assert fake_client.models.generate_content.call_count == 1
    assert sleeper.delays == []


@pytest.mark.parametrize("status", [401, 403, 404])
def test_other_client_errors_are_never_retried(fake_client, sleeper, status):
    instance = G.GeminiClient(client=fake_client, sleep=sleeper, rng=random.Random(0))
    fake_client.models.generate_content.side_effect = api_error(status)

    with pytest.raises(G.GeminiAPIError):
        instance.generate("hello")

    assert fake_client.models.generate_content.call_count == 1


def test_transient_socket_errors_are_retried(client, fake_client, sleeper):
    fake_client.models.generate_content.side_effect = [
        ConnectionResetError("connection reset by peer"),
        TimeoutError("read timed out"),
        make_response(text="third time"),
    ]

    assert client.generate("hello").text == "third time"
    assert len(sleeper.delays) == 2


def test_retries_are_bounded_and_then_it_gives_up(fake_client, sleeper):
    instance = G.GeminiClient(
        client=fake_client, max_retries=3, sleep=sleeper, rng=random.Random(0)
    )
    fake_client.models.generate_content.side_effect = api_error(503, "overloaded")

    with pytest.raises(G.GeminiAPIError, match="3 attempts"):
        instance.generate("hello")

    assert fake_client.models.generate_content.call_count == 3
    assert len(sleeper.delays) == 2  # no sleep after the final attempt


def test_backoff_grows_exponentially_and_stays_capped(fake_client, sleeper):
    instance = G.GeminiClient(
        client=fake_client, max_retries=8, sleep=sleeper, rng=random.Random(1)
    )
    fake_client.models.generate_content.side_effect = api_error(503)

    with pytest.raises(G.GeminiAPIError):
        instance.generate("hello")

    for attempt, delay in enumerate(sleeper.delays):
        ceiling = min(G._BACKOFF_CAP, G._BACKOFF_BASE * (2**attempt))
        assert ceiling / 2 <= delay <= ceiling
    assert max(sleeper.delays) <= G._BACKOFF_CAP
    # Jitter must actually vary, or a fleet of workers re-synchronises.
    assert len(set(sleeper.delays)) == len(sleeper.delays)


def test_count_tokens_is_retried_too(client, fake_client, sleeper):
    fake_client.models.count_tokens.side_effect = [
        api_error(429),
        types.CountTokensResponse(total_tokens=42),
    ]
    assert client.count_tokens("hello") == 42
    assert len(sleeper.delays) == 1


# --------------------------------------------------------------------------
# count_tokens
# --------------------------------------------------------------------------


def test_count_tokens_uses_the_pinned_model(client, fake_client):
    assert client.count_tokens(TIBETAN_TERM) == 8192
    kwargs = fake_client.models.count_tokens.call_args.kwargs
    assert kwargs["model"] == "gemini-3.5-flash"
    assert kwargs["contents"] == unicodedata.normalize("NFC", TIBETAN_TERM)


def test_count_tokens_of_empty_string_is_free(client, fake_client):
    assert client.count_tokens("") == 0
    fake_client.models.count_tokens.assert_not_called()


def test_count_tokens_rejects_non_strings(client):
    with pytest.raises(TypeError):
        client.count_tokens(None)  # type: ignore[arg-type]


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------


def test_parse_front_matter_splits_yaml_from_body():
    meta, body = G.parse_front_matter("---\nname: x\nversion: 2\n---\nBODY\nMORE\n")
    assert meta == {"name": "x", "version": 2}
    assert body == "BODY\nMORE\n"


def test_parse_front_matter_absent_returns_whole_text():
    meta, body = G.parse_front_matter("no front matter here")
    assert meta == {}
    assert body == "no front matter here"


def test_parse_front_matter_unclosed_raises():
    with pytest.raises(G.PromptError, match="never closed"):
        G.parse_front_matter("---\nname: x\nBODY")


def test_parse_front_matter_invalid_yaml_raises():
    with pytest.raises(G.PromptError):
        G.parse_front_matter("---\nname: [unclosed\n---\nBODY")


def test_parse_front_matter_non_mapping_raises():
    with pytest.raises(G.PromptError, match="mapping"):
        G.parse_front_matter("---\n- a\n- b\n---\nBODY")


def test_template_variables_finds_both_syntaxes():
    assert G.template_variables("$a and ${b} and $a again") == ("a", "b")


def test_template_variables_ignores_json_braces():
    assert G.template_variables('{"term": "x"} $term') == ("term",)


# --------------------------------------------------------------------------
# PromptLibrary
# --------------------------------------------------------------------------


def write_prompt(root: Path, stage: str, filename: str, front: str, body: str) -> Path:
    directory = root / stage
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / filename
    path.write_text(f"---\n{textwrap.dedent(front).strip()}\n---\n{body}", encoding="utf-8")
    return path


@pytest.fixture
def library(tmp_path: Path) -> G.PromptLibrary:
    write_prompt(
        tmp_path,
        "06-draft",
        "v1-forum-324.md",
        """
        name: article-draft
        version: 1
        stage: 06-draft
        source: forum-topic-324
        model_tested: claude-opus-4
        variables: [term]
        """,
        f"old prompt for $term{SHAD}\n",
    )
    write_prompt(
        tmp_path,
        "06-draft",
        "v2-canonical.md",
        """
        name: article-draft-canonical
        version: 2
        stage: 06-draft
        model_tested: none
        variables: [term, sections_json]
        """,
        'Write about $term. Emit JSON like {"term": "...", "refs": []}.\n\n$sections_json\n',
    )
    write_prompt(
        tmp_path,
        "03-terms",
        "v1.md",
        """
        name: key-term-extraction
        version: 1
        stage: 03-terms
        variables: [root_text]
        """,
        "$root_text\n",
    )
    return G.PromptLibrary(tmp_path)


def test_library_loads_every_prompt(library):
    assert len(library) == 3
    assert library.stages == ("03-terms", "06-draft")


def test_library_get_latest_picks_the_highest_version(library):
    assert library.get("06-draft").version == 2


def test_library_get_specific_version(library):
    for wanted in (1, "1", "v1"):
        assert library.get("06-draft", wanted).name == "article-draft"


def test_library_stage_aliases(library):
    assert library.get("draft").version == 2
    assert library.get("06").version == 2
    assert library.get("6").version == 2


def test_library_unknown_stage_lists_what_exists(library):
    with pytest.raises(G.PromptError, match="06-draft"):
        library.get("99-nope")


def test_library_unknown_version_lists_what_exists(library):
    with pytest.raises(G.PromptError, match="1, 2"):
        library.get("06-draft", 7)


def test_library_all_versions_oldest_first(library):
    assert [p.version for p in library.all("06-draft")] == [1, 2]


def test_library_exposes_provenance(library):
    prompt = library.get("06-draft", 1)
    assert prompt.meta["source"] == "forum-topic-324"
    assert prompt.model_tested == "claude-opus-4"


def test_duplicate_version_in_one_stage_is_a_hard_error(tmp_path):
    write_prompt(tmp_path, "06-draft", "a.md", "name: a\nversion: 1\n", "$term\n")
    write_prompt(tmp_path, "06-draft", "b.md", "name: b\nversion: 1\n", "$term\n")
    with pytest.raises(G.PromptError, match="duplicate version"):
        G.PromptLibrary(tmp_path)


def test_prompt_without_front_matter_is_rejected(tmp_path):
    (tmp_path / "06-draft").mkdir(parents=True)
    (tmp_path / "06-draft" / "raw.md").write_text("just prose", encoding="utf-8")
    with pytest.raises(G.PromptError, match="front matter"):
        G.PromptLibrary(tmp_path)


def test_prompt_with_empty_body_is_rejected(tmp_path):
    write_prompt(tmp_path, "06-draft", "v1.md", "name: a\nversion: 1\n", "\n\n")
    with pytest.raises(G.PromptError, match="body is empty"):
        G.PromptLibrary(tmp_path)


def test_stage_falls_back_to_the_directory_name(tmp_path):
    write_prompt(tmp_path, "04-extract", "v1.md", "name: a\nversion: 1\n", "$term\n")
    assert G.PromptLibrary(tmp_path).get("04-extract").stage == "04-extract"


def test_bad_version_in_front_matter_is_rejected(tmp_path):
    write_prompt(tmp_path, "06-draft", "v1.md", "name: a\nversion: draft-two\n", "$term\n")
    with pytest.raises(G.PromptError, match="version"):
        G.PromptLibrary(tmp_path)


def test_missing_prompt_root_is_rejected(tmp_path):
    with pytest.raises(G.PromptError, match="not a directory"):
        G.PromptLibrary(tmp_path / "nope")


# --------------------------------------------------------------------------
# Prompt.render
# --------------------------------------------------------------------------


def test_render_substitutes_dollar_placeholders(library):
    rendered = library.get("06-draft", 1).render(term=TIBETAN_TERM)
    assert TIBETAN_TERM in rendered
    assert "$term" not in rendered


def test_render_leaves_literal_json_braces_alone(library):
    rendered = library.get("06-draft").render(term="x", sections_json="[]")
    assert '{"term": "...", "refs": []}' in rendered


def test_render_preserves_tibetan_punctuation(library):
    rendered = library.get("06-draft", 1).render(term=TIBETAN_TERM)
    assert rendered.endswith(SHAD + "\n")
    assert TSHEG in rendered


def test_render_output_is_nfc(library):
    rendered = library.get("06-draft", 1).render(term="ཷ")
    assert rendered == unicodedata.normalize("NFC", rendered)


def test_render_missing_variable_names_it(library):
    with pytest.raises(G.PromptError, match="sections_json"):
        library.get("06-draft").render(term="x")


def test_render_none_value_is_rejected(library):
    with pytest.raises(G.PromptError, match="term"):
        library.get("06-draft", 1).render(term=None)


def test_render_serialises_structured_values(tmp_path):
    write_prompt(tmp_path, "05-organize", "v1.md", "name: a\nversion: 1\n", "$payload")
    rendered = G.PromptLibrary(tmp_path).get("05-organize").render(
        payload={"term": TIBETAN_TERM, "n": 2}
    )
    assert TIBETAN_TERM in rendered  # ensure_ascii=False keeps Tibetan readable
    assert json.loads(rendered)["n"] == 2


def test_render_escaped_dollar_and_stray_dollar_survive(tmp_path):
    write_prompt(
        tmp_path, "05-organize", "v1.md", "name: a\nversion: 1\n", "$$5 and $ and $term"
    )
    rendered = G.PromptLibrary(tmp_path).get("05-organize").render(term="X")
    assert rendered == "$5 and $ and X"


def test_render_extra_kwargs_are_ignored_not_fatal(library):
    assert library.get("06-draft", 1).render(term="x", unused="y") == "old prompt for x" + SHAD + "\n"


def test_library_render_shortcut(library):
    assert "x" in library.render("06-draft", 1, term="x")


def test_validate_flags_declared_variable_drift(tmp_path):
    write_prompt(
        tmp_path,
        "06-draft",
        "v1.md",
        "name: a\nversion: 1\nvariables: [term, gone]\n",
        "$term and $surprise\n",
    )
    problems = G.PromptLibrary(tmp_path).validate()
    assert len(problems) == 1
    assert "gone" in problems[0] and "surprise" in problems[0]


def test_validate_is_quiet_on_a_consistent_library(library):
    assert library.validate() == []


# --------------------------------------------------------------------------
# The prompts actually in this repo
# --------------------------------------------------------------------------

REPO_PROMPTS = G.default_prompt_root()


@pytest.mark.skipif(not REPO_PROMPTS.is_dir(), reason="repo prompts/ directory not present")
def test_repo_prompts_all_load_and_are_self_consistent():
    library = G.PromptLibrary(REPO_PROMPTS)
    assert len(library) > 0
    assert library.validate() == []


@pytest.mark.skipif(not REPO_PROMPTS.is_dir(), reason="repo prompts/ directory not present")
def test_repo_prompts_render_with_their_declared_variables():
    library = G.PromptLibrary(REPO_PROMPTS)
    for prompt in library:
        rendered = prompt.render(**{name: "PLACEHOLDER" for name in prompt.variables})
        assert "$" not in rendered.replace("$$", "")


# --------------------------------------------------------------------------
# House rule: importable with no key and no network
# --------------------------------------------------------------------------


def test_module_imports_without_an_api_key():
    """A stage that never calls Gemini must still be importable on a laptop
    with no credentials — checked in a clean subprocess, because this process
    has already imported the module."""
    src = str(Path(__file__).resolve().parents[1] / "src")
    env = {k: v for k, v in os.environ.items() if k not in (G.ENV_API_KEY, G.ENV_API_KEY_FALLBACK)}
    env["PYTHONPATH"] = src
    completed = subprocess.run(
        [sys.executable, "-c", "import kangyur_wiki.llm.gemini as m; print(m.DEFAULT_MODEL)"],
        capture_output=True,
        text=True,
        env=env,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.strip() == "gemini-3.5-flash"
