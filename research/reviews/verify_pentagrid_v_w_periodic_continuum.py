#!/usr/bin/env python3
"""Independent whole-family coefficient and irrational-fixture clipping audit.

No author script is imported.  Shapes are reconstructed from native sides,
all formal assertions are polynomial identities, and actual intersections
are independently clipped over exact real/complex algebraic fields.
"""
import argparse
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
R = PolynomialRing(K, ("b", "c"))
b, c = R.gens()


def conjugate(p):
    return R({monomial: coefficient.conjugate()
              for monomial, coefficient in R(p).dict().items()})


def cross_formal(a, b):
    return (conjugate(a)*b-a*conjugate(b))/(z-z.conjugate())


def area_formal(p):
    return sum(cross_formal(p[i], p[(i+1) % len(p)])
               for i in range(len(p)))/2


def native_vertices(lengths, directions):
    points = [R(0)]
    for length, direction in zip(lengths, directions):
        points.append(points[-1]+length*z**direction)
    assert points[-1] == 0
    return points[:-1]


def k_vector(a):
    coefficients = K(a).list()
    return [str(coefficients[i]) if i < len(coefficients) else "0"
            for i in range(4)]


def linear_coefficients(p):
    p = R(p)
    assert {tuple(monomial) for monomial in p.dict()} <= {(1, 0), (0, 1)}
    return [k_vector(p.monomial_coefficient(b)),
            k_vector(p.monomial_coefficient(c))]


def cross(a, b):
    return AA((a.conjugate()*b).imag())


def area(p):
    if len(p) < 3:
        return AA(0)
    return sum(cross(p[i], p[(i+1) % len(p)])
               for i in range(len(p)))/2


def evaluate(p, chosen_c):
    return sum(QQbar(coefficient)*QQbar(chosen_c)**monomial[1]
               for monomial, coefficient in R(p).dict().items())


def clean_polygon(p):
    out = []
    for point in p:
        if not out or point != out[-1]:
            out.append(point)
    if len(out) > 1 and out[-1] == out[0]:
        out.pop()
    return out


def convex_intersection(subject, clip):
    """Sutherland-Hodgman intersection, including exact boundary contacts."""
    out = list(subject)
    for i, a in enumerate(clip):
        edge = clip[(i+1) % len(clip)]-a
        if not out:
            break
        previous = out[-1]
        previous_height = cross(edge, previous-a)
        result = []
        for current in out:
            height = cross(edge, current-a)
            if (height >= 0) != (previous_height >= 0):
                fraction = previous_height/(previous_height-height)
                assert 0 <= fraction <= 1
                result.append(previous+QQbar(fraction)*(current-previous))
            if height >= 0:
                result.append(current)
            previous, previous_height = current, height
        out = clean_polygon(result)
    return out


def exact_saved_real(record):
    if "rational" in record:
        return AA(QQ(record["rational"]))
    polynomial = PolynomialRing(QQ, "x")(
        [QQ(v) for v in record["polynomial_coefficients"]])
    lo, hi = map(QQ, record["isolating_interval"])
    roots = [r for r in polynomial.roots(AA, multiplicities=False)
             if lo < r < hi]
    assert len(roots) == 1, record
    return roots[0]


def exact_saved_complex(record):
    return QQbar(exact_saved_real(record[0]))+QQbar.gen()*exact_saved_real(record[1])


def cycle_representative(cycle):
    cycle = tuple(tuple(corner) for corner in cycle)
    return min(cycle[i:]+cycle[:i] for i in range(len(cycle)))


