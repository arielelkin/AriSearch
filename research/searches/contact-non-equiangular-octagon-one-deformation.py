"""One exact changed non-equiangular Q8 fixture; no parameter sweep.
Q support edge rotated22.5 about(1/3,0). Positive dimer patch and exact
native corner stars, including flat host sectors, independently enumerated.
"""
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
pivot=QQ(1)/3
u=AA(QQ(1)/3);v=(2+r)/3;x=AA(1)
y=x-(v-u)/(r*c);w=(u+v)/r-t*(x+y)
assert all(z>0 for z in[x,u,v,y,w])
P=[vector(AA,[0,0])]
for ell,d in zip([x,u,v,y,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vector(AA,d))
assert P[-1]==P[0];P.pop()
k=r-1
q0x=k*pivot/(1+k);q1x=(1-k*pivot)/(1-k)
Q=[vector(AA,[q0x,-q0x]),vector(AA,[q1x,q1x-1]),vector(AA,[1+r/2,r/2]),vector(AA,[1+r/2,1+r/2]),vector(AA,[1,1+r]),vector(AA,[0,1+r]),vector(AA,[-r/2,1+r/2]),vector(AA,[-r/2,r/2])]
check(P);check(Q)
Pl=[(P[(i+1)%5]-P[i]).norm() for i in range(5)]
Ql=[(Q[(i+1)%8]-Q[i]).norm() for i in range(8)]
assert Pl==[x,u,v,y,w]
assert Ql[1:7]==[u]+[AA(1)]*5 and Ql[7]==v
H=Ql[0];assert H not in Pl
assert all(a!=b for i,a in enumerate(Pl) for b in Pl[i+1:])
assert all(ell not in[2*u,2*v] for ell in Pl+Ql)
# Exact native angle cosine-square identities, with signs fixing obtuse angles.
for F,angles in[(P,[5,5,4,5,5]),(Q,[5,7,6,6,6,6,6,6])]:
 for i,b in enumerate(F):
  A=F[i-1]-b;B=F[(i+1)%len(F)]-b;dot=A.dot_product(B)
  n=angles[i]
  if n==4:assert dot==0
  else:
   assert dot<0
   target={5:(2-r)/4,6:AA(QQ(1)/2),7:(2+r)/4}[n]
   assert dot**2==target*A.dot_product(A)*B.dot_product(B)
# The angle-domain enumeration is finite/completely specified: total16units
# for full stars or8units for one180 host, units=22.5degrees.
labels=["P90","P112","Q112","Q135","Q157"]
units=[4,5,5,6,7]
stars={}
for total in[16,8]:
 stars[total]=[counts for counts in product(range(5),repeat=5) if sum(n*a for n,a in zip(units,counts))==total]
 print("full" if total==16 else"flat",[dict((s,n) for s,n in zip(labels,C) if n) for C in stars[total]])
assert stars[8]==[(2,0,0,0,0)]
# An exact positive patch: two Q joined at the unique H side and P90 fills
# each endpoint. The native u/v contacts are whole and both Pcopies fit.
Qh=[Q[0]+Q[1]-z for z in Q]
Ua=[T for T in placements(P,Q[1],Q[2]) if T[2]==Q[1]]
Va=[T for T in placements(P,Q[7],Q[0]) if T[2]==Q[0]]
assert len(Ua)==len(Va)==1
patch=[Q,Qh,Ua[0],Va[0]]
for i,F in enumerate(patch):
 for G in patch[i+1:]:
  I=intersect(F,G)
  assert not I or area(I)==0
assert Ua[0][3] in Qh and Va[0][1] in Qh
print("PASS: positive genuine P/Q;exact new angle word;one private H;all native sides nondoubled;exact dimer+twoP patch disjoint")
print("P lengths",Pl,"Q lengths",Ql)
