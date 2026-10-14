"""Exact check of the two unit-chord-preserving cross-source maps.

This is a necessary-condition filter for a three-plus-one class assignment.
It does not claim to settle maps that send the canonical unit chord to
another unit diagonal.
"""

import importlib.util
from pathlib import Path

import sympy as S


SOURCE = Path(__file__).with_name("ammann-directed-offset-gate-2026-10-14.py")
spec = importlib.util.spec_from_file_location("directed_gate", SOURCE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

phi = (1 + S.sqrt(5)) / 2
t = S.sqrt(10 - 2 * S.sqrt(5)) / 4
unknowns = (gate.aX, gate.aY, gate.hX, gate.hY)
reps = [gate.outputs()[i] for i in (0, 1, 4, 5)]


def source_poly(row):
    c = phi / 2 if row[0] == "thin" else (phi - 1) / 2
    s = t if row[0] == "thin" else phi * t
    return [v.subs({gate.c: c, gate.s: s}) for v in row[4]]


def chord_frame(poly, index):
    origin = poly[index(0)]
    base = poly[index(2)] - origin
    assert S.simplify(base.dot(base) - 1) == 0
    return [
        (S.expand((poly[index(i)] - origin).dot(base)),
         S.expand(gate.cross(base, poly[index(i)] - origin)))
        for i in range(5)
    ]


def linear_system(i, j, reverse):
    p, q = source_poly(reps[i]), source_poly(reps[j])
    index = (lambda k: (2 - k) % 5) if reverse else (lambda k: k)
    pf, qf = chord_frame(p, lambda k: k), chord_frame(q, index)
    equations = []
    for k in (1, 3, 4):
        equations.extend((pf[k][0] - qf[k][0],
                          pf[k][1] - (-1 if reverse else 1) * qf[k][1]))
    return S.linear_eq_to_matrix(equations, unknowns)


if __name__ == "__main__":
    for i in range(2):
        for j in range(2, 4):
            for reverse in (False, True):
                matrix, rhs = linear_system(i, j, reverse)
                rank, augmented = matrix.rank(), matrix.row_join(rhs).rank()
                answer = S.linsolve((matrix, rhs), unknowns)
                if (i,j,reverse) == (0,3,False):
                    assert rank == augmented == 3 and len(answer) == 1
                    expected = (S.Rational(1,2), (phi-1)*(1+2*t*gate.hY), (phi-1)*(t+2*gate.hY), gate.hY)
                    actual = next(iter(answer))
                    assert all(S.simplify(u-v) == 0 for u,v in zip(actual,expected))
                elif (i,j,reverse) == (1,2,False):
                    assert rank == augmented == 4 and len(answer) == 1
                    negative = -(5-S.sqrt(5))*t/10
                    expected = (S.Rational(1,2), S.Rational(1,2), negative, -negative)
                    actual = next(iter(answer))
                    assert all(S.simplify(u-v) == 0 for u,v in zip(actual,expected))
                    assert negative.is_negative is True
                else:
                    assert augmented > rank and answer == S.EmptySet
                print(f"T{i} K{j - 2} reverse={reverse}: "
                      f"rank={rank}, augmented={augmented}, solution={answer}")
    # The only positive-height linear family is T0--K1, same orientation.
    y = S.symbols("y", positive=True)
    family = {
        gate.aX: S.Rational(1, 2),
        gate.aY: (phi - 1) * (1 + 2 * t * y),
        gate.hX: (phi - 1) * (t + 2 * y),
        gate.hY: y,
    }
    E_T = ((gate.aX - gate.aY) * (gate.aX + gate.aY - 2)
           + gate.hX ** 2 - gate.hY ** 2)
    positive_form = S.sqrt(5) - 2 + 2 * (S.sqrt(5) - 1) * t * y
    assert S.simplify(E_T.subs(family) - positive_form) == 0
    print("T0 K1 family: E_T = sqrt(5)-2 + 2(sqrt(5)-1)t*hY > 0")

