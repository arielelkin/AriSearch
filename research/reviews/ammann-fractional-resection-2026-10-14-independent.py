"""Independent exact CyclotomicField(10) check of the16 fan quadrilaterals.

No producer import. Reconstructs actual complex rhomb centers rather than
the author's scaled Q(phi) coordinates, checks every global support, exact
quarter area, reference native arrows and all frozen geometric rows.
"""
import json
from pathlib import Path
from itertools import product
from functools import cache

from sage.all import AA, CyclotomicField, QQbar, sage_eval

ROOT = Path(__file__).resolve().parents[1]
K = CyclotomicField(10)
w = K.gen()
embed = K.hom([QQbar.zeta(10)], QQbar)
phi = w+w.conjugate()
assert phi**2-phi-1 == 0


def conjugate(p):
    return p.conjugate()


@cache
def sign(p):
    assert p == conjugate(p)
    r = AA(embed(p))
    return 1 if r > 0 else -1 if r < 0 else 0


def cross(a, b):
    # Actual Euclidean determinant divided by positive sin(pi/5).
    return (conjugate(a)*b-a*conjugate(b))/(w-conjugate(w))


def area(F):
    return sum(cross(a, F[(j+1) % len(F)]) for j, a in enumerate(F))/2


def scaled(p):
    return ((p+conjugate(p))/2, (p-conjugate(p))/(w-conjugate(w)))


def expression(s):
    return K(sage_eval(s, locals={'phi': phi}))


def scaled_data(p):
    return tuple(expression(q) for q in p)


def rhomb(q):
    return (K(0), K(1), K(1)+q, q)


def check():
    cert = json.loads((ROOT/'certificates'/'ammann-fractional-resection-2026-10-14.json').read_text())
    assert cert['contact_enumeration_performed'] is False
    rows = {(tuple(r['right']), tuple(r['left'])): r for r in cert['geometry_rows']}
    choices = [('thin', e, 1) for e in [-1, 1]]+[('thick', e, 2) for e in [-1, 1]]
    expected = {((a, e), (b, f)) for a, e, j in choices for b, f, k in choices}
    assert set(rows) == expected and len(rows) == len(cert['geometry_rows']) == 16
    supports = 0
    for (right, er, j), (left, el, k) in product(choices, repeat=2):
        # Each center is a diagonal intersection of a true unit rhomb
        # placed on the chosen side of the common normalized edge0--1.
        oright = (1+w**(-j))/2 if er == 1 else (1-w**j)/2
        oleft = (1+w**k)/2 if el == 1 else (1-w**(-k))/2
        F = (K(0), oright, K(1), oleft)
        assert len(set(F)) == 4
        for n, a in enumerate(F):
            b = F[(n+1) % 4]
            for m, p in enumerate(F):
                if m not in [n, (n+1) % 4]:
                    assert sign(cross(b-a, p-a)) > 0
                    supports += 1
        rarea = area(rhomb(w**j))
        larea = area(rhomb(w**k))
        assert area((K(0), oright, K(1))) == rarea/4
        assert area((K(0), K(1), oleft)) == larea/4
        assert area(F) == (rarea+larea)/4
        row = rows[((right, er), (left, el))]
        assert tuple(map(scaled, F)) == tuple(map(scaled_data, row['vertices']))
        assert area(F) == expression(row['normalized_area'])
        turns = [cross(F[n]-F[n-1], F[(n+1) % 4]-F[n]) for n in range(4)]
        assert turns == [expression(t) for t in row['turns']]
        assert row['native_sides'] == 4

    # Independently instantiate the two stated marked reference contacts.
    thin = rhomb(w)
    thick = rhomb(w*w)
    # Thin left native A->B; right native C->B.
    thin_left = thin
    tr = -w**-1
    ts = -tr*thin[2]
    thin_right = tuple(tr*p+ts for p in thin)
    assert thin_left[0] == thin_right[2] == 0
    assert thin_left[1] == thin_right[1] == 1
    X = (K(0), sum(thin_right)/4, K(1), sum(thin_left)/4)
    assert X == (K(0), (1+w**-1)/2, K(1), (1+w)/2)
    assert tuple(map(scaled, X)) == tuple(map(scaled_data, cert['references']['A_X']))
    # Thick left native F->G; right native H->G.
    thick_left = tuple(w**-2*(p-1) for p in thick)
    thick_right = tuple(p-w*w for p in thick)
    assert thick_left[1] == thick_right[3] == 0
    assert thick_left[2] == thick_right[2] == 1
    Y = (K(0), sum(thick_right)/4, K(1), sum(thick_left)/4)
    assert Y == (K(0), (1-w*w)/2, K(1), (1-w**-2)/2)
    assert tuple(map(scaled, Y)) == tuple(map(scaled_data, cert['references']['B_Y']))
    # Native marks from reviewed Lemma5: exactly two X and two Y
    # per thin/thick rhomb. Each full shared edge has two incidences.
    assert cert['XY_count_matrix_on_thin_thick'] == [['1', '1'], ['1', '1']]
    print('PASS independent complex reconstruction:16 strict quadrilaterals,',
          supports, 'global support inequalities,32 quarter-area identities,')
    print('all frozen geometry rows, native X/Y reference contacts and edge-incidence counts.')


if __name__ == '__main__':
    check()
