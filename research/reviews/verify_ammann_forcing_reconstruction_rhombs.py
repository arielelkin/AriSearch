#!/usr/bin/env python3
"""Independent hostile re-check of Lemma 6 of
research/lemmas/ammann-forcing-aperiodicity.md (marked rhombs: vertex stars,
radius-1 patches, unique composition, closure of the composition).

Written from the lemma statement only; it does not import or copy the authors'
code.  All decisions are exact: points are integer vectors in Z[w],
w = exp(i pi/5), basis (1, w, w^2, w^3), w^4 = -1 + w - w^2 + w^3.  Sign tests
use Im(x) = sin36 * (c1 + phi*(c2 + c3)) and exact arithmetic in Q(sqrt5).

Run:
  conda run --no-capture-output -n arisearch python3 \
      research/reviews/verify_ammann_forcing_reconstruction_rhombs.py
"""
import sys, itertools
from fractions import Fraction as Fr

# ---------------------------------------------------------------- Z[w]
def add(u, v): return tuple(a + b for a, b in zip(u, v))
def sub(u, v): return tuple(a - b for a, b in zip(u, v))
def neg(u): return tuple(-a for a in u)
def timesw(u):
    a, b, c, d = u              # a + b w + c w^2 + d w^3 ;  d w^4 = d(-1 + w - w^2 + w^3)
    return (-d, a + d, b - d, c + d)
def wpow(u, k):
    for _ in range(k % 10):
        u = timesw(u)
    return u
O = (0, 0, 0, 0)
I1 = (1, 0, 0, 0)
def W(k): return wpow(I1, k)
def mul(u, v):
    r = O
    p = v
    for i in range(4):
        r = add(r, tuple(u[i] * x for x in p))
        p = timesw(p)
    return r
PHI = add(add(I1, W(2)), neg(W(3)))            # phi = 1 + w^2 - w^3  (checked below)
IPHI = sub(PHI, I1)
assert mul(PHI, PHI) == add(PHI, I1)
assert mul(PHI, IPHI) == I1
def conj(u):                                   # complex conjugate: w -> w^9 = w^-1
    r = O
    for i in range(4):
        r = add(r, tuple(u[i] * x for x in W(-i)))
    return r

# exact sign of real numbers a + b*sqrt5 (a, b rationals)
def sgn_q5(a, b):
    # sign of a + b sqrt5
    if b == 0: return (a > 0) - (a < 0)
    if a == 0: return (b > 0) - (b < 0)
    if (a > 0) == (b > 0): return 1 if a > 0 else -1
    # opposite signs: compare a^2 vs 5 b^2
    d = a * a - 5 * b * b
    if d == 0: return 0
    return (1 if a > 0 else -1) if d > 0 else (1 if b > 0 else -1)
def im_sign(u):
    # Im(u)/sin36 = c1 + phi (c2 + c3) ; phi = (1 + sqrt5)/2
    c0, c1, c2, c3 = u
    s = c2 + c3
    return sgn_q5(Fr(c1) + Fr(s, 2), Fr(s, 2))
def cross_sign(p, q, r):                       # orientation of (p, q, r)
    return im_sign(mul(conj(sub(q, p)), sub(r, p)))
# sanity of im_sign
assert all(im_sign(W(k)) == (1 if 0 < k < 5 else (-1 if k > 5 else 0)) for k in range(10))

# ---------------------------------------------------------------- marked rhombs
# A placed rhomb: (kind, anchor, k).  Vertices in ccw order with labels.
# thin : A=p, B=p+w^k, C=B+w^(k+1), D=p+w^(k+1)    (36 deg at A)
# thick: E=p, F=p+w^k, G=F+w^(k+2), H=p+w^(k+2)    (72 deg at E)
# Marks as stated in the lemma:
#  thin  X: A->B, C->B   Y: A->D, C->D ;  thick X: E->F, E->H   Y: F->G, H->G
LAB = {'thin': 'ABCD', 'thick': 'EFGH'}
MARKS = {'thin': [('X', 'A', 'B'), ('X', 'C', 'B'), ('Y', 'A', 'D'), ('Y', 'C', 'D')],
         'thick': [('X', 'E', 'F'), ('X', 'E', 'H'), ('Y', 'F', 'G'), ('Y', 'H', 'G')]}
