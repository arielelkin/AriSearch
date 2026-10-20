"""Independent exact P5/Q9 reconstruction and first periodicity attacks.

Run: mise exec -- conda run --no-capture-output -n arisearch python research/searches/q9-periodic-attack-2026-10-20.py
"""
from sage.all import AA, cos, sin, pi
from itertools import product
from math import atan2, degrees


def u(d):
    return (AA(cos(pi * d / 180)), AA(sin(pi * d / 180)))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(k, a):
    return (k * a[0], k * a[1])


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cprod(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def div(a, b):
    return mul(1 / dot(b, b), cprod(a, conj(b)))


def polygon(dirs, lengths):
    v = [(AA(0), AA(0))]
    for d, length in zip(dirs, lengths):
        v.append(add(v[-1], mul(length, u(d))))
    assert v[-1] == v[0]
    v.pop()
    assert all(cross(sub(v[(i + 1) % len(v)], v[i]), sub(v[(i + 2) % len(v)], v[(i + 1) % len(v)])) > 0 for i in range(len(v)))
    return tuple(v)


def place(poly, side, target, reverse=False, mirror=False):
    """Map given side endpoints onto target endpoints, optionally reversed."""
    a, b = poly[side], poly[(side + 1) % len(poly)]
    A, B = target
    if reverse:
        A, B = B, A
    w, W = sub(b, a), sub(B, A)
    if mirror:
        factor = div(W, conj(w))
        f = lambda z: add(A, cprod(factor, conj(sub(z, a))))
    else:
        factor = div(W, w)
        f = lambda z: add(A, cprod(factor, sub(z, a)))
    assert dot(factor, factor) == 1
    return tuple(f(z) for z in poly)


def overlap(p, q):
    """Strict positive-area overlap by separating axes for convex polygons."""
    for poly in (p, q):
        for a, b in zip(poly, poly[1:] + poly[:1]):
            axis = (a[1] - b[1], b[0] - a[0])
            pvals, qvals = [dot(axis, z) for z in p], [dot(axis, z) for z in q]
            if max(pvals) <= min(qvals) or max(qvals) <= min(pvals):
                return False
    return True


def overlap_margin(p, q):
    gaps = []
    for poly in (p, q):
        for a, b in zip(poly, poly[1:] + poly[:1]):
            axis = (a[1] - b[1], b[0] - a[0])
            pvals, qvals = [dot(axis, z) for z in p], [dot(axis, z) for z in q]
            gaps.append(min(max(pvals) - min(qvals), max(qvals) - min(pvals)))
    return min(gaps)


M = add(u(144), u(276))
N = add(u(72), u(216))
det = cross(M, N)
b = cross(mul(-1, u(0)), N) / det
c = cross(M, mul(-1, u(0))) / det
assert b > 0 and c > 0
P = polygon((0, 72, 144, 216, 276), (1, c, b, c, b))
Q = polygon((0, 36, 96, 120, 156, 216, 240, 276, 336), (1, b, c, 1, b, c, 1, b, c))

print("b,c", b.n(35), c.n(35))
print("P vertices", [(float(x), float(y)) for x, y in P])
print("Q vertices", [(float(x), float(y)) for x, y in Q])

hub = []
for choices in product((False, True), repeat=3):
    arms = []
    for i, mir in zip((0, 3, 6), choices):
        target = (Q[i], Q[(i + 1) % 9])
        arm = place(P, 0, target, reverse=not mir, mirror=mir)
        arms.append(arm)
    bad = any(overlap(Q, arm) for arm in arms) or any(overlap(arms[i], arms[j]) for i in range(3) for j in range(i + 1, 3))
    if not bad:
        hub.append((choices, arms))
    print("hub", choices, "overlap" if bad else "disjoint")
print("hub_count", len(hub))
assert len(hub) == 8

# Restrict the hub to the endpoint-compatible reflected unit seam.  At each
# Q-unit endpoint the residual is 108 degrees, hence a P108 corner.
core = (Q,) + tuple(next(arms for choice, arms in hub if choice == (True, True, True)))


def same(poly, other):
    return frozenset(poly) == frozenset(other)


def candidates_on(edge, species="P"):
    src = P if species == "P" else Q
    length2 = dot(sub(edge[1], edge[0]), sub(edge[1], edge[0]))
    for j in range(len(src)):
        if dot(sub(src[(j + 1) % len(src)], src[j]), sub(src[(j + 1) % len(src)], src[j])) != length2:
            continue
        for mirror, reverse in product((False, True), repeat=2):
            tile = place(src, j, edge, reverse=reverse, mirror=mirror)
            if any(overlap(tile, existing) for existing in core):
                continue
            if any(same(tile, existing) for existing in core):
                continue
            yield (species, j, mirror, reverse, tile)


endpoint_options = []
for k, qside in enumerate((0, 3, 6)):
    arm = core[k + 1]
    for endpoint, target_side, arm_vertex in ((qside, (qside - 1) % 9, 0), ((qside + 1) % 9, (qside + 1) % 9, 1)):
        v = Q[endpoint]
        qedge = (Q[target_side], Q[(target_side + 1) % 9])
        armother = arm[4 if arm_vertex == 0 else 2]
        armedge = frozenset((v, armother))
        opts = []
        for info in candidates_on(qedge):
            tile = info[-1]
            for vi in (1, 2, 3):  # exactly P108 vertices
                if tile[vi] == v and any(frozenset((tile[j], tile[(j + 1) % 5])) == armedge for j in range(5)):
                    opts.append(info[:-1] + (vi,))
        print("endpoint", k, endpoint, "Qside", target_side, "P108 candidates", len(opts), opts)
        endpoint_options.append([info[-1] for info in candidates_on(qedge) if any(info[-1][vi] == v and any(frozenset((info[-1][j], info[-1][(j + 1) % 5])) == armedge for j in range(5)) for vi in (1, 2, 3))])

assert len(endpoint_options) == 6 and all(len(opts) == 2 for opts in endpoint_options)

survivors = []
for labels in product((0, 1), repeat=6):
    tiles = [endpoint_options[i][labels[i]] for i in range(6)]
    if all(same(tiles[i], tiles[j]) or not overlap(tiles[i], tiles[j]) for i in range(6) for j in range(i + 1, 6)):
        unique = []
        for tile in tiles:
            if not any(same(tile, old) for old in unique):
                unique.append(tile)
        survivors.append((labels, len(unique)))
print("simultaneous endpoint completions", len(survivors))
assert len(survivors) == 64
for e, opts in enumerate(endpoint_options):
    for choice, tile in enumerate(opts):
        matches = []
        for k, arm in enumerate(core[1:]):
            delta = sub(tile[0], arm[0])
            if all(sub(tile[j], arm[j]) == delta for j in range(5)):
                matches.append((k, float(delta[0]), float(delta[1])))
        print("cap", e, choice, "translation_matches", matches)
print("unit_edge_directions")
for k, arm in enumerate(core[1:]):
    d = sub(arm[1], arm[0])
    print("arm", k, round(degrees(atan2(float(d[1]), float(d[0]))) % 360, 9))
for e, opts in enumerate(endpoint_options[:2]):
    for choice, tile in enumerate(opts):
        d = sub(tile[1], tile[0])
        print("cap", e, choice, round(degrees(atan2(float(d[1]), float(d[0]))) % 360, 9))


def q_owner(cap):
    edge = (cap[0], cap[1])
    opts = []
    for j in (0, 3, 6):
        for mir in (False, True):
            tile = place(Q, j, edge, reverse=False, mirror=mir)
            if not any(overlap(tile, other) for other in core + (cap,)):
                if not any(same(tile, old) for old in opts):
                    opts.append(tile)
    return opts


def forced_owner(cap):
    # The two unit edges have the same directed endpoint order; opposite
    # interiors require the Q chirality opposite the P chirality.
    cap_ccw = cross(sub(cap[1], cap[0]), sub(cap[2], cap[1])) > 0
    return place(Q, 0, (cap[0], cap[1]), reverse=False, mirror=cap_ccw)


owners = []
for e, opts in enumerate(endpoint_options):
    row = []
    for choice, cap in enumerate(opts):
        qopts = q_owner(cap)
        print("owner", e, choice, "count", len(qopts), "origins", [(round(float(q[0][0]), 9), round(float(q[0][1]), 9)) for q in qopts])
        row.append(qopts)
    owners.append(row)

assert [[len(row) for row in e] for e in owners] == [[0,1],[1,1]] * 3

for e in range(6):
    for c in range(2):
        if len(owners[e][c]) != 1:
            continue
        q = owners[e][c][0]
        shared = [(f, d) for f in range(e + 1, 6) for d in range(2) if len(owners[f][d]) == 1 and same(q, owners[f][d][0])]
        if shared:
            print("shared Q owner", (e, c), shared)

for odd in product((0, 1), repeat=3):
    labels = (1, odd[0], 1, odd[1], 1, odd[2])
    selected = [endpoint_options[i][labels[i]] for i in range(6)] + [owners[i][labels[i]][0] for i in range(6)]
    conflicts = [(i, j) for i in range(12) for j in range(i + 1, 12) if overlap(selected[i], selected[j])]
    print("six_owner_choice", labels, "conflicts", conflicts)
    assert conflicts

print("minimal_sector_certificate")
for choice in (0, 1):
    print("Q3_cap_choice", choice, "owner_vs_core", [(j, float(overlap_margin(forced_owner(endpoint_options[2][choice]), tile))) for j, tile in enumerate(core) if overlap(forced_owner(endpoint_options[2][choice]), tile)])
assert overlap(forced_owner(endpoint_options[2][0]), core[0])
assert overlap(forced_owner(endpoint_options[2][0]), core[1])
assert all(not overlap(forced_owner(endpoint_options[2][1]), tile) for tile in core)
for choice in (0, 1):
    print("Q1_cap_choice", choice, "against_forced_Q3_owner_margin", float(overlap_margin(endpoint_options[1][choice], forced_owner(endpoint_options[2][1]))))
    assert overlap_margin(endpoint_options[1][choice], forced_owner(endpoint_options[2][1])) > 0
