"""Bounded exact first-corona relaxation on remaining Cairo native strata.

For each central full native subdivision, every atomic edge is assigned an
actual original neighbor. Different assigned neighbors must have disjoint
interiors (or represent the identical occurrence). Vertex-only neighbors and
neighbor cut consistency away from the central boundary are ignored, so this
is a necessary relaxation, never a plane-extension certificate. No old copied
variant frequency or fixed quotient domain is enlarged.
"""
from pathlib import Path
from collections import Counter
import argparse
import json
from sage.all import QuadraticField, QQ, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
K = QuadraticField(3, "w")
w = K.gen()
h = QQ(1)/2
directions = tuple(vector(K, v) for v in ((1, 0), (w/2, h), (h, w/2),
    (0, 1), (-h, w/2), (-w/2, h), (-1, 0), (-w/2, -h),
    (-h, -w/2), (0, -1), (h, -w/2), (w/2, -h)))
native_directions = (0, 3, 5, 8, 10)


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def native(word):
    a, b, c, d, e = word
    assert all(q > 0 for q in word)
    assert b-c == w*(d-a) and e == w*c+d-2*a
    return tuple(vector(K, v) for v in ((0, 0), (a, 0), (a, b),
        (a-w*c/2, b+c/2), (-e/2, w*e/2)))


def canonical_polygon(p):
    return tuple(sorted(tuple(v) for v in p))


def overlap(p, q):
    # Exact separating-axis test for two CCW strictly convex polygons.
    # A support line of either polygon weakly separating the other proves
    # disjoint interiors, including contact at an edge or a single vertex.
    return not any(all(cross(a[(i+1) % 5]-a[i], z-a[i]) <= 0 for z in b)
                   for a, b in ((p, q), (q, p)) for i in range(5))


def inventory(record):
    # Producer inventory is used only for this explicitly preliminary finite
    # experiment. Any negative theorem would require independent native audit.
    path = ROOT / "research/searches/partial-contact-cairo-two-cross-residual-colors.py"
    text = path.read_text().split("ap=argparse.ArgumentParser()")[0]
    ns = {"__file__": str(path)}
    exec(text, ns)
    chamber = {"sample_kernel_point": record["sample_kernel_point"],
               "sample_parameter": "0"}
    raw, edges, corners, *_ = ns["M"](record, chamber)
    value = lambda f: sum(K(a)*K(b) for a, b in zip(f, record["sample_kernel_point"]))
    words = [tuple(value(row) for row in record["arm_forms"][4*s:4*s+4])+(
        value(record["e_forms"][s]),) for s in (0, 1)]
    polygons = [native(z) for z in words]
    variants = []
    for species, cuts, cs in raw:
        local, pos = [], vector(K, [0, 0])
        atoms = []
        for corner in cs:
            local.append(pos)
            angle, prev, nxt = corners[corner]
            key, colour = edges[nxt]
            native_side = key[1]
            length = value(colour[1])
            assert length > 0
            atoms.append((colour, native_directions[native_side], angle))
            pos = pos+length*directions[native_directions[native_side]]
        assert pos == vector(K, [0, 0])
        assert [v for v, atom in zip(local, atoms) if atom[2] != 180] == list(polygons[species])
        variants.append((species, local, atoms))
    return variants, polygons


