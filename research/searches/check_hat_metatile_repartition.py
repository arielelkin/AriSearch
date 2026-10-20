#!/usr/bin/env python3
"""Audit retained repartitions using edge cancellation and supporting lines.
Does not import repartition producer. Uses reviewed exact clipping primitives.
"""
import importlib.util,json,itertools,hashlib
from pathlib import Path
s=importlib.util.spec_from_file_location('audit','research/reviews/check_hat_eight_kite_convex_clusters.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
p=Path('research/certificates/hat-metatile-repartition-gate.json');raw=p.read_bytes();d=json.loads(raw)
def point(v):return (a.K(v[0])/4,a.r*a.K(v[1])/4)
representatives={};rowmaps={}
for name,R in d['regions'].items():
 cells=[[point(v) for v in P] for P in R['cells']]
 for P,Q in itertools.combinations(cells,2):assert a.area2(a.clip(P,Q))==0
 # Each constituent source hat has eight cells and exact area 2sqrt3.
 for owner in set(R['owners']):
  ps=[P for P,o in zip(cells,R['owners']) if o==owner]
  assert len(ps)==8 and sum(map(a.area2,ps))==4*a.r
  assert a.boundary(ps) is not None
 rows={r['mask']:r for r in R['eligible']};rowmaps[name]=rows
 for m,row in rows.items():
  ids=[i for i in range(len(cells)) if m>>i&1];assert ids==row['cells'] and 1<=len(ids)<=8
  P=a.boundary([cells[i] for i in ids]);Q=[point(v) for v in row['polygon']]
  assert P and a.same(P,Q) and len(P) in (5,6)
  assert all(a.turn(P[i-1],P[i],P[(i+1)%len(P)])>0 for i in range(len(P)))
  assert all(a.cross(a.subtract(b,c),a.subtract(v,c))>=0 for c,b in zip(P,P[1:]+P[:1]) for v in P)
  assert row['cross_hat']==(len({R['owners'][i] for i in ids})>1)
  c=row['class']
  if c in representatives:assert a.congruent(P,representatives[c])
  else:representatives[c]=P
 for m in rows:
  assert a.area2([point(v) for v in rows[m]['polygon']])==sum(a.area2(cells[i]) for i in rows[m]['cells'])
assert len(representatives)==3
for P,Q in itertools.combinations(representatives.values(),2):assert not a.congruent(P,Q)
for W in d['witnesses']:
 used=set();crossed=False
 for name,masks in W['covers'].items():
  union=0;R=d['regions'][name]
  for m in masks:
   assert not union&m;union|=m;row=rowmaps[name][m];used.add(row['class']);crossed|=row['cross_hat']
  assert union==(1<<len(R['cells']))-1
 assert used==set(W['pair']) and crossed
# Match the two pentagons to previously independently certified periodic carriers.
old=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())
oldP=[[a.point(v) for v in row['hull']] for row in old['convex_subsets'] if row['mask'] in (9,13)]
for P in representatives.values():
 if len(P)==5:
  # Initial hats are at half reference scale.
  assert any(a.congruent([(2*x,2*y) for x,y in P],Q) for Q in oldP)
 else:
  assert len(P)==6
  ds=[a.dot(a.subtract(P[(i+1)%6],P[i]),a.subtract(P[(i+1)%6],P[i])) for i in range(6)]
  assert len(set(ds))==1 and all(a.turn(P[i-1],P[i],P[(i+1)%6])==a.turn(P[-1],P[0],P[1]) for i in range(6))
print(json.dumps(dict(status='PASSED',sha256=hashlib.sha256(raw).hexdigest(),witnesses=len(d['witnesses']),classes=3,scope='Exact primitive disjointness, edge boundaries, strict convexity, all retained cover witnesses, congruence and periodic carrier matches. Enumeration completeness remains producer argument.'),indent=2))
