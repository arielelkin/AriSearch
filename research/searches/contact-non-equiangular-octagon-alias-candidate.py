"""One exact changed alias candidate, support pivotcos22.5. No metric sweep.
Complete single-Q native ring domain with privateH dimer and u/vP guests.
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


r=AA(2).sqrt();c=((2+r)/4).sqrt();t=((2-r)/4).sqrt();pivot=c
x=w=AA(1);u=c;v=1+t;y=r-1/(r*c)
assert all(z>0 for z in[x,u,v,y,w])
assert len(set([x,u,v,y,w]))==4
P=[vector(AA,[0,0])]
for ell,d in zip([x,u,v,y,w],[(c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1)]):P.append(P[-1]+ell*vector(AA,d))
assert P[-1]==P[0];P.pop()
k=r-1;q0x=k*pivot/(1+k);q1x=(1-k*pivot)/(1-k)
Q=[vector(AA,[q0x,-q0x]),vector(AA,[q1x,q1x-1]),vector(AA,[1+r/2,r/2]),vector(AA,[1+r/2,1+r/2]),vector(AA,[1,1+r]),vector(AA,[0,1+r]),vector(AA,[-r/2,1+r/2]),vector(AA,[-r/2,r/2])]
check(P);check(Q)
Pl=[(P[(i+1)%5]-P[i]).norm() for i in range(5)]
Ql=[(Q[(i+1)%8]-Q[i]).norm() for i in range(8)]
assert Pl==[x,u,v,y,w]
H=2*c-1;assert Ql==[H,u]+[AA(1)]*5+[v]
assert H not in Pl
assert all(ell not in[2*u,2*v] for ell in Pl+Ql)
Qh=[Q[0]+Q[1]-z for z in Q]
Uopts=[T for T in placements(P,Q[1],Q[2]) if T[2]==Q[1]]
Vopts=[T for T in placements(P,Q[7],Q[0]) if T[2]==Q[0]]
assert len(Uopts)==len(Vopts)==1
Pu,Pv=Uopts[0],Vopts[0]
assert Pu[3] in Qh and Pv[1] in Qh
options={i:placements(P,Q[i],Q[i+1]) for i in range(2,7)}
assert all(len(V)==4 for V in options.values())
# Every consecutive Pguest at a native Q135 vertex must have a whole
# opposite PPside. Identify the two exposed sides at that actual vertex.
def exposed(T,at,centralA,centralB):
 j=T.index(at)
 nbrs=[T[(j-1)%5],T[(j+1)%5]]
 return next(b for b in nbrs if b not in[centralA,centralB])
def compatible(L,R,at,Ledge,Redge):
 return exposed(L,at,*Ledge)==exposed(R,at,*Redge)
def disjoint(tiles):
 for i,F in enumerate(tiles):
  for G in tiles[i+1:]:
   I=intersect(F,G)
   if I and area(I)>0:return False
 return True
survivors=[]
for choices in product(range(4),repeat=5):
 guests=[Pu]+[options[i][j] for i,j in zip(range(2,7),choices)]+[Pv]
 if not all(compatible(guests[i-1],guests[i],Q[i+1],(Q[i],Q[i+1]),(Q[i+1],Q[(i+2)%8])) for i in range(1,7)):continue
 tiles=[Q,Qh]+guests
 if not disjoint(tiles):continue
 word=''.join('X' if any((T[(j+1)%5]-T[j]).norm()==x and j==0 and {tuple(T[j]),tuple(T[(j+1)%5])}=={tuple(Q[i]),tuple(Q[i+1])} for j in range(5)) else'W' for i,T in zip(range(2,7),guests[1:-1]))
 survivors.append((choices,word))
 print("surviving ring",choices,word)
assert len(survivors)==4
print("PASS: positive exact alias shapes,Hprivate,whole dimer+acute guests, complete4^5 ring domain and4 disjoint matching survivors")
print("Parea",area(P),"Qarea",area(Q),"lengths",Pl,Ql)

# Each four-tile local ring has an unavoidable second-layer far-end witness.
# At the far endpoint of a shared PPedge, twoP112 can only meet Q135.
# Whole Qcontacts then require its two native incident lengths to equal the
# two as-yet-unmatched Pedge lengths; enumerate the SIX actual Q135 slots.
q135pairs=[sorted([Ql[i-1],Ql[i]]) for i in range(2,8)]
for choices,word in survivors:
 guests=[Pu]+[options[i][j] for i,j in zip(range(2,7),choices)]+[Pv]
 witnesses=[]
 for i in range(1,7):
  L,R=guests[i-1],guests[i];at=Q[i+1]
  far=exposed(L,at,Q[i],Q[i+1])
  assert far==exposed(R,at,Q[i+1],Q[(i+2)%8])
  li=L.index(far);ri=R.index(far)
  if li==2 or ri==2:continue
  le=next(b for b in[L[(li-1)%5],L[(li+1)%5]] if b!=at)
  re=next(b for b in[R[(ri-1)%5],R[(ri+1)%5]] if b!=at)
  need=sorted([(le-far).norm(),(re-far).norm()])
  if need not in q135pairs:witnesses.append((i,need))
 assert witnesses
 print("second-layer obstruction",word,[(i,[('u' if a==u else'v' if a==v else'y' if a==y else'1') for a in need]) for i,need in witnesses])
print("PASS: every first-ring survivor has a forced P112/P112 far endpoint requiring a nonexistent Q135 native side pair")
