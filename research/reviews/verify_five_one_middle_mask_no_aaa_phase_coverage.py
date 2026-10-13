#!/usr/bin/env python3
"""Exact native noAAA phase classification; no producer imports."""
from itertools import product
words=('001212','002112','010212','011202','012012','012021','012102')
B=(3,4,4,4,4,4);BP={0:((1,-1),(5,1)),1:((4,-1),(2,1))}
legal={tuple(sorted(t)) for t in ((0,0,4),(1,1,3),(2,4,4))}
def corner(W,state,k):r,s=state;return W[(r+s*k)%6]
def side(state,k):r,s=state;return(r+k if s==1 else r-k-1)%6
states=tuple(product(range(6),(1,-1)))
private={w:{i for i in range(6) if '2' not in (w[i],w[(i+1)%6])} for w in words}
empty=[];survive=[]
for w in words:
 obstruct=[i for i in range(6) if w[i]!='2' and {(i-1)%6,i}<=private[w]]
 if obstruct:empty.append(w)
 else:assert private[w]=={0,3};survive.append(w)
assert empty==['001212','010212','011202','012021']
assert survive==['002112','012012','012102']
data={
 '002112':({0:((1,1),(0,-1)),1:((4,1),(3,-1))},1,0,0),
 '012012':({0:((1,1),(4,1)),1:((0,-1),(3,-1))},1,1,1),
 '012102':({0:((1,1),(3,-1)),1:((0,-1),(4,1))},0,0,1)}
count=0
for w,(AP,h,v,offset) in data.items():
 A=tuple(map(int,w))
 derived={a for a in states if {side(a,2),side(a,5)}=={0,3}}
 assert derived==set(AP[0]+AP[1])
 for phase in (0,1):assert all(corner(A,AP[phase][0],k)==corner(A,AP[phase][1],k) for k in range(6))
 for p,q in product((0,1),repeat=2):
  matches=[corner(A,left,5)==corner(A,right,3) and corner(A,left,0)==corner(A,right,2) for left,right in product(AP[p],AP[q])]
  assert all(matches) if q==(p^h) else not any(matches)
 for lower,upper,bphase in product((0,1),repeat=3):
  for bits in product((0,1),repeat=7):
   b=BP[bphase][bits[0]]
   neighbours=[(B,BP[bphase^h][bits[1]]),(A,AP[upper][bits[2]]),(A,AP[upper^h][bits[3]]),
               (B,BP[bphase^h][bits[4]]),(A,AP[lower][bits[5]]),(A,AP[lower^h][bits[6]])]
   stars=[]
   for k in range(6):
    W1,s1=neighbours[k];W2,s2=neighbours[(k+1)%6]
    stars.append(tuple(sorted((corner(B,b,k),corner(W1,s1,k+2),corner(W2,s2,k+4)))))
   assert all(t in legal for t in stars)==(upper==(lower^v) and bphase==(lower^offset))
   count+=1
assert count==3072
print('PASS:7 middle-mask words;4 noAAA empty;3 two-state phase bases;3072 exact native wheels')
