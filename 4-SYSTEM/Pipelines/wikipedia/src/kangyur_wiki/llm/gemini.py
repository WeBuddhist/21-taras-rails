"""The one place this repo talks to Gemini.

Every LLM call in the pipeline goes through :class:`GeminiClient`.  That is a
deliberate choke point, not a style preference: the Interactions API is now
Google's front door, but explicit context caching, the Batch API *and*
configurable safety settings are all legacy-``generateContent``-only features,
and this project needs all three (PLAN.md §5).  When Interactions eventually
gains them, the migration is one file.

Three decisions here cost real money or real correctness if they drift, so they
are constants rather than call sites:

* **The model is pinned** (:data:`DEFAULT_MODEL`).  A silent bump to a
  ``-preview`` id would invalidate every golden-file test and every number in
  the paper.  Preview and retired ids are rejected outright.
* **Explicit caching is the cost lever.**  The commentary corpus is identical
  for every term in a run; resending it per term costs ~$90 where a cache
  costs ~$11 (research/reports/r-gemini-api.md §4).  Caching is therefore a
  first-class method, not an optimisation to add later.
* **Safety thresholds are set explicitly.**  Tibetan Buddhist commentary
  carries wrathful-deity iconography, tīrthika polemic, tantric sexual
  symbolism and Vinaya transgression lists — all plausible false-positive
  triggers.  Relying on a permissive *default* means the day Google tightens
  it, articles start silently coming back empty.

Nothing in this module touches the network at import time, and it imports
without ``GEMINI_API_KEY`` set — only :meth:`GeminiClient.__init__` needs one,
and only when no pre-built client is injected.

Tools are never passed to the model.  Google Search grounding activates purely
by the presence of the tool, and web content must not leak into an article
whose whole claim to credibility is that every sentence is sourced to a named
Tibetan commentary.
"""

from __future__ import annotations

import json
import logging
import os
import random
import re
import string
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence, TypeVar

import yaml
from google import genai
from google.genai import errors as genai_errors
from google.genai import types

__all__ = [
    "DEFAULT_MODEL",
    "ENV_API_KEY",
    "ENV_API_KEY_FALLBACK",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CACHE_TTL_SECONDS",
    "MIN_CACHE_TOKENS",
    "RETRYABLE_STATUS_CODES",
    "ADJUSTABLE_HARM_CATEGORIES",
    "GeminiError",
    "MissingAPIKey",
    "GeminiAPIError",
    "ResponseBlocked",
    "StructuredOutputError",
    "PromptError",
    "Usage",
    "GenResult",
    "GeminiClient",
    "Prompt",
    "PromptLibrary",
    "default_safety_settings",
    "default_prompt_root",
    "parse_front_matter",
    "template_variables",
]

logger = logging.getLogger(__name__)

T = TypeVar("T")

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

#: The pinned production model.  Chosen over ``gemini-3.6-flash`` because 3.6
#: is tuned for code and agentic execution while 3.5 is the stronger general
#: reasoner, and a plausible-but-wrong Tibetan doctrinal sentence is the
#: expensive failure here.  Never a ``-preview`` id: preview models change
#: under you and are not covered by any deprecation notice period.
DEFAULT_MODEL = "gemini-3.5-flash"

#: Cheap model for mechanical passes (term extraction, classification).
#: Exposed so callers name a constant instead of a string literal.
LITE_MODEL = "gemini-3.5-flash-lite"

ENV_API_KEY = "GEMINI_API_KEY"
#: The SDK also honours this one; we read it as a fallback but error messages
#: always name ``GEMINI_API_KEY`` because that is what ``.env.example`` says.
ENV_API_KEY_FALLBACK = "GOOGLE_API_KEY"

#: Seconds.  Long, because a 300k-token cached corpus plus high thinking level
#: on a drafting call is genuinely slow; a short timeout here manifests as
#: mysterious retry storms rather than as an obvious error.
DEFAULT_TIMEOUT = 120.0

DEFAULT_MAX_RETRIES = 5
DEFAULT_CACHE_TTL_SECONDS = 3600

#: Minimum input tokens before Gemini 3.5 Flash will build an explicit cache.
#: Below this the API refuses, which is why :meth:`GeminiClient.create_cache`
#: degrades to "no cache" instead of failing the run.
MIN_CACHE_TOKENS = 4096

#: HTTP statuses worth trying again.  400 is deliberately absent: a malformed
#: request is malformed on the fifth attempt too, and retrying it just burns
#: wall-clock time before the same failure.
RETRYABLE_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})

#: Equal-jitter backoff bounds, in seconds.  Bounded so a run cannot stall for
#: an unbounded time on a wedged endpoint.
_BACKOFF_BASE = 1.0
_BACKOFF_CAP = 32.0