STEP = {'thin': 1, 'thick': 2}

def rverts(R, scale=I1):
    kind, p, k = R
    a = mul(scale, W(k)); b = mul(scale, W(k + STEP[kind]))
    return [p, add(p, a), add(add(p, a), b), add(p, b)]
def rlab(R, scale=I1):
    return dict(zip(LAB[R[0]], rverts(R, scale)))
def redges(R, scale=I1):
    """dict frozenset{u,v} -> (type, tail, head)"""
    L = rlab(R, scale)
    return {frozenset((L[a], L[b])): (t, L[a], L[b]) for t, a, b in MARKS[R[0]]}
def rcanon(R, scale=I1):
    """canonical key: kind + labelled vertex tuple (placements of a symmetric
    marked rhomb that coincide as marked sets get the same key)"""
    return (R[0], frozenset(redges(R, scale).values()))

# sanity: each edge of a rhomb is marked exactly once; all 4 boundary edges
for kind in LAB:
    for k in range(10):
        V = rverts((kind, O, k))
        E = redges((kind, O, k))
        assert set(E) == {frozenset((V[i], V[(i + 1) % 4])) for i in range(4)}
        assert all(cross_sign(V[i], V[(i + 1) % 4], V[(i + 2) % 4]) > 0 for i in range(4))

# The marked rhombs are mirror symmetric (thin: in line BD; thick: in line EG)?
# check: reflection fixing the symmetry axis maps marks to marks.
def reflect_line(z, p, d):                     # reflect z in the line p + R*d, d = w^m
    # z -> p + d^2 * conj(z - p)
    return add(p, mul(mul(d, d), conj(sub(z, p))))
def check_mirror_symmetry():
    out = {}
    for kind in LAB:
        R = (kind, O, 0)
        L = rlab(R)
        if kind == 'thin':
            p, q = L['B'], L['D']
        else:
            p, q = L['E'], L['G']
        dvec = sub(q, p)
        # find unit direction m with dvec parallel to w^m (cross = 0)
        ms = [m for m in range(10) if im_sign(mul(conj(W(m)), dvec)) == 0 and
              im_sign(mul(conj(W(m + 5)), dvec)) == 0]
        # dvec might not be a unit multiple in Z[w]; use reflection with d^2 = dvec/conj(dvec) unit
        # simpler: test both candidate m giving collinearity
        good = False
        for m in ms:
            img = {(t, reflect_line(a, p, W(m)), reflect_line(b, p, W(m))) for t, a, b in redges(R).values()}
            if img == set(redges(R).values()):
                good = True
        out[kind] = good
    return out

# ---------------------------------------------------------------- vertex stars
# All placements of a rhomb having a given vertex v, with the corner label.
def placements_at(v):
    res = []
    for kind in LAB:
        for k in range(10):
            R0 = (kind, O, k)
            for lab, z in rlab(R0).items():
                R = (kind, sub(v, z), k)
                res.append((lab, R))
    return res

def corner_dirs(R, v):
    """sector of rhomb R at its vertex v: (d1, d2, ang) with the corner spanning
    directions d1 .. d1+ang (ccw), in units of 36 deg"""
    V = rverts(R)
    i = V.index(v)
    nx, pv = V[(i + 1) % 4], V[(i - 1) % 4]
    d1 = [m for m in range(10) if sub(nx, v) == W(m)][0]
    d2 = [m for m in range(10) if sub(pv, v) == W(m)][0]
    return d1, (d2 - d1) % 10

