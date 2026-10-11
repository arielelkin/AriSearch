"""Independent native events, general quadrant and full-interval fixed overlap.
No author imports. All signs use exact field/polynomial arithmetic.
"""
from sage.all import QuadraticField,PolynomialRing,matrix,vector,AA
from itertools import combinations_with_replacement
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,['a','b','d']);a,b,d=R.gens();c=b-w*(d-a);e=w*c+d-2*a
edges=[vector(R,(a,0)),vector(R,(0,b)),vector(R,(-w*c/2,c/2)),vector(R,(-d/2,-w*d/2)),vector(R,(e/2,-w*e/2))]
vertices=[];current=vector(R,(0,0))
for edge in edges:vertices.append(current);current+=edge
assert current==0
turn120=matrix(R,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
quarter=[turn120*(vertices[j]-vertices[3]) for j in [3,4,0,1,2]]
expected=[(0,0),(d,0),(d+e/2,w*e/2),(d+(e-a)/2,w*(e+a)/2),(0,c)]
assert quarter==list(map(lambda u:vector(R,u),expected))
assert quarter[3][0]==w*b/2
# Every native bank slot is retained. Equal bank values never replace complement slots.
classes=[0,1,2,3,4,5,6,0];perp=[1,0,3,2,5,4,7,6]
by_bank={i:set() for i in range(8)};events=[]
for i,j in combinations_with_replacement(range(8),2):
 if classes[perp[i]]==classes[perp[j]]:
  event=tuple(sorted((classes[i],classes[j])));events.append((i,j,event))
  by_bank[i].add(event);by_bank[j].add(event)
assert {v for i,j,v in events}=={(0,0),(1,1),(6,6),(1,6),(2,2),(3,3),(4,4),(5,5)}
for i in [2,3,4,5]:assert by_bank[i]=={(classes[i],classes[i])}
# Symbolic normalized e=2a curve is uniquely forced by closure.
Z=PolynomialRing(K,'z');z=Z.gen();F=Z.fraction_field();z=F(z)
d=(w*z-1)/2;c=(3*w-z)/2
assert z-c-w*(d-1)==0 and w*c+d-2==2
# Reconstruct all native edges before rotating into the clockwise lower quadrant.
u=[vector(F,(0,0)),vector(F,(1,0)),vector(F,(1,z)),vector(F,(1-w*c/2,z+c/2)),vector(F,(-1,w))]
rot=matrix(F,[[-K(1)/2,-w/2],[w/2,-K(1)/2]])
upper=[rot*(u[j]-u[3]) for j in [3,4,0,1,2]]
A=[vector(F,(v[0],-v[1])) for v in upper]
assert A==list(map(lambda v:vector(F,v),[(0,0),(d,0),(d+1,-w),(d+K(1)/2,-3*w/2),(0,-c)]))
# The actual lower-left unit90 breakpoint and its private perpendicular edge.
left=[vector(F,(-v[0],v[1])) for v in A]
X=left[3];perpendicular=left[4]-X
assert X==vector(F,(-w*z/2,-3*w/2))
assert perpendicular==vector(F,(w*z/2,z/2))
# Reflection across this edge; reconstruct affine matrix from its direction.
D=perpendicular;den=D.dot_product(D)
reflection=2*matrix(F,[[D[i]*D[j] for j in range(2)] for i in range(2)])/den-matrix.identity(F,2)
assert reflection==matrix(F,[[K(1)/2,w/2],[w/2,-K(1)/2]])
center=X-reflection*X
assert center==vector(F,((9-w*z)/4,(3*z-9*w)/4))
assert center==(3*w-z)*vector(F,(w/4,-K(3)/4))
# Derive the fixed diagonal point by solving the affine reflection equation.
lam=(9-w*z)/(w*z+7);W=lam*A[2]
assert reflection*(W-X)+X==W
assert 1-lam==2*(w*z-1)/(w*z+7)
# Independently isolate roots of every original-tile strict supporting inequality.
TAA=PolynomialRing(AA,'T');lower=AA(1/w);upper=AA(3*w);mid=(lower+upper)/2
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
def sign(f):
 f=F(f);np=TAA([AA(a) for a in f.numerator().list()]);dp=TAA([AA(a) for a in f.denominator().list()])
 assert np and dp
 assert not any(lower<r<upper for r,m in np.roots())
 assert not any(lower<r<upper for r,m in dp.roots())
 return np(mid)*dp(mid)>0
assert sign(lam) and sign(1-lam) and sign(d) and sign(c)
for i in range(5):
 det=cross(A[(i+1)%5]-A[i],W-A[i]);assert not sign(det) and det!=0
# Convexity of the actual clockwise constituent, checked without trusting factors.
for i in range(5):
 for j in range(5):
  if j not in (i,(i+1)%5):assert not sign(cross(A[(i+1)%5]-A[i],A[j]-A[i]))
assert sign(3*w-z) # Distinct reflected canonical center everywhere positive.
print('PASS independent general native quadrant and all36 native event pairs;private core banks singleton;normalized raw closure;actual T reflection axis;full-interval fixed strict overlap and distinct center.')
