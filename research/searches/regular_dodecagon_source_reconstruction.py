#!/usr/bin/env python3
"""Exact geometry behind a conditional reading of arXiv2510.18734v2 Fig2b.

This verifies our AP3 reconstruction, not the source's missing indexed atlas.
Normal invocation is nondestructive; --output explicitly retains JSON.
"""
import argparse
import json
from pathlib import Path
from sage.all import AA, CyclotomicField, QQ, QQbar

K = CyclotomicField(24)
q = K.gen()
h = q**2 + q**-2
S = q + q**-1
L = 1 + h


def cross(a, b):
    return (a.conjugate()*b-a*b.conjugate())/(2*K.gen()**6)


def area(p):
    return sum(cross(p[i], p[(i+1) % len(p)]) for i in range(len(p)))/2


def walk(edges):
    p = [K(0)]
    for e in edges:
        p.append(p[-1]+e)
    assert p[-1] == 0
    return p[:-1]


def verify_angles(edges, native_degrees):
    for i, deg in enumerate(native_degrees):
        incoming, outgoing = edges[i-1], edges[i]
        # Exterior turn is signed; this retains a reflex corner's sign.
        turn = (180-deg)//15
        ratio = outgoing/incoming/q**turn
        assert ratio.conjugate() == ratio
        assert QQbar(ratio).real() > 0


def main():
    # Twelve AP3 unit directions, grouped consecutively 2,3,2,3,2.
    blocks = ((0, 1), (2, 3, 4), (5, 6), (7, 8, 9), (10, 11))
    pe = [sum(q**(2*j) for j in block) for block in blocks]
    P = walk(pe)
    assert pe == [S*q, L*q**6, S*q**11, L*q**16, S*q**21]
    pa = (120, 105, 105, 105, 105)
    verify_angles(pe, pa)
    for i in range(5):
        assert all(QQbar(cross(pe[i], P[j]-P[i])).real() > 0
                   for j in range(5) if j not in (i, (i+1) % 5))

    # Inferred interior fragment: four S edges and four L edges.
    fe = [S*q**21, L*q**2, S*q**7, S*q**3,
          L*q**8, S*q**13, L*q**16, L*q**18]
    F = walk(fe)
    fa = (135, 105, 105, 240, 105, 105, 135, 150)
    verify_angles(fe, fa)
    assert QQbar(cross(fe[2], fe[3])).real() < 0
    assert all(QQbar(cross(fe[i-1], fe[i])).real() > 0
               for i in range(8) if i != 3)
    # No proper intersections of nonadjacent edges; no vertex lies on one.
    for i in range(8):
        for j in range(i+1, 8):
            if (i-j) % 8 in (1, 7):
                continue
            x, y = F[i], F[(i+1) % 8]
            u, v = F[j], F[(j+1) % 8]
            a, b = cross(y-x, u-x), cross(y-x, v-x)
            c, d = cross(v-u, x-u), cross(v-u, y-u)
            assert not (QQbar(a*b).real() < 0 and QQbar(c*d).real() < 0)
    qa = 3*(2+h)*L**2
    assert area(F) == qa/4 == QQ(21)/2+6*h
    assert area(P) == QQ(17)/4+QQ(5)/2*h
    # Family p=0, ell=t=S/L=1/sqrt(2), with Q normalized to side1.
    assert (S/L)**2 == QQ(1)/2
    assert h*S/L-2*(q-q.conjugate())/(2*K.gen()**6) == S/L
    result = {
        "status": "PASS_exact_candidate_only",
        "source_identification": "inferred_from_raster_not_certified_atlas",
        "source_pdf_sha256": "c07f2dfa267cfb7f85064d4f0add374fa9992c46ab8762563cedb289cd6aa153",
        "field": "CyclotomicField(24), q=exp(i*pi/12)",
        "pentagon_unit_direction_blocks": [list(b) for b in blocks],
        "pentagon_angles_degrees": pa,
        "pentagon_side_word": ["S", "L", "S", "L", "S"],
        "S_squared": "2+sqrt(3)", "L": "1+sqrt(3)",
        "family_parameters": {"p": "0", "ell": "1/sqrt(2)", "t": "1/sqrt(2)"},
        "fragment_angles_degrees": fa,
        "fragment_edge_word": ["S", "L", "S", "S", "L", "S", "L", "L"],
        "fragment_area_over_regular_dodecagon": "1/4",
        "global_source_tiling_or_regrouping_verified": False,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    value = json.dumps(result, indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(value)
    print(value, end="")


if __name__ == "__main__":
    main()
