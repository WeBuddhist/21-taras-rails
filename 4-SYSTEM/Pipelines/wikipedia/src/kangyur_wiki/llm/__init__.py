"""LLM access layer: one wrapper around Gemini, one versioned prompt library.

Every model call in the pipeline goes through :class:`~kangyur_wiki.llm.gemini.GeminiClient`
so that the model id, the safety thresholds, the retry policy and the cache
lifecycle are decided in exactly one file.  The Interactions API will
eventually replace the legacy ``generateContent`` path this module uses; when
it does, this is the only module that changes.
"""

from kangyur_wiki.llm.gemini import (
    ADJUSTABLE_HARM_CATEGORIES,
    DEFAULT_CACHE_TTL_SECONDS,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    ENV_API_KEY,
    ENV_API_KEY_FALLBACK,
    LITE_MODEL,
    MIN_CACHE_TOKENS,
    RETRYABLE_STATUS_CODES,
    GeminiAPIError,
    GeminiClient,
    GeminiError,
    GenResult,
    MissingAPIKey,
    Prompt,
    PromptError,
    PromptLibrary,
    ResponseBlocked,
    StructuredOutputError,
    Usage,
    default_prompt_root,
    default_safety_settings,
    parse_front_matter,
    template_variables,
)

__all__ = [
    "ADJUSTABLE_HARM_CATEGORIES",
    "DEFAULT_CACHE_TTL_SECONDS",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_MODEL",
    "DEFAULT_TIMEOUT",
    "ENV_API_KEY",
    "ENV_API_KEY_FALLBACK",
    "LITE_MODEL",
    "MIN_CACHE_TOKENS",
    "RETRYABLE_STATUS_CODES",
    "GeminiAPIError",
    "GeminiClient",
    "GeminiError",
    "GenResult",
    "MissingAPIKey",
    "Prompt",
    "PromptError",
    "PromptLibrary",
    "ResponseBlocked",
    "StructuredOutputError",
    "Usage",
    "default_prompt_root",
    "default_safety_settings",
    "parse_front_matter",
    "template_variables",
]
