#!/usr/bin/env sage -python
"""Exact angle / edge-length data for Ammann's three convex tiles, and the
complete list of vertex and T-junction angle relations for generic J.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/searches/ammann-forcing-angles.py \
      research/certificates/ammann-forcing-angles.json

What is checked (all exact unless marked "bound"):

 1. Tiles H6, P1, P2 as functions of the free point x = J (holomorphic affine
    in x over K = Q(w), w = exp(i pi/5)).
 2. Edge labels: every edge vector equals (unit constant) * (x - C), (x - B),
    (x - D) or (K(x) - L(x)), identically in x  ->  labels a, b, r, c.
 3. Corner ratios rho = (v_{i-1}-v_i)/(v_{i+1}-v_i) in K(x).  With the basic
    angles chi = H6 corner 1, psi = H6 corner 5, kappa = P1 corner 4, each of
    the 16 corners satisfies, identically in x,
        rho_j / (w^{c_j} rho_chi^p rho_psi^q rho_kappa^r) = positive constant,
    i.e. theta_j == 36 c_j + p chi + q psi + r kappa (mod 360) for every J at
    which the tiles are defined; the representative is then pinned using only
    0 < theta < 180 (strict convexity).  The pinning is done exactly by
    interval counting.
 4. At each of the five listed points: strict convexity, a,b,r,c pairwise
    distinct (exact in Q(sqrt5)), and a certificate that 1, chi/pi, psi/pi,
    kappa/pi are Q-linearly independent: the valuation vectors of
    w_theta = rho_theta / conj(rho_theta) (theta = chi, psi, kappa) at the
    prime ideals of K have rank 3 (all five matrices are stored).
 5. Every non-negative integer combination of the 16 corner angles that is
    IDENTICALLY 180 or 360 (as a linear form in 36deg, chi, psi, kappa).
    Exact completeness (no floats): an identical relation has zero chi, psi,
    kappa coefficients, so it holds with value 180 (resp. 360) for ANY values
    chi', psi', kappa'.  We substitute rational "dummy" values for which all
    16 corner values are positive rationals (checked exactly); then
    m_j <= target / theta'_j and partial sums <= target, all in Fractions.
    The enumeration is repeated with the five dummy triples obtained by
    rounding the true angles at the five listed points to 3 decimals (floats
    only CHOOSE the dummy; correctness needs only the exact positivity
    check); all five runs must return the same relation set.
 6. All cyclic vertex stars (corners with orientation 'd' direct / 'm'
    mirror, consecutive corners sharing an edge of equal length) for every
    identical 360 relation (162 stars up to rotation and global reflection).
 7. Edge-consistency pruning to a fixed point: a star survives only if, for
    each pair of consecutive corners (X, Y) sharing an edge, the far-end
    corners (Y', X') of that edge are consecutive in some surviving star.
    Result: 14 viable stars, all with a single orientation.
"""
import sys, json, itertools
from fractions import Fraction
from sage.all import (CyclotomicField, PolynomialRing, QQ, AA, QQbar, CC,
                      matrix, RealField, ZZ, floor)

K = CyclotomicField(10)
w = K.gen()
R = PolynomialRing(K, 'x')
x = R.gen()
F = R.fraction_field()
emb = K.hom([QQbar.zeta(10)])
RF = RealField(200)

def cj(z):
    return z.conjugate()

# ----------------------------------------------------------------- tiles
A, B, C, D = K(0), K(1), 1 + w, w
E, Fv, G, H = K(0), K(1), 1 + w**2, w**2
Kp = w**2 + w**6 * (x - 1)
Lp = 1 + w**7 * (x - 1 - w)
Jp = 1 + w**4 * (x - 1)
Jpp = w + w**6 * (x - w)
J2 = 1 + w + w**2 - x
TILES = {
    'H6': [R(A), Jp, R(B), x, R(D), Jpp],
    'P1': [R(E), Jp, R(Fv), Lp, Kp],
    'P2': [Kp, Lp, R(G), J2, R(H)],
}
VNAMES = {'H6': ['A', "J'", 'B', 'J', 'D', "J''"],
          'P1': ['E', "J'", 'F', 'L', 'K'],
          'P2': ['K', 'L', 'G', 'J2', 'H']}

def is_unit_constant(f):
    """f in F constant lambda with lambda*conj(lambda)==1 ?"""
    f = F(f)
    if f.numerator().degree() > 0 or f.denominator().degree() > 0:
        return False
    lam = K(f.numerator().constant_coefficient() / f.denominator().constant_coefficient())
    return lam * cj(lam) == 1

LABEL_VEC = {'a': x - C, 'b': x - B, 'r': x - D, 'c': Kp - Lp}

def edge_label(e):
    labs = [l for l, v in LABEL_VEC.items() if is_unit_constant(F(e) / F(v))]
    assert len(labs) == 1, labs
    return labs[0]

