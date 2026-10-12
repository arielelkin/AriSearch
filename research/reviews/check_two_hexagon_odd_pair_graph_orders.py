#!/usr/bin/env python3
"""Independent full odd-pair census audit, loops/parallel edges included.
Graph generation uses permutations as oriented cycle covers, rather than
producer degree-budget search. No producer/solver imports or solver queries.
"""
import argparse,hashlib,itertools,json
from collections import Counter,defaultdict
from pathlib import Path
import importlib.util
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('own_ring_audit',HERE/'check_two_hexagon_balanced_root_cyclic_orders.py');own=importlib.util.module_from_spec(s);s.loader.exec_module(own)
ring,alg=own.ring,own.alg

def components(graph):
 adjacent={i:{i} for i in range(6)}
 for a,b in graph:adjacent[a].add(b);adjacent[b].add(a)
 remaining=set(range(6));sizes=[]
 while remaining:
  seen={min(remaining)};todo=list(seen)
  while todo:
   for b in adjacent[todo.pop()]:
    if b not in seen:seen.add(b);todo.append(b)
  remaining-=seen;sizes.append(len(seen))
 return tuple(sorted(sizes,reverse=True))
def allgraphs():
 return {tuple(sorted(tuple(sorted((i,p[i]))) for i in range(6))) for p in itertools.permutations(range(6))}
def cyclic_representatives(graph):
 counts=Counter(graph);words=[]
 def build(prefix):
  if len(prefix)==6:words.append(prefix);return
  for value in sorted(counts):
   if counts[value]:counts[value]-=1;build(prefix+(value,));counts[value]+=1
 build(());remaining=set(words);result=[]
 while remaining:
  word=min(remaining);reverse=word[::-1]
  orbit={word[k:]+word[:k] for k in range(6)}|{reverse[k:]+reverse[:k] for k in range(6)}
  assert orbit<=set(words);remaining-=orbit;result.append(word)
 return result

