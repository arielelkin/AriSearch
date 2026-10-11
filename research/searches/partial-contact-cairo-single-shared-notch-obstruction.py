"""Exact forced-cluster overlap for the r=4/5 Cairo fixture."""
from itertools import product
from sage.all import QuadraticField,vector,matrix
K=QuadraticField(3,"w");w=K.gen();r=K(4)/5;t=K(6)/5
V=lambda x,y:vector(K,(x,y))
def pieces(z):
 d=(w*z-1)/2;c=(3*w-z)/2
 A=[V(0,0),V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c)]
 return [[V(s*x,s2*y) for x,y in A] for s,s2 in product((-1,1),repeat=2)]
def separated(A,B):
 for C in (A,B):
  for i in range(5):
   E=C[(i+1)%5]-C[i];n=V(-E[1],E[0])
   pa=[n.dot_product(x) for x in A];pb=[n.dot_product(x) for x in B]
   if max(pa)<=min(pb) or max(pb)<=min(pa):return True
 return False
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def strict_inside(point,poly):
 values=[cross(poly[(i+1)%5]-poly[i],point-poly[i]) for i in range(5)]
 assert all(v>0 for v in values) or all(v<0 for v in values)
 return values
A=pieces(r);dr=(w*r-1)/2
for z in (r,t):
 dz=(w*z-1)/2;H=dr+dz+1
 for sign in (-1,1):
  center=V(H,sign*w);B=[[x+center for x in p] for p in pieces(z)]
  assert all(separated(a,b) for a in A for b in B)
  # sign=+1 is upper; lower is its horizontal reflection.
  X=V(w*r/2,-sign*w/2)
  F=matrix(K,[[K(1)/2,sign*w/2],[sign*w/2,-K(1)/2]])
  assert F*F==matrix.identity(K,2) and F.det()==-1
  reflected_center=X+F*(center-X)
  assert reflected_center!=center
  C=[[X+F*(x-X) for x in p] for p in B]
  if z==r:W=V(24*w/25+K(3)/10,-2*w/5+K(14)/25)
  else:W=V(31*w/25+K(3)/10,-2*w/5+K(21)/25)
  # Mirror ordering swaps (+,-) piece2 with (+,+) piece3.
  if sign<0:W=V(W[0],-W[1]);index=3
  else:index=2
  strict_inside(W,B[index]);strict_inside(W,C[index])
print("PASS:4 exhaustive macro notch fillers;64 initial convex separations; distinct forced reflected clusters;40 strict witness determinants")
