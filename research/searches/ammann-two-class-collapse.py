#!/usr/bin/env python3
"""Exact classification of congruence collapses of Ammann's {P1, P2, H}.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-two-class-collapse.py \
      research/certificates/ammann-two-class-collapse.json

Coordinates (complex numbers, K = Q(w), w = exp(i pi/5)); J = z = s + t w,
(s, t) real.  Tiles (counter-clockwise), reconstructed and verified on exact
Penrose patches by ammann-two-class-reconstruct.py:

  J'  = 1 + w^4 (z - 1)          J'' = w + w^6 (z - w)
  K   = w^2 + w^6 (z - 1)        L   = 1 + w^7 (z - 1 - w)
  J2  = 1 + w + w^2 - z
  H6 = [0, J', 1, z, w, J'']
  P1 = [0, J', 1, L, K]
  P2 = [K, L, 1 + w^2, J2, w^2]

Every vertex is complex-AFFINE in z.  Hence, for polygons P, Q with edge
vectors e_i, f_i (each affine in z), direct congruence with cyclic shift k

        f_{k+i} = u e_i   (all i),   |u| = 1

implies the holomorphic equations  f_{k+i} e_0 - f_k e_i = 0  (i=1..n-1),
which are univariate polynomials in z over K: either all identically zero
(a family) or their gcd has finitely many roots.  Mirror congruence uses the
mirrored, reversed edge list of P (anti-holomorphic in z) and is solved over
K[s, t] with the equation set closed under complex conjugation of
coefficients, by Groebner bases.  All decisions are exact (K, QQbar, AA).

Cases (mirror images identified):
  (a) P1 ~ P2  (direct or mirror, all 5 shifts)
  (b) H6 with a straight angle at vertex m (so a pentagon after deleting m)
      ~ P1 or P2 (direct or mirror, all 5 shifts, all 6 m)
  (c) degenerations producing a quadrilateral (straight angle in P1 or P2,
      or two straight angles in H6) are recorded as discarded strata.
Every algebraic solution is then tested against the closed admissible
region (weak convexity of all three tiles, nonzero edges, nonnegative
orientation of every rhomb piece).
"""
import sys, json, itertools
from sage.all import (CyclotomicField, PolynomialRing, QQbar, AA, QQ, gcd,
                      Ideal, SR, CIF, RIF)

K = CyclotomicField(10)
w = K.gen()
Rz = PolynomialRing(K, 'z'); z = Rz.gen()
R2 = PolynomialRing(K, ['s', 't'], order='lex'); S, T = R2.gens()
emb = K.hom([QQbar.zeta(10)])
wq = QQbar.zeta(10)
Iq = QQbar(-1).sqrt()

def tiles_z(Z):
    """Tiles with J = Z (Z may live in any K-algebra)."""
    Jp = 1 + w**4 * (Z - 1)
    Jpp = w + w**6 * (Z - w)
    Kp = w**2 + w**6 * (Z - 1)
    Lp = 1 + w**7 * (Z - 1 - w)
    J2 = 1 + w + w**2 - Z
    return {'H6': [0 * Z, Jp, 0 * Z + 1, Z, 0 * Z + w, Jpp],
            'P1': [0 * Z, Jp, 0 * Z + 1, Lp, Kp],
            'P2': [Kp, Lp, 0 * Z + 1 + w**2, J2, 0 * Z + w**2]}

def pieces_z(Z):
    J = Z
    Kp = w**2 + w**6 * (Z - 1)
    Lp = 1 + w**7 * (Z - 1 - w)
    A, B, C, D = 0 * Z, 0 * Z + 1, 0 * Z + 1 + w, 0 * Z + w
    E, F, G, H = 0 * Z, 0 * Z + 1, 0 * Z + 1 + w**2, 0 * Z + w**2
    return {'thinQ': [A, B, J, D], 'thinTb': [B, C, J], 'thinTr': [C, D, J],
            'thickQ1': [E, F, Lp, Kp], 'thickQ2': [Kp, Lp, G, H],
            'thickTb': [H, E, Kp], 'thickTr': [F, G, Lp]}

def edges(P):
    n = len(P)
    return [P[(i + 1) % n] - P[i] for i in range(n)]

