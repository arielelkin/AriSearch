"""Independent raw symbolic Cairo motif audit, no author imports or proposal search."""
from sage.all import QuadraticField,AA,PolynomialRing,vector,matrix
from itertools import product,combinations
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen();R=PolynomialRing(K,'u');u=R.gen()
D=json.loads(Path('research/certificates/partial-contact-cairo-reversed-right-pair-boundary.json').read_text())
P=(R(1),u,(3*w-u)/2,(w*u-1)/2,R(2));Q=(u,R(1),(3*w*u-1)/2,(w-u)/2,2*u)
def V(x,y):return vector(R,(x,y))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def native(L):
 a,b,c,d,e=L
 assert b-c==w*(d-a) and e==w*c+d-2*a
 return [V(0,0),V(a,0),V(a,b),V(a-w*c/2,b+c/2),V(-e/2,w*e/2)]
def quadrant(L):
 a,b,c,d,e=L
 return [V(0,0),V(d,0),V(d+e/2,w*e/2),V(d+(e-a)/2,w*(e+a)/2),V(0,c)]
rotate120=matrix(R,[[-R(1)/2,-w/2],[w/2,-R(1)/2]])
AR=PolynomialRing(AA,'z');lo,hi=AA(1/w),AA(w)
def roots(poly):return [r for r,m in AR([AA(c) for c in poly.list()]).roots(AA)]
supports=[]
for L in(P,Q):
 N=native(L);quad=quadrant(L)
 assert quad==[rotate120*(N[i]-N[3]) for i in(3,4,0,1,2)]
 for j in range(5):
  edge=N[(j+1)%5]-N[j]
  assert edge.dot_product(edge)==L[j]**2
  direction=((1,0),(0,1),(-w/2,K(1)/2),(-K(1)/2,-w/2),(K(1)/2,-w/2))[j]
  assert edge==V(*(L[j]*a for a in direction))
  for k in range(5):
   if k in(j,(j+1)%5):continue
   det=cross(edge,N[k]-N[j]);assert det(K(4)/5)>0
   assert all(not lo<r<hi for r in roots(det));supports.append(det)
 for length in L:
  assert length(K(4)/5)>0 and all(not lo<r<hi for r in roots(length))
assert P[3](1/w)==0 and Q[3](w)==0
assert supports==[R(s) for s in D['strict_support_polynomials']] and len(supports)==30
# Check the arm-privacy statement throughout the full interval, including specialu1.
for L in(P,Q):
 for a,b in combinations(L[:4],2):
  diff=a-b;assert diff!=0
  assert all(not lo<r<hi or r==1 for r in roots(diff))
for a,b in product(range(4),repeat=2):
 diff=P[a]-Q[b]
 if (a,b) in((0,1),(1,0)):assert diff==0
 else:assert diff!=0 and all(not lo<r<hi or r==1 for r in roots(diff))
assert tuple(x(1) for x in P)==tuple(x(1) for x in Q)
faces=[];atoms=[]
for species,L in enumerate((P,Q)):
 raw=quadrant(L)
 midpoint=(raw[1]+raw[2])/2
 segments=[(raw[0],raw[1]),(raw[1],midpoint),(midpoint,raw[2]),(raw[2],raw[3]),(raw[3],raw[4]),(raw[4],raw[0])]
 # The six atoms partition exactly the original five native sides.
 assert cross(midpoint-raw[1],raw[2]-raw[1])==0 and 2*midpoint==raw[1]+raw[2]
 for sx,sy in product((-1,1),repeat=2):
  def transform(z):
   z=V(sx*z[0],sy*z[1])
   return z if species==0 else V(z[1],3*w-z[0])
  transformed=[transform(z) for z in raw]
  if sx*sy<0:transformed=list(reversed(transformed))
  faces.append(transformed)
  for a,b in segments:
   a,b=transform(a),transform(b)
   if sx*sy<0:a,b=b,a
   atoms.append((a,b))
assert len(faces)==8 and len(atoms)==48
assert faces==[[V(*map(R,v)) for v in face] for face in D['faces']]
assert atoms==[tuple(V(*map(R,v)) for v in atom) for atom in D['atoms']]
t,v=V(w*u,-w),V(3*w*u,3*w)
assert [t,v]==[V(*map(R,z)) for z in D['periods']]
covol=cross(t,v);assert covol==18*u and R(D['area'])==covol
pairs=[(0,6,0,0),(1,15,-1,0),(2,34,1,-1),(3,46,1,-1),(4,32,2,-1),(5,17,0,0),(7,14,-1,0),(8,13,-1,0),(9,19,-1,0),(10,39,1,0),(11,23,0,0),(12,18,0,0),(16,33,2,-1),(20,40,2,0),(21,28,2,0),(22,38,1,0),(24,30,0,0),(25,44,-1,0),(26,43,-1,0),(27,37,-1,0),(29,41,0,0),(31,45,-1,0),(35,47,0,0),(36,42,0,0)]
assert pairs==[tuple(p) for p in D['pairs']]
assert sorted(k for i,j,m,n in pairs for k in(i,j))==list(range(48))
for i,j,m,n in pairs:
 a,b=atoms[i];c,d=atoms[j];shift=m*t+n*v
 assert a==d+shift and b==c+shift and a!=b
areas=[sum(cross(poly[j],poly[(j+1)%5]) for j in range(5))/2 for poly in faces]
assert areas[:4]==[9*u/4+w*(1-u*u)/8]*4
assert areas[4:]==[9*u/4-w*(1-u*u)/8]*4
assert sum(areas)==covol and D['atomic_edge_count']==48 and D['symbolic_pair_count']==24
# All identities specialize at u1 with positive lattice determinant and original faces.
assert covol(1)==18 and all(a(1)>0 for a in areas)
print('PASS fullinterval positivity/nativeclosure;30 complete strictsupports and armprivacies;8 original congruent convex CCW faces;48 actual atoms/24 disjoint complete reversepairs;polynomialendpoint identities;positivecovol18u=totalnativearea,includingu1.')
