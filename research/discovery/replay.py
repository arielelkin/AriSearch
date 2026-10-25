"""Replay the retained bounded pilot without rewriting its evidence.

Regenerates the complete finite catalogue, repeats bounded solver searches,
and independently verifies the retained and regenerated positive witnesses.
This does not verify global non-tilability, aperiodicity, or solver UNSAT.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

from .kite_grid import enumerate_convex
from .screen import run_screen
from .verify import verify_screen

DEFAULT = Path(__file__).parent / "runs/kite-n8-2026-10-24/screen.json"


def replay(path: Path) -> dict:
    original = path.read_bytes()
    retained = json.loads(original)
    checked = verify_screen(retained)
    provenance = retained["provenance"]
    if provenance["generator"] != "kite_grid.enumerate_convex":
        raise ValueError("This replay requires a complete built-in kite catalogue.")
    if provenance.get("catalogue_input") is not None:
        raise ValueError("External candidate catalogues need their own completeness specification.")
    for name, expected in provenance["source_sha256"].items():
        if name not in ("kite_grid.py", "screen.py", "render.py"):
            raise ValueError(f"Unrecognized retained source name: {name}")
        actual = hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"Source differs from retained run: {name}")
    budgets = retained["budgets"]
    started = time.perf_counter()
    regenerated = run_screen(
        enumerate_convex(provenance["max_cells"]),
        max_index=budgets["max_index"],
        solve_seconds=budgets["solve_seconds"],
        deterministic_time=budgets["deterministic_time"],
        seed=budgets["seed"],
        use_theorems=provenance["use_theorems"],
        provenance=provenance,
    )
    verify_screen(regenerated)
    if regenerated["result_sha256"] != retained["result_sha256"]:
        raise ValueError("Regenerated search differs from the retained search; evidence was not overwritten.")
    if path.read_bytes() != original:
        raise ValueError("Retained evidence changed during replay.")
    return {"status": "PASSED", "result_sha256": retained["result_sha256"],
            "catalogue": len(retained["catalogue"]),
            "periodic_witnesses": sum("witness" in r for r in retained["singletons"] + retained["pairs"]),
            "independent_verification": checked,
            "fresh_search_seconds": round(time.perf_counter() - started, 4),
            "scope": "Retained finite catalogue and bounded search only; original evidence unchanged."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    print(json.dumps(replay(args.certificate), sort_keys=True))


if __name__ == "__main__":
    main()
