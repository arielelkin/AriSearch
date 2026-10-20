#!/usr/bin/env python3
"""Exact 65536-subset sixteen-star gate; rational universal strip consequences."""
import importlib.util,itertools,json,time,hashlib
from pathlib import Path
from sage.all import QQ,matrix,vector
base=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',base/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,1,2,0,3,1));stars=[tuple(map(tuple,t)) for t in r['fixed_stars']];n=len(stars)
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
# One exact SAT call, capped at 120 seconds; no support enumeration.
from z3 import Solver, Bool, Real, Or, Not, Implies, Sum, sat, unsat
s=Solver();s.set(timeout=120000,random_seed=0)
x=[Bool('s%d'%i) for i in range(n)]
a=[Real('a%d'%i) for i in range(12)]
def clause(mask):return Or(*[x[i] for i in range(n) if mask>>i&1])
for c in cover:s.add(clause(c))
for i,req in enumerate(requirements):
 for g in req:s.add(Implies(x[i],clause(g)))
s.add(Or(*[__import__('z3').And(*[clause(g) for g in gs]) for gs in corona_groups]))
for f in range(2):s.add(Sum(a[6*f:6*f+6])==4)
for v in a:s.add(v>0,v<1)
for i,t in enumerate(stars):s.add(Implies(x[i],Sum([a[p[0]] for p in t])==2))
# Opposite equal-length repeats are edge0/edge3 in both words.
for f in range(2):s.add(Sum(a[6*f:6*f+3])!=2)
# Known four-face carrier of the preceding B=001231 family.
carrier=((0,6,7),(1,2,8),(3,9,10),(4,5,11))
s.add(Or(*[Sum([a[i] for i in t])!=2 for t in carrier]))
status=s.check()
out=dict(schema='THIRTYTWO_STAR_CANDIDATE_GATE_SOL_V1',A=m.A,B=r['B'],stars=stars,star_count=n,corona_count=len(corona_groups),cap='one SAT query, 120000ms, seed0; no support enumeration',status=str(status),scope='exact necessary full-cover endpoint-continuation witnessed formal corona, convex angles, avoidance of both repeated-opposite strip identities and preceding four-face carrier',metric_test='not run unless angle candidate survives',plane_extension='not established',unrestricted_aperiodicity='not established')
if status==sat:
 model=s.model();ids=[i for i in range(n) if bool(model.eval(x[i],model_completion=True))]
 out['star_indices']=ids
 out['angles_pi']=[str(model.eval(v)) for v in a]
 mask=sum(1<<i for i in ids)
 assert all(mask&c for c in cover)
 assert all(not(mask>>i&1) or all(mask&g for g in req) for i,req in enumerate(requirements))
 witnessed=[j for j,gs in enumerate(corona_groups) if all(mask&g for g in gs)]
 assert witnessed
 out['witnessed_formal_corona_indices']=witnessed
 out['support_mask']=mask
 rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
 rows += [[sum(p[0]==i for p in stars[k]) for i in range(12)]+[2] for k in ids]
 mat=matrix(QQ,rows);out['affine_angle_rank']=mat.rank();out['rref']=[[str(v) for v in row] for row in mat.echelon_form()]
# Narrow exact closure attempt: at most64 denominator12 angle models,
# within this one support. No collars or additional supports are searched.
if status==sat:
 from sage.all import CyclotomicField, vector
 from z3 import Int
 d=12;zz=[Int('z%d'%i) for i in range(12)];g=Solver();g.set(timeout=3000,random_seed=0)
 for v in zz:g.add(v>0,v<d)
 for f in range(2):g.add(Sum(zz[6*f:6*f+6])==4*d,Sum(zz[6*f:6*f+3])!=2*d)
 for k in ids:g.add(Sum([zz[p[0]] for p in stars[k]])==2*d)
 F=CyclotomicField(2*d);zeta=F.gen();trials=[];found=None
 for trial in range(64):
  ans=g.check()
  if ans!=sat:break
  mod=g.model();angs=[mod.eval(v).as_long() for v in zz]
  vectors=[]
  for f,word in enumerate((m.A,r['B'])):
   direction=0;v=[F(0)]*5
   for j,color in enumerate(word):
    v[color]+=zeta**direction;direction+=d-angs[6*f+(j+1)%6]
   vectors+=v
  # K embeds into C; equality zero means every rational coefficient zero.
  rows=[]
  for f in range(2):
   for k in range(F.degree()):rows.append([vectors[5*f+c][k] for c in range(5)])
  M=matrix(QQ,rows);ker=M.right_kernel();rec=dict(angles_twelfths=angs,closure_rank=int(M.rank()),kernel_dimension=int(ker.dimension()))
  # Linear rational positivity and pairwise distinctness are exact.
  ls=[Real('l%d'%i) for i in range(5)];q=Solver();q.set(timeout=3000)
  for v in ls:q.add(v>0)
  q.add(ls[0]==1)
  for i in range(5):
   for j in range(i):q.add(ls[i]!=ls[j])
  from z3 import RealVal
  for row in M:q.add(Sum([RealVal(str(v))*ls[i] for i,v in enumerate(row)])==0)
  feasible=q.check();rec['positive_five_distinct_lengths']=str(feasible)
  trials.append(rec)
  if feasible==sat:
   qm=q.model();found=dict(angles_twelfths=angs,lengths=[str(qm.eval(v)) for v in ls]);break
  g.add(Or(*[v!=value for v,value in zip(zz,angs)]))
 out['metric_test']=dict(domain='one retained support, at most64 convex denominator12 angle models, exact cyclotomic24 closure',cap=64,trials=trials,candidate=found,last_angle_solver_status=str(ans))
if status==sat:
 out['known_four_face_carrier_implied']=all(matrix(QQ,[[int(i in t) for i in range(12)]+[2]]).row(0) in mat.row_space() for t in carrier)
 out['monohedral_audit']='Under five-distinct-length assumption H2 needs two opposite equal pairs and H3 three adjacent pairs: neither native word has these. H1 only possible opposite pair is0/3 for both, explicitly avoided by sum angles0..2 !=2pi. No metric survived, so no concrete monohedral metric assertion.'
 out['stopping_state']='Blocked under protocol5: formal support survives but narrow exact metric gate has no candidate; no changed plane-extension mechanism. Reopen only with a new explicit closed five-distinct-length metric in this affine support plus witnessed corona geometry and a concrete unbounded extension mechanism, or a new invariant/construction.'
if status==__import__('z3').unknown:out['reason_unknown']=s.reason_unknown()
assert n==32 and len(corona_groups)==100
path=base/'research/certificates/hexagon-thirtytwo-star-candidate-gate-sol-2026-10-19.json'
path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('status','star_indices','affine_angle_rank','witnessed_formal_corona_indices','known_four_face_carrier_implied','stopping_state')},indent=2))
