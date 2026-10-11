"""Verify retained first-corona assignments without importing their search.

Rebuild the complete optional-cut variant inventory from raw side forms and
actual native bank sums. Verify the positive neighbor assignments directly;
they are relaxed finite collars and do not certify plane extension.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
from sage.all import QuadraticField, QQ, vector, matrix, identity_matrix

ROOT = Path(__file__).resolve().parents[2]
K = QuadraticField(3, "w")
w = K.gen()
h = QQ(1)/2
native_angles = (120, 90, 120, 90, 120)
native_dirs = (0, 3, 5, 8, 10)
units = tuple(vector(K, v) for v in ((1, 0), (w/2, h), (h, w/2),
    (0, 1), (-h, w/2), (-w/2, h), (-1, 0), (-w/2, -h),
    (-h, -w/2), (0, -1), (h, -w/2), (w/2, -h)))
perpendicular_arm = (1, 0, 3, 2, 5, 4, 7, 6)


def form(xs):
    return tuple(map(K, xs))


def point(xs):
    return vector(K, list(map(K, xs)))


def native(sides):
    a, b, c, d, e = sides
    assert all(t > 0 for t in sides)
    assert b-c == w*(d-a) and e == w*c+d-2*a
    return tuple(vector(K, p) for p in ((0, 0), (a, 0), (a, b),
        (a-w*c/2, b+c/2), (-e/2, w*e/2)))


def expected_inventory(forms, value):
    events = [(i, j, tuple(a+b for a, b in zip(forms[i], forms[j])))
              for i, j in product(range(8), repeat=2)
              if forms[perpendicular_arm[i]] == forms[perpendicular_arm[j]]]
    totals = [{t for i, j, t in events if i == k or j == k} for k in range(8)]
    options = [[None]+sorted({forms[j] for j in range(8)
        if forms[j] != forms[i] and value(forms[j]) < value(forms[i])
        and totals[i].intersection(totals[j])}) for i in range(8)]
    fifth = [[None]+sorted({(forms[i], forms[j]) for i, j, t in events if t == forms[e]})
             for e in (8, 9)]
    expected = Counter()
    for species in (0, 1):
        for cuts in product(*options[4*species:4*species+4], fifth[species]):
            lengths, directions, angles = [], [], []
            for side, cut in enumerate(cuts):
                full = forms[4*species+side] if side < 4 else forms[8+species]
                if cut is None:
                    parts = (full,)
                elif side == 4:
                    parts = cut
                else:
                    rem = tuple(a-b for a, b in zip(full, cut))
                    parts = (cut, rem) if side in (0, 2) else (rem, cut)
                assert all(value(p) > 0 for p in parts)
                lengths.extend(parts)
                directions.extend([native_dirs[side]]*len(parts))
                angles.extend([native_angles[side]]+[180]*(len(parts)-1))
            atoms = tuple((int(angles[i] == 120)+int(angles[(i+1) % len(angles)] == 120),
                           p, directions[i], angles[i]) for i, p in enumerate(lengths))
            expected[species, atoms] += 1
    return expected


def disjoint_interiors(p, q):
    # Independently stated exact SAT: intervals of projections onto every edge
    # normal of either polygon. Weak separation includes boundary touching.
    for polygon in (p, q):
        for i, a in enumerate(polygon):
            edge = polygon[(i+1) % len(polygon)]-a
            normal = vector(K, [-edge[1], edge[0]])
            P = [z.dot_product(normal) for z in p]
            Q = [z.dot_product(normal) for z in q]
            if max(P) <= min(Q) or max(Q) <= min(P):
                return True
    return False


source = json.loads((ROOT / "research/certificates/partial-contact-cairo-remaining-eighteen-residual-colors.json").read_text())
keys = (("orbit1", 759), ("orbit6", 906), ("orbit7", 575),
        ("orbit6", 239), ("separated", 46), ("separated", 49), ("orbit7", 459))
grand_total = 0
for pattern, flat_id in keys:
    path = ROOT / f"research/certificates/partial-contact-cairo-first-corona-{pattern}-flat{flat_id}.json"
    cert = json.loads(path.read_text())
    key = (pattern, flat_id, cert["source_order_chamber_id"])
    raw = next(r for r in source["records"] if
        (r["pattern"], r["flat_id"], r["source_order_chamber_id"]) == key)
    assert cert["native_arm_forms"] == raw["arm_forms"]
    assert cert["native_fifth_forms"] == raw["e_forms"]
    assert cert["sample_kernel_point"] == raw["sample_kernel_point"]
    parameters = form(raw["sample_kernel_point"])
    forms = [form(row) for row in raw["arm_forms"]+raw["e_forms"]]
    value = lambda row: sum(a*b for a, b in zip(row, parameters))
    originals = [native([value(forms[4*s+i]) for i in range(4)]+[value(forms[8+s])])
                 for s in (0, 1)]
    assert originals == [tuple(map(point, polygon)) for polygon in cert["original_native_polygons"]]
    if key[:2] == ("orbit6", 239):
        assert w*value(forms[0])/4 < value(forms[1]) < value(forms[0])/w
    variants = []
    actual = Counter()
    edge_index = {}
    for vid, record in enumerate(cert["variant_inventory"]):
        species = record["species"]
        atoms = tuple((a["endpoint120_count"], form(a["length_form"]),
                       a["direction_label"], a["angle_at_start"]) for a in record["atoms"])
        local = tuple(map(point, record["local_atomic_vertices"]))
        assert len(atoms) == len(local)
        assert [p for p, a in zip(local, atoms) if a[3] != 180] == list(originals[species])
        for i, (count, length, direction, angle) in enumerate(atoms):
            assert value(length) > 0
            assert local[(i+1) % len(local)]-local[i] == value(length)*units[direction]
            assert count == int(angle == 120)+int(atoms[(i+1) % len(atoms)][3] == 120)
            edge_index.setdefault((species, count, length), []).append((vid, i))
        actual[species, atoms] += 1
        variants.append((species, atoms, local))
    assert actual == expected_inventory(forms, value)
    assert len(variants) == cert["variant_count"]
    frames, polygons, origins = [], [], []
    for record in cert["placements"]:
        u = units[record["theta"]]
        sign = record["sign"]
        frame = matrix(K, [[u[0], -sign*u[1]], [u[1], sign*u[0]]])
        assert frame.transpose()*frame == identity_matrix(K, 2)
        assert frame.det() == sign
        origin = point(record["origin"])
        polygons.append(tuple(origin+frame*p for p in originals[record["species"]]))
        frames.append(frame)
        origins.append(origin)
    assert len(polygons) == cert["placement_count"]
    assert len({tuple(sorted(tuple(p) for p in polygon)) for polygon in polygons}) == len(polygons)
    assert cert["counts"] == {"finite-corona-witness": len(variants)}
    assert len(cert["variant_results"]) == len(variants)
    for vid, result in enumerate(cert["variant_results"]):
        assert result["central_variant"] == vid and result["result"] == "finite-corona-witness"
        species, atoms, local = variants[vid]
        assignments = result["assigned_neighbors"]
        assert set(map(int, assignments)) == set(range(len(atoms)))
        chosen = []
        for text, pid in assignments.items():
            i = int(text)
            assert pid in cert["candidate_domains"][vid][i]
            neighbor = cert["placements"][pid]
            count, length, _, angle = atoms[i]
            A = (local[i], local[(i+1) % len(local)])
            possible = False
            for uid, j in edge_index.get((neighbor["species"], count, length), []):
                _, other_atoms, other_local = variants[uid]
                C = tuple(origins[pid]+frames[pid]*other_local[k]
                          for k in (j, (j+1) % len(other_local)))
                reverse = neighbor["sign"] == 1
                if A != (C[::-1] if reverse else C):
                    continue
                outer_angles = (other_atoms[j][3], other_atoms[(j+1) % len(other_atoms)][3])
                if reverse:
                    outer_angles = outer_angles[::-1]
                central_angles = (angle, atoms[(i+1) % len(atoms)][3])
                assert all((a == 120) == (b == 120) and a+b <= 360
                           for a, b in zip(central_angles, outer_angles))
                possible = True
                break
            assert possible
            assert disjoint_interiors(originals[species], polygons[pid])
            chosen.append(pid)
        for a, b in product(set(chosen), repeat=2):
            assert a == b or disjoint_interiors(polygons[a], polygons[b])
    grand_total += len(variants)
    print("PASS exact relaxed corona", key, "all", len(variants), "native variants")
assert grand_total == 391
print("PASS complete391 finite assignments, no producer imports; no global extension inferred")
