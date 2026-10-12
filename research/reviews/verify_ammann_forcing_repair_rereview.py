#!/usr/bin/env sage -python
"""Independent re-review checks for the REPAIRS in
research/lemmas/ammann-forcing-aperiodicity.md (no author code imported).

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/reviews/verify_ammann_forcing_repair_rereview.py

Part A (local repairs D1-D4)
  A1  identical-relation enumeration from the lemma's printed angle table, with
      reviewer-chosen positive rational dummy triples (not the certificate's),
      plus a check that the found set is invariant and equals the certificate.
  A2  exact rank of every stored valuation matrix; independent recomputation
      of the valuation vectors of w_chi, w_psi, w_kappa from the tile formulas
      of ammann-two-class-reconstruction.md; prime lists vs the lemma table.
  A3  the lemma's example non-identical relation on chi = 108.
Part B (reconstruction repairs D1, D2, D4)
  B1  orientation rule (Lemma 5): X edge -> quad on the left, Y -> right.
  B2  closure (Lemma 6, cases alpha/beta) with parents found by BRUTE FORCE
      over all big marked halves (no inverse formulas), all 10 rotations.
  B3  deflation legality (Lemma 7(a)) checked DIRECTLY: for every legal
      full-edge contact of two big halves (all rotations, both chiralities),
      every pair of children meeting in a positive-length segment shares a
      full edge with compatible kind; children of one half are interior-
      disjoint and their areas sum to the parent's.
All decisions exact (K = Q(zeta_10), signs via AA, Fractions).
"""
import json, itertools
from fractions import Fraction
from sage.all import CyclotomicField, QQbar, AA, QQ, ZZ, matrix

K = CyclotomicField(10)
w = K.gen()
emb = K.hom([QQbar.zeta(10)])
cj = lambda z: z.conjugate()
CERT = 'research/certificates/ammann-forcing-angles.json'

# ============================================================ Part A
# lemma table, transcribed from the lemma text: (const deg, chi, psi, kappa)
TABLE = {
    'H6-A': (72, 0, 0, 0), 'P1-E': (72, 0, 0, 0), 'P2-G': (72, 0, 0, 0),
    'H6-B': (144, 0, 0, 0), 'H6-D': (144, 0, 0, 0),
    "H6-J'": (0, 1, 0, 0), "P1-J'": (0, 1, 0, 0),
    "H6-J''": (0, 0, 1, 0), 'P2-J2': (0, 0, 1, 0),
    'H6-J': (360, -1, -1, 0), 'P1-F': (252, -1, 0, 0), 'P2-H': (-36, 1, 0, 0),
    'P1-K': (0, 0, 0, 1), 'P1-L': (216, 0, 0, -1),
    'P2-K': (360, -1, 0, -1), 'P2-L': (144, 0, -1, 1),
}
NAMES = sorted(TABLE)

def enum_identical(dummy, T):
    """all m >= 0 with sum m_j * form_j == T identically; exact."""
    vals = [Fraction(TABLE[n][0]) + sum(Fraction(TABLE[n][i + 1]) * dummy[i] for i in range(3))
            for n in NAMES]
    assert all(v > 0 for v in vals), (dummy, vals)
    order = sorted(range(len(NAMES)), key=lambda i: -vals[i])   # different order from authors
    out = []
    def rec(k, rem, m):
        if k == len(order):
            if rem == 0:
                coef = [sum(m.get(n, 0) * TABLE[n][i] for n in NAMES) for i in range(4)]
                if coef == [T, 0, 0, 0]:
                    out.append(tuple(sorted(m.items())))
            return
        i = order[k]
        v = vals[i]
        c = 0
        while c * v <= rem:
            m2 = dict(m)
            if c:
                m2[NAMES[i]] = c
            rec(k + 1, rem - c * v, m2)
            c += 1
    rec(0, Fraction(T), {})
    return set(out)

