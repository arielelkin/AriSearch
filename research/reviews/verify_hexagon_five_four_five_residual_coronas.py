"""Independent validation of five surviving exact corona witnesses; no search."""
from sage.all import QuadraticField, vector, matrix
from pathlib import Path
import json
K=QuadraticField(3,'r');r=K.gen()
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'certificates/hexagon-five-four-39-omissions-2026-10-19.json').read_text())
cert=json.loads((root/'certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json').read_text())
parse=lambda x:K(x)
vec=lambda x:vector(K,[parse(y) for y in x])
key=lambda p:tuple(sorted(tuple(x) for x in p))
def separate(p,q):
 for poly in (p,q):
  for a,b in zip(poly,poly[1:]+poly[:1]):
   e=b-a;n=vector(K,[-e[1],e[0]])
   pp=[n.dot_product(v) for v in p];qq=[n.dot_product(v) for v in q]
   if max(pp)<=min(qq) or max(qq)<=min(pp):return True
 return False
for record in cert['rows']:
 row=source['rows'][record['row_index']]
 P=[[vector(K,[K(x[0])+r*K(x[1]) for x in v]) for v in p] for p in row['vertices']]
 assert [z['corona'] for z in record['results'] if z['valid']]==[6]
 z=record['results'][6];A=P[0];mate=[A[5]+A[0]-v for v in A];bd=A[:5]+mate[:5]
 generated=[A,mate]
 for k,t in enumerate(z['isometries']):
  M=matrix(K,[[parse(x) for x in rr] for rr in t['matrix']]);v=vec(t['translation'])
  assert M.transpose()*M==matrix.identity(K,2) and M.det()==t['handedness']
  p=[M*x+v for x in P[t['species']]];j=t['native_side']
  assert {tuple(p[j]),tuple(p[(j+1)%6])}=={tuple(bd[k]),tuple(bd[(k+1)%10])}
  generated.append(p)
 assert key(generated[2])==key(generated[11]) and key(generated[6])==key(generated[7])
 patch=list({key(p):p for p in generated}.values())
 assert {key(p) for p in patch}=={key([vec(v) for v in p]) for p in z['patch']}
 assert all(separate(p,q) for i,p in enumerate(patch) for q in patch[:i])
 for point in bd:
  total=0
  for p in patch:
   if point not in p:continue
   i=p.index(point);u=p[i-1]-point;v=p[(i+1)%6]-point;d=u.dot_product(v);n=u.dot_product(u)*v.dot_product(v)
   assert d<=0
   if d==0:total+=90
   elif 4*d*d==n:total+=120
   else:assert 4*d*d==3*n;total+=150
  assert total==360
 print('PASS row',record['row_index'],'corona 6 exact witness',len(patch),'tiles')
