#!/usr/bin/env python3
"""Independent hostile check of Lemma 5 of
research/lemmas/ammann-forcing-aperiodicity.md (regrouping Ammann tiles into
marked rhombs, and the converse decoration).

Exact arithmetic in Q(w), w = exp(i pi/5) (rational 4-vectors, basis 1,w,w^2,w^3,
w^4 = -1 + w - w^2 + w^3).  Tile formulas are re-typed from
research/lemmas/ammann-two-class-reconstruction.md; no author code is imported.

Checks, at several sample J (vertex formulas are complex-affine in J, so an
identity between two such points that holds at two distinct J holds for all J):
 (a) piece congruences: X-triangles of H6 and P1, BCJ and HEK are directly
     congruent with matching 'a-ends'; same for Y-triangles of H6, P2, CDJ, FGL.
 (b) star assembly: walking around each of the six J/K/L-type vertex stars
     listed in Lemma 4 (corners glued along full edges, ccw), the pieces
     land exactly as Lemma 5 says: the thin group is A,B,C,D with triangles
     BCJ (a-end C) and CDJ (a-end C); the thick group is E,F,G,H with the P2
     quad in standard position and triangles HEK (a-end E), FGL (a-end F).
 (c) decoration (existence direction): for every rhomb edge, the marks say on
     which side the quad lies; the triangle supplied by any legal neighbour
     (thin or thick) is exactly the triangle of H6/P1/P2 on that edge.
 (d) area: quad + triangles = rhomb area; J, K, L strictly inside the rhombs.
"""
from fractions import Fraction as Fr
import sys

# ------------------------------------------------------------- Q(w)
def V(*c): return tuple(Fr(x) for x in c) + (Fr(0),) * (4 - len(c))
def add(u, v): return tuple(a + b for a, b in zip(u, v))
def sub(u, v): return tuple(a - b for a, b in zip(u, v))
def sc(f, u): return tuple(Fr(f) * a for a in u)
def tw(u):
    a, b, c, d = u
    return (-d, a + d, b - d, c + d)
def mul(u, v):
    r = V(); p = v
    for i in range(4):
        r = add(r, sc(u[i], p)); p = tw(p)
    return r
ONE = V(1); ZERO = V()
def W(k):
    u = ONE
    for _ in range(k % 10): u = tw(u)
    return u
def galois(u, m):     # w -> w^m
    r = ZERO
    for i in range(4):
        r = add(r, sc(u[i], W(m * i)))
    return r
def inv(u):
    # u^{-1} = prod_{m in 3,7,9} sigma_m(u) / N(u)
    p = mul(mul(galois(u, 3), galois(u, 7)), galois(u, 9))
    n = mul(u, p)
    assert n[1] == n[2] == n[3] == 0 and n[0] != 0
    return sc(1 / n[0], p)
def div(u, v): return mul(u, inv(v))
def conj(u): return galois(u, 9)
def sgn_q5(a, b):
    if b == 0: return (a > 0) - (a < 0)
    if a == 0: return (b > 0) - (b < 0)
    if (a > 0) == (b > 0): return 1 if a > 0 else -1
    d = a * a - 5 * b * b
    if d == 0: return 0
    return (1 if a > 0 else -1) if d > 0 else (1 if b > 0 else -1)
def im_coef(u):       # Im(u) = sin36 * (c1 + phi (c2 + c3)) -> return (a, b) with value a + b sqrt5
    c0, c1, c2, c3 = u
    s = c2 + c3
    return (c1 + s / 2, s / 2)
def im_sign(u): return sgn_q5(*im_coef(u))
def is_unit_modulus(u): return mul(u, conj(u)) == ONE
def area2(poly):      # 2*area / sin36 as (a, b) in Q(sqrt5)
    A = Fr(0); B = Fr(0)
    for i in range(len(poly)):
        a, b = im_coef(mul(conj(poly[i]), poly[(i + 1) % len(poly)]))
        A += a; B += b
    return (A, B)
assert all(im_sign(W(k)) == (1 if 0 < k < 5 else (-1 if k > 5 else 0)) for k in range(10))
assert mul(div(V(3, 1, -2, 5), V(1, 1, 0, 2)), V(1, 1, 0, 2)) == V(3, 1, -2, 5)

