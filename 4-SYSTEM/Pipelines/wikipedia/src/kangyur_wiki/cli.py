"""Command line for the pipeline.

One subcommand per stage, in the order they run. Every command works on a corpus directory
under ``corpora/`` and records what it did in that corpus's ledger, so a run can be stopped
and resumed at any stage.

Nothing here writes to Wikipedia without ``--execute``.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import typer

from . import registry as registry_mod
from .config import load_settings
from .ledger import Ledger, LedgerEntry, TermStatus, ledger_path
from .stages import align as align_mod
from .stages.localwiki import emit_local_wiki
from .stages.pipeline import (
    Passage,
    TermArtifacts,
    load_claims,
    preserve_artifact,
    record_stage_model,
    run_audit,
    run_claims,
    run_draft,
    run_extract,
    run_organize,
    run_polish,
    run_update,
    run_verify,
)

app = typer.Typer(
    add_completion=False,
    help="Generate cited Tibetan Wikipedia articles from a root text and its commentaries.",
)


#: Categories the emitter is allowed to place an article in.  ``prompts/06-draft``
#: targets ནང་བསྟན།; articles drafted by the vault's own ``wiki-article-from-claims``
#: skill use bo.wikipedia's existing ནང་ཆོས། instead.  Both are real categories on the
#: wiki, so both are allowed rather than one being rewritten into the other — which
#: category an article belongs in is an editorial call, not the gate's.
DEFAULT_CATEGORIES: tuple[str, ...] = ("ནང་བསྟན།", "ནང་ཆོས།")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _corpus_dir(corpus: str) -> Path:
    return load_settings().corpus_dir(corpus)


def _echo_path(label: str, path: Path) -> None:
    typer.echo(f"  {label}: {path}")


def _resolve_source(local_path: Path | str) -> Path:
    """A registry ``local_path`` as an absolute path.

    Entries are written vault-relative (``1-SOURCES/Commentaries/….md``) so the
    registry reads the same from anywhere in the vault.  An absolute path is
    taken as given; a legacy corpus-relative one still resolves against the
    pipeline root.
    """
    path = Path(local_path)
    if path.is_absolute():
        return path
    from .config import repo_root, vault_root

    for base in (vault_root(), repo_root()):
        candidate = base / path
        if candidate.exists():
            return candidate
    return vault_root() / path


def _corpus_texts(corpus: str) -> tuple[Path, dict[str, Path]]:
    """``(root_text, {source_id: commentary_path})`` for one corpus.

    The binding between a corpus and the vault lives in its ``sources.yaml``:
    every entry names the ``1-SOURCES/`` file it stands for.  That is what lets
    ``source_id`` stay a stable siglum (``TARAC02_DGT_bo_segmented``) while the
    file it points at is a Tibetan-titled source file the rails work owns —
    citations and existing artifacts do not move when a file is renamed.

    Falls back to the vault's commentaries directory, keyed by filename stem,
    for a corpus whose registry has no ``local_path`` yet.
    """
    settings = load_settings()
    reg = registry_mod.load(settings.corpus_dir(corpus))
    root: Path | None = None
    commentaries: dict[str, Path] = {}
    for source in reg.sources:
        if source.local_path is None:
            continue
        path = _resolve_source(source.local_path)
        if source.source_id == "root":
            root = path
        else:
            commentaries[source.source_id] = path
    if root is None:
        texts = sorted(settings.source_text_dir.glob("*.md"))
        root = texts[0] if texts else settings.source_text_dir / "root.md"
    if not commentaries:
        commentaries = {p.stem: p for p in sorted(settings.source_commentaries_dir.glob("*.md"))}
    return root, commentaries


def _source_loaders(commentaries: dict[str, Path]):
    """``(raw, reading)`` loaders for a corpus's commentaries, by ``source_id``.

    Two views of the same file, for two different jobs:

    ``raw``      the bytes on disk, block IDs and anchors included. This is what
                 :func:`~kangyur_wiki.stages.align.segments_for_term` parses, because
                 the scaffolding is exactly what it is looking for.
    ``reading``  the same file with every layer of ingest scaffolding taken off.
                 This is what the verify gate compares quotations against: a
                 quotation spanning a block boundary must not fail on a caret the
                 pipeline itself wrote in the margin.
    """
    from .stages.commentary import reading_view

    def raw(source_id: str) -> str:
        path = commentaries.get(source_id)
        if path is None:
            # Sigla drift (a trailing ``_bo_segmented``, an edition suffix); match
            # on containment the way the directory-glob loader used to.
            for key, candidate in sorted(commentaries.items()):
                if source_id in key or key in source_id:
                    path = candidate
                    break
        if path is None or not path.exists():
            raise FileNotFoundError(f"no commentary file matching source_id {source_id!r}")
        return path.read_text(encoding="utf-8")

    def reading(source_id: str) -> str:
        return reading_view(raw(source_id))

    return raw, reading


# ---------------------------------------------------------------------------


@app.command()
def commentaries(
    corpus: str = typer.Argument(..., help="Corpus id, e.g. tara21"),
    only: Optional[str] = typer.Option(
        None, help="Process only files whose name contains this (e.g. TARAC02)."
    ),
    skip_toc: bool = typer.Option(
        False, "--skip-toc", help="Skip the sa-bcad heading pass. No model call, no headings."
    ),
    skip_refine: bool = typer.Option(
        False, "--skip-refine", help="Skip stage-2 refinement (use when already refined)."
    ),
    promote: bool = typer.Option(
        True, help="Write the finished files back over 1-SOURCES/Commentaries/. --no-promote to review first."
    ),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
) -> None:
    """Stage 1b — make a segmented commentary citable: headings, anchors, block IDs.

    ``commentary-segmentation`` leaves blocks and nothing else. This adds, per file:
    stage-2 refinement, sa-bcad headings (``tag-inline-toc``), root-verse transclusion
    anchors, and a block ID on every content block. Intermediates land in
    ``work/ingest/commentaries/`` so each step is inspectable; the finished file is copied
    back over ``1-SOURCES/Commentaries/`` only if every step held.

    The invariant that makes this safe to run over a whole corpus: the *reading view* of a
    file — its text with every layer of scaffolding taken back off — must be byte-identical
    before and after. A file that fails it is left alone and reported.
    """
    from .stages import commentary as comm_mod

    settings = load_settings()
    cdir = _corpus_dir(corpus)
    root, comm_paths = _corpus_texts(corpus)
    if not root.exists():
        raise typer.BadParameter(f"no root text at {root}")

    paths = [p for _, p in sorted(comm_paths.items()) if not only or only in p.name]
    if not paths:
        raise typer.BadParameter(
            f"no commentaries matching {only!r} in {settings.source_commentaries_dir}"
        )

    work = cdir / "work" / "ingest" / "commentaries"
    work.mkdir(parents=True, exist_ok=True)

    build_toc = None
    if not skip_toc:
        from .llm.gemini import GeminiClient, PromptLibrary

        client = GeminiClient(
            api_key=settings.require_gemini_api_key(), model=model or settings.gemini_model
        )
        library = PromptLibrary(settings.prompts_dir)
        build_toc = (client.generate, lambda stage, **kw: library.render(stage, **kw))

    results = []
    for path in paths:
        typer.echo(f"— {path.stem}")
        outcome = comm_mod.prepare_file(
            path,
            root=root,
            work_dir=work,
            toc=build_toc,
            refine=not skip_refine,
        )
        results.append(outcome)
        for line in outcome.format_lines():
            typer.echo(f"    {line}")

    ok = [r for r in results if r.ok]
    if promote:
        for outcome in ok:
            outcome.promote()

    report_path = work.parent / "COMMENTARY_REPORT.md"
    report_path.write_text(
        comm_mod.format_corpus_report(corpus, results, promoted=promote), encoding="utf-8"
    )

    typer.echo("")
    typer.echo(f"{len(ok)}/{len(results)} files completed" + (" and promoted" if promote else ""))
    failed = [r for r in results if not r.ok]
    for outcome in failed:
        typer.echo(f"  FAILED  {outcome.name}: {outcome.failure}")
    _echo_path("report", report_path)
    if promote and ok:
        typer.echo("")
        typer.echo(f"Re-run `kwiki align {corpus}` — the anchors have changed.")
    if failed:
        raise typer.Exit(code=1)


@app.command()
def align(
    corpus: str = typer.Argument(..., help="Corpus id, e.g. spyodjug"),
    min_score: float = typer.Option(
        align_mod.MIN_CLUSTER_SCORE,
        help="Cluster score below which a probe match is not trusted. Precision-first.",
    ),
) -> None:
    """Stage 2 — align the root text with every commentary, and report coverage.

    Read the coverage table before going further: a commentary with low coverage will
    contribute little to the articles, and a word-commentary may need the LLM pass.
    """
    cdir = _corpus_dir(corpus)
    root, paths = _corpus_texts(corpus)
    if not root.exists():
        raise typer.BadParameter(f"no root text at {root}")
    if not paths:
        raise typer.BadParameter(
            f"no commentaries in {load_settings().source_commentaries_dir}"
        )

    report = align_mod.align_corpus(root, paths, corpus, min_score=min_score)
    out = cdir / "work" / "aligned.json"
    align_mod.save_alignment(report, out)

    typer.echo(report.format_summary())
    typer.echo("")
    _echo_path("written", out)


@app.command()
def terms(
    corpus: str = typer.Argument(...),
    limit: int = typer.Option(0, help="Seed only the first N terms (0 = all)."),
) -> None:
    """Stage 3 — seed the ledger from the corpus term list.

    The team's registry already carries a curated term list per corpus, so this reads
    ``terms.yaml`` rather than re-deriving one. Statistical selection
    (``tibetan.keyness``) is for corpora that have no such list yet.
    """
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)
    names = [t.term for t in reg.terms]
    if limit:
        names = names[:limit]
    if not names:
        raise typer.BadParameter(f"no terms in {cdir}/terms.yaml")

    led = Ledger.load(ledger_path(load_settings().corpora_dir, corpus), corpus_id=corpus)
    led.seed(names, _now())
    led.save()

    typer.echo(f"{len(names)} terms seeded into the ledger")
    already = sum(1 for t in reg.terms if t.exists_on_wiki)
    typer.echo(f"  {already} of {len(reg.terms)} already have a bo.wikipedia article (update path)")
    _echo_path("ledger", ledger_path(load_settings().corpora_dir, corpus))


@app.command()
def article(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(..., help="The key term to write about"),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
    polish: bool = typer.Option(
        False,
        "--polish",
        help="Run the optional stage-6a literary rewrite between draft and audit.",
    ),
    audit_model: Optional[str] = typer.Option(
        None,
        "--audit-model",
        help="Run the stage-6b audit on a different model than the one that drafted. "
        "Canonically the auditor is never the writer — see the note this prints.",
    ),
) -> None:
    """Stages 4–7 — extract → claims → outline → draft [→ polish] → audit → verify.

    The claims table (stage 4b) is the only drafting input from there on; the audit
    (stage 6b) reads the drafted text back against it; the deterministic verify gate
    runs last either way. Reports are written even on failure, so a failure is
    diagnosable without re-running.
    """
    from .llm.gemini import GeminiClient, PromptLibrary  # imported late: needs an API key

    settings = load_settings()
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)

    alignment_path = cdir / "work" / "aligned.json"
    if not alignment_path.exists():
        raise typer.BadParameter(f"run `kwiki align {corpus}` first — no {alignment_path}")
    alignment = align_mod.load_alignment(alignment_path)

    client = GeminiClient(
        api_key=settings.require_gemini_api_key(), model=model or settings.gemini_model
    )
    library = PromptLibrary(settings.prompts_dir)

    def prompt_render(stage: str, **kwargs) -> str:
        return library.render(stage, **kwargs)

    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    led = Ledger.load(ledger_path(settings.corpora_dir, corpus), corpus_id=corpus)
    raw_source, reading_source = _source_loaders(_corpus_texts(corpus)[1])

    prompt_stages = ["04-extract", "04b-claims", "05-organize", "06-draft", "06b-audit"]
    if polish:
        prompt_stages.insert(4, "06a-polish")
    artifacts.ensure()
    # A fresh run resets model.json — preserve the outgoing one first: it may
    # carry another run's provenance (stand-in notes, fix_passes, stage_models).
    preserve_artifact(artifacts.model)
    artifacts.model.write_text(
        json.dumps(
            {
                "model": client.model,
                "run_at": _now(),
                "prompts": {stage: library.get(stage).path.name for stage in prompt_stages},
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    typer.echo(f"— {term}")

    passages = run_extract(
        term, alignment, client.generate, prompt_render, artifacts, source_loader=raw_source
    )
    located = sum(1 for p in passages if p.segment_id)
    typer.echo(f"  extract:  {len(passages)} passages, {located} with a block locator")
    if not passages:
        led.set_status(term, TermStatus.FAILED, _now(), error="no commentary material found")
        led.save()
        raise typer.Exit(code=1)
    led.set_status(term, TermStatus.EXTRACTED, _now())

    claims = run_claims(term, passages, reg, client.generate, prompt_render, artifacts)
    sub_consensus = sum(1 for c in claims if c.claim_type != "consensus")
    typer.echo(f"  claims:   {len(claims)} claims, {sub_consensus} below consensus")
    if not claims:
        led.set_status(term, TermStatus.FAILED, _now(), error="no claims survived stage 4b")
        led.save()
        raise typer.Exit(code=1)
    led.set_status(term, TermStatus.CLAIMED, _now())

    organization = run_organize(term, claims, client.generate, prompt_render, artifacts)
    gap_lines = len(organization.get("gap_report", []))
    typer.echo(
        f"  outline:  {len(organization.get('sections', []))} sections"
        + (f", {gap_lines} gap-report lines" if gap_lines else "")
    )
    led.set_status(term, TermStatus.ORGANIZED, _now())

    wikitext, citations = run_draft(
        term, passages, claims, organization, reg, client.generate, prompt_render, artifacts
    )
    typer.echo(f"  draft:    {len(wikitext)} chars, {len(citations)} citations")
    led.set_status(term, TermStatus.DRAFTED, _now())

    draft_data = json.loads(artifacts.draft.read_text(encoding="utf-8"))
    if polish:
        polish_result = run_polish(
            term, passages, claims, reg, client.generate, prompt_render, artifacts
        )
        if polish_result.accepted:
            wikitext, citations = polish_result.wikitext, polish_result.citations
            draft_data = json.loads(artifacts.polished.read_text(encoding="utf-8"))
            typer.echo(f"  polish:   accepted, {len(wikitext)} chars")
        else:
            typer.echo("  polish:   REJECTED — structure changed; keeping the unpolished draft")
            for p in polish_result.structure_problems:
                typer.echo(f"            - {p}")

    # Canonically the auditor is never the writer (cowork-pipeline steps 10–12: Claude
    # drafts, Gemini restyles, Claude audits). A model is a poor judge of its own drift,
    # so when the same model does both, say so rather than let a clean audit read as
    # stronger evidence than it is.
    auditor = client
    if audit_model and audit_model != client.model:
        from .llm.gemini import GeminiClient  # already imported above; explicit for clarity

        auditor = GeminiClient(api_key=settings.require_gemini_api_key(), model=audit_model)
    audit = run_audit(term, draft_data, claims, auditor.generate, prompt_render, artifacts)
    _record_stage_model(artifacts, auditor, library, "06b-audit")
    if auditor.model == client.model:
        typer.echo(
            f"  note:     the audit ran on {auditor.model} — the model that wrote the draft. "
            "Same-model audits miss the writer's own drift; use --audit-model, or run the "
            "audit through Claude (scripts/claude_article.py prompt/apply <term> audit)."
        )
    if audit.passed:
        typer.echo(f"  audit:    publish ({len(audit.findings)} findings, none blocking)")
        led.set_status(term, TermStatus.AUDITED, _now())
    else:
        typer.echo(
            f"  audit:    {audit.verdict or 'no verdict'} — {len(audit.blocking)} blocking "
            f"of {len(audit.findings)} findings"
        )
        led.set_status(term, TermStatus.FAILED, _now(), error="audit found blocking issues")

    result = run_verify(
        term, wikitext, citations, list(DEFAULT_CATEGORIES), reading_source, artifacts,
        raw_loader=raw_source,
    )
    if result.passed:
        detail = f"PASS — {result.located}/{result.total_citations} citations block-located"
        if result.locator_failures:
            detail += f", {len(result.locator_failures)} locators wrong"
        typer.echo(f"  verify:   {detail}")
        if audit.passed:
            led.set_status(term, TermStatus.VERIFIED, _now())
    else:
        n_err = sum(1 for f in result.findings if f.severity == "error")
        typer.echo(
            f"  verify:   FAIL — {n_err} errors, {len(result.quote_failures)} unverifiable quotations"
        )
        led.set_status(term, TermStatus.FAILED, _now(), error="verification failed")
    led.save()

    _echo_path("article", artifacts.wikitext)
    _echo_path("audit", artifacts.audit_report)
    _echo_path("report", artifacts.report)

    if result.passed and audit.passed:
        # Both gates cleared — offer the same grounding material to the vault's own
        # rails folder. Never fatal: a verified, audited article must still be
        # reported as such even if this rendering step has a problem of its own.
        try:
            lw = emit_local_wiki(term, corpus, artifacts, reg, settings.local_wiki_dir, model=client.model, run_at=_now())
            typer.echo(
                f"  local-wiki: {lw.commentaries_cited} commentaries, {lw.attestations} attestations"
            )
            _echo_path("local-wiki", lw.path)
        except Exception as exc:  # noqa: BLE001 - a rendering problem is not a verify failure
            typer.echo(f"  local-wiki: skipped ({type(exc).__name__}: {exc})")
    else:
        raise typer.Exit(code=1)


def _load_passages(artifacts: TermArtifacts) -> list[Passage]:
    """Read ``extract.json`` back for a stage run resumed from disk."""
    data = json.loads(artifacts.extract.read_text(encoding="utf-8"))
    return [
        Passage(
            source_id=p.get("source_id", ""),
            quote=p.get("quote", ""),
            kind=p.get("kind", ""),
            segment_id=p.get("segment_id", ""),
            note=p.get("note", ""),
        )
        for p in data.get("passages", [])
        if p.get("quote")
    ]


def _model_and_prompts(model: Optional[str]):
    """A ``(generate, prompt_render, client, library)`` tuple for a standalone stage command."""
    from .llm.gemini import GeminiClient, PromptLibrary  # imported late: needs an API key

    settings = load_settings()
    client = GeminiClient(
        api_key=settings.require_gemini_api_key(), model=model or settings.gemini_model
    )
    library = PromptLibrary(settings.prompts_dir)

    def prompt_render(stage: str, **kwargs) -> str:
        return library.render(stage, **kwargs)

    return client.generate, prompt_render, client, library


def _record_stage_model(artifacts: TermArtifacts, client, library, stage: str) -> None:
    """Log this stage's model + prompt version — same writer the scripts use."""
    record_stage_model(
        artifacts, stage, model=client.model, prompt=library.get(stage).path.name, run_at=_now()
    )


