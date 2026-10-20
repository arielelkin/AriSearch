#!/usr/bin/env python3
"""Exact finite phase/reflection angle gate, units pi. No metric search."""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import z3

BASE = Path(__file__).with_name("six-boundary-substitution-2026-10-19.json")
OUT = Path(__file__).with_suffix(".json")

def validate(data):
    for parent,disk in data.items():
        expected = (13,16,8,5) if parent == "P" else (12,15,7,7)
        assert len(disk["corner_words"]) == expected[0]
        assert set(disk["corner_words"]) == set(disk["species"])
        assert set(disk["species"].values()) == {"P", "Q"}
        assert sum(x == "P" for x in disk["species"].values()) == (11 if parent == "P" else 9)
        assert len(disk["faces"]) == expected[1]
        assert len(disk["boundary"]) == expected[2]
        assert disk["parent_corner_roles"] == {f"u{j}":j for j in range(expected[3])}
        nodes=defaultdict(list)
        for v,word in disk["corner_words"].items():
            assert len(word) == (5 if disk["species"][v] == "P" else 7)
            assert len(set(word)) == len(word)
            for node in word: nodes[node].append(v)
        assert set(nodes) == {f"{kind}{j}" for kind,n in zip("ftu",expected[1:]) for j in range(n)}
        for j,face in enumerate(disk["faces"]): assert set(nodes[f"f{j}"]) == set(face) and len(nodes[f"f{j}"]) == 3
        boundary=disk["boundary"]
        for j,v in enumerate(boundary): assert set(nodes[f"t{j}"]) == {v,boundary[(j+1)%len(boundary)]} and len(nodes[f"t{j}"]) == 2
        for j in range(expected[3]): assert len(nodes[f"u{j}"]) == 1


def verify(data, result):
    angles = {s: list(map(Fraction, result["angles_pi"][s])) for s in "PQ"}
    for s, total in [("P", 3), ("Q", 5)]:
        assert len(angles[s]) == (5 if s == "P" else 7)
        assert all(0 < x < 1 for x in angles[s])
        assert sum(angles[s]) == total
    counts = defaultdict(int)
    for parent, disk in data.items():
        nodes = defaultdict(list)
        assert set(result["assignment"][parent]) == set(disk["corner_words"])
        for v, word in disk["corner_words"].items():
            species = disk["species"][v]
            phase, reflection = result["assignment"][parent][v]
            n = len(angles[species])
            assert len(word) == n and 0 <= phase < n and reflection in [-1, 1]
            for k, node in enumerate(word):
                nodes[node].append(angles[species][(phase + reflection*k) % n])
        for node, values in nodes.items():
            if node.startswith("f"):
                assert len(values) == 3 and sum(values) == 2
                counts["interior_triples"] += 1
            elif node.startswith("t"):
                assert len(values) == 2 and sum(values) == 1
                counts["boundary_pairs"] += 1
            else:
                assert len(values) == 1
                assert values[0] == angles[parent][disk["parent_corner_roles"][node]]
                counts["parent_equalities"] += 1
    return dict(counts)

def solve(data, timeout, core=False):
    validate(data)
    solver = z3.Solver()
    solver.set(timeout=timeout, random_seed=0)
    if core:
        solver.set(unsat_core=True)
    def add(label, *constraints):
        if core:
            solver.assert_and_track(z3.And(*constraints), label)
        else:
            solver.add(*constraints)
    angles = {s: [z3.Real(f"{s}{j}") for j in range(n)] for s, n in [("P", 5), ("Q", 7)]}
    for s, total in [("P", 3), ("Q", 5)]:
        add(f"sum_{s}", z3.Sum(angles[s]) == total)
        for j,a in enumerate(angles[s]):
            add(f"bound_{s}_{j}", a > 0, a < 1)
    selectors = {}
    for parent, disk in data.items():
        nodes = defaultdict(list)
        for v, word in disk["corner_words"].items():
            a = angles[disk["species"][v]]
            n = len(a)
            choice = z3.Int(f"choice_{parent}_{v}")
            selectors[parent, v] = choice
            values = [z3.Real(f"angle_{parent}_{v}_{k}") for k in range(n)]
            # A finite disjunction of constant permutations keeps every branch linear.
            add(f"word_{parent}_{v}", z3.Or(*[z3.And(choice == 2*phase+r,
                *[values[k] == a[(phase+eps*k)%n] for k in range(n)])
                for phase in range(n) for r, eps in enumerate([1,-1])]))
            for node, value in zip(word, values):
                nodes[node].append(value)
        for node, values in nodes.items():
            target = 2 if node.startswith("f") else 1 if node.startswith("t") else angles[parent][disk["parent_corner_roles"][node]]
            add(f"node_{parent}_{node}", z3.Sum(values) == target)
    formula_hash = hashlib.sha256(solver.sexpr().encode()).hexdigest()
    start = time.monotonic()
    status = solver.check()
    result = {"status": str(status), "parents": sorted(data), "formula_sha256": formula_hash, "elapsed_seconds": time.monotonic()-start,
        "z3_version": z3.get_version_string(), "timeout_ms": timeout, "random_seed": 0,
        "input_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
        "scope": "Exact retained " + "+".join(sorted(data)) + " incidence; all 10 or 14 dihedral assignments independently for each child; strict native angles in units pi; no metric constraints.",
        "symmetry_reductions": "none; parent indices remain fixed"}
    if core and status == z3.unsat:
        result["unsat_core"] = [str(x) for x in solver.unsat_core()]
    if status == z3.sat:
        model = solver.model()
        result["angles_pi"] = {s: [str(model.eval(a)) for a in aa] for s, aa in angles.items()}
        result["assignment"] = {p: {} for p in data}
        for (p,v), c in selectors.items():
            value = model.eval(c).as_long()
            result["assignment"][p][v] = [value//2, [1,-1][value%2]]
        result["independent_fraction_checks"] = verify(data, result)
    elif status == z3.unknown:
        result["reason_unknown"] = solver.reason_unknown()
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout-ms", type=int, default=600000)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--parent", choices=["P","Q"])
    parser.add_argument("--core", action="store_true")
    args = parser.parse_args()
    data = json.loads(BASE.read_text())
    if args.parent:
        data = {args.parent:data[args.parent]}
    validate(data)
    if args.verify:
        print(verify(data, json.loads(OUT.read_text())))
    else:
        result = solve(data, args.timeout_ms, args.core)
        OUT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
        print(json.dumps(result, indent=2, sort_keys=True))
