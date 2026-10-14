#!/usr/bin/env python3
"""Independent local geometry checker for the directed X/Y two-node surgery.

This file intentionally does not import the constructor.  Run through the
repository's pinned environment.  Its symbolic assertions check all four
source/role cases; --fixture checks an exact rational-height/offset example.
"""

import argparse
import sympy as S

aX, aY, hX, hY = S.symbols("aX aY hX hY", real=True)
R5 = S.sqrt(5)
C36, C72 = (1 + R5) / 4, (R5 - 1) / 4
S36, S72 = S.sqrt(10 - 2 * R5) / 4, S.sqrt(10 + 2 * R5) / 4


def add(v, w):
    return (v[0] + w[0], v[1] + w[1])


def sub(v, w):
    return (v[0] - w[0], v[1] - w[1])


def mul(t, v):
    return (t * v[0], t * v[1])


def cross(v, w):
    return S.expand(v[0] * w[1] - v[1] * w[0])


def sq(v):
    return S.expand(v[0] ** 2 + v[1] ** 2)


def area(poly):
    return S.expand(sum(cross(poly[i], poly[(i + 1) % len(poly)])
                        for i in range(len(poly))) / 2)


def edge_sq_sum(poly):
    return S.expand(sum(sq(sub(poly[(i + 1) % len(poly)], poly[i]))
                        for i in range(len(poly))))


# Each edge flag is +1 for arrow in CCW direction and -1 otherwise.
# The cases are rhomb type (thin/thick) and which opposite pair donates.
CASES = {
    "thin_AB_CD": (C36, S36, (("X", 1), ("X", -1), ("Y", 1), ("Y", -1))),
    "thin_BC_DA": (-C36, S36, (("X", -1), ("Y", 1), ("Y", -1), ("X", 1))),
    "thick_EF_GH": (C72, S72, (("X", 1), ("Y", 1), ("Y", -1), ("X", -1))),
    "thick_FG_HE": (-C72, S72, (("Y", 1), ("Y", -1), ("X", -1), ("X", 1))),
}


def params(mark):
    return (aX, hX) if mark == "X" else (aY, hY)


def at_arrow_fraction(edge, mark_flag):
    """Fraction along the CCW edge corresponding to the directed apex."""
    mark, flag = mark_flag
    a, h = params(mark)
    f = a if flag == 1 else 1 - a
    # The right normal is the exterior side for a CCW source rhomb.
    normal = (edge[1], -edge[0])
    return f, h, normal


def case_geometry(case):
    c, s, edges = CASES[case]
    A, B, C, D = (S.Integer(0), S.Integer(0)), (S.Integer(1), S.Integer(0)), (1 + c, s), (c, s)
    # AB and CD donate; their apexes are on the source-interior side.
    ab_mark, ab_flag = edges[0]
    cd_mark, cd_flag = edges[2]
    a0, hh0 = params(ab_mark)
    a2, hh2 = params(cd_mark)
    u = a0 if ab_flag == 1 else 1 - a0
    v = 1 - a2 if cd_flag == 1 else a2
    p, q = (u, hh0), (c + v, s - hh2)
    bc_f, bc_h, bc_n = at_arrow_fraction(sub(C, B), edges[1])
    da_f, da_h, da_n = at_arrow_fraction(sub(A, D), edges[3])
    tBC = add(add(B, mul(bc_f, sub(C, B))), mul(bc_h, bc_n))
    tDA = add(add(D, mul(da_f, sub(A, D))), mul(da_h, da_n))
    sectors = ((A, B, p), (B, C, q, p), (C, D, q), (D, A, p, q))
    outputs = ((B, tBC, C, q, p), (D, tDA, A, p, q))
    return (A, B, C, D), sectors, outputs


def turns(poly):
    return tuple(cross(sub(poly[(i + 1) % len(poly)], poly[i]),
                       sub(poly[(i + 2) % len(poly)], poly[(i + 1) % len(poly)]))
                 for i in range(len(poly)))


