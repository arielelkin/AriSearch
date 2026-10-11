"""Independent full lattice tiling audit for r=1. No author imports."""
from sage.all import QuadraticField,AA,vector,matrix
from itertools import product
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
V=lambda x,y:vector(K,[x,y])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if len(poly)>2 else K(0)
def ccw(poly):return poly if area(poly)>0 else list(reversed(poly))
def clip(a,b):
 out=ccw(a)
 for i in range(len(b)):
  edge0=b[i];edge=b[(i+1)%len(b)]-edge0
  if not out:break
  prev=out[-1];prevside=cross(edge,prev-edge0);new=[]
  for cur in out:
   curside=cross(edge,cur-edge0)
   if (prevside<0 and curside>=0) or (prevside>=0 and curside<0):
    new.append(prev+(cur-prev)*prevside/(prevside-curside))
   if curside>=0:new.append(cur)
   prev,prevside=cur,curside
  out=new
 return out
c=(3*w-1)/2;d=(w-1)/2
quarter=[V(0,0),V(d,0),V(d+1,w),V(d+K(1)/2,3*w/2),V(0,c)]
assert area(quarter)==K(9)/4
for i in range(5):
 for j in range(5):
  if j not in [i,(i+1)%5]:assert cross(quarter[(i+1)%5]-quarter[i],quarter[j]-quarter[i])>0
# Raw native pentagons, original direction convention.
def native(sides):
 a,b,c1,d1,e=sides
 edges=[V(a,0),V(0,b),V(-w*c1/2,c1/2),V(-d1/2,-w*d1/2),V(e/2,-w*e/2)]
 assert sum(edges,V(0,0))==V(0,0)
 out=[V(0,0)]
 for e1 in edges[:-1]:out.append(out[-1]+e1)
 return out
P=native([K(1),K(1),c,d,K(2)])
Q=native([d,c,K(1),K(1),K(2)])
F30=matrix(K,[[K(1)/2,w/2],[w/2,-K(1)/2]])
assert Q==[F30*(P[i]-P[4]) for i in [4,3,2,1,0]]
rot240=matrix(K,[[ -K(1)/2,w/2],[-w/2,-K(1)/2]])
assert [rot240*x+P[3] for x in quarter]==[P[3],P[4],P[0],P[1],P[2]]
flip=matrix(K,[[-1,0],[0,1]])
assert [flip*x+Q[1] for x in quarter]==[Q[1],Q[0],Q[4],Q[3],Q[2]]
S=[ccw([V(s*x,s2*y) for x,y in quarter]) for s,s2 in product((-1,1),repeat=2)]
rot90=matrix(K,[[0,-1],[1,0]])
center=V(0,3*w);motif=S+[ccw([center+rot90*x for x in p]) for p in S]
u=V(w,-w);v=V(3*w,3*w)
assert cross(u,v)==18 and sum(area(p) for p in motif)==18
# Complete rigorous difference bound for ALL eight motif faces.
xs=[x[0] for p in motif for x in p];ys=[x[1] for p in motif for x in p]
assert max(xs)-min(xs)==3*w
assert max(ys)-min(ys)==5*w+K(1)/2<6*w
# Any overlap requires |w(m+3n)|<=3w, |w(-m+3n)|<6w.
# Hence |6n|<9 and |2m|<9: |n|<=1, |m|<=4.
checked=0
for m,n in product(range(-4,5),range(-1,2)):
 delta=m*u+n*v
 for i,a in enumerate(motif):
  for j,b0 in enumerate(motif):
   if m==n==0 and i==j:continue
   b=[x+delta for x in b0]
   assert area(clip(a,ccw(b)))==0,(m,n,i,j)
   checked+=1
assert checked==1720
certificate=Path(__file__).resolve().parents[1]/'certificates'/'partial-contact-cairo-adjacent-repeat-periodic.json'
data=json.loads(certificate.read_text())
serialized=[[V(K(x),K(y)) for x,y in poly] for poly in data['face_vertices']]
key=lambda poly:tuple(sorted(tuple(v) for v in poly))
assert sorted(key(poly) for poly in serialized)==sorted(key(poly) for poly in motif)
assert [V(K(x),K(y)) for x,y in data['periods']]==[u,v]
assert [K(x) for x in data['native_sides']]==[1,1,c,d,2]
assert data['face_count']==8 and K(data['cell_area'])==18 and K(data['tile_area'])==K(9)/4
print('PASS:exact native P and Q congruence;8 convex motif pentagons;complete1720 lattice-pair intersections zero;motif area18=lattice covolume18.')
