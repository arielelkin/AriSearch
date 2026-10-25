"""Run the complete discovery checkpoint checks without rewriting evidence.

Default checks retained finite data, source tests and the locked environment.
--replay additionally regenerates all declared finite computations. These
checks do not establish aperiodicity or mathematical completeness outside
the recorded domains. Historical generators are never called on retained
output directories by this driver.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
DISCOVERY = ROOT / "research/discovery"


def evidence_hashes():
    paths = [p for p in DISCOVERY.rglob("*") if p.is_file()
             and not {"__pycache__", ".pytest_cache"}.intersection(p.parts)
             and p.suffix != ".lock"]
    paths += [ROOT / name for name in (
        "discovery-log.md", "AGENTS.md", "mise.toml", "research-problem.md",
        "research-protocol.md", "environment/environment.yml",
        "environment/conda-lock.yml", "scripts/verify_environment.py",
    )]
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def checks(replay=False):
    py = sys.executable
    result = [
        ("locked environment", [py, "scripts/verify_environment.py"]),
        ("discovery tests", [py, "-m", "pytest", "research/discovery", "-q"]),
        ("kite pilot", [py, "-m", "research.discovery.replay"] if replay else
         [py, "-m", "research.discovery.verify",
          "research/discovery/runs/kite-n8-2026-10-24/screen.json"]),
        ("length-six baseline and four challenges",
         [py, "-m", "research.discovery.boundary_replay"] + ([] if replay else ["--verify-only"])),
    ]
    for label, module in (
        ("length-eight calibration", "calibration_verify"),
        ("mixed-angle support preflight", "mixed_verify"),
        ("angular-first ordering comparison", "angular_first_verify"),
    ):
        result.append((label, [py, "-m", "research.discovery." + module]
                       + (["--replay"] if replay else [])))
    return result


def run(replay=False):
    if sys.flags.optimize:
        raise ValueError("Assertions must remain enabled for discovery checks.")
    before = evidence_hashes()
    started = time.perf_counter()
    results = []
    for label, command in checks(replay):
        print("Checking " + label, file=sys.stderr, flush=True)
        phase = time.perf_counter()
        completed = subprocess.run(command, cwd=ROOT, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        results.append({"check": label, "returncode": completed.returncode,
                        "elapsed_seconds": round(time.perf_counter()-phase, 3),
                        "output": completed.stdout.strip()})
        if completed.returncode:
            break
    unchanged = evidence_hashes() == before
    passed = unchanged and len(results) == len(checks(replay)) and all(r["returncode"] == 0 for r in results)
    return {"status": "PASSED" if passed else "FAILED",
            "fresh_replays": replay, "source_and_evidence_unchanged": unchanged,
            "elapsed_seconds": round(time.perf_counter()-started, 3),
            "checked_file_count": len(before), "checks": results,
            "scope": "Discovery checkpoint only; historical research registry is separate; no global tiling claim."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--report", type=Path, help="Optional JSON report outside the repository")
    args = parser.parse_args()
    if args.report is not None and args.report.resolve().is_relative_to(ROOT):
        parser.error("report destination must be outside the repository so validation stays read-only")
    result = run(args.replay)
    output = json.dumps(result, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output)
    print(output, end="")
    raise SystemExit(0 if result["status"] == "PASSED" else 1)


if __name__ == "__main__":
    main()
