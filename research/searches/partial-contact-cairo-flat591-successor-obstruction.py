"""Exact raw supporting witness for the flat591 successor obstruction."""
from sage.all import QuadraticField,vector,matrix,PolynomialRing
K=QuadraticField(3,"w");w=K.gen();R=PolynomialRing(K,"u");u=R.gen();V=lambda x,y:vector(R,(x,y));sample=K(2)/5
P=(1,u,(-3*w/2-K(7)/2)*u+3*w/2+K(3)/2,(3*w/2+K(3)/2)*u-w/2-K(1)/2,(-2*w-3)*u+w+2)
Q=((-w-K(3)/2)*u+w/2+1,(-w/2-1)*u+w+K(1)/2,(-2*w-4)*u+w+2,1,P[4])
def raw(W):
 a,b,c,d,e=W
 assert b-c==w*(d-a) and e==w*c+d-2*a
 return[V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
q=raw(Q);A,B,C,s,f=Q;F90=matrix(R,[[-1,0],[0,1]]);mirror=[V(2*A,0)+F90*z for z in q]
R30=matrix(R,[[w/2,-K(1)/2],[K(1)/2,w/2]]);fill=[q[2]+R30*z for z in q]
R60=matrix(R,[[K(1)/2,-w/2],[w/2,K(1)/2]]);pforced=[q[4]+R60*z for z in raw(P)]
F30=matrix(R,[[K(1)/2,w/2],[w/2,-K(1)/2]]);F300=-F30;center=pforced[3]
pcore=[[center+M*(z-center) for z in pforced] for M in(matrix.identity(R,2),F30,F300,-matrix.identity(R,2))]
fillmate=[fill[1]+F300*(z-fill[1]) for z in fill]
rightcore=[[V(2*A,0)+F90*z for z in p] for p in pcore]

O=pforced[3];O1=q[2]+R30*O
W=V((2*w+K(22)/5)*u-3*w/2-K(59)/30,3*(w+1)*(1-u)/4)
second=[q[2]+R30*z for z in pcore[2]]
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
lo=K(1)/3;hi=K(1)/2
for name,L in(("original",pforced),("successor",second)):
 area=sum(cross(L[i],L[(i+1)%5]) for i in range(5));orientation=1 if area(sample)>0 else-1
 for i in range(5):
  det=orientation*cross(L[(i+1)%5]-L[i],W-L[i])
  roots=det.roots();assert sum(m for z,m in roots)==det.degree()
  assert det(sample)>0 and not any(lo<z<hi for z,m in roots)
  print(name,i,det.factor())
# Distinct intrinsic private-corner centers make the two original tiles distinct.
vertical=(O1-O)[1];assert vertical(sample)>0
assert not any(lo<z<hi for z,m in vertical.roots())
# Every native side remains positive and the only undeclared arm roots in
# the positive interval are exactly the two removed privacy points.
for L in(P,Q):
 for f0 in L:
  f0=R(f0);assert f0(sample)>0 and not any(lo<z<hi for z,m in f0.roots())
arms=list(P[:4])+list(Q[:4]);privacy=set()
from itertools import combinations
for i,j in combinations(range(8),2):
 if(i,j)==(0,7):assert arms[i]==arms[j];continue
 delta=R(arms[i]-arms[j]);assert delta!=0
 privacy.update(z for z,m in delta.roots() if lo<z<hi)
assert privacy=={(4+w)/13,(w-1)/2}
print("PASS: full normalized interval strict original-tile overlap, distinct centers, positivity and exact privacy exclusions")
