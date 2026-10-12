#!/usr/bin/env python3
"""Independent algebra-gate replay, with separately reconstructed coordinates."""
import importlib.util,itertools,json,time
from pathlib import Path
from sage.all import PolynomialRing
here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('audit',here/'kite-dart-exclusion-audit.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
CERT=a.C;F=a.F;phi=a.phi;start=time.monotonic()
rows=[json.loads(s) for s in (CERT/'penrose-kite-dart-recomposition-patch3.jsonl').read_text().splitlines()]
by={(r['kite'],r['dart']):r for r in rows};metric=[json.loads(s) for s in (CERT/'penrose-kite-dart-metric-collapse.jsonl').read_text().splitlines()]
def norm(A,B):
 x,y=A[0]-B[0],A[1]-B[1];return x*x+phi*x*y+y*y
def data(row):
 R,active,V=a.coordinates(row);D=[[[norm(x,y) for y in P] for x in P] for P in V]
 N=[norm(P[i],P[(i+1)%len(P)]) for P in V for i in range(len(P))]
 for p,q in ((0,1),(2,3)):
  if p in active and q in active:
   i,j=active.index(p),active.index(q);N.append(norm((R.gen(2*i),R.gen(2*i+1)),(R.gen(2*j),R.gen(2*j+1))))
 return R,active,V,D,N
cache={};status_counts={};checked=0
for r in metric:
 key=(r['kite'],r['dart'])
 if key not in cache:cache[key]=data(by[key])
 R,active,V,D,N=cache[key];i,j,o,shift=r['i'],r['j'],r['orientation'],r['shift'];n=len(V[i]);perm=[(shift+o*k)%n for k in range(n)]
 eq=[D[i][u][v]-D[j][perm[u]][perm[v]] for u in range(n) for v in range(u+1,n)]
 I=R.ideal(eq);G=I.groebner_basis();recorded=tuple(R(g) for g in r['basis']);assert tuple(G)==recorded
 dim=int(I.dimension());assert dim==r['dimension']
 st=r['status'];status_counts[st]=status_counts.get(st,0)+1
 if st=='unit':assert list(G)==[R(1)]
 elif st=='zero-dimensional':assert dim==0
 elif st=='forced-degeneracy':assert any(I.reduce(q)==0 for q in N)
 elif st=='fixed-exterior-node':
  idx=active.index(r['node']);x,y=I.reduce(R.gen(2*idx)),I.reduce(R.gen(2*idx+1));assert x.is_constant() and y.is_constant()
  # Direct planar inequalities, separate from producer's number-field inside.
  point=(F(x),F(y));ref=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1 if r['node']<2 else 1/phi)),(F(-1),phi)]
  def turn(A,B):return (B[0]-A[0])*(point[1]-A[1])-(B[1]-A[1])*(point[0]-A[0])
  if r['node']<2:inside=all(turn(ref[k],ref[(k+1)%4])>0 for k in range(4))
  else:
   A,B,C,D=ref;inside=(turn(A,B)>0 and turn(B,C)>0 and turn(C,A)>=0) or (turn(A,C)>=0 and turn(C,D)>0 and turn(D,A)>0)
  assert not inside
 else:assert st=='positive-dimensional-necessary-survivor' and dim>0 and all(I.reduce(q)!=0 for q in N)
 checked+=1
print(json.dumps({'metric_options_independently_rebuilt':checked,'statuses':status_counts}),flush=True)
# Two hexagon patterns: verify an incompatible triangle directly from the
# independently checked pair option statuses. Three mutually distinct faces
# cannot occupy only two congruence classes on a positive-dimensional locus.
hexagons=[]
for key in ((1,3),(3,1)):
 N=len(by[key]['classes']);bad=set()
 for i,j in itertools.combinations(range(N),2):
  options=[r for r in metric if (r['kite'],r['dart'])==key and r['i']==i and r['j']==j]
  assert len(options)==12
  if all(r['status']!='positive-dimensional-necessary-survivor' for r in options):bad.add((i,j))
 triangle=next(t for t in itertools.combinations(range(N),3) if all(pair in bad for pair in itertools.combinations(t,2)))
 hexagons.append({'pair':key,'incompatible_triangle':triangle})
# Replay complete pentagon joint search by a fresh Cartesian recursive sum
# of necessary pair ideals. Prune only zero-dimensional/unit/zero-edge ideals;
# each gate is monotone when equations are added.
partitions=0;leaves=0
for key in ((15,27),(27,15)):
 R,active,V,D,N=data(by[key]);nc=len(V);opts={};memo={}
 for i,j in itertools.combinations(range(nc),2):
  opts[i,j]={tuple(R(g) for g in r['basis']) for r in metric if (r['kite'],r['dart'])==key and (r['i'],r['j'])==(i,j) and r['status']=='positive-dimensional-necessary-survivor'}
 def viable(G):
  I=R.ideal(G)
  return int(I.dimension())>0 and all(I.reduce(q)!=0 for q in N)
 def explore(links,G):
  global leaves
  state=(tuple(links),G)
  if state in memo:return memo[state]
  if not links:
   leaves+=1;memo[state]=viable(G);return memo[state]
  i,j=links[0]
  for H in opts[i,j]:
   J=tuple(R.ideal(G+H).groebner_basis())
   if viable(J) and explore(links[1:],J):memo[state]=True;return True
  memo[state]=False;return False
 for mask in range(1<<(nc-1)):
  blocks=[[0]+[i for i in range(1,nc) if not(mask>>(i-1)&1)],[i for i in range(1,nc) if mask>>(i-1)&1]]
  links=[(b[0],i) for b in blocks if b for i in b[1:]];links.sort(key=lambda e:len(opts[e]))
  assert not explore(links,());partitions+=1