PL0 = placements_at(O)
SECT = {}
for lab, R in PL0:
    d1, ang = corner_dirs(R, O)
    SECT[rcanon(R)] = (lab, R, d1, ang)
# marked rhombs are mirror symmetric -> distinct placements could coincide; keep unique keys
CORN0 = list(SECT.values())

def edge_mark_at(R, v, d):
    """mark of the edge of R from v in direction d, as (type, 'out'/'in')"""
    u = add(v, W(d))
    t, a, b = redges(R)[frozenset((v, u))]
    return (t, 'out' if a == v else 'in')

def all_stars_at_origin():
    """exact covers of the 10 sectors at the origin by rhomb corners whose
    shared rays carry equal marks"""
    by_start = {}
    for lab, R, d1, ang in CORN0:
        by_start.setdefault(d1, []).append((lab, R, d1, ang))
    stars = []
    def rec(start, d, chosen):
        if d == start + 10:
            # closing ray mark
            first, last = chosen[0], chosen[-1]
            if edge_mark_at(first[1], O, first[2] % 10) == edge_mark_at(last[1], O, (last[2] + last[3]) % 10):
                stars.append(tuple(chosen))
            return
        for c in by_start.get(d % 10, []):
            if d + c[3] > start + 10:
                continue
            if chosen and edge_mark_at(chosen[-1][1], O, d % 10) != edge_mark_at(c[1], O, d % 10):
                continue
            rec(start, d + c[3], chosen + [c])
    # every star has a corner starting at some direction; fix the corner that
    # contains direction 0 at its start or interior: enumerate starts 0..9 and
    # dedupe by rhomb set
    seen = {}
    for s in range(10):
        stars.clear()
        rec(s, s, [])
        for st in stars:
            key = frozenset(rcanon(c[1]) for c in st)
            seen[key] = st
    return seen

def star_type(st):
    """rotation-invariant type: cyclic sequence of (kind, label) up to rotation"""
    seq = sorted(st, key=lambda c: c[2])
    names = [(c[1][0], c[0]) for c in seq]
    n = len(names)
    return min(tuple(names[i:] + names[:i]) for i in range(n))

RAW = all_stars_at_origin()          # all placed stars at origin (all rotations)
RAW_TYPES = {}
for key, st in RAW.items():
    RAW_TYPES.setdefault(star_type(st), []).append(key)

def rotate_R(R, m):
    kind, p, k = R
    return (kind, wpow(p, m), k + m)

def star_placements_at(v, types):
    """all placed stars at vertex v of the given types: list of frozensets of rcanon keys,
    together with the rhombs"""
    out = []
    for ty in types:
        for key in RAW_TYPES[ty]:
            st = RAW[key]
            Rs = [(c[1][0], add(c[1][1], v), c[1][2]) for c in st]
            out.append((frozenset(rcanon(R) for R in Rs), Rs))
    return out

def prune(types):
    """edge-consistency pruning: for a star S at origin and each ray, the two
    rhombs on both sides of the edge must occur together in some star (of a
    surviving type) at the far end of the ray."""
    alive = set(types)
    while True:
        # precompute set of rhomb-pairs present in surviving stars at origin
        pair_ok = set()
        for ty in alive:
            for key in RAW_TYPES[ty]:
                ks = list(key)
                for a in ks:
                    for b in ks:
                        if a != b:
                            pair_ok.add((a, b))
        def translate_key(key, v):
            kind, es = key
            return (kind, frozenset((t, sub(a, v), sub(b, v)) for t, a, b in es))
        new = set()
        for ty in alive:
            ok = True
            key = RAW_TYPES[ty][0]
            st = RAW[key]
            for d in range(10):
                u = W(d)
                side = [c for c in st if frozenset((O, u)) in redges(c[1])]
                if not side:
                    continue
                assert len(side) == 2
                a, b = (translate_key(rcanon(c[1]), u) for c in side)
                if (a, b) not in pair_ok:
                    ok = False
                    break
            if ok:
                new.add(ty)
        if new == alive:
            return alive
        alive = new