# ------------------------------------------------------------- data
w = W(1)
A_, B_, C_, D_ = ZERO, ONE, add(ONE, w), w                  # thin
E_, F_, G_, H_ = ZERO, ONE, add(ONE, W(2)), W(2)            # thick

def tiles(J):
    K = add(W(2), mul(W(6), sub(J, ONE)))
    L = add(ONE, mul(W(7), sub(sub(J, ONE), w)))
    Jp = add(ONE, mul(W(4), sub(J, ONE)))
    Jpp = add(w, mul(W(6), sub(J, w)))
    J2 = sub(add(add(ONE, w), W(2)), J)
    T = {
        'H6': (['A', "J'", 'B', 'J', 'D', "J''"], [ZERO, Jp, ONE, J, w, Jpp]),
        'P1': (['E', "J'", 'F', 'L', 'K'], [ZERO, Jp, ONE, L, K]),
        'P2': (['K', 'L', 'G', 'J2', 'H'], [K, L, add(ONE, W(2)), J2, W(2)]),
    }
    return T, K, L

def iso(p0, q0, p1, q1):
    """direct isometry mapping p0->p1, q0->q1 (requires equal lengths)"""
    u = div(sub(q1, p1), sub(q0, p0))
    assert is_unit_modulus(u), 'edge lengths differ'
    return lambda z: add(p1, mul(u, sub(z, p0)))

def strictly_convex_ccw(P):
    n = len(P)
    return all(im_sign(mul(conj(sub(P[(i + 1) % n], P[i])), sub(P[(i + 2) % n], P[(i + 1) % n]))) > 0
               for i in range(n))

def inside(z, P):
    n = len(P)
    return all(im_sign(mul(conj(sub(P[(i + 1) % n], P[i])), sub(z, P[i]))) > 0 for i in range(n))