@app.command()
def claims(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(...),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
) -> None:
    """Stage 4b alone — rebuild the atomic claims table from ``extract.json``.

    The claims table is the only drafting input downstream (invariant 1), so a re-run
    invalidates any later artifacts: re-run outline, draft, audit and verify after it.
    """
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    if not artifacts.extract.exists():
        raise typer.BadParameter(f"no {artifacts.extract} — run `kwiki article` or extract first")

    generate, prompt_render, client, library = _model_and_prompts(model)
    passages = _load_passages(artifacts)
    result = run_claims(term, passages, reg, generate, prompt_render, artifacts)
    _record_stage_model(artifacts, client, library, "04b-claims")

    led = Ledger.load(ledger_path(load_settings().corpora_dir, corpus), corpus_id=corpus)
    led.set_status(
        term,
        TermStatus.CLAIMED if result else TermStatus.FAILED,
        _now(),
        error=None if result else "no claims survived stage 4b",
    )
    led.save()

    by_type: dict[str, int] = {}
    for c in result:
        by_type[c.claim_type] = by_type.get(c.claim_type, 0) + 1
    typer.echo(f"{len(result)} claims from {len(passages)} passages")
    for kind, count in sorted(by_type.items(), key=lambda kv: -kv[1]):
        typer.echo(f"  {kind:<22} {count}")
    _echo_path("claims", artifacts.claims)
    typer.echo("Downstream artifacts are now stale — re-run outline → draft → audit → verify.")


