#!/usr/bin/env python3
"""Independent geometric replay of Theorem 1(a),(c) of
research/lemmas/two-hexagon-global-sft-encoding.md on every torus record of
research/certificates/two-hexagon-global-partition-strata.json.

No authors' code is imported; conventions are re-implemented from the lemma.
For each record and several random realisations (angles: random interior
point of the class's angle flat; side lengths: random positive solution of the
two hexagon-closure equations with the identifications E(x) imposed), the
torus labelling is unfolded on a large patch of Z^2 and the tiles are placed by
gluing side-slot k of z to side-slot k+3 of z+D_{k+1} (slot k -> slot k+4,
slot k+1 -> slot k+3).  Checked numerically:
  * every glued pair of tiles shares both endpoints (vertex closure);
  * translating by either lattice period is one and the same plane translation
    for all cells (actual periodic tiling, orientation-preserving period);
  * random sample points in a central disk lie in the interior of exactly one tile.
Usage: python verify_two_hexagon_global_develop.py [realisations_per_record]
"""
import sys, json, math, random, itertools
import numpy as np
from scipy.optimize import linprog

CERT = "research/certificates/two-hexagon-global-partition-strata.json"
D = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
SYMS = [(i // 12, i % 6, 1 if (i % 12) < 6 else -1) for i in range(24)]
TRIPLES = list(itertools.combinations_with_replacement(range(12), 3))


def corner(i, k):
    q, r, s = SYMS[i]
    return 6 * q + (r + s * k) % 6


def side(i, k):
    q, r, s = SYMS[i]
    return 6 * q + ((r + k) % 6 if s == 1 else (r - k - 1) % 6)


def tvec(t):
    v = [0] * 12
    for c in t:
        v[c] += 1
    return v


def random_angles(T, rng):
    A_eq = [[1] * 6 + [0] * 6, [0] * 6 + [1] * 6] + [tvec(t) for t in T]
    b_eq = [720, 720] + [360] * len(T)
    # maximise slack with a random tilt to get different interior points
    c = [rng.uniform(-0.05, 0.05) for _ in range(12)] + [-1]
    A_ub = [[(-1 if j == i else 0) for j in range(12)] + [1] for i in range(12)] + \
           [[(1 if j == i else 0) for j in range(12)] + [1] for i in range(12)]
    r = linprog(c, A_eq=[a + [0] for a in A_eq], b_eq=b_eq, A_ub=A_ub, b_ub=[0] * 12 + [180] * 12,
                bounds=[(None, None)] * 12 + [(0, 60)])
    assert r.success and r.x[-1] > 1e-6
    return list(r.x[:12])


def directions(alpha):
    """alpha: 6 interior angles (deg) of a ccw hexagon; side i from corner i to i+1."""
    th = [0.0]
    for i in range(1, 6):
        th.append(th[-1] + (180 - alpha[i]))
    return [(math.cos(math.radians(t)), math.sin(math.radians(t))) for t in th]


def random_lengths(angles, E, rng):
    U = directions(angles[:6]) + directions(angles[6:])
    A_eq, b_eq = [], []
    for q in range(2):
        for comp in range(2):
            A_eq.append([U[6 * q + i][comp] if j == 6 * q + i else 0 for j in range(12) for i in [j % 6]] + [0])
            b_eq.append(0)
    for a, b in E:
        row = [0] * 13; row[a] = 1; row[b] = -1; A_eq.append(row); b_eq.append(0)
    A_eq.append([1] * 12 + [0]); b_eq.append(12)
    A_ub = [[(-1 if j == i else 0) for j in range(12)] + [1] for i in range(12)]
    # stage 1: maximal common slack t*; stage 2: random direction with t >= t*/2
    r = linprog([0] * 12 + [-1], A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=[0] * 12, bounds=[(None, None)] * 12 + [(0, 1)])
    if not r.success or r.x[-1] < 1e-6:
        return None
    tstar = r.x[-1]
    c = [rng.uniform(-1, 1) for _ in range(12)] + [0]
    r2 = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=[0] * 12, bounds=[(None, None)] * 12 + [(tstar / 2, 1)])
    x = r2.x[:12] if r2.success else r.x[:12]
    lam = rng.uniform(0.2, 0.8)          # strictly interior mix of the two LP points
    return list(lam * x + (1 - lam) * r.x[:12])


def prototiles(angles, lengths):
    P = []
    for q in range(2):
        U = directions(angles[6 * q:6 * q + 6])
        V = [(0.0, 0.0)]
        for i in range(5):
            V.append((V[-1][0] + lengths[6 * q + i] * U[i][0], V[-1][1] + lengths[6 * q + i] * U[i][1]))
        last = (V[-1][0] + lengths[6 * q + 5] * U[5][0], V[-1][1] + lengths[6 * q + 5] * U[5][1])
        assert math.hypot(*last) < 1e-8, "hexagon does not close"
        P.append(V)
    return P


def local_slots(P, i):
    q, r, s = SYMS[i]
    pts = []
    for k in range(6):
        c = (r + s * k) % 6
        x, y = P[q][c]
        pts.append((x, y) if s == 1 else (-x, y))
    area = sum(pts[k][0] * pts[(k + 1) % 6][1] - pts[(k + 1) % 6][0] * pts[k][1] for k in range(6))
    assert area > 0, "slots not counter-clockwise"
    return pts


def iso_from(p0, p1, g0, g1):
    """direct isometry mapping p0->g0, p1->g1 (as rotation angle + translation)."""
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0]); b = math.atan2(g1[1] - g0[1], g1[0] - g0[0])
    assert abs(math.hypot(p1[0] - p0[0], p1[1] - p0[1]) - math.hypot(g1[0] - g0[0], g1[1] - g0[1])) < 1e-8, "length mismatch"
    ph = b - a; c, s = math.cos(ph), math.sin(ph)
    tx = g0[0] - (c * p0[0] - s * p0[1]); ty = g0[1] - (s * p0[0] + c * p0[1])
    return (ph, tx, ty)


