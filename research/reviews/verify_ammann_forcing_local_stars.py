#!/usr/bin/env python3
"""Independent hostile re-check of Lemmas 1-4 (local part) of
research/lemmas/ammann-forcing-aperiodicity.md.

Written from the lemma statements only; imports nothing from research/searches.

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/reviews/verify_ammann_forcing_local_stars.py [s t]
  (default point s=1/2, t=4/5; reviewer also ran s=9/20, t=3/4)

Every decision is exact:
 * tiles / edges / corner ratios live in K(x), K = Q(zeta10), x = J;
 * corner-angle coefficient vectors are DERIVED by search (not copied);
 * the multiplicity bound uses a rational "dummy angle" vector chosen so
   that every corner value is a positive rational; since an identical
   relation has zero chi/psi/kappa coefficients, it sums to 180/360 for ANY
   choice of the dummy angles, so the bound is rigorous with no floats;
 * stars and pruning are pure combinatorics.
"""
import sys, itertools
from fractions import Fraction as Fr
from sage.all import CyclotomicField, PolynomialRing, QQ, AA, QQbar, RealField, matrix, ZZ

K = CyclotomicField(10)
w = K.gen()
emb = K.hom([QQbar.zeta(10)])
R = PolynomialRing(K, 'x')
x = R.gen()
Fx = R.fraction_field()


def conj(z):
    return z.conjugate()


# ---------------------------------------------------------------- tiles (task statement)
Kv = w**2 + w**6 * (x - 1)
Lv = 1 + w**7 * (x - 1 - w)
J1 = 1 + w**4 * (x - 1)          # J'
J2p = w + w**6 * (x - w)         # J''
J2 = 1 + w + w**2 - x
TILES = {
    'H6': ([R(0), J1, R(1), x, R(w), J2p], ['A', "J'", 'B', 'J', 'D', "J''"]),
    'P1': ([R(0), J1, R(1), Lv, Kv], ['E', "J'", 'F', 'L', 'K']),
    'P2': ([Kv, Lv, R(1 + w**2), J2, R(w**2)], ['K', 'L', 'G', 'J2', 'H']),
}
BASE = {'a': x - (1 + w), 'b': x - 1, 'r': x - w, 'c': Kv - Lv}


def const_of(f):
    f = Fx(f)
    if f.numerator().degree() > 0 or f.denominator().degree() > 0:
        return None
    return K(f.numerator().constant_coefficient() / f.denominator().constant_coefficient())


def is_pos_real(lam):
    return lam == conj(lam) and AA(emb(lam)) > 0


def label(e):
    hits = []
    for l, v in BASE.items():
        lam = const_of(Fx(e) / Fx(v))
        if lam is not None and lam * conj(lam) == 1:
            hits.append(l)
    assert len(hits) == 1, hits
    return hits[0]


CORNERS = {}   # name -> dict
ORDER = []
for tn, (P, names) in TILES.items():
    n = len(P)
    for i in range(n):
        nxt = P[(i + 1) % n] - P[i]
        prv = P[i - 1] - P[i]
        nm = tn + '-' + names[i]
        CORNERS[nm] = dict(tile=tn, idx=i, n=n, rho=Fx(prv) / Fx(nxt),
                           cw=label(nxt), ccw=label(prv))
        ORDER.append(nm)
side_cycles = {}
for tn, (P, names) in TILES.items():
    n = len(P)
    side_cycles[tn] = [label(P[(i + 1) % n] - P[i]) for i in range(n)]
print('side cycles', side_cycles)
assert side_cycles == {'H6': list('abbrra'), 'P1': list('abaca'), 'P2': list('crrab')}

