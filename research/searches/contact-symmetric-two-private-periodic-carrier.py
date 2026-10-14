"""SUPERSEDED historical one-point extraction; do not register separately.
Canonical all-metric producer: contact-symmetric-two-private-symbolic-carrier.py.
Exact one-point symmetric-P / two-private-Q periodic carrier.
No search or numeric tolerance: six explicit polygons and eighteen pairings.
"""
from sage.all import QuadraticField, AA, vector, QQ
K=QuadraticField(2,"r",embedding=AA(2).sqrt());r=K.gen()
def vec(x,y):return vector(K,[x,y])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(F):return sum(cross(a,b) for a,b in zip(F,F[1:]+F[:1]))/2
P=[vec(0,-QQ(5)/4),vec((3-r)/8,-QQ(5)/8-r/2),vec((3-r)/8+r/2,-QQ(5)/8),vec((3-r)/8,-QQ(5)/8+r/2),vec(0,0)]
Q=[vec(0,0),vec(r/4+QQ(5)/4,0),vec(3*r/4+QQ(5)/4,r/2),vec(3*r/4+QQ(5)/4,r/2+1),vec(r/8+1,9*r/8+QQ(5)/4),vec(r/8,9*r/8+QQ(5)/4),vec(-r/2,r/2+QQ(5)/4),vec(-r/2,r/2)]
Qh=[Q[0]+Q[1]-p for p in Q]
F1=[vec(5*r/8+QQ(13)/8,QQ(5)/8),vec(3*r/4+QQ(5)/4,r/2),vec(r/4+QQ(5)/4,0),vec(3*r/4+QQ(5)/4,-r/2),vec(5*r/8+QQ(13)/8,-QQ(5)/8)]
F2=[vec(5*r/4+QQ(13)/8,5*r/8+QQ(5)/8),vec(3*r/4+QQ(9)/4,r/2+1),vec(3*r/4+QQ(5)/4,r/2+1),vec(3*r/4+QQ(5)/4,r/2),vec(5*r/8+QQ(13)/8,QQ(5)/8)]
F4=[vec(-3*r/8+QQ(5)/8,r+QQ(13)/8),vec(r/8,9*r/8+QQ(5)/4),vec(r/8+1,9*r/8+QQ(5)/4),vec(r/8+1,9*r/8+QQ(9)/4),vec(r/4+QQ(5)/8,13*r/8+QQ(13)/8)]
F7=[vec(-3*r/8-QQ(3)/8,-QQ(5)/8),vec(-r/2,-r/2),vec(0,0),vec(-r/2,r/2),vec(-3*r/8-QQ(3)/8,QQ(5)/8)]
reps=[Q,Qh,F1,F2,F4,F7]
V=vec(5*r/8+1,13*r/8+QQ(9)/4)
U=vec(-9*r/8-QQ(13)/8,r/2+QQ(5)/8)
pairs=[((0,0),(1,0),(0,0)),((0,1),(2,1),(0,0)),((0,2),(3,2),(0,0)),((0,3),(1,3),(1,0)),((0,4),(4,1),(0,0)),((0,5),(3,4),(0,1)),((0,6),(2,4),(0,1)),((0,7),(5,2),(0,0)),((1,1),(5,1),(0,0)),((1,2),(4,2),(-1,0)),((1,4),(3,1),(-1,0)),((1,5),(4,4),(-1,-1)),((1,6),(5,4),(0,-1)),((1,7),(2,2),(0,0)),((2,0),(3,3),(0,0)),((2,3),(5,3),(0,-1)),((3,0),(4,0),(0,-1)),((4,3),(5,0),(1,0))]
def positive(z):return AA(z)>0
def convex(F):
 assert positive(area(F))
 for i,a in enumerate(F):
  b=F[(i+1)%len(F)]
  for j,c in enumerate(F):
   if j not in(i,(i+1)%len(F)):assert positive(cross(b-a,c-a))
def congruent(F,G):
 n=len(F)
 return any(all((F[i]-F[j]).dot_product(F[i]-F[j])==(G[(s+d*i)%n]-G[(s+d*j)%n]).dot_product(G[(s+d*i)%n]-G[(s+d*j)%n]) for i in range(n) for j in range(n)) for s in range(n) for d in(-1,1))
def angle_check(F,target):
 for i,b in enumerate(F):
  a=F[i-1]-b;c=F[(i+1)%len(F)]-b;dot=a.dot_product(c)
  if target=="P" and dot==0:continue
  assert AA(dot)<0
  assert dot**2==((2-r)/4 if target=="P" else QQ(1)/2)*a.dot_product(a)*c.dot_product(c)
for F in[P]+reps:convex(F)
angle_check(P,"P");assert sum((P[i-1]-P[i]).dot_product(P[(i+1)%5]-P[i])==0 for i in range(5))==1
angle_check(Q,"Q")
assert all(congruent(P,F) for F in reps[2:]);assert congruent(Q,Qh)
Pl=[(P[(i+1)%5]-P[i]).dot_product(P[(i+1)%5]-P[i]) for i in range(5)]
Ql=[(Q[(i+1)%8]-Q[i]).dot_product(Q[(i+1)%8]-Q[i]) for i in range(8)]
assert Pl[1]==Pl[2]==1 and Pl[0]==Pl[3] and Pl[4]==QQ(25)/16
assert [i for i,z in enumerate(Ql) if z not in Pl]==[0,3]
assert Ql[0]==Ql[3]==((5+r)/4)**2
assert len(pairs)==18
seen=[]
for (f,i),(g,j),(m,n) in pairs:
 seen.extend([(f,i),(g,j)]);shift=m*V+n*U
 assert reps[f][i]==reps[g][(j+1)%len(reps[g])]+shift
 assert reps[f][(i+1)%len(reps[f])]==reps[g][j]+shift
assert len(set(seen))==36 and set(seen)=={(f,i) for f,F in enumerate(reps) for i in range(len(F))}
assert positive(cross(V,U));assert sum(area(F) for F in reps)==cross(V,U)
print("PASS: six explicit representatives,18 reversed pairs/36 edges,72 endpoint coordinate identities, strict convexity, congruence, native angles, exactly2 private Q slots, positive covolume and multiplicity-one area identity")
print("P area",area(P),"Q area",area(Q),"covolume",cross(V,U))
