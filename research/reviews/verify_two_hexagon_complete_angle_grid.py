#!/usr/bin/env python3
"""Exact bound arithmetic and deterministic angle representative construction.
No solver runs; does not decide joint polygon/length realisability.
"""
import argparse
from fractions import Fraction
import itertools
import json
from math import isqrt
from pathlib import Path
import sympy as sp

TRIPLES = list(itertools.combinations_with_replacement(range(12), 3))
UNIVERSAL_GRID = 5394
NEAR_REGULAR_GRID = 323633
BASE = [[int(c < 6) for c in range(12)], [int(c >= 6) for c in range(12)]]


def primitive(t):
    row = [t.count(c) for c in range(12)]
    return [x//3 for x in row] if len(set(t)) == 1 else row


def projected_norm_squared(row):
    return sum(x*x for x in row) - Fraction(sum(row[:6])**2+sum(row[6:])**2, 6)


def bound_table():
    norms = [projected_norm_squared(primitive(t)) for t in TRIPLES]
    assert max(norms) == Fraction(25, 6)
    table = []
    for k in range(10):
        d, H = 10-k, 364-k
        squared = Fraction(36*25**k, 6**k)
        D = isqrt(squared.numerator//squared.denominator)
        assert D*D <= squared < (D+1)*(D+1)
        h = (H+1)//2
        bound = D*(1+(d-1)*h)
        table.append(dict(rank=k, dimension=d, excluded_bound=H,
                          determinant_bound=D, coefficient_cap=h,
                          deviation_bound=bound, sufficient_grid=bound//60+1))
    assert max(r['deviation_bound'] for r in table)+1 == NEAR_REGULAR_GRID
    assert max(r['sufficient_grid'] for r in table) == UNIVERSAL_GRID
    return table


def construct(T, K=UNIVERSAL_GRID):
    T = sorted({tuple(t) for t in T})
    assert all(t in TRIPLES for t in T)
    rows = list(BASE)
    for t in T:
        candidate = primitive(t)
        if sp.Matrix(rows+[candidate]).rank() > len(rows):
            rows.append(candidate)
    M = sp.Matrix(rows)
    r, k = len(rows), len(rows)-2
    pivots = list(M.rref()[1])
    assert len(pivots) == r
    free = [c for c in range(12) if c not in pivots]
    kernel = M.nullspace()
    closed = [t for t in TRIPLES if all(sum(v[c] for c in t)==0 for v in kernel)]
    assert closed == T, 'Input triple set is not rationally closed'
    if not free:
        assert len(T) == 364
        return dict(rank=10, dimension=0, K=K, deviation=[0]*12,
                    angle_numerators=[120*K]*12, exact_triples=T,
                    kernel_basis=[], coefficients=[])
    B = M[:,pivots]
    delta = int(B.det())
    assert delta != 0
    basis = []
    for j in free:
        v = [0]*12
        v[j] = delta
        for a, c in enumerate(pivots):
            C = B.copy()
            C[:,a] = M[:,j]
            v[c] = -int(C.det())
        assert M*sp.Matrix(v) == sp.zeros(r,1)
        basis.append(v)
    D = bound_table()[k]['determinant_bound']
    assert all(abs(x) <= D for v in basis for x in v)
    missing = [t for t in TRIPLES if t not in set(T)]
    forms = [[sum(v[c] for c in t) for v in basis] for t in missing]
    assert all(any(g != 0 for g in form) for form in forms)
    H = len(missing)
    low, high = -(H//2), (H+1)//2
    choices = sorted(range(low, high+1), key=lambda c: (abs(c), c))
    coefficients = [1]
    # Keep every restricted forbidden form nonzero as an affine form in
    # the remaining variables. At most H scalar roots must be avoided.
    for j in range(1, len(basis)):
        forbidden = set()
        for form in forms:
            constant = sum(form[i]*coefficients[i] for i in range(j))
            if any(form[i] for i in range(j+1, len(basis))):
                continue
            if form[j]:
                forbidden.add(Fraction(-constant, form[j]))
            else:
                assert constant != 0
        coefficients.append(next(c for c in choices if c not in forbidden))
    deviation = [sum(a*v[c] for a,v in zip(coefficients,basis)) for c in range(12)]
    assert all(sum(deviation[c] for c in t) != 0 for t in missing)
    assert all(sum(deviation[c] for c in t) == 0 for t in T)
    assert sum(deviation[:6]) == sum(deviation[6:]) == 0
    actual_cap = D*(1+(len(basis)-1)*((H+1)//2))
    assert max(map(abs,deviation)) <= actual_cap < 60*K
    assert all(0 < 120*K+x < 180*K for x in deviation)
    return dict(rank=k, dimension=len(basis), K=K, deviation=deviation,
                angle_numerators=[120*K+x for x in deviation], exact_triples=T,
                kernel_basis=basis, coefficients=coefficients,
                determinant=delta, pivot_columns=pivots, free_columns=free,
                actual_excluded_count=H, actual_deviation_cap=actual_cap)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = args.input or root/'certificates/two-hexagon-corner-balance-obstruction-example.json'
    raw = json.loads(source.read_text())
    T = raw['T'] if isinstance(raw,dict) else raw
    result = dict(universal_grid=UNIVERSAL_GRID, near_regular_grid=NEAR_REGULAR_GRID, bound_table=bound_table(),
                  example_source=str(source), example=construct(T))
    if args.check:
        retained = json.loads(args.check.read_text())
        assert retained['universal_grid'] == result['universal_grid']
        assert retained['near_regular_grid'] == result['near_regular_grid']
        assert retained['bound_table'] == result['bound_table']
        assert retained['example'] == json.loads(json.dumps(result['example']))
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'K':UNIVERSAL_GRID,'bound_table':result['bound_table'],
                      'example_rank':result['example']['rank'],
                      'example_max_abs_deviation':max(map(abs,result['example']['deviation'])),
                      'example_coefficients':result['example']['coefficients']}))

if __name__ == '__main__':
    main()
