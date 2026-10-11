#!/usr/bin/env python3
"""Exact four-parameter double-Y V/V geometry and asymmetric fixture.

This constructs a prescribed continuum, not a search over arbitrary tilings.
The coefficient identities plus the analytic winding proof in the lemma give
whole-cone coverage. Exact clipping supplies an additional fixture audit.
"""
import argparse
import json
from itertools import product
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
R = PolynomialRing(K, ("x", "k", "y", "f"))
x, k, y, f = R.gens()


def conjugate(p):
    return R({tuple(t): q.conjugate() for t, q in R(p).dict().items()})


def cross(p, q):
    return (conjugate(p)*q-p*conjugate(q))/(z-z.conjugate())


def area(p):
    return sum(cross(p[j], p[(j+1) % len(p)]) for j in range(len(p)))/2


def linear_coefficients(p):
    coefficients = []
    for variable in (x, k, y, f):
        q = K(R(p).monomial_coefficient(variable)).list()
        coefficients.append([str(q[j]) if j < len(q) else "0" for j in range(4)])
    return coefficients


def construct():
    r, e = phi*(x+f)-y, f+phi*(x-y)
    l, m = phi*(x+k)-f, phi*(f-x)-k
    J = r*z**2-x*z**4
    H = 2*J+k
    A = [J, r*z**2, 0, y, y+e*z]
    B = [J+k, J, y+e*z, y+(e+l)*z, y+(e+l)*z+m*z**2]
    motifs = [A, [H-q for q in A], B, [H-q for q in B]]
    for polygon, lengths, directions in (
            (A, [x, r, y, e, f], [4, 7, 0, 1, 3]),
            (B, [k, f, l, m, x], [5, 8, 1, 2, 4])):
        assert [polygon[(j+1) % 5]-polygon[j] for j in range(5)] == [
            length*z**direction for length, direction in zip(lengths, directions)]
    beta, gamma = e+l, m+r
    assert beta == phi*(2*x+k-y)
    assert gamma == 2*phi*f-k-y
    assert H == y+beta*z+gamma*z**2
    macro = [0, y, y+beta*z, H, beta*z+gamma*z**2, gamma*z**2]
    seams = [(0, 0, 3, 4), (0, 4, 2, 1), (1, 0, 2, 4),
             (1, 4, 3, 1), (2, 0, 3, 0)]
    used = set()
    for i, h, j, g in seams:
        assert motifs[i][h] == motifs[j][(g+1) % 5]
        assert motifs[i][(h+1) % 5] == motifs[j][g]
        assert (i, h) not in used and (j, g) not in used
        used |= {(i, h), (j, g)}
    chains = [[(0, 2)], [(0, 3), (2, 2)], [(2, 3), (1, 1)],
              [(1, 2)], [(1, 3), (3, 2)], [(3, 3), (0, 1)]]
    for h, chain in enumerate(chains):
        point = macro[h]
        for i, g in chain:
            assert motifs[i][g] == point
            point = motifs[i][(g+1) % 5]
            assert (i, g) not in used
            used.add((i, g))
        assert point == macro[(h+1) % 6]
    assert len(used) == 20
    u, v = macro[2], macro[4]
    determinant = y*beta+phi*y*gamma+beta*gamma
    assert cross(u, v) == determinant
    assert sum(map(area, motifs)) == area(macro) == determinant
    macro_seams = [(0, 3, 0, -1), (1, 4, 1, -1), (2, 5, 1, 0)]
    for h, g, n, t in macro_seams:
        assert macro[h] == macro[(g+1) % 6]+n*u+t*v
        assert macro[(h+1) % 6] == macro[g]+n*u+t*v
    # An arbitrary native V=(b,d,c,h,j) is B=(k,f,l,m,x).
    # Choosing y=x makes A a mirror V=(x,phi*f+x/phi,x,f,f).
    assert R(r).subs({y: x}) == phi*f+x/phi
    assert R(e).subs({y: x}) == f
    assert R(r-m).subs({y: x}) == (2*phi-1)*x+k
    assert 1+z**6 == -z**3/phi
    assert z**7+z**9 == -phi*z**3
    return motifs, macro, (u, v), {
        "positive_cone": "x,k,y>0; x+k/phi<f<phi*(x+k); y<x+f/phi",
        "A_native_lengths": ["x", "phi*(x+f)-y", "y", "f+phi*(x-y)", "f"],
        "B_native_lengths": ["k", "f", "phi*(x+k)-f", "phi*(f-x)-k", "x"],
        "native_after_side_angles_pi_over_5": [2, 2, 4, 3, 4],
        "formal_motif_coefficients_x_k_y_f": [[linear_coefficients(q) for q in p] for p in motifs],
        "formal_macro_coefficients_x_k_y_f": list(map(linear_coefficients, macro)),
        "formal_period_coefficients_x_k_y_f": list(map(linear_coefficients, (u, v))),
        "internal_reversed_seams": seams, "outer_macro_chains": chains,
        "all_twenty_sides_accounted_once": True,
        "macro_seams": macro_seams, "macro_links": [[0, 4, 2], [1, 5, 3]],
        "normalized_macro_area_and_determinant": str(determinant),
        "arbitrary_V_mirror_partner": "B=(b,d,c,h,j) -> A=(j,phi*d+j/phi,j,d,d)",
        "coverage_proof": "Boundary-chain winding additivity; analytic strict convexity of native closed sorted-direction walks; degree-one macro lattice torus"}