# ------------------------------------------------------------- checks
def check(J, log):
    T, K, L = tiles(J)
    ok = True
    def need(c, msg):
        nonlocal ok
        if not c:
            ok = False
            log.append('FAIL ' + msg)
    for nm, (labs, P) in T.items():
        need(strictly_convex_ccw(P), nm + ' not strictly convex ccw')
    need(inside(J, [A_, B_, C_, D_]), 'J not inside thin')
    need(inside(K, [E_, F_, G_, H_]) and inside(L, [E_, F_, G_, H_]), 'K/L not inside thick')
    for q in ([A_, B_, J, D_], [B_, C_, J], [C_, D_, J], [E_, F_, L, K], [K, L, G_, H_], [H_, E_, K], [F_, G_, L]):
        need(strictly_convex_ccw(q), 'piece not ccw convex %r' % (q,))
    # (d) areas
    def asum(*ps):
        a = Fr(0); b = Fr(0)
        for p in ps:
            x, y = area2(p); a += x; b += y
        return (a, b)
    need(asum([A_, B_, J, D_], [B_, C_, J], [C_, D_, J]) == area2([A_, B_, C_, D_]), 'thin area')
    need(asum([E_, F_, L, K], [K, L, G_, H_], [H_, E_, K], [F_, G_, L]) == area2([E_, F_, G_, H_]), 'thick area')
    # tile = pieces (H6 = quad ABJD + tri(A,J',B) + tri(D,J'',A)) : area identity
    H6 = T['H6'][1]; P1 = T['P1'][1]; P2 = T['P2'][1]
    need(area2(H6) == asum([A_, B_, J, D_], [A_, H6[1], B_], [D_, H6[5], A_]), 'H6 = pieces')
    need(area2(P1) == asum([E_, F_, L, K], [E_, P1[1], F_]), 'P1 = pieces')
    need(area2(P2) == asum([K, L, G_, H_], [G_, P2[3], H_]), 'P2 = pieces')

    # (a) congruences: X triangle prototype (a-end, apex, b-end) = (C, J, B) ; Y = (C, J, D)
    X = (C_, J, B_); Y = (C_, J, D_)
    def congruent(tri, proto):
        f = iso(proto[0], proto[2], tri[0], tri[2])
        return f(proto[1]) == tri[1]
    need(congruent((A_, H6[1], B_), X), 'H6 X-tri')
    need(congruent((E_, P1[1], F_), X), 'P1 X-tri')
    need(congruent((E_, K, H_), X), 'thick HEK as X (a-end E)')
    need(congruent((A_, H6[5], D_), Y), 'H6 Y-tri (a-end A)')
    need(congruent((H_, P2[3], G_), Y), 'P2 Y-tri (a-end H)')
    need(congruent((F_, L, G_), Y), 'thick FGL as Y (a-end F)')
    # a-end really is the end at distance a=|CJ| (not b or r): lengths are distinct at generic J
    a2 = mul(sub(J, C_), conj(sub(J, C_))); b2 = mul(sub(J, B_), conj(sub(J, B_)))
    r2 = mul(sub(J, D_), conj(sub(J, D_))); c2 = mul(sub(K, L), conj(sub(K, L)))
    need(len({a2, b2, r2, c2}) == 4, 'G1 lengths not distinct')

    # (b) star assembly
    def walk(star, first_place):
        """star: list of (tile, label) ccw; first tile placed by first_place
        (dict label->point).  returns list of placed tiles (label->point)."""
        placed = [first_place]
        center = first_place[star[0][1]]
        for idx in range(1, len(star)):
            prev_t, prev_l = star[idx - 1]
            labs_p = T[prev_t][0]
            i = labs_p.index(prev_l)
            ray = placed[-1][labs_p[i - 1]]          # ccw ray of previous corner -> previous vertex
            tnm, lab = star[idx]
            labs, P = T[tnm]
            j = labs.index(lab)
            f = iso(P[j], P[(j + 1) % len(P)], center, ray)   # cw ray (next vertex) onto it
            placed.append({labs[m]: f(P[m]) for m in range(len(P))})
        # closure: ccw ray of last = cw ray of first
        lt, ll = star[-1]
        labs = T[lt][0]; i = labs.index(ll)
        ft, fl = star[0]
        labs0 = T[ft][0]; i0 = labs0.index(fl)
        closed = placed[-1][labs[i - 1]] == placed[0][labs0[(i0 + 1) % len(labs0)]]
        return placed, closed
    std = {nm: dict(zip(T[nm][0], T[nm][1])) for nm in T}
    # J-type
    for third in (('P2', 'J2'), ('H6', "J''")):
        st = [('H6', 'J'), ('P1', "J'"), third]
        pl, closed = walk(st, std['H6'])
        need(closed, 'J star not closed %r' % (st,))
        p1 = pl[1]
        need((p1['E'], p1["J'"], p1['F']) == (C_, J, B_), 'J star: X triangle is not BCJ with a-end C %r' % (st,))
        t3 = pl[2]
        if third[0] == 'P2':
            need((t3['H'], t3['J2'], t3['G']) == (C_, J, D_), 'J star: Y triangle (P2) not CDJ')
        else:
            need((t3['A'], t3["J''"], t3['D']) == (C_, J, D_), 'J star: Y triangle (H6) not CDJ')
        log.append('J-star %s closed=%s' % ([x[0] + '-' + x[1] for x in st], closed))
    # K-type: start at P1-K standard; ccw order [chi, P1-K, P2-K] -> rotate to start with P1-K
    for chi in (('P1', "J'"), ('H6', "J'")):
        st = [('P1', 'K'), ('P2', 'K'), chi]
        pl, closed = walk(st, std['P1'])
        need(closed, 'K star not closed')
        need(pl[1] == std['P2'], 'K star: P2 not in standard position (quad KLGH)')
        x = pl[2]
        if chi[0] == 'P1':
            tri = (x['E'], x["J'"], x['F'])
        else:
            tri = (x['A'], x["J'"], x['B'])
        need(tri == (E_, K, H_), 'K star: X triangle not HEK with a-end E: %r' % (chi,))
        log.append('K-star %s closed=%s' % ([x[0] + '-' + x[1] for x in st], closed))
    # L-type: [P1-L, P2-J2, P2-L] and [H6-J'', P2-L, P1-L]; start at P1-L
    for st in ([('P1', 'L'), ('P2', 'J2'), ('P2', 'L')], [('P1', 'L'), ('H6', "J''"), ('P2', 'L')]):
        pl, closed = walk(st, std['P1'])
        need(closed, 'L star not closed')
        need(pl[2] == std['P2'], 'L star: P2 not standard')
        x = pl[1]
        if st[1][0] == 'P2':
            tri = (x['H'], x['J2'], x['G'])
        else:
            tri = (x['A'], x["J''"], x['D'])
        need(tri == (F_, L, G_), 'L star: Y triangle not FGL with a-end F')
        log.append('L-star %s closed=%s' % ([x[0] + '-' + x[1] for x in st], closed))

    # (c) decoration across every edge.  Marked edges with the side of the quad:
    # thin  X A->B quad-left, X C->B tri-right?  Determine from geometry.
    MK = {'thin': [('X', 'A', 'B'), ('X', 'C', 'B'), ('Y', 'A', 'D'), ('Y', 'C', 'D')],
          'thick': [('X', 'E', 'F'), ('X', 'E', 'H'), ('Y', 'F', 'G'), ('Y', 'H', 'G')]}
    RH = {'thin': {'A': A_, 'B': B_, 'C': C_, 'D': D_}, 'thick': {'E': E_, 'F': F_, 'G': G_, 'H': H_}}
    # pieces adjacent to each rhomb edge: quad or triangle (with the triangle's apex)
    TRI = {('thin', 'B', 'C'): J, ('thin', 'C', 'D'): J, ('thick', 'E', 'H'): K, ('thick', 'F', 'G'): L}
    def side(kind, t, a, b):
        # +1 if rhomb interior is left of directed edge a->b
        R = RH[kind]
        other = [R[x] for x in R if x not in (a, b)]
        return im_sign(mul(conj(sub(R[b], R[a])), sub(other[0], R[a])))
    def tri_on(kind, a, b):
        for (k2, p, q), apex in TRI.items():
            if k2 == kind and {p, q} == {a, b}:
                return apex
        return None
    combos = 0
    for k1 in MK:
        for t1, a1, b1 in MK[k1]:
            for k2 in MK:
                for t2, a2_, b2_ in MK[k2]:
                    if t1 != t2:
                        continue
                    s1, s2 = side(k1, t1, a1, b1), side(k2, t2, a2_, b2_)
                    if s1 == s2:
                        continue         # same side: cannot be glued (would overlap)
                    combos += 1
                    q1, q2 = tri_on(k1, a1, b1) is None, tri_on(k2, a2_, b2_) is None
                    need(q1 != q2, 'edge %s%s/%s%s: quad|quad or tri|tri' % (k1, a1 + b1, k2, a2_ + b2_))
                    # rhomb 1 has the quad: neighbour 2 glued by the direct isometry tail->tail, head->head
                    if q1:
                        kq, aq, bq, kt, at, bt = k1, a1, b1, k2, a2_, b2_
                    else:
                        kq, aq, bq, kt, at, bt = k2, a2_, b2_, k1, a1, b1
                    f = iso(RH[kt][at], RH[kt][bt], RH[kq][aq], RH[kq][bq])
                    apex = f(tri_on(kt, at, bt))
                    # which tile owns that quad-edge, and its apex
                    exp = {('thin', 'A', 'B'): H6[1], ('thin', 'A', 'D'): H6[5],
                           ('thick', 'E', 'F'): P1[1], ('thick', 'H', 'G'): P2[3]}[(kq, aq, bq)]
                    need(apex == exp, 'decoration apex mismatch on %s %s->%s from %s' % (kq, aq, bq, kt))
    log.append('edge gluings checked: %d' % combos)
    return ok

def main():
    log = []
    samples = [(Fr(1, 2), Fr(4, 5)), (Fr(9, 20), Fr(3, 4)), (Fr(11, 20), Fr(17, 20)),
               (Fr(3, 7), Fr(5, 6)), (Fr(5, 11), Fr(7, 9))]
    allok = True
    for s, t in samples:
        J = add(V(s), sc(t, W(1)))
        log.append('--- J = %s + %s w' % (s, t))
        ok = check(J, log)
        log.append('ok' if ok else 'FAILED')
        allok &= ok
    print('\n'.join(log))
    print('ALL PIECE CHECKS PASSED' if allok else 'SOME PIECE CHECK FAILED')
    if len(sys.argv) > 1:
        open(sys.argv[1], 'w').write('\n'.join(log) + '\n')

if __name__ == '__main__':
    main()
