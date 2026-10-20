from sage.all import *
import json
from pathlib import Path
K=CyclotomicField(20); w=K.gen()
cross=lambda a,b: AA(((a.conjugate()*b-a*b.conjugate())/(2*w**5)))
P=[sum((w**(4*j) for j in range(i)),K(0)) for i in range(5)]
# Independent angle-walk: exterior turns 36 at A, 54 at B.
word="AAABBABB"; dirs=[0]
for c in word[1:]: dirs.append(dirs[-1]+(2 if c=='A' else 3))
assert dirs==[0,2,4,7,10,12,15,18]
# Solve real 2x2 closure for the two BB edges, rather than importing length.
u=w**dirs[3]; v=w**dirs[6]; other=sum((w**dirs[i] for i in range(8) if i not in [3,6]),K(0))
x=-cross(other,v)/cross(u,v); y=-cross(u,other)/cross(u,v)
assert x==y and x>0
Q=[K(0)]
for i in range(7):Q.append(Q[-1]+K(x if i in [3,6] else 1)*w**dirs[i])
assert Q[-1]+w**dirs[-1]==0
# Direct witness representatives, independent of search development.
t=[0,w**4+1,2*w**6-w**4-2,w**6+w**2,w**6-1,w**6-w**4-1]
r=[6,8,16,18,0,10]
T=[[w**r[f]*z+t[f] for z in (P if f<4 else Q)] for f in range(6)]
U=w**6-2*w**4-w**2-3; V=-3*w**6-2*w**2+2
det=cross(U,V); assert det>0
for poly in T:
 for i,a in enumerate(poly):
  b=poly[(i+1)%len(poly)]
  assert all(cross(b-a,z-a)>0 for j,z in enumerate(poly) if j not in [i,(i+1)%len(poly)])
area=sum(sum(cross(a,poly[(i+1)%len(poly)]) for i,a in enumerate(poly))/2 for poly in T)
assert area==det
coords=lambda z:(cross(z,V)/det,cross(U,z)/det)
D=[(f,i) for f in range(6) for i in range(len(T[f]))]
mate={}; shifts={}
for f,i in D:
 a=T[f][i]; b=T[f][(i+1)%len(T[f])]; hits=[]
 for g,j in D:
  c=T[g][j]; d=T[g][(j+1)%len(T[g])]
  if b-a != c-d:continue
  z=a-d; h=coords(z)
  if all(k in ZZ for k in h): hits.append(((g,j),tuple(ZZ(k) for k in h)))
 assert len(hits)==1,(f,i,hits)
 mate[f,i],shifts[f,i]=hits[0]
assert all(mate[mate[d]]==d and shifts[mate[d]]==tuple(-x for x in shifts[d]) for d in D)
unseen=set(D); cycles=[]
while unseen:
 d=min(unseen); c=[]
 while d not in c:
  c.append(d); unseen.remove(d); g,j=mate[d]; d=(g,(j+1)%len(T[g]))
 assert d==c[0] and len(c)==3
 labels=['P' if f<4 else word[i] for f,i in c]
 assert sorted(labels) in [['A','P','P'],['B','B','P']]
 assert sum(108 if z=='P' else 144 if z=='A' else 126 for z in labels)==360
 cycles.append(c)
assert len(cycles)==12
seen={0}
while True:
 new=seen|{mate[f,i][0] for f,i in D if f in seen}
 if new==seen:break
 seen=new
assert len(seen)==6
assert len(cycles)-len(D)/2+6==0
# Strong independent geometric check: complete finite translate bound and exact intersections.
A=[[coords(z) for z in poly] for poly in T]
H=[Polyhedron(vertices=poly,base_ring=AA) for poly in A]; tests=0
for f in range(6):
 for g in range(6):
  bounds=[(ceil(min(z[k] for z in A[f])-max(z[k] for z in A[g])),floor(max(z[k] for z in A[f])-min(z[k] for z in A[g]))) for k in [0,1]]
  for a in range(bounds[0][0],bounds[0][1]+1):
   for b in range(bounds[1][0],bounds[1][1]+1):
    if f==g and a==b==0:continue
    J=Polyhedron(vertices=[(z[0]+a,z[1]+b) for z in A[g]],base_ring=AA)
    assert H[f].intersection(J).dim()<2,(f,g,a,b)
    tests+=1
# Compare every retained claim to recovered geometry; certificate is data only.
data=json.loads(Path('research/searches/regular-pentagon-octagon-qdimer-carrier-sol-2026-10-19.json').read_text())
parse=lambda z: K(sage_eval(z,locals={'zeta20':w}))
for rec in data['records']:
 cert=rec['certificate']; S=[[parse(z) for z in poly] for poly in cert['polygons']]
 assert all(S[f]==T[f] for f in range(5))
 assert set(S[5])==set(T[5])
 for pair,h in zip(rec['pairs'],cert['shift_coefficients']):
  (f,i),(g,j)=[D[k] for k in pair]
  assert S[f][i]-S[g][(j+1)%len(S[g])]==h[0]*U+h[1]*V
  assert S[f][(i+1)%len(S[f])]-S[g][j]==h[0]*U+h[1]*V
# Q has a reflection symmetry, explaining duplicate maps.
assert set(-w**2*z.conjugate()+Q[2] for z in Q)==set(Q)
print('PASS exact geometry, 18 edge pairs, 12 links, connected torus; translate tests',tests,'area',area.n())