@app.command()
def polish(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(...),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
) -> None:
    """Stage 6a alone — the optional literary rewrite (the canonical gemini_polish.py).

    Hard constraints are enforced in code: if the stylist changes any citations array,
    paragraph count, heading order, or see-also, the rewrite is rejected and nothing on
    disk changes. After an accepted polish, re-run `kwiki audit` and `kwiki verify`.
    """
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    for needed in (artifacts.draft, artifacts.claims, artifacts.extract):
        if not needed.exists():
            raise typer.BadParameter(f"no {needed} — run the earlier stages first")

    generate, prompt_render, client, library = _model_and_prompts(model)
    result = run_polish(
        term, _load_passages(artifacts), load_claims(artifacts), reg,
        generate, prompt_render, artifacts,
    )
    _record_stage_model(artifacts, client, library, "06a-polish")
    if result.accepted:
        typer.echo(f"polish accepted ({client.model}) — {len(result.wikitext)} chars")
        _echo_path("polished", artifacts.polished)
        _echo_path("article", artifacts.wikitext)
        typer.echo("Re-run `kwiki audit` and `kwiki verify` — the prose changed.")
    else:
        typer.echo("polish REJECTED — the stylist broke a hard constraint; nothing was changed:")
        for p in result.structure_problems:
            typer.echo(f"  - {p}")
        raise typer.Exit(code=1)


