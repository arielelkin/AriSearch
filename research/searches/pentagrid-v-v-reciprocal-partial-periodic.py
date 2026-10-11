#!/usr/bin/env python3
"""Exact reciprocal mirror-V continuum with partial native-side contacts.

No search is performed. Five prescribed chambers cover all a,k>0. Formal
refined-side identities, complete vertex links and zero lattice holonomy
are checked over Q(z)[a,k]; exact clipping additionally audits five fixtures.
"""
import argparse
import json
from itertools import product
from pathlib import Path
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
R = PolynomialRing(K, ("a", "k"))
a, k = R.gens()
S = PolynomialRing(K, ("s", "t"))
s, t = S.gens()


def conjugate(q):
    return R({tuple(e): c.conjugate() for e, c in R(q).dict().items()})


def cross(q, w):
    return (conjugate(q)*w-q*conjugate(w))/(z-z.conjugate())


def area(p):
    return sum(cross(p[j], p[(j+1) % len(p)]) for j in range(len(p)))/2


def coefficients(q):
    return [str(c) for c in K(q).list()]


def linear_coefficients(q):
    return [coefficients(R(q).monomial_coefficient(v)) for v in (a, k)]


def positive(q, substitution):
    """A sufficient whole-chamber proof, not a sample sign check."""
    result = S(R(q).subs(substitution))
    assert result != 0
    assert all(QQbar(c).imag() == 0 and AA(QQbar(c).real()) > 0
               for c in result.coefficients())


def construct():
    r, f = phi*k+a/phi, phi*a+k/phi
    J, H = r*z**2-a*z**4, 2*(r*z**2-a*z**4)+k
    A = [J, r*z**2, 0, a, a+k*z]
    B = [J+k, J, J-f*z**3, J-f*z**3+k*z,
         J-f*z**3+k*z+a*z**2]
    motifs = [A, [H-q for q in A], B, [H-q for q in B]]
    directions = [[4, 7, 0, 1, 3], [9, 2, 5, 6, 8],
                  [5, 8, 1, 2, 4], [0, 3, 6, 7, 9]]
    lengths = [[a, r, a, k, k], [a, r, a, k, k],
               [k, f, k, a, a], [k, f, k, a, a]]
    for polygon, native_lengths, native_directions in zip(motifs, lengths, directions):
        assert [polygon[(h+1) % 5]-polygon[h] for h in range(5)] == [
            length*z**direction for length, direction in zip(native_lengths, native_directions)]
        for h, origin in enumerate(polygon):
            edge = polygon[(h+1) % 5]-origin
            for g, point in enumerate(polygon):
                if g not in (h, (h+1) % 5):
                    positive(cross(edge, point-origin), {a: s, k: t})
    U, V = B[3], H-a
    assert U-V == A[4]+B[2]-H
    assert H-U == (r+a)*z**2
    assert area(A) == (a*a+2*phi**2*a*k+phi*k*k)/2
    assert area(B) == (k*k+2*phi**2*a*k+phi*a*a)/2
    assert cross(U, V) == phi**2*(a*a+4*a*k+k*k)
    assert sum(map(area, motifs)) == cross(U, V)
    return motifs, directions, (U, V), (r, f, J)


CHAMBERS = [
    ("low", {a: phi**3*s+t, k: s}, {a: 10, k: 1}, "r<a; k<f"),
    ("lower_boundary", {a: s, k: phi**-3*s}, {a: 1, k: phi**-3}, "r=a; k<f"),
    ("middle", {a: s+t, k: phi**-3*s+phi**3*t}, {a: 1, k: 2}, "r>a; k<f"),
    ("upper_boundary", {a: s, k: phi**3*s}, {a: 1, k: phi**3}, "r>a; k=f"),
    ("high", {a: s, k: phi**3*s+t}, {a: 1, k: 10}, "r>a; k>f")]


