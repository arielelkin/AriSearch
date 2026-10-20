"""Independent exact check of retained four-cell carrier, no solver/import."""
import json
from pathlib import Path
words=((2,1,2,1,2,1),(2,2,3,1,3,2))
u=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
data=json.loads(Path("research/searches/hexagon-imbalance-periodic-small-sol-2026-10-19.json").read_text())["witness"]
assert (data["a"],data["b"],data["c"])==(2,1,2)
assert data["cells"]==[[0,0],[1,0],[0,1],[1,1]]
states=data["states"]
L=[]; Q=[]
for s in states:
 assert s["tile"] in (0,1) and 0<=s["r"]<6 and s["eps"] in (-1,1)
 row=tuple(words[s["tile"]][(s["r"]+s["eps"]*k)%6] for k in range(6))
 assert list(row)==s["lengths"]
 q=[(0,0)]
 for v,(x,y) in zip(row,u): q.append((q[-1][0]+v*x,q[-1][1]+v*y))
 assert q[-1]==(0,0)
 L.append(row); Q.append(q[:6])
def idx(x,y):
 q,r=divmod(y,2)
 return 2*r+(x-q)%2
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def step(x,y,k):
 i=idx(x,y); dx,dy=u[k]; j=idx(x+dx,y+dy)
 assert L[i][k]==L[j][(k+3)%6]
 return sub(Q[i][k],Q[j][(k+4)%6])
for y in range(2):
 for x in range(2):
  for k in range(6): step(x,y,k)
# Every elementary triangle, using both cyclic orientations of triangles.
for y in range(2):
 for x in range(2):
  for ks in ((0,2,4),(1,3,5)):
   pos=(x,y); total=(0,0)
   for k in ks:
    total=add(total,step(*pos,k)); pos=add(pos,u[k])
   assert pos==(x,y) and total==(0,0)
def path(ks):
 pos=(0,0); total=(0,0)
 for k in ks:
  total=add(total,step(*pos,k)); pos=add(pos,u[k])
 return pos,total
p,P=path((0,0)); r,R=path((0,1,1))
assert p==(2,0) and r==(1,2)
assert P[0]*R[1]-P[1]*R[0]!=0
print("PASS: all 24 directed seams, eight elementary triangles; physical periods",P,R,"determinant",P[0]*R[1]-P[1]*R[0])
