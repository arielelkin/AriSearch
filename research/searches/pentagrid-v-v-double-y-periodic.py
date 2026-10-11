#!/usr/bin/env python3
"""Exact four-V dissection of a centrally symmetric lattice hexagon.

The double-Y patch and whole-family containment/disjointness are symbolic.
The fixture's complete lattice comparisons use exact separating axes.
Normal invocation writes no file; --output explicitly retains a certificate.
"""
import argparse
import json
from itertools import combinations, product
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, RIF, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
R = PolynomialRing(K, ('a', 'k'))
a, k = R.gens()


def conj(p):
    return R({monomial: value.conjugate()
              for monomial, value in R(p).dict().items()})


def ncross(p, q):
    return (conj(p)*q-p*conj(q))/(z-z.conjugate())


def narea(p):
    return sum(ncross(p[j], p[(j+1) % len(p)]) for j in range(len(p)))/2


def nonnegative(p):
    return all(QQbar(c).imag() == 0 and QQbar(c).real() >= 0
               for c in R(p).coefficients())


def k_coefficients(p):
    values = K(p).list()
    return [str(values[j]) if j < len(values) else '0' for j in range(4)]


def linear_coefficients(p):
    assert {tuple(m) for m in R(p).dict()} <= {(1, 0), (0, 1)}
    return [k_coefficients(R(p).monomial_coefficient(a)),
            k_coefficients(R(p).monomial_coefficient(k))]


def symbolic():
    r = 2*phi*a+k
    e = phi*a+k/phi
    y, t = e+k, r+a
    macro = [0, a, a+y*z, a+y*z+t*z**2, y*z+t*z**2, t*z**2]
    X, Y = r*z**2, a+e*z
    J = X-a*z**4
    J2, X2, Y2 = macro[3]-J, macro[3]-X, macro[3]-Y
    A = [J, X, macro[0], macro[1], Y]
    B = [J2, J, Y, macro[2], X2]
    motifs = [A, [macro[3]-p for p in A],
              B, [macro[3]-p for p in B]]
    assert J2-J == k
    assert X2 == macro[2]+a*z**2
    assert Y-J == -e*z**3
    for polygon, lengths, directions in (
            (A, [a, r, a, e, e], [4, 7, 0, 1, 3]),
            (B, [k, e, k, a, a], [5, 8, 1, 2, 4])):
        assert [polygon[(j+1) % 5]-polygon[j] for j in range(5)] == [
            length*z**direction for length, direction in zip(lengths, directions)]
    assert r == 2*phi*a+phi**2*(k/phi**2)
    assert e == phi*(a+k/phi**2)
    assert e == 2*phi*k+phi**2*(a/phi-k)
    assert a == phi*(k+a/phi-k)
    support_count = 0
    for polygon in (A, B, macro):
        for j, point in enumerate(polygon):
            edge = polygon[(j+1) % len(polygon)]-point
            for h, other in enumerate(polygon):
                if h in (j, (j+1) % len(polygon)):
                    continue
                support = ncross(edge, other-point)
                assert support != 0 and nonnegative(support)
                support_count += 1
    assert support_count == 54
    # All120 containment support polynomials have nonnegative coefficients.
    for polygon in motifs:
        for point in polygon:
            for j, p in enumerate(macro):
                assert nonnegative(ncross(macro[(j+1) % 6]-p, point-p))
    separation_witnesses = []
    for i, j in combinations(range(4), 2):
        witness = None
        for first, second in ((i, j), (j, i)):
            for h, p in enumerate(motifs[first]):
                edge = motifs[first][(h+1) % 5]-p
                if all(nonnegative(-ncross(edge, q-p)) for q in motifs[second]):
                    witness = [i, j, first, h]
                    break
            if witness is not None:
                break
        assert witness is not None, (i, j)
        separation_witnesses.append(witness)
    seams = [(0, 0, 3, 4), (0, 4, 2, 1),
             (1, 0, 2, 4), (1, 4, 3, 1), (2, 0, 3, 0)]
    used = set()
    for i, h, j, g in seams:
        assert motifs[i][h] == motifs[j][(g+1) % 5]
        assert motifs[i][(h+1) % 5] == motifs[j][g]
        assert (i, h) not in used and (j, g) not in used
        used |= {(i, h), (j, g)}
    boundary = [[(0, 2)], [(0, 3), (2, 2)], [(2, 3), (1, 1)],
                [(1, 2)], [(1, 3), (3, 2)], [(3, 3), (0, 1)]]
    for h, chain in enumerate(boundary):
        point = macro[h]
        for i, g in chain:
            assert motifs[i][g] == point
            point = motifs[i][(g+1) % 5]
            assert (i, g) not in used
            used.add((i, g))
        assert point == macro[(h+1) % 6]
    assert len(used) == 20
    area_A = (3*phi+2)*a**2+2*phi*a*k+(phi-1)*k**2/2
    area_B = phi*a**2/2+phi**2*a*k+k**2/2
    expected = (7*phi+4)*a**2+(6*phi+2)*a*k+phi*k**2
    assert narea(A) == area_A
    assert narea(B) == area_B
    assert sum(narea(p) for p in motifs) == narea(macro) == expected
    u, v = macro[2], macro[4]
    assert ncross(u, v) == expected == a*y+phi*a*t+y*t
    # The central hexagon's three whole-edge lattice identifications.
    hex_seams = [(0, 3, 0, -1), (1, 4, 1, -1), (2, 5, 1, 0)]
    for h, g, n, m in hex_seams:
        assert macro[h] == macro[(g+1) % 6]+n*u+m*v
        assert macro[(h+1) % 6] == macro[g]+n*u+m*v
    hex_mates, hex_shifts = {}, {}
    for h, g, n, m in hex_seams:
        hex_mates[h], hex_mates[g] = g, h
        hex_shifts[h], hex_shifts[g] = (n, m), (-n, -m)
    remaining, hex_links = set(range(6)), []
    macro_angles = [2, 4, 4, 2, 4, 4]
    while remaining:
        start = min(remaining)
        current, link, shift_sum = start, [], [0, 0]
        while current not in link:
            remaining.remove(current)
            link.append(current)
            n, m = hex_shifts[current]
            shift_sum[0] += n
            shift_sum[1] += m
            current = (hex_mates[current]+1) % 6
        assert current == start and shift_sum == [0, 0]
        assert sum(macro_angles[j] for j in link) == 10
        hex_links.append(link)
    assert hex_links == [[0, 4, 2], [1, 5, 3]]
    assert r-a != 0
    return motifs, macro, u, v, {
        'domain': 'a>0,0<k<a/phi',
        'A_mirror_V_parameters': ['a', 'k/phi^2'],
        'B_mirror_V_parameters': ['k', 'a/phi-k'],
        'A_lengths': ['a', '2*phi*a+k', 'a', 'phi*a+k/phi', 'phi*a+k/phi'],
        'B_lengths': ['k', 'phi*a+k/phi', 'k', 'a', 'a'],
        'native_vertex_angles_pi_over_5': [4, 2, 2, 4, 3],
        'formal_motif_coefficients_a_k': [[linear_coefficients(p) for p in poly] for poly in motifs],
        'formal_macro_coefficients_a_k': [linear_coefficients(p) for p in macro],
        'formal_period_coefficients_a_k': [linear_coefficients(u), linear_coefficients(v)],
        'internal_reversed_seams': seams,
        'outer_macro_side_chains': boundary,
        'universal_strict_support_polynomials': support_count,
        'universal_macro_containment_polynomials': 120,
        'universal_pair_separation_edges': separation_witnesses,
        'formal_normalized_A_area': str(area_A),
        'formal_normalized_B_area': str(area_B),
        'formal_normalized_macro_area_and_determinant': str(expected),
        'whole_hexagon_lattice_seams': hex_seams,
        'whole_hexagon_corner_links': hex_links,
        'all_macro_link_integer_shift_sums_zero': True,
        'macro_vertex_angles_pi_over_5': macro_angles,
        'partial_contact_mismatch': 'macro side2 subdivision distances a versus r=2*phi*a+k',
    }


