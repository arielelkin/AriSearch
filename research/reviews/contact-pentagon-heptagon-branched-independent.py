"""Independent quartic-field P5/Q7 carrier reconstruction, no author imports."""
from sage.all import QQ, AA, NumberField, PolynomialRing, vector, matrix
Z=PolynomialRing(QQ,"z"); z=Z.gen()
K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen(); r=4*c*c-2; t=r/(4*c); w=r-2*t; A=1+w/r
V=lambda x,y:vector(K,[x,y])
# Closed coordinates, reconstructed directly from the two shape definitions.
P=[V(0,0),V(c,-t),V(c+1/r,1/r-t),V(c,r-t),V(0,w)]
Q=[V(0,0),V(A,0),V(A+1/r,1/r),V(A+1/r,1+1/r),
   V(1+1/r,A+1/r),V(1/r,A+1/r),V(0,A)]
def edges(F):return list(zip(F,F[1:]+F[:1]))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in edges(F))/2
for F, lengths in [(P,[1,1,1,1,w]),(Q,[A,1,1,w,1,1,A])]:
 assert AA(area(F))>0
 for i,(a,b) in enumerate(edges(F)):
  assert (b-a).dot_product(b-a)==lengths[i]**2
  assert all(AA(cross(b-a,p-a))>0 for j,p in enumerate(F) if j not in(i,(i+1)%len(F)))
R=matrix(K,[[1/r,-1/r],[1/r,1/r]])
assert R.transpose()*R==matrix.identity(K,2) and R.det()==1
B=V(A,0); W=[R*(p-P[4])+Q[4] for p in P]
reps=[Q,[B-q for q in Q],W,[B-p for p in W]]
D=V(A,-A); U=Q[2]-B+W[2]
L=matrix(K,[[D[0],U[0]],[D[1],U[1]]]); assert AA(L.det())>0
assert L.det()==2*area(P)+2*area(Q)
segments={(f,i):(a,b) for f,F in enumerate(reps) for i,(a,b) in enumerate(edges(F))}
partners={}
for name,(a,b) in segments.items():
 matches=[]
 for other,(p,q) in segments.items():
  if a-q!=b-p:continue
  mn=L.inverse()*(a-q)
  if all(x in QQ and QQ(x).denominator()==1 for x in mn):
   matches.append((other,tuple(int(x) for x in mn)))
 assert len(matches)==1,(name,matches)
 partners[name]=matches[0]
assert len(partners)==24
for name,(other,shift) in partners.items():
 assert partners[other]==(name,tuple(-x for x in shift))
for f,F in enumerate(reps):
 assert area(F)==area(Q if f<2 else P)
assert {i for (f,i),((g,j),mn) in partners.items() if f==0 and g<2}=={0,1,5,6}
print("PASS: exact independent P5/Q7 closed coordinates; positive convexity and lengths; unrestricted lattice solve regenerates24partners/12pairs; QQmask0,1,5,6; positivecovolume=2P+2Qarea")

# Generic reconstruction uses closed coordinates and regenerates the pairing;
# no producer pair table, bounded lattice window or parameter samples.
T=PolynomialRing(K,["x","y","u","a"]); x,y,u,a=T.gens(); F=T.fraction_field()
v=u+r*c*(x-y); w=(u+v)/r-t*(x+y); A=v+w/r; B=u+w/r
V=lambda p,q:vector(F,[p,q])
P=[V(0,0),V(x*c,-x*t),V(x*c+u/r,u/r-x*t),V(y*c,w+y*t),V(0,w)]
Q=[V(0,0),V(A,0),V(A+a/r,a/r),V(A+a/r,u+a/r),
   V(v+a/r,B+a/r),V(a/r,B+a/r),V(0,B)]
R=matrix(F,[[1/r,-1/r],[1/r,1/r]])
W=[R*(p-P[4])+Q[4] for p in P]; center=V(A,0)
reps=[Q,[center-q for q in Q],W,[center-p for p in W]]
D=V(A,-B); U=Q[2]-center+W[2]
L=matrix(F,[[D[0],U[0]],[D[1],U[1]]]); assert L.det()!=0
assert L.det()==2*area(P)+2*area(Q)
segments={(f,i):(p,q) for f,H in enumerate(reps) for i,(p,q) in enumerate(edges(H))}
partners={}
for name,(p,q) in segments.items():
 matches=[]
 for other,(h,j) in segments.items():
  if p-j!=q-h:continue
  mn=L.inverse()*(p-j)
  if all(z in QQ and QQ(z).denominator()==1 for z in mn):
   matches.append((other,tuple(int(z) for z in mn)))
 assert len(matches)==1,(name,matches)
 partners[name]=matches[0]
assert len(partners)==24
for name,(other,shift) in partners.items():
 assert partners[other]==(name,tuple(-z for z in shift))
assert {i for (f,i),((g,j),mn) in partners.items() if f==0 and g<2}=={0,1,5,6}
print("PASS: independent full Q(c)(x,y,u,a) family; closed-coordinate reconstruction;24unrestricted integral partners; area polynomial identity; no pairing-table imports or metric samples")
