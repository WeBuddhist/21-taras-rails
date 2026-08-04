"""Runtime settings: environment first, optional TOML underneath, secrets masked.

Two things this module exists to guarantee.

**``dry_run`` defaults to ``True``.**  Stage 8 writes to a live encyclopedia
with two administrators.  A misconfigured run must do nothing, not publish; the
default has to be the harmless one and ``--execute`` the deliberate act
(PLAN.md §3).  A settings file that forgets to mention ``dry_run`` therefore
means *dry run*, and an env var must be an affirmative word to turn it off.

**Secrets never reach a log.**  ``Settings`` is a dataclass, so its default
``repr`` would print the Gemini key and the bot password into every traceback,
CI log and ``print(settings)`` a hurried debugging session produces.  The
custom ``__repr__`` masks them.  Nothing in this module logs.

Precedence is environment > ``.env`` > TOML > built-in default.  The env var is
what a person reaches for when they need to override one value for one run; a
file they edited last week must not silently win over it.  ``.env`` sits just
below the real environment because that is what it stands in for — the README
tells a non-programmer to copy ``.env.example`` to ``.env`` and fill it in, and
a key that lands there has to actually reach the pipeline.

The ``.env`` parser is eight lines of stdlib rather than a ``python-dotenv``
dependency, because this module must import with no third-party package present
(``cli.py`` calls it before it knows whether the rest of the environment is
installed).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields, replace
from pathlib import Path
from typing import Any, Mapping

__all__ = [
    "DEFAULT_GEMINI_MODEL",
    "DEFAULT_WIKI_SITE",
    "ENV_KEYS",
    "Settings",
    "load_settings",
    "read_env_file",
    "repo_root",
]

#: Pinned model (PLAN.md §5).  A ``-preview`` id is never acceptable here: the
#: paper's numbers have to be reproducible, and preview endpoints change under
#: you without a version bump.
DEFAULT_GEMINI_MODEL = "gemini-3.5-flash"

#: Kept as a literal rather than imported from ``wiki.client``: this module
#: must import with no third-party package present, and the client pulls in
#: ``requests``.  The two constants are the same value by intent — if one
#: changes, change both.
DEFAULT_WIKI_SITE = "bo.wikipedia.org"

#: Field name -> environment variable(s), most preferred first.  These are the
#: names ``.env.example`` documents, because that is the file the README tells
#: a non-programmer to copy — a loader that reads a different name would leave
#: them with a config that silently does nothing.
#:
#: ``dry_run`` is the one field with two spellings: ``.env.example`` ships
#: ``KWIKI_DRY_RUN``, and the bare ``DRY_RUN`` is accepted as a convenience for
#: a one-off ``DRY_RUN=false kwiki publish``.  The prefixed name wins, since it
#: is the deliberate, project-scoped one.
ENV_KEYS: dict[str, tuple[str, ...]] = {
    "gemini_api_key": ("GEMINI_API_KEY",),
    "gemini_model": ("GEMINI_MODEL",),
    "wiki_site": ("WIKI_SITE",),
    "wiki_username": ("WIKI_USERNAME",),
    "wiki_bot_password": ("WIKI_BOT_PASSWORD",),
    "dry_run": ("KWIKI_DRY_RUN", "DRY_RUN"),
    "corpora_dir": ("KWIKI_CORPORA_DIR", "CORPORA_DIR"),
    "prompts_dir": ("KWIKI_PROMPTS_DIR", "PROMPTS_DIR"),
}

#: TOML section -> {key in that section: field name}.  Flat top-level keys named
#: after the fields work too; the sections exist because a human writing a
#: config file groups related settings, and refusing that grouping just means
#: they mistype the flat name.
_TOML_SECTIONS: dict[str, dict[str, str]] = {
    "gemini": {"api_key": "gemini_api_key", "model": "gemini_model"},
    "wiki": {
        "site": "wiki_site",
        "username": "wiki_username",
        "bot_password": "wiki_bot_password",
        "dry_run": "dry_run",
    },
    "paths": {"corpora_dir": "corpora_dir", "prompts_dir": "prompts_dir"},
}

#: Fields whose value must never be rendered.
_SECRET_FIELDS = frozenset({"gemini_api_key", "wiki_bot_password"})

_TRUE_WORDS = frozenset({"1", "true", "t", "yes", "y", "on"})
_FALSE_WORDS = frozenset({"0", "false", "f", "no", "n", "off"})


def repo_root() -> Path:
    """The repository root, derived from this file's location.

    ``src/kangyur_wiki/config.py`` -> two levels up.  A path computation, not a
    filesystem probe, so importing this module stays free of side effects.
    """
    return Path(__file__).resolve().parents[2]


def vault_root() -> Path:
    """The Railroads vault this pipeline lives inside.

    ``4-SYSTEM/Pipelines/wikipedia`` -> two levels up.  The pipeline no longer
    carries its own copy of the texts: the vault's ``1-SOURCES/`` is the single
    home for them, block IDs and all, and the rails work that puts them there
    (clean, segment, TOC, anchors) is the same work stages 1–2 used to do
    privately.  Falls back to the pipeline root when the folder does not sit in
    a vault, so a standalone checkout still resolves.
    """
    candidate = repo_root().parents[2]  # …/<vault>/4-SYSTEM/Pipelines/wikipedia
    return candidate if (candidate / "1-SOURCES").is_dir() else repo_root()


def _default_source_text_dir() -> Path:
    return vault_root() / "1-SOURCES" / "Text"


def _default_source_commentaries_dir() -> Path:
    return vault_root() / "1-SOURCES" / "Commentaries"


def _default_corpora_dir() -> Path:
    """Where the pipeline's *derived* artifacts live.

    Wikipedia articles are transformations, so they belong in the vault's
    citation chain (``1-SOURCES/`` -> ``2-RAILS/`` -> ``3-TRANSFORMATIONS/``)
    rather than in a private corpora tree.  Everything under here is generated:
    the registries, the ledger, ``work/``, and the per-term article folders.
    """
    root = vault_root()
    if (root / "3-TRANSFORMATIONS").is_dir():
        return root / "3-TRANSFORMATIONS" / "Wikipedia"
    return repo_root() / "corpora"


def _default_prompts_dir() -> Path:
    return repo_root() / "prompts"


def _default_local_wiki_dir() -> Path:
    """Where a verified article's grounding material is offered to the rails folder.

    Unlike ``corpora_dir``, this has no legacy fallback: Local-Wiki emission is new
    behaviour (the vault's 2-RAILS/ existed long before this pipeline did), so there
    is no prior in-repo location to fall back to. A standalone checkout with no
    ``2-RAILS/`` still gets a path here — ``emit_local_wiki`` creates the directory
    on first write — it simply will not be inside anyone's vault.
    """
    return vault_root() / "2-RAILS" / "Local-Wiki"


class ConfigError(RuntimeError):
    """A setting the run cannot proceed without is missing or unusable."""


@dataclass(frozen=True, repr=False)
class Settings:
    """Everything the pipeline needs to know that is not in the corpus itself.

    Frozen: settings are read once at startup and threaded through, so a stage
    cannot quietly flip ``dry_run`` for the stages after it.  Use ``replace``
    (re-exported below as ``Settings.with_``) to derive a variant.
    """

    gemini_api_key: str | None = None
    gemini_model: str = DEFAULT_GEMINI_MODEL
    wiki_site: str = DEFAULT_WIKI_SITE
    wiki_username: str | None = None
    wiki_bot_password: str | None = None
    dry_run: bool = True
    corpora_dir: Path = field(default_factory=_default_corpora_dir)
    prompts_dir: Path = field(default_factory=_default_prompts_dir)
    source_text_dir: Path = field(default_factory=_default_source_text_dir)
    source_commentaries_dir: Path = field(default_factory=_default_source_commentaries_dir)
    local_wiki_dir: Path = field(default_factory=_default_local_wiki_dir)

    def __repr__(self) -> str:
        """Masked representation — see the module docstring.

        Shows ``set``/``unset`` for a secret rather than a fixed ``'***'``,
        because "did the key load at all?" is the question a person is actually
        asking when they print settings, and answering it needs no secret.
        """
        parts = []
        for spec in fields(self):
            value = getattr(self, spec.name)
            if spec.name in _SECRET_FIELDS:
                parts.append(f"{spec.name}=<{'set' if value else 'unset'}>")
            else:
                parts.append(f"{spec.name}={value!r}")
        return f"Settings({', '.join(parts)})"

    def with_(self, **changes: Any) -> "Settings":
        """A copy with fields replaced — the only way to change a frozen setting."""
        return replace(self, **changes)

    def corpus_dir(self, corpus_id: str) -> Path:
        """``<corpora_dir>/<corpus_id>`` — the working directory for one corpus."""
        return self.corpora_dir / corpus_id

    def require_gemini_api_key(self) -> str:
        """The API key, or a ``ConfigError`` naming the variable to set.

        Stages call this instead of asserting on ``None`` so the failure reads
        as an instruction rather than an ``AttributeError`` three frames deep.
        """
        if not self.gemini_api_key:
            raise ConfigError(
                "GEMINI_API_KEY is not set — export it, put it in .env, "
                "or set api_key under [gemini] in your config TOML"
            )
        return self.gemini_api_key

    def require_wiki_credentials(self) -> tuple[str, str]:
        """``(username, bot password)``, or a ``ConfigError`` naming both variables."""
        missing = [
            name
            for name, value in (
                ("WIKI_USERNAME", self.wiki_username),
                ("WIKI_BOT_PASSWORD", self.wiki_bot_password),
            )
            if not value
        ]
        if missing:
            raise ConfigError(
                f"{' and '.join(missing)} not set — create a bot password at "
                f"https://{self.wiki_site}/wiki/Special:BotPasswords"
            )
        assert self.wiki_username is not None and self.wiki_bot_password is not None
        return (self.wiki_username, self.wiki_bot_password)


def _parse_bool(value: Any, *, source: str) -> bool:
    """Strict boolean parsing — an unrecognised word is an error, not a ``False``.

    ``DRY_RUN=fasle`` silently meaning "publish for real" is the failure mode
    this refuses to have.
    """
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in _TRUE_WORDS:
        return True
    if text in _FALSE_WORDS:
        return False
    raise ConfigError(
        f"{source} must be a boolean word (true/false, 1/0, yes/no, on/off), got {value!r}"
    )


def read_env_file(path: str | os.PathLike[str]) -> dict[str, str]:
    """Parse a ``.env`` file into ``{NAME: value}``.

    Deliberately minimal — the subset ``.env.example`` actually uses: ``NAME=value``
    one per line, ``#`` comments, blank lines, optional ``export`` prefix, and
    optional surrounding quotes on the value.  No interpolation, no multi-line
    values: a secret that needs either of those belongs in the real environment.

    A missing file is not an error (deployment sets real env vars and ships no
    ``.env``), and neither is a malformed line — it is skipped.  Refusing to start
    because line 12 has no ``=`` would be worse than ignoring line 12.
    """
    resolved = Path(path)
    try:
        raw = resolved.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    values: dict[str, str] = {}
    for line in raw.splitlines():
        entry = line.strip().lstrip("﻿")
        if not entry or entry.startswith("#"):
            continue
        if entry.startswith("export "):
            entry = entry[len("export ") :].lstrip()
        name, sep, value = entry.partition("=")
        name = name.strip()
        if not sep or not name:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        values[name] = value
    return values


def _read_toml(path: str | os.PathLike[str]) -> Mapping[str, Any]:
    """Parse a TOML file with the stdlib parser.

    ``tomllib`` is 3.11+.  On 3.10 there is no stdlib TOML and no third-party
    parser in this project's dependency set, so a config *file* is unsupported
    there — but only if one is actually passed.  Environment configuration
    works on every supported version, which is why the file is optional.
    """
    try:
        import tomllib  # noqa: PLC0415
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on interpreter
        raise ConfigError(
            "reading a TOML config needs Python 3.11+ (tomllib); "
            "on 3.10 configure the pipeline through environment variables"
        ) from exc
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def _flatten_toml(document: Mapping[str, Any]) -> dict[str, Any]:
    """Collapse the supported TOML shapes into ``{field name: value}``.

    Sections win over top-level keys of the same name: a file that says both is
    ambiguous, and the more specific placement is the more deliberate one.
    """
    flat: dict[str, Any] = {
        key: value
        for key, value in document.items()
        if key in ENV_KEYS and not isinstance(value, Mapping)
    }
    for section, mapping in _TOML_SECTIONS.items():
        block = document.get(section)
        if not isinstance(block, Mapping):
            continue
        for key, field_name in mapping.items():
            if key in block:
                flat[field_name] = block[key]
    return flat


def load_settings(
    env: Mapping[str, str] = os.environ,
    toml_path: str | os.PathLike[str] | None = None,
    env_file: str | os.PathLike[str] | None = None,
) -> Settings:
    """Assemble ``Settings`` from environment, ``.env`` and an optional TOML file.

    ``env`` defaults to the live ``os.environ`` and is injectable so tests
    never have to mutate the process environment.  An empty-string env var is
    treated as unset — that is what an unfilled line in a ``.env`` produces,
    and it should not shadow a real value from the file.

    ``env_file`` names a ``.env`` to merge in below the environment and above
    the TOML.  Left unset it is ``<repo root>/.env`` **only when reading the
    real ``os.environ``** — a caller who injects its own ``env`` mapping is
    asking for an isolated environment, and a developer's ``.env`` leaking into
    that would make every such test depend on an untracked file.  Pass a path
    explicitly to read one anyway.

    Raises ``ConfigError`` on an unparseable boolean or a TOML file that cannot
    be read; a bad config should stop the run at startup, not at stage 8.
    """
    values: dict[str, Any] = {}

    if toml_path is not None:
        resolved = Path(toml_path)
        if not resolved.exists():
            raise ConfigError(f"config file not found: {resolved}")
        values.update(_flatten_toml(_read_toml(resolved)))

    if env_file is not None:
        dotenv = read_env_file(env_file)
    elif env is os.environ:
        dotenv = read_env_file(repo_root() / ".env")
    else:
        dotenv = {}

    sources: dict[str, str] = {}
    for field_name, env_keys in ENV_KEYS.items():
        for env_key in env_keys:
            raw = env.get(env_key)
            if raw is None or str(raw).strip() == "":
                raw = dotenv.get(env_key)
            if raw is None or str(raw).strip() == "":
                continue
            values[field_name] = raw
            sources[field_name] = env_key
            break

    kwargs: dict[str, Any] = {}
    for field_name, value in values.items():
        if field_name == "dry_run":
            kwargs[field_name] = _parse_bool(
                value, source=sources.get(field_name, ENV_KEYS[field_name][0])
            )
        elif field_name in {"corpora_dir", "prompts_dir"}:
            kwargs[field_name] = Path(str(value)).expanduser()
        else:
            text = str(value).strip()
            kwargs[field_name] = text or None

    # A blank model or site would be worse than the default: it produces an API
    # call to nowhere with a confusing error.  Drop them and let the default win.
    for required in ("gemini_model", "wiki_site"):
        if kwargs.get(required) is None:
            kwargs.pop(required, None)

    return Settings(**kwargs)
