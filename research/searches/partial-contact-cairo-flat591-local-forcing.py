"""Exact finite local forcing on full flat591 interval; no infinite tiling claim."""
from sage.all import QuadraticField,vector,matrix,PolynomialRing
K=QuadraticField(3,"w");w=K.gen();R=PolynomialRing(K,"u");u=R.gen();V=lambda x,y:vector(R,(x,y));sample=K(2)/5
P=(1,u,(-3*w/2-K(7)/2)*u+3*w/2+K(3)/2,(3*w/2+K(3)/2)*u-w/2-K(1)/2,(-2*w-3)*u+w+2)
Q=((-w-K(3)/2)*u+w/2+1,(-w/2-1)*u+w+K(1)/2,(-2*w-4)*u+w+2,1,P[4])
def raw(W):
 a,b,c,d,e=W
 assert b-c==w*(d-a) and e==w*c+d-2*a
 return[V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
q=raw(Q);A,B,C,s,f=Q;F90=matrix(R,[[-1,0],[0,1]]);mirror=[V(2*A,0)+F90*z for z in q]
R30=matrix(R,[[w/2,-K(1)/2],[K(1)/2,w/2]]);fill=[q[2]+R30*z for z in q]
R60=matrix(R,[[K(1)/2,-w/2],[w/2,K(1)/2]]);pforced=[q[4]+R60*z for z in raw(P)]
F30=matrix(R,[[K(1)/2,w/2],[w/2,-K(1)/2]]);F300=-F30;center=pforced[3]
pcore=[[center+M*(z-center) for z in pforced] for M in(matrix.identity(R,2),F30,F300,-matrix.identity(R,2))]
fillmate=[fill[1]+F300*(z-fill[1]) for z in fill]
rightcore=[[V(2*A,0)+F90*z for z in p] for p in pcore]
def at(P,t):return [vector(K,[f(t) for f in z]) for z in P]
def axes(P,Q):
 normals=[]
 for L in(P,Q):
  for i in range(5):
   side=L[(i+1)%5]-L[i];direction=vector(K,[f(sample) for f in side]);n=vector(K,(-direction[1],direction[0]))
   assert side.dot_product(n)==0
   normals.append(n)
 return normals
def separate(P,Q,t):
 for n in axes(P,Q):
  a=[n.dot_product(z) for z in at(P,t)];b=[n.dot_product(z) for z in at(Q,t)]
  if max(a)<=min(b) or max(b)<=min(a):return True
 return False
pairs=[(fill,q),(fill,mirror),(fillmate,q),(fillmate,mirror),(fillmate,fill)]+[(p,t) for p in pcore+rightcore for t in(q,mirror,fill,fillmate)]+[(p,t) for p in pcore for t in rightcore]
lo=K(1)/3;hi=K(1)/2;roots=set()
for P,Q in pairs:
 for n in axes(P,Q):
  for p in P:
   for q0 in Q:
    delta=n.dot_product(p-q0)
    assert delta.degree()<=1
    if delta.degree()==1:
     root=-delta[0]/delta[1]
     if lo<root<hi:roots.add(root)
points=[lo]+sorted(roots)+[hi];samples=sorted(roots)+[(a+b)/2 for a,b in zip(points,points[1:])]
bad=[(str(t),j) for t in samples for j,(P,Q) in enumerate(pairs) if not separate(P,Q,t)]
print("Exact SAT critical roots",len(roots),"pair count",len(pairs),"samples",len(samples))
print("Strict overlap cases",bad)
print("Positive interval local disjointness",not bad)

assert not bad
