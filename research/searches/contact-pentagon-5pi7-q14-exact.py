"""Exact bounded P5/Q14 native-ring experiment; frozen JSON output.

Domain: the displayed word first, then all 35 opposite-seven binary periods
with three unit/four v lengths. Both hands and every equal native side alias
are enumerated before audited necessary palette/AA-dimer reductions.
No metric grid, randomization, solver, or patch-depth enlargement.
"""
import argparse
import json
from functools import cache
from itertools import combinations
from pathlib import Path
from platform import python_version
from sage.all import AA, QQ, QQbar, NumberField, PolynomialRing
from sage.env import SAGE_VERSION

R = PolynomialRing(QQ, "t")
t = R.gen()
field_polynomial = t**12-t**10+t**8-t**6+t**4-t**2+1
K = NumberField(field_polynomial, "z")
z = K.gen()
embedding = K.hom([QQbar.zeta(28)], QQbar)
conjugate = K.hom([z**-1], K)
ii = z**7
s = (z-z**-1)/(2*ii)
y = 2*s+4*s**2
v = 1+2*s*(1-y)
lengths = [K(1), K(1), K(1), v, y]
directions = [-5, 1, 7, 13, 19]


@cache
def real(q):
    assert q == conjugate(q)
    return AA(embedding(q))


@cache
def cross(a, b):
    return (conjugate(a)*b-a*conjugate(b))/(2*ii)


def area(polygon):
    return sum(cross(p, polygon[(i+1) % len(polygon)])
               for i, p in enumerate(polygon))/2


def strictly_convex(polygon):
    assert real(area(polygon)) > 0 and len(set(polygon)) == len(polygon)
    for i, p in enumerate(polygon):
        assert all(real(cross(polygon[(i+1) % len(polygon)]-p, q-p)) > 0
                   for j, q in enumerate(polygon)
                   if j not in (i, (i+1) % len(polygon)))


def separated(f, g):
    return any(all(real(cross(f[(i+1) % len(f)]-p, q-p)) <= 0 for q in g)
               for i, p in enumerate(f))


def polygon_from_edges(edges):
    polygon = [K(0)]
    for edge in edges[:-1]:
        polygon.append(polygon[-1]+edge)
    assert polygon[-1]+edges[-1] == 0
    strictly_convex(polygon)
    return polygon


def encode(q):
    return [str(c) for c in q.list()]+["0"]*(12-len(q.list()))


P = polygon_from_edges([length*z**power for length, power in zip(lengths, directions)])
assert [(directions[i]-directions[i-1]) % 28 for i in range(5)] == [4, 6, 6, 6, 6]
assert real(s) > QQ(22)/100 and real(s) < QQ(23)/100
assert 0 < real(y) < 1 < real(v)
assert (z**5+z**-5)/(z+z**-1) == 2*s
assert (z**5-z**-5)/(2*ii) == 1-2*s**2
assert v == 1+(1-y)*(z**5+z**-5)/(z+z**-1)
assert 1 == (1+y)*(1-2*s**2)-(1+v)*s
assert len({q*conjugate(q) for q in lengths}) == 3

# Complete angle and native-tag arithmetic before geometric enumeration.
angle_stars = [(a, b, c) for a in range(4) for b in range(4) for c in range(3)
               if 5*a+4*b+6*c == 14]
assert angle_stars == [(0, 2, 1), (2, 1, 0)]
beta_pairs = [(lengths[i-1], lengths[i]) for i in range(1, 5)]
eligible_beta = [i for i, pair in enumerate(beta_pairs, 1)
                 if pair[0] == pair[1] and pair[0] in (lengths[0], lengths[4])]
assert eligible_beta == [1, 2]
assert all(beta_pairs[i-1] == (K(1), K(1)) for i in eligible_beta)
assert lengths[0] != lengths[4]