def fixture(motifs, macro, periods):
    substitutions = {x: 1, k: 1, y: QQ(1)/2, f: 2}
    assert 1+1/QQbar(phi) < 2 < 2*QQbar(phi)
    assert 0 < QQ(1)/2 < 1+2/QQbar(phi)
    p = [[QQbar(R(q).subs(substitutions)) for q in polygon] for polygon in motifs]
    u, v = [QQbar(R(q).subs(substitutions)) for q in periods]
    def cr(p, q):
        return AA((p.conjugate()*q).imag())
    def ar(p):
        return sum(cr(p[j], p[(j+1) % len(p)]) for j in range(len(p)))/2 if len(p) >= 3 else AA(0)
    def clean(p):
        out = []
        for q in p:
            if not out or out[-1] != q:
                out.append(q)
        if len(out) > 1 and out[0] == out[-1]:
            out.pop()
        return out
    def intersect(first, second):
        out = list(first)
        for j, origin in enumerate(second):
            edge = second[(j+1) % 5]-origin
            if not out:
                break
            previous = out[-1]
            previous_height = cr(edge, previous-origin)
            result = []
            for current in out:
                height = cr(edge, current-origin)
                if (height >= 0) != (previous_height >= 0):
                    result.append(previous+QQbar(previous_height/(previous_height-height))*(current-previous))
                if height >= 0:
                    result.append(current)
                previous, previous_height = current, height
            out = clean(result)
        return out
    determinant = cr(u, v)
    assert determinant > 0 and sum(map(ar, p)) == determinant
    for polygon in p:
        for j, origin in enumerate(polygon):
            edge = polygon[(j+1) % 5]-origin
            assert all(cr(edge, q-origin) > 0 for h, q in enumerate(polygon)
                       if h not in (j, (j+1) % 5))
    boxes = []
    for polygon in p:
        coordinates = [(cr(q, v)/determinant, cr(u, q)/determinant) for q in polygon]
        boxes.append([(min(q[h] for q in coordinates), max(q[h] for q in coordinates))
                      for h in range(2)])
    comparisons = []
    for i, j in product(range(4), repeat=2):
        ranges = [range(int(ceil(boxes[i][h][0]-boxes[j][h][1])),
                        int(floor(boxes[i][h][1]-boxes[j][h][0]))+1) for h in range(2)]
        for n, t in product(*ranges):
            if i == j and n == t == 0:
                continue
            assert ar(intersect(p[i], [q+n*u+t*v for q in p[j]])) == 0
            comparisons.append([i, j, n, t])
    def coefficients(q):
        return [str(s) for s in K(q).list()]
    return {"parameters": {"x": "1", "k": "1", "y": "1/2", "f": "2"},
            "A_lengths": ["1", "3phi-1/2", "1/2", "2+phi/2", "2"],
            "B_lengths": ["1", "2", "2phi-2", "phi-1", "1"],
            "motif_cyclotomic_coefficients": [[coefficients(q) for q in polygon] for polygon in p],
            "period_cyclotomic_coefficients": list(map(coefficients, (u, v))),
            "complete_lattice_clipping_comparisons": comparisons,
            "comparison_count": len(comparisons), "all_intersection_areas_zero": True}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    motifs, macro, periods, formal = construct()
    result = {"status": "exact formal identities and completed fixture checks; independent proof review retained in lemma",
              "field": "Q(z), z=exp(pi*i/5), z^4-z^3+z^2-z+1=0",
              "formal_four_parameter_family": formal,
              "asymmetric_fixture": fixture(motifs, macro, periods)}
    rendered = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
