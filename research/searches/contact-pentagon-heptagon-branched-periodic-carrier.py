"""Exact P5/Q7 changed signature: explicit2P/2Q branched periodic carrier.
No metric sampling or finite-patch extension inference.
"""
from sage.all import AA, QQ, vector, matrix
from itertools import product
r=AA(2).sqrt();c=((2+r)/4).sqrt();t=((2-r)/4).sqrt();w=r-2*t
vec=lambda x,y:vector(AA,[x,y])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in zip(F,F[1:]+F[:1]))/2
def check(F):
 assert area(F)>0
 for i,a in enumerate(F):
  b=F[(i+1)%len(F)]
  for j,p in enumerate(F):
   if j not in[i,(i+1)%len(F)]:assert cross(b-a,p-a)>0
P=[vec(0,0)]
for ell,d in zip([1,1,1,1,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vec(*d))
assert P[-1]==P[0];P.pop()
A=1+w/r;Q=[vec(0,0)]
for ell,d in zip([A,1,1,w,1,1,A],[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1)]):Q.append(Q[-1]+ell*vec(*d))
assert Q[-1]==Q[0];Q.pop();check(P);check(Q)
assert 0<w<1<A and A not in[1,w]
assert [(P[(i+1)%5]-P[i]).norm() for i in range(5)]==[1,1,1,1,w]
assert [(Q[(i+1)%7]-Q[i]).norm() for i in range(7)]==[A,1,1,w,1,1,A]
for F,angles in[(P,[5,5,4,5,5]),(Q,[4,6,6,6,6,6,6])]:
 for i,b in enumerate(F):
  e=F[i-1]-b;f=F[(i+1)%len(F)]-b;dot=e.dot_product(f)
  if angles[i]==4:assert dot==0
  else:
   assert dot<0
   assert dot**2==((2-r)/4 if angles[i]==5 else AA(QQ(1)/2))*e.dot_product(e)*f.dot_product(f)
# Complete unrestricted angular corner ledger, including species-labelled
# right sectors and all one-flat-host possibilities.
labels=["P90","P112","Q90","Q135"];units=[4,5,4,6];scores=[4,1,4,-2]
for total in[16,8]:
 stars=[C for C in product(range(5),repeat=4) if sum(a*b for a,b in zip(C,units))==total]
 assert all(sum(a*b for a,b in zip(C,scores))>=0 for C in stars)
 print("full" if total==16 else"flat",[(dict((s,n)for s,n in zip(labels,C)if n),sum(a*b for a,b in zip(C,scores)))for C in stars])
assert 4+4*1==8 and 4-6*2==-8
R=matrix(AA,[[1/r,-1/r],[1/r,1/r]])
assert R.transpose()*R==matrix.identity(AA,2) and R.det()==1
B=vec(A,0)
W=[R*(p-P[4])+Q[4] for p in P]
reps=[Q,[B-q for q in Q],W,[B-p for p in W]]
D=vec(A,-A);U=Q[2]-B+W[2]
pairs=[((0,0),(1,0),(0,0)),((0,1),(0,5),(1,0)),((0,2),(3,1),(0,1)),((0,3),(2,4),(0,0)),((0,4),(3,2),(-1,1)),((0,6),(1,6),(-1,0)),((1,1),(1,5),(-1,0)),((1,2),(2,1),(0,-1)),((1,3),(3,4),(0,0)),((1,4),(2,2),(1,-1)),((2,0),(3,0),(0,1)),((2,3),(3,3),(-1,1))]
seen=[]
for(f,i),(g,j),(m,n) in pairs:
 seen.extend([(f,i),(g,j)]);shift=m*D+n*U
 assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
 assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
assert len(set(seen))==24 and set(seen)=={(f,i)for f,F in enumerate(reps)for i in range(len(F))}
assert area(reps[0])==area(reps[1])==area(Q)
assert area(reps[2])==area(reps[3])==area(P)
assert cross(D,U)>0 and sum(area(F) for F in reps)==cross(D,U)
assert [(f,i)for(f,i),(g,j),mn in pairs if f==0 and g in[0,1]]==[(0,0),(0,1),(0,6)]
print("PASS: genuine positive P5/Q7,nativeangles,lengths,2Q/2P reps,12reversedpairs/24edges/48coordinates,positivecovolume=area;QQmask0,1,5,6 branches at Q90")
print("Parea",area(P),"Qarea",area(Q),"A",A,"periods",D,U)

# Full analytic extension: any positive right pentagon, one freely positive
# a-side length. Same12 fixed pairs, exact polynomial identities, no sampling.
def verify_family():
 from sage.all import NumberField,PolynomialRing
 Z=PolynomialRing(QQ,"z");z=Z.gen()
 K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
 c=K.gen();r=4*c*c-2;t=r/(4*c)
 T=PolynomialRing(K,["x","y","u","a"]);x,y,u,a=T.gens()
 v=u+r*c*(x-y);w=(u+v)/r-t*(x+y)
 A=v+w/r;B=u+w/r
 vec=lambda x,y:vector(T,[x,y])
 P=[vec(0,0)];Q=[vec(0,0)]
 for ell,d in zip([x,u,v,y,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vec(*d))
 assert P[-1]==P[0];P.pop()
 for ell,d in zip([A,a,u,w,v,a,B],[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1)]):Q.append(Q[-1]+ell*vec(*d))
 assert Q[-1]==Q[0];Q.pop()
 for F,angles in[(P,[5,5,4,5,5]),(Q,[4,6,6,6,6,6,6])]:
  for i,p in enumerate(F):
   e=F[i-1]-p;f=F[(i+1)%len(F)]-p;dot=e.dot_product(f)
   if angles[i]==4:assert dot==0
   else:assert dot**2==((2-r)/4 if angles[i]==5 else K(QQ(1)/2))*e.dot_product(e)*f.dot_product(f)
 R=matrix(T,[[1/r,-1/r],[1/r,1/r]])
 assert R.transpose()*R==matrix.identity(T,2) and R.det()==1
 W=[R*(p-P[4])+Q[4] for p in P]
 reps=[Q,[vec(A,0)-q for q in Q],W,[vec(A,0)-p for p in W]]
 D=vec(A,-B);U=Q[2]-vec(A,0)+W[2]
 for(f,i),(g,j),(m,n) in pairs:
  shift=m*D+n*U
  assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
  assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
 assert sum(area(F)for F in reps)==cross(D,U)
 assert area(reps[0])==area(reps[1])==area(Q)
 assert area(reps[2])==area(reps[3])==area(P)
 print("PASS: fullK[x,y,u,a] symbolic family,12pairs/48coordinate identities,closures/rotations/nativeangles andarea; allpositivePmetrics,a>0, no sampling or symmetry premise")
verify_family()
