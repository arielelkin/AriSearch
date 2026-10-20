"""Bounded exact angle inventory; no inference of tilability."""
import itertools,json,collections
from pathlib import Path
import z3
Ps=[x for x in itertools.combinations_with_replacement(range(95,121,5),5) if sum(x)==540]
Qs=[x for x in itertools.combinations_with_replacement(range(120,151,5),7) if sum(x)==900]
records=[];selected=[];stats=collections.Counter()
for P in Ps:
 for Q in Qs:
  if (P,Q)==((100,100,110,115,115),(125,125,125,130,130,130,135)):continue
  labels=[('P',a) for a in sorted(set(P))]+[('Q',a) for a in sorted(set(Q))]
  stars=[t for t in itertools.combinations_with_replacement(range(len(labels)),3) if sum(labels[i][1] for i in t)==360]
  target=[(P if typ=='P' else Q).count(a) for typ,a in labels]
  if any(not any(i in t for t in stars) for i in range(len(labels))):stats['unused-angle']+=1;continue
  counts=[[t.count(i) for t in stars] for i in range(len(labels))]
  s=z3.Solver();x=[z3.Real('x%d'%j) for j in range(len(stars))]
  s.add(*[v>=0 for v in x]);s.add(*[z3.Sum([c*v for c,v in zip(row,x)])==b for row,b in zip(counts,target)])
  if s.check()!=z3.sat:stats['rational-infeasible']+=1;continue
  stats['rational-feasible']+=1
  weights=[str(s.model().eval(v)) for v in x]
  small=[]
  for n in (1,2):
   si=z3.Solver();y=[z3.Int('y%d'%j) for j in range(len(stars))];si.add(*[v>=0 for v in y]);si.add(*[z3.Sum([c*v for c,v in zip(row,y)])==n*b for row,b in zip(counts,target)])
   small.append(str(si.check()))
  if P==(95,105,110,115,115) and Q==(125,125,125,125,130,130,140):selected.append(dict(P=P,Q=Q,labels=labels,stars=[[labels[i] for i in t] for t in stars],rational_weights=weights,one_and_two_each=small))
  if small[1]=='unsat':records.append(dict(P=P,Q=Q,labels=labels,stars=[[labels[i] for i in t] for t in stars],rational_weights=weights,one_and_two_each=small))
out=dict(domain='P nondecreasing 5 entries from 95..120 step5 sum540; Q nondecreasing 7 entries from120..150 step5 sum900; exclude previous fixed palette; typed angle triples sum360. Rational nonnegative stars match one P+one Q. Integer stars tested one and two of each.',pairs=len(Ps)*len(Qs)-1,stats=dict(stats),four_face_inventory_obstructions=records,selected_palette=selected,z3=z3.get_version_string())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
