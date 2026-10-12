#!/usr/bin/env python3
"""Exact finite symbolic ledger; no spatial realizability assumption."""
from itertools import combinations_with_replacement, permutations
from collections import Counter

# Coefficients of x,y,360 after substituting z=360-x-y.
angle_types = [(1,0,0),(0,1,0),(-1,-1,1),(-2,0,1),(0,-2,1),(2,2,-1)]
identity_triples = [row for row in combinations_with_replacement(range(6),3)
                    if tuple(sum(angle_types[i][j] for i in row) for j in range(3)) == (0,0,1)]
assert identity_triples == [(0,0,3),(0,1,2),(1,1,4),(2,2,5),(3,4,5)]
native_types = [0,0,1,1,2,2,3,3,4,4,5,5]
native_triples = [row for row in combinations_with_replacement(range(12),3)
                  if tuple(sorted(native_types[i] for i in row)) in identity_triples]
assert len(native_triples) == 34
assert Counter(sum(i >= 6 for i in row) for row in native_triples) == {0:8,1:18,3:8}
def canonical(word):
    return min(v[k:]+v[:k] for v in (word,word[::-1]) for k in range(6))
bracelets = sorted({canonical(w) for w in permutations((0,0,1,1,2,2))})
assert len(bracelets) == 11
print('PASS: five exact type triples;34 native triples (8AAA,18AAB,8BBB);11 native bracelets')
print(' '.join(''.join(map(str,w)) for w in bracelets))
