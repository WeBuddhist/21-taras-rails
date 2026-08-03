"""Offline tests for settings loading.

The environment is always injected, never mutated: these tests must not be able
to leak a fake API key into the rest of the suite, and ``load_settings`` was
given an ``env`` parameter precisely so they do not have to try.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from kangyur_wiki.config import (
    DEFAULT_GEMINI_MODEL,
    DEFAULT_WIKI_SITE,
    ConfigError,
    Settings,
    load_settings,
    repo_root,
)

SECRET = "AIzaSyD-not-a-real-key-000000000000000"
BOT_PASSWORD = "kangyurbot@abcdef0123456789"


# --------------------------------------------------------------------------
# Defaults
# --------------------------------------------------------------------------


def test_an_empty_environment_gives_safe_defaults():
    settings = load_settings(env={})
    assert settings.dry_run is True
    assert settings.gemini_model == DEFAULT_GEMINI_MODEL
    assert settings.wiki_site == DEFAULT_WIKI_SITE
    assert settings.gemini_api_key is None
    assert settings.corpora_dir == repo_root() / "corpora"
    assert settings.prompts_dir == repo_root() / "prompts"


def test_the_pinned_model_is_not_a_preview_build():
    """PLAN.md §5: a ``-preview`` id changes under you and breaks reproducibility."""
    assert "preview" not in DEFAULT_GEMINI_MODEL


def test_repo_root_contains_the_plan():
    assert (repo_root() / "PLAN.md").exists()


# --------------------------------------------------------------------------
# Environment
# --------------------------------------------------------------------------


def test_environment_values_are_read():
    settings = load_settings(
        env={
            "GEMINI_API_KEY": SECRET,
            "GEMINI_MODEL": "gemini-3.6-flash",
            "WIKI_USERNAME": "Pecha-Bot",
            "WIKI_BOT_PASSWORD": BOT_PASSWORD,
            "WIKI_SITE": "test.wikipedia.org",
            "CORPORA_DIR": "/data/corpora",
            "PROMPTS_DIR": "/data/prompts",
        }
    )
    assert settings.gemini_api_key == SECRET
    assert settings.gemini_model == "gemini-3.6-flash"
    assert settings.wiki_username == "Pecha-Bot"
    assert settings.wiki_site == "test.wikipedia.org"
    assert settings.corpora_dir == Path("/data/corpora")
    assert settings.prompts_dir == Path("/data/prompts")


def test_a_blank_env_var_is_treated_as_unset():
    """An unfilled line in a ``.env`` must not shadow a real value."""
    settings = load_settings(env={"GEMINI_API_KEY": "", "GEMINI_MODEL": "   "})
    assert settings.gemini_api_key is None
    assert settings.gemini_model == DEFAULT_GEMINI_MODEL


def test_a_tilde_in_a_path_is_expanded():
    settings = load_settings(env={"CORPORA_DIR": "~/corpora"})
    assert not str(settings.corpora_dir).startswith("~")


@pytest.mark.parametrize("word", ["0", "false", "FALSE", "no", "off", "n"])
def test_dry_run_can_be_turned_off_by_an_affirmative_word(word):
    assert load_settings(env={"DRY_RUN": word}).dry_run is False


@pytest.mark.parametrize("word", ["1", "true", "TRUE", "yes", "on", "y"])
def test_dry_run_stays_on(word):
    assert load_settings(env={"DRY_RUN": word}).dry_run is True


def test_an_unparseable_dry_run_is_an_error_not_a_publish():
    """``DRY_RUN=fasle`` must stop the run, not quietly mean "publish"."""
    with pytest.raises(ConfigError, match="DRY_RUN"):
        load_settings(env={"DRY_RUN": "fasle"})


def test_the_name_dot_env_example_documents_is_read():
    """``.env.example`` ships ``KWIKI_DRY_RUN``; a user copying it must work."""
    assert load_settings(env={"KWIKI_DRY_RUN": "false"}).dry_run is False


def test_the_prefixed_name_wins_over_the_bare_one():
    settings = load_settings(env={"KWIKI_DRY_RUN": "true", "DRY_RUN": "false"})
    assert settings.dry_run is True


def test_the_error_names_the_variable_that_was_actually_set():
    with pytest.raises(ConfigError, match="KWIKI_DRY_RUN"):
        load_settings(env={"KWIKI_DRY_RUN": "maybe"})


# --------------------------------------------------------------------------
# TOML
# --------------------------------------------------------------------------

_TOMLLIB = pytest.mark.skipif(
    sys.version_info < (3, 11), reason="tomllib needs Python 3.11+"
)


@_TOMLLIB
def test_toml_sections_are_read(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text(
        "\n".join(
            [
                "[gemini]",
                f'api_key = "{SECRET}"',
                'model = "gemini-3.6-flash"',
                "[wiki]",
                'username = "Pecha-Bot"',
                "dry_run = false",
                "[paths]",
                f'corpora_dir = "{tmp_path / "corpora"}"',
            ]
        ),
        encoding="utf-8",
    )
    settings = load_settings(env={}, toml_path=config)
    assert settings.gemini_api_key == SECRET
    assert settings.gemini_model == "gemini-3.6-flash"
    assert settings.wiki_username == "Pecha-Bot"
    assert settings.dry_run is False
    assert settings.corpora_dir == tmp_path / "corpora"


@_TOMLLIB
def test_flat_toml_keys_work_too(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text(f'gemini_api_key = "{SECRET}"\n', encoding="utf-8")
    assert load_settings(env={}, toml_path=config).gemini_api_key == SECRET


@_TOMLLIB
def test_the_environment_overrides_the_file(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text('[gemini]\nmodel = "from-file"\n', encoding="utf-8")
    settings = load_settings(env={"GEMINI_MODEL": "from-env"}, toml_path=config)
    assert settings.gemini_model == "from-env"


@_TOMLLIB
def test_a_toml_that_forgets_dry_run_still_means_dry_run(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text('[wiki]\nusername = "Pecha-Bot"\n', encoding="utf-8")
    assert load_settings(env={}, toml_path=config).dry_run is True


def test_a_missing_toml_stops_the_run_at_startup(tmp_path):
    with pytest.raises(ConfigError, match="not found"):
        load_settings(env={}, toml_path=tmp_path / "absent.toml")


# --------------------------------------------------------------------------
# Secrets
# --------------------------------------------------------------------------


def test_repr_never_shows_a_secret():
    settings = load_settings(
        env={"GEMINI_API_KEY": SECRET, "WIKI_BOT_PASSWORD": BOT_PASSWORD}
    )
    text = repr(settings)
    assert SECRET not in text
    assert BOT_PASSWORD not in text
    assert "gemini_api_key=<set>" in text
    assert "wiki_bot_password=<set>" in text


def test_repr_says_when_a_secret_is_absent():
    assert "gemini_api_key=<unset>" in repr(load_settings(env={}))


def test_str_and_format_are_masked_too():
    """``f"{settings}"`` falls back to ``__repr__``; make sure that holds."""
    settings = load_settings(env={"GEMINI_API_KEY": SECRET})
    assert SECRET not in str(settings)
    assert SECRET not in f"{settings}"


def test_non_secret_fields_are_still_visible():
    settings = load_settings(env={"WIKI_USERNAME": "Pecha-Bot"})
    assert "wiki_username='Pecha-Bot'" in repr(settings)
    assert "dry_run=True" in repr(settings)


# --------------------------------------------------------------------------
# Requirements and derived paths
# --------------------------------------------------------------------------


def test_require_gemini_api_key_names_the_variable():
    with pytest.raises(ConfigError, match="GEMINI_API_KEY"):
        load_settings(env={}).require_gemini_api_key()


def test_require_gemini_api_key_returns_it():
    assert load_settings(env={"GEMINI_API_KEY": SECRET}).require_gemini_api_key() == SECRET


def test_require_wiki_credentials_names_both_missing_variables():
    with pytest.raises(ConfigError) as excinfo:
        load_settings(env={}).require_wiki_credentials()
    assert "WIKI_USERNAME" in str(excinfo.value)
    assert "WIKI_BOT_PASSWORD" in str(excinfo.value)
    assert "Special:BotPasswords" in str(excinfo.value)


def test_require_wiki_credentials_returns_the_pair():
    settings = load_settings(
        env={"WIKI_USERNAME": "Pecha-Bot", "WIKI_BOT_PASSWORD": BOT_PASSWORD}
    )
    assert settings.require_wiki_credentials() == ("Pecha-Bot", BOT_PASSWORD)


def test_corpus_dir():
    settings = load_settings(env={"CORPORA_DIR": "/data/corpora"})
    assert settings.corpus_dir("spyodjug") == Path("/data/corpora/spyodjug")


def test_settings_are_frozen():
    settings = load_settings(env={})
    with pytest.raises(Exception):
        settings.dry_run = False  # type: ignore[misc]


def test_with_derives_a_variant_without_touching_the_original():
    settings = load_settings(env={})
    executing = settings.with_(dry_run=False)
    assert executing.dry_run is False
    assert settings.dry_run is True
    assert isinstance(executing, Settings)


# ---------------------------------------------------------------------------
# .env
# ---------------------------------------------------------------------------
#
# Nothing loaded .env until 2026-08-01, so a key sitting in the file the README
# tells you to create never reached the pipeline and every model stage failed
# with "GEMINI_API_KEY is not set". These pin the fix and its precedence.


def test_env_file_is_read(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=from-the-file\n", encoding="utf-8")
    assert load_settings(env={}, env_file=env_file).gemini_api_key == "from-the-file"


def test_a_real_environment_variable_beats_the_file(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=from-the-file\n", encoding="utf-8")
    settings = load_settings(env={"GEMINI_API_KEY": "from-the-env"}, env_file=env_file)
    assert settings.gemini_api_key == "from-the-env"


def test_a_blank_environment_variable_does_not_shadow_the_file(tmp_path):
    """An unfilled line in a shell profile must not mask a filled one in .env."""
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=from-the-file\n", encoding="utf-8")
    settings = load_settings(env={"GEMINI_API_KEY": "  "}, env_file=env_file)
    assert settings.gemini_api_key == "from-the-file"


def test_env_file_beats_toml(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=from-the-file\n", encoding="utf-8")
    toml = tmp_path / "config.toml"
    toml.write_text('[gemini]\napi_key = "from-the-toml"\n', encoding="utf-8")
    settings = load_settings(env={}, toml_path=toml, env_file=env_file)
    assert settings.gemini_api_key == "from-the-file"


def test_an_injected_environment_does_not_pick_up_the_repo_env_file():
    """Every other test in this file depends on this: a caller that supplies its
    own env mapping is asking for isolation, and a developer's real .env leaking
    in would make the suite pass or fail on an untracked file."""
    assert load_settings(env={}).gemini_api_key is None


def test_a_missing_env_file_is_not_an_error(tmp_path):
    assert load_settings(env={}, env_file=tmp_path / "nope").dry_run is True


@pytest.mark.parametrize(
    "line, expected",
    [
        ("GEMINI_API_KEY=plain", "plain"),
        ('GEMINI_API_KEY="double quoted"', "double quoted"),
        ("GEMINI_API_KEY='single quoted'", "single quoted"),
        ("export GEMINI_API_KEY=exported", "exported"),
        ("GEMINI_API_KEY=  spaced  ", "spaced"),
    ],
)
def test_env_file_line_forms(tmp_path, line, expected):
    env_file = tmp_path / ".env"
    env_file.write_text(f"# a comment\n\n{line}\n", encoding="utf-8")
    assert load_settings(env={}, env_file=env_file).gemini_api_key == expected


def test_a_malformed_line_is_skipped_not_fatal(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("this line has no equals sign\nGEMINI_API_KEY=fine\n", encoding="utf-8")
    assert load_settings(env={}, env_file=env_file).gemini_api_key == "fine"


def test_dry_run_from_the_env_file_still_parses_strictly(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("KWIKI_DRY_RUN=fasle\n", encoding="utf-8")
    with pytest.raises(ConfigError):
        load_settings(env={}, env_file=env_file)