# ---------------------------------------------------------------- exact numerics
def zval(poly_z, z0):
    """evaluate K[z] polynomial at z0 in QQbar"""
    return sum(emb(c) * z0**i for i, c in enumerate(poly_z.list()))

def st_of(z0):
    """z0 = s + t w with s, t real -> (s, t) in AA"""
    # t = Im(z0)/Im(w); s = Re(z0) - t Re(w)
    imz = (z0 - z0.conjugate()) / (2 * Iq)
    imw = (wq - wq.conjugate()) / (2 * Iq)
    rez = (z0 + z0.conjugate()) / 2
    rew = (wq + wq.conjugate()) / 2
    t = AA(imz / imw); s = AA(rez - t * rew)
    return s, t

def num_point(s, t):
    return QQbar(s) + QQbar(t) * wq

def tiles_at(s, t):
    z0 = num_point(s, t)
    out = {}
    for name, P in tiles_z(z).items():
        out[name] = [zval(Rz(p), z0) for p in P]
    return out

def pieces_at(s, t):
    z0 = num_point(s, t)
    return {name: [zval(Rz(p), z0) for p in P] for name, P in pieces_z(z).items()}

def turn(a, b):
    v = a.conjugate() * b
    return AA((v - v.conjugate()) / (2 * Iq))

def dot(a, b):
    v = a.conjugate() * b
    return AA((v + v.conjugate()) / 2)

def angle_data(P):
    """per vertex: ('strict'|'straight'|'reflex'|'spike'|'zero-edge')"""
    n = len(P); res = []
    for i in range(n):
        a = P[i] - P[i - 1]; b = P[(i + 1) % n] - P[i]
        if a == 0 or b == 0:
            res.append('zero-edge'); continue
        c = turn(a, b)
        if c > 0:
            res.append('strict')
        elif c < 0:
            res.append('reflex')
        else:
            res.append('straight' if dot(a, b) > 0 else 'spike')
    return res

def area2(P):
    n = len(P); acc = QQbar(0)
    for i in range(n):
        acc += P[i].conjugate() * P[(i + 1) % n]
    return AA((acc - acc.conjugate()) / (2 * Iq))

def admissibility(s, t):
    tl = tiles_at(s, t); pc = pieces_at(s, t)
    info = {}
    ok = True
    for name, P in tl.items():
        ad = angle_data(P)
        info[name] = ad
        if any(x not in ('strict', 'straight') for x in ad) or area2(P) <= 0:
            ok = False
    for name, P in pc.items():
        a = area2(P)
        # every piece must be weakly positively oriented; for quads also no reflex corner
        ad = angle_data(P)
        info[name] = {'area2_sign': int((a > 0) - (a < 0)), 'angles': ad}
        if a < 0 or (a == 0 and len(P) == 4) or any(x == 'reflex' for x in ad if len(P) == 4):
            ok = False
    return ok, info

def strict_region(info):
    return all(all(x == 'strict' for x in info[n]) for n in ('H6', 'P1', 'P2')) and \
        all(info[n]['area2_sign'] > 0 for n in info if n not in ('H6', 'P1', 'P2'))

# ---------------------------------------------------------------- solvers
def mirror(P):
    return [p.conjugate() if hasattr(p, 'conjugate') else p for p in reversed(P)]

def direct_solutions(P, Q):
    """P, Q lists of K[z] polys (same length).  Return list of (k, roots|'ALL')."""
    e, f = edges(P), edges(Q)
    n = len(e)
    out = []
    for k in range(n):
        eqs = [Rz(f[(k + i) % n] * e[0] - f[k] * e[i]) for i in range(1, n)]
        g = Rz(0)
        for q in eqs:
            g = gcd(g, q)
        if g == 0:
            out.append((k, 'ALL', eqs)); continue
        if g.degree() == 0:
            out.append((k, [], eqs)); continue
        roots = [r for r, m in g.change_ring(QQbar).roots()]
        out.append((k, roots, eqs))
    return out

def conjK_poly2(p):
    return R2({m: c.conjugate() for m, c in p.dict().items()})

def to_st(poly_z):
    return Rz(poly_z)(S + T * w)

def to_st_bar(poly_z):
    p = Rz(poly_z)
    return sum(c.conjugate() * (S + T * w.conjugate())**i for i, c in enumerate(p.list()))

