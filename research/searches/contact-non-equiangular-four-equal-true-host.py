"""One four-equalP true-Q-host fixture; exact cap and farQ extension.
No parameter sampling, no plane inference from a finite patch.
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
x=y=u=v=AA(1);w=r-2*t;H=AA(2)
P=[vector(AA,[0,0])]
for ell,d in zip([1,1,1,1,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vector(AA,d))
assert P[-1]==P[0];P.pop()
Q=[vector(AA,[0,0])]
for ell,d in zip([H,1,1,1]*2,[(c,t),(1/r,1/r),(0,1),(-1/r,1/r),(-c,-t),(-1/r,-1/r),(0,-1),(1/r,-1/r)]):Q.append(Q[-1]+ell*vector(AA,d))
assert Q[-1]==Q[0];Q.pop();check(P);check(Q)
assert 0<w<1
Pl=[(P[(i+1)%5]-P[i]).norm() for i in range(5)]
Ql=[(Q[(i+1)%8]-Q[i]).norm() for i in range(8)]
assert Pl==[1,1,1,1,w] and Ql==[2,1,1,1]*2
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
labels=["P90","P112","Q112","Q135","Q157"]
units=[4,5,5,6,7];weights=[4,1,1,-2,-5]
stars={}
for total in[16,8]:
 stars[total]=[C for C in product(range(5),repeat=5) if sum(n*a for n,a in zip(units,C))==total]
 assert all(sum(n*a for n,a in zip(weights,C))>=0 for C in stars[total])
 print("full" if total==16 else"flat",[(dict((s,n) for s,n in zip(labels,C) if n),sum(n*a for n,a in zip(weights,C))) for C in stars[total]])
assert stars[8]==[(2,0,0,0,0)]
M=(Q[0]+Q[1])/2
Aopts=[T for T in placements(P,Q[0],M) if T[2]==M]
Bopts=[T for T in placements(P,M,Q[1]) if T[2]==M]
assert len(Aopts)==len(Bopts)==1
Pa,Pb=Aopts[0],Bopts[0]
def acute_other(T,hostend):
 return next(z for z in[T[1],T[3]] if z!=hostend)
far=acute_other(Pa,Q[0]);assert far==acute_other(Pb,Q[1])
la=Pa.index(far);lb=Pb.index(far)
assert la in[1,3] and lb in[1,3]
sa=next(z for z in[Pa[la-1],Pa[(la+1)%5]] if z!=M)
sb=next(z for z in[Pb[lb-1],Pb[(lb+1)%5]] if z!=M)
assert (sa-far).norm()==1==(sb-far).norm()
# Match complete nativeQ135 angle and BOTH outgoing unit edges.
faroptions=[]
for T in placements(Q,far,sa)+placements(Q,sa,far):
 if far not in T or sb not in T:continue
 j=T.index(far)
 if j not in[2,3,6,7]:continue
 if {tuple(T[j-1]),tuple(T[(j+1)%8])}!={tuple(sa),tuple(sb)}:continue
 if canonical(T) not in[canonical(F) for F in faroptions]:faroptions.append(T)
assert len(faroptions)==4
for F in faroptions:
 patch=[Q,Pa,Pb,F]
 for i,A in enumerate(patch):
  for B in patch[i+1:]:
   I=intersect(A,B);assert not I or area(I)==0
print("PASS: exact positive trueQH cap and FOUR disjoint farQ135 extensions; missing-side-pair shortcut genuinely escaped")
print("P lengths",Pl,"Q lengths",Ql,"Parea",area(P),"Qarea",area(Q))
