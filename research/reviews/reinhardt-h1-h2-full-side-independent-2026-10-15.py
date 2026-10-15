"""Check two fixed whole-side torus witnesses; no enumeration or producer imports.

Source convention: corner i; native side i joins corners i and i+1.
An oriented face of sign s has native corner s*k modulo 6 at boundary
position k. Its native edge is k (s=+) or -k-1 (s=-).
All pairings reverse oriented boundary endpoints. Extra accidental side
or angle equalities cause no problem.
"""

def check(name, signs, length_classes, legal_stars, pairs):
    n = len(signs)
    def edge(f, k):
        return k if signs[f] == 1 else (-k - 1) % 6
    def corner(f, k):
        return signs[f] * k % 6
    def label(i):
        return next(j for j, group in enumerate(length_classes) if i in group)
    mate = {}
    for a, b in pairs:
        assert a != b and a not in mate and b not in mate
        assert label(edge(*a)) == label(edge(*b))
        mate[a] = b
        mate[b] = a
    assert set(mate) == {(f,k) for f in range(n) for k in range(6)}
    unseen = set(mate)
    cycles = []
    while unseen:
        start = min(unseen)
        current = start
        cycle = []
        while current not in cycle:
            assert current in unseen
            unseen.remove(current)
            cycle.append(current)
            f,k = current
            current = mate[(f,(k-1)%6)]
        assert current == start
        native = tuple(sorted(corner(*c) for c in cycle))
        assert len(cycle) == 3 and native in legal_stars, (name,cycle,native)
        cycles.append(cycle)
    # This successor permutation computes complete circular vertex links.
    assert len(cycles) - len(pairs) + n == 0
    reached = {0}
    while True:
        extended = reached | {b[0] for a,b in mate.items() if a[0] in reached}
        if extended == reached:
            break
        reached = extended
    assert len(reached) == n
    # Reversed oriented side gluing gives orientability; connected closed
    # circular-link surface with Euler characteristic zero is a torus.
    print(f"PASS {name}: {n} faces, {len(pairs)} edges, {len(cycles)} trivalent vertices")

check("H1", (1,1), ((0,),(1,),(2,5),(3,),(4,)),
      {(0,1,2),(3,4,5)},
      [((0,0),(1,0)), ((0,1),(1,1)), ((0,2),(0,5)),
       ((1,2),(1,5)), ((0,3),(1,3)), ((0,4),(1,4))])
check("H2", (1,1,-1,-1), ((0,),(1,3),(2,5),(4,)),
      {(0,1,3),(2,4,5)},
      [((0,0),(1,0)), ((2,5),(3,5)), ((0,1),(2,2)),
       ((0,3),(2,4)), ((1,1),(3,2)), ((1,3),(3,4)),
       ((0,2),(3,0)), ((0,5),(3,3)), ((1,2),(2,0)),
       ((1,5),(2,3)), ((0,4),(1,4)), ((2,1),(3,1))])
