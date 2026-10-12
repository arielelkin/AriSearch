#!/usr/bin/env python3
"""Library of escape records from ALL labellings of small tori.

For every period lattice of index <= N and every labelling x of Z^2/Lambda by
the 24 abstract symbols, x is a legal torus of X(T,~) for every exact type with
U(x) <= T and E(x) <= ~ (U = corner triples at its vertices, E = glued side
pairs).  Hence the clause  not(U(x) <= t and E(x) <= e)  is sound for the
census of two-hexagon-global-cegar.py (no feasibility needed: if U(x) is
angle-infeasible the clause is vacuous on realisable types).
Records are reduced to canonical representatives under the 288 relabellings
and to inclusion-minimal pairs (U,E).
Output: JSON list of [U, E, lattice, labelling].
"""
import sys, os, json, itertools, importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cg", os.path.join(_here, "two-hexagon-global-cegar.py"))
cg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cg)


def lattices(N):
    for idx in range(1, N + 1):
        for n in range(1, idx + 1):
            if idx % n:
                continue
            mm = idx // n
            for s in range(n):
                yield (n, s, mm)


def canon(U, E):
    best = None
    for g in cg.GROUP:
        k = (tuple(sorted(cg.img_triple(g, t) for t in U)), tuple(sorted(cg.img_pair(g, p) for p in E)))
        if best is None or k < best:
            best = k
    return best


def main():
    N = int(sys.argv[1]); out = sys.argv[2]
    raw = {}
    for lat in lattices(N):
        n, s, mm = lat
        cells = [(x, y) for x in range(n) for y in range(mm)]
        for lab in itertools.product(range(cg.NS), repeat=len(cells)):
            sol = dict(zip(cells, lab))
            U, E = cg.usage(sol, lat)
            key = (tuple(U), tuple(E))
            if key not in raw:
                raw[key] = (lat, lab)
        print("lattice", lat, "distinct raw", len(raw), flush=True)
    # canonical
    can = {}
    for (U, E), w in raw.items():
        c = canon(U, E)
        if c not in can:
            can[c] = (U, E, w)
    print("canonical", len(can), flush=True)
    # inclusion-minimal (within canonical reps and their images is expensive;
    # do minimality among canonical reps only, which is still sound)
    keys = sorted(can, key=lambda k: (len(k[0]) + len(k[1])))
    kept = []
    for k in keys:
        U, E = set(k[0]), set(k[1])
        if any(set(a) <= U and set(b) <= E for a, b in kept):
            continue
        kept.append(k)
    print("minimal", len(kept), flush=True)
    # output the witness's own (U,E) (a symmetry image of the canonical key)
    json.dump([[list(map(list, can[k][0])), list(map(list, can[k][1])), list(can[k][2][0]), list(can[k][2][1])] for k in kept],
              open(out, "w"))


if __name__ == "__main__":
    main()
