"""Independent graph-based exhaustive check; run with environment Python."""
import json,itertools,hashlib
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'certificates/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.json').read_text())
src=R/'certificates/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.json'
s=json.loads(src.read_text());assert hashlib.sha256(src.read_bytes()).hexdigest()==d['source_sha256']
W=[s['A'],s['A'],s['B'],s['B']]
def pm(items):
 if not items:yield ();return
 for b in items[1:]:
  for tail in pm(tuple(v for v in items[1:] if v!=b)):yield ((items[0],b),)+tail
G=[list(pm(tuple(6*f+i for f in range(4) for i in range(6) if W[f][i]==c))) for c in range(5)]
assert [len(x) for x in G]==[105,15,3,3,1]
def components(adj):
 unseen=set(range(len(adj)));out=[]
 while unseen:
  reached={min(unseen)};todo=list(reached)
  while todo:
   for y in adj[todo.pop()]:
    if y not in reached:reached.add(y);todo.append(y)
  out.append(sorted(reached));unseen-=reached
 return out
part=[];kept=[];n=0
for hs in itertools.product([1,-1],repeat=3):
 h=[1,*hs]
 for groups in itertools.product(*G):
  n+=1;pairs=list(itertools.chain.from_iterable(groups));adj=[[] for _ in range(24)];fa=[[] for _ in range(4)]
  for a,b in pairs:
   f,i=divmod(a,6);g,j=divmod(b,6);fa[f].append(g);fa[g].append(f)
   assert W[f][i]==W[g][j]
   # endpoint 0=start, 1=end. Opposite handedness preserves native endpoints.
   for endpoint in (0,1):
    other=endpoint if h[f]!=h[g] else 1-endpoint
    u=6*f+(i-1+endpoint)%6;v=6*g+(j-1+other)%6
    adj[u].append(v);adj[v].append(u)
  cs=components(adj)
  if len(cs)!=8 or set(map(len,cs))!={3}:continue
  part.append(n)
  if len(components(fa))!=1:continue
  assert all(len(a)==2 for a in adj)
  kept.append(n);cert=next(x for x in d['candidates'] if x['index']==n)
  assert cert['handedness']==h and cert['pairs']==[list(x) for x in pairs] and cert['links']==cs
  assert cert['angle_triples']==[sorted(6*(x//12)+x%6 for x in c) for c in cs]
assert n==113400 and part==d['trivalent_partition_indices'] and kept==[40,88,9198,9264,14054,14078]
assert [r['mask'] for r in d['results']]==[x['unsigned_mask'] for x in s['strata'] if x['status']=='uncovered_branching']
for result in d['results']:
 stratum=next(x for x in s['strata'] if x['unsigned_mask']==result['mask'])
 triples=[s['unsigned_triples'][i] for i in stratum['unsigned_indices']]
 rows=[[int(i//6==f) for i in range(12)] for f in range(2)]+[[t.count(i) for i in range(12)] for t in triples]
 assert rows==result['source_rows']
 positives=[]
 for test in result['tests']:
  candidate=next(x for x in d['candidates'] if x['index']==test['candidate'])
  assert [x['triple'] for x in test['rows']]==candidate['angle_triples']
  passed=True
  for check in test['rows']:
   target=[check['triple'].count(i) for i in range(12)]
   if 'coefficients' in check:
    q=list(map(F,check['coefficients']));assert len(q)==len(rows)
    assert [sum(a*r[j] for a,r in zip(q,rows)) for j in range(12)]==target
    assert sum(a*(4 if i<2 else 2) for i,a in enumerate(q))==2
   else:
    passed=False;z=list(map(F,check['separator']))
    assert all(sum(a*b for a,b in zip(r,z))==0 for r in rows)
    dot=sum(a*b for a,b in zip(target,z));assert dot and dot==F(check['dot'])
  assert passed==test['passes']
  if passed:positives.append(test['candidate'])
 assert positives==result['positive_candidates'] and result['selected_witness']==positives[0]
assert len(d['results'])==9 and sum(len(t['rows']) for r in d['results'] for t in r['tests'])==432
print('INDEPENDENT PASS: 113400 domains; 8 partitions; 6 tori; 432 exact augmented/separator tests')
