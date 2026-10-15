#!/usr/bin/env python3
"""Small independent color-incidence audit; no producer imports or metric inequalities.
The universal framed carrier and strip arguments are reviewed in prose.
"""
from itertools import product,permutations,combinations
from collections import Counter

def canonical(w):
 return min(tuple(v[i:]+v[:i]) for v in (list(w),list(reversed(w))) for i in range(6))
def renamed_orbit(w):
 return min(canonical(tuple(p[x] for x in w)) for p in permutations(range(3)))

# k=3: shared colors 0,1,2, private seams named by their unordered flank pair.
private_pairs=[frozenset(p) for p in combinations(range(3),2)]
valid={};raw=0;assignments=0
for B in product(range(3),repeat=6):
 if Counter(B)!=Counter({0:2,1:2,2:2}):continue
 raw+=1;choices=[]
 for i in range(6):
  r,s=B[i],B[(i+1)%6]
  choices.append([j for j,pair in enumerate(private_pairs) if r in pair and s in pair])
 for corona in product(*choices):
  if not all(corona[i-1]!=corona[i] for i in range(6)):continue
  valid.setdefault(renamed_orbit(B),set()).add(canonical(B));assignments+=1
assert raw==90 and len(valid)==2
assert set(valid)=={renamed_orbit((0,1,2,0,1,2)),renamed_orbit((0,0,1,2,2,1))}
# For representative xxy zzy: only x and z have loop corners. Their private
# seam reflects; the other two private seams exchange endpoints.
B=(0,0,1,2,2,1)
loops={B[i] for i in range(6) if B[i]==B[(i+1)%6]}
pairs={frozenset((B[i],B[(i+1)%6])) for i in range(6) if B[i]!=B[(i+1)%6]}
assert loops=={0,2} and pairs=={frozenset((0,1)),frozenset((1,2))}
for pair in private_pairs:
 modes=[]
 if pair in pairs:modes.append('halfturn')
 if pair<=loops:modes.append('reflection')
 assert modes==(['reflection'] if pair==frozenset((0,2)) else ['halfturn'])

# b=k=4, multiplicity(3,1,1,1): all960rawBwords over the two A-private normalizations.
# Use the maximally noninjective color-to-physical-length map ell(c)=1.
A=tuple(range(6));raw_four=0;seam_tests=0
ell={c:1 for c in A}
for private in ((0,2),(0,3)):
 alphabet=sorted(set(A)-set(private));count=0
 for B in product(alphabet,repeat=6):
  if sorted(Counter(B).values())!=[1,1,1,3]:continue
  count+=1;raw_four+=1
  loops={B[i] for i in range(6) if B[i]==B[(i+1)%6]}
  assert len(loops)<=1
  for side in private:
   flank={A[(side-1)%6],A[(side+1)%6]}
   assert len(flank)==2 and not flank<=loops
   assert ell[A[side]]==ell[B[0]] # physical privacy is deliberately ABSENT
   seam_tests+=1
 assert count==480
assert (raw_four,seam_tests)==(960,1920)
print('PASS: all90double-each three-color words give exactly the2corona classes; unique double-block seam modes; all960triple-repeat four-color words exclude reflected private-color seams despite every physical length being1.')
