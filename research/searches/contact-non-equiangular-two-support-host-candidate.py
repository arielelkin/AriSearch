"""One exact two-support/non-equiangular Q-host fixture; no metric sweep."""
from sage.all import AA, QQ, vector, matrix
from itertools import product
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def J(a):return vector(AA,[-a[1],a[0]])
def area(P):return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2

def check(P):
 for i,a in enumerate(P):
  b=P[(i+1)%len(P)]
  for j,c in enumerate(P):
   if j not in(i,(i+1)%len(P)):assert cross(b-a,c-a)>0

def intersect(P,Q):
 P=P if area(P)>0 else P[::-1]
 Q=Q if area(Q)>0 else Q[::-1]
 out=list(P)
 for a,b in zip(Q,Q[1:]+Q[:1]):
  if not out:break
  prev=out[-1];dp=cross(b-a,prev-a);new=[]
  for cur in out:
   dc=cross(b-a,cur-a)
   if(dp<0)!=(dc<0):new.append(prev+(cur-prev)*dp/(dp-dc))
   if dc>=0:new.append(cur)
   prev=cur;dp=dc
  out=new
 return out

def canonical(P):return tuple(sorted(tuple(v) for v in P))
def placements(S,A,B):
 """Every full-side opposite placement, allowing all native slots/reflections."""
 seen={}
 for i,sa in enumerate(S):
  sb=S[(i+1)%len(S)];e=sb-sa
  if e.dot_product(e)!=(B-A).dot_product(B-A):continue
  e=e/e.norm(); E=matrix(AA,[list(e),list(J(e))]).transpose()
  for ta,tb in((A,B),(B,A)):
   f=(tb-ta)/(tb-ta).norm()
   for det in(-1,1):
    F=matrix(AA,[list(f),list(det*J(f))]).transpose()*E.transpose()
    T=[ta+F*(p-sa) for p in S]
    centre=sum(T,vector(AA,[0,0]))/len(T)
    if cross(B-A,centre-A)>=0:continue
    seen[canonical(T)]=T
 return list(seen.values())


