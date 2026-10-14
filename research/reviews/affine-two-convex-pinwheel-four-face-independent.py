"""Independent exact four-face census: canonical-edge embeddings and clipping."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
add=lambda p,q:(p[0]+q[0],p[1]+q[1])
sub=lambda p,q:(p[0]-q[0],p[1]-q[1])
scale=lambda a,p:(a*p[0],a*p[1])
dot=lambda p,q:p[0]*q[0]+p[1]*q[1]
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
edges=lambda P:list(zip(P,P[1:]+P[:1]))
area=lambda P:sum(cross(p,q) for p,q in edges(P))/2 if len(P)>=3 else F(0)
def hull(points):
 points=sorted(set(points));first=points[0];out=[first]
 while True:
  p=out[-1];candidates=[q for q in points if q!=p and all(cross(sub(q,p),sub(z,p))>=0 for z in points)]
  q=max(candidates,key=lambda q:dot(sub(q,p),sub(q,p)))
  if q==first:return tuple(out)
  out.append(q);assert len(out)<=len(points)
def intersection(P,Q):
 P=list(P)
 for a,b in edges(Q):
  new=[]
  for p,q in edges(tuple(P)):
   cp=cross(sub(b,a),sub(p,a));cq=cross(sub(b,a),sub(q,a))
   if cp>=0:new.append(p)
   if (cp<0 and cq>0) or(cp>0 and cq<0):new.append(add(p,scale(cp/(cp-cq),sub(q,p))))
  P=list(dict.fromkeys(new))
  if not P:break
 return tuple(P)
base=((F(0),F(0)),(F(2),F(0)),(F(0),F(1)))
def attached(T,a,b):
 length=dot(sub(b,a),sub(b,a));source=[(p,q) for p,q in edges(base) if dot(sub(q,p),sub(q,p))==length];assert len(source)==1
 p,q=source[0];e=sub(q,p);images=set()
 for first,last in((a,b),(b,a)):
  f=sub(last,first);normal=(-f[1],f[0])
  for sign in(-1,1):
   image=hull([add(first,add(scale(dot(sub(z,p),e)/length,f),scale(sign*cross(e,sub(z,p))/length,normal))) for z in base])
   third=next(z for z in image if z not in(a,b));old=next(z for z in T if z not in(a,b))
   if cross(sub(b,a),sub(third,a))*cross(sub(b,a),sub(old,a))<0:images.add(image)
 assert len(images)==2;return images
def congruent(P,Q):
 if len(P)!=len(Q):return False
 for rev in(Q,Q[::-1]):
  for k in range(len(P)):
   S=rev[k:]+rev[:k]
   if all(dot(sub(P[i],P[j]),sub(P[i],P[j]))==dot(sub(S[i],S[j]),sub(S[i],S[j])) for i in range(len(P)) for j in range(i)):return True
 return False
patches={(base,)};counts=[1]
for n in(2,3,4):
 following=set()
 for patch in patches:
  for T in patch:
   for a,b in edges(T):
    for image in attached(T,a,b):
     if all(area(intersection(image,old))==0 for old in patch):following.add(tuple(sorted(patch+(image,))))
 patches=following;counts.append(len(patches))
assert counts==[1,6,36,221],counts
classes=[]
for patch in sorted(patches):
 P=hull([z for T in patch for z in T])
 if area(P)==4 and not any(congruent(P,Q) for Q in classes):classes.append(P)
assert len(classes)==15
assert Counter(map(len,classes))=={3:1,4:10,5:3,6:1}
H=tuple((F(x),F(y)) for x,y in[(0,0),("6/5","-8/5"),(2,-1),(2,0),("4/5","8/5"),(0,1)])
assert congruent(next(P for P in classes if len(P)==6),H)
assert area(H)==4 and all(add(H[i],H[i+3])==(2,0) for i in range(3))
U=(F(2),F(-1));V=(F(4,5),F(8,5));assert cross(U,V)==4
partners=[]
for i,(p,q) in enumerate(edges(H)):
 candidates=[]
 for j,(s,t) in enumerate(edges(H)):
  shift=sub(p,t)
  if sub(q,s)!=shift:continue
  m=cross(shift,V)/4;n=cross(U,shift)/4
  if m.denominator==n.denominator==1:candidates.append((j,int(m),int(n)))
 assert len(candidates)==1;candidates=candidates[0];partners.append(candidates)
assert len(set(tuple(sorted((i,p[0]))) for i,p in enumerate(partners)))==3
print("PASS independent canonical-edge embedding plus rational clipping:counts",counts,"convexclasses",dict(Counter(map(len,classes))),"hexagon3 reversed boundary pairs,covolume=area4")

# Supplementary omission carriers, independently reconstructed.
polys=[tuple((F(x),F(y)) for x,y in Z) for Z in[[(0,-1),("4/5","-8/5"),(2,0),("4/5","8/5"),(0,1)],[(0,-1),("4/5","-8/5"),(2,0),(2,1),(0,1)],[(0,-1),("4/5","-8/5"),("14/5","-3/5"),(2,0),(0,1)]]]
assert all(any(congruent(P,Q) for Q in classes if len(Q)==5) for P in polys)
assert not any(congruent(polys[i],polys[j]) for i in range(3) for j in range(i))
for index,P in enumerate(polys):
 supp=[]
 for i in range(5):
  e=sub(P[i],P[i-1]);f=sub(P[(i+2)%5],P[(i+1)%5])
  if cross(e,f)==0 and dot(e,f)<0:supp.append(i)
 assert supp==[[],[3],[1]][index]
 if not supp:continue
 i=supp[0];centre2=add(P[i],P[(i+1)%5]);image=tuple(sub(centre2,z) for z in P);H=hull(P+image)
 assert area(intersection(P,tuple(reversed(image))))==0 if area(image)<0 else area(intersection(P,image))==0
 assert len(H)==6 and area(H)==8
 U=scale(F(1,2),sub(add(H[3],H[4]),add(H[0],H[1])));V=scale(F(1,2),sub(add(H[4],H[5]),add(H[1],H[2])))
 covol=cross(U,V);assert abs(covol)==8
 for p,q in edges(H):
  matches=[]
  for s,t in edges(H):
   shift=sub(p,t)
   if sub(q,s)!=shift:continue
   m=cross(shift,V)/covol;n=cross(U,shift)/covol
   if m.denominator==n.denominator==1:matches.append((s,t,m,n))
  assert len(matches)==1
print("PASS supplementary B/C:exact halfturn2P partitions,strict6edge hulls,complete reversed boundary pairs,covol=area8; no claimAmono")
