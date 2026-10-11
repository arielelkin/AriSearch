"""Symbolic exceptional-family privacy and forced reflected overlap."""
from itertools import combinations,product
from sage.all import QuadraticField,PolynomialRing,vector,matrix
K=QuadraticField(3,"w");w=K.gen();R=PolynomialRing(K,"r");r=R.gen();t=2-r
P=(R(1),r,(3*w-r)/2,(w*r-1)/2,R(2))
Q=((w*t-1)/2,(3*w-t)/2,t,R(1),R(2))
for a,b,c,d,e in (P,Q):assert b-c==w*(d-a) and e==w*c+d-2*a
lo=1/w;hi=2-1/w;r0=(2*w-1)/(w+2);r2=5/(w+2)
assert lo<r0<1<r2<hi and r0+r2==2
internal=[];cross=[]
for species,L in enumerate((P,Q)):
 for i,j in combinations(range(4),2):
  f=L[i]-L[j];assert f!=0 and f.degree()<=1
  if f.degree()==1:
   root=-f[0]/f[1]
   if lo<root<hi:internal.append((species,i,j,root))
assert {x[3] for x in internal}=={K(1)}
for i,j in product(range(4),repeat=2):
 f=P[i]-Q[j]
 if f==0:assert (i,j)==(0,3);continue
 assert f.degree()<=1
 if f.degree()==1:
  root=-f[0]/f[1]
  if lo<root<hi:cross.append((i,j,root))
assert {(i,j) for i,j,x in cross if x==r0}=={(1,0)}
assert {(i,j) for i,j,x in cross if x==r2}=={(3,2)}
assert {(i,j) for i,j,x in cross if x==1}=={(0,2),(1,2),(1,3),(2,1),(3,0)}
assert {x for i,j,x in cross}=={r0,K(1),r2}
Z=PolynomialRing(K,"z");z=Z.gen();V=lambda x,y:vector(Z,(x,y))
d=(w*z-1)/2;c=(3*w-z)/2
A=[V(0,0),V(d,0),V(d+1,-w),V(d+K(1)/2,-3*w/2),V(0,-c)]
X=V(-w*z/2,-3*w/2);F=matrix(Z,[[K(1)/2,w/2],[w/2,-K(1)/2]])
W=V(w*z/5+K(3)/10,7*z/10-7*w/5)
assert W==X+F*(W-X)
reflected_center=X-F*X
assert reflected_center==V((9-w*z)/4,(3*z-9*w)/4)
assert reflected_center==(3*w-z)*V(w/4,-K(3)/4)
assert hi<3*w
cross2=lambda a,b:a[0]*b[1]-a[1]*b[0]
dets=[cross2(A[(i+1)%5]-A[i],W-A[i]) for i in range(5)]
assert dets==[K(7)/20*(w*z-1)*(z-2*w),-(z+3*w)/5,(w-8*z)/10,-z*(2*w*z+3)/10,w*z**2/10-3*z/4-9*w/20]
assert 1<w<2 and lo==w/3 and hi<2<2*w
assert lo>w/8 and w*hi==2*w-1<3
print("PASS:12 internal/16 cross equality roots; exact3 exceptions; closure; universal reflection-fixed strict witness factorizations")