@app.command()
def audit(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(...),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
) -> None:
    """Stage 6b alone — re-audit the drafted text against the claims table.

    Audits the polished draft when one exists, else the stage-6 draft. Blocking findings
    (added facts, attribution loss) fail the run; nothing publishes without a pass here
    AND a pass from the deterministic `kwiki verify` gate.
    """
    cdir = _corpus_dir(corpus)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    for needed in (artifacts.draft, artifacts.claims):
        if not needed.exists():
            raise typer.BadParameter(f"no {needed} — run the earlier stages first")

    source = artifacts.polished if artifacts.polished.exists() else artifacts.draft
    draft_data = json.loads(source.read_text(encoding="utf-8"))

    generate, prompt_render, client, library = _model_and_prompts(model)
    result = run_audit(term, draft_data, load_claims(artifacts), generate, prompt_render, artifacts)
    _record_stage_model(artifacts, client, library, "06b-audit")

    led = Ledger.load(ledger_path(load_settings().corpora_dir, corpus), corpus_id=corpus)
    led.set_status(
        term,
        TermStatus.AUDITED if result.passed else TermStatus.FAILED,
        _now(),
        error=None if result.passed else "audit found blocking issues",
    )
    led.save()

    typer.echo(f"audited {source.name}: verdict {result.verdict or 'missing'} — "
               f"{len(result.blocking)} blocking of {len(result.findings)} findings")
    _echo_path("audit", artifacts.audit_report)
    if not result.passed:
        raise typer.Exit(code=1)