def check_order(row):
 T={tuple(sorted((*pair,6+i))) for i,pair in enumerate(row['B_pair_order'])};ring.T=T;rebuilt=[]
 for B in ring.A:
  _,solutions=ring.rings(B);rebuilt.extend((B,a) for a in solutions)
 stored=[own.statekey(state) for state in row['states']]
 assert set(stored)==set(rebuilt) and len(stored)==len(rebuilt)
 relations=[]
 for k in range(6):
  opposite=ring.add(ring.D[k],ring.D[(k+1)%6]);u=ring.D.index(ring.subtract(ring.D[k],opposite));v=ring.D.index(ring.subtract(ring.D[(k+1)%6],opposite))
  relation={(i,j) for i,a in enumerate(stored) for j,b in enumerate(stored) if a[1][k]==b[1][u] and a[1][(k+1)%6]==b[1][v]}
  assert relation==set(map(tuple,row['compatibility'][k]));relations.append(relation)
 alive=set(range(len(stored)));rounds=0
 for deletions in row['edge_deletion_rounds']:
  assert len({i for i,k in deletions})==len(deletions)
  for i,k in deletions:assert i in alive and not any(a==i and b in alive for a,b in relations[k])
  alive-={i for i,k in deletions};rounds+=1
 assert alive==set(row['edge_consistent_states'])
 for deletions in row['triangle_deletion_rounds']:
  assert len({i for i,k in deletions})==len(deletions)
  for i,k in deletions:
   assert i in alive
   J={b for a,b in relations[k] if a==i and b in alive};L={b for a,b in relations[(k+1)%6] if a==i and b in alive}
   assert not any((j,l) in relations[(k+2)%6] for j in J for l in L)
  alive-={i for i,k in deletions};rounds+=1
 assert alive==set(row['surviving_states'])
 degrees=[max((sum(a==i and b in alive for a,b in relation) for i in alive),default=0) for relation in relations]
 assert degrees==row['max_successor_degrees']
 verdict='EMPTY' if not alive else ('FUNCTIONAL' if min(degrees)<=1 else 'BRANCHING')
 assert row['verdict']==verdict
 return len(stored),rounds

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--metrics');ap.add_argument('--residue');args=ap.parse_args()
 path=Path('research/certificates/two-hexagon-odd-pair-graph-orders.json');raw=path.read_bytes();data=json.loads(raw)
 graphs=allgraphs();assert len(graphs)==data['all_pair_graphs']==388
 odd={g for g in graphs if any(n%2 for n in components(g))};assert len(odd)==data['odd_component_graphs']==268
 graphrows={tuple(map(tuple,g['edges'])):g for g in data['graphs']};assert set(graphrows)==odd and len(graphrows)==len(data['graphs'])
 families=Counter(components(g) for g in odd);assert len(families)==8
 ids={g['id']:tuple(map(tuple,g['edges'])) for g in data['graphs']};assert set(ids)==set(range(268))
 expected=set()
 for g,record in graphrows.items():
  assert components(g)==tuple(record['components'])
  # A loop contributes two incidences; each parallel occurrence contributes
  # separately. This validates actual pseudograph multiplicity, not sets.
  assert [sum(edge.count(i) for edge in g) for i in range(6)]==[2]*6
  words=cyclic_representatives(g);assert len(words)==record['cyclic_order_count']
  expected.update((record['id'],word) for word in words)
 actual={(r['graph_id'],tuple(map(tuple,r['B_pair_order']))) for r in data['rows']}
 assert actual==expected and len(actual)==len(data['rows'])==data['rooted_order_count']==11850
 states=rounds=0;family_stats=defaultdict(Counter)
 for i,row in enumerate(data['rows']):
  assert row['id']==i and tuple(sorted(map(tuple,row['B_pair_order'])))==ids[row['graph_id']]
  ns,nr=check_order(row);states+=ns;rounds+=nr;family_stats[components(ids[row['graph_id']])][row['verdict']]+=1
  if (i+1)%1000==0:print('independent orders checked',i+1,flush=True)
 stats=dict(Counter(row['verdict'] for row in data['rows']));assert stats==data['stats']=={'EMPTY':11739,'FUNCTIONAL':77,'BRANCHING':34}
 assert {'-'.join(map(str,k)):dict(v) for k,v in family_stats.items()}==data['component_stats']
 result={'status':'PASSED','all_degree_two_graphs':388,'odd_component_graphs':268,'component_family_counts':{'-'.join(map(str,k)):v for k,v in families.items()},'rooted_orders':11850,'stats':stats,'ring_states_checked':states,'valid_deletion_rounds':rounds,'source_sha256':hashlib.sha256(raw).hexdigest(),'scope':'All eight odd-component degree-two pair-graph families and their rooted B pair-value orders; metric escape coverage separate'}
 if args.metrics:
  mp=Path(args.metrics);mraw=mp.read_bytes();metric=json.loads(mraw);byid={r['id']:r for r in metric['rows']};covered=tori=branching=oldmaps=0;verdicts=Counter()
  residues={};residue_raw=b''
  if args.residue:
   residue_raw=Path(args.residue).read_bytes();residue=json.loads(residue_raw);residues={r['id']:r for r in residue['rows']}
  old_source_path=Path('research/certificates/two-hexagon-balanced-root-cyclic-orders.json');old_source_raw=old_source_path.read_bytes();old_source=json.loads(old_source_raw)
  old_metric_path=Path('research/certificates/two-hexagon-balanced-root-ring-metrics.json');old_metric_raw=old_metric_path.read_bytes();old_metric=json.loads(old_metric_raw);old_byid={r['id']:r for r in old_metric['rows']}
  for row in data['rows']:
   if row['verdict']!='BRANCHING':continue
   branching+=1;T={tuple(sorted((*p,6+i))) for i,p in enumerate(row['B_pair_order'])}
   if row['id'] in byid:
    queries=byid[row['id']]['queries']
   else:
    # Transfer an old two-triangle representative by an explicit native B
    # dihedral map. A coordinates and lattice coordinates stay fixed.
    pairs=list(map(tuple,row['B_pair_order']));matches=[]
    for old in old_source['rows']:
     if old['id'] not in old_byid:continue
     opairs=list(map(tuple,old['B_pair_order']))
     for r,s in ring.A:
      if all(opairs[i]==pairs[(r+s*i)%6] for i in range(6)):matches.append((old,r,s))
    assert matches,'Uncovered branching order';old,r,s=matches[0];oldmaps+=1
    cm=[(r+s*i)%6 for i in range(6)];sm=[alg.side_from_endpoints(cm,i) for i in range(6)]
    queries=[]
    for oq in old_byid[old['id']]['queries']:
     oclasses=tuple(oq['length_classes']);assert all(i in old['surviving_states'] and own.forced_metric(old['states'][i])[0]==oclasses for i in oq['state_indices'])
     oldE=[(i,j) for i in range(12) for j in range(i+1,12) if oclasses[i]==oclasses[j]]
     side_map=lambda x:x if x<6 else 6+sm[x-6]
     mappedE=[tuple(sorted((side_map(a),side_map(b)))) for a,b in oldE];_,C=alg.equality(mappedE)
     classes=tuple(min(comp) for i in range(12) for comp in C if i in comp)
     q={'length_classes':classes,'verdict':oq['verdict'],'torus_queries':[]}
     for trial in oq['torus_queries']:
      if 'labels' not in trial:continue
      transformed=[]
      for x,y,v in trial['labels']:
       if v>=12:
        pr,ps=ring.A[v-12];v=12+ring.A.index(((r+s*pr)%6,s*ps))
       transformed.append([x,y,v])
      q['torus_queries'].append({'lattice':trial['lattice'],'labels':transformed})
     queries.append(q)
   byclass={tuple(q['length_classes']):q for q in queries}
   required={own.forced_metric(row['states'][i])[0] for i in row['surviving_states']};assert required<=set(byclass)
   for classes in required:
    q=byclass[classes];Ec,_=alg.equality([(i,j) for i in range(12) for j in range(i+1,12) if classes[i]==classes[j]])
    if 'state_indices' in q:assert q['state_indices'] and all(i in row['surviving_states'] and own.forced_metric(row['states'][i])[0]==classes for i in q['state_indices'])
    trials=list(q['torus_queries'])
    if row['id'] in residues:
     residue=residues[row['id']];assert tuple(residue['length_classes'])==classes
     trials+=residue['torus_queries']
    witnesses=[trial for trial in trials if 'labels' in trial];assert witnesses,'No retained periodic witness for a required metric closure'
    for witness in witnesses:
     n,shear,m=witness['lattice'];lab={(x,y):v for x,y,v in witness['labels']};assert set(lab)=={(x,y) for x in range(n) for y in range(m)}
     U,E=alg.used(lab,(n,shear,m));assert U<=T and E<=Ec;tori+=1
    verdicts['PERIODIC_ESCAPE']+=1;covered+=1
  assert branching==34 and oldmaps==4 and covered==49 and tori==49
  result.update(metric_branching_orders_checked=branching,old_representatives_dihedrally_transferred=oldmaps,required_forced_metric_closures=covered,metric_verdicts=dict(verdicts),periodic_tori_checked=tori,metric_sha256=hashlib.sha256(mraw).hexdigest(),residue_sha256=hashlib.sha256(residue_raw).hexdigest(),old_census_sha256=hashlib.sha256(old_source_raw).hexdigest(),old_metric_sha256=hashlib.sha256(old_metric_raw).hexdigest())
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
