"""Exact adjacent-repeat Cairo arithmetic; geometry remains in the proof."""
from itertools import combinations_with_replacement
from sage.all import QuadraticField, PolynomialRing, vector
K=QuadraticField(3,"w");w=K.gen()
R=PolynomialRing(K,names=("a","d"));a,d=R.gens()
c=a+w*(a-d);e=w*c+d-2*a
assert e-2*c==(w-3)*(2*c+a)/3
# Equality a=c forces d=a; d=c has the same sole root.
assert c-a==w*(a-d)
assert c-d==(1+w)*(a-d)
# Positive exceptional host fixture, scaled so a=b=1.
a=b=K(1);c=(1+3*w)/4;d=(1+w)/4;e=(1+w)/2
L=(a,b,c,d,e)
assert all(x>0 for x in L)
assert b-c==w*(d-a) and e==w*c+d-2*a
assert len({a,c,d})==3 and e==2*d and e!=2*a and e!=2*c
V=lambda x,y:vector(K,(x,y))
P=[V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
for i in range(5):
 edge=P[(i+1)%5]-P[i]
 assert edge.dot_product(edge)==L[i]**2
 for j in range(5):
  if j not in (i,(i+1)%5):assert cross(edge,P[j]-P[i])>0
slots=[(a,b),(b,a),(c,d),(d,c)]
events=[(u,r,s) for(u,r),(v,s) in combinations_with_replacement(slots,2) if u==v]
assert len(events)==5 and all(r==s for u,r,s in events)
assert [(r,s) for u,r,s in events if r+s==e]==[(d,d)]
print("PASS: symbolic adjacent-repeat closure;5 equal-bank events; exact convex e=2d fixture; only d/d split contacts")
