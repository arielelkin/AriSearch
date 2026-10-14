"""Independent quartic/SAT true-host geometry and complete corner census.
No author imports or clipping routine; finite positive patches only.
"""
from sage.all import QQ, AA, NumberField, PolynomialRing, vector, matrix
from itertools import product
Z=PolynomialRing(QQ,"z");z=Z.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c);w=r-2*t
assert AA(w)>0 and AA(w)<1
I=matrix.identity(K,2)
def vec(a,b):return vector(K,[a,b])
def J(a):return vec(-a[1],a[0])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def edges(F):return list(zip(F,F[1:]+F[:1]))
def key(F):return frozenset(tuple(a) for a in F)
def area(F):return sum(cross(a,b) for a,b in edges(F))/2
P=[vec(0,0)]
for ell,d in zip((1,1,1,1,w),((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):P.append(P[-1]+ell*vec(*d))
assert P[-1]==P[0];P.pop()
Q=[vec(0,0)]
for ell,d in zip((2,1,1,1)*2,((c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r))):Q.append(Q[-1]+ell*vec(*d))
assert Q[-1]==Q[0];Q.pop()
for F in(P,Q):
 assert AA(area(F))>0
 for i,(a,b) in enumerate(edges(F)):
  assert all(AA(cross(b-a,p-a))>0 for j,p in enumerate(F) if j not in(i,(i+1)%len(F)))
def disjoint(F,G):
 for a,b in edges(F)+edges(G):
  n=J(b-a);f=[n.dot_product(p) for p in F];g=[n.dot_product(p) for p in G]
  if AA(max(f,key=AA))<=AA(min(g,key=AA)) or AA(max(g,key=AA))<=AA(min(f,key=AA)):return True
 return False
mid=(Q[0]+Q[1])/2
caps=[]
for endpoint in(Q[0],Q[1]):
 seen={}
 target=endpoint-mid
 for native,sign in product((1,3),(-1,1)):
  source=P[native]-P[2]
  A=matrix(K,[list(source),list(J(source))]).transpose()
  B=matrix(K,[list(target),list(sign*J(target))]).transpose()
  O=B*A.inverse();assert O.transpose()*O==I
  F=[mid+O*(p-P[2]) for p in P]
  if AA(cross(Q[1]-Q[0],sum(F,vec(0,0))/5-Q[0]))<0:seen[key(F)]=F
 assert len(seen)==1;caps.append(next(iter(seen.values())))
A,B=caps
assert all(disjoint(F,G) for i,F in enumerate((Q,A,B)) for G in(Q,A,B)[:i])
farA=next(a for a in(A[1],A[3]) if a!=Q[0]);farB=next(a for a in(B[1],B[3]) if a!=Q[1]);assert farA==farB
far=farA
ends=[]
for F in caps:
 j=F.index(far);ends.append(next(a for a in(F[j-1],F[(j+1)%5]) if a!=mid))
assert all((a-far).dot_product(a-far)==1 for a in ends)
farQs={}
for j,swap in product((2,3,6,7),(False,True)):
 S=matrix(K,[list(Q[j-1]-Q[j]),list(Q[(j+1)%8]-Q[j])]).transpose()
 a,b=ends[::-1] if swap else ends
 T=matrix(K,[list(a-far),list(b-far)]).transpose();O=T*S.inverse()
 assert O.transpose()*O==I
 F=[far+O*(p-Q[j]) for p in Q]
 farQs[key(F)]=F
assert len(farQs)==4
assert all(all(disjoint(F,G) for i,F in enumerate((Q,A,B,T)) for G in(Q,A,B,T)[:i]) for T in farQs.values())
units=(4,5,5,6,7);weights=(4,1,1,-2,-5)
full=[a for a in product(range(5),repeat=5) if sum(x*y for x,y in zip(units,a))==16]
flat=[a for a in product(range(5),repeat=5) if sum(x*y for x,y in zip(units,a))==8]
assert len(full)==7 and flat==[(2,0,0,0,0)]
assert all(sum(x*y for x,y in zip(weights,a))==(16 if a==(4,0,0,0,0) else 0) for a in full)
assert sum(x*y for x,y in zip(weights,flat[0]))==8
assert 4+4*1==8 and 2*1+4*(-2)+2*(-5)==-16
print('PASS: independent quartic geometry/SAT projections; unique cap/twoP; FOUR disjoint farQ extensions; complete7 full/1 flat corner stars; no author imports')
