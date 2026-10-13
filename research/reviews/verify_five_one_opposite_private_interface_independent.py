#!/usr/bin/env python3
"""Independent global-slot boundary interface; endpoint-derived native sides."""
from itertools import product
poses=list(product(range(6),(1,-1)))
def co(W,p,k):return W[(p[0]+p[1]*k)%6]
def si(p,k):
 ends={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 return next(j for j in range(6) if {j,(j+1)%6}==ends)
count=0;outerlegal=0
for word in ('002112','012012','012102'):
 W=tuple(map(int,word));eligible=[p for p in poses if co(W,p,1)==2]
 assert len(eligible)==4
 for p in eligible:
  assert {si(p,5),si(p,2)}=={0,3}
  assert {co(W,p,0),co(W,p,5)}<={0,1}
  assert {co(W,p,2),co(W,p,3)}<={0,1}
 for p,q in product(eligible,repeat=2):
  outer=(co(W,p,0),co(W,q,2));inner=(co(W,p,5),co(W,q,3))
  if word=='002112':assert inner==outer
  else:assert inner==tuple(1-v for v in outer)
  assert not(outer[0]==outer[1] and inner[0]!=inner[1])
  outerlegal+=outer[0]==outer[1];count+=1
assert count==48 and outerlegal==24
print('PASS all12 native states perword;48 eligibleinterfaces;24 legalouterAAB;zero innerAAA-compatible;allmetric/reflection scope')