# ---------------------------------------------------------------- radius-1 patches
def angular_ok(rhombs):
    occ = {}
    for R in rhombs:
        for v in rverts(R):
            d1, ang = corner_dirs(R, v)
            s = occ.setdefault(v, [0] * 10)
            for j in range(ang):
                s[(d1 + j) % 10] += 1
                if s[(d1 + j) % 10] > 1:
                    return False
    return True

def interiors_disjoint(R1, R2):
    P, Q = rverts(R1), rverts(R2)
    for A, B in ((P, Q), (Q, P)):
        for i in range(4):
            p, q = A[i], A[(i + 1) % 4]
            if all(cross_sign(p, q, z) <= 0 for z in B):
                return True
    return False

def patches_for(type0, alive):
    key0 = RAW_TYPES[type0][0]
    base = {rcanon(c[1]): c[1] for c in RAW[key0]}
    nbrs = sorted({v for R in base.values() for v in rverts(R) if v != O})
    cands = {v: star_placements_at(v, alive) for v in nbrs}
    res = []
    def rec(P, i):
        if i == len(nbrs):
            res.append(dict(P))
            return
        v = nbrs[i]
        present = {k for k, R in P.items() if v in rverts(R)}
        for keys, Rs in cands[v]:
            if not present <= keys:
                continue
            Q = dict(P)
            for R in Rs:
                Q[rcanon(R)] = R
            if angular_ok(Q.values()):
                rec(Q, i + 1)
    rec(base, 0)
    # dedupe
    uniq = {}
    for P in res:
        uniq[frozenset(P)] = P
    return list(uniq.values()), nbrs

# ---------------------------------------------------------------- halves and deflation
# half = (colour, apex, Blab, Clab): leg apex-Blab is the X leg, apex-Clab the Y leg.
def halves_of(R, scale=I1):
    L = rlab(R, scale)
    if R[0] == 'thin':
        return [('red', L['A'], L['B'], L['D']), ('red', L['C'], L['B'], L['D'])]
    return [('blue', L['F'], L['E'], L['G']), ('blue', L['H'], L['E'], L['G'])]

def deflate(h):
    """Robinson/Preshing P3 deflation of a half of edge length phi into halves
    of edge length 1 (exact: division by phi = multiplication by phi - 1)."""
    col, A, B, C = h
    if col == 'red':
        P = add(A, mul(IPHI, sub(B, A)))
        return [('red', C, P, B), ('blue', P, C, A)]
    Q = add(B, mul(IPHI, sub(A, B)))
    Rr = add(B, mul(IPHI, sub(C, B)))
    return [('blue', Rr, C, A), ('blue', Q, Rr, B), ('red', Rr, Q, A)]

def big_children(R):
    return [c for h in halves_of(R, PHI) for c in deflate(h)]

# canonical big rhombs at origin, their children
BIG0 = [(kind, O, k) for kind in LAB for k in range(10)]
BIGCH0 = {R: big_children(R) for R in BIG0}

def tr_half(h, v): return (h[0],) + tuple(add(x, v) for x in h[1:])

def parent_candidates(t):
    """all big marked rhombs R (edge phi) with t among the deflation halves of R
    (brute force over 20 orientations and all children)"""
    out = {}
    for R0, chs in BIGCH0.items():
        for h in chs:
            if h[0] != t[0]:
                continue
            v = sub(t[1], h[1])
            if tr_half(h, v) == t:
                R = (R0[0], v, R0[2])
                out[rcanon(R, PHI)] = R
    return list(out.values())

def common_vertex(chs):
    s = set(chs[0][1:])
    for c in chs[1:]:
        s &= set(c[1:])
    return s

