"""Independent retained geometry and scope checks; no producer import.

Rebuilds the 1430-signature closure census and checks all retained native
parents and jointly completed partial-contact patches in a separate field.
The accompanying review audits the negative T-pruning/exhaustiveness logic.
"""
import json
from collections import Counter
from functools import cache
from itertools import product
from pathlib import Path
from sage.all import AA, CyclotomicField, QQ, QQbar

K = CyclotomicField(24)
z = K.gen()
conj = K.hom([z**-1], K)
embed = K.hom([QQbar.zeta(24)], QQbar)
ii = z**6
r, s = z**2+z**-2, z**3+z**-3
g = r+s
assert r*r == 3 and s*s == 2


@cache
def real(q):
    assert conj(q) == q
    return AA(embed(q))


def decode(coefficients):
    return sum((QQ(q)*g**i for i, q in enumerate(coefficients)), K(0))


def polygon(encoded):
    return [decode(p[0])+ii*decode(p[1]) for p in encoded]


def cross(a, b):
    return (conj(a)*b-a*conj(b))/(2*ii)


def area(face):
    return sum(cross(p, face[(i+1) % len(face)]) for i, p in enumerate(face))/2


def ccw(face):
    return face if real(area(face)) > 0 else list(reversed(face))


def strict(face):
    face = ccw(face)
    assert len(set(face)) == len(face)
    assert all(real(cross(face[(i+1) % len(face)]-p, q-p)) > 0
               for i, p in enumerate(face) for j, q in enumerate(face)
               if j not in (i, (i+1) % len(face)))


def separated(a, b):
    return any(all(real(cross(a[(i+1) % len(a)]-p, q-p)) <= 0 for q in b)
               for i, p in enumerate(a))


P = [K(0), K(3), 4+ii*r, QQ(7)/2+ii*3*r/2, ii/r]
Q = [K(0), K(3), 3+1/(s*r)+ii/(s*r),
     3+1/(s*r)+ii*(7/r+1/(s*r)), s+ii*(7/r+1/(s*r)),
     ii*(7/r+1/(s*r)-s)]
shapes = {"P": P, "Q": Q}
angles = {"P": [90, 120, 120, 90, 120], "Q": [90, 135, 135, 90, 135, 135]}
for face in shapes.values():
    strict(face)
assert area(P) == 10/r and area(P) != area(Q)
cairo_lengths = [K(1), 7/r, 1/r, K(3), K(2)]
cairo = [z**-8*(p-P[2]) for p in P[2:]+P[:2]]
assert [cairo[(i+1) % 5]-cairo[i] for i in range(5)] == [
    length*z**power for length, power in zip(cairo_lengths, (0, 6, 10, 16, 20))]
assert len(set(cairo_lengths[:4])) == 4
assert cairo_lengths[1]-cairo_lengths[2] == r*(cairo_lengths[3]-cairo_lengths[0])
assert cairo_lengths[4] == r*cairo_lengths[2]+cairo_lengths[3]-2*cairo_lengths[0]


def congruent_native(face, shape):
    for native in (shape, [conj(p) for p in shape]):
        rotation = (face[1]-face[0])/(native[1]-native[0])
        if rotation*conj(rotation) == 1 and all(
                face[i]-face[0] == rotation*(native[i]-native[0]) for i in range(len(face))):
            return
    raise AssertionError("Retained native vertex order is not an isometric source copy")


data = json.loads(Path("research/certificates/nonconvex-parent-construction-2026-10-14-pentagon-repair.json").read_text())
assert polygon(data["atoms"]["P_vertices"]) == P
assert polygon(data["atoms"]["Q_vertices"]) == Q
assert data["inflation"] == 2 and data["inflated_atomic_counts"] == [4, 4]
assert data["counts"] == {"native_attachments": 8, "nonconvex_parents": 8}

# Independently enumerate the full native mixed-edge attachment count.
equal_sides = [(i, j) for i in range(5) for j in range(6)
               if (P[(i+1) % 5]-P[i])*conj(P[(i+1) % 5]-P[i]) ==
                  (Q[(j+1) % 6]-Q[j])*conj(Q[(j+1) % 6]-Q[j])]
