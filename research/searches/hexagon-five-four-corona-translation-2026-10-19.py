#!/usr/bin/env python3
"""Exact orbit compatibility of the forced two-halfturn corona; no patch search."""
from sage.all import QuadraticField, vector, floor, ceil
from pathlib import Path
import json
K=QuadraticField(3,'r');r=K.gen()
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'certificates/hexagon-five-four-39-omissions-2026-10-19.json').read_text())
cert=json.loads((root/'certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json').read_text())
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def overlap(p,q):
 for poly,other in ((p,q),(q,p)):
  orient=1 if cross(poly[1]-poly[0],poly[2]-poly[1])>0 else -1
  for i in range(6):
   if all(orient*cross(poly[(i+1)%6]-poly[i],x-poly[i])<=0 for x in other):return False
 return True
def key(p):return tuple(sorted(tuple(x) for x in p))
rows=[]
for entry in cert['rows']:
 idx=entry['row_index']; row=source['rows'][idx]
 A=[vector(K,[K(x[0])+K(x[1])*r for x in v]) for v in row['vertices'][0]]
 v=A[3]+A[4]-A[5]-A[0];assert v!=0
 state=entry['results'][6];assert state['valid']
 patch=[[vector(K,[K(x) for x in w]) for w in p] for p in state['patch']]
 # H3 H5 is translation v. Both H5 and H3 map root A to forced A.
 h5=A[5]+A[0];h3=A[3]+A[4]
 assert any(key([h3-x for x in A])==key(p) for p in patch)
 assert any(key([h5-x for x in A])==key(p) for p in patch)
 dots=[x.dot_product(v) for p in patch for x in p]
 width=max(dots)-min(dots); norm=v.dot_product(v)
 # All |n| >= ceil(width/norm) have disjoint interior projection intervals.
 cap=int(ceil(width/norm));bad=[];same=[]
 for n in range(1,cap):
  for i,p in enumerate(patch):
   for j,q in enumerate(patch):
    moved=[x+n*v for x in q]
    if key(p)==key(moved):same.append([n,i,j])
    elif overlap(p,moved):bad.append([n,i,j])
 # Canonical representatives modulo v and exact exposed side quotient.
 reps={}
 for p in patch:
  shift=int(floor(min(x.dot_product(v) for x in p)/norm))
  q=[x-shift*v for x in p];reps[key(q)]=q
 edges={}
 for f,p in enumerate(reps.values()):
  for side in range(6):
   a,b=p[side],p[(side+1)%6]
   shift=int(floor(min(a.dot_product(v),b.dot_product(v))/norm))
   edge=tuple(sorted((tuple(a-shift*v),tuple(b-shift*v))))
   edges.setdefault(edge,[]).append([f,side])
 assert all(len(x)<=2 for x in edges.values())
 boundary=[dict(endpoints=[[str(z) for z in x] for x in e],incidence=inc) for e,inc in edges.items() if len(inc)==1]
 result=dict(row_index=idx,fundamental_tiles=len(reps),boundary=boundary,translation=[str(x) for x in v],projection_width=str(width),norm_squared=str(norm),integer_cap_exclusive=cap,overlaps=bad,identifications=same)
 rows.append(result);print(result)
out=dict(schema='FORCED_CORONA_TRANSLATION_ORBIT_V1',domain='rows15,16,23,26,31; corona6; integer orbit of H3 H5, projection bounded',rows=rows)
(root/'certificates/hexagon-five-four-corona-translation-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