# ---------------------------------------------------------------- closure
def closure_check():
    """For each big rhomb R and each child h of R whose twin (other half of h's
    small rhomb) is not a child of R, every big rhomb R' having that twin as a
    child either overlaps R in its interior (excluded in a tiling) or shares a
    full edge with R carrying the same mark.  Also: every edge of R carries
    such a child base."""
    bad = []
    stats = {'cases': 0, 'overlap_excluded': 0, 'edge_match': 0}
    for R in BIG0:
        chs = BIGCH0[R]
        chset = set(chs)
        Redges = redges(R, PHI)
        covered = set()
        for h in chs:
            col, A, B, C = h
            tw = (col, add(B, sub(C, A)), B, C)
            if tw in chset:
                continue
            # base B-C must lie on the boundary of R: find which edge
            stats['cases'] += 1
            for R2 in parent_candidates(tw):
                if not interiors_disjoint_big(R, R2):
                    stats['overlap_excluded'] += 1
                    continue
                E2 = redges(R2, PHI)
                shared = set(Redges) & set(E2)
                ok = any(Redges[e] == E2[e] and on_segment(B, e) and on_segment(C, e) for e in shared)
                if ok:
                    stats['edge_match'] += 1
                    for e in shared:
                        if on_segment(B, e) and on_segment(C, e):
                            covered.add(e)
                else:
                    bad.append((R, h, R2))
        if covered != set(Redges):
            bad.append(('uncovered edge', R, set(Redges) - covered))
    return bad, stats

def on_segment(z, e):
    p, q = tuple(e)
    if cross_sign(p, q, z) != 0:
        return False
    # between: (z-p).(q-p) >= 0 and (z-q).(p-q) >= 0 ; dot = Re(conj(a) b)
    return re_sign(mul(conj(sub(z, p)), sub(q, p))) >= 0 and re_sign(mul(conj(sub(z, q)), sub(p, q))) >= 0

def re_sign(u):
    # Re(sum c_k w^k) = c0 + c1 cos36 + c2 cos72 + c3 cos108 ; cos36 = phi/2, cos72 = (phi-1)/2
    c0, c1, c2, c3 = u
    # cos36 = (1+s5)/4, cos72 = (s5-1)/4, cos108 = -(s5-1)/4
    a = Fr(c0) + Fr(c1, 4) - Fr(c2, 4) + Fr(c3, 4)
    b = Fr(c1, 4) + Fr(c2, 4) - Fr(c3, 4)
    return sgn_q5(a, b)

def interiors_disjoint_big(R1, R2):
    P, Q = rverts(R1, PHI), rverts(R2, PHI)
    for A, B in ((P, Q), (Q, P)):
        for i in range(4):
            p, q = A[i], A[(i + 1) % 4]
            if all(cross_sign(p, q, z) <= 0 for z in B):
                return True
    return False

# ---------------------------------------------------------------- deflation closure
def legs(h):
    col, A, B, C = h
    x = ('X', A, B) if col == 'red' else ('X', B, A)
    return [x, ('Y', A, C)]

def deflation_closure():
    """sigma maps legal tilings (and legal patches) to legal ones.  Every leg l
    of a child of big rhomb R1 lies inside R1 or on an edge e of R1; for each
    legal neighbour R2 across e (and for R1 alone when l is interior), the
    unique other child containing l must have l as a full leg with the same
    mark, and no child may have l as its base."""
    bad = []; n = 0
    for R1 in BIG0:
        E1 = redges(R1, PHI)
        ch1 = big_children(R1)
        for e, mk in E1.items():
            # all legal neighbours across e
            nbrs = []
            for kind in LAB:
                for k in range(10):
                    R0 = (kind, O, k)
                    for e0, mk0 in redges(R0, PHI).items():
                        if mk0[0] != mk[0]:
                            continue
                        v = sub(mk[1], mk0[1])
                        if add(mk0[2], v) != mk[2]:
                            continue
                        R2 = (kind, v, k)
                        if interiors_disjoint_big(R1, R2):
                            nbrs.append(R2)
            if not nbrs:
                bad.append(('no neighbour', R1, mk))
            for R2 in nbrs:
                allch = ch1 + big_children(R2)
                for h in ch1:
                    for lg in legs(h):
                        seg = frozenset(lg[1:])
                        # skip legs on an edge of R1 other than e
                        on_other = [f for f in E1 if f != e and all(on_segment(z, f) for z in seg)]
                        if on_other:
                            continue
                        n += 1
                        others = [g for g in allch if g != h and any(frozenset(m[1:]) == seg for m in legs(g))]
                        bases = [g for g in allch if frozenset(g[2:]) == seg]
                        if len(others) != 1 or bases or \
                                [m for m in legs(others[0]) if frozenset(m[1:]) == seg][0] != lg:
                            bad.append((R1, R2, h, lg, len(others), len(bases)))
    return bad, n

