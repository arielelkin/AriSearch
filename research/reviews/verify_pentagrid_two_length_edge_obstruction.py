#!/usr/bin/env python3
"""Independent integer audit of the fixed U/V edge-to-edge obstruction.

Reconstructs corner classes from actual cyclic side data. Enumerates
angle budgets recursively and checks full length cycles by a memoized
walk using every corner. Does not import the author's parity enumerator.
Also checks exact closures modulo Phi_10 and enumerates all half stars,
which remain permitted when partial-side contacts are allowed.
"""
from functools import lru_cache
from math import prod
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


root = Path(__file__).resolve().parents[2]
c = json.loads((root / "research/certificates/pentagrid-golden-metric-two-length-stars.json").read_text())
angles = {"U": (1, 3, 4, 4, 3), "V": (2, 2, 4, 3, 4)}
sides = {"U": ("L", "L", "S", "S", "S"), "V": ("L", "L", "L", "S", "S")}
require(c["U_angles_after_sides"] == list(angles["U"]), "U angles")
require(c["V_angles_after_sides"] == list(angles["V"]), "V angles")
require(c["U_side_labels"] == list(sides["U"]), "U sides")
require(c["V_side_labels"] == list(sides["V"]), "V sides")
require(c["lengths"] == {"L": "phi^3", "S": "1"}, "length values")

class_names = ("U36_LL", "U108_LS", "U144_SS", "V72_LL", "V144_LS", "V108_SS")
require(c["corner_order"] == list(class_names), "corner order")
classes = {}
for shape in ("U", "V"):
    for i in range(5):
        pair = tuple(sorted((sides[shape][i], sides[shape][(i+1) % 5])))
        name = shape+str(36*angles[shape][i])+"_"+"".join(pair)
        require(name in class_names, "reconstructed corner name")
        require(name not in classes or classes[name] == (angles[shape][i], pair),
                "consistent repeated corner")
        classes[name] = (angles[shape][i], pair)
require(set(classes) == set(class_names), "corner completeness")
weights = tuple(classes[name][0] for name in class_names)
edges = tuple(classes[name][1] for name in class_names)


def angle_vectors(total, index=0):
    if index == len(weights):
        if total == 0:
            yield ()
        return
    for count in range(total//weights[index]+1):
        for suffix in angle_vectors(total-count*weights[index], index+1):
            yield (count,)+suffix


@lru_cache(None)
def walk(remaining, first_ray, current_ray):
    if not any(remaining):
        return current_ray == first_ray
    for i, count in enumerate(remaining):
        if not count:
            continue
        a, b = edges[i]
        if current_ray not in (a, b):
            continue
        next_ray = b if current_ray == a else a
        rest = remaining[:i]+(count-1,)+remaining[i+1:]
        if walk(rest, first_ray, next_ray):
            return True
    return False


full_angle_vectors = sorted(angle_vectors(10))
full_cycles = [s for s in full_angle_vectors
               if any(walk(s, ray, ray) for ray in ("L", "S"))]
require(c["raw_integer_vectors"] == prod(10//w+1 for w in weights) == 9504, "raw domain")
require(c["stars"] == [list(s) for s in full_cycles], "all full cycles")
require(len(full_cycles) == 17, "full cycle count")
u144 = [s for s in full_cycles if s[2]]
require(u144 == [(0, 0, 1, 0, 0, 2), (0, 2, 1, 0, 0, 0)], "U144 possibilities")
require(c["U144_stars"] == [list(s) for s in u144], "retained U144 stars")
v_only = [s for s in full_cycles if not any(s[:3])]
require(c["V_only_stars"] == [list(s) for s in v_only], "V-only stars")
require(all(not s[5] for s in v_only), "no V108 full star")
require(all(s[1]+s[5] >= 2*s[2] for s in full_cycles), "supplementary count inequality")

for shape in ("U", "V"):
    endpoints = [(angles[shape][(j-1) % 5], angles[shape][j]) for j in range(5)]
    require((3, 3) not in endpoints, "no 108-to-108 native side")
    if shape == "U":
        require(endpoints[3] == (4, 4) and sides[shape][3] == "S", "critical U side")
require(c["U_side_joining_two144_corners"] == 3, "critical side certificate")
require(c["neither_tile_has_side_joining_two108_corners"] is True, "endpoint flag")

# All nine half-angle count signatures are legal without a whole-side
# numerical cycle requirement. The two listed signatures join unequal
# whole-side lengths on their common ray, and can be placed as a local
# T-junction patch by the convex-sector argument in the review.
half = sorted(angle_vectors(5))
require(len(half) == 9, "all half-star signatures")
require((1, 0, 1, 0, 0, 0) in half, "U36/U144 half star")
require((0, 0, 0, 1, 0, 1) in half, "V72/V108 half star")
require(edges[0] == edges[3] == ("L", "L") and edges[2] == edges[5] == ("S", "S"),
        "unequal-length half-star contact")

# Integer cyclotomic closure checks, independent of the metric producer.
def add(a, b):
    return tuple(a[i]+b[i] for i in range(4))


def multiply(a, b):
    p = [0]*7
    for i in range(4):
        for j in range(4):
            p[i+j] += a[i]*b[j]
    # Phi_10 = 1-z+z^2-z^3+z^4.
    for degree in range(6, 3, -1):
        leading = p[degree]
        for k, coefficient in enumerate((1, -1, 1, -1, 1)):
            p[degree-4+k] -= leading*coefficient
    return tuple(p[:4])


one, zero = (1, 0, 0, 0), (0, 0, 0, 0)
z = (0, 1, 0, 0)
z_powers = [one]
for i in range(10):
    z_powers.append(multiply(z_powers[-1], z))
require(z_powers[10] == one, "tenth root identity")
phi = add(z, z_powers[9])
require(add(multiply(phi, phi), tuple(-a for a in phi)) == one, "golden ratio identity")
long = multiply(multiply(phi, phi), phi)
directions = {"U": (0, 4, 6, 7, 8), "V": (0, 3, 6, 7, 9)}
for shape in ("U", "V"):
    result = zero
    for i, direction in enumerate(directions[shape]):
        length = long if sides[shape][i] == "L" else one
        result = add(result, multiply(length, z_powers[direction]))
        turn = (directions[shape][(i+1) % 5]-direction) % 10
        require(0 < turn < 5 and 5-turn == angles[shape][i], "corner from directed edges")
    require(result == zero, "exact polygon closure")

print("PASS: exact U/V closures and corner classes; all 17 full length cycles; "
      "critical opposite-side obstruction and V-only exclusion. "
      "All nine half-star signatures remain permitted; unrestricted tilability is unresolved.")
