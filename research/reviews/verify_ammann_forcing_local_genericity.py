#!/usr/bin/env python3
"""Independent check of the genericity statement of
research/lemmas/ammann-forcing-aperiodicity.md (Lemma 2(c) and the header claim
"D \\ G is contained in a locally finite union of real algebraic curves").

Replay:
  conda run --no-capture-output -n arisearch python3 \
      research/reviews/verify_ammann_forcing_local_genericity.py

Shows exactly:
 (1) rho_chi(J) is a non-constant holomorphic rational function of J, with
     rho_chi'(J0) != 0; hence chi = arg rho_chi is a non-constant harmonic
     function, so chi takes every value of an open interval on every ball in D
     and {J in D : chi(J)/pi in Q} (a subset of D \\ G) is DENSE in D.
 (2) explicit algebraic points J* in D on lines s = const with
     chi(J*) = 108 or 120 deg exactly (so J* is not in G), and the three
     tiles strictly convex there (exact, AA/QQbar).
A locally finite union of curves is closed and nowhere dense, so it cannot
contain a dense subset of D: the header/Lemma 2(c) claim is false as stated.
"""
from sage.all import CyclotomicField, PolynomialRing, QQ, AA, QQbar

L = CyclotomicField(30)
z30 = L.gen()
w = z30**3            # zeta10
z3 = z30**10          # zeta3 = exp(2 pi i/3)
R = PolynomialRing(L, 'x')
x = R.gen()
Fx = R.fraction_field()

Kv = w**2 + w**6 * (x - 1)
Lv = 1 + w**7 * (x - 1 - w)
J1 = 1 + w**4 * (x - 1)
J2p = w + w**6 * (x - w)
J2 = 1 + w + w**2 - x
TILES = {
    'H6': [R(0), J1, R(1), x, R(w), J2p],
    'P1': [R(0), J1, R(1), Lv, Kv],
    'P2': [Kv, Lv, R(1 + w**2), J2, R(w**2)],
}
P = TILES['H6']
rho_chi = Fx(P[0] - P[1]) / Fx(P[2] - P[1])     # corner at J' (index 1)
print('rho_chi =', rho_chi)
num, den = rho_chi.numerator(), rho_chi.denominator()
print('deg num, den:', num.degree(), den.degree())
assert num.degree() + den.degree() > 0
J0 = L(QQ(1) / 2) + L(QQ(4) / 5) * w
d = (num.derivative() * den - num * den.derivative())(J0)
print("rho_chi'(J0) != 0 :", d != 0)
assert d != 0

# (2) chi = target on a line s = s0 : rho_chi(s0 + t w) * conj(u) real positive, u = e^{i target}.
T = PolynomialRing(L, 't')
t = T.gen()
emb = L.hom([QQbar.zeta(30)])


def conj_poly(f):
    return T([c.conjugate() for c in f.list()])


found = None
for s0 in (QQ(1) / 2, QQ(9) / 20, QQ(11) / 20, QQ(2) / 5):
    for deg_, u in ((108, w**3), (120, z3)):
        Jt = s0 + t * w
        n_t, d_t = num(Jt), den(Jt)
        G = n_t * conj_poly(d_t) * u.conjugate() - conj_poly(n_t) * d_t * u
        Gq = PolynomialRing(QQbar, 't')([emb(c) for c in G.list()])
        for r, m in Gq.roots(QQbar):
            if r.imag() != 0 or not (0 < r.real() < 1):
                continue
            tv = AA(r.real())
            Jv = QQbar(s0) + QQbar(tv) * QQbar.zeta(10)
            rv = QQbar(num.map_coefficients(emb, QQbar)(Jv)) / QQbar(den.map_coefficients(emb, QQbar)(Jv))
            ratio = rv / emb(u)
            if not (ratio.imag() == 0 and ratio.real() > 0):
                continue
            conv = True
            for tn, Pt in TILES.items():
                V = [QQbar(v.map_coefficients(emb, QQbar)(Jv)) for v in Pt]
                n = len(V)
                for i in range(n):
                    a_, b_ = V[i] - V[i - 1], V[(i + 1) % n] - V[i]
                    if not ((a_.conjugate() * b_).imag() > 0):
                        conv = False
            print('s0 =', s0, ' t* =', tv.n(40), ' chi =', deg_, 'deg exactly; tiles strictly convex ccw:', conv)
            if conv and found is None:
                found = (s0, tv, deg_)
assert found
print('=> explicit J* = %s + t* w (t* ~ %s) in D with chi = %d deg: J* not in G.' % (found[0], found[1].n(30), found[2]))
print('   With (1), D \\ G is dense in D.')