def enc(x):
    x = AA(x)
    if x in QQ:
        return {'rational': str(QQ(x))}
    polynomial = x.minpoly()
    iv = x.interval(RIF)
    lo, hi = iv.lower().exact_rational(), iv.upper().exact_rational()
    assert sum(lo < root < hi for root in polynomial.roots(AA, multiplicities=False)) == 1
    return {'polynomial_coefficients': [str(QQ(t)) for t in polynomial.list()],
            'isolating_interval': [str(lo), str(hi)]}


def fixture(motifs, macro, u, v):
    kval = AA(QQbar(phi**-2))
    assert 0 < kval < AA(QQbar(phi**-1))
    def evaluate(p):
        return sum(QQbar(value)*QQbar(kval)**monomial[1]
                   for monomial, value in R(p).dict().items())
    polygons = [[evaluate(p) for p in poly] for poly in motifs]
    outer = list(map(evaluate, macro))
    periods = list(map(evaluate, (u, v)))
    def cross(p, q):
        return AA((p.conjugate()*q).imag())
    def area(poly):
        return sum(cross(poly[j], poly[(j+1) % len(poly)]) for j in range(len(poly)))/2
    det = cross(*periods)
    assert det > 0 and sum(map(area, polygons)) == area(outer) == det
    def separated(p, q):
        for poly in (p, q):
            for j, x in enumerate(poly):
                edge = poly[(j+1) % len(poly)]-x
                first, second = [cross(edge, w) for w in p], [cross(edge, w) for w in q]
                if max(first) <= min(second) or max(second) <= min(first):
                    return True
        return False
    lattice = [[(cross(p, periods[1])/det, cross(periods[0], p)/det) for p in poly]
               for poly in polygons]
    comparisons = []
    for i, j in product(range(4), repeat=2):
        ranges = [range(int(ceil(min(p[h] for p in lattice[i])-max(p[h] for p in lattice[j]))),
                        int(floor(max(p[h] for p in lattice[i])-min(p[h] for p in lattice[j])))+1)
                  for h in (0, 1)]
        for n, m in product(*ranges):
            if i == j and n == m == 0:
                continue
            translated = [p+n*periods[0]+m*periods[1] for p in polygons[j]]
            assert separated(polygons[i], translated), (i, j, n, m)
            comparisons.append([i, j, n, m])
    def point(p):
        return [enc(QQbar(p).real()), enc(QQbar(p).imag())]
    return {'a': enc(1), 'k': enc(kval),
            'motifs': [[point(p) for p in poly] for poly in polygons],
            'macro': list(map(point, outer)), 'periods': list(map(point, periods)),
            'areas': [enc(area(poly)) for poly in polygons], 'determinant': enc(det),
            'complete_lattice_overlap_comparisons': comparisons,
            'comparison_count': len(comparisons)}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Run without Python -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    motifs, macro, u, v, formal = symbolic()
    result = {'status': 'exact formal identities and completed fixture checks; independent proof review retained in lemma',
              'field': 'Q(z), z=exp(pi*i/5), z^4-z^3+z^2-z+1=0',
              'formal_family': formal, 'exact_fixture': fixture(motifs, macro, u, v)}
    rendered = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end='')