def placements(Q, slot, target_length):
    out = []
    for native_side, source_length in enumerate(lengths):
        if source_length != target_length:
            continue
        for hand in (1, -1):
            base = P if hand == 1 else [conjugate(q) for q in P]
            start, end = (Q[(slot+1) % 14], Q[slot]) if hand == 1 else (Q[slot], Q[(slot+1) % 14])
            rotation = (end-start)/(base[(native_side+1) % 5]-base[native_side])
            assert rotation*conjugate(rotation) == 1
            shift = start-rotation*base[native_side]
            native = [rotation*q+shift for q in base]
            ccw = native if hand == 1 else list(reversed(native))
            strictly_convex(ccw)
            assert separated(Q, ccw) or separated(ccw, Q)
            reason = None
            if native_side == 0:
                reason = "alpha endpoint cannot meet Qgamma"
            elif native_side == 2:
                reason = "forced v-Q contact makes adjacent w-Q contact impossible"
            else:
                assert native_side in (1, 3)
            out.append(dict(native_side=native_side, hand=hand, rotation=rotation,
                            shift=shift, native=native, ccw=ccw, rejection=reason))
    return out


def other_endpoint(placement, vertex):
    native = placement["native"]
    k = native.index(vertex)
    side = placement["native_side"]
    assert k in (side, (side+1) % 5)
    return native[(k-1) % 5] if k == side else native[(k+1) % 5]


def compatible(left, right, vertex):
    # Equal actual PP edge endpoints, rather than merely matching length tags.
    return other_endpoint(left, vertex) == other_endpoint(right, vertex)


def forced_alpha_mate(guest):
    native = guest["native"]
    edge = native[0]-native[4]
    rotation = edge/conjugate(edge)
    shift = native[4]-rotation*conjugate(native[4])
    mate = [rotation*conjugate(q)+shift for q in native]
    assert mate[0] == native[0] and mate[4] == native[4]
    ccw = list(reversed(mate)) if guest["hand"] == 1 else mate
    strictly_convex(ccw)
    assert separated(guest["ccw"], ccw) or separated(ccw, guest["ccw"])
    return ccw


def audit_word(period):
    tags = list(period)*2
    qlengths = [v if tag == "v" else K(1) for tag in tags]
    Q = polygon_from_edges([q*z**(2*i) for i, q in enumerate(qlengths)])
    all_guests = [placements(Q, i, q) for i, q in enumerate(qlengths)]
    guests = [[g for g in slot if g["rejection"] is None] for slot in all_guests]
    assert all(len(slot) == 2 for slot in guests)
    transitions = []
    for i in range(14):
        vertex = Q[(i+1) % 14]
        transitions.append([[int(compatible(a, b, vertex)) for b in guests[(i+1) % 14]]
                            for a in guests[i]])
    cycles = []

    def extend(path):
        i = len(path)-1
        if len(path) == 14:
            if transitions[13][path[-1]][path[0]]:
                cycles.append(tuple(path))
            return
        for nxt in range(2):
            if transitions[i][path[-1]][nxt]:
                extend(path+[nxt])

    for first in range(2):
        extend([first])
    survivors = []
    overlap_rejections = []
    completed_dimer_survivors = []
    forced_dimer_rejections = []
    retained_patch = None
    for cycle in cycles:
        faces = [guests[i][c]["ccw"] for i, c in enumerate(cycle)]
        bad = next(((i, j) for i, f in enumerate(faces) for j, g in enumerate(faces[i+1:], i+1)
                    if not (separated(f, g) or separated(g, f))), None)
        if bad is None:
            survivors.append(cycle)
            patch = [Q]+faces
            identity = {frozenset(face) for face in patch}
            for slot, choice in enumerate(cycle):
                mate = forced_alpha_mate(guests[slot][choice])
                key = frozenset(mate)
                if key not in identity:
                    identity.add(key)
                    patch.append(mate)
            bad_mate = next(((i, j) for i, f in enumerate(patch) for j, g in enumerate(patch[i+1:], i+1)
                             if not (separated(f, g) or separated(g, f))), None)
            if bad_mate is None:
                completed_dimer_survivors.append(dict(cycle=cycle, face_count=len(patch)))
                if retained_patch is None:
                    retained_patch = dict(cycle=cycle, faces=[list(map(encode, face)) for face in patch])
            else:
                forced_dimer_rejections.append(dict(cycle=cycle, overlapping_patch_faces=bad_mate))
        else:
            overlap_rejections.append(dict(cycle=cycle, overlapping_guest_slots=bad))
    guest_data = [[dict(native_side=g["native_side"], hand=g["hand"], rejection=g["rejection"],
                        rotation=encode(g["rotation"]), shift=encode(g["shift"]))
                   for g in slot] for slot in all_guests]
    return dict(period="".join(period), Q_vertices=[encode(q) for q in Q],
                raw_native_guests=guest_data, allowed_native_guests_per_slot=2,
                adjacent_PP_endpoint_transitions=transitions,
                complete_native_cycles=cycles, overlap_rejections=overlap_rejections,
                disjoint_native_cycles=survivors,
                forced_dimer_rejections=forced_dimer_rejections,
                forced_dimer_completed_patches=completed_dimer_survivors,
                retained_completed_patch=retained_patch)


