"""Exact full-interval geometry for the one-shared-arm forced-core obstruction."""
from sage.all import QuadraticField,PolynomialRing,vector,matrix
from itertools import combinations_with_replacement
K=QuadraticField(3,"w");w=K.gen()
R=PolynomialRing(K,names=("s","h","l"));s,h,l=R.gens();k=h-w*(l-s);g=w*k+l-2*s
V=lambda x,y:vector(R,(x,y))
raw=[V(0,0),V(s,0),V(s,h),V(s-w*k/2,h+k/2),V(-g/2,w*g/2)]
rot=matrix(R,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
quarter=[rot*(raw[i]-raw[3]) for i in(3,4,0,1,2)]
assert quarter==[V(0,0),V(l,0),V(l+g/2,w*g/2),V(l+(g-s)/2,w*(g+s)/2),V(0,k)]
# Cross-class privacy is symbolic and native slots remain separate.
labels=(0,1,2,3,4,5,6,0);other=(1,0,3,2,5,4,7,6)
events={(tuple(sorted((labels[i],labels[j])))) for i,j in combinations_with_replacement(range(8),2) if labels[other[i]]==labels[other[j]]}
assert events=={(0,0),(1,1),(6,6),(1,6),(2,2),(3,3),(4,4),(5,5)}
Z=PolynomialRing(K,"z");z=Z.gen();L=Z.fraction_field();z=L(z)
VV=lambda x,y:vector(L,(x,y))
d=(w*z-1)/2;c=(3*w-z)/2
assert z-c==w*(d-1) and w*c+d-2==2
A=[VV(0,0),VV(d,0),VV(d+1,-w),VV(d+K(1)/2,-3*w/2),VV(0,-c)]
X=VV(-w*z/2,-3*w/2);F=matrix(L,[[K(1)/2,w/2],[w/2,-K(1)/2]])
center=X-F*X
assert center==VV((9-w*z)/4,(3*z-9*w)/4)==(3*w-z)*VV(w/4,-K(3)/4)
lambda_=(9-w*z)/(w*z+7);W=lambda_*A[2]
assert W==X+F*(W-X)
assert -W[0]+w*W[1]==(w*z-9)/2
assert 1-lambda_==2*(w*z-1)/(w*z+7)
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
dets=[cross(A[(i+1)%5]-A[i],W-A[i]) for i in range(5)]
# Clear the positive denominator. Every remaining numerator is negative
# for 1<w*z<9, which is exactly 1/w<z<3w.
den=z+7*w/3
expected=[K(3)/2*(z-3*w)*(z-w/3)/den,
          -3*(z-w/3)**2/den,
          -K(3)/2*(z-w/3)*(z+w)/den,
          w/2*(z-3*w)*z*(z+w/3)/den,
          -w/4*(z+w/3)*(z-3*w)**2/den]
assert dets==expected,(dets,expected)
assert 1<w<2
print("PASS: raw general quadrant, all native event banks, closure, full positive interval reflection-fixed diagonal point and five strict determinants")
