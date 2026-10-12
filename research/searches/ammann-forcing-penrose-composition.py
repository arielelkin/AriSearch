#!/usr/bin/env python3
"""Self-contained, exact verification that every tiling by the arrow-marked
Penrose rhombs (the marking induced by Ammann's decoration) has a unique,
translation-equivariant composition into a legal tiling scaled by phi; hence
no such tiling has a nonzero translational symmetry.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-forcing-penrose-composition.py \
      research/certificates/ammann-forcing-penrose-composition.json

Exact arithmetic: points are integer vectors in Z[w] = Z^4 (basis 1,w,w^2,w^3,
w^4 = -1+w-w^2+w^3), directions are integers mod 10 (units of 36 degrees).
No floating point is used anywhere.

Marked rhombs (unit edges, counter-clockwise vertex order):
  thin  A,B,C,D  (A,C: 36 deg; B,D: 144 deg)   X: A->B, C->B   Y: A->D, C->D
  thick E,F,G,H  (E,G: 72 deg; F,H: 108 deg)   X: E->F, E->H   Y: F->G, H->G
A legal tiling: edge-to-edge tiling of the plane by translated/rotated copies
(each marked rhomb is mirror symmetric, so reflections add nothing), every
shared edge carrying the same type and direction from both sides.

Robinson halves (Preshing labels (colour, apex, Blabel, Clabel)):
  thin  -> red (A;B,D), red (C;B,D);  thick -> blue (F;E,G), blue (H;E,G).
Deflation sigma (Preshing):
  red (A,B,C):  P = A+(B-A)/phi  -> red (C,P,B), blue (P,C,A)
  blue(A,B,C):  Q = B+(A-B)/phi, R = B+(C-B)/phi
                -> blue (R,C,A), blue (Q,R,B), red (R,Q,A)

Steps.
 R1 vertex stars: all cyclic corner sequences of total angle 360 with equal
    marks on shared rays, pruned to a fixed point by requiring that, for every
    pair of consecutive corners, the two far-end corners of the shared edge are
    consecutive (in the right order) in some surviving star.
 R2 vertex patches: for every surviving star S placed at the origin, all ways
    of choosing surviving stars at every neighbouring vertex (every vertex of a
    rhomb of S) consistently (same corners where they overlap, no two corners
    overlapping at any vertex).  This is a SUPERSET of the radius-1 patches of
    legal tilings (no global overlap test is needed for soundness).
 R3 for every patch and every half-triangle t with a vertex at the origin:
    among the parent hypotheses H of t (5 possible, see parents()), exactly
    ONE is valid, where H is valid iff every sigma-child of H and of its
    mirror twin H* (same colour, apex reflected in the base BC) is a half in
    the patch.  Locality: the pivot of H (C for red parents, R for blue
    parents) is a vertex of t, and every child of H and of H* contains the
    pivot, so all of them are halves of rhombs in the star at a vertex of t,
    which the patch contains.  (Using H alone is NOT enough: a big blue
    triangle (A;B,C) contains the big red (B;A,R), so the red hypothesis is
    then also satisfied; requiring the twin removes exactly such cases.)
"""
import sys, json, itertools

# ------------------------------------------------------------- Z[w] arithmetic
def add(u, v): return (u[0] + v[0], u[1] + v[1], u[2] + v[2], u[3] + v[3])
def sub(u, v): return (u[0] - v[0], u[1] - v[1], u[2] - v[2], u[3] - v[3])
def mulw(u):
    a, b, c, d = u
    return (-d, a + d, b - d, c + d)
def rot(u, k):
    for _ in range(k % 10):
        u = mulw(u)
    return u
def smul(n, u): return tuple(n * x for x in u)
ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)
def W(k): return rot(ONE, k)
def mulphi(u):          # phi = 1 + w^2 - w^3
    return sub(add(u, rot(u, 2)), rot(u, 3))
def mul_iphi(u):        # 1/phi = phi - 1
    return sub(mulphi(u), u)
