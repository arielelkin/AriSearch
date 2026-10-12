#!/usr/bin/env python3
"""Independent re-verification of the final UNSAT claims of the fixed-angle
census from a certificate file only (no import of the census code).

For each angle type T in the certificate, with escape records E_k (the full
glued side-pair sets of the recorded tori; torus x_k is legal in X(T,e) iff
E_k <= e), the claim is:

  there is NO equivalence relation e on the 12 sides and NO legal radius-R
  patch of X(T,e) such that, for every k and every relabelling g of the
  12+12 corners/sides preserving T, g(E_k) is not contained in e.

Re-encoded differently from the census: one-hot symbol booleans, explicit
clauses for side identifications, table constraints for angle triples, and a
separately recomputed symmetry stabiliser.  Solved with CP-SAT
(single worker, fixed seed).  Usage:
  python two-hexagon-global-strata-verify.py CERT.json R [first last]
"""
import sys, json, itertools
from ortools.sat.python import cp_model

DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
SYM = [(q, r, s) for q in range(2) for s in (1, -1) for r in range(6)]


def corner(sym, k):
    q, r, s = sym
    return 6 * q + (r + s * k) % 6


def side(sym, k):
    q, r, s = sym
    return 6 * q + ((r + k) % 6 if s == 1 else (r - k - 1) % 6)


def relabellings():
    out = []
    d6 = [(r, s) for r in range(6) for s in (1, -1)]
    for (ra, sa), (rb, sb), sw in itertools.product(d6, d6, (0, 1)):
        cm, sm = [0] * 12, [0] * 12
        for q, (r, s) in ((0, (ra, sa)), (1, (rb, sb))):
            qq = q ^ sw
            for i in range(6):
                cm[6 * q + i] = 6 * qq + (r + s * i) % 6
                # side i = {corner i, corner i+1}
                a, b = (r + s * i) % 6, (r + s * (i + 1)) % 6
                j = a if (a + 1) % 6 == b else b
                sm[6 * q + i] = 6 * qq + j
        out.append((cm, sm))
    return out


def verify(T, Fs, R):
    T = set(tuple(sorted(t)) for t in T)
    G = [g for g in relabellings() if set(tuple(sorted(g[0][c] for c in t)) for t in T) == T]
    m = cp_model.CpModel()
    pairs = [(i, j) for i in range(12) for j in range(i + 1, 12)]
    e = {p: m.NewBoolVar("") for p in pairs}
    def E(i, j):
        return None if i == j else e[(min(i, j), max(i, j))]
    for i, j, k in itertools.permutations(range(12), 3):
        m.AddBoolOr([E(i, j).Not(), E(j, k).Not(), E(i, k)])
    cells = [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1) if max(abs(x), abs(y), abs(x + y)) <= R]
    cs = set(cells)
    oh = {z: [m.NewBoolVar("") for _ in SYM] for z in cells}
    xv = {}
    for z in cells:
        m.AddExactlyOne(oh[z])
        xv[z] = m.NewIntVar(0, 23, "")
        for i in range(24):
            m.Add(xv[z] == i).OnlyEnforceIf(oh[z][i])
    for z in cells:
        for k in (0, 1):
            b = (z[0] + DIRS[k][0], z[1] + DIRS[k][1]); c = (z[0] + DIRS[k + 1][0], z[1] + DIRS[k + 1][1])
            if b in cs and c in cs:
                tab = [(i, j, l) for i in range(24) for j in range(24) for l in range(24)
                       if tuple(sorted((corner(SYM[i], k), corner(SYM[j], k + 2), corner(SYM[l], (k + 4) % 6)))) in T]
                m.AddAllowedAssignments([xv[z], xv[b], xv[c]], tab)
        for k in range(6):
            w = (z[0] + DIRS[(k + 1) % 6][0], z[1] + DIRS[(k + 1) % 6][1])
            if w in cs and z < w:
                for i in range(24):
                    for j in range(24):
                        p, q = side(SYM[i], k), side(SYM[j], (k + 3) % 6)
                        if p != q:
                            m.AddBoolOr([oh[z][i].Not(), oh[w][j].Not(), E(p, q)])
    seen = set()
    for F in Fs:
        for g in G:
            key = tuple(sorted((min(g[1][a], g[1][b]), max(g[1][a], g[1][b])) for a, b in F))
            if key in seen:
                continue
            seen.add(key)
            m.AddBoolOr([e[p].Not() for p in key])
    s = cp_model.CpSolver()
    s.parameters.num_workers = 1
    s.parameters.random_seed = 12345
    s.parameters.max_time_in_seconds = 1800
    st = s.Solve(m)
    return s.StatusName(st), len(G)


def main():
    C = json.load(open(sys.argv[1])); R = int(sys.argv[2])
    items = C.get("strata", []) + C.get("flats", [])
    a, b = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, len(items))
    bad = 0
    for it in items[a:b]:
        st, ng = verify(it["T"], [r["E"] for r in it["tori"]], R)
        print(it["index"], st, "stab", ng, "records", len(it["tori"]), flush=True)
        bad += st != "INFEASIBLE"
    print("non-INFEASIBLE:", bad)


if __name__ == "__main__":
    main()
