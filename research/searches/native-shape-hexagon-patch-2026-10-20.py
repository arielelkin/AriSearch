"""Exact native-word local patch gate for one shape-first hexagon pair.

The search uses only integer side equality on the triangular dual. It makes
no claim that a finite assignment extends to an infinite tiling.
"""

from collections import Counter
from fractions import Fraction

WORDS = {
    'A': (1, 3, 2, 3, 1, 4),
    'B': (2, 5, 3, 4, 3, 5),
}
STEPS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
UNIT = ((1, 0), (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(-1, 2), Fraction(1, 2)), (-1, 0),
        (Fraction(-1, 2), Fraction(-1, 2)),
        (Fraction(1, 2), Fraction(-1, 2)))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def vertices(word):
    out = [(Fraction(0), Fraction(0))]
    for length, unit in zip(word, UNIT):
        out.append(add(out[-1], (length * unit[0], length * unit[1])))
    assert out[-1] == out[0]
    return out


def area_coefficient(word):
    """Area divided by sqrt(3)."""
    v = vertices(word)
    return sum(v[k][0] * v[k + 1][1] - v[k + 1][0] * v[k][1]
               for k in range(6)) / 2


FOUR_STATES = (
    ('A', (1, 3, 2, 3, 1, 4)),
    ('A', (3, 1, 4, 1, 3, 2)),
    ('B', (5, 3, 4, 3, 5, 2)),
    ('B', (3, 5, 2, 5, 3, 4)),
)


def periodic_carrier():
    """Four states at triangular-dual site (i,j), indexed by i-j mod 4."""
    for t, (_, word) in enumerate(FOUR_STATES):
        for k, (di, dj) in enumerate(STEPS):
            neighbor = FOUR_STATES[(t + di - dj) % 4][1]
            assert word[k] == neighbor[(k + 3) % 6]

    def displacement(t, k):
        di, dj = STEPS[k]
        here = vertices(FOUR_STATES[t][1])
        there = vertices(FOUR_STATES[(t + di - dj) % 4][1])
        return sub(here[k + 1], there[(k + 3) % 6])

    # One (1,1) step is side 0 then side 1. Four (1,0) steps are side 0.
    first = add(displacement(0, 0), displacement(1, 1))
    second = (Fraction(0), Fraction(0))
    for t in range(4):
        second = add(second, displacement(t, 0))
    determinant_coefficient = first[0] * second[1] - first[1] * second[0]
    assert determinant_coefficient != 0
    assert abs(determinant_coefficient) == 2 * area_coefficient(WORDS['A']) + 2 * area_coefficient(WORDS['B'])
    print('four-state carrier', FOUR_STATES)
    print('physical period (1,1):', first, 'meaning (x, y*sqrt(3))')
    print('physical period (4,0):', second, 'meaning (x, y*sqrt(3))')
    print('period determinant:', determinant_coefficient, '*sqrt(3)')


def states():
    return sorted({(name, tuple(w[(j + parity * k) % 6] for k in range(6)))
                   for name, w in WORDS.items() for parity in (-1, 1)
                   for j in range(6)})


STATES = states()


def solve(domain, seed, cap=None):
    """Enumerate labelled native placements on a finite dual-site domain."""
    domain = set(domain)
    assignment = {(0, 0): seed}
    count = 0
    sample = None
    branching = Counter()

    def options(p):
        out = []
        for state in STATES:
            if all(q not in assignment or state[1][k] == assignment[q][1][(k + 3) % 6]
                   for k, step in enumerate(STEPS)
                   for q in [(p[0] + step[0], p[1] + step[1])]):
                out.append(state)
        return out

    def rec():
        nonlocal count, sample
        if len(assignment) == len(domain):
            count += 1
            if sample is None:
                sample = dict(assignment)
            return
        frontier = [p for p in domain - assignment.keys()
                    if any((p[0] + di, p[1] + dj) in assignment for di, dj in STEPS)]
        candidates = [(options(p), p) for p in frontier]
        opts, p = min(candidates, key=lambda z: (len(z[0]), z[1]))
        branching[len(opts)] += 1
        for state in opts:
            assignment[p] = state
            rec()
            del assignment[p]
            if cap is not None and count >= cap:
                return

    rec()
    return count, sample, branching


def audit():
    ring = {(0, 0)} | set(STEPS)
    disk2 = {(i, j) for i in range(-2, 3) for j in range(-2, 3)
             if max(abs(i), abs(j), abs(i + j)) <= 2}
    assert len(ring) == 7 and len(disk2) == 19
    for name in ('A', 'B'):
        seed = (name, WORDS[name])
        n, sample, branching = solve(ring, seed)
        print(name, 'one-ring count', n, 'branching', sorted(branching.items()))
        if sample:
            print(name, 'one-ring sample', sorted(sample.items()))
        n2, sample2, branching2 = solve(disk2, seed, cap=1)
        print(name, 'two-ring existence', bool(n2),
              'search branches', sorted(branching2.items()))
        if sample2:
            print(name, 'two-ring sample', sorted(sample2.items()))
    periodic_carrier()


if __name__ == '__main__':
    audit()