displayed = tuple("vvu vvuu".replace(" ", ""))
assert displayed == ("v", "v", "u", "v", "v", "u", "u")
periods = []
for positions in combinations(range(7), 3):
    unit = set(positions)
    periods.append(tuple("u" if i in unit else "v" for i in range(7)))
assert len(periods) == len(set(periods)) == 35
periods.sort(key=lambda p: (p != displayed, p))
# No antipodal symmetry is imposed silently: exhaust all 3003 binary masks.
closed_masks = []
for positions in combinations(range(14), 8):
    if sum((z**(2*i) for i in positions), K(0)) == 0:
        closed_masks.append(positions)
assert len(closed_masks) == 35
expected_masks = {tuple(i for i, tag in enumerate(list(period)*2) if tag == "v") for period in periods}
assert set(closed_masks) == expected_masks
rows = [audit_word(period) for period in periods]
assert sum(bool(r["complete_native_cycles"]) for r in rows) == 14
assert sum(len(r["disjoint_native_cycles"]) for r in rows) == 896
assert all(r["complete_native_cycles"] == r["disjoint_native_cycles"] for r in rows)
assert sum(len(r["forced_dimer_completed_patches"]) for r in rows) == 364
assert sum(len(r["forced_dimer_rejections"]) for r in rows) == 532
assert all(len(r["forced_dimer_completed_patches"])+len(r["forced_dimer_rejections"]) == len(r["disjoint_native_cycles"]) for r in rows)
data = dict(schema="arisearch-p5-q14-native-ring-v1", status="complete bounded enumeration",
            software=dict(sage=SAGE_VERSION, python=python_version()),
            scope="one exact P metric; all 35 opposite-seven binary Q periods with 6u/8v; no inference of plane existence from a surviving ring",
            field=dict(polynomial=str(field_polynomial), root="z=exp(i*pi/14); zeta28",
                       representation="12 rational coefficients in ascending powers of z"),
            source=dict(s=encode(s), y=encode(y), v=encode(v),
                        P_direction_exponents=directions, P_lengths=[encode(q) for q in lengths],
                        P_vertices=[encode(q) for q in P]),
            deductions=dict(angle_stars_alpha_beta_gamma=angle_stars,
                            eligible_PPP_beta_indices=eligible_beta,
                            forced_alpha_alpha_side=4, forced_v_Q_side=3,
                            forbidden_w_Q_side=2, Q_unit_contact_side=1,
                            bulk_p_per_q=8, Q_native_unit_count=6, Q_native_v_count=8),
            displayed_period="".join(displayed), rows=rows,
            full_binary_closure_audit=dict(domain_masks=3003, v_count=8, u_count=6,
                                           closed_masks=closed_masks, closed_count=35),
            summary=dict(words=35, words_with_native_cycles=sum(bool(r["complete_native_cycles"]) for r in rows),
                         words_with_disjoint_cycles=sum(bool(r["disjoint_native_cycles"]) for r in rows),
                         total_disjoint_cycles=sum(len(r["disjoint_native_cycles"]) for r in rows),
                         total_forced_dimer_completed_cycles=sum(len(r["forced_dimer_completed_patches"]) for r in rows),
                         total_forced_dimer_rejected_cycles=sum(len(r["forced_dimer_rejections"]) for r in rows),
                         words_with_forced_dimer_patch=sum(bool(r["forced_dimer_completed_patches"]) for r in rows)))

parser = argparse.ArgumentParser()
parser.add_argument("certificate", nargs="?", type=Path)
args = parser.parse_args()
serialized = json.dumps(data, indent=2, sort_keys=True)+"\n"
if args.certificate:
    args.certificate.write_text(serialized)
    print(json.dumps(data["summary"], sort_keys=True))
    print("displayed:", rows[0]["period"], "native cycles", len(rows[0]["complete_native_cycles"]),
          "disjoint cycles", len(rows[0]["disjoint_native_cycles"]),
          "forced-dimer completions", len(rows[0]["forced_dimer_completed_patches"]))
else:
    print(serialized, end="")
