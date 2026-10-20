#!/usr/bin/env python
"""Independent exact reconstruction; imports neither producer nor atlas builder."""
import itertools as it,json
from collections import Counter
from pathlib import Path
from sage.all import QQ,matrix,vector
R=Path(__file__).resolve().parents[1]
cert=json.loads((R/'certificates/hexagon-thirtytwo-resonance-strata-sol-2026-10-19.json').read_text())
W=((0,1,2,0,3,4),(0,1,2,0,3,1))
def ends(p):
 c,h=p;f,j=divmod(c,6);a=(c,6*f+(j+1)%6)
 return a if h==1 else a[::-1]
def color(s):return W[s//6][s%6]
def cycle(t):return min(t,t[1:]+t[:1],t[2:]+t[:2])
def remote(p,s):
 c,h=p;f,j=divmod(s,6)
 return (6*f+((j-1)%6 if c==s else j),h)
S={cycle(t) for t in it.product(it.product(range(12),(1,-1)),repeat=3) if all(color(ends(t[k])[1])==color(ends(t[(k+1)%3])[0]) for k in range(3))}
def partners(t,k,U):
 p,q=t[k],t[(k+1)%3]
 pair=(remote(q,ends(q)[0]),remote(p,ends(p)[1]))
 return {u for u in U if any((u[j],u[(j+1)%3])==pair for j in range(3))}
while True:
 N={t for t in S if all(partners(t,k,S) for k in range(3))}
 if N==S:break
 S=N
stars=sorted(S);assert len(stars)==32
triples=sorted({tuple(sorted(p[0] for p in t)) for t in S})
assert triples==list(map(tuple,cert['unsigned_triples'])) and len(triples)==16
lifts=[[j for j,t in enumerate(stars) if tuple(sorted(p[0] for p in t))==u] for u in triples]
assert lifts==cert['signed_lifts'] and all(len(x)==2 for x in lifts)
# Independently enumerate canonical exact row spaces, rather than closed-mask BFS.
totals=[vector(QQ,[int(j//6==f) for j in range(12)]) for f in range(2)]
rows=[vector(QQ,[int(j in u) for j in range(12)]) for u in triples]
def basis(rs):return tuple(tuple(r) for r in matrix(QQ,rs).rref().rows() if any(r))
base=basis(totals);spaces=[base]*65536;transition={}
for mask in range(1,65536):
 bit=mask.bit_length()-1;old=spaces[mask^(1<<bit)];key=(old,bit)
 if key not in transition:transition[key]=basis(list(old)+[rows[bit]])
 spaces[mask]=transition[key]
unique=set(spaces);assert len(unique)==628
by_mask={}
for b in unique:
 V=matrix(QQ,b).row_space();closed=sum(1<<i for i,r in enumerate(rows) if r in V)
 assert closed not in by_mask;by_mask[closed]=b
assert set(by_mask)=={r['unsigned_mask'] for r in cert['strata']}
# Regenerate all ten-boundary cyclic chains from star incidences.
factors=[{} for _ in range(5)]
for n,t in enumerate(stars):
 for k,p in enumerate(t):
  left,right=t[(k-1)%3],t[(k+1)%3]
  if p[1]==1 and p[0]<4:
   a=p[0]+1;pair=((ends(left)[1],left[1]),(ends(right)[0],right[1]))
   factors[a].setdefault(pair,set()).add(n)
  if p==(4,1) and right==(5,1):
   q=t[(k+2)%3];pair=((ends(q)[1],q[1]),(ends(q)[0],q[1]))
   factors[0].setdefault(pair,set()).add(n)
chains=[(a,b) for a,b in sorted(factors[0])]
for k in range(1,10):chains=[c+(b,) for c in chains for a,b in sorted(factors[k%5]) if c[-1]==a]
coronas=[c for c in chains if c[-1]==c[0]];assert len(coronas)==100
counts=Counter();branch=[];support=set();filter_count=0
for rec in cert['strata']:
 mask=rec['unsigned_mask'];b=by_mask[mask]
 assert rec['rref_x']==[[str(x) for x in r] for r in b]
 assert rec['angle_dimension']==12-len(b)>=4
 active={j for i,g in enumerate(lifts) if mask>>i&1 for j in g};rounds=[]
 assert sorted(active)==rec['signed_indices']
 while True:
  U={stars[j] for j in active};nxt={j for j in active if all(partners(stars[j],k,U) for k in range(3))}
  if nxt==active:break
  rounds.append(sorted(active-nxt));active=nxt
 assert rounds==rec['seam_pruning_rounds'] and sorted(active)==rec['active_signed_indices']
 covered={p[0] for j in active for p in stars[j]}==set(range(12))
 cis=[i for i,c in enumerate(coronas) if all(active & factors[k%5][(c[k],c[k+1])] for k in range(10))]
 assert covered==rec['full_corner_cover'] and cis==rec['formal_corona_indices']
 pure=[u for u in triples if len({x//6 for x in u})==1 and u in [(0,1,2),(3,4,5),(6,7,8),(9,10,11)] and mask>>triples.index(u)&1]
 assert list(map(list,pure))==rec['pure_triples']
 opts={}
 for j in active:
  t=stars[j]
  for k,p in enumerate(t):
   q=t[(k+1)%3];opts.setdefault((ends(p)[1],p[1]),set()).add((ends(q)[0],q[1]))
 table=[dict(source=list(k),alternatives=list(map(list,sorted(v)))) for k,v in sorted(opts.items())]
 deterministic=len(opts)==24 and all(len(v)==1 for v in opts.values())
 if deterministic:
  M={k:next(iter(v)) for k,v in opts.items()};assert all(M[M[k]]==k for k in M)
 status='pure_triple_monohedral_escape' if pure else 'fails_necessary_full_corner_cover' if not covered else 'fails_necessary_formal_corona' if not cis else 'deterministic_conditional_periodic_escape' if deterministic else 'uncovered_branching'
 assert status==rec['status'];counts[status]+=1;filter_count+=bool(covered and cis)
 if not pure and covered and cis:
  assert table==rec['signed_neighbor_table']
  bs=[x for x in table if len(x['alternatives'])>1];assert bs==rec['branching_states']
  if deterministic:support.add(tuple(sorted(active)))
  else:branch.append((mask,12-len(b),len(rec['signed_indices']),len(cis),len(bs)))
assert dict(counts)==cert['summary']['status_counts'] and filter_count==99
assert branch==[(3162,6,12,4,8),(3778,6,12,4,8),(3802,5,16,9,14),(3814,5,16,4,8),(27672,6,12,1,10),(27714,6,12,1,12),(27738,5,16,4,16),(27750,5,16,1,12),(27836,5,18,1,10)]
minimal=[x[0] for x in branch if not any(y[0]!=x[0] and y[0]&x[0]==y[0] for y in branch)]
assert [(r['unsigned_mask'],len(r['active_signed_indices'])) for r in cert['strata'] if r['status']=='uncovered_branching']==[(3162,12),(3778,12),(3802,16),(3814,12),(27672,12),(27714,12),(27738,16),(27750,12),(27836,12)]
assert minimal==[3162,3778,27672,27714] and len(support)==3
print('PASS: independent atlas, 65536 exact row spaces, 628 strata, pruning, 100 coronas, 13 deterministic tables and nine residuals')
print(dict(counts));print('deterministic supports:',sorted(support))
