#!/usr/bin/env python3
"""Exact rational control: two convex pentagons, free angle, mixed periodic escape.
No search, source recognition, or aperiodicity inference is made.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def add(a, b):
    return tuple((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b))))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def pt(x, y):
    return ((Q(x),), (Q(y),))


def diff(a, b):
    return sub(a[0], b[0]), sub(a[1], b[1])


def cross(a, b):
    return sub(mul(a[0], b[1]), mul(a[1], b[0]))


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return tuple(a)


def area(poly):
    out = (Q(0),)
    for a, b in zip(poly, poly[1:] + poly[:1]):
        out = add(out, cross(a, b))
    return trim(tuple(x/2 for x in out))


def turns(poly):
    return [trim(cross(diff(poly[(i+1) % len(poly)], v),
                       diff(poly[(i+2) % len(poly)], poly[(i+1) % len(poly)])))
            for i, v in enumerate(poly)]


def positive_interval(poly):
    # Exact Bernstein coefficients on t in [0,1/4], degree at most two.
    assert len(poly) <= 3
    c = list(poly) + [Q(0)] * (3-len(poly))
    b = [c[0], c[0] + c[1]/8, c[0] + c[1]/4 + c[2]/16]
    assert all(x > 0 for x in b)
    return [str(x) for x in b]


def plain_cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def plain_area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(plain_cross(a, b) for a, b in
                   zip(poly, poly[1:]+poly[:1])))/2


def intersection(subject, clip):
    out = subject
    for a, b in zip(clip, clip[1:]+clip[:1]):
        def height(p):
            return plain_cross((b[0]-a[0], b[1]-a[1]),
                               (p[0]-a[0], p[1]-a[1]))
        incoming, out = out, []
        if not incoming:
            break
        for p, q in zip(incoming, incoming[1:]+incoming[:1]):
            hp, hq = height(p), height(q)
            if hp >= 0:
                out.append(p)
            if (hp < 0 <= hq) or (hq < 0 <= hp):
                z = hp/(hp-hq)
                out.append((p[0]+z*(q[0]-p[0]), p[1]+z*(q[1]-p[1])))
    return out


def verify():
    Hplain = [(Q(x), Q(y)) for x, y in
              [(0,0),(2,0),(3,1),(2,2),(0,2),(-1,1)]]
    H = [pt(x, y) for x, y in Hplain]
    p = ((Q(1,2), Q(-1)), (Q(0),))
    q = ((Q(1,2), Q(1)), (Q(2),))
    A = [p, q, pt(0,2), pt(-1,1), pt(0,0)]
    B = [p, pt(2,0), pt(3,1), pt(2,2), q]
    assert area(H) == (Q(6),)
    assert area(A) == (Q(2),)
    assert area(B) == (Q(4),)
    turn_control = {}
    for name, poly in [('A', A), ('B', B)]:
        turn_control[name] = [{'power': list(map(str, c)),
                              'bernstein_interval_0_to_quarter': positive_interval(c)}
                             for c in turns(poly)]
    # Bounding boxes imply |3m|<4 and |m+2n|<2 for positive overlap.
    checks = []
    for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            if (m, n) == (0, 0) or abs(m+2*n) >= 2:
                continue
            dx, dy = Q(3*m), Q(m+2*n)
            shifted = [(x+dx, y+dy) for x, y in Hplain]
            overlap = plain_area(intersection(Hplain, shifted))
            assert overlap == 0
            checks.append({'indices': [m,n], 'translation': [str(dx),str(dy)],
                           'exact_intersection_area': str(overlap)})
    assert len(checks) == 4
    return {
        'status': 'verified periodic control; killed for every parameter',
        'role': 'control only, not a promising aperiodic construction',
        'parameter': '0 < t < 1/4',
        'source_hexagon': [[str(x), str(y)] for x, y in Hplain],
        'cut': 'x = 1/2 + t*(y-1)',
        'A': ['p','q','(0,2)','(-1,1)','(0,0)'],
        'B': ['p','(2,0)','(3,1)','(2,2)','q'],
        'p': '(1/2-t,0)', 'q': '(1/2+t,2)',
        'areas': {'H':'6','A':'2','B':'4'},
        'distinct_shape_classes_reason': 'unequal exact areas',
        'convexity': turn_control,
        'angle_variation': 'cut angles pi/2 +/- arctan(t); derivative magnitude 1/(1+t^2)',
        'lattice_generators': [[3,1],[0,2]],
        'lattice_covolume': '6',
        'lattice_overlap_checks': checks,
        'coverage_argument': 'locally finite closed translates; disjoint interiors; area equals covolume',
        'periodic_witness': 'translate the same two-pentagon split of H by the lattice',
        'contact_model': 'partial-edge contacts allowed, including at unmatched cut endpoints',
        'reconstruction_investment': 'none; candidate killed by explicit mixed periodic witness'
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    certificate = verify()
    certificate['verifier_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    certificate['replay'] = ('conda run --no-capture-output -n arisearch python '
                             'research/searches/boundary-attachment-periodic-control.py '
                             '--output ' + args.output)
    Path(args.output).write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps({'status': certificate['status'], 'classes': 2,
                      'lattice_checks': len(certificate['lattice_overlap_checks'])}))