r=AA(2).sqrt();c=((2+r)/4).sqrt();t=((2-r)/4).sqrt()
x=w=AA(1);u=AA(QQ(2)/3)
y=(r*u+c-t-1)/(c+t);v=u+r*c*(1-y);H=2*u
P=[vector(AA,[0,0])]
for ell,d in zip([x,u,v,y,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vector(AA,d))
assert P[-1]==P[0];P.pop()
Q=[vector(AA,[0,0])]
for ell,d in zip([H,u,1,v]*2,[(c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r)]):Q.append(Q[-1]+ell*vector(AA,d))
assert Q[-1]==Q[0];Q.pop()
check(P);check(Q)
Pl=[(P[(i+1)%5]-P[i]).norm() for i in range(5)]
Ql=[(Q[(i+1)%8]-Q[i]).norm() for i in range(8)]
assert Pl==[x,u,v,y,w] and Ql==[H,u,1,v]*2
assert all(z>0 for z in Pl+Ql) and len(set(Pl))==4 and H not in Pl
assert all(z!=2*v for z in Ql) and [i for i,z in enumerate(Ql) if z==2*u]==[0,4]
assert y not in Ql
centre=(Q[0]+Q[4])/2
assert all(Q[i]+Q[i+4]==2*centre for i in range(4))
for F,angles in[(P,[5,5,4,5,5]),(Q,[5,7,6,6,5,7,6,6])]:
 for i,b in enumerate(F):
  A=F[i-1]-b;B=F[(i+1)%len(F)]-b;dot=A.dot_product(B)
  n=angles[i]
  if n==4:assert dot==0
  else:
   assert dot<0
   assert dot**2=={5:(2-r)/4,6:AA(QQ(1)/2),7:(2+r)/4}[n]*A.dot_product(A)*B.dot_product(B)
# Minimal cap on firstH: twoP90 at its midpoint,alongu/perpv whole.
M=(Q[0]+Q[1])/2
Aopts=[T for T in placements(P,Q[0],M) if T[2]==M]
Bopts=[T for T in placements(P,M,Q[1]) if T[2]==M]
assert len(Aopts)==len(Bopts)==1
cap=[Q,Aopts[0],Bopts[0]]
for i,F in enumerate(cap):
 for G in cap[i+1:]:
  I=intersect(F,G);assert not I or area(I)==0
assert Aopts[0][3]==Bopts[0][3]
far=Aopts[0][3]
assert (Aopts[0][4]-far).norm()==y==(Bopts[0][4]-far).norm()
print("PASS: positive minimal QHhost/twoP cap; far twoP112 force absentQ135 pair(y,y), so cap cannot extend")
# Source ring after cap obstruction restoresH QQ. Forced whole public acute
# guests and all native1 guest alternatives are enumerated exactly.
private={0,4};opts={}
for i in[1,3,5,7]:
 acute=Q[i] if i in[1,5] else Q[(i+1)%8]
 O=[T for T in placements(P,Q[i],Q[(i+1)%8]) if T[2]==acute]
 assert len(O)==1;opts[i]=O
for i in[2,6]:opts[i]=placements(P,Q[i],Q[(i+1)%8]);assert len(opts[i])==4
Q0h=[Q[0]+Q[1]-p for p in Q];Q4h=[Q[4]+Q[5]-p for p in Q]
def exposed(T,at,A,B):
 j=T.index(at);return next(z for z in[T[j-1],T[(j+1)%5]] if z not in[A,B])
survivors=[]
for choices in product(range(4),repeat=2):
 guests={i:opts[i][choices[0] if i==2 else choices[1] if i==6 else 0] for i in[1,2,3,5,6,7]}
 if not all(exposed(guests[i],Q[i+1],Q[i],Q[i+1])==exposed(guests[i+1],Q[i+1],Q[i+1],Q[(i+2)%8]) for i in[1,2,5,6]):continue
 tiles=[Q,Q0h,Q4h]+list(guests.values())
 if any((I:=intersect(F,G)) and area(I)>0 for j,F in enumerate(tiles) for G in tiles[j+1:]):continue
 survivors.append((choices,guests))
 print("whole source ring survivor",choices)
assert len(survivors)==1
print("PASS: complete4^2 first ring domain has one disjoint matching whole-contact ring")
print("P lengths",Pl,"Q lengths",Ql,"Parea",area(P),"Qarea",area(Q))

# Explicit periodic carrier after cap branch falsification. No period search
# is performed here: three reps and nine fixed oriented-edge pairings.
Fp=[p+Q[3]-P[4] for p in P]
Fm=[-p+Q[7]+P[4] for p in P]
assert canonical(Fp)==canonical(survivors[0][1][2])
assert canonical(Fm)==canonical(survivors[0][1][6])
L=Q[1]-Q[4];U=Q[1]-Q[7]+P[2]-P[4]
reps=[Q,Fp,Fm]
pairs=[((0,0),(0,4),(1,0)),((0,1),(2,1),(0,1)),((0,2),(1,4),(0,0)),((0,3),(2,2),(-1,1)),((0,5),(1,1),(0,-1)),((0,6),(2,4),(0,0)),((0,7),(1,2),(1,-1)),((1,0),(2,0),(0,1)),((1,3),(2,3),(-1,1))]
seen=[]
for(f,i),(g,j),(m,n) in pairs:
 seen.extend([(f,i),(g,j)]);shift=m*L+n*U
 assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
 assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
assert len(set(seen))==18 and set(seen)=={(f,i) for f,F in enumerate(reps) for i in range(len(F))}
assert cross(L,U)>0 and sum(area(F) for F in reps)==cross(L,U)
print("PASS: explicit1Q/2P periodic carrier,9 reversed pairs/18 native edges/36 coordinate identities, positive covolume=area")