def part_A():
    res = {}
    dummies = [(Fraction(100), Fraction(100), Fraction(100)),
               (Fraction(130), Fraction(110), Fraction(70)),
               (Fraction(90), Fraction(90), Fraction(60)),
               (Fraction(1091, 10), Fraction(3013, 20), Fraction(1517, 10))]
    sets = []
    for d in dummies:
        s180, s360 = enum_identical(d, 180), enum_identical(d, 360)
        sets.append((s180, s360))
        print('A1 dummy', [str(x) for x in d], '->', len(s180), len(s360))
    assert all(a == sets[0][0] and b == sets[0][1] for a, b in sets)
    cert = json.load(open(CERT))
    certset = {tuple(sorted(r['relation'].items())) for r in cert['identical_360_relations_with_stars']}
    assert certset == sets[0][1] and len(cert['identical_180_relations']) == 0 == len(sets[0][0])
    res['A1'] = {'n180': len(sets[0][0]), 'n360': len(sets[0][1]), 'equals_certificate': True,
                 'dummies': [[str(x) for x in d] for d in dummies]}
    # A1': the certificate's cross-check record
    res['A1_cert_cross_check'] = cert['relation_enumeration_cross_check']

    # A2: stored matrices, exact rank; independent recomputation
    lemma_primes = {('1/2', '4/5'): {11, 41, 181, 251, 1031},
                    ('9/20', '3/4'): {4441, 26321, 35401, 116461},
                    ('11/20', '17/20'): {11, 41, 131, 281, 911, 5171},
                    ('3/7', '5/6'): {11, 61, 101, 151, 37021, 42491, 1025161},
                    ('5/11', '7/9'): {61, 271, 46411, 258871, 886741, 24167551}}
    out = []
    for p in cert['points_tested']:
        s, t = QQ(p['s']), QQ(p['t'])
        M = matrix(ZZ, p['valuation_matrix_rows_chi_psi_kappa'])
        J = s + t * w
        Jp = 1 + w**4 * (J - 1); Jpp = w + w**6 * (J - w)
        Kp = w**2 + w**6 * (J - 1); Lp = 1 + w**7 * (J - 1 - w)
        H6 = [K(0), Jp, K(1), J, w, Jpp]; P1 = [K(0), Jp, K(1), Lp, Kp]
        def rho(P, i):
            return (P[i - 1] - P[i]) / (P[(i + 1) % len(P)] - P[i])
        ws = [rho(H6, 1), rho(H6, 5), rho(P1, 4)]
        ws = [z / cj(z) for z in ws]
        facs = [dict(K.fractional_ideal(z).factor()) for z in ws]
        primes = sorted({P for f in facs for P in f}, key=lambda P: (P.norm(), str(P.gens_two())))
        Mi = matrix(ZZ, [[f.get(P, 0) for P in primes] for f in facs])
        rp = {int(P.norm().factor()[0][0]) for P in primes}
        ok = (M.rank() == 3 and Mi.rank() == 3 and rp == lemma_primes[(p['s'], p['t'])]
              and sorted(map(tuple, M.columns())) == sorted(map(tuple, Mi.columns())))
        out.append({'point': [p['s'], p['t']], 'stored_rank': int(M.rank()), 'recomputed_rank': int(Mi.rank()),
                    'rational_primes': sorted(rp), 'matches_lemma_table': rp == lemma_primes[(p['s'], p['t'])],
                    'stored_columns_equal_recomputed_up_to_order': sorted(map(tuple, M.columns())) == sorted(map(tuple, Mi.columns()))})
        print('A2', out[-1])
        assert ok
    res['A2'] = out

    # A3: the example relation P1-F + H6-B + P1-E on chi = 108
    m = {'P1-F': 1, 'H6-B': 1, 'P1-E': 1}
    coef = [sum(k * TABLE[n][i] for n, k in m.items()) for i in range(4)]
    assert coef == [468, -1, 0, 0]          # 468 - chi = 360 iff chi = 108: non-identical
    res['A3'] = {'relation': m, 'form_const_chi_psi_kappa': coef}
    print('A3', res['A3'])
    return res