def mulphi2(u): return mulphi(mulphi(u))
assert mulphi(mul_iphi((3, -1, 2, 5))) == (3, -1, 2, 5)
assert mulphi(mulphi(ONE)) == add(mulphi(ONE), ONE)      # phi^2 = phi + 1

# ------------------------------------------------------------- marked rhombs
# corner data: label -> (angle units, offset of vertex from reference, cw-ray dir offset,
#                        (cw mark, ccw mark));  mark = (type, 'out'|'in') at the vertex
THIN = {
    'A': (1, lambda k: ZERO, 0, (('X', 'out'), ('Y', 'out'))),
    'B': (4, lambda k: W(k), 1, (('X', 'in'), ('X', 'in'))),
    'C': (1, lambda k: add(W(k), W(k + 1)), 5, (('Y', 'out'), ('X', 'out'))),
    'D': (4, lambda k: W(k + 1), 6, (('Y', 'in'), ('Y', 'in'))),
}
THICK = {
    'E': (2, lambda k: ZERO, 0, (('X', 'out'), ('X', 'out'))),
    'F': (3, lambda k: W(k), 2, (('Y', 'out'), ('X', 'in'))),
    'G': (2, lambda k: add(W(k), W(k + 2)), 5, (('Y', 'in'), ('Y', 'in'))),
    'H': (3, lambda k: W(k + 2), 7, (('X', 'in'), ('Y', 'out'))),
}
SHAPE = {'thin': THIN, 'thick': THICK}
ORDER = {'thin': 'ABCD', 'thick': 'EFGH'}

def verts(rh):
    typ, p, k = rh
    return {lab: add(p, d[1](k)) for lab, d in SHAPE[typ].items()}

def corner_dirs(rh):
    typ, p, k = rh
    return {lab: (k + d[2]) % 10 for lab, d in SHAPE[typ].items()}

def rhomb_from_corner(typ, lab, u, cwdir):
    d = SHAPE[typ][lab]
    k = (cwdir - d[2]) % 10
    return (typ, sub(u, d[1](k)), k)

# self-check of the geometry: the cw ray of each corner points to the next vertex,
# the ccw ray to the previous one, and angles are right
for typ in SHAPE:
    for k in range(10):
        rh = (typ, ZERO, k)
        V = verts(rh); D = corner_dirs(rh); O = ORDER[typ]
        for i, lab in enumerate(O):
            nxt, prv = V[O[(i + 1) % 4]], V[O[i - 1]]
            assert sub(nxt, V[lab]) == W(D[lab])
            assert sub(prv, V[lab]) == W(D[lab] + SHAPE[typ][lab][0])
            assert rhomb_from_corner(typ, lab, V[lab], D[lab]) == rh
CORNERS = [(t, l) for t in ('thin', 'thick') for l in ORDER[t]]
def ang(c): return SHAPE[c[0]][c[1]][0]
def cwmark(c): return SHAPE[c[0]][c[1]][3][0]
def ccwmark(c): return SHAPE[c[0]][c[1]][3][1]

# consistency: for edge from vertex l (cw ray, to next) the mark seen at the next
# vertex on its ccw ray must be the same arrow with in/out swapped
for t in ('thin', 'thick'):
    O = ORDER[t]
    for i, l in enumerate(O):
        m1 = cwmark((t, l)); m2 = ccwmark((t, O[(i + 1) % 4]))
        assert m1[0] == m2[0] and m1[1] != m2[1], (t, l)

# ------------------------------------------------------------- R1 stars
def far_ccw(c):     # far corner along the ccw ray (edge to previous vertex)
    t, l = c; O = ORDER[t]; return (t, O[(O.index(l) - 1) % 4])
def far_cw(c):
    t, l = c; O = ORDER[t]; return (t, O[(O.index(l) + 1) % 4])

def raw_stars():
    out = set()
    def rec(seq, total):
        if total == 10:
            if ccwmark(seq[-1]) == cwmark(seq[0]):
                n = len(seq)
                out.add(min(tuple(seq[k:] + seq[:k]) for k in range(n)))
            return
        for c in CORNERS:
            if total + ang(c) <= 10 and (not seq or ccwmark(seq[-1]) == cwmark(c)):
                rec(seq + [c], total + ang(c))
    rec([], 0)
    return sorted(out)