def certificate(author_certificate):
    embedded_z = QQbar(z)
    assert embedded_z.imag() > 0
    assert QQ(4)/5 < embedded_z.real() < QQ(81)/100
    E = phi*(b+c)
    D = 2*phi*b+phi**2*c
    H = 2*b+phi**2*c
    # Independent reconstruction starts from the native pentagon walks,
    # rather than accepting author motif coordinates from the certificate.
    native_V = native_vertices([b, D, b, E, E], [0, 3, 6, 7, 9])
    W = native_vertices([b, H, b, E, E], [0, 2, 4, 6, 8])
    Q = native_vertices([b, E, E, b, b, E, E, b],
                        [0, 1, 3, 4, 5, 6, 8, 9])
    assert Q[4] == D*z**2
    assert all(Q[(j+4) % 8] == Q[4]-Q[j] for j in range(8))
    V = [Q[3]+z**4*p for p in native_V]
    assert V == [Q[3], Q[4], Q[0], Q[1], Q[2]]
    assert W[3] == phi*E*z**2
    motifs = [V, [Q[4]-p for p in V], [b-p for p in W],
              [Q[5]+p for p in W]]
    u = 2*b+E*z-D*z**2
    v = 2*phi*E*z**2
    # Every strict support polynomial has nonnegative real coefficients
    # and is nonzero. This certifies the WHOLE positive domain b,c>0.
    formal_support_tests = 0
    for polygon in (native_V, W, Q):
        for i, point in enumerate(polygon):
            edge = polygon[(i+1) % len(polygon)]-point
            for j, other in enumerate(polygon):
                if j in (i, (i+1) % len(polygon)):
                    continue
                support = cross_formal(edge, other-point)
                assert support != 0
                assert all(QQbar(t).imag() == 0 and QQbar(t).real() >= 0
                           for t in support.coefficients())
                formal_support_tests += 1
    assert formal_support_tests == 78
    seams = [(0, 1, 1, 1, 0, 0), (0, 2, 2, 0, 0, 0),
             (0, 3, 1, 3, 1, 0), (0, 4, 3, 4, 1, 0),
             (0, 0, 2, 2, 0, 1), (1, 2, 3, 0, 0, 0),
             (1, 4, 2, 4, -1, 0), (1, 0, 3, 2, 0, -1),
             (2, 1, 3, 1, 0, -1), (2, 3, 3, 3, 1, -1)]
    mates, shifts = {}, {}
    neighbors = {i: set() for i in range(4)}
    for i, a, j, d, n, m in seams:
        assert motifs[i][a] == motifs[j][(d+1) % 5]+n*u+m*v
        assert motifs[i][(a+1) % 5] == motifs[j][d]+n*u+m*v
        assert (i, a) not in mates and (j, d) not in mates
        mates[i, a], mates[j, d] = (j, d), (i, a)
        shifts[i, a], shifts[j, d] = (n, m), (-n, -m)
        neighbors[i].add(j)
        neighbors[j].add(i)
    assert len(mates) == 20
    reached, frontier = {0}, [0]
    while frontier:
        for j in neighbors[frontier.pop()]:
            if j not in reached:
                reached.add(j)
                frontier.append(j)
    assert reached == set(range(4))
    remaining, links = set(mates), []
    angles = [[4, 2, 2, 4, 3], [4, 2, 2, 4, 3], [3]*5, [3]*5]
    while remaining:
        start = min(remaining)
        current, link, total_shift = start, [], [0, 0]
        while current not in link:
            assert current in remaining
            remaining.remove(current)
            link.append(current)
            n, m = shifts[current]
            total_shift[0] += n
            total_shift[1] += m
            j, d = mates[current]
            current = (j, (d+1) % 5)
        assert current == start and total_shift == [0, 0]
        assert sum(angles[i][a] for i, a in link) == 10
        links.append(link)
    assert len(links) == 6
    angle_multisets = [sorted(angles[i][a] for i, a in link) for link in links]
    assert angle_multisets.count([2, 2, 3, 3]) == 2
    assert angle_multisets.count([3, 3, 4]) == 4
    assert len(links)-len(seams)+len(motifs) == 0
    V_area = (3*phi+2)*b**2+(4*phi+2)*b*c+(phi+QQ(1)/2)*c**2
    W_area = (3*phi+1)*b**2+(4*phi+2)*b*c+(phi+QQ(1)/2)*c**2
    determinant = 2*phi**3*(b+c)*(3*b+c)
    assert area_formal(V) == V_area
    assert area_formal(W) == W_area
    assert area_formal(Q) == 2*V_area
    assert cross_formal(u, v) == determinant
    assert sum(area_formal(p) for p in motifs) == determinant
    saved = json.loads(author_certificate.read_text())
    symbolic = saved['symbolic_family']
    assert [[linear_coefficients(p) for p in poly] for poly in motifs] == symbolic['formal_motif_coefficients_b_c']
    assert list(map(linear_coefficients, (u, v))) == symbolic['formal_lattice_coefficients_b_c']
    assert {cycle_representative(link) for link in links} == {
        cycle_representative(link) for link in symbolic['ordered_corner_links']}
    assert [[n, m] for i, a, j, d, n, m in seams] == symbolic['seam_integer_shifts']
    assert [[i, a, j, d] for i, a, j, d, n, m in seams] == symbolic['side_pairs']
    assert angles == symbolic['vertex_angles_in_pi_over_5']
    for form, coefficients in zip((V_area, W_area), symbolic['quadratic_normalized_area_coefficients_b2_bc_c2_V_W']):
        assert [K(t) for t in coefficients] == [form.monomial_coefficient(b**2), form.monomial_coefficient(b*c), form.monomial_coefficient(c**2)]
    root2 = AA(2).sqrt()
    assert QQ(7)/5 < root2 < QQ(3)/2
    assert list(root2.minpoly()) == [-2, 0, 1]
    polys = [[evaluate(p, root2) for p in poly] for poly in motifs]
    periods = [evaluate(p, root2) for p in (u, v)]
    det = cross(*periods)
    areas = list(map(area, polys))
    assert det > 0 and sum(areas) == det
    for polygon in polys:
        for i, a in enumerate(polygon):
            edge = polygon[(i+1) % 5]-a
            assert all(cross(edge, polygon[j]-a) > 0
                       for j in range(5) if j not in (i, (i+1) % 5))
    fixture = saved['irrational_fixture']
    assert exact_saved_real(fixture['b']) == 1
    assert exact_saved_real(fixture['c']) == root2
    assert [exact_saved_complex(p) for p in fixture['lattice']] == periods
    assert [[exact_saved_complex(p) for p in poly] for poly in fixture['motifs']] == polys
    assert [exact_saved_real(a) for a in fixture['areas']] == areas
    assert exact_saved_real(fixture['determinant']) == det

    def coordinates(p):
        return cross(p, periods[1])/det, cross(periods[0], p)/det

    boxes = []
    for poly in polys:
        coords = list(map(coordinates, poly))
        boxes.append([(min(p[k] for p in coords), max(p[k] for p in coords))
                      for k in range(2)])
    comparisons = []
    for i, first in enumerate(polys):
        for j, second in enumerate(polys):
            n_lo = ceil(boxes[i][0][0]-boxes[j][0][1])
            n_hi = floor(boxes[i][0][1]-boxes[j][0][0])
            m_lo = ceil(boxes[i][1][0]-boxes[j][1][1])
            m_hi = floor(boxes[i][1][1]-boxes[j][1][0])
            for n in range(int(n_lo), int(n_hi)+1):
                for m in range(int(m_lo), int(m_hi)+1):
                    if i == j and n == m == 0:
                        continue
                    translated = [p+n*periods[0]+m*periods[1] for p in second]
                    intersection = convex_intersection(first, translated)
                    assert area(intersection) == 0, (i, j, n, m)
                    comparisons.append([i, j, n, m])
    assert sorted(comparisons) == sorted(fixture['complete_overlap_comparisons'])
    assert len(comparisons) == fixture['comparison_count'] == 32
    return {'status': 'VALID',
            'scope': 'whole b,c>0 family: formal identities and global positivity; irrational fixture independently clipped',
            'whole_domain_strict_support_polynomial_checks': formal_support_tests,
            'native_V_and_W_closure_formal': True,
            'convex_central_octagon_and_exact_V_dimer': True,
            'all_20_seam_endpoints_formally_equal': True,
            'ordered_corner_links': links,
            'all_link_translation_sums_zero': True,
            'vertex_angle_multisets_pi_over_5': angle_multisets,
            'surface_euler_characteristic': 0,
            'formal_area_V': str(V_area),
            'formal_area_W': str(W_area),
            'formal_determinant': str(determinant),
            'source_target_area_identity_formal': True,
            'author_certificate_coordinates_and_isolations_match': True,
            'fixture_complete_integer_translation_domain': comparisons,
            'fixture_exact_polygon_clipping_tests': len(comparisons),
            'fixture_every_intersection_area_zero': True,
            'fixture_strict_support_checks': 60,
            'conclusion': 'The compact local-isometry quotient has degree1 by exact area; V/W admits the specified doubly periodic tiling for every b,c>0.'}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Run without Python -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author-certificate', type=Path,
                        default=Path(__file__).parents[1]/'certificates'/'pentagrid-v-w-periodic-continuum.json')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(certificate(args.author_certificate), indent=2)+'\n'
    if args.output:
        args.output.write_text(value)
    else:
        print(value, end='')
