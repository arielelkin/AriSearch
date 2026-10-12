#!/usr/bin/env python3
"""Independent exact ring/pruning/metric escape audit; no solver calls."""
import argparse,hashlib,importlib.util,itertools,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ring=load('canonical_ring_audit',HERE/'check_two_hexagon_balanced_rank_five_ring.py')
alg=load('affine_escape_audit',HERE/'two-hexagon-inherited-escape-check.py')
def statekey(state):return tuple(state['B']),tuple(state['A_ring'])
def forced_metric(state):
 labels={(0,0):12+ring.A.index(tuple(state['B']))}
 labels.update({ring.D[k]:a for k,a in enumerate(state['A_ring'])});E=set()
 for z,w in itertools.combinations(labels,2):
  delta=ring.subtract(w,z)
  if delta in ring.D:
   k=(ring.D.index(delta)-1)%6
   a,b=alg.side(labels[z],k),alg.side(labels[w],(k+3)%6)
   if a!=b:E.add(tuple(sorted((a,b))))
 Ec,components=alg.equality(E)
 classes=tuple(min(C) for i in range(12) for C in components if i in C)
 return classes,Ec

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
 sp=Path('research/certificates/two-hexagon-balanced-root-cyclic-orders.json');raw=sp.read_bytes();data=json.loads(raw)
 expected=set()
 for group in itertools.combinations(range(6),3):
  if 0 not in group:continue
  other=tuple(x for x in range(6) if x not in group);edges=list(itertools.combinations(group,2))+list(itertools.combinations(other,2))
  for p in itertools.permutations(range(1,6)):
   if p[0]>=p[-1]:continue
   expected.add((group,other,tuple(edges[i] for i in (0,)+p)))
 actual={(tuple(r['A_groups'][0]),tuple(r['A_groups'][1]),tuple(map(tuple,r['B_pair_order']))) for r in data['rows']}
 assert actual==expected and len(actual)==len(data['rows'])==data['rooted_order_count']==600
 functional=[];branches=[];empty=[];stateschecked=0;roundschecked=0
 for index,row in enumerate(data['rows']):
  assert row['id']==index
  T={tuple(sorted(t)) for t in row['T']};assert T=={tuple(sorted((*pair,6+i))) for i,pair in enumerate(row['B_pair_order'])}
  ring.T=T;rebuilt=[]
  for B in ring.A:
   constraints,solutions=ring.rings(B);rebuilt.extend((B,a) for a in solutions)
  stored=[statekey(s) for s in row['states']];assert set(stored)==set(rebuilt) and len(stored)==len(rebuilt);stateschecked+=len(stored)
  relations=[]
  for k in range(6):
   opposite=ring.add(ring.D[k],ring.D[(k+1)%6]);u=ring.D.index(ring.subtract(ring.D[k],opposite));v=ring.D.index(ring.subtract(ring.D[(k+1)%6],opposite))
   rel={(i,j) for i,a in enumerate(stored) for j,b in enumerate(stored) if a[1][k]==b[1][u] and a[1][(k+1)%6]==b[1][v]}
   assert rel==set(map(tuple,row['compatibility'][k]));relations.append(rel)
  alive=set(range(len(stored)))
  for deletes in row['deletion_rounds']:
   assert len({i for i,k in deletes})==len(deletes)
   for i,k in deletes:assert i in alive and not any(a==i and b in alive for a,b in relations[k])
   alive-={i for i,k in deletes};roundschecked+=1
  assert alive==set(row['edge_consistent_states'])
  for deletes in row['triangle_deletion_rounds']:
   assert len({i for i,k in deletes})==len(deletes)
   for i,k in deletes:
    assert i in alive
    J={b for a,b in relations[k] if a==i and b in alive};L={b for a,b in relations[(k+1)%6] if a==i and b in alive}
    # Adjacent B-step difference is the next-next B direction.
    step=lambda t:ring.add(ring.D[t%6],ring.D[(t+1)%6])
    assert ring.subtract(step(k+1),step(k))==step(k+2)
    assert not any((j,l) in relations[(k+2)%6] for j in J for l in L)
   alive-={i for i,k in deletes};roundschecked+=1
  assert alive==set(row['surviving_states']) and row['verdict']==('SURVIVOR' if alive else 'EMPTY')
  if not alive:empty.append(row['id']);continue
  maxima=[max(sum(a==i and b in alive for a,b in rel) for i in alive) for rel in relations]
  if any(d<=1 for d in maxima):functional.append(row['id'])
  else:branches.append(row['id'])
 assert dict(Counter(r['verdict'] for r in data['rows']))==data['stats']
 assert len(empty)==581 and len(functional)==15 and branches==[0,209,349,549]
 mp=Path('research/certificates/two-hexagon-balanced-root-ring-metrics.json');mraw=mp.read_bytes();metrics=json.loads(mraw);byid={r['id']:r for r in metrics['rows']};covered=0;tori=0
 for rid in branches:
  row=data['rows'][rid];queries=byid[rid]['queries'];byclass={tuple(q['length_classes']):q for q in queries}
  required={forced_metric(row['states'][i])[0] for i in row['surviving_states']}
  assert required<=set(byclass)
  T={tuple(sorted(t)) for t in row['T']}
  for classes in required:
   q=byclass[classes];assert q['verdict']=='PERIODIC_ESCAPE';Ec,C=alg.equality([(i,j) for i in range(12) for j in range(i+1,12) if classes[i]==classes[j]])
   ids=q['state_indices'];assert ids and all(i in row['surviving_states'] and forced_metric(row['states'][i])[0]==classes for i in ids)
   assert {tuple(sorted(p)) for p in q['one_ring_equalities'] if p[0]!=p[1]}<=Ec
   witnesses=[trial for trial in q['torus_queries'] if 'labels' in trial];assert witnesses
   for trial in witnesses:
    n,s,m=trial['lattice'];lab={(x,y):a for x,y,a in trial['labels']};assert set(lab)=={(x,y) for x in range(n) for y in range(m)}
    U,E=alg.used(lab,(n,s,m));assert U<=T and E<=Ec;tori+=1
   covered+=1
 assert covered==19
 result={'status':'PASSED','rooted_orders':600,'ring_states_checked':stateschecked,'valid_deletion_rounds':roundschecked,'empty_order_count':len(empty),'functional_order_count':len(functional),'functional_ids':functional,'branching_ids':branches,'forced_metric_closures_covered':covered,'periodic_tori_independently_checked':tori,'source_sha256':hashlib.sha256(raw).hexdigest(),'metric_sha256':hashlib.sha256(mraw).hexdigest(),'scope':'600 stated rooted native orders only; exact local exclusions plus conditional functional periodicity or forced-metric torus escape'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
