#!/usr/bin/env python3
"""Independent exhaustive boundary/cover audit of the retained finite gate.
Uses integer edge cancellation, not producer imports or convex hulls.
"""
import json,itertools,hashlib,importlib.util
from fractions import Fraction
from collections import Counter
from pathlib import Path
path=Path('research/certificates/hat-metatile-repartition-gate.json')
raw=path.read_bytes();D=json.loads(raw)
def turn(a,b,c):return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
def edges(P):return list(zip(P,P[1:]+P[:1]))
def boundary(cells):
 E=Counter(e for P in cells for e in edges(P))
 E={e for e,n in E.items() if n>E[e[::-1]]}
 nxt={a:b for a,b in E}
 if len(nxt)!=len(E) or set(nxt)!=set(nxt.values()):return None
 start=min(nxt);P=[];v=start
 while v not in P:P.append(v);v=nxt[v]
 if v!=start or len(P)!=len(E):return None
 while True:
  ix=next((i for i in range(len(P)) if turn(P[i-1],P[i],P[(i+1)%len(P)])==0),None)
  if ix is None:break
  P.pop(ix)
 return P
# Rebuild source placement from the separately reviewed reference kite data.
spec=importlib.util.spec_from_file_location('source','research/searches/source-decoration-hat-patch.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
old=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())
ref=[[tuple(h.Q3(*v) for v in p) for p in K] for K in old['kites']]
def encode(p):
 x,y=p
 assert x.b==y.a==0 and (4*x.a).denominator==(4*y.b).denominator==1
 return int(4*x.a),int(4*y.b)
for name,meta in zip('HTPF',h.init()):
 R=D['regions'][name];out=[];h.expand(meta,h.IDENT,out)
 assert len(out)==len(set(R['owners']))
 for owner,(_,t) in enumerate(out):
  expected={tuple(sorted(encode(h.transPt(t,p)) for p in K)) for K in ref}
  actual={tuple(sorted(map(tuple,K))) for K,o in zip(R['cells'],R['owners']) if o==owner}
  assert expected==actual
rows={};allcovers={}
for name,R in D['regions'].items():
 C=[[tuple(v) for v in P] for P in R['cells']];n=len(C)
 # Establish conforming edges: no vertex lies strictly inside any primitive edge.
 for P in C:
  for a,b in edges(P):
   for Q in C:
    for v in Q:
     assert not (turn(a,b,v)==0 and min(a[0],b[0])<=v[0]<=max(a[0],b[0]) and min(a[1],b[1])<=v[1]<=max(a[1],b[1]) and v not in (a,b))
 E=[set(frozenset(e) for e in edges(P)) for P in C]
 N=[{j for j in range(n) if j!=i and E[i]&E[j]} for i in range(n)]
 F={frozenset([i]) for i in range(n)};eligible=set();counts=[]
 for size in range(1,9):
  counts.append(len(F))
  for S in F:
   P=boundary([C[i] for i in S])
   if P and len(P) in (5,6) and all(turn(P[i-1],P[i],P[(i+1)%len(P)])>0 for i in range(len(P))):
    eligible.add(sum(1<<i for i in S))
  if size<8:F={S|{j} for S in F for i in S for j in N[i]-S}
 assert counts==R['connected_counts']
 rows[name]={r['mask']:r for r in R['eligible']}
 assert len(rows[name])==len(R['eligible']) and eligible==set(rows[name])
 print(name,counts,len(eligible),flush=True)
# An alternative exact-cover traversal: branch on greatest uncovered cell.
for pair in itertools.combinations(sorted(c['id'] for c in D['classes']),2):
 regioncovers={}
 for name,R in D['regions'].items():
  masks=[m for m,r in rows[name].items() if r['class'] in pair]
  def rec(rem):
   if not rem:return [()]
   bit=1<<(rem.bit_length()-1)
   return [tuple(sorted((m,)+rest)) for m in masks if m&bit and m&rem==m for rest in rec(rem^m)]
  regioncovers[name]=rec((1<<len(R['cells']))-1)
 expected=set()
 for covers in itertools.product(*regioncovers.values()):
  rr=[rows[name][m] for name,cover in zip(regioncovers,covers) for m in cover]
  if {r['class'] for r in rr}==set(pair) and any(r['cross_hat'] for r in rr):expected.add(covers)
 saved=[tuple(tuple(sorted(w['covers'][name])) for name in regioncovers) for w in D['witnesses'] if tuple(w['pair'])==pair]
 assert len(saved)==len(set(saved)) and set(saved)==expected
 print('pair',pair,'covers',list(map(len,regioncovers.values())),'admissible',len(expected),flush=True)
# Independent regular-hexagon recognition by equal circumradii and chords.
def norm(v):return v[0]*v[0]+3*v[1]*v[1]
for R in D['regions'].values():
 for row in R['eligible']:
  P=row['polygon']
  if len(P)==6:
   c=[sum(Fraction(v[i],6) for v in P) for i in (0,1)]
   radii={norm([v[i]-c[i] for i in (0,1)]) for v in P}
   chords={norm([a[i]-b[i] for i in (0,1)]) for a,b in edges(P)}
   assert len(radii)==1 and radii==chords
print('PASSED',hashlib.sha256(raw).hexdigest())