# ============================================================ Part B
phi = w + w**9                       # 2 cos 36
assert phi**2 == phi + 1
iphi = phi - 1
def im_sign(z):
    v = AA(emb((z - cj(z)) / (w - cj(w))))     # positive multiple of Im z
    return (v > 0) - (v < 0)
def re_val(z):
    return AA(emb((z + cj(z)) / 2))
def cross(u, v):                     # sign of Im(conj(u) v)
    return im_sign(cj(u) * v)

def rhomb(typ, k, o=K(0), sc=K(1)):
    if typ == 'thin':
        V = [o, o + sc * w**k, o + sc * (w**k + w**(k + 1)), o + sc * w**(k + 1)]   # A B C D
        marks = {(0, 1): ('X', 1), (2, 1): ('X', 1), (0, 3): ('Y', 3), (2, 3): ('Y', 3)}
    else:
        V = [o, o + sc * w**k, o + sc * (w**k + w**(k + 2)), o + sc * w**(k + 2)]   # E F G H
        marks = {(0, 1): ('X', 1), (0, 3): ('X', 3), (1, 2): ('Y', 2), (3, 2): ('Y', 2)}
    return V, marks                   # marks: (tail, head) -> (type, head index)

# ---- B1: orientation rule, with the pieces at J0
def part_B1():
    s, t = QQ(1) / 2, QQ(4) / 5
    J = s + t * w
    Jp = 1 + w**4 * (J - 1); Jpp = w + w**6 * (J - w)
    Kp = w**2 + w**6 * (J - 1); Lp = 1 + w**7 * (J - 1 - w); J2 = 1 + w + w**2 - J
    def inside(V, p):
        return all(cross(V[(i + 1) % 4] - V[i], p - V[i]) > 0 for i in range(4))
    thin, mt = rhomb('thin', 0); thick, mk = rhomb('thick', 0)
    assert inside(thin, J) and inside(thick, Kp) and inside(thick, Lp)
    assert not inside(thin, Jp) and not inside(thin, Jpp) and not inside(thick, J2)
    # which rhomb edge carries the quad of the tile whose chord it is (quad inside rhomb)
    # thin: H6 quad ABJD -> edges AB, DA; triangles BCJ, CDJ inside -> BC, CD triangle side
    # thick: P1 quad EFLK -> EF; P2 quad KLGH -> GH; triangles HEK, FGL -> EH, FG
    quad_inside = {('thin', frozenset((0, 1))): True, ('thin', frozenset((0, 3))): True,
                   ('thin', frozenset((1, 2))): False, ('thin', frozenset((2, 3))): False,
                   ('thick', frozenset((0, 1))): True, ('thick', frozenset((2, 3))): True,
                   ('thick', frozenset((0, 3))): False, ('thick', frozenset((1, 2))): False}
    # confirm geometrically: the triangle apex of each chord lies outside the rhomb
    # (quad inside) or the third piece vertex J/K/L lies inside next to that edge
    rows = []
    for typ, (V, mk_) in (('thin', (thin, mt)), ('thick', (thick, mk))):
        cen = sum(V) / 4
        for (a, b), (ty, h) in mk_.items():
            left_is_interior = cross(V[b] - V[a], cen - V[a]) > 0
            q = quad_inside[(typ, frozenset((a, b)))]
            quad_left = left_is_interior if q else not left_is_interior
            rows.append((typ, a, b, ty, quad_left))
            assert quad_left == (ty == 'X'), (typ, a, b, ty)
    print('B1 orientation rule holds on all 8 marked edges')
    return {'edges_checked': len(rows), 'rule_holds': True}

# ---- halves and deflation
def halves_of(typ, k, o=K(0), sc=K(1)):
    V, _ = rhomb(typ, k, o, sc)
    if typ == 'thin':
        return [('r', V[0], V[1], V[3]), ('r', V[2], V[1], V[3])]
    return [('b', V[1], V[0], V[2]), ('b', V[3], V[0], V[2])]

