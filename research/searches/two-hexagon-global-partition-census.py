#!/usr/bin/env python3
"""Census of the generic tileable angle strata ("partition strata").

A partition stratum is given by a partition Pi of the twelve corners
A0..A5,B0..B5 into four 3-element blocks.  Its angle flat is
   sum(A)=sum(B)=720,  sum(block)=360 for each block.
T(Pi) = all corner multisets of size 3 whose angle sum is 360 on the whole
flat (computed exactly by rational linear algebra).  A pair is in the stratum
when its exact set of 360-triples is T(Pi).

This script enumerates partitions up to the symmetry group
(D6 on A corners) x (D6 on B corners) x (swap A,B), and for each computes
the angle-only SFT with ALL side lengths declared equal (the coarsest length
structure; every real length structure gives a sub-SFT).
"""
import sys, os, json, itertools, importlib.util
from fractions import Fraction as Fr
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
S_ = _load("thg_sft", "two-hexagon-global-sft.py")

CORNERS = list(range(12))  # 0..5 = A0..A5, 6..11 = B0..B5


def d6_maps():
    maps = []
    for r in range(6):
        for s in (1, -1):
            maps.append(tuple((r + s * i) % 6 for i in range(6)))
    return maps


def group():
    G = []
    for ma in d6_maps():
        for mb in d6_maps():
            g = [ma[i] for i in range(6)] + [6 + mb[i] for i in range(6)]
            G.append(tuple(g))
            G.append(tuple([6 + ma[i] for i in range(6)] + [mb[i] for i in range(6)]))
    return G


def canon(blocks, G):
    best = None
    for g in G:
        nb = tuple(sorted(tuple(sorted(g[c] for c in b)) for b in blocks))
        if best is None or nb < best:
            best = nb
    return best


def partitions12():
    def rec(rem):
        if not rem:
            yield []
            return
        f = rem[0]
        for a, b in itertools.combinations(rem[1:], 2):
            r = [x for x in rem if x not in (f, a, b)]
            for rest in rec(r):
                yield [(f, a, b)] + rest
    yield from rec(list(range(12)))


def flat_matrix(blocks):
    rows, rhs = [], []
    rows.append([1] * 6 + [0] * 6); rhs.append(720)
    rows.append([0] * 6 + [1] * 6); rhs.append(720)
    for b in blocks:
        r = [0] * 12
        for c in b: r[c] += 1
        rows.append(r); rhs.append(360)
    return sp.Matrix(rows), sp.Matrix(rhs)


ALLTRIPLES = list(itertools.combinations_with_replacement(range(12), 3))


def implied_triples(blocks):
    A, b = flat_matrix(blocks)
    Ab = A.row_join(b)
    rk = Ab.rank()
    out = []
    for t in ALLTRIPLES:
        r = [0] * 12
        for c in t: r[c] += 1
        if Ab.col_join(sp.Matrix([r + [360]])).rank() == rk:
            out.append(t)
    return out


def generic_angles(blocks, seed=0):
    """an exact rational point of the flat, in (0,180), whose 360-triples are
    exactly the implied ones (verified)."""
    import random
    rnd = random.Random(seed)
    A, b = flat_matrix(blocks)
    sol, params = A.gauss_jordan_solve(b)
    free = list(params)
    imp = set(implied_triples(blocks))
    for trial in range(2000):
        vals = {p: sp.Rational(rnd.randint(-900, 900), 97) for p in free}
        ang = [sol[i].subs(vals) for i in range(12)]
        # move toward 120 to keep inside the box: convex combination
        lam = sp.Rational(rnd.randint(1, 20), 41)
        ang = [120 + lam * (a - 120) for a in ang]
        if not all(0 < a < 180 for a in ang):
            continue
        ok = all(((sum(ang[c] for c in t) == 360) == (t in imp)) for t in ALLTRIPLES)
        if ok:
            return [Fr(int(sp.fraction(a)[0]), int(sp.fraction(a)[1])) for a in ang]
    return None


def main():
    G = group()
    seen = {}
    for p in partitions12():
        c = canon(p, G)
        seen.setdefault(c, p)
    print("partition classes:", len(seen), flush=True)
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    out = []
    for idx, c in enumerate(sorted(seen)):
        imp = implied_triples(c)
        ang = generic_angles(c, seed=idx)
        rec = {"partition": [list(b) for b in c], "implied": [list(t) for t in imp],
               "angles": None if ang is None else [str(a) for a in ang]}
        if ang is None:
            rec["status"] = "no-generic-point-found"
            out.append(rec); print(json.dumps(rec), flush=True); continue
        sft = S_.SFT([ang[:6], ang[6:]], [[0] * 6, [0] * 6])
        st, _ = sft.patch(R, time=60)
        rec["patch"] = st
        if st == "SAT":
            rec["monoA"] = sft.patch(R, time=60, only={0})[0]
            rec["monoB"] = sft.patch(R, time=60, only={1})[0]
            lat, sol = sft.tori(N, time=60)
            rec["torus"] = None if lat is None else list(lat) if lat[0] != "UNKNOWN" else str(lat)
            if lat is not None and lat[0] != "UNKNOWN":
                assert S_.check_torus(sft, lat, sol)
                rec["torus_types"] = sorted({sft.syms[v][0] for v in sol.values()})
        out.append(rec)
        print(json.dumps({k: rec[k] for k in rec if k != "implied"}), flush=True)
    if len(sys.argv) > 3:
        json.dump(out, open(sys.argv[3], "w"), indent=0)


if __name__ == "__main__":
    main()