corners = []    # dicts
for tn, P in TILES.items():
    n = len(P)
    for i in range(n):
        nxt, prv = P[(i + 1) % n] - P[i], P[i - 1] - P[i]
        corners.append({'tile': tn, 'idx': i, 'name': tn + '-' + VNAMES[tn][i],
                        'rho': F(prv) / F(nxt),
                        'first': edge_label(nxt),    # cw ray of the corner (to next vertex)
                        'second': edge_label(prv)})  # ccw ray (to previous vertex)
cn = {c['name']: c for c in corners}
rho_chi, rho_psi, rho_kap = cn["H6-J'"]['rho'], cn["H6-J''"]['rho'], cn['P1-K']['rho']

# claimed coefficient vectors (c in units of 36 deg, p, q, r)
CLAIM = {
    'H6-A': (2, 0, 0, 0), "H6-J'": (0, 1, 0, 0), 'H6-B': (4, 0, 0, 0),
    'H6-J': (10, -1, -1, 0), 'H6-D': (4, 0, 0, 0), "H6-J''": (0, 0, 1, 0),
    'P1-E': (2, 0, 0, 0), "P1-J'": (0, 1, 0, 0), 'P1-F': (7, -1, 0, 0),
    'P1-L': (6, 0, 0, -1), 'P1-K': (0, 0, 0, 1),
    'P2-K': (10, -1, 0, -1), 'P2-L': (4, 0, -1, 1), 'P2-G': (2, 0, 0, 0),
    'P2-J2': (0, 0, 1, 0), 'P2-H': (-1, 1, 0, 0),
}

def positive_real_constant(f):
    f = F(f)
    if f.numerator().degree() > 0 or f.denominator().degree() > 0:
        return False
    lam = K(f.numerator().constant_coefficient() / f.denominator().constant_coefficient())
    if lam != cj(lam):
        return False
    return AA(emb(lam)) > 0

identity_report = []
for c in corners:
    cc, p, q, r = CLAIM[c['name']]
    ratio = c['rho'] / (F(w)**cc * rho_chi**p * rho_psi**q * rho_kap**r)
    ok_mod360 = positive_real_constant(ratio)
    # pin representative: theta - p chi - q psi - r kappa lies in open interval
    lo = 0 - sum(180 * max(v, 0) for v in (p, q, r))
    hi = 180 - sum(180 * min(v, 0) for v in (p, q, r))
    reps = [36 * cc + 360 * k for k in range(-5, 6) if lo < 36 * cc + 360 * k < hi]
    assert ok_mod360 and reps == [36 * cc], (c['name'], ok_mod360, reps)
    identity_report.append({'corner': c['name'], 'coeffs_36deg_chi_psi_kappa': [cc, p, q, r],
                            'edges_cw_ccw': [c['first'], c['second']],
                            'identity_mod360_exact': True, 'representative_pinned': True})
print('angle identities: all 16 corners verified identically in J')

# --------------------------------------------------------------- point J0
def at(f, J0):
    return K(F(f).numerator()(J0) / F(f).denominator()(J0))

def turn_pos(u, v):
    """Im(conj(u) v) > 0, exact"""
    z = cj(u) * v
    return AA(emb((z - cj(z)) / (w - cj(w)))) > 0

def check_point(s, t, verbose=True):
    J0 = K(s) + K(t) * w
    out = {'s': str(s), 't': str(t)}
    conv = {}
    for tn, P in TILES.items():
        V = [K(v(J0)) for v in P]
        n = len(V)
        conv[tn] = all(turn_pos(V[i] - V[i - 1], V[(i + 1) % n] - V[i]) for i in range(n))
    out['strictly_convex_ccw'] = conv
    L2 = {}
    for l, v in LABEL_VEC.items():
        z = at(v, J0)
        L2[l] = z * cj(z)
    out['lengths_sq'] = {l: str(v) for l, v in L2.items()}
    out['lengths_float'] = {l: float(AA(emb(v)).sqrt()) for l, v in L2.items()}
    out['lengths_pairwise_distinct'] = len(set(L2.values())) == 4
    return J0, out, all(conv.values())

def angles_deg(J0):
    vals = {}
    for c in corners:
        z = CC(emb(at(c['rho'], J0)))
        vals[c['name']] = float(RF(z.arg()) * 180 / RF.pi())
    return vals

def valuation_certificate(J0):
    ws = []
    for f in (rho_chi, rho_psi, rho_kap):
        z = at(f, J0)
        ws.append(z / cj(z))
    primes = []
    facs = []
    for v in ws:
        fa = K.fractional_ideal(v).factor()
        facs.append(fa)
        for P, e in fa:
            if P not in primes:
                primes.append(P)
    M = matrix(ZZ, [[dict((P, e) for P, e in fa).get(P, 0) for P in primes] for fa in facs])
    return M.rank(), M, primes

