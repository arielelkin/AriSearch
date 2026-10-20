#!/usr/bin/env python3
"""Independent audit of a completed one-cut gate; no construction traversal."""
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict, Counter
from fractions import Fraction
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parents[2]
source=root/'research/searches/one-t-junction-substitution-sol-2026-10-19.json'
cert=json.loads((root/'research/searches/one-t-affine-state-gate-sol-2026-10-19.json').read_text())
assert hashlib.sha256(source.read_bytes()).hexdigest()==cert['input_sha256']=='33d0b6da814916e886daa93daee3b095519749120e42b0eaabfe6e84e550a47b'
m=json.loads(source.read_text())['maps']['P'][0]
# Independently reconstruct native words from expanded polygons, rather than
# trusting the implementer's incidence table source.
native={v:[x for x in word if not (v==m['host'] and x==m['flat'])] for v,word in m['expanded_words'].items()}
assert native==m['corner_words']
children=tuple(sorted(native));assert len(children)==13
assert Counter(m['species'].values())=={'P':11,'Q':2}
for v,word in native.items():assert len(word)==(5 if m['species'][v]=='P' else 7)
inc=defaultdict(list)
for v in children:
 for k,x in enumerate(native[v]):inc[x].append((v,k))
all_scores=[]
for n in range(1,len(children)):
 for sub in combinations(children,n):
  selected=set(sub)
  frontier=[x for x,slots in inc.items() if 0<sum(v in selected for v,k in slots)<len(slots)]
  domain=1
  for v in sub:domain*=2*len(native[v])
  all_scores.append((len(frontier),domain,n,sub))
assert len(all_scores)==8190
best=min(all_scores)
assert best==(3,10,1,('e0',))
assert list(best[:3])+[list(best[3])]==cert['selection_score']
selected=set(best[3]);frontier=sorted(x for x,slots in inc.items() if 0<sum(v in selected for v,k in slots)<len(slots))
complete=sorted(x for x,slots in inc.items() if all(v in selected for v,k in slots))
assert frontier==cert['frontier_nodes']==['f16','t0','t1']
assert complete==cert['completed_nodes']==['u1','u2']
assert cert['assigned_children']==['e0']
assert cert['remaining_children']==[v for v in children if v!='e0']
assert len(cert['entries'])==10
assert sorted(tuple(e['assignment']['e0']) for e in cert['entries'])==sorted(product(range(5),[-1,1]))
a=list(map(Fraction,cert['strict_partial_certificate']))
assert a==[Fraction(3,5)]*5+[Fraction(5,7)]*7
assert all(0<x<1 for x in a)
signatures=[]
for entry in cert['entries']:
 p,e=entry['assignment']['e0'];assert p in range(5) and e in [-1,1]
 rows=[[1]*5+[0]*7+[3],[0]*5+[1]*7+[5]]
 for x in complete:
  row=[0]*13
  for v,k in inc[x]:
   assert v=='e0';row[(p+e*k)%5]+=1
  if x in m['parent_corner_roles']:row[m['parent_corner_roles'][x]]-=1
  else:row[-1]=1 if x.startswith('t') or x==m['flat'] else 2
  rows.append(row)
 assert all(sum(Fraction(c)*v for c,v in zip(row[:12],a))==row[-1] for row in rows)
 reduced=S.Matrix(rows).rref()[0]
 reduced=[list(row) for row in reduced.tolist() if any(row)]
 assert reduced==[[S.Rational(x) for x in row] for row in entry['rref']]
 boundary=[[x,[[v,k,(p+e*k)%5] for v,k in inc[x] if v in selected]] for x in frontier]
 assert boundary==entry['unfinished_native_incidences']
 signatures.append(tuple((x,tuple(tuple(t) for t in slots)) for x,slots in boundary))
assert len(set(signatures))==10
assert cert['raw_prefix_count']==cert['distinct_exact_states']==10
assert cert['maximum_multiplicity']==1
assert cert['status']=='STOP_NO_NONTRIVIAL_MERGING'
assert cert['full_parent_cover'] is False and cert['shared_parent_witness'] is False
print('PASS independent: native reconstruction; 8190 cuts; minimum (3,10,1,e0); 10 distinct exact states; all strict partial certificates')