def run(record, node_cap):
    variants, originals = inventory(record)
    edge_index = {}
    for vid, (species, local, atoms) in enumerate(variants):
        for j, atom in enumerate(atoms):
            edge_index.setdefault(atom[0], []).append((vid, j))
    placements, polygons, descriptions = [], [], []
    placement_index = {}
    # Every central tile is in the original native frame. Each possible full
    # matching neighbor atom is developed by exact 30-degree frame/sign.
    domains = []
    for vid, (species, local, atoms) in enumerate(variants):
        variant_domains = []
        for i, (colour, direction, angle) in enumerate(atoms):
            options = set()
            for uid, j in edge_index[colour]:
                typ, other, o_atoms = variants[uid]
                for sign in (-1, 1):
                    reverse = sign == 1
                    theta = (direction-sign*o_atoms[j][1]+(6 if reverse else 0)) % 12
                    c, s = directions[theta]
                    frame = matrix(K, [[c, -sign*s], [s, sign*c]])
                    offset = local[(i+1) % len(local)] if reverse else local[i]
                    origin = offset-frame*other[j]
                    end_a = local[i] if reverse else local[(i+1) % len(local)]
                    assert origin+frame*other[(j+1) % len(other)] == end_a
                    cp = tuple(origin+frame*v for v in originals[typ])
                    if sign == -1:
                        cp = cp[::-1]
                    # Native corner angles at both matched endpoints must fit
                    # a Cairo star. Ignoring all other angles is a relaxation.
                    central_angles = (angle, atoms[(i+1) % len(atoms)][2])
                    other_angles = (o_atoms[j][2], o_atoms[(j+1) % len(o_atoms)][2])
                    if reverse:
                        other_angles = other_angles[::-1]
                    if any((a == 120) != (b == 120) or a+b > 360
                           for a, b in zip(central_angles, other_angles)):
                        continue
                    assert not overlap(originals[species], cp)
                    canonical = canonical_polygon(cp)
                    if canonical not in placement_index:
                        pid = len(placements)
                        placement_index[canonical] = pid
                        placements.append(canonical)
                        polygons.append(cp)
                        descriptions.append({"species": typ, "theta": theta,
                            "sign": sign, "origin": [str(t) for t in origin]})
                    options.add(placement_index[canonical])
            variant_domains.append(sorted(options))
        domains.append(variant_domains)
    clash_cache = {}

    def clash(a, b):
        if a == b:
            return False
        key = tuple(sorted((a, b)))
        if key not in clash_cache:
            clash_cache[key] = overlap(polygons[a], polygons[b])
        return clash_cache[key]

    outcomes, node_counts = [], []
    certificates = []
    for vid, ds in enumerate(domains):
        nodes = 0
        cutoff = False
        answer = None

        def solve(remaining, assigned):
            nonlocal nodes, cutoff, answer
            nodes += 1
            if node_cap and nodes > node_cap:
                cutoff = True
                return False
            if not remaining:
                answer = assigned
                return True
            legal = [(i, [p for p in ds[i] if not any(clash(p, q) for q in assigned.values())])
                     for i in remaining]
            i, ps = min(legal, key=lambda z: (len(z[1]), z[0]))
            for p in ps:
                if cutoff:
                    return False
                if solve(remaining-{i}, dict(assigned, **{str(i): p})):
                    return True
            return False

        sat = solve(set(range(len(ds))), {})
        outcome = "finite-corona-witness" if sat else "resource-limit" if cutoff else "finite-corona-exhausted"
        outcomes.append(outcome)
        node_counts.append(nodes)
        certificates.append({"central_variant": vid, "result": outcome,
            "nodes": nodes, "assigned_neighbors": answer})
    print("CORONA", record["pattern"], record["flat_id"], record["source_order_chamber_id"],
          "variants", len(variants), "placements", len(placements), "pair_tests", len(clash_cache),
          "results", dict(Counter(outcomes)), "nodes", sum(node_counts), flush=True)
    encoded_variants = [{"species": species, "local_atomic_vertices": [[str(t) for t in p] for p in local],
        "atoms": [{"endpoint120_count": colour[0], "length_form": [str(t) for t in colour[1]],
                   "direction_label": direction, "angle_at_start": angle}
                  for colour, direction, angle in atoms]}
        for species, local, atoms in variants]
    return {"pattern": record["pattern"], "flat_id": record["flat_id"],
        "source_order_chamber_id": record["source_order_chamber_id"],
        "sample_kernel_point": record["sample_kernel_point"],
        "variant_count": len(variants), "placement_count": len(placements),
        "pair_tests": len(clash_cache), "node_bound_per_variant": node_cap,
        "counts": dict(Counter(outcomes)), "placements": descriptions,
        "native_arm_forms": record["arm_forms"], "native_fifth_forms": record["e_forms"],
        "original_native_polygons": [[[str(t) for t in p] for p in polygon] for polygon in originals],
        "variant_inventory": encoded_variants, "candidate_domains": domains,
        "variant_results": certificates}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", required=True)
    ap.add_argument("--flat", required=True, type=int)
    ap.add_argument("--chamber", type=int, default=0)
    ap.add_argument("--max-nodes", type=int, default=100000)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    source = ROOT / "research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json"
    record = next(r for r in json.loads(source.read_text())["records"]
                  if (r["pattern"], r["flat_id"], r["source_order_chamber_id"]) ==
                     (args.pattern, args.flat, args.chamber))
    result = run(record, args.max_nodes)
    result["scope"] = "exact finite first-corona relaxation at retained metric only; no plane-extension or whole higher-dimensional-domain claim"
    Path(args.output).write_text(json.dumps(result, indent=2)+"\n")
