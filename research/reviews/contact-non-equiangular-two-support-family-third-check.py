"""Third exact-family checker: explicit coordinates and unrestricted lattice solve."""
from sage.all import QQ,PolynomialRing,NumberField,AA,vector,matrix
Z=PolynomialRing(QQ,"z");z=Z.gen();K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt());c=K.gen();r=4*c*c-2;t=r/(4*c)
R=PolynomialRing(K,"x,y,u,H");x,y,u,H=R.gens();F=R.fraction_field();v=u+r*c*(x-y);w=(u+v)/r-t*(x+y)
V=lambda a,b:vector(F,[a,b])
P=[V(0,0),V(c*x,-t*x),V(c*x+u/r,-t*x+u/r),V(c*y,w+t*y),V(0,w)]
Q=[V(0,0),V(H*c,H*t),V(H*c+u/r,H*t+u/r),V(H*c+u/r,H*t+u/r+w),V(H*c+(u-v)/r,H*t+(u+v)/r+w),V((u-v)/r,(u+v)/r+w),V(-v/r,v/r+w),V(-v/r,v/r)]
edges=lambda A:list(zip(A,A[1:]+A[:1]))
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
area=lambda A:sum(cross(a,b) for a,b in edges(A))/2
for poly,lengths,coss in((P,[x,u,v,y,w],[-t,-t,0,-t,-t]),(Q,[H,u,w,v]*2,[-t,-c,-1/r,-1/r]*2)):
 for i,(a,b) in enumerate(edges(poly)):
  assert (b-a).dot_product(b-a)==lengths[i]**2
  assert (poly[i-1]-a).dot_product(b-a)==coss[i]*lengths[i-1]*lengths[i]
assert all(Q[i]+Q[i+4]==Q[4] for i in range(4))
reps=[Q,[p+Q[3]-P[4] for p in P],[-p+Q[7]+P[4] for p in P]]
L=V((v-u)/r,-(u+v)/r-w)
U=V(c*(H+x)+(u+v)/r,t*(H-x)+(u-v)/r-w)
assert L==Q[1]-Q[4] and U==Q[1]-Q[7]+P[2]-P[4]
B=matrix(F,[[L[0],U[0]],[L[1],U[1]]]);assert B.det()==area(Q)+2*area(P)
assert all(area(rep)==area(P) for rep in reps[1:])
segments={(f,i):(a,b) for f,A in enumerate(reps) for i,(a,b) in enumerate(edges(A))}
partners={}
for key,(a,b) in segments.items():
 matches=[]
 for other,(p,q) in segments.items():
  shift=a-q
  if b-p!=shift:continue
  coeff=B.inverse()*shift
  if all(z in QQ and z.denominator()==1 for z in coeff):matches.append((other,tuple(coeff)))
 assert len(matches)==1,(key,matches)
 partners[key]=matches[0]
for key,(other,shift) in partners.items():assert partners[other]==(key,tuple(-z for z in shift))
assert len(partners)==18
print("PASS: third explicit-coordinate4parameter family, signed native angles/lengths,18 unrestricted lattice edgepartners/36 identities, exact area=covolume")