def cpairs(st):
    n = len(st)
    return {(st[i], st[(i + 1) % n]) for i in range(n)}

def prune(stars):
    alive = list(stars)
    while True:
        avail = set()
        for s in alive:
            avail |= cpairs(s)
        new = [s for s in alive if all((far_cw(Y), far_ccw(X)) in avail
                                       for X, Y in cpairs(s))]
        if len(new) == len(alive):
            return alive
        alive = new

# ------------------------------------------------------------- R2 patches
def place_star(st, u, r):
    """list of (corner, cwdir, rhomb) for star st at vertex u, first corner at dir r"""
    out = []
    d = r
    for c in st:
        out.append((c, d % 10, rhomb_from_corner(c[0], c[1], u, d % 10)))
        d += ang(c)
    return out

def corners_at(patch):
    """vertex -> list of (corner, cwdir, rhomb)"""
    m = {}
    for rh in patch:
        V = verts(rh); D = corner_dirs(rh)
        for lab in V:
            m.setdefault(V[lab], []).append(((rh[0], lab), D[lab], rh))
    return m

def consistent(patch):
    for u, cs in corners_at(patch).items():
        occ = [0] * 10
        for c, d, rh in cs:
            for j in range(ang(c)):
                occ[(d + j) % 10] += 1
        if max(occ) > 1:
            return False
    return True

def vertex_patches(stars, st0):
    base = frozenset(rh for c, d, rh in place_star(st0, ZERO, 0))
    nbrs = sorted({v for rh in base for v in verts(rh).values() if v != ZERO})
    results = []
    def rec(patch, i):
        if i == len(nbrs):
            results.append(patch)
            return
        u = nbrs[i]
        have = {(c, d) for c, d, rh in corners_at(patch).get(u, [])}
        seen = set()
        for st in stars:
            for r in range(10):
                pl = place_star(st, u, r)
                cd = {(c, d) for c, d, rh in pl}
                if not have <= cd:
                    continue
                newp = patch | frozenset(rh for c, d, rh in pl)
                if newp in seen:
                    continue
                seen.add(newp)
                if consistent(newp):
                    rec(newp, i + 1)
    rec(base, 0)
    return results, nbrs

# ------------------------------------------------------------- halves / sigma
def halves(rh):
    V = verts(rh)
    if rh[0] == 'thin':
        return [(0, V['A'], V['B'], V['D']), (0, V['C'], V['B'], V['D'])]
    return [(1, V['F'], V['E'], V['G']), (1, V['H'], V['E'], V['G'])]

def children(T):
    col, A, B, C = T
    if col == 0:
        P = add(A, mul_iphi(sub(B, A)))
        return [(0, C, P, B), (1, P, C, A)]
    Q = add(B, mul_iphi(sub(A, B)))
    R = add(B, mul_iphi(sub(C, B)))
    return [(1, R, C, A), (1, Q, R, B), (0, R, Q, A)]

def parents(t):
    """all parent hypotheses H (each verified to contain t among children(H)),
    with the pivot point"""
    col, a, b, c = t
    hyps = []
    if col == 0:
        C0, P, B0 = a, b, c                       # red(C,P,B) of red parent
        A0 = sub(mulphi2(P), mulphi(B0))
        hyps.append(((0, A0, B0, C0), C0))
        R, Q, A0 = a, b, c                        # red(R,Q,A) of blue parent
        B0 = sub(mulphi2(Q), mulphi(A0))
        C0 = add(B0, mulphi(sub(R, B0)))
        hyps.append(((1, A0, B0, C0), R))
    else:
        P, C0, A0 = a, b, c                       # blue(P,C,A) of red parent
        B0 = add(A0, mulphi(sub(P, A0)))
        hyps.append(((0, A0, B0, C0), C0))
        R, C0, A0 = a, b, c                       # blue(R,C,A) of blue parent
        B0 = sub(mulphi2(R), mulphi(C0))
        hyps.append(((1, A0, B0, C0), R))
        Q, R, B0 = a, b, c                        # blue(Q,R,B) of blue parent
        A0 = add(B0, mulphi(sub(Q, B0)))
        C0 = add(B0, mulphi(sub(R, B0)))
        hyps.append(((1, A0, B0, C0), R))
    for H, pv in hyps:
        assert t in children(H)
        # locality facts used in R3: the pivot is a vertex of t, and every
        # child of H and of its twin contains the pivot
        assert pv in t[1:]
        assert all(pv in ch[1:] for ch in children(H) + children(twin(H)))
    return hyps