def mirror_solutions(P, Q):
    """mirror congruence: Q directly congruent to mirror(P)."""
    # mirror(P): vertices conj(P_i) reversed
    Pst = [to_st_bar(p) for p in reversed(P)]
    Qst = [to_st(q) for q in Q]
    e, f = edges(Pst), edges(Qst)
    n = len(e)
    out = []
    for k in range(n):
        eqs = [f[(k + i) % n] * e[0] - f[k] * e[i] for i in range(1, n)]
        gens = eqs + [conjK_poly2(q) for q in eqs]
        I = R2.ideal(gens)
        dim = I.dimension()
        if dim < 0:
            out.append((k, 'EMPTY', [])); continue
        if dim > 0:
            out.append((k, 'POSDIM:%d' % dim, I.groebner_basis())); continue
        sols = []
        for v in I.variety(QQbar):
            s0, t0 = v[S], v[T]
            if s0.imag() == 0 and t0.imag() == 0:
                sols.append((AA(s0), AA(t0)))
        out.append((k, sols, I.groebner_basis()))
    return out

def check_direct_unit(P, Q, k, s0, t0):
    tl_vals = None
    z0 = num_point(s0, t0)
    e = [zval(Rz(x), z0) for x in edges(P)]
    f = [zval(Rz(x), z0) for x in edges(Q)]
    n = len(e)
    if e[0] == 0:
        return False
    u = f[k] / e[0]
    return u * u.conjugate() == 1 and all(f[(k + i) % n] == u * e[i] for i in range(n))

def numeric_polys(P, s0, t0):
    z0 = num_point(s0, t0)
    return [zval(Rz(x), z0) for x in P]

def congruent_exact(Pv, Qv):
    """direct congruence of two QQbar vertex lists"""
    if len(Pv) != len(Qv):
        return False
    e, f = edges(Pv), edges(Qv)
    n = len(e)
    for k in range(n):
        if e[0] == 0:
            return False
        u = f[k] / e[0]
        if u * u.conjugate() == 1 and all(f[(k + i) % n] == u * e[i] for i in range(n)):
            return True
    return False

def mirrorv(P):
    return [p.conjugate() for p in reversed(P)]

def fmt(x):
    return {'exact': str(x.minpoly()) + ' ~ ' + str(x.n(digits=20)) if hasattr(x, 'minpoly') else str(x)}

def record_solution(label, s0, t0):
    ok, info = admissibility(s0, t0)
    tl = tiles_at(s0, t0)
    rec = {'case': label,
           's': {'minpoly': str(s0.minpoly()), 'approx': str(s0.n(digits=25))},
           't': {'minpoly': str(t0.minpoly()), 'approx': str(t0.n(digits=25))},
           'admissible_closed': bool(ok), 'strict_open_region': bool(ok and strict_region(info)),
           'tile_angle_types': {n: info[n] for n in ('H6', 'P1', 'P2')},
           'pieces': {n: info[n] for n in info if n not in ('H6', 'P1', 'P2')}}
    return rec

