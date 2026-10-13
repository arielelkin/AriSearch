#!/usr/bin/env python3
"""Independent finite native phase and binary equality checks; no search imports."""
from itertools import product
A=(0,0,2,1,1,2);B=(3,4,4,4,4,4)
AP={0:((1,1),(0,-1)),1:((4,1),(3,-1))}
BP={0:((1,-1),(5,1)),1:((4,-1),(2,1))}
legal={tuple(sorted(t)) for t in ((0,0,4),(1,1,3),(2,4,4))}
def corner(word,state,k):r,s=state;return word[(r+s*k)%6]
def side(state,k):r,s=state;return (r+k if s==1 else r-k-1)%6
for phase in (0,1):
 assert {side(a,5) for a in AP[phase]}=={3*phase}
 assert {side(a,2) for a in AP[phase]}=={3*(1-phase)}
 assert all(corner(A,AP[phase][0],k)==corner(A,AP[phase][1],k) for k in range(6))
 assert all(corner(B,BP[phase][0],k)==corner(B,BP[phase][1],k) for k in range(6))
 # Both AA seam endpoints have the same non2 colour regardless of chirality.
 for left,right in product(AP[phase],AP[1-phase]):
  assert side(left,5)==side(right,2)
  assert corner(A,left,5)==corner(A,right,3)==phase
  assert corner(A,left,0)==corner(A,right,2)==phase
# Four A neighbours lie in upper/lower rows; row phases must coincide.
count=0
for lower,upper,bphase in product((0,1),repeat=3):
 for bits in product((0,1),repeat=7):
  b=BP[bphase][bits[0]]
  neighbours=[(B,BP[1-bphase][bits[1]]),(A,AP[upper][bits[2]]),
              (A,AP[1-upper][bits[3]]),(B,BP[1-bphase][bits[4]]),
              (A,AP[lower][bits[5]]),(A,AP[1-lower][bits[6]])]
  stars=[]
  for k in range(6):
   word1,state1=neighbours[k];word2,state2=neighbours[(k+1)%6]
   stars.append(tuple(sorted((corner(B,b,k),corner(word1,state1,k+2),corner(word2,state2,k+4)))))
  valid=all(t in legal for t in stars)
  assert valid==(lower==upper==bphase)
  count+=1
# Equality of two binary-valued length functions always has a conjunction of
# pins and signed binary equalities. Enumerate all four-value equality types
# redundantly with values0..3: all Bell4 partitions occur.
universe={(0,0),(0,1),(1,0),(1,1)}
atoms=[{p for p in universe if p[j]==v} for j in (0,1) for v in (0,1)]
atoms += [{p for p in universe if p[0]==p[1]}, {p for p in universe if p[0]!=p[1]}]
expressible=set()
for selected in product((0,1),repeat=6):
 rel=universe.copy()
 for use,atom in zip(selected,atoms):
  if use:rel &= atom
 expressible.add(frozenset(rel))
relations=set()
for a0,a1,b0,b1 in product(range(4),repeat=4):
 rel=frozenset((i,j) for i,j in universe if (a0,a1)[i]==(b0,b1)[j])
 assert rel in expressible and len(rel)!=3
 relations.add(rel)
print('PASS:4 A/4 B states;1024 native wheel phase/chirality assignments;256 binary equality-value assignments')
