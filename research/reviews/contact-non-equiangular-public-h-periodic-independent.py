"""Exact independent proposed public-H periodic carrier; no producer imports."""
from sage.all import QQ, AA, NumberField, PolynomialRing, vector, matrix
Z=PolynomialRing(QQ,"z");z=Z.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c);w=r-2*t
assert AA(w)>0 and AA(w)<1
def vec(a,b):return vector(K,[a,b])
def edges(F):return list(zip(F,F[1:]+F[:1]))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in edges(F))/2
P=[vec(0,0)]
for ell,d in zip((1,1,1,1,w),((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):P.append(P[-1]+ell*vec(*d))
assert P[-1]==P[0];P.pop()
Q=[vec(0,0)]
for d in((c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r)):Q.append(Q[-1]+vec(*d))
assert Q[-1]==Q[0];Q.pop()
for F in(P,Q):
 assert AA(area(F))>0
 for i,(a,b) in enumerate(edges(F)):
  assert all(AA(cross(b-a,p-a))>0 for j,p in enumerate(F) if j not in(i,(i+1)%len(F)))
R=matrix(K,[[t,-c],[c,t]]);assert R.transpose()*R==matrix.identity(K,2)
S=Q[1]-R*P[2];S1=Q[1]+R*P[1]
F0=[R*p+S for p in P];F1=[-R*p+S1 for p in P]
L=Q[3];U=Q[4]-S-S1
assert L==S1-S-R*(P[0]+P[4])
assert U==vec(-c-t,r+1+c-t)
B=matrix(K,[[L[0],U[0]],[L[1],U[1]]]);assert AA(B.det())>0
reps=[Q,F0,F1];segments={(f,i):(a,b) for f,F in enumerate(reps) for i,(a,b) in enumerate(edges(F))}
partners={}
for name,(a,b) in segments.items():
 matches=[]
 for other,(p,q) in segments.items():
  if a-q!=b-p:continue
  mn=B.inverse()*(a-q)
  if all(x in QQ and QQ(x).denominator()==1 for x in mn):matches.append((other,tuple(int(x) for x in mn)))
 assert len(matches)==1,(name,matches)
 partners[name]=matches[0]
assert len(partners)==18
for name,(other,shift) in partners.items():assert partners[other]==(name,tuple(-x for x in shift))
assert area(F0)==area(F1)==area(P)
assert B.det()==area(Q)+2*area(P)
print('PASS: public-H exact rank-two periodic carrier;1Q/2P;18native edges;9regenerated pairs;36endpoint identities;area=covolume')
print('L',L,'U',U,'det',B.det())
print('partners',partners)