# ---------------------------------------------------------------- genuine P3 patches
def sun_halves():
    out = []
    for i in range(10):
        B, C = W(i), W(i + 1)
        if i % 2 == 0:
            B, C = C, B
        out.append(('red', O, B, C))
    return out

def scale_half(h, f): return (h[0],) + tuple(mul(f, x) for x in h[1:])

def p3_patch(n):
    hs = sun_halves()
    for _ in range(n):
        hs = [c for h in hs for c in deflate(scale_half(h, PHI))]
    return hs

def rhombs_from_halves(hs):
    S = set(hs)
    out = []
    for h in hs:
        col, A, B, C = h
        tw = (col, add(B, sub(C, A)), B, C)
        if tw in S and h < tw:
            out.append((h, tw))
    return out

def legality_of_patch(hs):
    """build marked rhombs from complete twin pairs; check every edge shared by
    two rhombs carries equal marks and no edge has 3 rhombs; collect complete
    vertex stars"""
    pairs = rhombs_from_halves(hs)
    edges = {}
    rh_list = []
    for h, tw in pairs:
        col, A, B, C = h
        A2 = tw[1]
        # legs: A-B X (red: A->B ; blue: B->A), A-C Y (A->C) ; same for twin
        if col == 'red':
            mk = [('X', A, B), ('X', A2, B), ('Y', A, C), ('Y', A2, C)]
        else:
            mk = [('X', B, A), ('X', B, A2), ('Y', A, C), ('Y', A2, C)]
        rh_list.append((col, mk))
        for m in mk:
            edges.setdefault(frozenset(m[1:]), []).append(m)
    bad = [e for e, ms in edges.items() if len(ms) > 2 or (len(ms) == 2 and ms[0] != ms[1])]
    return len(pairs), sum(1 for ms in edges.values() if len(ms) == 2), bad

