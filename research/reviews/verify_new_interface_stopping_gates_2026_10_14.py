"""Independent fixed-case checks for two 2026-10-14 interface failures.

No producer import, search, solver, certificate write, or coordinate census.
Run with: python research/reviews/verify_new_interface_stopping_gates_2026_10_14.py
"""

from sympy import symbols, simplify


class DSU:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def boundary_word(names, sides, seams, start):
    """Glue whole CCW edges with reversed direction, then trace the exterior."""
    vertices = [(name, j) for name in names for j in range(sides)]
    dsu = DSU(vertices)
    paired = set()
    for (left, i), (right, j) in seams:
        assert (left, i) not in paired and (right, j) not in paired
        paired.update(((left, i), (right, j)))
        dsu.join((left, i), (right, (j + 1) % sides))
        dsu.join((left, (i + 1) % sides), (right, j))
    exposed = [(name, j) for name in names for j in range(sides)
               if (name, j) not in paired]
    outgoing = {}
    for edge in exposed:
        source = dsu.find(edge)
        assert source not in outgoing, (edge, outgoing.get(source))
        outgoing[source] = edge
    word = []
    edge = start
    while edge not in word:
        word.append(edge)
        end = dsu.find((edge[0], (edge[1] + 1) % sides))
        assert end in outgoing
        edge = outgoing[end]
    assert edge == start and len(word) == len(exposed)
    return word, dsu


def check_wheel(names, sides):
    a, b, c = names
    seams = [((b, 0), (a, sides - 1)),
             ((c, 0), (b, sides - 1)),
             ((a, 0), (c, sides - 1))]
    actual, dsu = boundary_word(names, sides, seams, (a, 1))
    expected = [(name, j) for name in names
                for j in range(1, sides - 1)]
    assert actual == expected
    assert len(actual) == 3 * sides - 6
    for left, right in ((a, b), (b, c), (c, a)):
        assert dsu.find((left, sides - 1)) == dsu.find((right, 1))
    assert dsu.find((a, 0)) == dsu.find((b, 0)) == dsu.find((c, 0))


def check_join():
    actual, dsu = boundary_word(
        ("H", "K"), 9, [(('H', 0), ('K', 8))], ('H', 1)
    )
    assert actual == ([('H', j) for j in range(1, 9)]
                      + [('K', j) for j in range(0, 8)])
    assert len(actual) == 16
    assert dsu.find(('H', 0)) == dsu.find(('K', 0))
    assert dsu.find(('H', 1)) == dsu.find(('K', 8))


def check_corner_budgets():
    # Six internal native atom corners persist in each three-pentagon wheel.
    # Up to three wheel seam endpoints may flatten; all allowed integer counts.
    for p_h in range(6, 10):
        for p_k in range(6, 10):
            macro_h_lower = 2 * p_h + p_k - 9
            macro_k_lower = p_h + p_k - 4
            assert macro_h_lower > p_h, (p_h, p_k)
            assert macro_k_lower > p_k, (p_h, p_k)
    # If all three base seam endpoints are genuine, the sharper bounds hold.
    assert 3 * (9 - 3) == 18 > 9
    assert 2 * (9 - 2) == 14 > 9


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def check_split_edge_turn():
    a, b, h, r, k = symbols('a b h r k', real=True)
    m_minus_t = (a - b, h)
    r_minus_m = (r - a, k)
    m_minus_r = (a - r, -k)
    t_minus_m = (b - a, -h)
    left = cross(m_minus_t, r_minus_m)
    right = cross(m_minus_r, t_minus_m)
    c = (a - b) * k - h * (r - a)
    assert simplify(left - c) == 0
    assert simplify(right + c) == 0
    # At C=0, k(t-M)+h(R-M)=0. Since h,k>0, M is strictly
    # between the donor apex T and receiver splitter R.
    collinear_relation = (
        k * t_minus_m[0] + h * r_minus_m[0],
        k * t_minus_m[1] + h * r_minus_m[1],
    )
    assert simplify(collinear_relation[0] + c) == 0
    assert simplify(collinear_relation[1]) == 0


def main():
    check_wheel(('P1', 'P2', 'Q1'), 5)   # H = 2P+Q
    check_wheel(('P3', 'Q2', 'Q3'), 5)   # K = P+2Q
    check_wheel(('H1', 'H2', 'K1'), 9)   # phi H = 2H+K
    check_join()                         # phi K = H+K
    check_corner_budgets()
    check_split_edge_turn()
    print('PASS: four fixed boundary pairings, corner budgets, and split-edge turns')


if __name__ == '__main__':
    main()