assert len(equal_sides) == 4
for parent in data["parents"]:
    i, j = parent["P_native_side"], parent["Q_native_side"]
    assert (i, j) in equal_sides
    image = polygon(parent["Q_placement"])
    congruent_native(image, Q)
    assert separated(ccw(P), ccw(image)) or separated(ccw(image), ccw(P))
    assert area(polygon(parent["boundary"])) == area(P)+area(Q)
    assert any(angles["P"][k] == 120 and angles["Q"][image.index(P[k])] in (90, 135)
               for k in (i, (i+1) % 5))
    assert parent["plane_extension"] == "IMPOSSIBLE_NATIVE_SEAM_ENDPOINT"

records = data["partial_contact_gate"]["records"]
assert len(records) == 216
expected = set(product(product((1, 2, 4), (False, True)), repeat=3))
actual = {tuple(zip(row["native_corners"], row["reverse_arms"])) for row in records}
assert actual == expected
statuses = Counter(row["status"] for row in records)
assert statuses == {"NO_90_GUEST_COMPLETION": 116, "SHORT_RAY_END_IS_120": 80,
                    "LOCAL_COMPLETION_SURVIVOR": 20}
filled_values = {90*a+120*b+135*c+180*d
                 for a in range(5) for b in range(4) for c in range(3) for d in range(3)}
switch_patches = 0
for row in records:
    central = [polygon(face) for face in row["central_P_vertices"]]
    for native, face in zip(row["native_corners"], central):
        congruent_native(face, P)
        assert face[native] == 0
    if row["status"] != "LOCAL_COMPLETION_SURVIVOR":
        continue
    assert len(row["joint_completions"]) == 1
    guests = row["joint_completions"][0]
    parts = [("P", face) for face in central]
    identity = {frozenset(face) for _, face in parts}
    for guest in guests:
        face = polygon(guest["vertices"])
        congruent_native(face, shapes[guest["type"]])
        if frozenset(face) not in identity:
            identity.add(frozenset(face))
            parts.append((guest["type"], face))
    faces = [ccw(face) for _, face in parts]
    for face in faces:
        strict(face)
    assert all(separated(a, b) or separated(b, a)
               for i, a in enumerate(faces) for b in faces[i+1:])
    for point in {p for _, face in parts for p in face}:
        total = 0
        for name, face in parts:
            if point in face:
                total += angles[name][face.index(point)]
            elif any(cross(b-a, point-a) == 0 and
                     real((point-a)*conj(point-b)+(point-b)*conj(point-a)) < 0
                     for a, b in zip(face, face[1:]+face[:1])):
                total += 180
        assert total <= 360 and 360-total in filled_values
    switches = sum(guest["host_switch"] for guest in guests)
    if 4 in row["native_corners"]:
        assert switches == 2 and len(parts) == 5
        switch_patches += 1
assert switch_patches == 6

# Rebuild the zero-B exact angle-grid closure without author code.
L = CyclotomicField(36)
w = L.gen()
raw, positive = 0, []
grid = range(10, 180, 10)
arcs = [q for q in grid if q != 120]
for beta, eta, u in product(arcs, arcs, grid):
    v = 480-beta-eta-u
    if v not in grid:
        continue
    raw += 1
    directions = [0, 60, 240-beta, u+eta-60, u+eta, u+180]
    coeff_p = sum((w**((d//10) % 36) for d in directions[:3]), L(0))
    coeff_one = sum((w**((d//10) % 36) for d in directions[3:]), L(0))
    assert coeff_p != 0
    ratio = -coeff_one/coeff_p
    if ratio == ratio.conjugate() and AA(ratio) > 0 and ratio != 1:
        positive.append((beta, eta, u, v))
assert raw == 1430 and not positive
base = json.loads(Path("research/certificates/nonconvex-parent-construction-2026-10-14.json").read_text())
assert base["counts"] == {"angle_signatures": 1430, "positive_distinct_closed_B": 0,
                          "atomic_pairs": 0, "atomic_gate_survivors": 0}
print("PASS independent closure1430/0; all8 nonextendible mixed parents; complete216 placement keys;20 exact joint patches including6 five-P host-switch patches")