# ------------------------------------------------------------ relations
def dummy_from_angles(theta):
    """rational dummy (chi', psi', kappa') = true angles rounded to 3 decimals"""
    return tuple(Fraction(int(round(theta[nm] * 1000)), 1000) for nm in ("H6-J'", "H6-J''", 'P1-K'))

def identical_relations(dummy, target):
    """all m >= 0 with sum m_j coeff_j == (target/36, 0, 0, 0); exact."""
    names = [c['name'] for c in corners]
    coeff = [CLAIM[nm] for nm in names]
    chi_, psi_, kap_ = dummy
    val = [36 * cc + p * chi_ + q * psi_ + r * kap_ for (cc, p, q, r) in coeff]
    assert all(v > 0 for v in val), 'dummy angles must make every corner positive'
    T = Fraction(target)
    bound = [int(T // v) for v in val]
    sols = []
    def rec(i, acc, m, ang):
        if ang > T:
            return
        if i == len(names):
            if acc == (target // 36, 0, 0, 0):
                sols.append(dict((names[k], m[k]) for k in range(len(names)) if m[k]))
            return
        for k in range(bound[i] + 1):
            a2 = tuple(acc[j] + k * coeff[i][j] for j in range(4))
            rec(i + 1, a2, m + [k], ang + k * val[i])
    rec(0, (0, 0, 0, 0), [], Fraction(0))
    return sols

def stars_for(rel):
    """cyclic vertex stars: sequences of (corner, orientation) with matching edges"""
    multiset = []
    for nm, k in rel.items():
        multiset += [nm] * k
    n = len(multiset)
    found = set()
    out = []
    for perm in sorted(set(itertools.permutations(multiset))):
        for ori in itertools.product((0, 1), repeat=n):
            seq = []
            for nm, o in zip(perm, ori):
                c = cn[nm]
                e1, e2 = (c['first'], c['second']) if o == 0 else (c['second'], c['first'])
                seq.append((nm, 'd' if o == 0 else 'm', e1, e2))
            if all(seq[i][3] == seq[(i + 1) % n][2] for i in range(n)):
                # canonical form under rotation and global reflection
                variants = []
                for s2 in (seq, [(nm, 'm' if o == 'd' else 'd', e2, e1) for nm, o, e1, e2 in reversed(seq)]):
                    for k in range(n):
                        variants.append(tuple(s2[k:] + s2[:k]))
                key = min(variants)
                if key not in found:
                    found.add(key)
                    out.append([list(t) for t in key])
    return out

# ------------------------------------------------ edge-consistency pruning
NV = {'H6': 6, 'P1': 5, 'P2': 5}

def far(corner, ori, side):
    """far corner (name, ori) along the cw ('cw') or ccw ('ccw') ray"""
    tn, vn = corner.split('-', 1)
    i = VNAMES[tn].index(vn)
    step = {('d', 'cw'): 1, ('d', 'ccw'): -1, ('m', 'cw'): -1, ('m', 'ccw'): 1}[(ori, side)]
    j = (i + step) % NV[tn]
    return (tn + '-' + VNAMES[tn][j], ori)

def variants(star):
    seq = [tuple(c) for c in star]
    n = len(seq)
    out = []
    refl = [(nm, 'm' if o == 'd' else 'd', e2, e1) for nm, o, e1, e2 in reversed(seq)]
    for s2 in (seq, refl):
        for k in range(n):
            out.append(s2[k:] + s2[:k])
    return out

def consecutive_pairs(star):
    pairs = set()
    for v in variants(star):
        n = len(v)
        for i in range(n):
            pairs.add(((v[i][0], v[i][1]), (v[(i + 1) % n][0], v[(i + 1) % n][1])))
    return pairs

def prune(all_stars):
    """iterate: keep a star only if every consecutive pair (X,Y) has its far
    pair (Y', X') consecutive in some kept star"""
    alive = list(range(len(all_stars)))
    rounds = []
    while True:
        avail = set()
        for k in alive:
            avail |= consecutive_pairs(all_stars[k])
        new, killed = [], []
        for k in alive:
            st = all_stars[k]
            n = len(st)
            ok = True
            for i in range(n):
                X, Y = st[i], st[(i + 1) % n]
                Xp = far(X[0], X[1], 'ccw')
                Yp = far(Y[0], Y[1], 'cw')
                if (Yp, Xp) not in avail:
                    ok = False
                    killed.append({'star': st, 'pair': [X[:2], Y[:2]], 'missing_far_pair': [Yp, Xp]})
                    break
            if ok:
                new.append(k)
        rounds.append(killed)
        if len(new) == len(alive):
            return alive, rounds
        alive = new

if __name__ == '__main__':
    outpath = sys.argv[1] if len(sys.argv) > 1 else None
    s0, t0 = QQ(1) / 2, QQ(4) / 5
    cands = [(QQ(1) / 2, QQ(4) / 5), (QQ(9) / 20, QQ(3) / 4), (QQ(11) / 20, QQ(17) / 20),
             (QQ(3) / 7, QQ(5) / 6), (QQ(5) / 11, QQ(7) / 9)]
    chosen = None
    pts = []
    dummies = []
    for s, t in cands:
        J0, info, conv = check_point(s, t)
        rk, M, primes = valuation_certificate(J0)
        info['valuation_rank'] = int(rk)
        info['valuation_matrix_rows_chi_psi_kappa'] = [list(map(int, r)) for r in M.rows()]
        info['valuation_primes'] = [str(P.gens_two()) + ' norm ' + str(P.norm()) for P in primes]
        info['in_G'] = bool(conv and info['lengths_pairwise_distinct'] and rk == 3)
        th = angles_deg(J0)
        info['dummy_angles_chi_psi_kappa'] = [str(v) for v in dummy_from_angles(th)]
        dummies.append(dummy_from_angles(th))
        pts.append(info)
        print({k: v for k, v in info.items() if k != 'valuation_matrix_rows_chi_psi_kappa'})
        assert info['in_G']
        if chosen is None:
            chosen = (s, t, J0, info, M, primes)
    assert chosen is not None
    s, t, J0, info, M, primes = chosen
    theta = angles_deg(J0)
    print('J0 =', s, '+', t, 'w; angles:', {k: round(v, 6) for k, v in theta.items()})
    # numeric consistency of identities at J0
    chi, psi, kap = theta["H6-J'"], theta["H6-J''"], theta['P1-K']
    for nm, (cc, p, q, r) in CLAIM.items():
        assert abs(theta[nm] - (36 * cc + p * chi + q * psi + r * kap)) < 1e-9
    runs = []
    for dm in dummies:
        r180 = identical_relations(dm, 180)
        r360 = identical_relations(dm, 360)
        runs.append((r180, r360))
    key = lambda rl: sorted(tuple(sorted(x.items())) for x in rl)
    assert all(key(a) == key(runs[0][0]) and key(b) == key(runs[0][1]) for a, b in runs)
    rel180, rel360 = runs[0]
    multi_point = [{'dummy': [str(v) for v in dm], 'n180': len(a), 'n360': len(b)}
                   for dm, (a, b) in zip(dummies, runs)]
    print('exact relation enumeration at 5 dummy triples:', multi_point)
    print('identical 180-relations:', rel180)
    print('identical 360-relations:', len(rel360))
    star_list = []
    for rel in rel360:
        st = stars_for(rel)
        star_list.append({'relation': rel, 'stars': st})
        print(rel, '->', len(st), 'stars')
    all_stars = [s_ for e in star_list for s_ in e['stars']]
    alive, rounds = prune(all_stars)
    print('stars total', len(all_stars), 'viable after edge-consistency pruning', len(alive),
          'rounds', [len(r) for r in rounds])
    viable = [all_stars[k] for k in alive]
    for r_ in rounds:
        for kk in r_:
            if any(c[0] in ('P1-K', 'P1-L', 'P2-K', 'P2-L', 'H6-J') for c in kk['star']):
                print('  killed', [(c[0], c[1]) for c in kk['star']], 'missing', kk['missing_far_pair'])
    # the corners that matter for the reconstruction
    special = ['H6-J', 'P1-K', 'P1-L', 'P2-K', 'P2-L', "H6-J'", "P1-J'", "H6-J''", 'P2-J2']
    spec = {}
    for nm in special:
        rels = [r for r in rel360 if nm in r]
        stars = [s_ for s_ in viable if any(c[0] == nm for c in s_)]
        spec[nm] = {'relations': rels, 'stars': stars}
        print(nm, rels, len(stars))
    cert = {
        'field': 'K = Q(w), w = exp(i pi/5) = CyclotomicField(10).gen()',
        'tiles': {k: [str(v) for v in P] for k, P in TILES.items()},
        'corner_identities': identity_report,
        'points_tested': pts,
        'J0': {'s': str(s), 't': str(t), 'info': info,
               'valuation_matrix': [list(map(int, r)) for r in M.rows()],
               'primes': [str(P.gens_two()) + ' norm ' + str(P.norm()) for P in primes],
               'angles_deg_float': theta},
        'relation_enumeration_cross_check': multi_point,
        'identical_180_relations': rel180,
        'identical_360_relations_with_stars': star_list,
        'special_corners_viable': spec,
        'viable_stars': viable,
        'pruning_rounds': rounds,
    }
    if outpath:
        json.dump(cert, open(outpath, 'w'), indent=1, default=str)
    print('DONE')
