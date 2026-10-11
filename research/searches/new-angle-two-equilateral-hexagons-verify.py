#!/usr/bin/env python3
"""Exact symbolic checks for two rational-angle equilateral hexagons.

No bounded rational-angle sweep: symbolic triple coefficients are exhausted.
The root-of-unity classification and defect-free limit are proof dependencies,
not claims established by this finite verifier.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
import json

# Labels A+, A-, B+, B-; every angle is 120 plus its affine deviation.
coefficients = ((1, 0), (-1, 0), (0, 1), (0, -1))
triangle_rows = []
for triple in combinations_with_replacement(range(4), 3):
    x = sum(coefficients[i][0] for i in triple)
    y = sum(coefficients[i][1] for i in triple)
    ratio = Fraction(-x, y) if y else None
    legal = ratio is not None and ratio > 0
    triangle_rows.append({"corners": list(triple), "a_coefficient": x,
                          "b_coefficient": y,
                          "positive_b_over_a": str(ratio) if legal else None})
ratios = sorted({Fraction(r["positive_b_over_a"])
                 for r in triangle_rows if r["positive_b_over_a"] is not None})
assert ratios == [Fraction(1, 2), Fraction(2)]
ratio_two = [r["corners"] for r in triangle_rows if r["positive_b_over_a"] == "2"]
assert ratio_two == [[0, 0, 3], [1, 1, 2]]
assert all(sum(coefficients[i][0] for i in triple) != 0
           for triple in combinations_with_replacement((0, 1), 3))

# Sporadic+triangle: affine angles constant + coefficient*a.
angles = ((120, 1), (120, -1), (60, 0), (108, 0), (168, 0))
sporadic_parameter_rows = []
for triple in combinations_with_replacement(range(5), 3):
    if 4 not in triple:
        continue
    constant = sum(angles[i][0] for i in triple)
    slope = sum(angles[i][1] for i in triple)
    if slope:
        root = Fraction(360 - constant, slope)
        if 0 < root < 60:
            sporadic_parameter_rows.append({"corners": list(triple), "a": str(root)})
    else:
        assert constant != 360
assert sorted(Fraction(r["a"]) for r in sporadic_parameter_rows) == [12, 24, 36]
sporadic_cases = []
for a in (12, 24, 36):
    evaluated = [constant + slope * a for constant, slope in angles]
    triples = [list(t) for t in combinations_with_replacement(range(5), 3)
               if sum(evaluated[i] for i in t) == 360]
    covered = {i for t in triples for i in t}
    missing = sorted(set(range(5)) - covered)
    # Every sporadic corner category is native: labels2,3,4 counts1,3,2.
    missing_sporadic = sorted({2, 3, 4} - covered)
    assert missing_sporadic
    sporadic_cases.append({"a": a, "angles": evaluated, "legal_triples": triples,
                            "uncovered_categories": missing,
                            "uncovered_sporadic_categories": missing_sporadic})
sporadic_only = [list(t) for t in combinations_with_replacement((60, 108, 168), 3)
                 if sum(t) == 360]
assert not sporadic_only

# Three CCW faces: 0,1 are A with deviations +,- alternating;
# 2 is B with deviations -2,+2 alternating. A corner indices have been
# cyclically shifted by one from the source edge-direction normalization.
pairings = []
for c in range(3):
    for j in range(3):
        d = (c + (1 if j % 2 == 0 else 2)) % 3
        pairings.append(((c, j), (d, j + 3)))
assert len({s for pair in pairings for s in pair}) == 18
parent = list(range(18))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    parent[find(x)] = find(y)

links = defaultdict(list)
seam_endpoint_pairs = []
adjacency = defaultdict(set)
for (c, j), (d, k) in pairings:
    assert c != d
    adjacency[c].add(d)
    adjacency[d].add(c)
    # Opposite endpoint order for CCW boundary sides.
    for (f, v), (g, w) in (((c, j), (d, (k + 1) % 6)),
                            ((c, (j + 1) % 6), (d, k))):
        seam_endpoint_pairs.append([[f, v], [g, w]])
        union(6*f+v, 6*g+w)
        links[(f, v)].append((g, w))
        links[(g, w)].append((f, v))
components = defaultdict(list)
for x in range(18):
    components[find(x)].append(divmod(x, 6))
classes = sorted(sorted(vertices) for vertices in components.values())
assert len(classes) == 6
assert all(len(vs) == 3 and {f for f, j in vs} == {0, 1, 2} for vs in classes)
flat_vertices = []
for vs in classes:
    assert len({j % 2 for f, j in vs}) == 1
    assert all(len(links[v]) == 2 and set(links[v]) == set(vs)-{v} for v in vs)
    # Symbolically sum the angle coefficients; constant is 3*120.
    coefficient = sum((1 if j % 2 == 0 else -1) if f != 2
                      else (-2 if j % 2 == 0 else 2) for f, j in vs)
    assert coefficient == 0
    flat_vertices.append({"corners": [list(v) for v in vs],
                          "constant_angle_degrees": 360,
                          "a_coefficient": coefficient})
seen = {0}
while True:
    expanded = seen | {g for f in seen for g in adjacency[f]}
    if expanded == seen:
        break
    seen = expanded
assert seen == {0, 1, 2}
assert len(classes) - len(pairings) + 3 == 0
result = {
    "status": "PASS",
    "domain": {
        "triangle_affine_multisets": len(triangle_rows),
        "sporadic_168_containing_multisets": sum(1 for t in combinations_with_replacement(range(5), 3) if 4 in t),
        "sporadic_evaluated_parameter_values": [12, 24, 36],
        "all_sporadic_evaluated_multisets_per_value": 35,
        "torus_faces": 3,
        "torus_edges": len(pairings),
        "torus_vertices": len(classes)
    },
    "triangle_symbolic_rows": triangle_rows,
    "positive_triangle_parameter_ratios": [str(x) for x in ratios],
    "b_equals_two_a_triples": ratio_two,
    "sporadic_168_parameter_rows": sporadic_parameter_rows,
    "sporadic_cases": sporadic_cases,
    "sporadic_only_triples": sporadic_only,
    "torus_pairings": [[list(a), list(b)] for a, b in pairings],
    "torus_flat_vertices": flat_vertices,
    "torus_seam_endpoint_pairs": seam_endpoint_pairs,
    "reference_reflections": [False, False, False],
    "torus_connected": True,
    "torus_reversed_endpoint_gluing": True,
    "torus_euler_characteristic": 0,
    "proof_dependencies_not_computed": [
        "unrestricted positive weight-six root-of-unity classification",
        "defect-free edge-to-edge trivalent hexagon limit",
        "complete simply connected flat surface is the Euclidean plane"
    ]
}
print(json.dumps(result, indent=2, sort_keys=True))