# ---------------------------------------------------------------- main
def main():
    log = []
    def say(*a):
        s = ' '.join(str(x) for x in a)
        print(s, flush=True)
        log.append(s)
    say('mirror symmetry of the marked rhombs:', check_mirror_symmetry())
    types = sorted(RAW_TYPES)
    say('R1 raw vertex-star types (up to rotation, reflections distinct):', len(types),
        '| placed raw stars at origin:', len(RAW))
    alive = prune(types)
    say('R1 viable after edge-consistency pruning:', len(alive))
    for ty in sorted(alive):
        say('   ', [lab for kind, lab in ty])
    dead = sorted(set(types) - alive)
    say('   pruned:', [[lab for kind, lab in ty] for ty in dead])

    # R2 patches (superset) and real subset (pairwise disjoint interiors)
    total = 0; total_real = 0; ncases = 0; fails = []
    pivot_ok = True
    hist = {}
    for ty in sorted(alive):
        pats, nbrs = patches_for(ty, alive)
        nreal = 0
        for P in pats:
            Rs = list(P.values())
            real = all(interiors_disjoint(a, b) for a, b in itertools.combinations(Rs, 2))
            nreal += real
            H = set()
            for R in Rs:
                H.update(halves_of(R))
            for t in [h for h in H if O in h[1:]]:
                ncases += 1
                cands = parent_candidates(t)
                valid = []
                for R in cands:
                    chs = big_children(R)
                    cv = common_vertex(chs)
                    # locality: some common point of all children is a vertex of t
                    if not (cv & set(t[1:])):
                        pivot_ok = False
                    if all(c in H for c in chs):
                        valid.append(R)
                hist[(len(cands), len(valid))] = hist.get((len(cands), len(valid)), 0) + 1
                if len(valid) != 1:
                    fails.append((ty, t, len(valid), real))
        total += len(pats); total_real += nreal
        say('R2 star', [lab for kind, lab in ty], 'neighbours', len(nbrs), 'patches', len(pats),
            'with pairwise-disjoint interiors', nreal)
    say('R2 total patches', total, '(geometrically non-overlapping:', total_real, ')')
    say('R3 half-at-origin cases', ncases, 'failures', len(fails),
        'locality (common child vertex is a vertex of t) holds:', pivot_ok)
    say('   histogram (#candidate big rhombs, #valid) -> count:', dict(sorted(hist.items())))
    for f in fails[:10]:
        say('   FAIL', f)

    bad, st = closure_check()
    say('closure: twin-outside cases', st, 'defects', len(bad))
    for b in bad[:10]:
        say('   CLOSURE DEFECT', b)

    badd, nd = deflation_closure()
    say('deflation closure (sigma maps legal to legal): leg checks', nd, 'defects', len(badd))
    for b in badd[:10]:
        say('   DEFLATION DEFECT', b)
    bad = bad + badd
    # genuine P3 patches (Robinson deflation of a sun)
    for n in range(1, 8):
        hs = p3_patch(n)
        nr, ne, badm = legality_of_patch(hs)
        say('P3 sun deflated', n, 'times: complete rhombs', nr, 'shared edges', ne, 'mark conflicts', len(badm))
    # observed stars in genuine patch vs viable list
    hs = p3_patch(7)
    pairs = rhombs_from_halves(hs)
    # reconstruct placed rhombs (kind, anchor, k) from halves
    def rhomb_of(h):
        col, A, B, C = h
        for R0 in [(kind, O, k) for kind in LAB for k in range(10)]:
            L = rlab(R0)
            if col == 'red':
                cand = [(L['A'], L['B'], L['D']), (L['C'], L['B'], L['D'])] if R0[0] == 'thin' else []
            else:
                cand = [(L['F'], L['E'], L['G']), (L['H'], L['E'], L['G'])] if R0[0] == 'thick' else []
            for a, b, c in cand:
                v = sub(A, a)
                if add(b, v) == B and add(c, v) == C:
                    return (R0[0], v, R0[2])
        raise AssertionError
    placed = [rhomb_of(h) for h, tw in pairs]
    at = {}
    for R in placed:
        for v in rverts(R):
            at.setdefault(v, []).append(R)
    obs = {}
    for v, Rs in at.items():
        if sum(corner_dirs(R, v)[1] for R in Rs) != 10:
            continue
        seq = sorted(Rs, key=lambda R: corner_dirs(R, v)[0])
        names = [(R[0], LAB[R[0]][rverts(R).index(v)]) for R in seq]
        n = len(names)
        ty = min(tuple(names[i:] + names[:i]) for i in range(n))
        obs[ty] = obs.get(ty, 0) + 1
    say('genuine P3 (sun x7): complete vertices', sum(obs.values()), 'distinct star types', len(obs))
    say('   observed - viable:', [list(x) for x in set(obs) - alive])
    say('   viable - observed:', [list(x) for x in alive - set(obs)])
    ok = (not fails) and pivot_ok and not bad and len(alive) == 8 and set(obs) == alive
    say('ALL RHOMB CHECKS PASSED' if ok else 'SOME CHECK FAILED')
    if len(sys.argv) > 1:
        open(sys.argv[1], 'w').write('\n'.join(log) + '\n')

if __name__ == '__main__':
    main()
