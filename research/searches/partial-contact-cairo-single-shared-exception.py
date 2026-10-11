"""Exact fixture for a one-shared-arm exceptional Cairo family."""
from itertools import combinations_with_replacement
from sage.all import QuadraticField,vector
K=QuadraticField(3,"w");w=K.gen();r=K(4)/5;t=2-r
P=(K(1),r,(3*w-r)/2,(w*r-1)/2,K(2))
Q=((w*t-1)/2,(3*w-t)/2,t,K(1),K(2))
V=lambda x,y:vector(K,(x,y))
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
for L in (P,Q):
 a,b,c,d,e=L
 assert all(x>0 for x in L)
 assert b-c==w*(d-a) and e==w*c+d-2*a
 X=[V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
 for i in range(5):
  E=X[(i+1)%5]-X[i]
  assert E.dot_product(E)==L[i]**2
  for j in range(5):
   if j not in (i,(i+1)%5):assert cross(E,X[j]-X[i])>0
 assert len(set(L[:4]))==4
matches={(i,j) for i in range(4) for j in range(4) if P[i]==Q[j]}
assert matches=={(0,3)}
slots=[(L[i],L[(1,0,3,2)[i]],species,i) for species,L in enumerate((P,Q)) for i in range(4)]
events=[(u,x,y,sp,i,sq,j) for(u,x,sp,i),(v,y,sq,j) in combinations_with_replacement(slots,2) if u==v]
assert len(events)==9
assert any(x==r and y==t for u,x,y,sp,i,sq,j in events)
assert sum(x+y==2 for u,x,y,sp,i,sq,j in events)==3
assert P[4]==Q[4]==r+t==2
assert sorted(P)!=sorted(Q)
private_totals={2*P[1],2*P[2],2*P[3],2*Q[0],2*Q[1],2*Q[2]}
assert len(private_totals)==6 and 2 not in private_totals
assert r<1<r+t and 1<t<2 and r<t
# Direct native-vertex cluster identities, with no author artifact imports.
def vertices(L):
 a,b,c,d,e=L
 return [V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
XP=vertices(P);XQ=vertices(Q)
u=V(K(1)/2,w/2);v=V(-w/2,K(1)/2)
pquad=[V(-u.dot_product(XP[i]-XP[3]),-v.dot_product(XP[i]-XP[3])) for i in (3,4,0,1,2)]
qquad=[V(-(XQ[i]-XQ[1])[0],(XQ[i]-XQ[1])[1]) for i in (1,0,4,3,2)]
def expected(z):
 d=(w*z-1)/2;c=(3*w-z)/2
 return [V(0,0),V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c)]
assert pquad==expected(r) and qquad==expected(t)
assert all(X[0]>=0 and X[1]>=0 for X in pquad+qquad)
print("PASS: convex one-shared-arm P/Q;9 events and singleton private totals; strict switches; exact S(r)/S(2-r) native quadrant geometry")
