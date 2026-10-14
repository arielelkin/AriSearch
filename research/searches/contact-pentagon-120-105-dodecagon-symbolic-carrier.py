"""Exact all-positive-middle-length 6P/1Q periodic carrier; Sage number field."""
from sage.all import QQ,PolynomialRing,NumberField,AA
import json
B=PolynomialRing(QQ,'t');t=B.gen()
K=NumberField(t**4-4*t**2+1,'R',embedding=(AA(2)+AA(3).sqrt()).sqrt())
R=K.gen();assert AA(R)>1
s3=R**2-2;assert s3*s3==3 and AA(s3)>0
S=PolynomialRing(K,'w');w=S.gen();F=S.fraction_field()
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(c,p):return tuple(c*x for x in p)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rot(p):return ((s3*p[0]-p[1])/2,(p[0]+s3*p[1])/2)
def positive(p):
 p=S(p);assert p and all(AA(c)>=0 for c in p.list()) and any(AA(c)>0 for c in p.list())
def area(p):return sum(cross(a,p[(i+1)%len(p)]) for i,a in enumerate(p))/2
Q=[(S(R),S(0))]
for i in range(11):Q.append(rot(Q[-1]))
assert rot(Q[-1])==Q[0]
for i,p in enumerate(Q):
 outgoing=sub(Q[(i+1)%12],p);incoming=sub(Q[(i-1)%12],p)
 assert dot(outgoing,outgoing)==1 and dot(incoming,outgoing)==-s3/2
 for j,z in enumerate(Q):
  if j not in (i,(i+1)%12):positive(cross(outgoing,sub(z,p)))
d=2*R+w;a=(d,S(0));b=(d/2,s3*d/2);V=(d/2,d/(2*s3))
P=[V,Q[1],Q[0],add(a,Q[6]),add(a,Q[5])]
x=(w+1/R)/s3
assert dot(sub(P[1],P[0]),sub(P[1],P[0]))==x*x
lengths=[x,1,w,1,x];cosines=[-K(1)/2,-1/(2*R),-1/(2*R),-1/(2*R),-1/(2*R)]
for i,p in enumerate(P):
 incoming=sub(P[(i-1)%5],p);outgoing=sub(P[(i+1)%5],p)
 assert dot(outgoing,outgoing)==lengths[i]**2
 assert dot(incoming,outgoing)==cosines[i]*lengths[i-1]*lengths[i]
 positive(-dot(incoming,outgoing))
 for j,z in enumerate(P):
  if j not in (i,(i+1)%5):positive(cross(outgoing,sub(z,p)))
reps=[Q];U=P
for k in range(6):
 reps.append(U);U=[rot(rot(z)) for z in U]
assert U==P
covol=cross(a,b);positive(covol)
assert sum(area(p) for p in reps)==covol
partners=[]
for k,T in enumerate(reps):
 for i,p in enumerate(T):
  end=T[(i+1)%len(T)];found=[]
  for l,U in enumerate(reps):
   for j,z in enumerate(U):
    shift=sub(p,U[(j+1)%len(U)])
    if add(z,shift)!=end:continue
    m=F(cross(shift,b))/F(covol);n=F(cross(a,shift))/F(covol)
    if m in QQ and n in QQ and QQ(m).denominator()==QQ(n).denominator()==1:found.append((l,j,int(m),int(n)))
  assert len(found)==1,(k,i,found)
  partners.append([k,i,*found[0]])
assert len(partners)==42
print(json.dumps(dict(scope="P120/105 and regularQ12: all w>0 symbolic6P1Q carrier; unrestricted lattice partner solve",field=str(K.defining_polynomial()),parameter="w>0;u=1;x=y=(w+1/R)/sqrt3",P=P,Q=Q,reps=reps,periods=(a,b),covolume=covol,area_sum=sum(area(p) for p in reps),directed_partners=partners),default=str,indent=2))
