"""Independent integer polygon/lattice witness verification; no solver."""
import json
from pathlib import Path
from math import ceil
U=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
W=((2,1,2,1,2,1),(2,2,3,1,3,2))
w=json.loads(Path('research/certificates/hexagon-imbalance-four-cell-periodic-sol-2026-10-19.json').read_text())['witness']
assert (w['a'],w['b'],w['c'])==(2,1,2)
T=((4,-8),(9,-8))
def add(p,q):return tuple(a+b for a,b in zip(p,q))
def sub(p,q):return tuple(a-b for a,b in zip(p,q))
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
Q=[]
for s in w['states']:
 ls=[W[s['tile']][(s['r']+s['eps']*k)%6] for k in range(6)]
 assert ls==s['lengths']
 q=[(0,0)]
 for k,l in enumerate(ls):q.append(add(q[-1],(l*U[k][0],l*U[k][1])))
 assert q[-1]==(0,0)
 Q.append(q[:-1])
def index(x,y):
 n,yr=divmod(y,2);m,xr=divmod(x-n,2)
 return 2*yr+xr,m,n
# Build representatives by prescribed short paths; then independently
# require ALL24 seams to agree with the displayed physical periods.
positions=[(0,0)]*4
for cell,ks in [((1,0),[0]),((0,1),[1]),((1,1),[0,1])]:
 x=y=0;p=(0,0)
 for k in ks:
  i,_,_=index(x,y);dx,dy=U[k];j,_,_=index(x+dx,y+dy)
  p=add(p,sub(Q[i][k],Q[j][(k+4)%6]));x+=dx;y+=dy
 positions[index(*cell)[0]]=p
P=[[add(v,p) for v in q] for q,p in zip(Q,positions)]
for i,(x,y) in enumerate(w['cells']):
 for k,(dx,dy) in enumerate(U):
  j,m,n=index(x+dx,y+dy)
  d=(m*T[0][0]+n*T[1][0],m*T[0][1]+n*T[1][1])
  assert P[i][k]==add(P[j][(k+4)%6],d)
  assert P[i][(k+1)%6]==add(P[j][(k+3)%6],d)
def disjoint(P,Q):
 # Independent complete convex SAT, exact integer supporting lines.
 return any(all(cross(sub(R[(i+1)%6],a),sub(q,a))<=0 for q in S)
            for R,S in ((P,Q),(Q,P)) for i,a in enumerate(R))
xs=[v[0] for p in P for v in p];ys=[v[1] for p in P for v in p]
width=max(xs)-min(xs);height=max(ys)-min(ys)
# Inverse lattice map: m=-(8x+9y)/40, n=(2x+y)/10.
# Intersecting polygons require a displacement in the difference bbox.
M=ceil((8*width+9*height)/40);N=ceil((2*width+height)/10)
checked=0
for m in range(-M,M+1):
 for n in range(-N,N+1):
  d=(m*T[0][0]+n*T[1][0],m*T[0][1]+n*T[1][1])
  for i,p in enumerate(P):
   for j,q in enumerate(P):
    if m==n==0 and i==j:continue
    assert disjoint(p,[add(v,d) for v in q]),(m,n,i,j)
    checked+=1
area2=sum(sum(cross(p[k],p[(k+1)%6]) for k in range(6)) for p in P)
assert cross(*T)==40 and area2==80
print('PASS: periods',T,'representative positions',positions,'lattice det40, area2 sum80;',checked,'exact separation checks; displacement coefficient bounds',M,N)