#: Model ids we refuse to talk to.  ``gemini-2.5-*`` is scheduled for shutdown
#: from 2026-10-16 and ``gemini-3.1-flash-lite`` is deprecated; both would fail
#: mid-run rather than at startup, which is the worst time to find out.
_FORBIDDEN_MODEL_PREFIXES = ("gemini-2.5", "gemini-2.0", "gemini-1.5")
_FORBIDDEN_MODEL_IDS = frozenset({"gemini-3.1-flash-lite"})

#: The four adjustable *text* harm categories.  The IMAGE_* and JAILBREAK
#: categories are omitted on purpose: this is a text-only pipeline, and sending
#: a category the endpoint does not accept turns every call into a 400.
ADJUSTABLE_HARM_CATEGORIES: tuple[types.HarmCategory, ...] = (
    types.HarmCategory.HARM_CATEGORY_HARASSMENT,
    types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
)

#: ``finish_reason`` values that mean the model produced nothing usable.
_BLOCKING_FINISH_REASONS = frozenset(
    {"SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII", "RECITATION", "IMAGE_SAFETY"}
)

#: Transient transport failures.  ``OSError`` covers ``ConnectionError``,
#: ``socket.timeout`` and ``socket.gaierror``; the SDK's httpx transport raises
#: its own hierarchy, added below when importable.
_TRANSIENT_ERRORS: tuple[type[BaseException], ...] = (OSError, TimeoutError)
try:  # pragma: no cover - httpx ships with google-genai, but guard anyway
    import httpx as _httpx

    _TRANSIENT_ERRORS = _TRANSIENT_ERRORS + (_httpx.TransportError,)
except Exception:  # pragma: no cover
    pass

#: A 400 from ``caches.create`` that matches this is "your corpus is too small
#: to cache", which is a degradable condition rather than a bug.
_CACHE_TOO_SMALL = re.compile(
    r"(minimum|too small|too few|at least|smaller than).{0,80}token"
    r"|token.{0,80}(minimum|too small|too few|at least)",
    re.IGNORECASE | re.DOTALL,
)

_CODE_FENCE = re.compile(r"^\s*```(?:json|JSON)?\s*\n(?P<body>.*?)\n?\s*```\s*$", re.DOTALL)


# --------------------------------------------------------------------------
# Exceptions
# --------------------------------------------------------------------------


class GeminiError(RuntimeError):
    """Base class for every failure this module raises."""


class MissingAPIKey(GeminiError):
    """No API key was supplied and none is in the environment."""