def twin(h):
    c, a, b, d = h
    return (c, b + d - a, b, d)

def legs(h):
    """legs with marks derived from the lemma's rhomb arrows:
       red  (apex;B,C): apex-B is X with head B, apex-C is Y with head C
       blue (apex;B,C): apex-B is X with head apex, apex-C is Y with head C"""
    c, a, b, d = h
    if c == 'r':
        return [((a, b), ('X', b)), ((a, d), ('Y', d))]
    return [((a, b), ('X', a)), ((a, d), ('Y', d))]

def edges(h):
    c, a, b, d = h
    return [(frozenset(e), ('leg',) + m) for e, m in legs(h)] + [(frozenset((b, d)), ('base', c, b, d))]

# consistency of half marks with rhomb marks
for typ in ('thin', 'thick'):
    for k in range(10):
        V, mk_ = rhomb(typ, k)
        rm = {frozenset((V[a], V[b])): (ty, V[h]) for (a, b), (ty, h) in mk_.items()}
        for h in halves_of(typ, k):
            for e, m in legs(h):
                assert rm[frozenset(e)] == m

def children(T):
    c, A, B, C = T
    if c == 'r':
        P = A + (B - A) * iphi
        return [('r', C, P, B), ('b', P, C, A)]
    Q = B + (A - B) * iphi
    R = B + (C - B) * iphi
    return [('b', R, C, A), ('b', Q, R, B), ('r', R, Q, A)]

def area2(h):
    _, a, b, c = h
    z = cj(b - a) * (c - a)
    return abs(AA(emb(z - cj(z)) / (2 * QQbar.zeta(4))))   # |Im z|, exact

def on_seg_collinear(p, a, b):
    return cross(b - a, p - a) == 0

def overlap_pos(e1, e2):
    a, b = tuple(e1); c, d = tuple(e2)
    if not (on_seg_collinear(c, a, b) and on_seg_collinear(d, a, b)):
        return False
    u = b - a
    nn = re_val(u * cj(u))
    pr = lambda x: re_val((x - a) * cj(u)) / nn
    lo = max(min(pr(a), pr(b)), min(pr(c), pr(d)))
    hi = min(max(pr(a), pr(b)), max(pr(c), pr(d)))
    return lo < hi

def interior_disjoint(h1, h2):
    for X, Y in ((h1, h2), (h2, h1)):
        P = X[1:]
        orient = cross(P[1] - P[0], P[2] - P[0])
        for i in range(3):
            a, b = P[i], P[(i + 1) % 3]
            if all(cross(b - a, q - a) * orient <= 0 for q in Y[1:]):
                return True
    return False

BIG = []          # all big halves at the origin (legs phi), all rotations
for typ in ('thin', 'thick'):
    for k in range(10):
        BIG += halves_of(typ, k, K(0), phi)

def translate(h, tau):
    return (h[0],) + tuple(v + tau for v in h[1:])

def brute_parents(t):
    """all big halves G (any rotation, any translation) with t among children(G)"""
    out = []
    for G in BIG:
        for c in children(G):
            if c[0] != t[0]:
                continue
            tau = t[1] - c[1]
            if translate(c, tau) == t:
                Gt = translate(G, tau)
                if Gt not in out:
                    out.append(Gt)
    return out