def chamber(name, substitution, sample, signs, motifs, directions, periods, aux):
    U, V = periods
    r, f, J = aux
    seams = []
    # A seam records two occurrences on a common line. Translation indices
    # place each occurrence on that line; native polygons are never altered.
    def add(first, second, start, end):
        assert start != end
        seams.append((first, second, R(start), R(end)))
    full = [(0, 0, 3, 4, 0, 0), (1, 0, 2, 4, 0, 0),
            (2, 0, 3, 0, 0, 0), (0, 2, 1, 2, 0, -1),
            (0, 3, 3, 2, 1, -1), (1, 3, 2, 2, -1, 1)]
    for i, h, j, g, n, m in full:
        add((i, h, 0, 0), (j, g, n, m), motifs[i][h], motifs[i][(h+1) % 5])
    # L2: A0.D=[0,r], B0.a-U=[0,a], A1.D-U=[a,r+a],
    # B1.a=[r,r+a], coordinate q*z^2. Opposite directions match.
    A0, B0, A1, B1 = (0, 1, 0, 0), (2, 3, -1, 0), (1, 1, -1, 0), (3, 3, 0, 0)
    if name == "low":
        rows = [(A0, B0, 0, r), (B1, B0, r, a), (B1, A1, a, r+a)]
    elif name == "lower_boundary":
        rows = [(A0, B0, 0, a), (B1, A1, a, r+a)]
    else:
        rows = [(A0, B0, 0, a), (A0, A1, a, r), (B1, A1, r, r+a)]
    for first, second, lo, hi in rows:
        positive(R(hi)-R(lo), substitution)
        add(first, second, R(lo)*z**2, R(hi)*z**2)
    # L3: A0.k=[-k,0], B0.D=[-f,0], A1.k+U-V=[-k-f,-f],
    # B1.D+U-V=[-k-f,-k], coordinate J+q*z^3.
    A0, B0, A1, B1 = (0, 4, 0, 0), (2, 1, 0, 0), (1, 4, 1, -1), (3, 1, 1, -1)
    if name == "high":
        rows = [(A0, B0, -f, 0), (A0, A1, -k, -f), (B1, A1, -k-f, -k)]
    elif name == "upper_boundary":
        rows = [(A0, B0, -k, 0), (B1, A1, -k-f, -f)]
    else:
        rows = [(A0, B0, -k, 0), (B1, B0, -f, -k), (B1, A1, -k-f, -f)]
    for first, second, lo, hi in rows:
        positive(R(hi)-R(lo), substitution)
        add(first, second, J+R(lo)*z**3, J+R(hi)*z**3)

    # Formal boundary parameters before substitution are retained. On a
    # coalescence boundary, first restrict all identities to its closed ray.
    def restrict(q):
        if name == "lower_boundary":
            return R(q).subs({k: phi**-3*a})
        if name == "upper_boundary":
            return R(q).subs({k: phi**3*a})
        return R(q)
    cuts = {(i, h): {restrict(motifs[i][h]), restrict(motifs[i][(h+1) % 5])}
            for i in range(4) for h in range(5)}
    for first, second, start, end in seams:
        for i, h, n, m in (first, second):
            shift = n*U+m*V
            for point in (start-shift, end-shift):
                point = restrict(point)
                assert cross(point-restrict(motifs[i][h]), z**directions[i][h]) == 0
                cuts[i, h].add(point)
    refined = []
    provenance = []
    for i in range(4):
        points, labels = [], []
        for h in range(5):
            origin = restrict(motifs[i][h])
            parameters = [(R((point-origin)/z**directions[i][h]), point) for point in cuts[i, h]]
            parameters.sort(key=lambda item: AA(QQbar(item[0].subs(sample)).real()))
            assert parameters[0][1] == origin
            assert parameters[-1][1] == restrict(motifs[i][(h+1) % 5])
            for j in range(len(parameters)-1):
                positive(parameters[j+1][0]-parameters[j][0], substitution)
                points.append(parameters[j][1])
                labels.append((h, 4 if h in (0, 3) else 2 if h in (1, 2) else 3)
                              if j == 0 else (h, 5))
        refined.append(points)
        provenance.append(labels)
    partners = {}
    retained_seams = []
    for first, second, start, end in seams:
        edges = []
        for i, h, n, m in (first, second):
            endpoints = {restrict(start-n*U-m*V), restrict(end-n*U-m*V)}
            candidates = [g for g in range(len(refined[i]))
                          if provenance[i][g][0] == h and
                          {refined[i][g], refined[i][(g+1) % len(refined[i])]} == endpoints]
            assert len(candidates) == 1
            edges.append((i, candidates[0], n, m))
        i, h, n, m = edges[0]
        j, g, q, w = edges[1]
        d = (q-n, w-m)
        assert refined[i][h] == refined[j][(g+1) % len(refined[j])]+restrict(d[0]*U+d[1]*V)
        assert refined[i][(h+1) % len(refined[i])] == refined[j][g]+restrict(d[0]*U+d[1]*V)
        assert (i, h) not in partners and (j, g) not in partners
        partners[i, h] = (j, g, *d)
        partners[j, g] = (i, h, -d[0], -d[1])
        retained_seams.append([i, h, j, g, *d])
    assert len(partners) == sum(map(len, refined))
    remaining = set(partners)
    links = []
    while remaining:
        initial = min(remaining)
        current = initial
        cycle, total, displacement = [], 0, [0, 0]
        while current in remaining:
            remaining.remove(current)
            i, h = current
            cycle.append([i, h, provenance[i][h][0], provenance[i][h][1]])
            total += provenance[i][h][1]
            j, g, n, m = partners[i, h]
            displacement[0] += n
            displacement[1] += m
            current = (j, (g+1) % len(refined[j]))
        assert current == initial and total == 10 and displacement == [0, 0]
        links.append({"corners_face_refined_native_angle": cycle,
                      "angle_sum_pi_over_5": total, "lattice_holonomy": displacement})
    assert len(links)-len(seams)+4 == 0
    return {"name": name, "conditions": signs,
            "positive_parameterization": {"a": str(substitution[a]), "k": str(substitution[k])},
            "refined_motif_coefficients_a_k": [[linear_coefficients(q) for q in p] for p in refined],
            "refined_vertex_native_side_angle": provenance,
            "refined_reversed_seams": retained_seams, "complete_vertex_links": links,
            "faces_edges_vertices": [4, len(seams), len(links)],
            "whole_chamber_positive_segment_lengths": True}