def apply(M, p):
    ph, tx, ty = M; c, s = math.cos(ph), math.sin(ph)
    return (c * p[0] - s * p[1] + tx, s * p[0] + c * p[1] + ty)


def develop(lab, lat, P, Rd=9):
    n, s, m = lat

    def red(z):
        x, y = z
        q = y // m
        return ((x - s * q) % n, y - m * q)
    cells = [(x, y) for x in range(-Rd, Rd + 1) for y in range(-Rd, Rd + 1) if max(abs(x), abs(y), abs(x + y)) <= Rd]
    cs = set(cells)
    L = {z: local_slots(P, lab[red(z)]) for z in cells}
    M = {(0, 0): (0.0, 0.0, 0.0)}
    queue = [(0, 0)]
    while queue:
        z = queue.pop(0)
        for k in range(6):
            w = (z[0] + D[(k + 1) % 6][0], z[1] + D[(k + 1) % 6][1])
            if w in cs and w not in M:
                g0 = apply(M[z], L[z][k]); g1 = apply(M[z], L[z][(k + 1) % 6])
                M[w] = iso_from(L[w][(k + 4) % 6], L[w][(k + 3) % 6], g0, g1)
                queue.append(w)
    G = {z: [apply(M[z], p) for p in L[z]] for z in cells}
    err = 0.0
    for z in cells:
        for k in range(6):
            w = (z[0] + D[(k + 1) % 6][0], z[1] + D[(k + 1) % 6][1])
            if w in cs:
                for a, b in ((k, (k + 4) % 6), ((k + 1) % 6, (k + 3) % 6)):
                    err = max(err, math.dist(G[z][a], G[w][b]))
    perr = 0.0
    for p in ((n, 0), (s, m)):
        tr = None
        for z in cells:
            w = (z[0] + p[0], z[1] + p[1])
            if w in cs:
                d = [(G[w][k][0] - G[z][k][0], G[w][k][1] - G[z][k][1]) for k in range(6)]
                if tr is None:
                    tr = d[0]
                perr = max(perr, max(math.dist(x, tr) for x in d))
        assert tr is not None and math.hypot(*tr) > 1e-6
    # overlap / coverage sampling in a disk around the origin tile
    rng = random.Random(7)
    cx = sum(p[0] for p in G[(0, 0)]) / 6; cy = sum(p[1] for p in G[(0, 0)]) / 6
    rad = 0.35 * min(math.hypot(G[z][0][0] - cx, G[z][0][1] - cy) for z in cells
                     if max(abs(z[0]), abs(z[1]), abs(z[0] + z[1])) == Rd)
    bad = 0; used = 0
    for _ in range(3000):
        px, py = cx + rng.uniform(-rad, rad), cy + rng.uniform(-rad, rad)
        if math.hypot(px - cx, py - cy) > rad:
            continue
        cnt = 0; near = False
        for z in cells:
            Q = G[z]; inside = True
            for k in range(6):
                (x1, y1), (x2, y2) = Q[k], Q[(k + 1) % 6]
                cr = ((x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)) / math.hypot(x2 - x1, y2 - y1)
                if abs(cr) < 1e-7:
                    near = True
                if cr <= 0:
                    inside = False
            cnt += inside
        if near:
            continue
        used += 1
        bad += cnt != 1
    return err, perr, bad, used


def main():
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    cert = json.load(open(CERT))
    rng = random.Random(2026)
    worst = [0, 0]; nbad = 0; nrun = 0; nolen = 0; nsamp = 0
    for st in cert["strata"]:
        T = [tuple(t) for t in st["T"]]
        for t in st["tori"]:
            lab = {tuple(map(int, k.split(","))): v for k, v in t["sol"].items()}
            lat = tuple(t["lat"])
            E = [tuple(p) for p in t["E"]]
            for rep in range(reps):
                ang = random_angles(T, rng)
                ln = random_lengths(ang, E, rng)
                if ln is None:
                    nolen += 1; continue
                P = prototiles(ang, ln)
                err, perr, bad, used = develop(lab, lat, P)
                nrun += 1; nsamp += used
                worst[0] = max(worst[0], err); worst[1] = max(worst[1], perr)
                if err > 1e-6 or perr > 1e-6 or bad:
                    nbad += 1
                    print("FAIL class", st["index"], lat, err, perr, bad, flush=True)
    print("developments", nrun, "failures", nbad, "no positive lengths", nolen,
          "max gluing error %.2e  max period error %.2e  sample points %d" % (worst[0], worst[1], nsamp))


if __name__ == "__main__":
    main()
