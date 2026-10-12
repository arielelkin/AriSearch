#!/usr/bin/env python3
"""Exact pi/5 convex pentagon/hexagon shapes with Z[phi] sides, and the cheap
monohedral filters (Rao Table 2 for pentagons, Reinhardt types for hexagons).

Rao table copied verbatim from research/searches/pentagrid_monohedral_family_filter.py
(reviewed in research/reviews/pentagrid-monohedral-filter-review.md): vertex
angle m_i at vertex i, side i joins vertices i,i+1, target 10 = 2pi.
"""
import importlib.util
from itertools import product
from pathlib import Path

_spec = importlib.util.spec_from_file_location("cs_core", Path(__file__).with_name("convex-substitution-core.py"))
core = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(core)

def _eq(row, target=10): return tuple(row), target
def _L(*rows): return tuple(tuple(r) for r in rows)
RAO = {
1:([_eq((1,1,1,0,0))],_L()),
2:([_eq((1,1,0,1,0))],_L((0,0,1,0,-1))),
3:([_eq((0,0,0,0,3)),_eq((0,0,0,1,2)),_eq((0,1,0,0,2))],_L((0,0,1,-1,1),(1,-1,0,0,0))),
4:([_eq((1,1,0,1,0)),_eq((0,0,0,0,2),5)],_L((0,0,0,1,-1),(0,1,-1,0,0))),
5:([_eq((0,0,0,0,3)),_eq((1,1,0,1,0))],_L((0,0,0,1,-1),(0,1,-1,0,0))),
6:([_eq((0,0,0,1,2)),_eq((1,0,1,1,0))],_L((0,0,1,-1,0),(0,0,0,1,-1),(1,-1,0,0,0))),
7:([_eq((0,0,0,1,2)),_eq((1,0,2,0,0))],_L((1,0,-1,0,0),(0,0,1,-1,0),(0,0,0,1,-1))),
8:([_eq((0,0,0,1,2)),_eq((0,2,1,0,0))],_L((1,-1,0,0,0),(0,1,-1,0,0),(0,0,1,-1,0))),
9:([_eq((0,0,0,1,2)),_eq((2,0,1,0,0))],_L((1,-1,0,0,0),(0,1,-1,0,0),(0,0,1,-1,0))),
10:([_eq((0,0,2,1,0)),_eq((0,1,1,0,1)),_eq((1,2,0,0,0))],_L((1,0,1,-1,0),(0,0,0,1,-1))),
11:([_eq((0,0,1,2,0)),_eq((0,1,0,1,1)),_eq((1,2,0,0,0))],_L((1,-1,0,0,0),(0,1,-1,0,-2))),
12:([_eq((0,0,1,2,0)),_eq((0,1,0,1,1)),_eq((1,2,0,0,0))],_L((1,-1,1,0,0),(0,1,0,0,-2))),
13:([_eq((0,1,0,2,0)),_eq((1,1,0,1,0)),_eq((0,0,0,0,2),5)],_L((1,-2,0,0,0),(0,1,-1,0,0))),
14:([_eq((0,0,1,2,0)),_eq((0,1,0,1,1)),_eq((1,2,0,0,0))],_L((1,-1,0,0,0),(0,1,-2,0,0),(0,0,1,0,-1))),
15:([_eq((0,0,1,2,0)),_eq((0,2,0,0,1)),_eq((2,0,0,1,0)),_eq((0,0,0,0,2),5)],_L((0,1,0,-1,0),(0,0,0,1,-1),(0,-2,1,0,0))),
}