def fixture(sample, motifs, periods):
    p = [[QQbar(R(q).subs(sample)) for q in polygon] for polygon in motifs]
    u, v = [QQbar(R(q).subs(sample)) for q in periods]
    def cr(x, y):
        return AA((x.conjugate()*y).imag())
    def ar(polygon):
        return sum(cr(polygon[h], polygon[(h+1) % len(polygon)]) for h in range(len(polygon)))/2 if len(polygon) >= 3 else AA(0)
    def clip(first, second):
        out = list(first)
        for h, origin in enumerate(second):
            edge = second[(h+1) % 5]-origin
            if not out:
                break
            old, result = out[-1], []
            old_height = cr(edge, old-origin)
            for new in out:
                height = cr(edge, new-origin)
                if (height >= 0) != (old_height >= 0):
                    result.append(old+QQbar(old_height/(old_height-height))*(new-old))
                if height >= 0:
                    result.append(new)
                old, old_height = new, height
            out = []
            for q in result:
                if not out or out[-1] != q:
                    out.append(q)
            if len(out) > 1 and out[0] == out[-1]:
                out.pop()
        return out
    determinant = cr(u, v)
    assert determinant > 0 and sum(map(ar, p)) == determinant
    boxes = []
    for polygon in p:
        coordinates = [(cr(q, v)/determinant, cr(u, q)/determinant) for q in polygon]
        boxes.append([(min(q[h] for q in coordinates), max(q[h] for q in coordinates)) for h in range(2)])
    comparisons = []
    for i, j in product(range(4), repeat=2):
        bounds = [range(int(ceil(boxes[i][h][0]-boxes[j][h][1])),
                        int(floor(boxes[i][h][1]-boxes[j][h][0]))+1) for h in range(2)]
        for n, m in product(*bounds):
            if i == j and n == m == 0:
                continue
            assert ar(clip(p[i], [q+n*u+m*v for q in p[j]])) == 0
            comparisons.append([i, j, n, m])
    return {"parameters": {"a": str(sample[a]), "k": str(sample[k])},
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
    motifs, directions, periods, aux = construct()
    result = {"field": "Q(z), z=exp(pi*i/5), z^4-z^3+z^2-z+1=0",
              "family": {"A_lengths": ["a", "phi*k+a/phi", "a", "k", "k"],
                         "B_lengths": ["k", "phi*a+k/phi", "k", "a", "a"],
                         "domain": "a,k>0; two distinct classes iff a!=k",
                         "native_after_side_angles_pi_over_5": [2, 2, 4, 3, 4]},
              "formal_motif_coefficients_a_k": [[linear_coefficients(q) for q in p] for p in motifs],
              "formal_period_coefficients_a_k": list(map(linear_coefficients, periods)),
              "normalized_area_and_determinant": "phi^2*(a^2+4*a*k+k^2)",
              "five_chambers": [], "five_exact_fixtures": []}
    for name, substitution, sample, signs in CHAMBERS:
        result["five_chambers"].append(chamber(name, substitution, sample, signs, motifs, directions, periods, aux))
        result["five_exact_fixtures"].append({"chamber": name, **fixture(sample, motifs, periods)})
    rendered = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
