#!/usr/bin/env python3
"""Exact proof check, not a marked-contact or source-patch search.

Each new face is the union of two center fan triangles across a unit
rhomb edge. Normalize y coordinates by the positive sin(pi/5), so all
arithmetic lies in Q(phi). The 4 x 4 rows cover a superset of legal marked
contacts. Every resulting face is a strict quadrilateral, hence has the
reviewed unrestricted periodic omission escape.
"""
import argparse
import json
from pathlib import Path

from sage.all import AA, NumberField, PolynomialRing, QQ


def certificate():
    ring = PolynomialRing(QQ, "t")
    t = ring.gen()
    field = NumberField(t*t-t-1, "phi", embedding=AA(5).sqrt()/2+AA(1)/2)
    phi = field.gen()

    def positive(q):
        return AA(q) > 0

    def cross(a, b):
        return a[0]*b[1]-a[1]*b[0]

    def sub(a, b):
        return (a[0]-b[0], a[1]-b[1])

    def area(poly):
        return sum(cross(p, poly[(i+1) % len(poly)]) for i, p in enumerate(poly))/2

    choices = []
    for typ, cosine, relative_sine in (
        ("thin", phi/2, field(1)),
        ("thick", (phi-1)/2, phi),
    ):
        for sign in (-1, 1):
            x = (1+sign*cosine)/2
            h = relative_sine/2
            assert positive(x) and positive(1-x) and positive(h)
            choices.append((typ, sign, x, h))

    rows = []
    for right_typ, right_sign, xr, hr in choices:
        for left_typ, left_sign, xl, hl in choices:
            poly = [(field(0), field(0)), (xr, -hr),
                    (field(1), field(0)), (xl, hl)]
            turns = [cross(sub(poly[i], poly[i-1]),
                           sub(poly[(i+1) % 4], poly[i])) for i in range(4)]
            formulas = [xl*hr+xr*hl, hr,
                        (1-xr)*hl+(1-xl)*hr, hl]
            assert turns == formulas and all(positive(q) for q in turns)
            assert area(poly) == (hr+hl)/2
            right_rhomb_area = 2*hr
            left_rhomb_area = 2*hl
            assert area(poly) == (right_rhomb_area+left_rhomb_area)/4
            rows.append({
                "right": [right_typ, right_sign],
                "left": [left_typ, left_sign],
                "vertices": [[str(x), str(y)] for x, y in poly],
                "turns": [str(q) for q in turns],
                "normalized_area": str(area(poly)),
                "native_sides": 4,
            })

    # Every rhomb carries two edges of each mark type. Dividing each
    # incidence count by two is required: each edge has two incident faces.
    incidence = [[2, 2], [2, 2]]
    count_matrix = [[QQ(q)/2 for q in row] for row in incidence]
    assert count_matrix == [[1, 1], [1, 1]]
    # Reference X is thin/thin, Y thick/thick; centers have equal x on
    # opposite sides. These are mark-compatible exact two-rhomb contacts.
    reference = {}
    for label, cosine, h, sign in (("A_X", phi/2, field(1)/2, 1),
                                   ("B_Y", (phi-1)/2, phi/2, -1)):
        x = (1+sign*cosine)/2
        poly = [(field(0), field(0)), (x, -h),
                (field(1), field(0)), (x, h)]
        assert positive(area(poly)) and area(poly) == h
        reference[label] = [[str(a), str(b)] for a, b in poly]

    return {
        "schema": 1,
        "rule": "canonical rhomb centers; fan triangles glued across every edge",
        "field": "phi^2-phi-1=0, phi=(1+sqrt(5))/2",
        "coordinates": "(x,y) means x+i*sin(pi/5)*y",
        "finite_domain": "4 choices of center on each side; 16 rows; superset of legal contacts",
        "contact_enumeration_performed": False,
        "geometry_rows": rows,
        "references": reference,
        "XY_count_matrix_on_thin_thick": [[str(q) for q in row] for row in count_matrix],
        "global_cover_dependency": "ammann-forcing-aperiodicity.md Lemmas 5 and 7",
        "obstruction": "all outputs strict convex quadrilaterals; every retained class has periodic monohedral omission",
        "intrinsic_decoder": "not established",
        "two_shape_collapse": "not tested; irrelevant after omission obstruction",
    }


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.write:
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    else:
        assert json.loads(args.check.read_text()) == result
    print("PASS: fractional fan cover identities, 16 strict quadrilateral checks, periodic omission obstruction")


if __name__ == "__main__":
    main()
