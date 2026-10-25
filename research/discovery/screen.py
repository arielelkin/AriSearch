"""Small, reproducible same-grid screens, never global negative certificates.

Run as ``python -m research.discovery.screen --help``. HNF index counts
triangular-lattice fundamental cells, each containing six elementary kites.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import shlex
import sys
from typing import Iterable

import ortools
from ortools.sat.python import cp_model

from .kite_grid import (boundary_polygon, canonical_polygon, cell_polygon, enumerate_convex,
                        grid_orientations, translate_cell)

Cell = tuple[int, int, int, int]


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value) -> str:
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def wrap_cell(cell: Cell, hnf: tuple[int, int, int]) -> Cell:
    """Reduce modulo (a,0),(b,c), including negative and skew translates."""
    a, b, c = hnf
    if a <= 0 or c <= 0 or not 0 <= b < a:
        raise ValueError("HNF requires a,c>0 and 0<=b<a")
    i, j, orientation, corner = cell
    quotient, remainder = divmod(j, c)
    return ((i - quotient * b) % a, remainder, orientation, corner)


def hnf_domains(max_index: int):
    for index in range(1, max_index + 1):
        for a in range(1, index + 1):
            if index % a == 0:
                for b in range(a):
                    yield (a, b, index // a)


def _record(candidate, index: int) -> dict:
    data = candidate.to_dict() if hasattr(candidate, "to_dict") else dict(candidate)
    data["id"] = str(data.get("id", f"K{index:04d}"))
    data["cells"] = sorted([list(c) for c in data["cells"]])
    return data


def _orientations(tile: dict):
    embeddings = tile.get("embeddings") or [tile["cells"]]
    unique = set()
    for embedding in embeddings:
        for mask in grid_orientations(tuple(tuple(c) for c in embedding)):
            unique.add(tuple(sorted(mask)))
    return sorted(unique)


def _prototile(tile: dict) -> dict:
    return {"id": tile["id"], "polygon": tile["polygon"], "cells": tile["cells"]}


def periodic_placements(tiles: list[dict], hnf: tuple[int, int, int]):
    """All phases and grid orientations, dropping self-overlapping torus tiles."""
    a, _, c = hnf
    placements = []
    seen = set()
    for tile in tiles:
        for mask in _orientations(tile):
            for i in range(a):
                for j in range(c):
                    cells = tuple(sorted(translate_cell(cell, i, j) for cell in mask))
                    wrapped = tuple(sorted(wrap_cell(cell, hnf) for cell in cells))
                    if len(set(wrapped)) != len(cells):
                        continue
                    key = (tile["id"], wrapped)
                    if key not in seen:
                        seen.add(key)
                        placements.append({"tile": tile["id"], "cells": cells,
                                           "wrapped_cells": wrapped})
    return placements


def solve_exact_cover(placements: list[dict], targets: Iterable[Cell], *,
                      required_tiles: Iterable[str] = (), seconds: float = 0.1,
                      deterministic_time: float = 0.01, seed: int = 0,
                      fixed_indices: Iterable[int] = ()) -> dict:
    """Cover targets once and enforce disjointness on every exterior cell too."""
    targets = set(targets)
    model = cp_model.CpModel()
    variables = [model.new_bool_var(f"p{i}") for i in range(len(placements))]
    incidence: dict[Cell, list] = {}
    by_tile: dict[str, list] = {}
    for p, variable in zip(placements, variables):
        occupied = p.get("wrapped_cells", p["cells"])
        if len(set(occupied)) != len(occupied):
            model.add(variable == 0)
        for cell in set(occupied):
            incidence.setdefault(cell, []).append(variable)
        by_tile.setdefault(p["tile"], []).append(variable)
    for target in sorted(targets):
        model.add_exactly_one(incidence.get(target, []))
    for cell in sorted(incidence.keys() - targets):
        model.add_at_most_one(incidence[cell])
    for tile in required_tiles:
        model.add_bool_or(by_tile.get(tile, []))
    for index in fixed_indices:
        model.add(variables[index] == 1)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.max_deterministic_time = deterministic_time
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = seed
    status = solver.solve(model)
    label = solver.status_name(status)
    result = {"status": label, "selected": []}
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result["selected"] = [i for i, variable in enumerate(variables)
                              if solver.boolean_value(variable)]
    return result


def search_periodic(tiles: list[dict], *, max_index: int = 4,
                    solve_seconds: float = 0.1, deterministic_time: float = 0.01,
                    seed: int = 0) -> dict:
    attempts = []
    for hnf in hnf_domains(max_index):
        a, b, c = hnf
        targets = [(i, j, orientation, corner) for i in range(a) for j in range(c)
                   for orientation in range(2) for corner in range(3)]
        placements = periodic_placements(tiles, hnf)
        solved = solve_exact_cover(placements, targets,
                                   required_tiles=[tile["id"] for tile in tiles],
                                   seconds=solve_seconds, deterministic_time=deterministic_time,
                                   seed=seed)
        attempts.append({"hnf": list(hnf), "placement_count": len(placements),
                         "status": solved["status"]})
        if solved["status"] in ("OPTIMAL", "FEASIBLE"):
            chosen = []
            for index in solved["selected"]:
                placement = dict(placements[index])
                placement["polygon"] = boundary_polygon(placement["cells"])
                chosen.append(placement)
            witness = {"kind": "periodic", "domain_hnf": list(hnf),
                       "period_vectors": [[12*a, 0], [12*b+6*c, 6*c]],
                       "prototiles": [_prototile(tile) for tile in tiles],
                       "placements": chosen}
            return {"status": "PERIODIC_WITNESS", "attempts": attempts,
                    "witness": witness, "witness_sha256": digest(witness)}
    unknown = any(attempt["status"] == "UNKNOWN" for attempt in attempts)
    invalid = any(attempt["status"] == "MODEL_INVALID" for attempt in attempts)
    return {"status": "MODEL_INVALID" if invalid else
            "UNKNOWN" if unknown else "NO_PERIODIC_WITNESS_IN_TESTED_DOMAINS",
            "attempts": attempts}


def monohedral_theorem(tile: dict) -> str | None:
    """Reliable positive geometric omissions; this is not a mesh witness."""
    polygon = tile["polygon"]
    if len(polygon) in (3, 4):
        return "Every convex triangle or quadrilateral tiles the plane (half-turn construction)."
    if len(polygon) == 6:
        opposite_sums = {(polygon[i][0]+polygon[i+3][0],
                          polygon[i][1]+polygon[i+3][1]) for i in range(3)}
        if len(opposite_sums) == 1:
            return "Every centrally symmetric convex hexagon tiles by translations."
    return None


def run_screen(candidates: list, *, max_index=4, solve_seconds=0.1,
               deterministic_time=0.01, seed=0, use_theorems=True,
               provenance=None) -> dict:
    tiles = [_record(candidate, i) for i, candidate in enumerate(candidates)]
    if len({tile["id"] for tile in tiles}) != len(tiles):
        raise ValueError("Candidate IDs must be unique")
    if len({canonical_polygon(tuple(tuple(p) for p in tile["polygon"]))
            for tile in tiles}) != len(tiles):
        raise ValueError("Catalogue must contain distinct congruence classes")
    budgets = {"max_index": max_index, "solve_seconds": solve_seconds,
               "deterministic_time": deterministic_time, "seed": seed,
               "workers": 1}
    singleton_results = []
    survivors = []
    for tile in tiles:
        theorem = monohedral_theorem(tile) if use_theorems else None
        result = ({"status": "MONOHEDRAL_THEOREM", "reason": theorem}
                  if theorem else search_periodic([tile], **budgets_without_workers(budgets)))
        singleton_results.append({"tile": tile["id"], **result})
        if result["status"] not in ("MONOHEDRAL_THEOREM", "PERIODIC_WITNESS"):
            survivors.append(tile)
    pairs = []
    for left, right in itertools.combinations(survivors, 2):
        pairs.append({"tiles": [left["id"], right["id"]],
                      **search_periodic([left, right], **budgets_without_workers(budgets))})
    result = {"schema": "arisearch.discovery.screen.v1", "catalogue": tiles,
              "catalogue_sha256": digest(tiles), "budgets": budgets,
              "versions": {"python": platform.python_version(), "ortools": ortools.__version__},
              "scope": "Same-grid D6 placements of all supplied mesh embeddings; bounded HNF domains. Negative search results are not global exclusions.",
              "singletons": singleton_results, "pairs": pairs,
              "funnel": {"catalogue": len(tiles),
                         "monohedral_theorem": sum(r["status"] == "MONOHEDRAL_THEOREM" for r in singleton_results),
                         "monohedral_periodic": sum(r["status"] == "PERIODIC_WITNESS" for r in singleton_results),
                         "unresolved_singletons": len(survivors),
                         "remaining_unordered_pairs": len(pairs),
                         "periodic_pairs": sum(p["status"] == "PERIODIC_WITNESS" for p in pairs),
                         "unresolved_pairs": sum(p["status"] != "PERIODIC_WITNESS" for p in pairs)}}
    if provenance is not None:
        result["provenance"] = provenance
    result["result_sha256"] = digest(result)
    return result


def budgets_without_workers(budgets):
    return {key: value for key, value in budgets.items() if key != "workers"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-cells", type=int, default=6)
    parser.add_argument("--max-index", type=int, default=4)
    parser.add_argument("--solve-seconds", type=float, default=0.1)
    parser.add_argument("--deterministic-time", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output-dir", type=Path, default=Path("research/discovery/output"))
    parser.add_argument("--catalogue", type=Path)
    parser.add_argument("--no-theorems", action="store_true")
    args = parser.parse_args(argv)
    if min(args.max_cells, args.max_index, args.solve_seconds, args.deterministic_time) <= 0:
        parser.error("catalogue, domain and effort bounds must be positive")
    if args.catalogue:
        loaded = json.loads(args.catalogue.read_text())
        candidates = loaded["catalogue"] if isinstance(loaded, dict) else loaded
    else:
        candidates = enumerate_convex(args.max_cells)
    source_dir = Path(__file__).parent
    provenance = {"max_cells": args.max_cells if args.catalogue is None else None,
                  "generator": "kite_grid.enumerate_convex" if args.catalogue is None else None,
                  "generator_algorithm": "edge-connected convex-closure expansion with forced filling of positive-area hull intersections; exact convex hull area equality; congruence by cyclic squared-distance words; all mesh embeddings retained" if args.catalogue is None else None,
                  "catalogue_input": str(args.catalogue) if args.catalogue else None,
                  "catalogue_input_sha256": hashlib.sha256(args.catalogue.read_bytes()).hexdigest() if args.catalogue else None,
                  "source_sha256": {name: hashlib.sha256((source_dir/name).read_bytes()).hexdigest()
                                    for name in ("kite_grid.py", "screen.py", "render.py")},
                  "use_theorems": not args.no_theorems}
    result = run_screen(candidates, max_index=args.max_index,
                        solve_seconds=args.solve_seconds,
                        deterministic_time=args.deterministic_time, seed=args.seed,
                        use_theorems=not args.no_theorems, provenance=provenance)
    # Output destination is execution metadata; it does not change the search hash.
    command_args = list(argv) if argv is not None else sys.argv[1:]
    result["execution"] = {"command": shlex.join(["mise", "exec", "--", "conda", "run",
                          "--no-capture-output", "-n", "arisearch", "python", "-m",
                          "research.discovery.screen", *command_args]),
                          "result_hash_scope": "all top-level fields except result_sha256 and execution"}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "screen.json").write_text(canonical_json(result)+"\n")
    from .render import write_gallery
    write_gallery(result, args.output_dir / "gallery.html")
    print(json.dumps(result["funnel"], sort_keys=True))


if __name__ == "__main__":
    main()