@app.command()
def update(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(..., help="A term whose bo.wikipedia article already exists"),
    from_file: Optional[Path] = typer.Option(
        None,
        help="Read the existing article's wikitext from a file instead of the live wiki.",
    ),
    model: Optional[str] = typer.Option(None, help="Override the Gemini model id"),
) -> None:
    """The update path — merge new commentary material into an existing article.

    This is the majority case (520 of 545 spyodjug terms already have an article). New
    passages are classified against the live article — duplicate / new / conflict — and
    only safe insertions are applied; conflicts are flagged ⚑ for you, never auto-merged.
    Reads the wiki anonymously; nothing is written to Wikipedia here (that stays behind
    `kwiki publish --execute`).
    """
    from .llm.gemini import GeminiClient, PromptLibrary  # imported late: needs an API key

    settings = load_settings()
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)

    alignment_path = cdir / "work" / "aligned.json"
    if not alignment_path.exists():
        raise typer.BadParameter(f"run `kwiki align {corpus}` first — no {alignment_path}")
    alignment = align_mod.load_alignment(alignment_path)

    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    led = Ledger.load(ledger_path(settings.corpora_dir, corpus), corpus_id=corpus)

    # The existing article: an explicit file wins, then a prior snapshot, then the wiki.
    if from_file is not None:
        existing = from_file.read_text(encoding="utf-8")
        origin = str(from_file)
    elif artifacts.existing_wiki.exists():
        existing = artifacts.existing_wiki.read_text(encoding="utf-8")
        origin = f"{artifacts.existing_wiki} (prior snapshot; delete it to re-fetch)"
    else:
        from .wiki.client import WikiClient

        wiki = WikiClient(site=settings.wiki_site, dry_run=True)
        resolution = wiki.resolve_title(term.strip("།་"))
        if not resolution.exists:
            raise typer.BadParameter(
                f"no bo.wikipedia article exists for {term} under any title variant — "
                "this term takes the create path: `kwiki article`"
            )
        title = resolution.final_title or resolution.matched_variant or term
        existing = wiki.get_wikitext(title) or ""
        origin = f"https://{settings.wiki_site}/wiki/{title}"
    if not existing.strip():
        raise typer.BadParameter(f"existing article from {origin} is empty")

    typer.echo(f"— {term}")
    typer.echo(f"  existing: {origin} ({len(existing)} chars)")

    client = GeminiClient(
        api_key=settings.require_gemini_api_key(), model=model or settings.gemini_model
    )
    library = PromptLibrary(settings.prompts_dir)

    def prompt_render(stage: str, **kwargs) -> str:
        return library.render(stage, **kwargs)

    raw_source, reading_source = _source_loaders(_corpus_texts(corpus)[1])

    if artifacts.extract.exists():
        data = json.loads(artifacts.extract.read_text(encoding="utf-8"))
        passages = [
            Passage(
                source_id=p.get("source_id", ""),
                quote=p.get("quote", ""),
                kind=p.get("kind", ""),
                segment_id=p.get("segment_id", ""),
                note=p.get("note", ""),
            )
            for p in data.get("passages", [])
            if p.get("quote")
        ]
        typer.echo(f"  extract:  {len(passages)} passages (reused {artifacts.extract.name})")
    else:
        passages = run_extract(
            term, alignment, client.generate, prompt_render, artifacts, source_loader=raw_source
        )
        typer.echo(f"  extract:  {len(passages)} passages")
    if not passages:
        led.set_status(term, TermStatus.FAILED, _now(), error="no commentary material found")
        led.save()
        raise typer.Exit(code=1)
    led.set_status(term, TermStatus.EXTRACTED, _now())

    merge_result, verification = run_update(
        term,
        existing,
        passages,
        reg,
        client.generate,
        prompt_render,
        artifacts,
        allowed_categories=list(DEFAULT_CATEGORIES),
        source_loader=reading_source,
    )
    typer.echo(
        f"  merge:    {len(merge_result.applied)} applied, {len(merge_result.skipped)} skipped, "
        f"{len(merge_result.conflicts)} ⚑ conflicts"
    )
    led.set_status(term, TermStatus.DRAFTED, _now())

    if verification.passed:
        suffix = " (⚑ conflicts await your call — see the report)" if merge_result.conflicts else ""
        typer.echo(f"  verify:   PASS{suffix}")
        led.set_status(term, TermStatus.VERIFIED, _now())
    else:
        n_err = sum(
            1
            for f in verification.findings
            if f.severity == "error" and f.rule in {"V1", "V3", "V4", "V5"}
        )
        typer.echo(
            f"  verify:   FAIL — {n_err} blocking findings, "
            f"{len(verification.quote_failures)} unverifiable quotations"
        )
        led.set_status(term, TermStatus.FAILED, _now(), error="merge verification failed")
    led.save()

    _echo_path("merged", artifacts.wikitext)
    _echo_path("merge report", artifacts.update_report)
    _echo_path("verify report", artifacts.report)
    if not verification.passed:
        raise typer.Exit(code=1)


