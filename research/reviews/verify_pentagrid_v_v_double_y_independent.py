#!/usr/bin/env python3
"""Independent formal geometry and exact lattice-clipping audit of double-Y V/V.

No producer code is imported. Native edge walks independently reconstruct the
children and derive the hexagon from their exposed sides. Formal support and
containment certify every a,k>0, while the author's fixture is decoded and its
complete intersection domain is recomputed with convex clipping.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z + z**-1
R = PolynomialRing(K, ("a", "k"))
a, k = R.gens()


def conjugate(p):
    return R({tuple(exponent): value.conjugate()
              for exponent, value in R(p).dict().items()})


def cross_formal(p, q):
    return (conjugate(p)*q-p*conjugate(q))/(z-z.conjugate())


def area_formal(p):
    return sum(cross_formal(p[j], p[(j+1) % len(p)])
               for j in range(len(p)))/2


def native_walk(lengths, directions):
    p = [R(0)]
    for length, direction in zip(lengths, directions):
        p.append(p[-1] + length*z**direction)
    assert p[-1] == 0
    return p[:-1]


def positive_coefficients(p, strict=False):
    p = R(p)
    assert all(QQbar(value).imag() == 0 and QQbar(value).real() >= 0
               for value in p.coefficients()), p
    if strict:
        assert p != 0


def vector(value):
    coefficients = K(value).list()
    return [str(coefficients[j]) if j < len(coefficients) else "0"
            for j in range(4)]


def linear_vector(p):
    p = R(p)
    assert {tuple(t) for t in p.dict()} <= {(1, 0), (0, 1)}
    return [vector(p.monomial_coefficient(a)), vector(p.monomial_coefficient(k))]


def cross(p, q):
    return AA((p.conjugate()*q).imag())


def area(p):
    return (sum(cross(p[j], p[(j+1) % len(p)]) for j in range(len(p)))/2
            if len(p) >= 3 else AA(0))


def clean(p):
    result = []
    for q in p:
        if not result or q != result[-1]:
            result.append(q)
    if len(result) > 1 and result[0] == result[-1]:
        result.pop()
    return result


def intersection(subject, clip):
    result = list(subject)
    for j, origin in enumerate(clip):
        if not result:
            break
        edge = clip[(j+1) % len(clip)]-origin
        previous = result[-1]
        previous_height = cross(edge, previous-origin)
        out = []
        for current in result:
            height = cross(edge, current-origin)
            if (height >= 0) != (previous_height >= 0):
                fraction = previous_height/(previous_height-height)
                assert 0 <= fraction <= 1
                out.append(previous + QQbar(fraction)*(current-previous))
            if height >= 0:
                out.append(current)
            previous, previous_height = current, height
        result = clean(out)
    return result


def decode_real(record):
    if "rational" in record:
        return AA(QQ(record["rational"]))
    polynomial = PolynomialRing(QQ, "x")(
        [QQ(q) for q in record["polynomial_coefficients"]])
    lo, hi = map(QQ, record["isolating_interval"])
    candidates = [root for root in polynomial.roots(AA, multiplicities=False)
                  if lo < root < hi]
    assert len(candidates) == 1
    return candidates[0]


def decode_complex(record):
    return QQbar(decode_real(record[0])) + QQbar.gen()*decode_real(record[1])


def evaluate(p, kval):
    return sum(QQbar(value)*QQbar(kval)**exponent[1]
               for exponent, value in R(p).dict().items())


def verify(path):
    assert QQbar(z).imag() > 0 and QQ(4)/5 < QQbar(z).real() < QQ(81)/100
    assert phi**2 == phi+1
    # The general mirror-V native closure has exactly this single relation.
    assert 1+z**6 == -z**3/phi
    assert z**7+z**9 == -phi*z**3
    r = 2*phi*a+k
    e = phi*a+k/phi
    A_native = native_walk([a, r, a, e, e], [4, 7, 0, 1, 3])
    B_native = native_walk([k, e, k, a, a], [5, 8, 1, 2, 4])
    # Pin exposed A vertex2 at0; the first B edge ends at A vertex0.
    A = [q-A_native[2] for q in A_native]
    B = [q+A[0]+k for q in B_native]
    assert B[1] == A[0] and B[2] == A[4]
    center_twice = A[0]+B[0]
    motifs = [A, [center_twice-q for q in A],
              B, [center_twice-q for q in B]]
    macro = [A[2], A[3], B[3], motifs[1][2], motifs[1][3], motifs[3][3]]
    assert macro == [0, a, a+phi*(a+k)*z,
                     a+phi*(a+k)*z+(phi**3*a+k)*z**2,
                     phi*(a+k)*z+(phi**3*a+k)*z**2,
                     (phi**3*a+k)*z**2]
    assert center_twice == macro[3]
    u, v = macro[2], macro[4]
    support_count = 0
    for polygon in (A, B, macro):
        for j, origin in enumerate(polygon):
            edge = polygon[(j+1) % len(polygon)]-origin
            for h, q in enumerate(polygon):
                if h not in (j, (j+1) % len(polygon)):
                    positive_coefficients(cross_formal(edge, q-origin), strict=True)
                    support_count += 1
    assert support_count == 54
    containment_count = 0
    for polygon in motifs:
        for q in polygon:
            for j, origin in enumerate(macro):
                positive_coefficients(cross_formal(macro[(j+1) % 6]-origin, q-origin))
                containment_count += 1
    assert containment_count == 120
    # Fixed whole-polygon separation tests, independently evaluated.
    separations = [(0, 1, 0, 4), (0, 2, 0, 4), (0, 3, 0, 0),
                   (1, 2, 1, 0), (1, 3, 1, 4), (2, 3, 2, 0)]
    for i, j, first, h in separations:
        second = j if first == i else i
        origin = motifs[first][h]
        edge = motifs[first][(h+1) % 5]-origin
        for q in motifs[second]:
            positive_coefficients(-cross_formal(edge, q-origin))
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
    for j, chain in enumerate(chains):
        point = macro[j]
        for i, h in chain:
            assert motifs[i][h] == point
            assert (i, h) not in used
            used.add((i, h))
            point = motifs[i][(h+1) % 5]
        assert point == macro[(j+1) % 6]
    assert len(used) == 20
    expected = (7*phi+4)*a**2+(6*phi+2)*a*k+phi*k**2
    assert sum(map(area_formal, motifs)) == area_formal(macro) == expected
    assert cross_formal(u, v) == expected
    macro_seams = [(0, 3, 0, -1), (1, 4, 1, -1), (2, 5, 1, 0)]
    mates, shifts = {}, {}
    for h, g, n, m in macro_seams:
        assert macro[h] == macro[(g+1) % 6]+n*u+m*v
        assert macro[(h+1) % 6] == macro[g]+n*u+m*v
        mates[h], mates[g] = g, h
        shifts[h], shifts[g] = (n, m), (-n, -m)
    remaining, links = set(range(6)), []
    angles = [2, 4, 4, 2, 4, 4]
    while remaining:
        start = min(remaining)
        current, link, total_shift = start, [], [0, 0]
        while current not in link:
            assert current in remaining
            remaining.remove(current)
            link.append(current)
            total_shift = [total_shift[h]+shifts[current][h] for h in range(2)]
            current = (mates[current]+1) % 6
        assert current == start and total_shift == [0, 0]
        assert sum(angles[j] for j in link) == 10
        links.append(link)
    assert links == [[0, 4, 2], [1, 5, 3]]
    assert len(links)-len(macro_seams)+1 == 0
    # Actual partial contact across macro side2: a and r never coincide.
    assert macro[2]+r*z**2 == motifs[0][1]+u
    assert macro[2]+a*z**2 == motifs[2][4]
    positive_coefficients(r-a, strict=True)
    saved = json.loads(path.read_text())
    formal = saved["formal_family"]
    assert [[linear_vector(q) for q in p] for p in motifs] == formal["formal_motif_coefficients_a_k"]
    assert list(map(linear_vector, macro)) == formal["formal_macro_coefficients_a_k"]
    assert list(map(linear_vector, (u, v))) == formal["formal_period_coefficients_a_k"]
    assert [list(q) for q in seams] == formal["internal_reversed_seams"]
    assert [[[i, h] for i, h in row] for row in chains] == formal["outer_macro_side_chains"]
    assert [list(q) for q in macro_seams] == formal["whole_hexagon_lattice_seams"]
    assert links == formal["whole_hexagon_corner_links"]
    kval = AA(QQbar(phi**-2))
    assert 0 < kval < AA(QQbar(phi**-1))
    p = [[evaluate(q, kval) for q in polygon] for polygon in motifs]
    outer = list(map(lambda q: evaluate(q, kval), macro))
    periods = list(map(lambda q: evaluate(q, kval), (u, v)))
    determinant = cross(*periods)
    areas = list(map(area, p))
    assert determinant > 0 and sum(areas) == area(outer) == determinant
    fixture = saved["exact_fixture"]
    assert decode_real(fixture["a"]) == 1
    assert decode_real(fixture["k"]) == kval
    assert [[decode_complex(q) for q in polygon] for polygon in fixture["motifs"]] == p
    assert list(map(decode_complex, fixture["macro"])) == outer
    assert list(map(decode_complex, fixture["periods"])) == periods
    assert list(map(decode_real, fixture["areas"])) == areas
    assert decode_real(fixture["determinant"]) == determinant
    boxes = []
    for polygon in p:
        coordinates = [(cross(q, periods[1])/determinant,
                        cross(periods[0], q)/determinant) for q in polygon]
        boxes.append([(min(q[h] for q in coordinates), max(q[h] for q in coordinates))
                      for h in range(2)])
    comparisons = []
    for i, first in enumerate(p):
        for j, second in enumerate(p):
            ranges = [range(int(ceil(boxes[i][h][0]-boxes[j][h][1])),
                            int(floor(boxes[i][h][1]-boxes[j][h][0]))+1)
                      for h in range(2)]
            for n in ranges[0]:
                for m in ranges[1]:
                    if i == j and n == m == 0:
                        continue
                    translated = [q+n*periods[0]+m*periods[1] for q in second]
                    assert area(intersection(first, translated)) == 0, (i, j, n, m)
                    comparisons.append([i, j, n, m])
    assert sorted(comparisons) == sorted(fixture["complete_lattice_overlap_comparisons"])
    assert len(comparisons) == fixture["comparison_count"] == 44
    return {"status": "VALID",
            "formal_domain_checked": "every a>0,k>0; includes stated 0<k<a/phi subdomain",
            "native_shapes_reconstructed_without_author_imports": True,
            "strict_support_polynomials": support_count,
            "macro_containment_polynomials": containment_count,
            "universal_child_separating_edges": separations,
            "internal_seams": seams, "outer_chains": chains,
            "macro_links": links, "macro_zero_link_shifts": True,
            "all_twenty_native_sides_accounted_once": True,
            "normalized_area_and_determinant": str(expected),
            "partial_contacts_distances": ["a", "r=2phi*a+k"],
            "certificate_coordinates_root_isolations_match": True,
            "complete_clipping_comparisons": comparisons,
            "comparison_count": len(comparisons),
            "all_intersections_area_zero": True,
            "conclusion": "Macro torus has covering degree1; dissection yields periodic two-class tiling for all a,k>0."}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-certificate", type=Path,
                        default=Path(__file__).parents[1]/"certificates"/"pentagrid-v-v-double-y-periodic.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(verify(args.author_certificate), indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
