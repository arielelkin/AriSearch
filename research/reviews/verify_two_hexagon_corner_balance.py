#!/usr/bin/env python3
"""Exact corner balance / separating-potential check; does not decide tiling.
Input JSON is a triple list, or a dict with key T. Output is exact rational.
Run with --registry to summarize the retained low-rank registry.
"""
import argparse
import json
from fractions import Fraction
import itertools
from collections import Counter
from pathlib import Path
import z3


def check(T):
    T = [tuple(t) for t in T]
    w = [z3.Real(f'w_{i}') for i in range(len(T))]
    a, b = z3.Reals('a b')
    s = z3.Solver()
    s.add(a > 0, b > 0, a+b == 1)
    s.add(*[v >= 0 for v in w])
    for c in range(12):
        s.add(z3.Sum([t.count(c)*v for t,v in zip(T,w)]) == (a if c < 6 else b))
    result = s.check()
    if result == z3.sat:
        m = s.model()
        av, bv = m.eval(a).as_fraction(), m.eval(b).as_fraction()
        weights = [m.eval(v).as_fraction() for v in w]
        assert av > 0 and bv > 0 and av+bv == 1
        assert all(v >= 0 for v in weights)
        assert all(sum(t.count(c)*v for t,v in zip(T,weights)) == (av if c < 6 else bv) for c in range(12))
        return {'two_species_balance': True, 'a': str(m.eval(a)),
                'b': str(m.eval(b)), 'weights': [
                    [list(t), str(m.eval(v))] for t,v in zip(T,w)
                    if m.eval(v).as_fraction() > 0]}
    if result != z3.unsat:
        raise RuntimeError(result)
    d = [z3.Real(f'd_{i}') for i in range(12)]
    dual = z3.Solver()
    sa, sb = z3.Sum(d[:6]), z3.Sum(d[6:])
    dual.add(sa <= 0, sb <= 0, sa+sb == -1)
    dual.add(*[z3.Sum([d[c] for c in t]) >= 0 for t in T])
    if dual.check() != z3.sat:
        raise RuntimeError('No separating potential: duality check failed')
    m = dual.model()
    values = [m.eval(v).as_fraction() for v in d]
    assert sum(values[:6]) <= 0 and sum(values[6:]) <= 0
    assert sum(values) == -1
    assert all(sum(values[c] for c in t) >= 0 for t in T)
    return {'two_species_balance': False,
            'potential': [str(v) for v in values],
            'species_sums': [str(sum(values[:6])), str(sum(values[6:]))],
            'empty_if_both_species_sums_negative':
                sum(values[:6]) < 0 and sum(values[6:]) < 0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?')
    parser.add_argument('--registry', action='store_true')
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()
    if args.example:
        import sympy as sp
        path = Path(__file__).resolve().parents[1]/'certificates/two-hexagon-corner-balance-obstruction-example.json'
        data = json.loads(path.read_text())
        T = [tuple(t) for t in data['T']]
        d = [Fraction(v) for v in data['empty_potential']]
        assert sum(d[:6]) == sum(d[6:]) == -1
        assert all(sum(d[c] for c in t) >= 0 for t in T)
        rows = [[int(i < 6) for i in range(12)], [int(i >= 6) for i in range(12)]] + [[t.count(i) for i in range(12)] for t in T]
        matrix = sp.Matrix(rows)
        assert matrix.rank()-2 == data['rank'] == 5
        # Center all angles at 120 degrees. Triple implication is then
        # ordinary row-space membership, independently of census code.
        kernel = matrix.nullspace()
        alltriples = list(itertools.combinations_with_replacement(range(12),3))
        closure = [t for t in alltriples if all(sum(v[c] for c in t)==0 for v in kernel)]
        assert closure == T
        essential = T[:5]
        assert all(any(sum(c in t for t in T)==1 for c in t0) for t0 in essential)
        assert sp.Matrix(rows[:2]+[[t.count(i) for i in range(12)] for t in essential]).rank() == 7
        region = [t for t in alltriples if sum(d[c] for c in t)>=0]
        print(json.dumps({'exact_closure': True, 'rank': 5, 'minimal_covering': True, 'empty_for_all_side_equalities': True, 'potential_region_triples': len(region)}))
    elif args.registry:
        path = Path(__file__).resolve().parents[1]/'certificates/two-hexagon-global-angle-flats-rank3.json'
        counts = Counter()
        examples = []
        for T, rank in json.loads(path.read_text()):
            if len({c for t in T for c in t}) != 12:
                continue
            result = check(T)
            counts[(rank, result['two_species_balance'])] += 1
            if not result['two_species_balance'] and len(examples) < 3:
                examples.append({'T': T, 'rank': rank, **result})
        print(json.dumps({'counts': [[*k,v] for k,v in sorted(counts.items())], 'obstructed_examples': examples}, indent=2))
    else:
        raw = json.loads(Path(args.input).read_text())
        T = raw['T'] if isinstance(raw,dict) else raw
        print(json.dumps(check(T), indent=2))

if __name__ == '__main__':
    main()