def part_B2():
    stats = {'outward_children': 0, 'cases': 0, 'alpha_has_h_as_child': 0,
             'beta_full_edge_same_mark': 0, 'alpha_also_interior_overlap_with_R': 0,
             'neither': 0, 'edges_with_one_outward_base': 0}
    for typ in ('thin', 'thick'):
        for k in range(10):
            Hs = halves_of(typ, k, K(0), phi)
            chR = [c for H in Hs for c in children(H)]
            Rlegs = {frozenset(e): m for H in Hs for e, m in legs(H)}
            per_edge = {e: 0 for e in Rlegs}
            for h in chR:
                if twin(h) in chR:
                    continue
                stats['outward_children'] += 1
                base = frozenset((h[2], h[3]))
                car = [e for e in Rlegs if all(on_seg_collinear(p, *tuple(e)) and
                                                 overlap_pos(e, base) for p in base)]
                assert len(car) == 1
                eR = car[0]; per_edge[eR] += 1
                hs = twin(h)
                pars = brute_parents(hs)
                assert len(pars) == (2 if hs[0] == 'r' else 3), len(pars)
                for Gp in pars:
                    stats['cases'] += 1
                    Rp = [Gp, twin(Gp)]
                    chRp = [c for H in Rp for c in children(H)]
                    if h in chRp:
                        stats['alpha_has_h_as_child'] += 1
                        if any(not interior_disjoint(a, b) for a in Rp for b in Hs):
                            stats['alpha_also_interior_overlap_with_R'] += 1
                        continue
                    Rplegs = {frozenset(e): m for H in Rp for e, m in legs(H)}
                    if eR in Rplegs and Rplegs[eR] == Rlegs[eR]:
                        stats['beta_full_edge_same_mark'] += 1
                    else:
                        stats['neither'] += 1
            assert all(v == 1 for v in per_edge.values()), per_edge
            stats['edges_with_one_outward_base'] += len(per_edge)
    assert stats['neither'] == 0
    print('B2', stats)
    return stats

def compatible(k1, k2):
    return k1 == k2

def legal_pair(c1, c2):
    """two halves with disjoint interiors: every positive-length edge contact is a
    shared full edge with compatible kind"""
    for e1, k1 in edges(c1):
        for e2, k2 in edges(c2):
            if overlap_pos(e1, e2):
                if e1 != e2 or not compatible(k1, k2):
                    return False
    return True

def part_B3():
    stats = {'single_halves': 0, 'contacts': 0, 'child_pairs_checked': 0}
    # (a) single halves
    for H in BIG:
        ch = children(H)
        assert sum(area2(c) for c in ch) == area2(H)
        for c in ch:                      # child inside parent (all vertices in closed H)
            P = H[1:]
            o = cross(P[1] - P[0], P[2] - P[0])
            assert all(cross(P[(i + 1) % 3] - P[i], v - P[i]) * o >= 0 for i in range(3) for v in c[1:])
        for c1, c2 in itertools.combinations(ch, 2):
            assert interior_disjoint(c1, c2) and legal_pair(c1, c2)
            stats['child_pairs_checked'] += 1
        stats['single_halves'] += 1
    # (b) every legal full-edge contact of two big halves
    for H in BIG:
        P = H[1:]
        for e, kd in edges(H):
            a, b = tuple(e)
            third = [v for v in P if v not in (a, b)][0]
            sH = cross(b - a, third - a)
            partners = []
            if kd[0] == 'base':
                partners = [twin(H)]
            else:
                for G in BIG:
                    for e2, kd2 in edges(G):
                        if kd2[0] != 'leg' or kd2[1] != kd[1]:
                            continue
                        tau = kd[2] - kd2[2]                 # heads coincide
                        if frozenset(v + tau for v in e2) != e:
                            continue
                        Gt = translate(G, tau)
                        th = [v for v in Gt[1:] if v not in (a, b)][0]
                        if cross(b - a, th - a) == -sH:
                            if Gt not in partners:
                                partners.append(Gt)
            assert partners
            for G in partners:
                assert interior_disjoint(H, G)
                stats['contacts'] += 1
                for c1 in children(H):
                    for c2 in children(G):
                        assert interior_disjoint(c1, c2)
                        assert legal_pair(c1, c2), (H, G, c1, c2)
                        stats['child_pairs_checked'] += 1
    print('B3', stats)
    return stats

if __name__ == '__main__':
    out = {'A': part_A(), 'B1': part_B1(), 'B2': part_B2(), 'B3': part_B3()}
    print('ALL CHECKS PASSED')