class GeminiAPIError(GeminiError):
    """The API refused, or kept refusing until the retry budget ran out.

    Carries ``status_code`` so callers (and :meth:`GeminiClient.create_cache`)
    can distinguish "malformed request" from "cluster is busy" without parsing
    strings.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        attempts: int = 1,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.attempts = attempts


class ResponseBlocked(GeminiError):
    """A safety filter blocked the prompt or the response.

    Raised rather than returned as an empty string, because a silent ``None``
    in a batch of 200 articles is exactly the failure that goes unnoticed until
    publication.  ``result`` carries the full :class:`GenResult` — including
    the safety ratings — so the caller can log the triggering passage.  Every
    block on a canonical Buddhist text is a data point for the paper.
    """

    def __init__(self, message: str, *, result: "GenResult") -> None:
        super().__init__(message)
        self.result = result


class StructuredOutputError(GeminiError):
    """``schema=`` was requested but the response was not parseable JSON."""


class PromptError(RuntimeError):
    """A prompt file is malformed, missing, or rendered with bad arguments."""


# --------------------------------------------------------------------------
# Pure helpers
# --------------------------------------------------------------------------


def _nfc(text: str) -> str:
    """NFC-normalise.  Tibetan comparison is meaningless without it."""
    return unicodedata.normalize("NFC", text)


def default_safety_settings(
    threshold: str = types.HarmBlockThreshold.BLOCK_NONE,
) -> list[types.SafetySetting]:
    """All four adjustable text harm categories at ``threshold``.

    Explicit beats implicit here even though Gemini 3's documented default is
    already permissive: defaults change without a migration notice, and an
    article that comes back empty because a threshold moved is indistinguishable
    from a model that simply had nothing to say.
    """
    return [
        types.SafetySetting(category=category, threshold=threshold)
        for category in ADJUSTABLE_HARM_CATEGORIES
    ]


def _validate_model(model: str) -> str:
    """Reject preview, retired and deprecated ids at construction time.

    Failing here costs a second; failing 40 articles into a batch run costs the
    run.
    """
    name = (model or "").strip()
    if not name:
        raise ValueError("model must be a non-empty model id")
    if "-preview" in name:
        raise ValueError(
            f"refusing preview model {name!r}: preview ids change without notice "
            f"and invalidate every golden-file test — pin {DEFAULT_MODEL!r}"
        )
    if name in _FORBIDDEN_MODEL_IDS:
        raise ValueError(f"model {name!r} is deprecated — use {DEFAULT_MODEL!r}")
    for prefix in _FORBIDDEN_MODEL_PREFIXES:
        if name.startswith(prefix):
            raise ValueError(
                f"model {name!r} is scheduled for shutdown — use {DEFAULT_MODEL!r}"
            )
    return name


def _status_code(exc: BaseException) -> int | None:
    """HTTP status off a genai error, whatever attribute it landed on."""
    for attribute in ("code", "status_code"):
        value = getattr(exc, attribute, None)
        if isinstance(value, int):
            return value
    return None


def _enum_value(value: Any) -> str | None:
    """``FinishReason.STOP`` -> ``'STOP'``; passthrough for plain strings."""
    if value is None:
        return None
    inner = getattr(value, "value", None)
    if isinstance(inner, str):
        return inner
    if isinstance(value, str):
        return value
    return str(value)


def _as_dict(value: Any) -> dict[str, Any]:
    """Best-effort plain-dict view of a pydantic model, for logging/JSON."""
    dump = getattr(value, "model_dump", None)
    if callable(dump):
        try:
            return {k: _enum_value(v) if hasattr(v, "value") else v for k, v in dump().items()}
        except Exception:  # pragma: no cover - defensive
            pass
    if isinstance(value, Mapping):
        return dict(value)
    return {"value": str(value)}


def _response_text(response: Any) -> str:
    """Concatenate the visible text parts of a response.

    Parts are walked directly rather than reading ``response.text`` first for
    two reasons: ``.text`` warns (or returns ``None``) on multi-part responses,
    and thinking parts must be dropped — a chain-of-thought fragment landing in
    a Wikipedia article is the exact "leftover model chatter" the validator
    exists to reject (wikitext-spec.md §7, V12).
    """
    chunks: list[str] = []
    for candidate in getattr(response, "candidates", None) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", None) or []:
            if getattr(part, "thought", False):
                continue
            text = getattr(part, "text", None)
            if isinstance(text, str) and text:
                chunks.append(text)
    if chunks:
        return "".join(chunks)
    fallback = getattr(response, "text", None)
    return fallback if isinstance(fallback, str) else ""


def _strip_code_fence(text: str) -> str:
    """Unwrap a ```json fence.

    ``response_mime_type='application/json'`` normally prevents fencing, but a
    single fenced response failing an otherwise-good 200-article batch is a bad
    trade against three lines of tolerance.
    """
    match = _CODE_FENCE.match(text)
    return match.group("body") if match else text


def template_variables(body: str) -> tuple[str, ...]:
    """Placeholder names in ``body``, in first-appearance order.

    Implemented against :attr:`string.Template.pattern` rather than
    ``Template.get_identifiers`` because that method is 3.11+ and this repo
    targets 3.10.
    """
    template = string.Template(body)
    seen: dict[str, None] = {}
    for match in template.pattern.finditer(template.template):
        name = match.group("named") or match.group("braced")
        if name:
            seen.setdefault(name, None)
    return tuple(seen)


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Split ``---\\nYAML\\n---\\nBODY`` into its two halves.

    Returns ``({}, text)`` when there is no front matter at all; raises when
    front matter is *opened and not closed*, because that is a corrupt file
    rather than a plain-markdown one.
    """
    stripped = text.lstrip("﻿")
    if not stripped.startswith("---"):
        return {}, text

    lines = stripped.splitlines(keepends=True)
    if lines[0].strip() != "---":
        return {}, text

    for index in range(1, len(lines)):
        if lines[index].strip() in ("---", "..."):
            raw = "".join(lines[1:index])
            body = "".join(lines[index + 1 :])
            try:
                meta = yaml.safe_load(raw) if raw.strip() else {}
            except yaml.YAMLError as exc:
                raise PromptError(f"invalid YAML front matter: {exc}") from exc
            if meta is None:
                meta = {}
            if not isinstance(meta, Mapping):
                raise PromptError(
                    f"front matter must be a YAML mapping, got {type(meta).__name__}"
                )
            return dict(meta), body.lstrip("\n")

    raise PromptError("front matter opened with '---' but never closed")


def default_prompt_root() -> Path:
    """``<repo>/prompts``, derived from this file's location.

    A path computation, not a filesystem read — importing this module still
    touches no disk.
    """
    return Path(__file__).resolve().parents[3] / "prompts"


# --------------------------------------------------------------------------
# Value objects
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Usage:
    """Token counts for one call.

    ``cached_tokens`` is the number that decides whether the run costs $11 or
    $97, so it is surfaced as a first-class field rather than left buried in
    ``usage_metadata``: a refactor that silently breaks cache hits is invisible
    in output quality and obvious in this number.
    """

    input_tokens: int = 0
    output_tokens: int = 0
    cached_tokens: int = 0
    thought_tokens: int = 0
    total_tokens: int = 0

    @property
    def uncached_input_tokens(self) -> int:
        """Input tokens billed at full rate (10x the cached rate)."""
        return max(0, self.input_tokens - self.cached_tokens)

    @classmethod
    def from_metadata(cls, metadata: Any) -> "Usage":
        if metadata is None:
            return cls()

        def read(name: str) -> int:
            value = getattr(metadata, name, None)
            return int(value) if isinstance(value, (int, float)) else 0

        return cls(
            input_tokens=read("prompt_token_count"),
            output_tokens=read("candidates_token_count"),
            cached_tokens=read("cached_content_token_count"),
            thought_tokens=read("thoughts_token_count"),
            total_tokens=read("total_token_count"),
        )


@dataclass(frozen=True)
class GenResult:
    """One generation, with everything needed to audit it afterwards.

    ``parsed`` is populated only when ``schema=`` was passed.  ``finish_reason``
    and ``safety_ratings`` are kept even on success because ``MAX_TOKENS`` is a
    silent truncation: valid-looking prose that stops mid-argument.
    """

    text: str
    parsed: Any | None
    usage: Usage
    model: str
    finish_reason: str | None
    cache_name: str | None = None
    block_reason: str | None = None
    safety_ratings: tuple[Mapping[str, Any], ...] = ()

    @property
    def blocked(self) -> bool:
        return bool(self.block_reason) or (self.finish_reason in _BLOCKING_FINISH_REASONS)

    @property
    def truncated(self) -> bool:
        """Hit the output cap — the text is real but incomplete."""
        return self.finish_reason == "MAX_TOKENS"

    @property
    def used_cache(self) -> bool:
        return self.usage.cached_tokens > 0


# --------------------------------------------------------------------------
# Client
# --------------------------------------------------------------------------


class GeminiClient:
    """Wrapper over ``client.models.generate_content`` and ``client.caches``.

    ``sleep`` and ``rng`` are injectable so the retry path is testable without
    a five-attempt exponential wait; nothing else about them is configurable
    on purpose.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str = DEFAULT_MODEL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        *,
        client: Any | None = None,
        safety_settings: Sequence[types.SafetySetting] | None = None,
        sleep: Callable[[float], None] = time.sleep,
        rng: random.Random | None = None,
    ) -> None:
        self.model = _validate_model(model)
        self.timeout = float(timeout)
        self.max_retries = max(1, int(max_retries))
        self.safety_settings = list(
            safety_settings if safety_settings is not None else default_safety_settings()
        )
        self._sleep = sleep
        self._rng = rng if rng is not None else random.Random()

        if client is not None:
            # An injected client is assumed to carry its own auth: a test
            # double, or a caller that built a Vertex-backed client.  Do not
            # go looking for a key we do not need.
            self._client = client
            self._api_key: str | None = None
            return

        key = api_key or os.environ.get(ENV_API_KEY) or os.environ.get(ENV_API_KEY_FALLBACK)
        if not key:
            raise MissingAPIKey(
                f"no Gemini API key: pass api_key=... or set the {ENV_API_KEY} "
                f"environment variable (see .env.example)"
            )
        self._api_key = key
        # timeout is milliseconds on the wire; seconds in this API, because
        # every other timeout in this repo is seconds.
        self._client = genai.Client(
            api_key=key,
            http_options=types.HttpOptions(timeout=int(self.timeout * 1000)),
        )

    # -- plumbing ---------------------------------------------------------

    @property
    def client(self) -> Any:
        """The underlying ``genai.Client``, for the batch path built later."""
        return self._client

    def _backoff_delay(self, attempt: int) -> float:
        """Equal-jitter exponential backoff, bounded at :data:`_BACKOFF_CAP`.

        Jitter matters more than the exponent: without it, N workers that hit
        the same 429 all wake at the same instant and re-create the burst.
        """
        ceiling = min(_BACKOFF_CAP, _BACKOFF_BASE * (2**attempt))
        return ceiling / 2 + self._rng.random() * (ceiling / 2)

    def _call_with_retries(self, operation: str, call: Callable[[], T]) -> T:
        """Run ``call``, retrying only what is worth retrying."""
        last: BaseException | None = None
        status: int | None = None

        for attempt in range(self.max_retries):
            try:
                return call()
            except genai_errors.APIError as exc:
                status = _status_code(exc)
                if status not in RETRYABLE_STATUS_CODES:
                    raise GeminiAPIError(
                        f"{operation} failed ({status}): {getattr(exc, 'message', exc)}",
                        status_code=status,
                        attempts=attempt + 1,
                    ) from exc
                last = exc
            except _TRANSIENT_ERRORS as exc:
                status = None
                last = exc

            if attempt + 1 >= self.max_retries:
                break
            delay = self._backoff_delay(attempt)
            logger.warning(
                "%s: retryable failure (%s) on attempt %d/%d; sleeping %.2fs",
                operation,
                status if status is not None else type(last).__name__,
                attempt + 1,
                self.max_retries,
                delay,
            )
            self._sleep(delay)

        raise GeminiAPIError(
            f"{operation} gave up after {self.max_retries} attempts: {last}",
            status_code=status,
            attempts=self.max_retries,
        ) from last

    # -- generation -------------------------------------------------------

    def generate(
        self,
        prompt: str,
        *,
        system: str | None = None,
        schema: Any = None,
        temperature: float | None = 0.2,
        cache: str | None = None,
        safety_settings: Sequence[types.SafetySetting] | None = None,
        max_output_tokens: int | None = None,
    ) -> GenResult:
        """One ``generate_content`` call.

        ``schema`` switches on structured output (``response_mime_type`` plus
        ``response_schema``) and populates :attr:`GenResult.parsed`.  Pass a
        pydantic model class, a :class:`types.Schema`, or a plain JSON-Schema
        dict; the SDK parses the first two for us and the dict form falls back
        to ``json.loads``.

        ``cache`` is a cache name from :meth:`create_cache`.  ``system`` cannot
        be combined with it: a cached prefix owns its own system instruction,
        so passing both is a programming error rather than a merge.

        ``temperature`` is sent when not ``None``.  Gemini 3.x currently
        ignores sampling parameters and future models are documented to reject
        them with a 400 — pass ``temperature=None`` to omit the field entirely
        if that day arrives.
        """
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be a non-empty string")
        if cache and system:
            raise ValueError(
                "system_instruction cannot be combined with cached_content — "
                "put the system instruction in create_cache(system_instruction=...)"
            )

        config_kwargs: dict[str, Any] = {
            "safety_settings": list(
                safety_settings if safety_settings is not None else self.safety_settings
            ),
        }
        if system:
            config_kwargs["system_instruction"] = _nfc(system)
        if cache:
            config_kwargs["cached_content"] = cache
        if temperature is not None:
            config_kwargs["temperature"] = float(temperature)
        if max_output_tokens is not None:
            config_kwargs["max_output_tokens"] = int(max_output_tokens)
        if schema is not None:
            config_kwargs["response_mime_type"] = "application/json"
            config_kwargs["response_schema"] = schema

        contents = _nfc(prompt)
        config = types.GenerateContentConfig(**config_kwargs)

        response = self._call_with_retries(
            "generate_content",
            lambda: self._client.models.generate_content(
                model=self.model, contents=contents, config=config
            ),
        )
        return self._build_result(response, schema=schema, cache=cache)

    def _build_result(self, response: Any, *, schema: Any, cache: str | None) -> GenResult:
        """Turn an SDK response into a :class:`GenResult`, loudly."""
        candidates = getattr(response, "candidates", None) or []
        candidate = candidates[0] if candidates else None

        feedback = getattr(response, "prompt_feedback", None)
        block_reason = _enum_value(getattr(feedback, "block_reason", None))
        ratings = list(getattr(candidate, "safety_ratings", None) or [])
        if not ratings and feedback is not None:
            ratings = list(getattr(feedback, "safety_ratings", None) or [])

        result = GenResult(
            text=_response_text(response),
            parsed=None,
            usage=Usage.from_metadata(getattr(response, "usage_metadata", None)),
            model=getattr(response, "model_version", None) or self.model,
            finish_reason=_enum_value(getattr(candidate, "finish_reason", None)),
            cache_name=cache,
            block_reason=block_reason,
            safety_ratings=tuple(_as_dict(rating) for rating in ratings),
        )

        if result.blocked:
            logger.error(
                "blocked by safety filter: finish_reason=%s block_reason=%s ratings=%s",
                result.finish_reason,
                result.block_reason,
                result.safety_ratings,
            )
            raise ResponseBlocked(
                f"Gemini blocked this call (finish_reason={result.finish_reason}, "
                f"block_reason={result.block_reason})",
                result=result,
            )
        if result.truncated:
            logger.warning(
                "response hit MAX_TOKENS after %d output tokens — text is truncated",
                result.usage.output_tokens,
            )
        if cache and not result.used_cache:
            # Not fatal, but it is the difference between $11 and $97 per run.
            logger.warning(
                "cache %s was requested but usage reports 0 cached tokens", cache
            )

        if schema is None:
            return result

        parsed = getattr(response, "parsed", None)
        if parsed is None:
            payload = _strip_code_fence(result.text).strip()
            if not payload:
                raise StructuredOutputError(
                    "schema was requested but the response carried no text "
                    f"(finish_reason={result.finish_reason})"
                )
            try:
                parsed = json.loads(payload)
            except json.JSONDecodeError as exc:
                hint = " (response was truncated at MAX_TOKENS)" if result.truncated else ""
                raise StructuredOutputError(
                    f"schema was requested but the response is not valid JSON{hint}: {exc}"
                ) from exc

        return GenResult(
            text=result.text,
            parsed=parsed,
            usage=result.usage,
            model=result.model,
            finish_reason=result.finish_reason,
            cache_name=result.cache_name,
            block_reason=result.block_reason,
            safety_ratings=result.safety_ratings,
        )

    # -- tokens -----------------------------------------------------------

    def count_tokens(self, text: str) -> int:
        """Input tokens for ``text`` under the pinned model.

        Measured, never estimated: Google publishes no tokens-per-syllable
        figure for Tibetan, and the low-resource literature puts Tibetan
        fertility at the worst of every language measured.  Chunk sizes and
        context budgets calibrated on the "~4 characters per token" rule of
        thumb would be wrong by a large factor.
        """
        if not isinstance(text, str):
            raise TypeError("count_tokens expects a string")
        if not text:
            return 0
        contents = _nfc(text)
        response = self._call_with_retries(
            "count_tokens",
            lambda: self._client.models.count_tokens(model=self.model, contents=contents),
        )
        total = getattr(response, "total_tokens", None)
        return int(total) if isinstance(total, (int, float)) else 0

    # -- explicit caching -------------------------------------------------

    def create_cache(
        self,
        contents: str | Sequence[str],
        display_name: str,
        ttl_seconds: int = DEFAULT_CACHE_TTL_SECONDS,
        *,
        system_instruction: str | None = None,
        check_min_tokens: bool = True,
    ) -> str | None:
        """Cache a corpus once and reuse it across every term in the run.

        This is the project's main cost lever.  The commentary corpus is
        byte-identical for all ~200 terms; resending it per term costs roughly
        8x what a cache costs.

        Returns the cache name, or ``None`` when the corpus is **too small to
        cache** — the API requires at least :data:`MIN_CACHE_TOKENS` input
        tokens (4,096 on Gemini 3.5 Flash).  ``None`` is not an error:
        :meth:`generate` accepts ``cache=None`` and runs uncached, which is
        correct behaviour for a small test corpus.  Every other 400 is a real
        bug and propagates.

        The caller owns the lifecycle.  Storage bills per token-hour whether or
        not you generate, so call :meth:`delete_cache` in a ``finally`` block;
        a 300k-token cache left alive overnight is real money for nothing.
        Cached content is immutable — editing the corpus means a new cache.
        """
        parts = [contents] if isinstance(contents, str) else list(contents)
        normalised = [_nfc(part) for part in parts if part]
        if not normalised:
            raise ValueError("create_cache needs at least one non-empty content block")
        if not display_name or not display_name.strip():
            raise ValueError("display_name is required — caches outlive the process")

        if check_min_tokens:
            measured = self.count_tokens("\n\n".join(normalised))
            if measured < MIN_CACHE_TOKENS:
                logger.warning(
                    "corpus %r is %d tokens, below the %d-token cache minimum — "
                    "proceeding uncached",
                    display_name,
                    measured,
                    MIN_CACHE_TOKENS,
                )
                return None

        config_kwargs: dict[str, Any] = {
            "display_name": display_name.strip(),
            "contents": normalised,
            "ttl": f"{int(ttl_seconds)}s",
        }
        if system_instruction:
            config_kwargs["system_instruction"] = _nfc(system_instruction)
        config = types.CreateCachedContentConfig(**config_kwargs)

        try:
            cache = self._call_with_retries(
                "caches.create",
                lambda: self._client.caches.create(model=self.model, config=config),
            )
        except GeminiAPIError as exc:
            if exc.status_code == 400 and _CACHE_TOO_SMALL.search(str(exc)):
                logger.warning(
                    "API refused to cache %r as too small (%s) — proceeding uncached",
                    display_name,
                    exc,
                )
                return None
            raise

        name = getattr(cache, "name", None)
        if not name:
            logger.warning("caches.create returned no name for %r — proceeding uncached",
                           display_name)
            return None
        logger.info(
            "cached %r as %s (ttl %ss, %s)",
            display_name,
            name,
            int(ttl_seconds),
            _as_dict(getattr(cache, "usage_metadata", None)) if
            getattr(cache, "usage_metadata", None) else "usage unreported",
        )
        return str(name)

    def delete_cache(self, name: str | None) -> bool:
        """Tear a cache down.  Safe to call with ``None`` in a ``finally``.

        Never raises on a delete failure: an orphaned cache costs a few cents
        and expires on its TTL, whereas an exception thrown from cleanup masks
        the real error that sent us into ``finally``.
        """
        if not name:
            return False
        try:
            self._call_with_retries(
                "caches.delete", lambda: self._client.caches.delete(name=name)
            )
        except GeminiError as exc:
            logger.warning("could not delete cache %s: %s", name, exc)
            return False
        logger.info("deleted cache %s", name)
        return True


# --------------------------------------------------------------------------
# Prompt library
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Prompt:
    """One versioned prompt file: front matter plus body.

    Prompts are git-tracked artifacts with provenance (which forum topic, which
    author, which model it was actually tuned on) because the paper's
    reproducibility claim depends on knowing exactly which text produced which
    article.  ``meta`` is kept whole rather than flattened into fields so a new
    front-matter key does not require a code change.
    """

    name: str
    stage: str
    version: int
    path: Path
    body: str
    meta: Mapping[str, Any]

    @property
    def variables(self) -> tuple[str, ...]:
        """Placeholders actually present in the body."""
        return template_variables(self.body)

    @property
    def declared_variables(self) -> tuple[str, ...]:
        """The front matter's ``variables:`` list, if it declares one."""
        declared = self.meta.get("variables")
        if isinstance(declared, str):
            return (declared,)
        if isinstance(declared, Sequence):
            return tuple(str(item) for item in declared)
        return ()

    @property
    def model_tested(self) -> str:
        """Which model this prompt was actually validated on.

        Several inherited prompts say ``claude-only``.  That is a live risk
        (PLAN.md §7), not a footnote, so it gets an accessor.
        """
        return str(self.meta.get("model_tested", "unknown"))

    def render(self, **kwargs: Any) -> str:
        """Substitute ``$name`` placeholders.

        ``$``-delimited :class:`string.Template` syntax, not ``str.format``:
        the prompt bodies contain literal JSON braces (``{"term": ...}``) as
        output examples, and ``str.format`` would either choke on them or force
        every example to be double-braced — an editing trap for the Tibetan
        speakers who maintain these files.  ``$`` never occurs in Tibetan text.
        Escape a literal dollar as ``$$``.

        Substitution is *safe*: an unknown ``$foo`` in the body is left as
        literal text rather than raising, so a stray dollar sign cannot break a
        run.  Missing arguments are still an error, checked up front against
        the placeholders actually present.

        Non-string values are JSON-encoded with ``ensure_ascii=False`` so
        Tibetan survives readable in the prompt.
        """
        required = set(self.variables)
        missing = sorted(required - set(kwargs))
        if missing:
            raise PromptError(
                f"{self.path.name}: missing template argument(s) "
                f"{', '.join(missing)} (needs: {', '.join(sorted(required))})"
            )
        unexpected = sorted(set(kwargs) - required)
        if unexpected:
            logger.warning(
                "%s: ignoring argument(s) not in the template: %s",
                self.path.name,
                ", ".join(unexpected),
            )

        mapping = {key: _render_value(self.path, key, kwargs[key]) for key in required}
        return _nfc(string.Template(self.body).safe_substitute(mapping))


def _render_value(path: Path, key: str, value: Any) -> str:
    """Coerce one template argument to text, NFC-normalised."""
    if value is None:
        raise PromptError(
            f"{path.name}: template argument {key!r} is None — pass a value or "
            f"an explicit empty string"
        )
    if isinstance(value, str):
        return _nfc(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return _nfc(json.dumps(value, ensure_ascii=False, indent=2))


class PromptLibrary:
    """Every prompt under ``root``, indexed by stage and version.

    Layout is ``root/<stage>/<file>.md`` (the stage directory is the fallback
    when front matter omits ``stage:``).  Files are read eagerly at
    construction so a malformed prompt fails at startup rather than three
    stages into a run.
    """

    def __init__(self, root: Path | str) -> None:
        self.root = Path(root)
        if not self.root.is_dir():
            raise PromptError(f"prompt root {self.root} is not a directory")
        self._by_stage: dict[str, dict[int, Prompt]] = {}
        self._aliases: dict[str, str] = {}
        self._load()

    # -- loading ----------------------------------------------------------

    def _load(self) -> None:
        for path in sorted(self.root.rglob("*.md")):
            if path.name.startswith("."):
                continue
            prompt = self._read(path)
            versions = self._by_stage.setdefault(prompt.stage, {})
            existing = versions.get(prompt.version)
            if existing is not None:
                raise PromptError(
                    f"duplicate version {prompt.version} for stage {prompt.stage!r}: "
                    f"{existing.path.name} and {path.name} — bump one, because "
                    f"'latest' would otherwise be a coin flip"
                )
            versions[prompt.version] = prompt

        self._aliases = _build_stage_aliases(self._by_stage)

    def _read(self, path: Path) -> Prompt:
        text = _nfc(path.read_text(encoding="utf-8"))
        meta, body = parse_front_matter(text)
        if not meta:
            raise PromptError(
                f"{path}: no YAML front matter — every prompt must declare at least "
                f"name, version and stage"
            )

        relative = path.relative_to(self.root)
        fallback_stage = relative.parts[0] if len(relative.parts) > 1 else ""
        stage = str(meta.get("stage") or fallback_stage).strip()
        if not stage:
            raise PromptError(f"{path}: no 'stage' in front matter and no stage directory")

        raw_version = meta.get("version")
        version = _coerce_version(raw_version)
        if version is None:
            raise PromptError(
                f"{path}: front matter 'version' must be an integer, got {raw_version!r}"
            )

        name = str(meta.get("name") or path.stem).strip()
        if not body.strip():
            raise PromptError(f"{path}: front matter present but body is empty")

        return Prompt(name=name, stage=stage, version=version, path=path, body=body, meta=meta)

    # -- access -----------------------------------------------------------

    @property
    def stages(self) -> tuple[str, ...]:
        return tuple(sorted(self._by_stage))

    def __len__(self) -> int:
        return sum(len(versions) for versions in self._by_stage.values())

    def __iter__(self) -> Iterator[Prompt]:
        for stage in self.stages:
            for version in sorted(self._by_stage[stage]):
                yield self._by_stage[stage][version]

    def get(self, stage: str, version: int | str = "latest") -> Prompt:
        """One prompt by stage and version.

        ``stage`` accepts the directory name (``06-draft``), the bare name
        (``draft``) or the numeric prefix (``06``).  ``version`` accepts
        ``"latest"``, ``2``, ``"2"`` or ``"v2"``.
        """
        key = self._resolve_stage(stage)
        versions = self._by_stage[key]

        if isinstance(version, str) and version.strip().lower() in ("latest", "*", ""):
            return versions[max(versions)]

        wanted = _coerce_version(version)
        if wanted is None:
            raise PromptError(f"bad version {version!r}: use 'latest', 2, '2' or 'v2'")
        if wanted not in versions:
            raise PromptError(
                f"stage {key!r} has no version {wanted}; available: "
                f"{', '.join(str(v) for v in sorted(versions))}"
            )
        return versions[wanted]

    def all(self, stage: str) -> tuple[Prompt, ...]:
        """Every version for one stage, oldest first."""
        versions = self._by_stage[self._resolve_stage(stage)]
        return tuple(versions[v] for v in sorted(versions))

    def render(self, stage: str, version: int | str = "latest", **kwargs: Any) -> str:
        """Convenience: :meth:`get` then :meth:`Prompt.render`."""
        return self.get(stage, version).render(**kwargs)

    def _resolve_stage(self, stage: str) -> str:
        key = str(stage).strip()
        if key in self._by_stage:
            return key
        resolved = self._aliases.get(key) or self._aliases.get(key.lower())
        if resolved:
            return resolved
        raise PromptError(
            f"no prompts for stage {stage!r}; available: {', '.join(self.stages)}"
        )

    # -- integrity --------------------------------------------------------

    def validate(self) -> list[str]:
        """Non-raising consistency check, for a test or a CLI ``doctor``.

        The one that matters: a ``variables:`` list in front matter that no
        longer matches the ``$placeholders`` in the body.  That drift is
        invisible until a render silently leaves ``$term`` in the text sent to
        the model.
        """
        problems: list[str] = []
        for prompt in self:
            declared = set(prompt.declared_variables)
            actual = set(prompt.variables)
            if declared and declared != actual:
                only_declared = sorted(declared - actual)
                only_actual = sorted(actual - declared)
                detail = []
                if only_declared:
                    detail.append(f"declared but unused: {', '.join(only_declared)}")
                if only_actual:
                    detail.append(f"used but undeclared: {', '.join(only_actual)}")
                problems.append(f"{prompt.path.name}: {'; '.join(detail)}")
            if not prompt.meta.get("name"):
                problems.append(f"{prompt.path.name}: front matter has no 'name'")
        return problems


def _coerce_version(value: Any) -> int | None:
    """``2`` / ``'2'`` / ``'v2'`` -> ``2``; anything else -> ``None``."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        text = value.strip().lower().lstrip("v")
        if text.isdigit():
            return int(text)
    return None


def _build_stage_aliases(by_stage: Mapping[str, Mapping[int, Prompt]]) -> dict[str, str]:
    """Map ``draft`` and ``06`` onto ``06-draft``, dropping ambiguous ones."""
    candidates: dict[str, set[str]] = {}
    for stage in by_stage:
        aliases = {stage.lower()}
        match = re.match(r"^(\d+)[-_](.+)$", stage)
        if match:
            aliases.add(match.group(1))
            aliases.add(match.group(1).lstrip("0") or "0")
            aliases.add(match.group(2).lower())
        for alias in aliases:
            candidates.setdefault(alias, set()).add(stage)
    return {
        alias: next(iter(stages))
        for alias, stages in candidates.items()
        if len(stages) == 1
    }