def twin(H):
    """mirror image of H in the line BC.  |AB| = |AC|, so A lies on the
    perpendicular bisector of BC and its mirror image is B + C - A."""
    col, A, B, C = H
    return (col, add(B, sub(C, A)), B, C)

# ------------------------------------------------------------- exact helpers
def zmul(u, v):
    out = ZERO
    for k in range(4):
        if v[k]:
            out = add(out, smul(v[k], rot(u, k)))
    return out

def zconj(u):
    a, b, c, d = u                       # conj(w^k) = w^(10-k)
    return (a + b, -b, b - d, -b - c)

assert zconj((0, 1, 0, 0)) == rot(ONE, 9) and zconj((0, 0, 1, 0)) == rot(ONE, 8) \
    and zconj((0, 0, 0, 1)) == rot(ONE, 7)

def sign_phi(x, y):
    """exact sign of x + y*phi, phi = (1+sqrt5)/2"""
    u, v = 2 * x + y, y                  # 2(x + y phi) = u + v sqrt5
    if u >= 0 and v >= 0:
        return 0 if u == 0 and v == 0 else 1
    if u <= 0 and v <= 0:
        return -1
    if u * u > 5 * v * v:
        return 1 if u > 0 else -1
    return 1 if v > 0 else -1

def im_sign(z):                          # Im z = sin36 * (b + (c+d) phi)
    return sign_phi(z[1], z[2] + z[3])

def real_part_phi(z):
    """z real in Z[w] -> (x, y) with z = x + y phi"""
    a, b, c, d = z
    assert b == 0 and c + d == 0
    return (a - c, c)

def on_segment(p, s0, s1):
    d = sub(s1, s0)
    q = zmul(sub(p, s0), zconj(d))
    if im_sign(q) != 0:
        return False
    x, y = real_part_phi(q)
    X, Y = real_part_phi(zmul(d, zconj(d)))
    return sign_phi(x, y) >= 0 and sign_phi(X - x, Y - y) >= 0

def half_edges(h):
    """edges of a half: (endpoints, kind, data); legs carry (type, head),
    the base carries (colour, Blabel, Clabel) = twin identity"""
    col, A, B, C = h
    if col == 0:
        legs = [((A, B), ('leg', 'X', B)), ((A, C), ('leg', 'Y', C))]
    else:
        legs = [((A, B), ('leg', 'X', A)), ((A, C), ('leg', 'Y', C))]
    return legs + [((B, C), ('base', col, B, C))]

def compatible(k1, k2):
    return k1 == k2          # leg: same type and head; base: twins (same colour, B, C)

def big_halves(typ, k):
    rh = (typ, ZERO, k)
    return [tuple([h[0]] + [mulphi(v) for v in h[1:]]) for h in halves(rh)]

