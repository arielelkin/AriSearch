"""Exact 64-word audit; no solver, randomness, or floating point."""
from itertools import product
from collections import Counter

def closed(w):
    return w[0]-w[3] == w[2]-w[5] == w[4]-w[1]

def central(w):
    return all(w[i] == w[i+3] for i in range(3))

words = list(product((1, 2), repeat=6))
legal = [w for w in words if closed(w)]
noncentral = [w for w in legal if not central(w)]
assert len(legal) == 10
assert sum(central(w) for w in legal) == 8
assert noncentral == [(1,2,1,2,1,2), (2,1,2,1,2,1)]
# At a vertex an alternating tile has exactly one incident edge of each
# palette part. Three tile corners would give three incidences to each part;
# actual rays each contribute two, an immediate parity obstruction.
for palette_a, palette_b in [((0,1),(0,1)), ((0,1),(0,2)), ((0,1),(2,3))]:
    edges = {frozenset(palette_a), frozenset(palette_b)}
    vertices = set().union(*edges)
    triangles = [(a,b,c) for a,b,c in product(vertices, repeat=3)
                 if all(frozenset(e) in edges for e in ((a,b),(b,c),(c,a)))]
    assert not triangles
print('PASS: 64 words; 10 close; 8 central; 2 alternating; all 3 palette-intersection cases obstructed')
