#!/usr/bin/env python3
"""Independent unordered equivalence-block enumeration of the native cross22 gate.
No producer imports; no metric or geometric-existence inference from partitions.
"""
from itertools import product
C=(0,0,1,1,2,2)
def equivalence(eq):
 E={(i,i) for i in range(6)}|set(eq)|{(b,a)for a,b in eq}
 while True:
  F=E|{(a,d)for a,b in E for c,d in E if b==c}
  if F==E:break
  E=F
 return frozenset(frozenset(j for j in range(6)if(i,j)in E)for i in range(6))
def coarse(p,q):return all(any(B<=D for D in q)for B in p)
def H2(p):
 for r,s in product(range(6),(1,-1)):
  c=[C[(r+s*k)%6]for k in range(6)]
  e=[(r+k)%6 if s==1 else(r-k-1)%6 for k in range(6)]
  if set(c[i]for i in(0,1,3))=={0,1,2} and coarse(equivalence([(e[1],e[3]),(e[2],e[5])]),p):return True
 return False
req=[]
for side in range(6):
 for order in(0,1):
  ends=(side,(side+1)%6)[::(-1 if order else 1)]
  if any(C[a]==2 for a in ends):continue
  offers=[]
  for corner,neighbor in zip((4,5),ends):
   offer=[]
   for third in range(6):
    if sorted([C[corner],C[neighbor],C[third]])!=[0,1,2]:continue
    arms=tuple(e for e in((corner-1)%6,corner)if e!=4)+tuple(e for e in((neighbor-1)%6,neighbor)if e!=side)
    for rays in[((third-1)%6,third),(third,(third-1)%6)]:offer.append(list(zip(arms,rays)))
   offers.append(offer)
  for left,right in product(*offers):req.append(equivalence([(4,side)]+left+right))
# Restricted growth generation supplies every partition exactly once.
labels=[()]
for _ in range(6):labels=[p+(j,)for p in labels for j in range(max(p,default=-1)+2)]
allparts={equivalence([(i,j)for i in range(6)for j in range(i)if label[i]==label[j]])for label in labels}
actual={p for p in allparts if any(coarse(q,p)for q in req)}
minimal={p for p in req if not any(q!=p and coarse(q,p)for q in req)}
assert(len(req),len(set(req)),len(minimal),len(allparts),len(actual),sum(H2(p)for p in actual))==(96,26,4,203,41,40)
assert {p for p in actual if not H2(p)}=={equivalence([(0,3),(1,4),(2,5)])}
# Exact Laurent calculation; independently derived native turns.
from sage.all import PolynomialRing,QQ
R=PolynomialRing(QQ,'U');U=R.fraction_field().gen()
# u=180-x; native turns u,u,-5u,-5u,4u-180,4u-180.
rot=[U,U,U**-5,U**-5,-U**4,-U**4]
d=[U**0]
for r in rot[1:]:d.append(d[-1]*r)
assert d==[1,U,U**-4,U**-9,-U**-5,U**-1]
v=[(d[i]+d[i+3])*U**6/(1+U**3)for i in range(3)]
assert v==[U**3+U**-3-1,U**4-U,U**2]
# For54<u<72 all realparts negative, except transformation undefinedu60:
# 3u in(162,216),2u in(108,144), and
# cos4u-cosu=-2sin(5u/2)sin(3u/2), bothsines positive.
assert 90<3*54<3*72<270 and 90<2*54<2*72<180
assert 0<QQ(5)*54/2<QQ(5)*72/2<=180
assert 0<QQ(3)*54/2<QQ(3)*72/2<180
print('PASS independent96raycases,26requirements,4minimal,203partitions,41coarsenings,40H2; unique012012 has strict halfplane separator')
