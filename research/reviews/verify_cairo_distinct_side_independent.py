#!/usr/bin/env python3
"""Independent complete cross-equality and closure-kernel audit, ETE only."""
from itertools import combinations, permutations, combinations_with_replacement
from sage.all import AA, QuadraticField, matrix, vector

K = QuadraticField(3, "w", embedding=AA(3).sqrt())
w = K.gen()
beta = (1,3,4)  # corner after side
A = (0,1,2,3,4)
corners = tuple((n,i) for n in ("A","B") for i in beta)
star_candidates = tuple(combinations_with_replacement(corners,3))


def all_cross_equalities():
    # Exact equivalence relations with each type internally injective.
    # Unmatched B slots have private symbols 5+i; they cannot equal each other.
    for k in range(6):
        for slots in combinations(range(5),k):
            for labels in permutations(range(5),k):
                b = [5+i for i in range(5)]
                for i,a in zip(slots,labels):
                    b[i] = a
                yield tuple(b)


def allowed_beta_star(star, words):
    if len({n for n,i in star}) == 1:
        return False
    edges = [frozenset((words[n][i],words[n][(i+1) % 5])) for n,i in star]
    if len(set(edges)) != 3:
        return False  # in particular, two copies of the same corner cannot help
    rays = set().union(*edges)
    return len(rays) == 3 and set(edges) == {frozenset(z) for z in combinations(rays,2)}


def main():
    supports = []
    count = 0
    for b in all_cross_equalities():
        count += 1
        words = {"A":A,"B":b}
        legal = [star for star in star_candidates if allowed_beta_star(star,words)]
        covered = set().union(*(set(s) for s in legal)) if legal else set()
        if covered == set(corners):
            supports.append(b)
    assert count == 1546
    expected = {(z0,z1,z2,z3,f) for z0,z3 in ((1,2),(2,1))
                for z1,z2 in ((0,3),(3,0)) for f in (4,9)}
    assert set(supports) == expected and len(supports) == 8
    # Derive closure directly from the five direction vectors, then compute
    # its full linear kernel.  No author's eliminated residuals are used.
    directions = [(K(1),K(0)),(K(0),K(1)),(-w/2,K(1)/2),
                  (-K(1)/2,-w/2),(K(1)/2,-w/2)]
    def rows(word):
        out = [[K(0)]*6 for _ in range(2)]
        for i,slot in enumerate(word):
            for d in (0,1):
                out[d][slot] += directions[i][d]
        return out
    cases = [(1,0,3,2,5),(2,0,3,1,5),(1,3,0,2,5),(2,3,0,1,5)]
    for b in cases:
        closure = matrix(K,rows((0,1,2,3,4))+rows(b))
        assert closure.rank() == 4
        kernel = closure.right_kernel()
        assert kernel.dimension() == 2
        assert all(z[0] == z[3] and z[1] == z[2] for z in kernel.basis())
        # Equivalent row-space proof applies to every closed side-length vector.
        assert vector(K,[1,0,0,-1,0,0]) in closure.row_space()
        assert vector(K,[0,1,-1,0,0,0]) in closure.row_space()
    print("PASS independent ETE-only audit: all1546 internally-injective cross-equality patterns; "
          "exactly8 beta-covering supports (four words, private side new or equal e); "
          "all four direct vector-closure kernels force a=d and b=c.")


if __name__ == "__main__":
    main()
