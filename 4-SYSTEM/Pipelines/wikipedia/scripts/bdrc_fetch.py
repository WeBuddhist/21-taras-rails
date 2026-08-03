#!/usr/bin/env python3
"""Prefill source metadata from the BDRC API — the canonical pipeline's ``bdrc_fetch.py``.

Step 1 of docs/reference/cowork-pipeline.md: **metadata is fetched, never recalled from
model memory.** Given BDRC RIDs (W/MW/WA/IE…), this queries the public JSON-LD endpoint,
follows the scan → instance → work → creator → person chain, and prints one JSON object
per RID with titles, authors (name + life dates), and a derived ``copyright`` hint:

    public-domain        author died 70+ years ago
    copyrighted          author died within the last 70 years
    copyrighted-assumed  no death year found — flag for human review, per the step-1
                         prompt's "never invent metadata" rule

The output is meant to be read by a human (or by Claude in /ingest) while filling
``sources.yaml`` fields (``bdrc_id``, ``author``, ``author_dates``, ``copyright``); it
writes nothing itself. stdlib only, no API key.

Usage:
    python scripts/bdrc_fetch.py W22084 MW23703 …
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import date
from typing import Any

BDRC = "http://purl.bdrc.io/resource/"
CORE = "http://purl.bdrc.io/ontology/core/"
PREF_LABEL = "http://www.w3.org/2004/02/skos/core#prefLabel"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
PD_YEARS = 70

_cache: dict[str, dict[str, Any]] = {}


def fetch_graph(rid: str) -> dict[str, Any]:
    """The full JSON-LD graph for one resource, keyed by URI (bnodes included)."""
    if rid not in _cache:
        req = urllib.request.Request(
            f"https://purl.bdrc.io/resource/{rid}.json",
            headers={"User-Agent": "kangyur-wiki bdrc_fetch (IATS-2026 pipeline)"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            _cache[rid] = json.load(resp)
    return _cache[rid]


def values(node: dict[str, Any] | None, predicate: str) -> list[dict[str, Any]]:
    return list((node or {}).get(predicate) or [])


def uris(node: dict[str, Any] | None, predicate: str) -> list[str]:
    return [v["value"] for v in values(node, predicate) if v.get("type") == "uri"]


def literals(node: dict[str, Any] | None, predicate: str) -> list[dict[str, Any]]:
    return [v for v in values(node, predicate) if v.get("type") == "literal"]


def rid_of(uri: str) -> str:
    return uri.rsplit("/", 1)[-1]


def node_for(graph: dict[str, Any], uri: str) -> dict[str, Any] | None:
    """The node for ``uri``, fetching its own record if it is not in this graph."""
    if uri in graph:
        return graph[uri]
    if uri.startswith(BDRC):
        try:
            other = fetch_graph(rid_of(uri))
        except Exception:
            return None
        return other.get(uri)
    return None


def labels(node: dict[str, Any] | None) -> list[str]:
    seen: dict[str, None] = {}
    for lit in literals(node, PREF_LABEL):
        text = lit.get("value", "").strip()
        if text:
            seen.setdefault(f"{text} ({lit.get('lang', '')})", None)
    return list(seen)


def person_dates(graph: dict[str, Any], person_uri: str) -> tuple[str, int | None]:
    """``("1357–1419", 1419)`` from a person's event nodes, best effort."""
    person = node_for(graph, person_uri)
    birth = death = None
    for event_uri in uris(person, CORE + "personEvent"):
        event = node_for(graph, event_uri)
        kinds = uris(event, RDF_TYPE)
        year_lits = literals(event, CORE + "onYear") or literals(event, CORE + "eventWhen")
        year = year_lits[0]["value"] if year_lits else None
        if not year:
            continue
        if any(k.endswith("PersonBirth") for k in kinds):
            birth = year
        if any(k.endswith("PersonDeath") for k in kinds):
            death = year
    text = f"{birth or '?'}–{death or '?'}" if (birth or death) else ""
    try:
        death_year: int | None = int(str(death)[:4]) if death else None
    except ValueError:
        death_year = None
    return text, death_year


def copyright_hint(death_years: list[int | None]) -> str:
    """The step-1 router value. Uncertain death dates never default to public-domain."""
    if not death_years or any(y is None for y in death_years):
        return "copyrighted-assumed  # TODO: no death year on BDRC — verify by hand"
    if all(date.today().year - y >= PD_YEARS for y in death_years if y is not None):
        return "public-domain"
    return "copyrighted"


def describe(rid: str) -> dict[str, Any]:
    graph = fetch_graph(rid)
    uri = BDRC + rid
    node = graph.get(uri)
    if node is None:
        return {"rid": rid, "error": "no such resource on BDRC"}

    out: dict[str, Any] = {"rid": rid, "titles": labels(node)}

    # Scan → instance (MW) → abstract work (WA); each hop is optional.
    instance_uri = next(iter(uris(node, CORE + "instanceReproductionOf")), None) or uri
    instance = node_for(graph, instance_uri)
    if instance_uri != uri:
        out["instance"] = rid_of(instance_uri)
        out["titles"] = out["titles"] or labels(instance)
    work_uri = next(iter(uris(instance, CORE + "instanceOf")), None)
    work = node_for(graph, work_uri) if work_uri else None
    if work_uri:
        out["work"] = rid_of(work_uri)
        out["titles"] = out["titles"] or labels(work)

    authors: list[dict[str, str]] = []
    death_years: list[int | None] = []
    for holder in (work, instance, node):
        for creator_uri in uris(holder, CORE + "creator"):
            creator = node_for(graph, creator_uri)
            for agent_uri in uris(creator, CORE + "agent"):
                dates, death_year = person_dates(graph, agent_uri)
                authors.append(
                    {
                        "rid": rid_of(agent_uri),
                        "name": "; ".join(labels(node_for(graph, agent_uri))),
                        "dates": dates,
                    }
                )
                death_years.append(death_year)
        if authors:
            break
    out["authors"] = authors
    out["copyright"] = copyright_hint(death_years) if authors else (
        "copyrighted-assumed  # TODO: no author on BDRC record — verify by hand"
    )

    volumes = literals(node, CORE + "numberOfVolumes")
    if volumes:
        out["volumes"] = volumes[0]["value"]
    out["show_url"] = f"https://library.bdrc.io/show/bdr:{rid}"
    return out


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    results = []
    for rid in argv:
        try:
            results.append(describe(rid.strip()))
        except Exception as exc:  # noqa: BLE001 - report per-RID, keep going
            results.append({"rid": rid, "error": str(exc)})
    json.dump(results, sys.stdout, ensure_ascii=False, indent=1)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
