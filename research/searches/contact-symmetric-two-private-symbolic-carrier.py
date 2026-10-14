"""Symbolic all-positive symmetric distance3 periodic carrier; no sweep."""
from sage.all import QuadraticField, AA, PolynomialRing, vector, matrix, QQ
K=QuadraticField(2,"r",embedding=AA(2).sqrt());r=K.gen()
R=PolynomialRing(K,"a,w");a,w=R.gens()
def vec(x,y):return vector(R,[x,y])
def cross(v,w):return v[0]*w[1]-v[1]*w[0]
def area(F):return sum(cross(p,q) for p,q in zip(F,F[1:]+F[:1]))/2
bx=((2+r)*a-(1+r)*w)/2
P=[vec(0,-w),vec(bx,-w/2-a/r),vec(bx+a/r,-w/2),vec(bx,-w/2+a/r),vec(0,0)]
H=(1+r)*w-r*a
Q=[vec(0,0)]
dirs=[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]
for ell,d in zip([H,a,a,H,a,w,w,a],dirs):Q.append(Q[-1]+ell*vec(*d))
assert Q[-1]==Q[0];Q.pop()
Rm=matrix(R,[[1/r,1/r],[-1/r,1/r]])
Rp=matrix(R,[[-1/r,-1/r],[1/r,-1/r]])
assert Rm.transpose()*Rm==matrix.identity(R,2) and Rp.transpose()*Rp==matrix.identity(R,2)
reps=[Q,[Q[0]+Q[1]-p for p in Q],[Q[1]-(p-P[2]) for p in P],[Q[3]+Rp*(p-P[2]) for p in P],[Q[4]+Rm*(p-P[2]) for p in P],[p-P[2] for p in P]]
V=Q[3]+Q[4]-Q[1]
U=Q[5]-reps[3][0]
pairs=[((0, 0), (1, 0), (0, 0)), ((0, 1), (2, 1), (0, 0)), ((0, 2), (3, 2), (0, 0)), ((0, 3), (1, 3), (1, 0)), ((0, 4), (4, 1), (0, 0)), ((0, 5), (3, 4), (0, 1)), ((0, 6), (2, 4), (0, 1)), ((0, 7), (5, 2), (0, 0)), ((1, 1), (5, 1), (0, 0)), ((1, 2), (4, 2), (-1, 0)), ((1, 4), (3, 1), (-1, 0)), ((1, 5), (4, 4), (-1, -1)), ((1, 6), (5, 4), (0, -1)), ((1, 7), (2, 2), (0, 0)), ((2, 0), (3, 3), (0, 0)), ((2, 3), (5, 3), (0, -1)), ((3, 0), (4, 0), (0, -1)), ((4, 3), (5, 0), (1, 0))]
# Exact native-angle and side-length identities, independent of parameter values.
for F,target in[(P,"P"),(Q,"Q")]:
 for i,p in enumerate(F):
  e=F[i-1]-p;f=F[(i+1)%len(F)]-p;dot=e.dot_product(f)
  if target=="P" and i==2:assert dot==0
  else:assert dot**2==((2-r)/4 if target=="P" else QQ(1)/2)*e.dot_product(e)*f.dot_product(f)
assert (P[2]-P[1]).dot_product(P[2]-P[1])==a**2
assert (P[3]-P[2]).dot_product(P[3]-P[2])==a**2
assert (P[4]-P[0]).dot_product(P[4]-P[0])==w**2
seen=[]
for(f,i),(g,j),(m,n) in pairs:
 seen.extend([(f,i),(g,j)]);shift=m*V+n*U
 assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
 assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
assert len(set(seen))==36 and set(seen)=={(f,i) for f,F in enumerate(reps) for i in range(len(F))}
assert sum(area(F) for F in reps)==cross(V,U)
print("PASS: symbolic18 reversed-edge pairs and72 endpoint identities, full edge coverage, exact rotations and area identity")
print("V",V,"U",U,"det",cross(V,U).factor(),"Parea",area(P).factor(),"Qarea",area(Q).factor())
