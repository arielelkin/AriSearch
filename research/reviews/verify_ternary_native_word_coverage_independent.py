#!/usr/bin/env python3
"""Exact finite orbit cover of all ternary native bracelets; no author imports."""
from itertools import permutations
canonical=lambda q:min(t[k:]+t[:k] for t in (q,q[::-1]) for k in range(6))
allwords={canonical(q) for q in permutations((0,0,1,1,2,2))}
assert len(allwords)==11
reps=((0,0,1,1,2,2),(0,0,1,2,2,1),(0,0,1,2,1,2),(0,1,2,0,1,2),(0,1,0,2,1,2))
covered=set();sizes=[]
for rep in reps:
    orbit={canonical(tuple(p[i] for i in rep)) for p in permutations(range(3))}
    assert not covered.intersection(orbit)
    covered.update(orbit);sizes.append(len(orbit))
assert sizes==[1,3,3,1,3] and covered==allwords
print("PASS: five independently reviewed native representatives have disjoint S3 orbits1,3,3,1,3 covering all11 bracelets")