def strict_support_values(poly):
    """Cross products of each edge with every nonendpoint vertex."""
    n = len(poly)
    return tuple(cross(sub(poly[j], poly[i]),
                       sub(poly[(i + 1) % n], poly[i])) * -1
                 for i in range(n) for j in range(n)
                 if j not in (i, (i + 1) % n))


def distance_word(poly):
    n = len(poly)
    return tuple(sq(sub(poly[(i + j) % n], poly[i]))
                 for i in range(n) for j in range(1, n))


def congruent(P, Q):
    """Exact cyclic distance comparison, rotations and reflections allowed."""
    n = len(P)
    for direction in (1, -1):
        for shift in range(n):
            R = tuple(Q[(shift + direction * i) % n] for i in range(n))
            if all(S.simplify(sq(sub(P[i], P[j])) - sq(sub(R[i], R[j]))) == 0
                   for i in range(n) for j in range(i + 1, n)):
                return True
    return False


def symbolic_checks():
    dt = (aY - aX) * S36 + (C36 + 1 - aY) * hX + (aX - 1 - C36) * hY
    dk = (1 - aX - aY) * S72 + (C72 + aY - 1) * hX + (aX - C72) * hY
    expected = ((S36, dt), (S36, -dt), (S72, dk), (S72, dk))
    for case, (s, diff) in zip(CASES, expected):
        rhomb, sectors, outputs = case_geometry(case)
        assert S.simplify(sum(area(p) for p in sectors) - s) == 0, case
        assert S.simplify(sum(area(p) for p in outputs) - s) == 0, case
        assert S.simplify(area(outputs[0]) - area(outputs[1]) - diff) == 0, case
    t0 = case_geometry("thin_AB_CD")[2]
    k0 = case_geometry("thick_EF_GH")[2]
    et = (aX - aY) * (aX + aY - 2) + hX**2 - hY**2
    ek = aX**2 - aY**2 + 2 * aY + hX**2 - hY**2 - 1
    # Equality of two ordered pentagons implies equality of this invariant.
    assert S.simplify(edge_sq_sum(t0[0]) - edge_sq_sum(t0[1]) - 2 * et) == 0
    assert S.simplify(edge_sq_sum(k0[0]) - edge_sq_sum(k0[1]) + 2 * ek) == 0
    assert S.simplify(et - ek - (1 - 2 * aX)) == 0
    # The reflection equations are checked by complete distance words
    # under independent exact rational parameter specialization in fixture().
    return dt, dk


def fixture():
    # Small, asymmetric, exact data; used to catch sign and arrow-tail errors.
    spec = {aX: S.Rational(2, 5), aY: S.Rational(3, 5),
            hX: S36 / 10, hY: S36 / 20}
    polys = {}
    for case in CASES:
        rhomb, sectors, outputs = case_geometry(case)
        for poly in sectors + outputs:
            vals = [S.simplify(z.subs(spec)) for z in strict_support_values(poly)]
            assert all(v.is_positive is True for v in vals), (case, vals)
        polys[case] = [tuple((S.simplify(x.subs(spec)), S.simplify(y.subs(spec)))
                             for x, y in poly) for poly in outputs]
    assert congruent(polys["thin_AB_CD"][0], polys["thin_BC_DA"][1])
    assert congruent(polys["thin_AB_CD"][1], polys["thin_BC_DA"][0])
    assert congruent(polys["thick_EF_GH"][0], polys["thick_FG_HE"][0])
    assert congruent(polys["thick_EF_GH"][1], polys["thick_FG_HE"][1])
    print("Exact asymmetric fixture: 8 strict pentagons; opposite roles reflect correctly.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", action="store_true")
    args = parser.parse_args()
    dt, dk = symbolic_checks()
    print("Symbolic area differences:", dt, dk)
    if args.fixture:
        fixture()
