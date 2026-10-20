#!/usr/bin/env sage-python
"""Complete rational affine closure census of the 16 unsigned star equations.
No metric, torus, plane extension, or deeper corona search is performed.
"""
import argparse,importlib.util,json,sys
from sage.env import SAGE_VERSION
from collections import Counter,deque
from pathlib import Path
from sage.all import QQ,matrix,vector
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('atlas',R/'searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,1,2,0,3,1));stars=[tuple(map(tuple,t)) for t in r['fixed_stars']]
triples=sorted(set(tuple(sorted(p[0] for p in t)) for t in stars))
assert len(stars)==32 and len(triples)==16 and len(r['boundary_coronas'])==100
lifts=[[i for i,t in enumerate(stars) if tuple(sorted(p[0] for p in t))==u] for u in triples]
assert all(len(g)==2 for g in lifts)
# Translate alpha_i to x_i=alpha_i-2/3. All equations are homogeneous.
totals=[vector(QQ,[int(i//6==f) for i in range(12)]) for f in range(2)]
rows=[vector(QQ,[u.count(i) for i in range(12)]) for u in triples]
assert all(sum(row)*QQ(2)/3==2 for row in rows)
cache={}
def close(mask):
 if mask in cache:return cache[mask]
 V=matrix(QQ,totals+[rows[i] for i in range(16) if mask>>i&1]).row_space()
 out=sum(1<<i for i,row in enumerate(rows) if row in V)
 cache[mask]=out
 return out
# Enumerate every flat by closure under single-element extension. Every
# subset is reached through its ordered generators, so none of 2^16 is lost.
start=close(0);seen={start};queue=deque([start]);extensions=0
while queue:
 mask=queue.popleft()
 for i in range(16):
  if not(mask>>i&1):
   extensions+=1;c=close(mask|1<<i)
   if c not in seen:seen.add(c);queue.append(c)
# Independent exhaustive coverage of all 65536 masks by nearest-flat DP:
# closure(M)=closure(closure(M without highest bit) union highest bit).
allclosures=[start]*65536
for mask in range(1,65536):
 bit=mask&-mask;allclosures[mask]=close(allclosures[mask^bit]|bit)
assert set(allclosures)==seen

def sides(p):
 c,h=p;f,j=divmod(c,6)
 return (c,6*f+(j+1)%6) if h==1 else (6*f+(j+1)%6,c)
requirements=[[] for _ in stars]
for x in r['endpoint_microstates']:
 k=stars.index(tuple(map(tuple,x['star'])))
 requirements[k].append(sum(1<<stars.index(tuple(map(tuple,t))) for t in x['opposite_stars']))
cover=[sum(1<<i for i,t in enumerate(stars) if any(p[0]==c for p in t)) for c in range(12)]
factors=[{} for _ in range(5)]
for k,t in enumerate(stars):
 for i,p in enumerate(t):
  prev,nxt=t[(i-1)%3],t[(i+1)%3]
  if p[1]==1 and 0<=p[0]<=3:
   pair=((sides(prev)[1],prev[1]),(sides(nxt)[0],nxt[1]));a=p[0]+1
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
  if p==(4,1) and nxt==(5,1):
   q=t[(i+2)%3];pair=((sides(q)[1],q[1]),(sides(q)[0],q[1]));a=0
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
corona_groups=[[factors[j%5][(tuple(c[j]),tuple(c[j+1]))] for j in range(10)] for c in r['boundary_coronas']]
pure=[triples.index(t) for t in ((0,1,2),(3,4,5),(6,7,8),(9,10,11))]
records=[]
for mask in sorted(seen):
 ids=[j for i,g in enumerate(lifts) if mask>>i&1 for j in g]
 signed=sum(1<<j for j in ids);active=signed;rounds=[]
 while True:
  nxt=sum(1<<j for j in range(32) if active>>j&1 and all(active&g for g in requirements[j]))
  if nxt==active:break
  rounds.append([j for j in range(32) if (active^nxt)>>j&1]);active=nxt
 covered=all(active&g for g in cover)
 coronas=[i for i,gs in enumerate(corona_groups) if all(active&g for g in gs)]
 pure_present=[triples[i] for i in pure if mask>>i&1]
 opts={}
 for j,t in enumerate(stars):
  if not(active>>j&1):continue
  for i,p in enumerate(t):
   q=t[(i+1)%3]
   opts.setdefault((sides(p)[1],p[1]),set()).add((sides(q)[0],q[1]))
 table=[dict(source=list(k),alternatives=[list(v) for v in sorted(vs)]) for k,vs in sorted(opts.items())]
 deterministic=len(opts)==24 and all(len(v)==1 for v in opts.values())
 if deterministic:
  M={k:next(iter(v)) for k,v in opts.items()};assert all(M.get(M[k])==k for k in M)
 if pure_present:status='pure_triple_monohedral_escape'
 elif not covered:status='fails_necessary_full_corner_cover'
 elif not coronas:status='fails_necessary_formal_corona'
 elif deterministic:status='deterministic_conditional_periodic_escape'
 else:status='uncovered_branching'
 V=matrix(QQ,totals+[rows[i] for i in range(16) if mask>>i&1]).row_space()
 # Retain exact normalized x-equations, enough to verify row-span closure.
 rec=dict(unsigned_mask=mask,unsigned_indices=[i for i in range(16) if mask>>i&1],signed_indices=sorted(ids),active_signed_indices=[i for i in range(32) if active>>i&1],seam_pruning_rounds=rounds,angle_dimension=12-int(V.dimension()),rref_x=[[str(v) for v in row] for row in V.basis_matrix()],pure_triples= pure_present,full_corner_cover=covered,formal_corona_indices=coronas,status=status)
 if covered and coronas and not pure_present:
  rec['signed_neighbor_table']=table
  rec['branching_states']=[t for t in table if len(t['alternatives'])>1]
 records.append(rec)
summary=dict(closed_angle_spaces=len(records),subset_domain=65536,closure_extension_calls=extensions,closure_cache_size=len(cache),status_counts=dict(Counter(t['status'] for t in records)),necessary_filter_survivors=sum(t['full_corner_cover'] and bool(t['formal_corona_indices']) for t in records),no_pure_necessary_survivors=sum(t['full_corner_cover'] and bool(t['formal_corona_indices']) and not t['pure_triples'] for t in records))
out=dict(software=dict(python=sys.version.split()[0],sage=SAGE_VERSION),schema='THIRTYTWO_RESONANCE_STRATA_SOL_V1',A=list(m.A),B=r['B'],angle_units='pi',unsigned_triples=triples,signed_lifts=lifts,strict_angle_feasibility='Every closed affine space contains alpha=(2/3)^12, strictly between0 and1. Exact strata avoid finitely many proper hyperplanes; finite rational perturbations preserve strictness. This does not establish polygon or common-length metric closure.',enumeration='All 65536 subsets, rational affine row-span closure modulo both polygon totals; no symmetry quotient.',summary=summary,strata=records,scope='Necessary ETE trivalent angle-atlas strata with full species corner cover. Monohedral omissions are screened separately. Formal coronas are necessary only; no finite-to-plane inference.',stopping_state='Branching residuals have no identified new global invariant; stop under protocol5 without metric feasibility, larger corona, or torus search.')
parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
path=R/'certificates/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.json'
if args.check:assert json.loads(path.read_text())==json.loads(json.dumps(out))
else:path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
