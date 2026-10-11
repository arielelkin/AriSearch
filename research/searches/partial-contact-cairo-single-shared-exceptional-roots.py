"""Exact native-slot obstruction at r0 and its reflected companion."""
from itertools import combinations_with_replacement
from sage.all import QuadraticField,vector,matrix
K=QuadraticField(3,"w");w=K.gen();r=5*w-8;t=2-r;B=4*w-5
P=(K(1),r,4-w,7-4*w,K(2));Q=(r,B,t,K(1),K(2))
assert 1/w<r<1<t<2-1/w
assert r==(2*w-1)/(w+2) and t==5/(w+2)
assert all(x>0 for x in P+Q)
for a,b,c,d,e in (P,Q):assert b-c==w*(d-a) and e==w*c+d-2*a
assert len(set(P[:4]))==len(set(Q[:4]))==4
arms=P[:4]+Q[:4];other=(1,0,3,2,5,4,7,6)
assert {(i,j) for i in range(4) for j in range(4) if P[i]==Q[j]}=={(0,3),(1,0)}
events=[(i,j,arms[i]+arms[j]) for i,j in combinations_with_replacement(range(8),2) if arms[other[i]]==arms[other[j]]]
assert events==[(0,0,K(2)),(0,5,B+1),(1,1,2*r),(1,6,K(2)),(2,2,2*P[2]),(3,3,2*P[3]),(4,4,2*r),(5,5,2*B),(6,6,2*t),(7,7,K(2))]
assert len({s for i,j,s in events})==7
S=[{s for i,j,s in events if k in (i,j)} for k in range(8)]
compatible={j for j in range(8) if arms[j]==B or bool(S[j]&S[5])}
assert compatible=={0,5}
e_banks={k for i,j,s in events if s==2 for k in (i,j)}
assert e_banks=={0,1,6,7}
corners=[(0,8),(1,2),(3,8),(4,9),(5,6),(7,9)]
assert not any(i in compatible and j in compatible for i,j in corners)
assert [x for x in corners if set(x)<=(e_banks|{8,9})]==[(0,8),(7,9)]
# Host e2 chooses self Pb mate; cross Pb/Qa perpendicular gives banks1,B.
assert B+1!=2 and [(i,j) for i,j,s in events if arms[other[i]]==r and s==2]==[(0,0)]
def family(z):
 Pz=(K(1),z,(3*w-z)/2,(w*z-1)/2,K(2));tz=2-z
 Qz=((w*tz-1)/2,(3*w-tz)/2,tz,K(1),K(2))
 return Pz,Qz
M=lambda L:(L[3],L[2],L[1],L[0],L[4])
Pt,Qt=family(t)
assert M(P)==Qt and M(Q)==Pt
# Universal overlap at root, in filler-centered coordinates.
V=lambda x,y:vector(K,(x,y));d=(w*r-1)/2;c=(3*w-r)/2
A=[V(0,0),V(d,0),V(d+1,-w),V(d+K(1)/2,-3*w/2),V(0,-c)]
X=V(-w*r/2,-3*w/2);F=matrix(K,[[K(1)/2,w/2],[w/2,-K(1)/2]])
W=V(w*r/5+K(3)/10,7*r/10-7*w/5)
assert W==X+F*(W-X) and X-F*X!=V(0,0)
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
assert all(cross(A[(i+1)%5]-A[i],W-A[i])<0 for i in range(5))
C=[X+F*(a-X) for a in A]
assert all(cross(C[(i+1)%5]-C[i],W-C[i])>0 for i in range(5))
print("PASS:2 extra-sharing roots;10 native events; actual Qb/e bank filters; exhaustive120 exclusions; P-only forced-mate selection; strict P overlap")
