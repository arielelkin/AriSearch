"""Bounded native-edge experiment on equiangular 120-degree hexagons.

The symbolic honeycomb disk is not a physical circle or a tile corona claim.
Every negative claim names its finite domain and deterministic effort bound.
"""
from __future__ import annotations

import argparse
from collections import deque
import hashlib
import itertools
import json
from pathlib import Path
import platform
import shlex
import sys
import time

from .boundary_words import (enumerate_words, library_metadata,
                             prior_fixture_overlap, states, vertices)

STEPS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
CONVENTIONS = {"coordinate_metric": "(x,y) means (x,sqrt(3)*y)",
               "face_steps": STEPS,
               "edge_vectors_per_native_length": ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)),
               "edge_matching": "slot k equals neighbor slot (k+3)%6",
               "vertex_order": "CCW; vertex 0 is origin; edge k joins vertex k to (k+1)%6",
               "disk": "max(abs(i),abs(j),abs(i+j)) <= radius; symbolic face radius only"}


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value):
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def disk(radius):
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return tuple((i, j) for i in range(-radius, radius+1)
                 for j in range(-radius, radius+1)
                 if max(abs(i), abs(j), abs(i+j)) <= radius)


def hnf_domains(max_index):
    for index in range(1, max_index+1):
        for a in range(1, index+1):
            if index % a == 0:
                for b in range(a):
                    yield (a, b, index//a)


def wrap_face(face, hnf):
    a, b, c = hnf
    if a <= 0 or c <= 0 or not 0 <= b < a:
        raise ValueError("invalid HNF")
    n, j = divmod(face[1], c)
    m, i = divmod(face[0]-n*b, a)
    return (i, j), (m, n)


class StateBank:
    """Shared bitset domains and per-edge length masks for all pair solves."""
    def __init__(self, tiles):
        self.cpu_deadline = None
        self.tiles = {tile["id"]: tile for tile in tiles}
        self.states = states(tiles)
        self.by_tile = {}
        self.length_masks = [{} for _ in range(6)]
        self.self_masks = []
        for index, state in enumerate(self.states):
            bit = 1 << index
            self.by_tile[state["tile_id"]] = self.by_tile.get(state["tile_id"], 0) | bit
            for k, length in enumerate(state["word"]):
                self.length_masks[k][length] = self.length_masks[k].get(length, 0) | bit
        for k in range(6):
            self.self_masks.append(sum(1 << i for i, state in enumerate(self.states)
                                       if state["word"][k] == state["word"][(k+3)%6]))
        self._support_cache = [{} for _ in range(6)]

    def mask(self, tile_ids):
        mask = 0
        for tile in tile_ids:
            mask |= self.by_tile[tile]
        return mask

    def support(self, neighbor_domain, heading):
        cache = self._support_cache[heading]
        if neighbor_domain in cache:
            return cache[neighbor_domain]
        opposite = (heading+3) % 6
        supported = 0
        for length, opposite_mask in self.length_masks[opposite].items():
            if neighbor_domain & opposite_mask:
                supported |= self.length_masks[heading].get(length, 0)
        # A bounded cache avoids retaining every branch of the entire batch.
        if len(cache) < 100000:
            cache[neighbor_domain] = supported
        return supported


def graph_for_faces(faces, hnf=None):
    faces = tuple(sorted(faces))
    index = {face: i for i, face in enumerate(faces)}
    arcs = []
    incoming = [[] for _ in faces]
    for u, (i, j) in enumerate(faces):
        for k, (di, dj) in enumerate(STEPS):
            other = (i+di, j+dj)
            if hnf is not None:
                other = wrap_face(other, hnf)[0]
            if other in index:
                arc = (u, index[other], k)
                incoming[index[other]].append(len(arcs))
                arcs.append(arc)
    return faces, arcs, incoming


class _BudgetStop(Exception):
    pass


def solve_csp(bank, graph, tile_ids, *, seed_tile=None, node_budget=1000,
              propagation_budget=50000, required_tiles=()):
    """Exact finite CSP with AC propagation and deterministic bounded DFS."""
    faces, arcs, incoming = graph
    initial = bank.mask(tile_ids)
    domains = [initial]*len(faces)
    if seed_tile is not None:
        # Disk symmetry permits fixing one directed seed state up to D6.
        seed_mask = bank.by_tile[seed_tile]
        domains[faces.index((0, 0))] = seed_mask & -seed_mask
    counters = {"nodes": 0, "propagations": 0,
                "initial_domains": len(faces), "initial_arcs": len(arcs)}
    budget_reason = None

    def check_cpu():
        if bank.cpu_deadline is not None and time.process_time() >= bank.cpu_deadline:
            raise _BudgetStop("outer_cpu_budget")

    def propagate(current, queued):
        queue = deque(queued)
        while queue:
            if counters["propagations"] % 256 == 0:
                check_cpu()
            if counters["propagations"] >= propagation_budget:
                raise _BudgetStop("propagation_budget")
            counters["propagations"] += 1
            arc_index = queue.popleft()
            u, v, k = arcs[arc_index]
            supported = (bank.self_masks[k] if u == v else bank.support(current[v], k))
            revised = current[u] & supported
            if revised != current[u]:
                if not revised:
                    return False
                current[u] = revised
                queue.extend(incoming[u])
        return True

    def visit(current, queued):
        check_cpu()
        if counters["nodes"] >= node_budget:
            raise _BudgetStop("node_budget")
        counters["nodes"] += 1
        if not propagate(current, queued):
            return None
        undecided = [(domain.bit_count(), i) for i, domain in enumerate(current)
                     if domain & (domain-1)]
        if not undecided:
            present = {bank.states[domain.bit_length()-1]["tile_id"] for domain in current}
            if not set(required_tiles) <= present:
                return None
            return current
        _, branch = min(undecided)
        available = current[branch]
        while available:
            chosen = available & -available
            available -= chosen
            child = current.copy()
            child[branch] = chosen
            answer = visit(child, incoming[branch])
            if answer is not None:
                return answer
        return None

    try:
        solved = visit(domains, range(len(arcs)))
    except _BudgetStop as error:
        solved = None
        budget_reason = str(error)
    status = "UNKNOWN" if budget_reason else "SAT" if solved is not None else "UNSAT"
    result = {"status": status, **counters}
    if budget_reason:
        result["budget_reason"] = budget_reason
    if solved is not None:
        result["assignment"] = [domain.bit_length()-1 for domain in solved]
    return result


def _add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def _sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def _edge_displacement(left, right, k):
    return _sub(left["polygon"][k], right["polygon"][(k+4)%6])


def develop_certificate(bank, faces, assignment, tile_ids, *, radius=None, hnf=None,
                        seed_tile=None):
    """Develop matched edges into exact physical polygons; reject holonomy."""
    assigned = {tuple(face): bank.states[state] for face, state in zip(faces, assignment)}

    def get_state(face):
        return assigned[wrap_face(face, hnf)[0] if hnf else face]

    origins = {(0, 0): (0, 0)}
    periods = None
    if hnf:
        def path_origin(face):
            i, j = 0, 0
            origin = (0, 0)
            for axis, count in ((0, face[0]), (1, face[1])):
                direction = axis if count >= 0 else axis+3
                for _ in range(abs(count)):
                    di, dj = STEPS[direction]
                    other = (i+di, j+dj)
                    origin = _add(origin, _edge_displacement(get_state((i, j)), get_state(other), direction))
                    i, j = other
            return origin
        a, b, c = hnf
        periods = (path_origin((a, 0)), path_origin((b, c)))
        origins = {face: path_origin(face) for face in faces}
    else:
        queue = deque([(0, 0)])
        while queue:
            face = queue.popleft()
            for k, step in enumerate(STEPS):
                other = _add(face, step)
                if other not in assigned:
                    continue
                origin = _add(origins[face], _edge_displacement(assigned[face], assigned[other], k))
                if other in origins:
                    if origins[other] != origin:
                        raise ValueError("nonzero patch holonomy")
                else:
                    origins[other] = origin
                    queue.append(other)
    for face in faces:
        for k, step in enumerate(STEPS):
            other = _add(face, step)
            if hnf:
                rep, (m, n) = wrap_face(other, hnf)
                expected = (origins[rep][0]+m*periods[0][0]+n*periods[1][0],
                            origins[rep][1]+m*periods[0][1]+n*periods[1][1])
            elif other in assigned:
                expected = origins[other]
            else:
                continue
            actual = _add(origins[face], _edge_displacement(get_state(face), get_state(other), k))
            if actual != expected:
                raise ValueError("nonzero edge-development holonomy")
    placements = [{"tile": assigned[face]["tile_id"], "state_id": assigned[face]["state_id"],
                   "word": assigned[face]["word"], "face": face, "origin": origins[face],
                   "polygon": [_add(origins[face], point) for point in assigned[face]["polygon"]]}
                  for face in faces]
    witness = {"kind": "boundary_periodic" if hnf else "boundary_patch",
               "conventions": CONVENTIONS,
               "prototiles": [{"id": tile, "word": bank.tiles[tile]["word"],
                                "polygon": bank.tiles[tile]["polygon"]} for tile in tile_ids],
               "placements": placements,
               "species_present": sorted({placement["tile"] for placement in placements})}
    if hnf:
        witness.update(domain_hnf=hnf, period_vectors=periods)
    else:
        witness.update(symbolic_radius=radius, seed_face=(0, 0), seed_tile=seed_tile)
    return witness


def solve_disk(bank, tile_ids, radius, seed_tile, *, node_budget=1000,
               propagation_budget=50000):
    graph = graph_for_faces(disk(radius))
    result = solve_csp(bank, graph, tile_ids, seed_tile=seed_tile,
                       node_budget=node_budget, propagation_budget=propagation_budget)
    result.update(symbolic_radius=radius, seed_tile=seed_tile)
    if result["status"] == "SAT":
        assignment = result.pop("assignment")
        witness = develop_certificate(bank, graph[0], assignment, tile_ids,
                                       radius=radius, seed_tile=seed_tile)
        result.update(witness=witness, witness_sha256=digest(witness))
    return result


def search_periodic(bank, tile_ids, *, max_index=4, node_budget=1000,
                    propagation_budget=50000, required_tiles=()):
    attempts = []
    for hnf in hnf_domains(max_index):
        a, _, c = hnf
        faces = tuple((i, j) for i in range(a) for j in range(c))
        graph = graph_for_faces(faces, hnf)
        result = solve_csp(bank, graph, tile_ids, node_budget=node_budget,
                           propagation_budget=propagation_budget, required_tiles=required_tiles)
        attempt = {key: value for key, value in result.items() if key != "assignment"}
        attempt["domain_hnf"] = hnf
        attempts.append(attempt)
        if result["status"] == "SAT":
            witness = develop_certificate(bank, graph[0], result["assignment"], tile_ids, hnf=hnf)
            return {"status": "PERIODIC_WITNESS", "attempts": attempts,
                    "witness": witness, "witness_sha256": digest(witness)}
        if result.get("budget_reason") == "outer_cpu_budget":
            return {"status": "UNKNOWN", "budget_reason": "outer_cpu_budget",
                    "attempts": attempts}
    return {"status": "UNKNOWN" if any(a["status"] == "UNKNOWN" for a in attempts)
            else "NO_PERIODIC_WITNESS_IN_TESTED_DOMAINS", "attempts": attempts}


def screen_pair(bank, tile_ids, *, max_index=4, radii=(1, 2, 4), node_budget=1000,
                propagation_budget=50000):
    effort = {"node_budget": node_budget, "propagation_budget": propagation_budget}
    record = {"tiles": list(tile_ids), "local": [], "growth": []}
    local_radius = min(radii) if radii else 1
    for seed in tile_ids:
        result = solve_disk(bank, tile_ids, local_radius, seed, **effort)
        # Keep only the strongest patch per seed in the growth records below.
        record["local"].append({key: value for key, value in result.items()
                                if key not in ("witness", "witness_sha256")})
        if result.get("budget_reason") == "outer_cpu_budget":
            record.update(status="UNKNOWN", budget_reason="outer_cpu_budget",
                          periodic={"status": "DEFERRED_OUTER_BUDGET"},
                          growth_status="DEFERRED_OUTER_BUDGET")
            return record
        if result["status"] == "UNSAT":
            record.update(status="LOCAL_OBSTRUCTION",
                          periodic={"status": "DEFERRED_LOCAL_OBSTRUCTION"},
                          growth_status="DEFERRED_LOCAL_OBSTRUCTION",
                          conclusion="No native honeycomb tiling containing both species can contain this seeded disk.")
            return record
        if "witness" in result:
            record["growth"].append({key: value for key, value in result.items()
                                     if key not in ("nodes", "propagations", "initial_domains", "initial_arcs")})
    periodic = search_periodic(bank, tile_ids, max_index=max_index, **effort)
    record["periodic"] = periodic
    if periodic.get("budget_reason") == "outer_cpu_budget":
        record.update(status="UNKNOWN", budget_reason="outer_cpu_budget",
                      growth_status="DEFERRED_OUTER_BUDGET")
        return record
    if periodic["status"] == "PERIODIC_WITNESS":
        record["status"] = "PERIODIC_WITNESS"
        record["growth"] = []
        record["growth_status"] = "DEFERRED_POSITIVE_PERIODIC_WITNESS"
        return record
    for radius in sorted(set(radii)-{local_radius}):
        for seed in tile_ids:
            result = solve_disk(bank, tile_ids, radius, seed, **effort)
            # Store all bounded outcomes but at most the largest SAT patch/seed.
            if result["status"] == "SAT":
                for previous in record["growth"]:
                    if previous["seed_tile"] == seed:
                        previous.pop("witness", None)
                        previous.pop("witness_sha256", None)
            record["growth"].append(result)
            if result.get("budget_reason") == "outer_cpu_budget":
                record.update(status="UNKNOWN", budget_reason="outer_cpu_budget",
                              growth_status="DEFERRED_OUTER_BUDGET")
                return record
            if result["status"] == "UNSAT":
                record.update(status="FINITE_EXTENSION_FAILURE",
                              growth_status="STOPPED_EXHAUSTED_FINITE_DOMAIN",
                              conclusion="No native honeycomb tiling containing both species can contain this seeded disk.")
                return record
    outcomes = record["local"] + record["growth"]
    record["status"] = ("UNKNOWN" if periodic["status"] == "UNKNOWN" or
                        any(item["status"] == "UNKNOWN" for item in outcomes)
                        else "SURVIVES_BOUNDED_SCREENS")
    record["growth_status"] = "BOUNDED_GROWTH_COMPLETE"
    return record


def source_provenance(max_length):
    directory = Path(__file__).parent
    return {"max_length": max_length, "family": "equiangular 120-degree convex hexagons",
            "scale": "one common scale: native integer length l has physical length 2*l",
            "generator": "boundary_words.enumerate_words",
            "generator_algorithm": "four free lengths, exact closure, bounded six native lengths, D6 canonical words, no per-tile rescaling",
            "source_sha256": {name: hashlib.sha256((directory/name).read_bytes()).hexdigest()
                              for name in ("boundary_words.py", "boundary_screen.py", "boundary_render.py")}}


def _funnel(result):
    from collections import Counter
    counts = dict(sorted(Counter(pair["status"] for pair in result["pairs"]).items()))
    return {"library": len(result["catalogue"]), "central_theorem_omissions": len(result["central_omissions"]),
            "noncentral_singletons": len(result["singletons"]),
            "positive_singleton_periodic": sum(s["status"] == "PERIODIC_WITNESS" for s in result["singletons"]),
            "unordered_pairs": len(result["pairs"]), "pair_status_counts": counts}


def _effort_summary(value):
    """Aggregate actual deterministic solver work, including initial arcs."""
    summary = {"solves": 0, "nodes": 0, "propagations": 0,
               "initial_domains": 0, "initial_arcs": 0,
               "max_nodes": 0, "max_propagations": 0}
    def visit(item):
        if isinstance(item, dict):
            if "nodes" in item and "propagations" in item:
                summary["solves"] += 1
                for key in ("nodes", "propagations", "initial_domains", "initial_arcs"):
                    summary[key] += item.get(key, 0)
                summary["max_nodes"] = max(summary["max_nodes"], item["nodes"])
                summary["max_propagations"] = max(summary["max_propagations"], item["propagations"])
            for key, child in item.items():
                if key != "effort_summary":
                    visit(child)
        elif isinstance(item, (list, tuple)):
            for child in item:
                visit(child)
    visit(value)
    return summary


def save_result(result, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    result["funnel"] = _funnel(result)
    result["effort_summary"] = _effort_summary(result)
    result.pop("result_sha256", None)
    result["result_sha256"] = digest({key: value for key, value in result.items() if key != "execution"})
    temporary = directory / "boundary-screen.json.tmp"
    temporary.write_text(canonical_json(result)+"\n")
    temporary.replace(directory / "boundary-screen.json")


def run_batch(*, max_length=6, max_index=4, radii=(1, 2, 4), node_budget=1000,
              propagation_budget=50000, cpu_seconds=600, output_dir=None,
              pair_filter=None):
    started = time.process_time()
    catalogue = [tile.to_dict() for tile in enumerate_words(max_length)]
    noncentral = [tile for tile in catalogue if not tile["centrally_symmetric"]]
    bank = StateBank(noncentral)
    bank.cpu_deadline = started+cpu_seconds
    budgets = {"max_index": max_index, "radii": list(radii), "node_budget": node_budget,
               "propagation_budget": propagation_budget, "cpu_seconds_outer_cap": cpu_seconds,
               "state_order": "sorted tile ID, sorted D6 word", "workers": 1,
               "periodic_requires_both_species": False}
    result = {"schema": "arisearch.discovery.boundary.v1", "provenance": source_provenance(max_length),
              "catalogue": catalogue, "catalogue_sha256": digest(catalogue),
              "metadata": library_metadata(catalogue), "prior_fixture_overlap": prior_fixture_overlap(catalogue),
              "conventions": CONVENTIONS, "budgets": budgets,
              "versions": {"python": platform.python_version(), "solver": "native-bitset-ac-dfs-v1"},
              "scope": "Finite common-scale integer-length 120-degree hexagons; native full-edge honeycomb CSP; finite failures are scoped to this model; periodic absence is bounded; symbolic disks are not physical circles or certified tile-corona counts.",
              "central_omissions": [{"tile": tile["id"], "status": "MONOHEDRAL_THEOREM",
                                      "reason": "Centrally symmetric convex hexagon tiles by translations."}
                                     for tile in catalogue if tile["centrally_symmetric"]],
              "singletons": [], "pairs": []}
    effort = {"max_index": max_index, "node_budget": node_budget,
              "propagation_budget": propagation_budget}
    mono = set()
    mono_hashes = {}
    for tile in noncentral:
        singleton = ({"tile": tile["id"], "status": "NOT_RUN_OUTER_BUDGET"}
                     if time.process_time() >= bank.cpu_deadline else
                     {"tile": tile["id"], **search_periodic(bank, [tile["id"]], **effort)})
        result["singletons"].append(singleton)
        if singleton["status"] == "PERIODIC_WITNESS":
            mono.add(tile["id"])
            mono_hashes[tile["id"]] = singleton["witness_sha256"]
    pairs = list(itertools.combinations([tile["id"] for tile in noncentral], 2))
    if pair_filter is not None:
        wanted = frozenset(pair_filter)
        pairs = [pair for pair in pairs if frozenset(pair) == wanted]
        if not pairs:
            raise ValueError("--pair must name two distinct noncentral library members")
    result["selection"] = {"pair_filter": list(pairs[0]) if pair_filter is not None else None,
                           "expected_pair_count": len(pairs)}
    stopped = time.process_time() >= bank.cpu_deadline
    for pair_index, tile_ids in enumerate(pairs):
        if any(tile in mono for tile in tile_ids):
            record = {"tiles": list(tile_ids), "status": "OMITTED_MONOHEDRAL_MEMBER",
                      "positive_members": sorted(set(tile_ids) & mono),
                      "singleton_witness_refs": [{"tile": tile, "witness_sha256": mono_hashes[tile]}
                                                  for tile in sorted(set(tile_ids) & mono)],
                      "growth_status": "DEFERRED_POSITIVE_SINGLETON_WITNESS"}
        elif stopped or time.process_time()-started >= cpu_seconds:
            stopped = True
            record = {"tiles": list(tile_ids), "status": "NOT_RUN_OUTER_BUDGET",
                      "growth_status": "DEFERRED_OUTER_BUDGET"}
        else:
            record = screen_pair(bank, tile_ids, radii=radii, **effort)
            if record.get("budget_reason") == "outer_cpu_budget":
                stopped = True
        result["pairs"].append(record)
        if output_dir is not None and (pair_index+1) % 100 == 0:
            save_result(result, output_dir)
            print(f"boundary checkpoint {pair_index+1}/{len(pairs)}", file=sys.stderr)
    result["batch_complete"] = not stopped
    result["batch_complete_meaning"] = "Every scheduled pair received its bounded pipeline or a positive singleton omission; individual CSP UNKNOWN remains UNKNOWN."
    result["funnel"] = _funnel(result)
    if output_dir:
        save_result(result, output_dir)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=6)
    parser.add_argument("--max-index", type=int, default=4)
    parser.add_argument("--radii", type=int, nargs="+", default=[1, 2, 4])
    parser.add_argument("--node-budget", type=int, default=1000)
    parser.add_argument("--propagation-budget", type=int, default=50000)
    parser.add_argument("--cpu-seconds", type=float, default=600)
    parser.add_argument("--output-dir", type=Path, default=Path("research/discovery/runs/boundary-m6"))
    parser.add_argument("--pair", nargs=2)
    parser.add_argument("--grow", type=int, help="Focused pair: largest symbolic disk radius")
    args = parser.parse_args(argv)
    if min(args.max_length, args.max_index, args.node_budget, args.propagation_budget, args.cpu_seconds) <= 0:
        parser.error("bounds must be positive")
    if min(args.radii) < 1 or (args.grow is not None and args.grow < 1):
        parser.error("symbolic radii must be positive")
    if args.grow is not None and args.pair is None:
        parser.error("--grow requires --pair")
    radii = sorted(set(args.radii if args.grow is None else [1, args.grow]))
    started_cpu, started_wall = time.process_time(), time.perf_counter()
    result = run_batch(max_length=args.max_length, max_index=args.max_index, radii=radii,
                       node_budget=args.node_budget, propagation_budget=args.propagation_budget,
                       cpu_seconds=args.cpu_seconds, output_dir=args.output_dir, pair_filter=args.pair)
    command_args = list(argv) if argv is not None else sys.argv[1:]
    result["execution"] = {"command": shlex.join(["mise", "exec", "--", "conda", "run",
                           "--no-capture-output", "-n", "arisearch", "python", "-m",
                           "research.discovery.boundary_screen", *command_args]),
                           "cpu_seconds": time.process_time()-started_cpu,
                           "wall_seconds": time.perf_counter()-started_wall,
                           "result_hash_scope": "all fields except execution and result_sha256"}
    save_result(result, args.output_dir)
    from .boundary_render import write_gallery
    write_gallery(result, args.output_dir / "gallery.html")
    print(json.dumps(result["funnel"], sort_keys=True))


if __name__ == "__main__":
    main()