def pentagon_tiles_alone(angles, lengths):
    """angles in pi/N units (N=core.HALF) at vertices; lengths[i] side from
    vertex i to i+1.  Returns the first matching (type, sign, offset) or None.
    Rao targets 10 (=2pi) and 5 (=pi) are rescaled to 2N and N."""
    N = core.HALF
    for typ, (aeqs0, leqs) in RAO.items():
        aeqs = [(row, t * N // 5) for row, t in aeqs0]
        for sign in (1, -1):
            for off in range(5):
                amap = [(off + sign * i) % 5 for i in range(5)]
                new = [angles[j] for j in amap]
                if not all(sum(a * b for a, b in zip(row, new)) == t for row, t in aeqs):
                    continue
                smap = [(off + i) % 5 if sign == 1 else (off - i - 1) % 5 for i in range(5)]
                ok = True
                for row in leqs:
                    tot = core.ZERO
                    for c, side in zip(row, smap):
                        tot = core.zadd(tot, core.zscale(c, lengths[side]))
                    if tot != core.ZERO:
                        ok = False; break
                if ok:
                    return (typ, sign, off)
    return None

def hexagon_tiles_alone(angles, lengths):
    """Reinhardt types, conservative (two side-label conventions for type 2).
    Type1: three consecutive angles sum 2pi and the parallel sides they bound
    are equal.  Type2: B+C+E=2pi, a=d, c=e.  Type3 needs 2pi/3 angles, absent."""
    n = 6
    for sign in (1, -1):
        for off in range(6):
            A = [angles[(off + sign * i) % 6] for i in range(6)]  # A..F
            if sign == 1:
                side = [lengths[(off + i) % 6] for i in range(6)]       # AB,BC,..,FA
            else:
                side = [lengths[(off - i - 1) % 6] for i in range(6)]
            a, b, c, d, e, f = side
            B, C, D, E = A[1], A[2], A[3], A[4]
            N = core.HALF
            if B + C + D == 2 * N and a == d:
                return ("type1", sign, off)
            if B + C + E == 2 * N:
                if a == d and c == e:
                    return ("type2", sign, off)
                # alternative convention a=FA,b=AB,...
                a2, b2, c2, d2, e2, f2 = f, a, b, c, d, e
                if a2 == d2 and c2 == e2:
                    return ("type2alt", sign, off)
            if A[1] == A[3] == A[5] and 3 * A[1] == 2 * N and a == b and c == d and e == f:
                return ("type3", sign, off)
    return None

def solve_closure(angles, free):
    """Directions from the angle word; free lengths for sides 2..n-1 (Z[phi],
    each a multiple of 2 so the solved sides are integral).  Returns full
    length list or None if side0/side1 are not positive."""
    n = len(angles)
    H = core.HALF; ND = core.NDIR
    dirs = [0]
    for i in range(1, n):
        dirs.append((dirs[-1] + H - angles[i]) % ND)
    assert (dirs[-1] + H - angles[0]) % ND == 0, "angle sum"
    R = (0, 0, 0, 0)
    for L, d in zip(free, dirs[2:]):
        R = core.padd(R, core.vec(L, d))
    u0, u1 = core.UNIT[dirs[0]], core.UNIT[dirs[1]]
    den = core.cross(u0, u1)      # 2*sin(angle)/sin(pi/5): (2,0) or (0,2) up to sign
    negR = core.psub((0, 0, 0, 0), R)
    n0 = core.cross(negR, u1); n1 = core.cross(u0, negR)
    def div(num, den):
        # exact division in Z[w]: num*conj(den)/norm(den), integrality required
        a, b = den
        if core.Q1 == 1:   # w=phi, conj(w)=1-w, norm=a^2+ab-b^2
            cj = (a + b, -b); nrm = a * a + a * b - b * b
        else:              # w=sqrt(d)
            cj = (a, -b); nrm = a * a - core.Q0 * b * b
        q = core.zmul(num, cj)
        if q[0] % nrm or q[1] % nrm: return None
        return (q[0] // nrm, q[1] // nrm)
    L0 = div(n0, den); L1 = div(n1, den)
    if L0 is None or L1 is None: return None
    if core.zsign(L0) <= 0 or core.zsign(L1) <= 0: return None
    lengths = [L0, L1] + list(free)
    pts = core.polygon_from_word(angles, lengths)
    assert pts is not None
    assert core.is_strictly_convex_ccw(pts)
    return lengths

def cyclic_words(n, total, maxangle=4):
    """angle words up to rotation/reversal, entries 1..maxangle."""
    seen = set(); out = []
    for w in product(range(1, maxangle + 1), repeat=n):
        if sum(w) != total: continue
        reps = []
        for s in range(n):
            r = w[s:] + w[:s]
            reps.append(r); reps.append(tuple(reversed(r)))
        c = min(reps)
        if c in seen: continue
        seen.add(c); out.append(c)
    return out

def adjacent_supplementary(word, N=5):
    n = len(word)
    return any(word[i] + word[(i + 1) % n] == N for i in range(n))
