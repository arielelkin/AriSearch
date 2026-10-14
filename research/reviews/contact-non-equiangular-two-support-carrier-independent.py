"""Independent symbolic two-support periodic carrier; no author imports.
Domain: x,y,u,H>0; v=u+r*c*(x-y)>0;
w=(u+v)/r-t*(x+y)>0. Verifies every positive right-P metric.
"""
from sage.all import QQ, AA, NumberField, PolynomialRing, vector
from itertools import product
Z=PolynomialRing(QQ,"z");z=Z.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c)
R=PolynomialRing(K,["x","y","u","H"]);x,y,u,H=R.gens()
v=u+r*c*(x-y);w=(u+v)/r-t*(x+y)
assert (u-v)/r==c*(y-x) and w==(u+v)/r-t*(x+y)
def vec(a,b):return vector(R,[a,b])
def edges(F):return list(zip(F,F[1:]+F[:1]))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in edges(F))/2
P=[vec(0,0)]
for ell,d in zip((x,u,v,y,w),((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):P.append(P[-1]+ell*vec(*d))
assert P[-1]==P[0];P.pop()
Q=[vec(0,0)]
for ell,d in zip((H,u,w,v)*2,((c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r))):Q.append(Q[-1]+ell*vec(*d))
assert Q[-1]==Q[0];Q.pop()
for F,angles in((P,(5,5,4,5,5)),(Q,(5,7,6,6,5,7,6,6))):
 for i,a in enumerate(F):
  e=F[i-1]-a;f=F[(i+1)%len(F)]-a;dot=e.dot_product(f)
  if angles[i]==4:assert dot==0
  else:
   ratio={5:(2-r)/4,6:QQ(1)/2,7:(2+r)/4}[angles[i]]
   assert dot*dot==ratio*e.dot_product(e)*f.dot_product(f)
reps=[Q,[p+Q[3]-P[4] for p in P],[-p+Q[7]+P[4] for p in P]]
L=Q[1]-Q[4];U=Q[1]-Q[7]+P[2]-P[4]
segments={(f,i):(a,b) for f,F in enumerate(reps) for i,(a,b) in enumerate(edges(F))}
partners={}
for key,(a,b) in segments.items():
 matches=[]
 for other,(p,q) in segments.items():
  for m,n in product((-1,0,1),repeat=2):
   shift=m*L+n*U
   if a==q+shift and b==p+shift:matches.append((other,(m,n)))
 assert len(matches)==1,(key,matches)
 partners[key]=matches[0]
assert len(partners)==18
for key,(other,(m,n)) in partners.items():assert partners[other]==(key,(-m,-n))
assert area(reps[1])==area(reps[2])==area(P)
assert cross(L,U)==area(Q)+2*area(P)
# This independent symbolic result includes the exact author's fixture.
fixture={x:K(1),y:(r*K(2)/3+c-t-1)/(c+t),u:K(2)/3,H:K(4)/3}
assert AA(y.subs(fixture))>0 and AA(v.subs(fixture))>0
assert AA(cross(L,U).subs(fixture))>0
print('PASS: independent symbolic field reconstruction; all18 native edges/9 reversed pairs/36 coordinate identities; every positive right-P metric; no producer imports')
print('covolume',cross(L,U))