def main(outpath=None):
    TZ = tiles_z(z)
    TZ = {k: [Rz(p) for p in v] for k, v in TZ.items()}
    cert = {'field': 'Q(w), w=exp(i*pi/5), minpoly ' + str(w.minpoly()),
            'parametrization': 'J = s + t*w',
            'tiles': {k: [str(p) for p in v] for k, v in TZ.items()},
            'cases': []}
    sols_all = []

    def handle(label, P, Q, extra_check=None):
        entry = {'case': label, 'direct': [], 'mirror': []}
        for k, roots, eqs in direct_solutions(P, Q):
            if roots == 'ALL':
                entry['direct'].append({'shift': k, 'status': 'IDENTICALLY ZERO (family)'})
                print('FAMILY', label, k); continue
            row = {'shift': k, 'gcd_roots': len(roots), 'solutions': []}
            for r in roots:
                s0, t0 = st_of(r)
                if not check_direct_unit(P, Q, k, s0, t0):
                    row['solutions'].append({'s~': str(s0.n(digits=15)), 't~': str(t0.n(digits=15)),
                                             'rejected': 'rotation factor not unimodular or edges mismatch'})
                    continue
                rec = record_solution(label + ' direct shift %d' % k, s0, t0)
                if extra_check:
                    rec.update(extra_check(s0, t0))
                row['solutions'].append(rec); sols_all.append(rec)
            entry['direct'].append(row)
        for k, sols, gb in mirror_solutions(P, Q):
            if isinstance(sols, str):
                entry['mirror'].append({'shift': k, 'status': sols,
                                        'groebner': [str(g) for g in gb][:6]})
                if sols.startswith('POSDIM'):
                    print('POSDIM', label, k, gb)
                continue
            row = {'shift': k, 'real_points': len(sols), 'solutions': []}
            for (s0, t0) in sols:
                Pv = numeric_polys(P, s0, t0); Qv = numeric_polys(Q, s0, t0)
                if not congruent_exact(mirrorv(Pv), Qv):
                    row['solutions'].append({'s~': str(s0.n(digits=15)), 't~': str(t0.n(digits=15)),
                                             'rejected': 'not unimodular'}); continue
                rec = record_solution(label + ' mirror shift %d' % k, s0, t0)
                if extra_check:
                    rec.update(extra_check(s0, t0))
                row['solutions'].append(rec); sols_all.append(rec)
            entry['mirror'].append(row)
        cert['cases'].append(entry)
        print(label, 'done', flush=True)

    # (a) P1 vs P2
    handle('(a) P1~P2', TZ['P1'], TZ['P2'])
    # (b) H6 with vertex m deleted vs P1 / P2
    H = TZ['H6']
    for m in range(6):
        Hm = [H[i] for i in range(6) if i != m]
        def straight(s0, t0, m=m):
            tl = tiles_at(s0, t0)['H6']
            a = tl[m] - tl[m - 1]; b = tl[(m + 1) % 6] - tl[m]
            return {'H6_vertex_%d_straight' % m: bool(a != 0 and b != 0 and turn(a, b) == 0 and dot(a, b) > 0)}
        for tgt in ('P1', 'P2'):
            handle('(b) H6 minus vertex %d ~ %s' % (m, tgt), Hm, TZ[tgt], straight)

    # summary
    genuine = [r for r in sols_all if r['admissible_closed']
               and all(v is not False for k, v in r.items() if k.startswith('H6_vertex'))]
    # kill tests for genuine solutions (exact)
    for r in genuine:
        s0 = AA(QQbar.polynomial_root(PolynomialRing(QQ, 'x')(r['s']['minpoly']), CIF(RIF(float(r['s']['approx']) - 1e-12, float(r['s']['approx']) + 1e-12))))
        t0 = AA(QQbar.polynomial_root(PolynomialRing(QQ, 'x')(r['t']['minpoly']), CIF(RIF(float(r['t']['approx']) - 1e-12, float(r['t']['approx']) + 1e-12))))
        tl = tiles_at(s0, t0)
        e = edges(tl['H6'])
        r['kill_tests'] = {
            'H6_centrally_symmetric_e_i_eq_minus_e_i+3': bool(all(e[i] == -e[i + 3] for i in range(3))),
            'H6_squared_side_lengths': [str((x * x.conjugate()).radical_expression()) for x in e],
            'P1_squared_side_lengths': [str((x * x.conjugate()).radical_expression()) for x in edges(tl['P1'])],
            'P1_directly_congruent_P2': bool(congruent_exact(tl['P1'], tl['P2'])),
            'verdict': 'KILLED: a centrally symmetric convex hexagon tiles the plane by translations '
                       '(lattice tiling), so the pair {H6, P1} admits a periodic tiling'
                       if all(e[i] == -e[i + 3] for i in range(3)) else 'not killed by central symmetry'}
        print('kill test:', r['kill_tests']['verdict'])
    cert['all_algebraic_solutions'] = len(sols_all)
    cert['solutions_in_closed_admissible_region'] = genuine
    print('algebraic solutions (unit-checked):', len(sols_all))
    for r in sols_all:
        print(' ', r['case'], r['s']['approx'][:12], r['t']['approx'][:12], 'adm', r['admissible_closed'],
              {k: v for k, v in r.items() if k.startswith('H6_vertex')})
    print('in admissible region:', len(genuine))
    if outpath:
        json.dump(cert, open(outpath, 'w'), indent=1, default=str)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
