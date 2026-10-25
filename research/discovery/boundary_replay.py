"""Replay the exact boundary-word comparison and its focused challenges.

Regenerates finite deterministic CSP outcomes and independently verifies all
retained positive geometry without rewriting the evidence. Solver exhaustion
is computational evidence on the recorded finite domains, not aperiodicity.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import time

from .boundary_screen import digest, run_batch, _effort_summary
from .boundary_verify import verify_batch

DEFAULT = Path(__file__).parent / "runs/boundary-m6-2026-10-24/manifest.json"


def _read_record(base, entry):
    path = (base / entry["path"]).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("Manifest record escapes its evidence directory.")
    raw = path.read_bytes()
    data = json.loads(raw)
    if data["result_sha256"] != entry["result_sha256"]:
        raise ValueError(f"Manifest hash differs from record: {path}")
    return path, raw, data


def replay_record(path, retained, *, fresh=True):
    checked = verify_batch(retained)
    if fresh:
        budgets = retained["budgets"]
        selected = retained["selection"]["pair_filter"]
        regenerated = run_batch(
            max_length=retained["provenance"]["max_length"],
            max_index=budgets["max_index"], radii=budgets["radii"],
            node_budget=budgets["node_budget"],
            propagation_budget=budgets["propagation_budget"],
            cpu_seconds=budgets["cpu_seconds_outer_cap"],
            pair_filter=selected,
        )
        regenerated["effort_summary"] = _effort_summary(regenerated)
        regenerated["result_sha256"] = digest(regenerated)
        if regenerated["result_sha256"] != retained["result_sha256"]:
            raise ValueError(f"Fresh finite search differs from retained run: {path}")
    return {"path":str(path), "result_sha256":retained["result_sha256"],
            "pairs":checked["pairs"], "verified_witnesses":checked["verified_witnesses"],
            "fresh_search_matched":fresh}


def replay(manifest_path=DEFAULT, *, fresh=True):
    started = time.perf_counter()
    manifest_raw = manifest_path.read_bytes()
    manifest = json.loads(manifest_raw)
    if manifest["schema"] != "arisearch.discovery.boundary-manifest.v1":
        raise ValueError("Unknown boundary experiment manifest schema.")
    expected_hash = digest({k:v for k,v in manifest.items() if k != "manifest_sha256"})
    if expected_hash != manifest["manifest_sha256"]:
        raise ValueError("Experiment manifest hash mismatch.")
    base = manifest_path.parent
    baseline_path, baseline_raw, baseline = _read_record(base, manifest["baseline"])
    if baseline["selection"]["pair_filter"] is not None:
        raise ValueError("Baseline is not the full bounded pair census.")
    seeds = {frozenset(r["tiles"]) for r in baseline["pairs"]
             if r["status"] == "SURVIVES_BOUNDED_SCREENS"}
    followed = set()
    final_counts = Counter(r["status"] for r in baseline["pairs"])
    records = [(baseline_path, baseline_raw, baseline)]
    for entry in manifest["followups"]:
        path, raw, data = _read_record(base, entry)
        if data["provenance"]["max_length"] != baseline["provenance"]["max_length"]:
            raise ValueError("Focused challenge changed the candidate library.")
        pair = frozenset(data["selection"]["pair_filter"] or ())
        if frozenset(entry["selected_pair"]) != pair:
            raise ValueError("Manifest selected pair differs from its focused record.")
        if pair not in seeds or pair in followed or len(data["pairs"]) != 1:
            raise ValueError("Focused challenges do not uniquely cover initial survivors.")
        followed.add(pair)
        final_counts["SURVIVES_BOUNDED_SCREENS"] -= 1
        final_counts[data["pairs"][0]["status"]] += 1
        records.append((path, raw, data))
    if followed != seeds:
        raise ValueError("Some initial survivor has no retained stronger challenge.")
    final_counts = {k:v for k,v in sorted(final_counts.items()) if v}
    if manifest["final_pair_status_counts"] != final_counts:
        raise ValueError("Final experiment funnel disagrees with the retained records.")
    if manifest["final_flags"] != final_counts.get("SURVIVES_BOUNDED_SCREENS", 0):
        raise ValueError("Manifest flag count disagrees with the final funnel.")
    checked = [replay_record(path,data,fresh=fresh) for path,raw,data in records]
    if manifest_path.read_bytes() != manifest_raw or any(path.read_bytes() != raw for path,raw,data in records):
        raise ValueError("Retained evidence changed during replay.")
    return {"status":"PASSED", "manifest_sha256":manifest["manifest_sha256"],
            "records":checked, "final_pair_status_counts":final_counts,
            "elapsed_seconds":round(time.perf_counter()-started,4),
            "scope":"Exact bounded library, finite CSP replay and independently checked positive geometry; evidence unchanged."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest",nargs="?",type=Path,default=DEFAULT)
    parser.add_argument("--verify-only",action="store_true",help="Check geometry, hashes and coverage without rerunning finite searches")
    args = parser.parse_args()
    print(json.dumps(replay(args.manifest,fresh=not args.verify_only),sort_keys=True))


if __name__ == "__main__":
    main()
