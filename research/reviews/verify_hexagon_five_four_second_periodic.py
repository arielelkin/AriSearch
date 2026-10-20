"""Independent exact positive carrier checker; imports no search code."""
from sage.all import QuadraticField,vector,matrix,ZZ
from pathlib import Path
import json
K=QuadraticField(3,'r');r=K.gen()
d=json.loads((Path(__file__).resolve().parents[1]/'certificates/hexagon-five-four-second-periodic-2026-10-19.json').read_text())
def decode(p):return [vector(K,[K(x) for x in v]) for v in p]
P=[decode(p) for p in d['prototile_vertices']]
T=[(x['type'],decode(x['vertices'])) for x in d['representatives']]
h,t=decode(d['periods']);M=matrix(K,[h,t]).transpose();Mi=M.inverse()
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
area=lambda p:sum(cross(p[i],p[(i+1)%6]) for i in range(6))/2
assert M.det()>0
for f,q in T:
 p=P[f]
 assert all(cross(q[(i+1)%6]-q[i],q[j]-q[i])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
 assert any(all((p[i]-p[j]).dot_product(p[i]-p[j])==(q[(k+s*i)%6]-q[(k+s*j)%6]).dot_product(q[(k+s*i)%6]-q[(k+s*j)%6]) for i in range(6) for j in range(6)) for k in range(6) for s in (-1,1))
assert sum(area(q) for _,q in T)==M.det()
ledger=[]
for f,(_,p) in enumerate(T):
 for i in range(6):
  a,b=p[i],p[(i+1)%6];mates=[]
  for g,(_,q) in enumerate(T):
   for j in range(6):
    z=Mi*(a-q[(j+1)%6])
    if b-a==q[j]-q[(j+1)%6] and all(x in ZZ for x in z):mates.append((g,j,tuple(z)))
  assert len(mates)==1,(f,i,mates)
  ledger.append((f,i,mates[0]))
print('PASS exact 2A+2B periodic carrier; determinant',M.det())
print('Periods:',h,t)
print('Boundary ledger:',ledger)
