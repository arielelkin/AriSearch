"""Exact repeated-arm monohedral counterexample: finite local arithmetic."""
from itertools import combinations_with_replacement
from sage.all import QuadraticField,vector
K=QuadraticField(3,"w");w=K.gen()
a=b=K(1);c=1+w/2;d=K(1)/2;e=w
L=(a,b,c,d,e)
assert b-c==w*(d-a) and e==w*c+d-2*a
V=lambda x,y:vector(K,(x,y))
P=[V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
for i in range(5):
 edge=P[(i+1)%5]-P[i]
 assert edge.dot_product(edge)==L[i]**2
 for j in range(5):
  if j not in(i,(i+1)%5):assert cross(edge,P[j]-P[i])>0
slots=[(a,b),(b,a),(c,d),(d,c)]
events=[(u,r,s) for(u,r),(v,s) in combinations_with_replacement(slots,2) if u==v]
assert len(events)==5
assert all(r==s for u,r,s in events)
assert {r+s for u,r,s in events}=={2*a,2*c,2*d}
assert e not in {r+s for u,r,s in events}
assert len({a,c,d})==3
assert c!=a and c!=d
print("PASS: repeated-arm exact convex Cairo shape;5 equal-bank events; no e subdivision; isolated120 e-seam obstruction")
