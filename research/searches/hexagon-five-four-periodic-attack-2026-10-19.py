#!/usr/bin/env python3
# Independent exact periodic omission certificate. Run with Python in arisearch.
from sage.all import QuadraticField, vector, matrix, ZZ
K=QuadraticField(3, "r");r=K.gen()
V=vector
lengths=[K(1),K(2),K(3),r,K(4)]
words=[(0,1,2,0,3,4),(0,1,1,0,2,3)]
angles=[(90,120,150,120,90,150),(150,120,90,150,90,120)]
rots={30:(r/2,K(1)/2),60:(K(1)/2,r/2),90:(K(0),K(1))}
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def polygon(word,ang):
 p=V(K,[0,0]);d=V(K,[1,0]);v=[]
 for i in range(6):
  v.append(p);p=p+lengths[word[i]]*d
  c,s=rots[180-ang[i]];d=V(K,[c*d[0]-s*d[1],s*d[0]+c*d[1]])
 assert p==V(K,[0,0]) and d==V(K,[1,0])
 edges=[v[(i+1)%6]-v[i] for i in range(6)]
 assert all(cross(edges[i],edges[(i+1)%6])>0 for i in range(6))
 # Every other vertex lies strictly left of each directed side: simplicity and strict convexity.
 assert all(cross(edges[i],v[j]-v[i])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
 return v
A,B=[polygon(w,a) for w,a in zip(words,angles)]
assert A==[V(K,x) for x in [(0,0),(1,0),(1,2),(1-3*r/2,K(7)/2),(-3*r/2,K(7)/2),(-2*r,2)]]
h=V(K,[2+2*r,0]);t=V(K,[-3*r/2,K(7)/2]);s=V(K,[2,2])
M=matrix(K,[h,t]).transpose();assert M.det()>0
polys=[A,[s-p for p in A]]
area=lambda p:sum(cross(p[i],p[(i+1)%6]) for i in range(6))/2
assert area(A)>0 and area(B)>0 and 2*area(A)==M.det()==7+7*r
# On the quotient by lattice Zh+Zt every directed edge has one oppositely
# directed mate, with the exact same endpoints. Retain their offsets.
ledger=[]
for f,p in enumerate(polys):
 for i in range(6):
  a,b=p[i],p[(i+1)%6];matches=[]
  for g,q in enumerate(polys):
   for j in range(6):
    u,v=q[j],q[(j+1)%6]
    if b-a!=u-v:continue
    z=M.inverse()*(a-v)
    if all(x in ZZ for x in z) and b-u==M*z:matches.append((g,j,tuple(z)))
  assert len(matches)==1,(f,i,matches)
  ledger.append((f,i,matches[0]))
print("PASS exact closure and strict convexity of A,B; two-tile A-only periodic certificate")
print("A vertices:",A);print("B vertices:",B)
print("periods:",h,t,"; second representative: -A +",s)
print("A area:",area(A),"; lattice determinant:",M.det())
print("edge mates (face,side)->(face,side,lattice offset):",ledger)