print(json.dumps({'joint_partitions_independently_replayed':partitions}),flush=True)
# Independent flat-cell exhaustiveness: weak turns contain opposite
# multiples of one polynomial, forcing precisely the three recorded zeros.
import z3
key=(3,1);row=by[key];R,active,V,D,N=data(row)
turns=[];indices=[]
for ci,P in enumerate(V):
 for i in range(len(P)):
  A,B,C=P[i-1],P[i],P[(i+1)%len(P)]
  turns.append((B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]));indices.append((ci,i))
forced={(0,4),(3,2),(4,0)};q=turns[indices.index((0,4))]
ratios=[]
for ix in forced:
 t=turns[indices.index(ix)];assert t==q or t==-q;ratios.append(1 if t==q else -1)
assert -1 in ratios and 1 in ratios
solver=z3.SolverFor('QF_NRA');solver.set(timeout=30000)
solver.from_string((CERT/'kite-dart-exclusion-audit.3-1.smt2').read_text())
root=z3.Real('sqrt_five');Y=[z3.Real(str(x)) for x in R.gens()]
def cv(poly):
 total=z3.RealVal(0)
 for mon,coeff in R(poly).dict().items():
  aa,bb=F(coeff).vector();term=z3.RealVal(str(aa))+z3.RealVal(str(bb))*root
  for y,k in zip(Y,mon):
   if k:term*=y**int(k)
  total+=term
 return total
baseline=solver.check();assert baseline==z3.sat
solver.add(cv(q)==0)
solver.add(z3.Or([cv(t)==0 for ix,t in zip(indices,turns) if ix not in forced]))
answer=solver.check();print(json.dumps({'flat_exhaustion_status':str(answer),'reason':solver.reason_unknown() if answer==z3.unknown else ''}),flush=True);assert answer==z3.unsat,'Independent flat-cell exhaustion unresolved'
(CERT/'kite-dart-exclusion-audit-flat-extra-zero.smt2').write_text(solver.sexpr()+'\n(check-sat)\n')
classes=[dict(c,forms=[f for i,f in enumerate(c['forms']) if (ci,i) not in forced]) for ci,c in enumerate(row['classes'])]
R,active,V,D,N=data(dict(row,classes=classes));Q=tuple(R.ideal([q]).groebner_basis());flat_exclusions=[]
for i,j in itertools.combinations(range(len(V)),2):
 if len(V[i])!=len(V[j]):continue
 surviving=0;dims=[]
 for orientation in (1,-1):
  for shift in range(len(V[i])):
   perm=[(shift+orientation*k)%len(V[i]) for k in range(len(V[i]))]
   equations=[D[i][u][v]-D[j][perm[u]][perm[v]] for u in range(len(V[i])) for v in range(u+1,len(V[i]))]
   J=R.ideal(list(Q)+equations);dim=int(J.dimension());dims.append(dim)
   if dim>0 and all(J.reduce(t)!=0 for t in N):surviving+=1
 flat_exclusions.append({'classes':[i,j],'options':2*len(V[i]),'necessary_survivors':surviving,'dimensions':dims})
assert any(r['necessary_survivors']==0 for r in flat_exclusions),'Further exterior-point/joint gates needed'
# All three pentagons must be one shape and both hexagons the other; every
# equal-side pair is therefore mandatory in any two-shape partition.
# Mirror map independently checked against our reconstructed distances.
A=by[1,3];B=by[3,1];R,active,VA,DA,NA=data(A);_,_,VB,DB,NB=data(B)
h=R.hom([v for i in range(len(active)) for v in (-R.gen(2*i),phi*R.gen(2*i)+R.gen(2*i+1))],R)
mirror=json.loads((CERT/'penrose-kite-dart-flat-mirror-map.json').read_text())
for ci,cj,o,shift in mirror['class_map']:
 n=len(DA[ci]);perm=[(shift+o*k)%n for k in range(n)]
 assert all(h(DA[ci][i][j])==DB[cj][perm[i]][perm[j]] for i in range(n) for j in range(n))
assert all(h(h(x))==x for x in R.gens())
for typ in ('kite','dart'):
 ref={a.K(0),a.K(1),a.w if typ=='kite' else a.w/a.kp,a.w**2}
 assert {a.w**2*z.conjugate() for z in ref}==ref
flat_result={'pair':[3,1],'forced_zero_turn_vertices':sorted(forced),'further_zero_turn_patterns':'independently UNSAT',
 'equal_side_pair_metric_gates':flat_exclusions,'mirror_transfer_independently_checked':True}
print(json.dumps({'flat_cell_independently_closed':True}),flush=True)
result={'metric_options_independently_rebuilt':checked,'statuses':status_counts,'hexagon_no_deletion_incompatibility_triangles':hexagons,
 'joint_partitions_independently_replayed':partitions,'joint_retained_positive_dimensional_loci':0,'flat_cell_audit':flat_result,'elapsed_seconds':round(time.monotonic()-start,3),
 'scope':'Independent input/coordinate reconstruction and gate implementation; Sage/Singular algebra engine shared, no formal proof-assistant certificate.'}
(CERT/'kite-dart-exclusion-audit-algebra.json').write_text(json.dumps(result,indent=1)+'\n')
