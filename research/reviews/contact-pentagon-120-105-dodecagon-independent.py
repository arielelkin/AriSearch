"""Independent native-direction reconstruction of the full positive Q12 family."""
from sage.all import QQ,AA,PolynomialRing,NumberField,vector,matrix
Z=PolynomialRing(QQ,"z");z=Z.gen()
K=NumberField(z**4-4*z**2+1,"h",embedding=(AA(2)-AA(3).sqrt()).sqrt())
h=K.gen();s=2-h*h;assert AA(h)>0 and AA(h)<1 and s*s==3 and AA(s)>0
T=PolynomialRing(K,"w");w=T.gen();F=T.fraction_field()
V=lambda p,q:vector(F,[p,q])
x=(w+h)/s;R=1/h;d=2*R+w
# Rebuild P from its native lengths and prescribed edge directions.
P=[V(0,0),V(x/2,-s*x/2),V(x/2+1/(2*h),-s*x/2+h/2),
   V(x/2+1/(2*h),-s*x/2+h/2+w),V(x/2,s*x/2)]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def area(H):return sum(cross(p,H[(i+1)%len(H)]) for i,p in enumerate(H))/2
def positive(p):
 p=T(p);assert p and all(AA(a)>=0 for a in p.list()) and any(AA(a)>0 for a in p.list())
lengths=[x,1,w,1,x];cosines=[-K(1)/2,-h/2,-h/2,-h/2,-h/2]
for i,p in enumerate(P):
 e=P[(i+1)%5]-p;f=P[(i-1)%5]-p
 assert e.dot_product(e)==lengths[i]**2
 assert e.dot_product(f)==cosines[i]*lengths[i]*lengths[i-1]
 positive(-e.dot_product(f))
 for j,q in enumerate(P):
  if j not in(i,(i+1)%5):positive(cross(e,q-p))
# Independent regular-Q coordinates and alignment of the native P.
Q=[V(R,0),V(s*R/2,R/2),V(R/2,s*R/2),V(0,R),
   V(-R/2,s*R/2),V(-s*R/2,R/2),V(-R,0),V(-s*R/2,-R/2),
   V(-R/2,-s*R/2),V(0,-R),V(R/2,-s*R/2),V(s*R/2,-R/2)]
for i,p in enumerate(Q):assert (Q[(i+1)%12]-p).dot_product(Q[(i+1)%12]-p)==1
J=matrix(F,[[0,1],[-1,0]]);center=V(d/2,d/(2*s))
Pstar=[J*p+center for p in P]
assert Pstar[1]==Q[1] and Pstar[2]==Q[0]
assert Pstar[3]==Q[6]+V(d,0) and Pstar[4]==Q[5]+V(d,0)
C=matrix(F,[[K(1)/2,-s/2],[s/2,K(1)/2]])
assert C.transpose()*C==matrix.identity(F,2) and C**6==matrix.identity(F,2)
reps=[Q]+[[C**i*p for p in Pstar] for i in range(6)]
a=V(d,0);b=V(d/2,s*d/2);L=matrix(F,[[a[0],b[0]],[a[1],b[1]]])
positive(L.det());assert sum(area(H) for H in reps)==L.det()
segments={(k,i):(p,H[(i+1)%len(H)]) for k,H in enumerate(reps) for i,p in enumerate(H)}
partners={}
for name,(p,q) in segments.items():
 matches=[]
 for other,(u,v) in segments.items():
  if p-v!=q-u:continue
  mn=L.inverse()*(p-v)
  if all(z in QQ and QQ(z).denominator()==1 for z in mn):matches.append((other,tuple(int(z) for z in mn)))
 assert len(matches)==1,(name,matches)
 partners[name]=matches[0]
assert len(partners)==42
for name,(other,shift) in partners.items():assert partners[other]==(name,tuple(-z for z in shift))
print("PASS: alternate quartic embedding, native-direction P reconstruction, full w>0 support signs/lengths/angles, independently regenerated42integral partners,6P1Q area=covolume")
