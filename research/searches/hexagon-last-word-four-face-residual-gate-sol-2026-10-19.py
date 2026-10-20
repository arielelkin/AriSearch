#!/usr/bin/env python3
"""Exact reuse of the 113400 labeled 2A2B pairing domain; no enlargement."""
import itertools,json,argparse,hashlib
from pathlib import Path
from sage.all import QQ,matrix,vector
from sage.env import SAGE_VERSION
R=Path(__file__).resolve().parents[1]
source=R/'certificates/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.json'
d=json.loads(source.read_text()); W=(tuple(d['A']),tuple(d['B']))
def matchings(xs):
 if not xs: yield [];return
 a=xs[0]
 for k in range(1,len(xs)):
  for rest in matchings(xs[1:k]+xs[k+1:]):yield [(a,xs[k])]+rest
G=[list(matchings([6*f+i for f in range(4) for i in range(6) if W[f//2][i]==c])) for c in range(5)]
candidates=[];n=0;trivalent_partitions=[]
for signs in itertools.product((1,-1),repeat=3):
 H=(1,)+signs
 for groups in itertools.product(*G):
  n+=1;P=sum(groups,[]);pa=list(range(24));adj=[[] for _ in range(24)]
  def root(x):
   while pa[x]!=x:x=pa[x]
   return x
  for x,y in P:
   f,i=divmod(x,6);g,j=divmod(y,6)
   assert W[f//2][i]==W[g//2][j]
   ends=((i,j),((i-1)%6,(j-1)%6)) if H[f]!=H[g] else ((i,(j-1)%6),((i-1)%6,j))
   for a,b in ends:
    u,v=6*f+a,6*g+b;pa[root(u)]=root(v);adj[u].append(v);adj[v].append(u)
  C={}
  for x in range(24):C.setdefault(root(x),[]).append(x)
  if len(C)!=8 or any(len(c)!=3 for c in C.values()):continue
  trivalent_partitions.append(n)
  seen={0}
  for _ in range(4):
   for x,y in P:
    f,g=x//6,y//6
    if f in seen or g in seen:seen.update((f,g))
  if len(seen)!=4:continue
  for c in C.values():
   assert all(len(adj[x])==2 for x in c)
   reached={c[0]}
   for _ in c:
    reached.update(y for x in list(reached) for y in adj[x])
   assert reached==set(c)
  # Oriented polygons with reversed boundary gluing form a connected orientable
  # closed surface; circular links plus V-E+F=8-12+4=0 give a torus.
  candidates.append(dict(index=n,handedness=H,pairs=P,links=list(C.values()),
   angle_triples=[sorted(6*(x//12)+x%6 for x in c) for c in C.values()]))
assert n==113400 and len(trivalent_partitions)==8 and len(candidates)==6
results=[]
for s in d['strata']:
 if s['status']!='uncovered_branching':continue
 triples=[d['unsigned_triples'][i] for i in s['unsigned_indices']]
 rows=[[int(i//6==f) for i in range(12)] for f in range(2)]+[[t.count(i) for i in range(12)] for t in triples]
 M=matrix(QQ,rows); V=M.row_space(); tests=[]
 for c in candidates:
  checks=[]
  for t in c['angle_triples']:
   row=vector(QQ,[t.count(i) for i in range(12)])
   if row in V:
    coeff=M.transpose().solve_right(row)
    assert coeff*M==row
    assert sum(coeff[i]*(4 if i<2 else 2) for i in range(len(coeff)))==2
    checks.append(dict(triple=t,coefficients=list(map(str,coeff))))
   else:
    # Explicit rational nullspace separator certifies nonimplication.
    z=next(z for z in M.right_kernel().basis() if row.dot_product(z)!=0)
    assert M*z==0 and row.dot_product(z)!=0
    checks.append(dict(triple=t,separator=list(map(str,z)),dot=str(row.dot_product(z))))
  tests.append(dict(candidate=c['index'],passes=all('coefficients' in x for x in checks),rows=checks))
 results.append(dict(mask=s['unsigned_mask'],source_rows=rows,tests=tests,selected_witness=next(x['candidate'] for x in tests if x['passes']),positive_candidates=[x['candidate'] for x in tests if x['passes']]))
out=dict(schema='four-face-residual-rowspan-v1',sage_version=SAGE_VERSION,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),domain=113400,trivalent_partition_indices=trivalent_partitions,candidates=candidates,results=results)
path=R/'certificates/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.json'
if argparse.ArgumentParser().parse_known_args()[1]==['--check']:
 assert json.loads(path.read_text())==json.loads(json.dumps(out));print('CHECK PASS')
else:path.write_text(json.dumps(out,indent=2)+'\n')
print('EXHAUSTED',n,'candidates',len(candidates))
for s in results:print(s['mask'],s['positive_candidates'])
