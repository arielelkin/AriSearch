"""Fixed 6P4Q native-edge flat torus, capped CP-SAT; no larger domains."""
import argparse,itertools,json,time
from collections import Counter
from pathlib import Path
from ortools.sat.python import cp_model
P=[(0,0),(2,0),(3,2),(2,3),(0,2)]
Q=[(2,3),(1,4),(-1,4),(-2,3),(0,2)]
FACES=[P]*6+[Q]*4
WORDS=['rabba']*6+['cggcd']*4
STARS=['rgg']*2+['aad']*4+['bbcc']*4+['abg']*4+['rrrr']
LABELS=[WORDS[f][i] for f in range(10) for i in range(5)]
ANGLES={'r':(2,0),'a':(4,-1),'b':(1,1),'c':(3,-1),'g':(3,0),'d':(0,2)}
def edge_length(e):
 f,i=divmod(e,5);a,b=FACES[f][i],FACES[f][(i+1)%5]
 return sum((x-y)**2 for x,y in zip(a,b))
def nxt(c):return 5*(c//5)+(c+1)%5
def validation(pairs,vertices):
 mate={a:b for a,b in pairs for a,b in [(a,b),(b,a)]}
 assert len(mate)==50 and all(edge_length(a)==edge_length(b) for a,b in pairs)
 assert all(vertices[a]==vertices[nxt(b)] and vertices[nxt(a)]==vertices[b] for a,b in pairs)
 successor={c:nxt(mate[c]) for c in range(50)}
 seen=set();cycles=[]
 for c in range(50):
  if c in seen:continue
  cy=[];v=c
  while v not in seen:seen.add(v);cy.append(v);v=successor[v]
  assert v==c
  cycles.append(cy)
 goodlinks=len(cycles)==15 and all(len({vertices[c] for c in cy})==1 and
   Counter(LABELS[c] for c in cy)==Counter(STARS[vertices[cy[0]]]) for cy in cycles)
 adj={f:set() for f in range(10)}
 for a,b in pairs:adj[a//5].add(b//5);adj[b//5].add(a//5)
 reached={0};pending=[0]
 while pending:
  for f in adj[pending.pop()]-reached:reached.add(f);pending.append(f)
 connected=len(reached)==10
 return {'valid':goodlinks and connected,'corner_cycles':cycles,'connected':connected,'V':len(cycles),'E':25,'F':10}
def run(output,cap=120,max_rejected=100):
 start=time.monotonic();model=cp_model.CpModel()
 domains={t:[v for v,star in enumerate(STARS) if t in star] for t in ANGLES}
 ids=[];at={}
 for c,t in enumerate(LABELS):
  vid=model.new_int_var_from_domain(cp_model.Domain.from_values(domains[t]),'v%d'%c);ids.append(vid)
  for v in domains[t]:
   b=model.new_bool_var('c%d_at%d'%(c,v));at[c,v]=b
   model.add(vid==v).only_enforce_if(b);model.add(vid!=v).only_enforce_if(b.Not())
 for v,star in enumerate(STARS):
  for t,n in Counter(star).items():model.add(sum(at[c,v] for c in range(50) if LABELS[c]==t)==n)
 # Sound face/vertex permutation symmetry: P's unique R appears at both RGG
 # vertices once and four times at RRRR. Q's unique D labels the four AADs.
 for f,v in enumerate([0,1,14,14,14,14]):model.add(ids[5*f]==v)
 for f in range(6,10):model.add(ids[5*f+4]==f-4)
 choices={};incident={e:[] for e in range(50)}
 for a in range(50):
  for b in range(a+1,50):
   if edge_length(a)!=edge_length(b):continue
   decision=model.new_bool_var('pair_%d_%d'%(a,b));choices[a,b]=decision
   incident[a].append(decision);incident[b].append(decision)
   model.add(ids[a]==ids[nxt(b)]).only_enforce_if(decision)
   model.add(ids[nxt(a)]==ids[b]).only_enforce_if(decision)
 for e in range(50):model.add_exactly_one(incident[e])
 solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
 solver.parameters.random_seed=20261014
 rejected=0;history=[];witness=None;last='UNKNOWN';reason='wall_cap'
 while time.monotonic()-start<cap:
  solver.parameters.max_time_in_seconds=max(0.001,cap-(time.monotonic()-start))
  status=solver.solve(model);last=solver.status_name(status)
  history.append({'status':last,'wall_time':solver.wall_time,'conflicts':solver.num_conflicts,'branches':solver.num_branches})
  if status==cp_model.INFEASIBLE:reason='proved_infeasible_fixed_domain';break
  if status not in (cp_model.OPTIMAL,cp_model.FEASIBLE):reason='solver_cap_or_unknown';break
  pairs=[list(k) for k,v in choices.items() if solver.boolean_value(v)]
  vertices=[solver.value(v) for v in ids];check=validation(pairs,vertices)
  if check['valid']:
   witness={'pairs':pairs,'corner_vertex_ids':vertices,'validation':check};reason='valid_flat_torus';break
  rejected+=1
  if rejected>=max_rejected:reason='rejected_assignment_cap';last='UNKNOWN';break
  model.add(sum(choices[tuple(pair)] for pair in pairs)<=24)
 if witness is None and reason=='wall_cap':last='UNKNOWN'
 result={'schema':'Y_NATIVE_EDGE_TORUS_V1','domain':{'P_faces':6,'Q_faces':4,'native_sides':50,'stars':STARS,'canonical_chirality':'P reflection y=x; Q reflection x=0; reflected placements equivalent by native reversal'},
 'caps':{'wall_seconds':cap,'max_rejected_assignments':max_rejected,'workers':1,'seed':20261014},
 'status':'SAT_VALID_FLAT_TORUS' if witness else last,'stop_reason':reason,'elapsed_seconds':time.monotonic()-start,
 'rejected_assignments':rejected,'solver_version':__import__('ortools').__version__,'history':history,'witness':witness,
 'scope':'fixed full-native-edge 6P4Q torus only; UNKNOWN is not exclusion'}
 Path(output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',default='research/certificates/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.json');ap.add_argument('--check')
 args=ap.parse_args()
 if args.check:
  cert=json.loads(Path(args.check).read_text())
  assert cert['schema']=='Y_NATIVE_EDGE_TORUS_V1'
  assert (cert['domain']['P_faces'],cert['domain']['Q_faces'],cert['domain']['native_sides'])==(6,4,50)
  assert cert['domain']['stars']==STARS
  assert cert['caps']=={'wall_seconds':120,'max_rejected_assignments':100,'workers':1,'seed':20261014}
  assert Counter(LABELS)==Counter(''.join(STARS))
  assert len(FACES)==10 and len(LABELS)==50
  assert set((y,x) for x,y in P)==set(P)
  assert set((-x,y) for x,y in Q)==set(Q)
  assert cert['rejected_assignments']<=100
  if cert['witness'] is not None:
   check=validation(cert['witness']['pairs'],cert['witness']['corner_vertex_ids']);assert check['valid'];print(json.dumps(check,indent=2))
  else:
   assert cert['status']=='INFEASIBLE' and cert['stop_reason']=='proved_infeasible_fixed_domain'
   assert cert['history'] and cert['history'][-1]['status']=='INFEASIBLE'
   assert cert['elapsed_seconds']>=0 and all(row['wall_time']>=0 for row in cert['history'])
   import runpy
   runpy.run_path(str(Path(__file__).resolve().parents[1]/'reviews'/'pentagon-y-no-full-edge-independent-2026-10-14.py'),run_name='__main__')
   print('PASS: retained fixed-domain negative metadata and independent native-propagation proof; no solver rerun or formal UNSAT certificate claim')
 else:run(args.output)