# ---------------------------------------------------------------- L1: derive coefficients
rc, rp, rk = CORNERS["H6-J'"]['rho'], CORNERS["H6-J''"]['rho'], CORNERS['P1-K']['rho']
COEF = {}
for nm in ORDER:
    sols = []
    for c in range(10):
        for p, q, r in itertools.product(range(-2, 3), repeat=3):
            lam = const_of(CORNERS[nm]['rho'] / (Fx(w)**c * rc**p * rp**q * rk**r))
            if lam is not None and is_pos_real(lam):
                sols.append((c, p, q, r))
    # mod-360 identity theta == 36c + p chi + q psi + r kappa ; pin representative with
    # 0<theta<180 and 0<chi,psi,kappa<180 : theta - (p chi+q psi+r kappa) in (lo, hi)
    pinned = []
    for (c, p, q, r) in sols:
        lo = -180 * sum(max(v, 0) for v in (p, q, r))
        hi = 180 - 180 * sum(min(v, 0) for v in (p, q, r))
        reps = [36 * c + 360 * k for k in range(-6, 7) if lo < 36 * c + 360 * k < hi]
        if len(reps) == 1:
            pinned.append((reps[0] // 36, p, q, r))
    pinned = sorted(set(pinned), key=lambda v: (sum(map(abs, v[1:])), v))
    assert pinned, nm
    COEF[nm] = pinned[0]     # simplest identity; others are consequences (checked below)
    CORNERS[nm]['all_identities'] = pinned
CLAIM = {
    'H6-A': (2, 0, 0, 0), 'P1-E': (2, 0, 0, 0), 'P2-G': (2, 0, 0, 0),
    'H6-B': (4, 0, 0, 0), 'H6-D': (4, 0, 0, 0),
    "H6-J'": (0, 1, 0, 0), "P1-J'": (0, 1, 0, 0),
    "H6-J''": (0, 0, 1, 0), 'P2-J2': (0, 0, 1, 0),
    'H6-J': (10, -1, -1, 0), 'P1-F': (7, -1, 0, 0), 'P2-H': (-1, 1, 0, 0),
    'P1-K': (0, 0, 0, 1), 'P1-L': (6, 0, 0, -1), 'P2-K': (10, -1, 0, -1),
    'P2-L': (4, 0, -1, 1),
}
CLAIM_EDGES = {
    'H6-A': ('a', 'a'), 'P1-E': ('a', 'a'), 'P2-G': ('r', 'r'), 'H6-B': ('b', 'b'),
    'H6-D': ('r', 'r'), "H6-J'": ('b', 'a'), "P1-J'": ('b', 'a'), "H6-J''": ('a', 'r'),
    'P2-J2': ('a', 'r'), 'H6-J': ('r', 'b'), 'P1-F': ('a', 'b'), 'P2-H': ('b', 'a'),
    'P1-K': ('a', 'c'), 'P1-L': ('c', 'a'), 'P2-K': ('c', 'b'), 'P2-L': ('r', 'c'),
}
for nm in ORDER:
    ok_c = CLAIM[nm] in CORNERS[nm]['all_identities']
    ok_e = CLAIM_EDGES[nm] == (CORNERS[nm]['cw'], CORNERS[nm]['ccw'])
    print('L1', nm, 'derived', CORNERS[nm]['all_identities'], 'claim ok', ok_c, 'edges ok', ok_e)
    assert ok_c and ok_e
# the three basic angles are not multiplicatively related identically (else the
# coefficient vectors would not be unique); unique derived identity per corner:
assert all(len(CORNERS[nm]['all_identities']) == 1 for nm in ORDER)
print('L1: all 16 identities confirmed and unique within |p|,|q|,|r|<=2')

# ---------------------------------------------------------------- point checks
s0 = QQ(sys.argv[1]) if len(sys.argv) > 2 else QQ(1) / 2
t0 = QQ(sys.argv[2]) if len(sys.argv) > 2 else QQ(4) / 5
J0 = K(s0) + K(t0) * w


def ev(f):
    f = Fx(f)
    return K(f.numerator()(J0) / f.denominator()(J0))


def im_pos(z):          # Im z > 0 exactly
    return AA(emb((z - conj(z)) / (w - conj(w)))) > 0


for tn, (P, names) in TILES.items():
    V = [K(v(J0)) for v in P]
    n = len(V)
    assert all(im_pos(conj(V[i] - V[i - 1]) * (V[(i + 1) % n] - V[i])) for i in range(n)), tn
    # also: simple polygon (convex + total turning 360 deg): sum of exterior angles check via
    # the product of normalized turn ratios being 1 is automatic; check winding numerically
print('point', s0, t0, ': all three tiles strictly convex, ccw (exact)')
L2 = {l: ev(v) * conj(ev(v)) for l, v in BASE.items()}
assert len(set(L2.values())) == 4
print('(G1) exact: a^2,b^2,r^2,c^2 pairwise distinct:', {l: str(v) for l, v in L2.items()})
assert 0 < s0 < 1 and 0 < t0 < 1

# (G2) via valuations, own code path: primes_above of norms
wvals = []
for nm in ("H6-J'", "H6-J''", 'P1-K'):
    z = ev(CORNERS[nm]['rho'])
    wvals.append(z / conj(z))
ps = set()
for nm in ("H6-J'", "H6-J''", 'P1-K'):
    z = ev(CORNERS[nm]['rho'])     # primes of w=z/conj(z) divide N(z) (N(w)=1 always)
    for fac in (z.norm().numerator(), z.norm().denominator()):
        ps |= set(ZZ(fac).prime_factors())
primes = [P for p in sorted(ps) for P in K.primes_above(p)]
M = matrix(ZZ, [[u.valuation(P) for P in primes] for u in wvals])
print('(G2) rational primes under the valuations:', sorted(ps), ' rank =', M.rank())
assert M.rank() == 3
# a relation n0*pi + n1 chi + n2 psi + n3 kappa = 0 forces prod w_j^{n_j} = 1,
# whose valuation vector n*M must vanish; rank 3 -> n=0 -> n0=0.

# numeric angles (sanity only)
import cmath
num = {}
for nm in ORDER:
    z = complex(emb(ev(CORNERS[nm]['rho'])))
    num[nm] = cmath.phase(z) * 180 / cmath.pi
chi, psi, kap = num["H6-J'"], num["H6-J''"], num['P1-K']
for nm in ORDER:
    c, p, q, r = CLAIM[nm]
    assert abs(num[nm] - (36 * c + p * chi + q * psi + r * kap)) < 1e-9
print('numeric chi psi kappa (deg):', chi, psi, kap)

# ---------------------------------------------------------------- exact multiplicity bound
# dummy rational basic angles: any values making all 16 corner values positive work.
dch, dps, dka = (Fr(round(v * 1000), 1000) for v in (chi, psi, kap))
TH = {}
for nm in ORDER:
    c, p, q, r = COEF[nm]
    TH[nm] = 36 * c + p * dch + q * dps + r * dka
    assert TH[nm] > 0
print('dummy rational angles', dch, dps, dka, 'all corner values > 0')


def relations(target):
    names = ORDER
    out = []

    def rec(i, m, acc, tot):
        if tot > target:
            return
        if i == len(names):
            if tot == target and acc == (target // 36, 0, 0, 0):
                out.append({names[k]: m[k] for k in range(len(names)) if m[k]})
            return
        nm = names[i]
        k = 0
        while tot + k * TH[nm] <= target:
            cc = COEF[nm]
            rec(i + 1, m + [k], tuple(acc[j] + k * cc[j] for j in range(4)), tot + k * TH[nm])
            k += 1
    rec(0, [], (0, 0, 0, 0), Fr(0))
    return out


rel180 = relations(180)
rel360 = relations(360)
print('L2: identical 180-relations:', len(rel180), rel180)
print('L3: identical 360-relations:', len(rel360))
# NB tot==target is implied by acc==(target/36,0,0,0); kept as a redundant exact check.

# ---------------------------------------------------------------- stars
FLIP = {'d': 'm', 'm': 'd'}


def rays(nm, o):
    c = CORNERS[nm]
    return (c['cw'], c['ccw']) if o == 'd' else (c['ccw'], c['cw'])


def reflect(st):
    return tuple((nm, FLIP[o]) for nm, o in reversed(st))


def rotations(st):
    return [st[k:] + st[:k] for k in range(len(st))]


def canon(st):
    return min(rotations(st) + rotations(reflect(st)))


def stars_of(rel):
    items = []
    for nm, k in rel.items():
        items += [nm] * k
    n = len(items)
    res = set()
    # DFS: first element fixed to each distinct (name, ori); remaining multiset arranged
    from collections import Counter

    def dfs(seq, left):
        if not left:
            if rays(*seq[-1])[1] == rays(*seq[0])[0]:
                res.add(canon(tuple(seq)))
            return
        need = rays(*seq[-1])[1]
        for nm in list(left):
            for o in 'dm':
                if rays(nm, o)[0] == need:
                    left[nm] -= 1
                    if left[nm] == 0:
                        del left[nm]
                    dfs(seq + [(nm, o)], left)
                    left[nm] = left.get(nm, 0) + 1
    cnt = Counter(items)
    for nm in list(cnt):
        for o in 'dm':
            left = Counter(cnt)
            left[nm] -= 1
            if left[nm] == 0:
                del left[nm]
            dfs([(nm, o)], left)
    return sorted(res)


ALL = []
for rel in rel360:
    ALL += stars_of(rel)
print('L3: stars up to rotation+reflection:', len(ALL))


def far(corner, side):
    nm, o = corner
    c = CORNERS[nm]
    tn = c['tile']
    names = TILES[tn][1]
    # direct: ccw ray -> vertex i-1, cw ray -> vertex i+1 ; mirror: swapped
    step = {('d', 'ccw'): -1, ('d', 'cw'): +1, ('m', 'ccw'): +1, ('m', 'cw'): -1}[(o, side)]
    return (tn + '-' + names[(c['idx'] + step) % c['n']], o)


# work with both chiral copies explicitly
def oriented_set(stars):
    out = set()
    for st in stars:
        out.add(min(rotations(st)))
        out.add(min(rotations(reflect(st))))
    return out


print('L3: of these, mixed-handedness stars:', sum(1 for st in ALL if len({o for _, o in st}) == 2))
live = oriented_set(ALL)
rounds = []
history = []
while True:
    pairs = set()
    for st in live:
        n = len(st)
        for i in range(n):
            pairs.add((st[i], st[(i + 1) % n]))
    keep = set()
    for st in live:
        n = len(st)
        ok = True
        for i in range(n):
            X, Y = st[i], st[(i + 1) % n]
            # shared edge: X's ccw ray == Y's cw ray (labels must agree)
            assert rays(*X)[1] == rays(*Y)[0]
            Xf, Yf = far(X, 'ccw'), far(Y, 'cw')
            # at far end, Yf's ccw ray and Xf's cw ray are the same edge: same label
            assert rays(*Yf)[1] == rays(*Xf)[0] == rays(*X)[1]
            if (Yf, Xf) not in pairs:
                ok = False
                break
        if ok:
            keep.add(st)
    rounds.append(len(live) - len(keep))
    history.append(sorted({canon(st) for st in live - keep}))
    if keep == live:
        break
    live = keep
viable = sorted({canon(st) for st in live})
print('L3: pruning removed (oriented counts per round)', rounds, '; survivors up to reflection:', len(viable))
for st in viable:
    print('   ', st)
mono = all(len({o for _, o in st}) == 1 for st in viable)
print('L3: all survivors single-handed:', mono)

# ---------------------------------------------------------------- L4(i) facts
def rels_with(nm):
    return [r for r in rel360 if nm in r]


for nm in ('H6-J', 'P2-K', 'P2-L', 'P1-K', 'P1-L', 'P1-F'):
    print('L4 relations containing', nm, ':', rels_with(nm))
for nm in ("H6-J'", "P1-J'", "H6-J''", 'P2-J2'):
    print('L4 relations containing', nm, ':', rels_with(nm))

print('L3: stars (up to reflection) killed in round 2:')
for st in history[1]:
    print('   ', st)