@app.command()
def verify(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(...),
    category: list[str] = typer.Option(
        list(DEFAULT_CATEGORIES),
        "--category",
        help="Allowed category, repeatable. The default is what the drafting prompt targets; "
        "articles drafted outside the chain may carry another of bo.wikipedia's own categories.",
    ),
) -> None:
    """Stage 7 alone — re-run the gate over an already-drafted article."""
    from .wiki.wikitext import Citation

    cdir = _corpus_dir(corpus)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    if not artifacts.wikitext.exists():
        raise typer.BadParameter(f"no drafted article at {artifacts.wikitext}")

    wikitext = artifacts.wikitext.read_text(encoding="utf-8")
    citations = [Citation(**c) for c in json.loads(artifacts.citations.read_text("utf-8"))]
    raw_source, reading_source = _source_loaders(_corpus_texts(corpus)[1])

    result = run_verify(
        term, wikitext, citations, list(category), reading_source, artifacts,
        raw_loader=raw_source,
    )
    typer.echo(result.format_report())
    raise typer.Exit(code=0 if result.passed else 1)


@app.command()
def publish(
    corpus: str = typer.Argument(...),
    term: str = typer.Argument(...),
    sandbox: bool = typer.Option(True, help="Publish to your userspace sandbox, not mainspace."),
    execute: bool = typer.Option(
        False, "--execute", help="Actually write to Wikipedia. Without this it is a dry run."
    ),
) -> None:
    """Stage 8 — create or update the article on bo.wikipedia.

    Refuses to publish anything that has not passed verification. Dry run by default;
    ``--execute`` is the only way to make a real edit.
    """
    from .wiki.client import WikiClient, sandbox_title
    from .wiki.wikitext import Citation

    settings = load_settings()
    cdir = _corpus_dir(corpus)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    if not artifacts.wikitext.exists():
        raise typer.BadParameter(f"no article at {artifacts.wikitext}")

    led = Ledger.load(ledger_path(settings.corpora_dir, corpus), corpus_id=corpus)
    entry = led.get(term)
    if entry is None or entry.status not in {TermStatus.VERIFIED, TermStatus.APPROVED, TermStatus.PUBLISHED}:
        status = entry.status.value if entry else "unknown"
        raise typer.BadParameter(
            f"{term} is {status}; only a verified article may be published. Run `kwiki verify` first."
        )

    wikitext = artifacts.wikitext.read_text(encoding="utf-8")
    username, password = settings.require_wiki_credentials()

    client = WikiClient(site=settings.wiki_site, dry_run=not execute)
    client.login(username, password)

    title = sandbox_title(username.split("@")[0], term.strip("།་")) if sandbox else term
    resolution = client.resolve_title(title)

    summary = f"[[Wikipedia:IATS-2026|pipeline-assisted]] draft for {term}, human-reviewed"
    if resolution and resolution.exists:
        current = client.get_wikitext(resolution.title)
        plan = client.edit_page(
            resolution.title,
            wikitext,
            summary=summary,
            basetimestamp=current.timestamp if current else None,
            starttimestamp=None,
        )
        action = "update"
    else:
        plan = client.create_page(title, wikitext, summary=summary)
        action = "create"

    typer.echo(f"{'EXECUTED' if execute else 'DRY RUN'} — {action} {title}")
    typer.echo(json.dumps(plan, ensure_ascii=False, indent=1)[:800] if isinstance(plan, dict) else str(plan))

    if execute:
        led.set_status(term, TermStatus.PUBLISHED, _now(), wiki_title=title)
        led.save()