# ---------------------------------------------- R5: closure (twin roles)
def closure_check():
    """For every big rhomb R and child h of R whose twin h* is outside R:
    every parent hypothesis R' (= H', twin(H')) of h* either contains h among
    its children (impossible for valid parents: h would have two parents) or
    has, as a full edge, the edge of R carrying the base of h, with the same
    mark (type and head)."""
    stats = {'cases': 0, 'excluded_by_disjointness': 0, 'full_edge_same_mark': 0}
    for typ in ('thin', 'thick'):
        Hs = big_halves(typ, 0)
        chR = set(ch for H in Hs for ch in children(H))
        legsR = [(e, kd) for H in Hs for e, kd in half_edges(H) if kd[0] == 'leg']
        for h in chR:
            ht = twin(h)
            if ht in chR:
                continue
            B, C = h[2], h[3]
            carriers = [(e, kd) for e, kd in legsR if on_segment(B, *e) and on_segment(C, *e)]
            assert len(carriers) == 1, 'base of an outward child must lie on one edge of R'
            eR, kR = carriers[0]
            for Hp, pv in parents(ht):
                stats['cases'] += 1
                chRp = set(children(Hp)) | set(children(twin(Hp)))
                if h in chRp:
                    stats['excluded_by_disjointness'] += 1
                    continue
                legsRp = [(frozenset(e), kd) for H in (Hp, twin(Hp)) for e, kd in half_edges(H) if kd[0] == 'leg']
                assert (frozenset(eR), kR) in legsRp, ('closure failure', typ, h, Hp)
                stats['full_edge_same_mark'] += 1
    return stats

# ------------------------------- R6: deflation preserves legality (existence)
def deflation_legality_check():
    """Legal half-patch: halves with disjoint interiors such that two halves
    meeting along a boundary segment of positive length share a full edge,
    legs with equal mark, bases only between twins.  Check: (a) the children
    of one big half form a legal half-patch; (b) for every legal contact of
    two big halves along a full edge E (base-base twins, or leg-leg with the
    same mark, interiors on opposite sides), the children of the two halves
    lying on E induce the same partition of E with compatible kinds."""
    stats = {'single_halves': 0, 'contacts': 0, 'child_edge_matches': 0}
    pool = [H for typ in ('thin', 'thick') for k in range(10) for H in big_halves(typ, k)]
    base_halves = [H for typ in ('thin', 'thick') for H in big_halves(typ, 0)]
    for H in base_halves:
        # (a) internal edges of the children of H: each used exactly twice, compatibly
        bnd = [e for e, kd in half_edges(H)]
        cnt = {}
        for ch in children(H):
            for e, kd in half_edges(ch):
                onb = any(on_segment(e[0], *b) and on_segment(e[1], *b) for b in bnd)
                if not onb:
                    cnt.setdefault(frozenset(e), []).append(kd)
        for e, kds in cnt.items():
            assert len(kds) == 2 and compatible(kds[0], kds[1]), ('internal', H, e, kds)
        stats['single_halves'] += 1
        # (b) contacts
        third = {frozenset((H[2], H[3])): H[1], frozenset((H[1], H[2])): H[3], frozenset((H[1], H[3])): H[2]}
        for e, kd in half_edges(H):
            s0, s1 = e
            d = sub(s1, s0)
            side1 = im_sign(zmul(zconj(d), sub(third[frozenset(e)], s0)))
            partners = []
            if kd[0] == 'base':
                partners.append(twin(H))
            else:
                for G in pool:
                    for e2, kd2 in half_edges(G):
                        if kd2[0] != 'leg' or kd2[1] != kd[1]:
                            continue
                        tail2 = e2[0] if e2[1] == kd2[2] else e2[1]
                        tail1 = s0 if s1 == kd[2] else s1
                        tau = sub(kd[2], kd2[2])
                        if add(tail2, tau) != tail1:
                            continue
                        Gt = (G[0],) + tuple(add(v, tau) for v in G[1:])
                        th = [v for v in Gt[1:] if v not in (s0, s1)][0]
                        if im_sign(zmul(zconj(d), sub(th, s0))) == -side1:
                            partners.append(Gt)
            assert partners
            for G in partners:
                stats['contacts'] += 1
                def on_E(chs):
                    out = {}
                    for ch in chs:
                        for e3, kd3 in half_edges(ch):
                            if on_segment(e3[0], s0, s1) and on_segment(e3[1], s0, s1):
                                out[frozenset(e3)] = kd3
                    return out
                m1, m2 = on_E(children(H)), on_E(children(G))
                assert set(m1) == set(m2), ('partition mismatch', H, G)
                for ee in m1:
                    assert compatible(m1[ee], m2[ee]), ('kind mismatch', H, G, ee)
                    stats['child_edge_matches'] += 1
    return stats

