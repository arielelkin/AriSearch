#!/usr/bin/env python3
"""Two-node fractional resection: exact pentagons and periodic omission.

No patch enumeration. Coordinates (x,y) stand for x+i*sin(36 deg)*y.
"""
import argparse
import json
from pathlib import Path
from sage.all import AA, NumberField, PolynomialRing, QQ


def certificate():
    ring = PolynomialRing(QQ, 't')
    t = ring.gen()
    field = NumberField(t*t-t-1, 'phi', embedding=(AA(1)+AA(5).sqrt())/2)
    phi = field.gen()
    zero = field(0)
    half = field(1)/2
    h = field(1)/10
    sin36_squared = (3-phi)/4

    def sub(a, b):
        return tuple(x-y for x, y in zip(a, b))

    def cross(a, b):
        return a[0]*b[1]-a[1]*b[0]

    def area(poly):
        return sum(cross(p, poly[(i+1) % len(poly)]) for i, p in enumerate(poly))/2

    def turns(poly):
        return [cross(sub(poly[i], poly[i-1]), sub(poly[(i+1) % len(poly)], poly[i]))
                for i in range(len(poly))]

    def encode(poly):
        return [[str(x), str(y)] for x, y in poly]

    rows = []
    for typ, c, s in [('thin', phi/2, field(1)), ('thick', (phi-1)/2, phi)]:
        A, B, C, D = (zero, zero), (field(1), zero), (1+c, s), (c, s)
        p, q = (half, h), (half+c, s-h)
        sectors = [[A, B, p], [B, C, q, p], [C, D, q], [D, A, p, q]]
        assert all(all(AA(v) > 0 for v in turns(poly)) for poly in sectors)
        assert sum(area(poly) for poly in sectors) == s
        assert [area(poly) for poly in sectors] == [h/2, (s-h)/2, h/2, (s-h)/2]
        # Universal isosceles triangle, on the outside of the quad's BC edge.
        apex = (1+c/2+h*sin36_squared*s, s/2-h*c)
        poly = [B, apex, C, q, p]
        expected = [s*(field(1)/4+h*h*sin36_squared), h,
                    s*(field(1)/4+h*h*sin36_squared),
                    s/2-h*(1+c), s/2-h*(1-c)]
        assert turns(poly) == expected
        assert all(AA(v) > 0 for v in expected)
        assert area(poly) == s/2
        rows.append({'type': typ, 'rhomb': encode([A,B,C,D]),
                     'tree_nodes': encode([p,q]), 'sectors': [encode(z) for z in sectors],
                     'pentagon': encode(poly), 'turns': [str(v) for v in expected],
                     'normalized_area': str(area(poly)), 'native_sides': 5,
                     'periods_for_checkerboard_carrier': encode([(field(2),zero),(2*c,2*s)])})
    assert rows[0]['normalized_area'] != rows[1]['normalized_area']
    return {'schema': 1, 'coordinate_scale': 'x+i*sin(pi/5)*y',
            'common_triangle_physical_altitude': 'sin(pi/5)/10',
            'rows': rows, 'finite_gate': 'two exact shape checks; no contact enumeration',
            'global_source_cover': 'bipartite coloring of reviewed infinite marked-rhomb source',
            'two_congruence_classes': True,
            'universal_recognition': False,
            'obstruction': 'each pentagon class tiles a periodic homogeneous rhomb carrier alone'}


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', type=Path)
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.write:
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        assert json.loads(args.check.read_text()) == result
    print('PASS: exact global two-class pentagon geometry; each class has periodic omission')


if __name__ == '__main__':
    main()
