"""Independent symbolic reconstruction and native-boundary pairing."""
from sage.all import QuadraticField,PolynomialRing,matrix,vector,QQ
K=QuadraticField(2,"r");r=K.gen()
R=PolynomialRing(K,"a,w");a,w=R.gens();F=R.fraction_field()
v=lambda x,y:vector(F,[x,y])
b=((2+r)*a-(1+r)*w)/2
P=[v(0,-w),v(b,-w/2-a/r),v(b+a/r,-w/2),v(b,-w/2+a/r),v(0,0)]
H=(1+r)*w-r*a
Q=[v(0,0)]
for length,direction in zip([H,a,a,H,a,w,w,a],[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]):Q.append(Q[-1]+length*v(*direction))
assert Q.pop()==Q[0]
minus=matrix(F,[[1/r,1/r],[-1/r,1/r]])
plus=matrix(F,[[-1/r,-1/r],[1/r,-1/r]])
assert minus.det()==plus.det()==1
reps=[Q,[Q[1]-p for p in Q],[Q[1]+P[2]-p for p in P],[Q[3]+plus*(p-P[2]) for p in P],[Q[4]+minus*(p-P[2]) for p in P],[p-P[2] for p in P]]
U=v(-(r/2+1)*a-(r/2+QQ(1)/2)*w,r*a/2+w/2)
V=v(a+r*w/2,(r+1)*a+(r/2+1)*w)
L=matrix(F,[[V[0],U[0]],[V[1],U[1]]]);assert L.det()==2*(1+r)*(a+r*w/2)**2
edges={(i,j):(p,q) for i,rep in enumerate(reps) for j,(p,q) in enumerate(zip(rep,rep[1:]+rep[:1]))}
partners={}
for name,(p,q) in edges.items():
 candidates=[]
 for other,(s,t) in edges.items():
  shift=p-t
  if q-s!=shift:continue
  coeff=L.inverse()*shift
  if all(z in QQ and z.denominator()==1 for z in coeff):candidates.append((other,tuple(coeff)))
 assert len(candidates)==1,(name,candidates)
 partners[name]=candidates[0]
for name,(other,shift) in partners.items():assert partners[other]==(name,tuple(-z for z in shift))
assert len(partners)==36
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
area=lambda rep:sum(cross(p,q) for p,q in zip(rep,rep[1:]+rep[:1]))/2
assert sum(area(rep) for rep in reps)==L.det()
print("PASS: independent symbolic reconstruction,36 uniquely paired native edges,72 endpoint identities, positive-domain determinant formula, area/covolume")
