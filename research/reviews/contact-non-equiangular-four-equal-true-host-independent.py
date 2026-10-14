"""Independent quartic-coordinate cap and mixedM/V endpoint check."""
from sage.all import QQ,AA,PolynomialRing,NumberField,vector,matrix
from itertools import product
R=PolynomialRing(QQ,"z");z=R.gen();K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt());c=K.gen();r=4*c*c-2;t=r/(4*c);w=r-2*t
vec=lambda x,y:vector(K,[x,y])
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
edges=lambda P:list(zip(P,P[1:]+P[:1]))
area=lambda P:sum(cross(p,q) for p,q in edges(P))/2
P=[vec(0,0),vec(c,-t),vec(c+1/r,-t+1/r),vec(c,r-t),vec(0,w)]
Q=[vec(0,0)]
for length,d in zip([2,1,1,1]*2,[(c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r)]):Q.append(Q[-1]+length*vec(*d))
assert Q.pop()==Q[0]
assert 0<AA(w)<1
for poly,angles in((P,[5,5,4,5,5]),(Q,[5,7,6,6,5,7,6,6])):
 for i,(a,b) in enumerate(edges(poly)):
  for j,p in enumerate(poly):
   if j not in(i,(i+1)%len(poly)):assert AA(cross(b-a,p-a))>0
  u=poly[i-1]-a;v=b-a;n=angles[i];dot=u.dot_product(v)
  if n==4:assert dot==0
  else:
   assert AA(dot)<0
   assert dot**2=={5:(2-r)/4,6:K(1)/2,7:(2+r)/4}[n]*u.dot_product(u)*v.dot_product(v)
assert all(Q[i]+Q[i+4]==Q[0]+Q[4] for i in range(4))
def disjoint(A,B):
 for p,q in edges(A)+edges(B):
  e=q-p;n=vec(-e[1],e[0]);a=[z.dot_product(n) for z in A];b=[z.dot_product(n) for z in B]
  if max(a,key=AA)<=min(b,key=AA) or max(b,key=AA)<=min(a,key=AA):return True
 return False
def poses(S,a,b):
 images={}
 for p,q in edges(S):
  e=q-p;L=e.dot_product(e)
  if L!=(b-a).dot_product(b-a):continue
  for first,last in((a,b),(b,a)):
   f=last-first;n=vec(-f[1],f[0])
   for sign in(-1,1):
    image=[first+(z-p).dot_product(e)/L*f+sign*cross(e,z-p)/L*n for z in S]
    if all(AA(cross(b-a,z-a))<=0 for z in image):images.setdefault(frozenset(tuple(z) for z in image),image)
 return list(images.values())
m=(Q[0]+Q[1])/2
left=[F for F in poses(P,Q[0],m) if F[2]==m];right=[F for F in poses(P,m,Q[1]) if F[2]==m]
assert len(left)==len(right)==1;A,B=left[0],right[0]
far=next(z for z in(A[1],A[3]) if z!=Q[0]);assert far==next(z for z in(B[1],B[3]) if z!=Q[1])
def outside_bevel(F):
 i=F.index(far);return next(z for z in(F[i-1],F[(i+1)%5]) if z!=m)
sa=outside_bevel(A);sb=outside_bevel(B)
farQs={}
for F in poses(Q,far,sa)+poses(Q,sa,far):
 if far not in F:continue
 i=F.index(far)
 if i in(2,3,6,7) and frozenset(tuple(z) for z in(F[i-1],F[(i+1)%8]))==frozenset((tuple(sa),tuple(sb))):farQs[frozenset(tuple(z) for z in F)]=F
assert len(farQs)==4
for F in farQs.values():
 patch=[Q,A,B,F]
 assert all(disjoint(patch[i],patch[j]) for i in range(4) for j in range(i))
# The sole angle-compatible M/Vmate exposes a private2edge opposite Pbevel1.
Uguests=[F for F in poses(P,Q[1],Q[2]) if F[2]==Q[1]]
assert len(Uguests)==1;guest=Uguests[0]
Mmates=poses(Q,Q[2],Q[3]);compatible=[]
for F in Mmates:
 if Q[2] not in F:continue
 i=F.index(Q[2])
 if i not in(0,4):continue
 compatible.append(F)
assert len(compatible)==1
F=compatible[0];i=F.index(Q[2]);hostend=F[(i+1)%8];assert (hostend-Q[2]).dot_product(hostend-Q[2])==4
g=guest.index(Q[2]);tip=next(z for z in(guest[g-1],guest[(g+1)%5]) if z!=Q[1])
assert tip==(Q[2]+hostend)/2
assert tip in guest and tip not in F
assert g in(1,3)
# Native full/flat angle and weight census independently enumerated.
units=(4,5,5,6,7);weights=(4,1,1,-2,-5)
full=[v for v in product(range(5),repeat=5) if sum(a*b for a,b in zip(v,units))==16]
flat=[v for v in product(range(5),repeat=5) if sum(a*b for a,b in zip(v,units))==8]
assert len(full)==7 and flat==[(2,0,0,0,0)]
assert [sum(a*b for a,b in zip(v,weights)) for v in full].count(16)==1
assert all(sum(a*b for a,b in zip(v,weights)) in(0,16) for v in full)
print("PASS: independent convexshape reconstruction,complete7/1anglecensus,Qtruecap/fourfarQextensions viaSAT,mixedM/V unitP112endpoint exactlyinsideprivate2host")
