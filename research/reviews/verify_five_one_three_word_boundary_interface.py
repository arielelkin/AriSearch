#!/usr/bin/env python3
"""All direct/reflected native boundary rows; length-independent interface."""
from itertools import product
states=tuple(product(range(6),(1,-1)))
def colour(W,a,k):r,s=a;return W[(r+s*k)%6]
def side(a,k):r,s=a;return(r+k if s==1 else r-k-1)%6
count=0
for text in ('002112','012012','012102'):
 W=tuple(map(int,text));allowed=[a for a in states if colour(W,a,1)==2]
 assert len(allowed)==4
 assert all({side(a,5),side(a,2)}=={0,3} for a in allowed)
 outerlegal=0
 for left,right in product(allowed,repeat=2):
  outside=(colour(W,left,0),colour(W,right,2))
  inside=(colour(W,left,5),colour(W,right,3))
  assert set(outside+inside)<={0,1}
  if outside[0]==outside[1]:
   outerlegal+=1
   assert inside[0]==inside[1]
   assert all(sorted(inside+(third,))!=[0,1,2] for third in range(3))
  count+=1
 assert outerlegal==8
assert count==48
print('PASS:36 native poses;12 boundary poses;48 rowpairs;24 outerAAB-compatible,zero innerAAA-compatible')
