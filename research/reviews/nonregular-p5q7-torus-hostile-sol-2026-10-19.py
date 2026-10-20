"""Independent audit: endpoint union-find and exact metric; no search imports."""
from sage.all import CyclotomicField, AA
import json
K=CyclotomicField(72); z=K.gen(); ii=z**18
real=lambda x:(x+x.conjugate())/2
imag=lambda x:(x-x.conjugate())/(2*ii)
cross=lambda x,y:imag(x.conjugate()*y)
pa=[115,115,100,110,100]; qa=[130,130,130,125,125,125,135]
pd=[0,13,29,43,59]; qd=[0,10,20,31,42,53,62]
L=2*(real(z**7)-real(z**13))
u=z**10; v=z**31; target=-sum(z**k for k in [0,20,42,53,62])
det=cross(u,v)
a=cross(target,v)/det; b=cross(u,target)/det
pl=[L,K(1),K(1),K(1),K(1)]; ql=[K(1),a,K(1),b,K(1),K(1),K(1)]
polys=[]
for ang,dirs,lens in [(pa,pd,pl),(qa,qd,ql)]:
 assert all(AA(x)>0 for x in lens)
 assert sum(lens[j]*z**dirs[j] for j in range(len(lens)))==0
 assert all((dirs[j]-dirs[j-1])%72==36-ang[j]//5 for j in range(len(lens)))
 pts=[K(0)]
 for x,k in zip(lens,dirs): pts.append(pts[-1]+x*z**k)
 pts.pop(); n=len(pts)
 assert all(AA(cross(pts[(j+1)%n]-pts[j],pts[k]-pts[j]))>0 for j in range(n) for k in range(n) if k not in [j,(j+1)%n])
 polys.append(pts)
alpha=[5,16,21,12,17,0,23,14,19,10,9,18,3,20,7,22,1,4,11,8,13,2,15,6]
faces=[list(range(5)),list(range(5,10)),list(range(10,17)),list(range(17,24))]
nextd={d:f[(j+1)%len(f)] for f in faces for j,d in enumerate(f)}
faceof={d:k for k,f in enumerate(faces) for d in f}
angles=pa+pa+qa+qa; lengths=pl+pl+ql+ql
points=polys[0]+polys[0]+polys[1]+polys[1]
parent=list(range(24))
def root(x):
 while parent[x]!=x: x=parent[x]
 return x
def union(x,y): parent[root(x)]=root(y)
pairs=[]; adjacency=[set() for _ in faces]
for d,e in enumerate(alpha):
 assert e!=d and alpha[e]==d
 assert lengths[d]==lengths[e]
 # Direct orientation-preserving rigid motion sends mate head to d tail,
 # mate tail to d head, so interiors occupy opposite sides of seam.
 ed=points[nextd[d]]-points[d]; ee=points[nextd[e]]-points[e]
 rot=-ed/ee; shift=points[d]-rot*points[nextd[e]]
 assert rot*rot.conjugate()==1
 assert rot*points[e]+shift==points[nextd[d]]
 assert rot*points[nextd[e]]+shift==points[d]
 union(d,nextd[e]); union(nextd[d],e)
 adjacency[faceof[d]].add(faceof[e])
 if d<e:pairs.append([d,e])
classes=sorted([sorted([d for d in range(24) if root(d)==r]) for r in set(root(d) for d in range(24))])
for cls in classes:
 assert len(cls)==3 and sum(angles[d] for d in cls)==360
 # Link explicitly visits every sector once.
 visited=[]; x=cls[0]
 while x not in visited: visited.append(x); x=nextd[alpha[x]]
 assert x==cls[0] and set(visited)==set(cls)
seen={0}
while True:
 new=seen|set.union(*(adjacency[f] for f in seen))
 if seen==new:break
 seen=new
assert len(seen)==4 and 4-len(pairs)+len(classes)==0
# Conditional symbolic transfer: classify pairs by native side indices.
crosspairs=set()
for d,e in pairs:
 f,g=faceof[d],faceof[e]; j=faces[f].index(d); k=faces[g].index(e)
 if (f<2)==(g<2): assert j==k
 else: crosspairs.add((j,k) if f<2 else (k,j))
assert crosspairs=={(4,0),(3,2),(2,4),(1,6)}
print(json.dumps({'verdict':'PASS exact metric and endpoint/link audit','pairs':pairs,'vertex_classes':classes,'cross_species_equalities':sorted(crosspairs),'F':4,'E':12,'V':8},indent=2))