@app.command(name="local-wiki")
def local_wiki(corpus: str = typer.Argument(...), term: str = typer.Argument(...)) -> None:
    """Emit a verified article's grounding material to 2-RAILS/Local-Wiki/.

    Same status gate as `kwiki publish`: refuses a term that has not reached
    ``verified`` (or later) — a Local-Wiki candidate built from a draft that might
    still fail the deterministic gate is not worth writing. Re-running preserves the
    outgoing file to ``2-RAILS/Local-Wiki/history/`` first, the same convention every
    other per-stage artifact in this pipeline follows.
    """
    settings = load_settings()
    cdir = _corpus_dir(corpus)
    reg = registry_mod.load(cdir)
    artifacts = TermArtifacts(cdir / "articles" / term.strip("།་"))
    if not artifacts.wikitext.exists():
        raise typer.BadParameter(f"no drafted article at {artifacts.wikitext}")

    led = Ledger.load(ledger_path(settings.corpora_dir, corpus), corpus_id=corpus)
    entry = led.get(term)
    if entry is None or entry.status not in {TermStatus.VERIFIED, TermStatus.APPROVED, TermStatus.PUBLISHED}:
        status_value = entry.status.value if entry else "unknown"
        raise typer.BadParameter(
            f"{term} is {status_value}; only a verified article's material is emitted. "
            "Run `kwiki verify` first."
        )

    result = emit_local_wiki(term, corpus, artifacts, reg, settings.local_wiki_dir)
    typer.echo(
        f"{result.commentaries_cited} commentaries cited, {result.attestations} attestations, "
        f"{result.divergences} divergences"
    )
    for warning in result.warnings:
        typer.echo(f"  warning: {warning}")
    _echo_path("local-wiki", result.path)


@app.command()
def status(corpus: str = typer.Argument(...)) -> None:
    """Where every term in the corpus has got to."""
    led = Ledger.load(ledger_path(load_settings().corpora_dir, corpus), corpus_id=corpus)
    summary = led.summary()
    if not summary:
        typer.echo("ledger is empty — run `kwiki terms` first")
        return
    width = max(len(k) for k in summary)
    for key, count in sorted(summary.items(), key=lambda kv: -kv[1]):
        typer.echo(f"  {key:<{width}}  {count}")


if __name__ == "__main__":  # pragma: no cover
    app()
