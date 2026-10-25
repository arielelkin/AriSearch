"""One bounded M8 calibration, using the preserved native boundary engine.

The baseline has a 600-process-CPU-second cap. All focused follow-ups share
one additional 600-process-CPU-second cap, including their singleton cache.
No bound is increased automatically beyond this experiment.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shlex
import sys
import time

from .boundary_render import write_gallery
from .boundary_screen import (StateBank, _effort_summary, canonical_json, digest,
                              run_batch, save_result, screen_pair, search_periodic)


def _source_snapshot(prior_path):
    prior = json.loads(prior_path.read_text())
    expected = prior["provenance"]["source_sha256"]
    directory = Path(__file__).parent
    current = {name: hashlib.sha256((directory/name).read_bytes()).hexdigest()
               for name in expected}
    if current != expected:
        raise RuntimeError("Preserved M6 source hashes no longer match; experiment was not started")
    return current


def _save_manifest(manifest, output_dir):
    manifest.pop("manifest_sha256", None)
    manifest["manifest_sha256"] = digest({key: value for key, value in manifest.items()
                                         if key != "execution"})
    temporary = output_dir / "manifest.json.tmp"
    temporary.write_text(canonical_json(manifest)+"\n")
    temporary.replace(output_dir / "manifest.json")


def _execution(command, cpu_start, wall_start):
    return {"command": command, "cpu_seconds": time.process_time()-cpu_start,
            "wall_seconds": time.perf_counter()-wall_start,
            "result_hash_scope": "all top-level fields except result_sha256 and execution"}


def _retained_summary(result, relative_path):
    return {"path": str(relative_path), "result_sha256": result["result_sha256"],
            "batch_complete": result["batch_complete"], "selection": result["selection"],
            "funnel": result["funnel"], "effort_summary": result["effort_summary"]}


def run_experiment(output_dir, *, prior_path, command):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    if (output_dir/"manifest.json").exists():
        raise ValueError("This one-shot output directory already has a manifest")
    preserved = _source_snapshot(prior_path)
    orchestrator_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    total_cpu, total_wall = time.process_time(), time.perf_counter()
    manifest = {"schema": "arisearch.discovery.length8-calibration.v1", "status": "RUNNING",
                "scope": "One M8 common-scale equiangular-120 length calibration; no M9 expansion; finite native honeycomb model only.",
                "orchestrator_source_sha256": orchestrator_hash,
                "preserved_source_sha256": preserved,
                "baseline_budget": {"max_length": 8, "max_index": 8, "radii": [1, 2, 4],
                                    "node_budget": 1000, "propagation_budget": 50000,
                                    "cpu_seconds": 600},
                "followup_budget": {"max_index": 16, "radii": [1, 2, 4, 8],
                                    "node_budget": 10000, "propagation_budget": 500000,
                                    "cpu_seconds_shared_total": 600},
                "baseline": None, "followups": [], "unfinished": []}
    _save_manifest(manifest, output_dir)
    print("M8 baseline: 330 shapes, 210 noncentral shapes, 21945 unordered pairs", flush=True)
    baseline_cpu, baseline_wall = time.process_time(), time.perf_counter()
    baseline = run_batch(max_length=8, max_index=8, radii=(1, 2, 4),
                         node_budget=1000, propagation_budget=50000,
                         cpu_seconds=600, output_dir=None)
    baseline["experiment_provenance"] = {"orchestrator_source_sha256": orchestrator_hash,
                                         "stage": "M8_BASELINE"}
    baseline["execution"] = _execution(command, baseline_cpu, baseline_wall)
    save_result(baseline, output_dir)
    write_gallery(baseline, output_dir/"gallery.html")
    manifest["baseline"] = _retained_summary(baseline, Path("boundary-screen.json"))
    manifest["execution"] = {"baseline": baseline["execution"]}
    _save_manifest(manifest, output_dir)
    print("M8 baseline complete: "+json.dumps(baseline["funnel"], sort_keys=True), flush=True)

    survivors = [pair for pair in baseline["pairs"]
                 if pair["status"] in ("SURVIVES_BOUNDED_SCREENS", "UNKNOWN")]
    manifest["followup_eligible_pairs"] = [pair["tiles"] for pair in survivors]
    manifest["unfinished"] = [{"tiles": pair["tiles"], "stage": "BASELINE",
                                "status": pair["status"]} for pair in baseline["pairs"]
                               if pair["status"] == "NOT_RUN_OUTER_BUDGET"]
    _save_manifest(manifest, output_dir)
    followup_cpu, followup_wall = time.process_time(), time.perf_counter()
    actual_followup_pairs = []
    if survivors:
        bank = StateBank([tile for tile in baseline["catalogue"] if not tile["centrally_symmetric"]])
        bank.cpu_deadline = followup_cpu+600
        effort = {"max_index": 16, "node_budget": 10000, "propagation_budget": 500000}
        singletons = []
        for tile in bank.tiles:
            item = ({"tile": tile, "status": "NOT_RUN_OUTER_BUDGET"}
                    if time.process_time() >= bank.cpu_deadline else
                    {"tile": tile, **search_periodic(bank, [tile], **effort)})
            singletons.append(item)
        singleton_cache_hash = digest(singletons)
        singleton_cache = {"schema": "arisearch.discovery.shared-singletons.v1",
                           "catalogue_sha256": baseline["catalogue_sha256"],
                           "budgets": effort, "singletons": singletons,
                           "singletons_sha256": singleton_cache_hash,
                           "orchestrator_source_sha256": orchestrator_hash}
        (output_dir/"followup-singletons.json").write_text(canonical_json(singleton_cache)+"\n")
        mono = {item["tile"]: item["witness_sha256"] for item in singletons
                if item["status"] == "PERIODIC_WITNESS"}
        print(f"M8 shared follow-up singleton cache ready; {len(survivors)} selected pairs", flush=True)
        for index, original in enumerate(survivors, 1):
            tile_ids = original["tiles"]
            if time.process_time() >= bank.cpu_deadline:
                manifest["unfinished"].extend({"tiles": pair["tiles"], "stage": "FOLLOWUP",
                                                "status": "NOT_RUN_SHARED_OUTER_BUDGET"}
                                               for pair in survivors[index-1:])
                break
            pair_cpu, pair_wall = time.process_time(), time.perf_counter()
            if any(tile in mono for tile in tile_ids):
                record = {"tiles": tile_ids, "status": "OMITTED_MONOHEDRAL_MEMBER",
                          "positive_members": sorted(set(tile_ids) & mono.keys()),
                          "singleton_witness_refs": [{"tile": tile, "witness_sha256": mono[tile]}
                                                      for tile in sorted(set(tile_ids) & mono.keys())],
                          "growth_status": "DEFERRED_POSITIVE_SINGLETON_WITNESS"}
            else:
                record = screen_pair(bank, tile_ids, radii=(1, 2, 4, 8), **effort)
            actual_followup_pairs.append(record)
            focused = {key: value for key, value in baseline.items()
                       if key not in ("result_sha256", "execution", "funnel", "effort_summary",
                                      "experiment_provenance", "pairs", "singletons")}
            focused["budgets"] = {**baseline["budgets"], "max_index": 16,
                                   "radii": [1, 2, 4, 8], "node_budget": 10000,
                                   "propagation_budget": 500000, "cpu_seconds_outer_cap": 600}
            focused["selection"] = {"pair_filter": tile_ids, "expected_pair_count": 1}
            focused["pairs"], focused["singletons"] = [record], singletons
            focused["batch_complete"] = record.get("budget_reason") != "outer_cpu_budget"
            focused["experiment_provenance"] = {
                "orchestrator_source_sha256": orchestrator_hash, "stage": "M8_FOCUSED_FOLLOWUP",
                "baseline_result_sha256": baseline["result_sha256"],
                "shared_followup_cpu_seconds": 600,
                "shared_singletons_sha256": singleton_cache_hash,
                "singleton_work_accounting": "Computed once in shared cache; copied here for independent full-envelope verification."}
            focused["execution"] = _execution(command, pair_cpu, pair_wall)
            directory = output_dir/f"followup-{index:03d}"
            save_result(focused, directory)
            write_gallery(focused, directory/"gallery.html")
            summary = _retained_summary(focused, directory.relative_to(output_dir)/"boundary-screen.json")
            summary.update(tiles=tile_ids, status=record["status"])
            if record["status"] == "PERIODIC_WITNESS":
                summary["domain_hnf"] = record["periodic"]["witness"]["domain_hnf"]
            manifest["followups"].append(summary)
            if record["status"] in ("UNKNOWN", "SURVIVES_BOUNDED_SCREENS"):
                manifest["unfinished"].append({"tiles": tile_ids, "stage": "FOLLOWUP",
                                               "status": record["status"], "path": summary["path"]})
            _save_manifest(manifest, output_dir)
            print(f"M8 follow-up {index}/{len(survivors)}: {record['status']}", flush=True)
        manifest["actual_followup_effort"] = _effort_summary({"singletons": singletons,
                                                              "pairs": actual_followup_pairs})
    else:
        manifest["actual_followup_effort"] = _effort_summary({})
    if _source_snapshot(prior_path) != preserved:
        raise RuntimeError("Preserved sources changed during the experiment")
    manifest["status"] = "COMPLETE_WITH_UNFINISHED" if manifest["unfinished"] else "COMPLETE"
    manifest["execution"].update(followup={"cpu_seconds": time.process_time()-followup_cpu,
                                          "wall_seconds": time.perf_counter()-followup_wall},
                                  total={"cpu_seconds": time.process_time()-total_cpu,
                                         "wall_seconds": time.perf_counter()-total_wall})
    _save_manifest(manifest, output_dir)
    print("M8 calibration stopped; manifest "+str(output_dir/"manifest.json"), flush=True)
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        default=Path("research/discovery/runs/boundary-m8-2026-10-24"))
    parser.add_argument("--preserved-run", type=Path,
                        default=Path("research/discovery/runs/boundary-m6-2026-10-24/boundary-screen.json"))
    args = parser.parse_args(argv)
    command_args = list(argv) if argv is not None else sys.argv[1:]
    command = shlex.join(["mise", "exec", "--", "conda", "run", "--no-capture-output", "-n",
                          "arisearch", "python", "-m", "research.discovery.length8_experiment", *command_args])
    run_experiment(args.output_dir, prior_path=args.preserved_run, command=command)


if __name__ == "__main__":
    main()
