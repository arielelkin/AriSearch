#!/usr/bin/env python3
"""Endpoint-derived row-state enumeration; no author imports."""
from itertools import product
A=(0,0,2,1,1,2);B=(3,4,4,4,4,4)
states=list(product(range(6),(1,-1)))
def corner(w,p,k):return w[(p[0]+p[1]*k)%6]
def side(p,k):
 ends={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 ans=[j for j in range(6) if {j,(j+1)%6}==ends]
 assert len(ans)==1
 return ans[0]
a=[p for p in states if {side(p,5),side(p,2)}=={0,3}]
b=[p for p in states if {side(p,5),side(p,2)}=={1,4}]
AP={h:[p for p in a if side(p,5)==3*h] for h in (0,1)}
BP={h:[p for p in b if corner(B,p,1 if h==0 else 4)==3] for h in (0,1)}
assert all(len(t)==2 for t in list(AP.values())+list(BP.values()))
for word,groups in ((A,AP),(B,BP)):
 for group in groups.values():
  assert len({tuple(corner(word,p,k) for k in range(6)) for p in group})==1
legal={tuple(sorted(t)) for t in ((0,0,4),(1,1,3),(2,4,4))}
valid=0
for h,l,c in product((0,1),repeat=3):
 for p in BP[c]:
  for choices in product(BP[1-c],AP[h],AP[1-h],BP[1-c],AP[l],AP[1-l]):
   words=[B,A,A,B,A,A]
   stars=[tuple(sorted((corner(B,p,k),corner(words[k],choices[k],k+2),corner(words[(k+1)%6],choices[(k+1)%6],k+4)))) for k in range(6)]
   ok=all(star in legal for star in stars)
   assert ok==(h==l==c)
   valid+=ok
assert valid==256
for h in (0,1):
 for p,q in product(AP[h],AP[1-h]):
  assert side(p,5)==side(q,2)
  assert corner(A,p,0)==corner(A,q,2)==h
  assert corner(A,p,5)==corner(A,q,3)==h
print('PASS endpoint-derived fourA/fourB states;1024 complete wheels;256 valid aligned wheels;all chirality AA seams')