# ------------------------------------------------------------- sanity test
def deflation_sanity(n=5):
    """On a Preshing sun deflated n times (exact, integer Z[w] coordinates,
    scaled by phi^n so children have unit edges), every child triangle whose
    parent rhomb is interior gets exactly one valid hypothesis, and it is its
    true parent.  (Validates formulas/conventions; not used in the proof.)"""
    def sun():
        tris = []
        for i in range(10):
            B, C = W(i), W(i + 1)
            if i % 2 == 0:
                B, C = C, B
            tris.append((0, ZERO, B, C))
        return tris
    def scale(T, f):
        return (T[0],) + tuple(f(x) for x in T[1:])
    tris = sun()
    for _ in range(n):
        tris = [scale(T, mulphi) for T in tris]       # parent tiling at scale phi
        tris = [ch for T in tris for ch in children(T)]
    # one more level, keeping track of parents
    parents_of = {}
    big = [scale(T, mulphi) for T in tris]
    small = set()
    for T in big:
        for ch in children(T):
            parents_of[ch] = T
            small.add(ch)
    bigset = set(big)
    checked = 0
    for t, T in parents_of.items():
        if twin(T) not in bigset:
            continue                                  # boundary parent rhomb
        hyp = [H for H, pv in parents(t)
               if all(ch in small for ch in children(H)) and all(ch in small for ch in children(twin(H)))]
        assert hyp == [T], (t, hyp, T)
        checked += 1
    return checked

# ------------------------------------------------------------- main
def main():
    outp = sys.argv[1] if len(sys.argv) > 1 else None
    raw = raw_stars()
    stars = prune(raw)
    print('raw stars', len(raw), 'viable', len(stars))
    for s in stars:
        print('  ', [c[1] for c in s], [c[0] for c in s])
    report = {'raw_star_count': len(raw),
              'viable_stars': [[list(c) for c in s] for s in stars],
              'per_star': []}
    total_patches = 0
    fails = []
    for st0 in stars:
        pats, nbrs = vertex_patches(stars, st0)
        total_patches += len(pats)
        nh_hist = {}
        twin_checks = 0
        for pat in pats:
            H = set()
            for rh in pat:
                H.update(halves(rh))
            at0 = [t for t in H if ZERO in t[1:]]
            for t in at0:
                valid1 = [(Hp, pv) for Hp, pv in parents(t) if all(ch in H for ch in children(Hp))]
                valid = [(Hp, pv) for Hp, pv in valid1 if all(ch in H for ch in children(twin(Hp)))]
                nh_hist[len(valid)] = nh_hist.get(len(valid), 0) + 1
                twin_checks += len(valid1)
                if len(valid) != 1:
                    fails.append({'star': [list(c) for c in st0], 't': str(t), 'nvalid': len(valid),
                                  'nvalid_without_twin': len(valid1)})
        rec_ = {'star': [list(c) for c in st0], 'neighbour_vertices': len(nbrs),
                'patches': len(pats), 'valid_parent_count_histogram': nh_hist,
                'twin_checks': twin_checks}
        print(rec_)
        report['per_star'].append(rec_)
    report['closure_check_R5'] = closure_check()
    print('R5 closure:', report['closure_check_R5'])
    report['deflation_legality_check_R6'] = deflation_legality_check()
    print('R6 deflation legality:', report['deflation_legality_check_R6'])
    report['deflation_sanity_children_checked'] = deflation_sanity(5)
    print('deflation sanity: children checked', report['deflation_sanity_children_checked'])
    report['total_patches'] = total_patches
    report['failures'] = fails
    print('total patches', total_patches, 'failures', len(fails))
    if fails:
        for f in fails[:20]:
            print(f)
    else:
        print('COMPOSITION CHECK PASSED')
    if outp:
        json.dump(report, open(outp, 'w'), indent=1, default=str)

if __name__ == '__main__':
    main()
