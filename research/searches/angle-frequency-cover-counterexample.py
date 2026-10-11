#!/usr/bin/env python3
"""Exact finite angle-frequency comparison and concrete tangent hexagons."""
import argparse
import itertools
import json
from fractions import Fraction
import z3
from sage.all import AA, QQbar, CyclotomicField, matrix, vector

ANGLES = tuple(range(100, 171, 10))
A = (100, 100, 100, 140, 140, 140)
B = (100, 100, 110, 130, 140, 140)
WEIGHTS = {100: 2, 110: -1, 130: -1, 140: 2}

def enumerate_pairs():
    words = [x for x in itertools.combinations_with_replacement(ANGLES, 6)
             if sum(x) == 720]
    all_stars = [x for x in itertools.combinations_with_replacement(ANGLES, 3)
                 if sum(x) == 360]
    covered = 0
    killed = []
    feasible = []
    for i, a in enumerate(words):
        for b in words[i:]:
            present = set(a + b)
            stars = [t for t in all_stars if set(t) <= present]
            if {v for t in stars for v in t} != present:
                continue
            covered += 1
            fa, fb = z3.Reals('fa fb')
            xs = [z3.Real('star_' + str(j)) for j in range(len(stars))]
            solver = z3.Solver()
            solver.add(fa >= 0, fb >= 0, fa + fb == 1,
                       *[x >= 0 for x in xs])
            for v in present:
                solver.add(sum(x * t.count(v) for x, t in zip(xs, stars))
                           == a.count(v) * fa + b.count(v) * fb)
            result = solver.check()
            if result == z3.unsat:
                # Small exact Farkas witnesses separate both type marginals.
                ws = {v: z3.Real('weight_' + str(v)) for v in sorted(present)}
                dual = z3.Solver()
                dual.add(*[sum(ws[v] for v in t) >= 0 for t in stars])
                dual.add(sum(ws[v] for v in a) <= -1,
                         sum(ws[v] for v in b) <= -1)
                assert dual.check() == z3.sat
                model = dual.model()
                weights = {}
                for v in sorted(present):
                    val = model.eval(ws[v])
                    weights[v] = Fraction(val.numerator_as_long(),
                                          val.denominator_as_long())
                assert all(sum(weights[v] for v in t) >= 0 for t in stars)
                assert sum(weights[v] for v in a) <= -1
                assert sum(weights[v] for v in b) <= -1
                killed.append({'A': a, 'B': b, 'stars': stars,
                               'separating_weights': {str(v): str(w)
                                                      for v, w in weights.items()}})
            elif result == z3.sat:
                model = solver.model()
                def fraction_string(expr):
                    val = model.eval(expr, model_completion=True)
                    return str(Fraction(val.numerator_as_long(), val.denominator_as_long()))
                feasible.append({'A': a, 'B': b, 'stars': stars,
                                 'fa': fraction_string(fa), 'fb': fraction_string(fb),
                                 'star_frequencies': [fraction_string(x) for x in xs]})
            else:
                raise RuntimeError('Incomplete solver result: ' + str(result))
    return {'angle_domain': ANGLES, 'angle_multisets': len(words),
            'unordered_pair_domain': len(words) * (len(words) + 1) // 2,
            'angle_covered_pairs': covered, 'infeasible_pairs': len(killed),
            'certified_rejections': killed, 'certified_feasible': feasible}

K = CyclotomicField(36)
z = K.gen()
I = z ** 9
embedding = K.hom([QQbar.zeta(36)], QQbar)

def real(x):
    return AA(embedding(x))

def normal(degrees):
    j = degrees // 10
    assert j * 10 == degrees
    return vector(K, [(z**j + z**(-j))/2,
                      (z**j - z**(-j))/(2*I)])

def make_polygon(angles):
    theta = [0]
    for alpha in angles[1:]:
        theta.append(theta[-1] + 180-alpha)
    ns = [normal(t) for t in theta]
    vertices = [matrix(K, [ns[j-1], ns[j]]).solve_right(vector(K, [1, 1]))
                for j in range(6)]
    for j, p in enumerate(vertices):
        for k, n in enumerate(ns):
            value = real(n.dot_product(p))
            assert value == 1 if k in {(j-1)%6, j} else value < 1
        u = ns[j-1]
        v = ns[j]
        assert u.dot_product(v) == normal(180-angles[j])[0]
        p1, p2 = vertices[(j+1)%6], vertices[(j+2)%6]
        e, f = p1-p, p2-p1
        assert real(e[0]*f[1]-e[1]*f[0]) > 0
    coords = [[[[str(c) for c in x.list()] for x in p] for p in vertices]][0]
    return {'angles_degrees': angles, 'normal_degrees': theta,
            'coordinates_in_zeta36': coords}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()
    assert __debug__, 'Assertions must be enabled'
    result = enumerate_pairs()
    stars = [t for t in itertools.combinations_with_replacement(sorted(WEIGHTS), 3)
             if sum(t) == 360]
    assert stars == [(100, 130, 130), (110, 110, 140)]
    assert all(sum(WEIGHTS[v] for v in t) == 0 for t in stars)
    result['concrete_obstruction'] = {
        'A': make_polygon(A), 'B': make_polygon(B),
        'stars': stars, 'weights': WEIGHTS,
        'tile_charges': [sum(WEIGHTS[v] for v in a) for a in (A, B)],
        'field': 'Q(z), z^12-z^6+1=0, Re(z) in (98/100,99/100), Im(z) in (17/100,18/100)',
        'scope': 'Angle-only exact counterexample and untileability family; not resolution.'}
    assert result['angle_multisets'] == 46
    assert result['unordered_pair_domain'] == 1081
    assert result['angle_covered_pairs'] == 692
    assert result['infeasible_pairs'] == 11
    data = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        Path = __import__('pathlib').Path
        Path(args.output).write_text(data)
    else:
        print(data, end='')

if __name__ == '__main__':
    main()
