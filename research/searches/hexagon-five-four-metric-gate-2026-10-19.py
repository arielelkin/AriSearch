#!/usr/bin/env python3
"""Exact fixed-word support gate. UNKNOWN stops metric work; no plane assertion."""
import importlib.util,itertools,json,time,hashlib
from pathlib import Path
import sympy as S
import z3 as Z
base=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',base/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,1,1,0,2,3));stars=[tuple(map(tuple,t)) for t in r['fixed_stars']];n=len(stars)
M=S.Matrix([[0,1,-1,-1,1],[0,1,1,-1,-1],[0,0,-1,1,0],[0,2,-1,-1,0]])
assert M.nullspace()==[S.Matrix([1,0,0,0,0]),S.Matrix([0,1,1,1,1])]
def sides(p):
 c,h=p;f,j=divmod(c,6);return (6*f+j,6*f+(j+1)%6) if h==1 else (6*f+(j+1)%6,6*f+j)
requirements=[[] for _ in stars]
for x in r['endpoint_microstates']:
 i=stars.index(tuple(map(tuple,x['star'])))
 requirements[i].append(sum(1<<stars.index(tuple(map(tuple,t))) for t in x['opposite_stars']))
cover=[sum(1<<i for i,t in enumerate(stars) if any(p[0]==c for p in t)) for c in range(12)]
factors=[{} for _ in range(5)]
for k,t in enumerate(stars):
 for i,p in enumerate(t):
  prev=t[(i-1)%3];nxt=t[(i+1)%3]
  if p[1]==1 and 0<=p[0]<=3:
   pair=((sides(prev)[1],prev[1]),(sides(nxt)[0],nxt[1]));a=p[0]+1
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
  if p==(4,1) and nxt==(5,1):
   q=t[(i+2)%3];pair=((sides(q)[1],q[1]),(sides(q)[0],q[1]));a=0
   factors[a][pair]=factors[a].get(pair,0)|(1<<k)
corona_groups=[[factors[j%5][(tuple(c[j]),tuple(c[j+1]))] for j in range(10)] for c in r['boundary_coronas']]
# Exhaust all 2^22 signed-star subsets, including asymmetrical handed supports.
counts=[0]*7;survivors=[];digest=hashlib.sha256();start=time.monotonic()
for mask in range(1<<n):
 if not all(mask&g for g in cover):continue
 if any(mask&(1<<i) and any(not(mask&g) for g in requirements[i]) for i in range(n)):continue
 cs=[j for j,groups in enumerate(corona_groups) if all(mask&g for g in groups)]
 if not cs:continue
 survivors.append(mask);digest.update(mask.to_bytes(3,'little'))
 for j in cs:counts[j]+=1
# Inclusion-minimal necessary supports suffice for feasibility: extra stars only add equations.
minimal=[]
for mask in sorted(survivors,key=lambda x:(x.bit_count(),x)):
 if not any(t&mask==t for t in minimal):minimal.append(mask)
out={'schema':'FIXED_FIVE_FOUR_METRIC_GATE_V1','A':m.A,'B':r['B'],'domain_subsets':1<<n,'support_count':len(survivors),'support_counts_by_corona':counts,'support_sha256_ascending_3byte_little':digest.hexdigest(),'minimal_supports':minimal,'enumeration_seconds':time.monotonic()-start,'equiangular_matrix':[[int(x) for x in row] for row in M.tolist()],'equiangular_kernel':[[1,0,0,0,0],[0,1,1,1,1]],'metric_timeout_ms':30000,'metric_results':[]}
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
for mask in minimal:
 solver=Z.SolverFor('QF_NRA');solver.set(timeout=30000)
 lengths=Z.Reals('l0 l1 l2 l3 l4');solver.add(lengths[0]==1,*[x>0 for x in lengths],Z.Distinct(*lengths))
 turns=[Z.Reals('c%d s%d'%(i,i)) for i in range(12)]
 for c,s in turns:solver.add(c*c+s*s==1,s>0)
 for i,t in enumerate(stars):
  if mask&(1<<i):
   q=(1,0)
   for c,h in t:q=mul(q,turns[c])
   solver.add(q[0]==-1,q[1]==0)
 for f,word in enumerate((m.A,r['B'])):
  direction=(1,0);vertices=[(0,0)]
  for j,color in enumerate(word):
   x,y=vertices[-1];vertices.append((x+lengths[color]*direction[0],y+lengths[color]*direction[1]))
   direction=mul(direction,turns[6*f+j])
  solver.add(vertices[-1][0]==0,vertices[-1][1]==0)
  for j in range(6):
   x,y=vertices[j];u,v=vertices[j+1];dx,dy=u-x,v-y
   for k in range(6):
    if k not in (j,(j+1)%6):
     a,b=vertices[k];solver.add(dx*(b-y)-dy*(a-x)>0)
  solver.add(direction[0]==1,direction[1]==0)
 start=time.monotonic();res=solver.check();entry={'support_mask':mask,'star_indices':[i for i in range(n) if mask&(1<<i)],'result':str(res),'seconds':time.monotonic()-start}
 if res==Z.unknown:entry['reason']=solver.reason_unknown()
 if res==Z.sat:entry['model']=str(solver.model())
 out['metric_results'].append(entry)
 # First unknown is a stop; first SAT needs an independent exact witness audit.
 if res!=Z.unsat:break
out['status']='blocked' if any(x['result']=='unknown' for x in out['metric_results']) else ('local_metric_witness_pending_audit' if any(x['result']=='sat' for x in out['metric_results']) else 'all_minimal_support_metrics_unsat')
path=base/'research/certificates/hexagon-five-four-metric-gate-2026-10-19.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
