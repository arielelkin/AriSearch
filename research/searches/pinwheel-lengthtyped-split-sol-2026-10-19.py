"""Exact opposing-turn gate; fixed patch, length-typed seams, two handed centers."""
import importlib.util,json
from pathlib import Path
import sympy as S
import z3
spec=importlib.util.spec_from_file_location('source',Path(__file__).with_name('pinwheel-barycentric-crossboundary-2026-10-19.py'))
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
ts=[g.base]
for _ in range(3):ts=[u for t in ts for u in g.subdivide(t)]
vs=set(v for t in ts for v in t)
interior=lambda v:not any(g.on(v,a,b) for a,b in zip(g.base,g.base[1:]+g.base[:1]))
edges={}
for i,t in enumerate(ts):
 for a,b in zip(t,t[1:]+t[:1]):
  pts=sorted((v for v in vs if g.on(v,a,b)),key=lambda v:g.dot(g.sub(v,a),g.sub(b,a)))
  for x,y in zip(pts,pts[1:]):edges.setdefault(tuple(sorted((x,y))),set()).add(i)
lengths=sorted(set(g.dot(g.sub(a,b),g.sub(a,b)) for a,b in edges))
pp,qp,pm,qm=S.symbols('pp qp pm qm')
splits=S.symbols('s0:'+str(len(lengths)));variables=(pp,qp,pm,qm)+splits
centers=[]
for t in ts:
 o,l,s=g.ordered(t);p,q=(pp,qp) if g.cross(g.sub(l,o),g.sub(s,o))>0 else (pm,qm)
 centers.append(g.add(o,g.add(g.mul(g.sub(l,o),p),g.mul(g.sub(s,o),q))))
def signature(v,ids):
 return sorted(tuple(g.dot(g.sub(v,x),g.sub(v,x)) for x in g.ordered(ts[i])) for i in ids)
records=[]
for (a,b),ids in sorted(edges.items()):
 if len(ids)!=2 or not(interior(a) and interior(b)):continue
 ids=sorted(ids);sa,sb=signature(a,ids),signature(b,ids)
 if sb<sa:a,b=b,a
 length=g.dot(g.sub(a,b),g.sub(a,b));f=S.Rational(1,2) if sa==sb else splits[lengths.index(length)]
 seam=g.add(a,g.mul(g.sub(b,a),f));c,d=(centers[i] for i in ids)
 raw=S.expand(g.cross(g.sub(c,seam),g.sub(d,seam)))
 expr=S.Poly(raw,*variables).clear_denoms()[1].primitive()[1].as_expr()
 records.append(dict(endpoints=[[str(x) for x in v] for v in (a,b)],triangles=ids,length=str(length),fraction=str(f),polynomial=str(expr),raw_determinant=str(raw),frames=[[[str(x) for x in v] for v in g.ordered(ts[i])] for i in ids]))
# Proof certificate independent of the solver, derived before solving anything.
witness_endpoints=[[['1/25','2/25'],['3/25','1/25']],[['3/25','11/25'],['1/5','2/5']]]
witness=[next(r for r in records if r['endpoints']==e) for e in witness_endpoints]
A,B=[S.sympify(r['polynomial']) for r in witness]
assert S.expand(A+B)==-2*pm
assert all(all(g.cross(g.sub(g.ordered(ts[i])[1],g.ordered(ts[i])[0]),g.sub(g.ordered(ts[i])[2],g.ordered(ts[i])[0]))<0 for i in r['triangles']) for r in witness)
# Equations arise before all numerical or convexity/class enumeration.
polys=list(dict.fromkeys(r['polynomial'] for r in records))
print('lengths',lengths,'seams',len(records),'unique equations',len(polys),flush=True)
zvars={str(v):z3.Real(str(v)) for v in variables}
def zexpr(expr):
 poly=S.Poly(S.sympify(expr),*variables)
 return sum(z3.RealVal(str(c))*__import__('functools').reduce(lambda a,b:a*b,(zvars[str(v)]**e for v,e in zip(variables,powers)),z3.RealVal(1)) for powers,c in poly.terms())
solver=z3.SolverFor('QF_NRA');solver.set(timeout=30000)
for p,q in ((pp,qp),(pm,qm)):solver.add(zvars[str(p)]>0,zvars[str(q)]>0,zvars[str(p)]+zvars[str(q)]<1)
for s in splits:solver.add(zvars[str(s)]>0,zvars[str(s)]<1)
for j,expr in enumerate(polys):solver.assert_and_track(zexpr(expr)==0,'eq'+str(j))
status=solver.check();print(status,flush=True)
out=dict(exact_obstruction='A+B=-2*pm; interior centers require pm>0',witness=witness,lengths=[str(x) for x in lengths],variables=[str(x) for x in variables],seams=records,status=str(status),z3_version=z3.get_version_string(),timeout_ms=30000)
if status==z3.unsat:
 core=[int(str(x)[2:]) for x in solver.unsat_core()];out['core']=[polys[j] for j in core];print('core',out['core'],flush=True)
elif status==z3.sat:out['model']=str(solver.model());print(out['model'])
else:out['reason']=solver.reason_unknown()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
