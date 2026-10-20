"""One exact common-center feasibility gate, fixed depth-3 patch; no patch growth."""
import importlib.util,json
from pathlib import Path
import sympy as S
import z3
spec=importlib.util.spec_from_file_location('gate',Path(__file__).with_name('pinwheel-barycentric-crossboundary-2026-10-19.py'));g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
p,q=S.symbols('p q');zp,zq=z3.Reals('p q')
ts=[g.base]
for _ in range(3):ts=[c for t in ts for c in g.subdivide(t)]
vs=set(v for t in ts for v in t)
constraints=[];locations=[]
for v in sorted(vs):
 if any(g.on(v,a,b) for a,b in zip(g.base,g.base[1:]+g.base[:1])):continue
 steps={}
 for t in ts:
  if not any(g.on(v,a,b) for a,b in zip(t,t[1:]+t[:1])):continue
  if g.area(t)<0:t=t[::-1]
  o,u,w=g.ordered(t);center=g.add(o,g.add(g.mul(g.sub(u,o),p),g.mul(g.sub(w,o),q)))
  neighbors=[]
  for a,b in zip(t,t[1:]+t[:1]):
   if g.on(v,a,b):
    pts=sorted((r for r in vs if g.on(r,a,b)),key=lambda r:g.dot(g.sub(r,a),g.sub(b,a)));j=pts.index(v)
    if j:neighbors.append(('in',pts[j-1]))
    if j+1<len(pts):neighbors.append(('out',pts[j+1]))
  prev=next(r for typ,r in neighbors if typ=='in');nxt=next(r for typ,r in neighbors if typ=='out')
  steps[g.midpoint(v,nxt)]=(center,g.midpoint(v,prev))
 start=min(steps);poly=[];cur=start
 while True:
  center,nxt=steps[cur];poly.extend([cur,center]);cur=nxt
  if cur==start:break
 for i in range(len(poly)):
  expr=S.Poly(S.expand(g.cross(g.sub(poly[i],poly[i-1]),g.sub(poly[(i+1)%len(poly)],poly[i]))),p,q)
  if expr.is_zero:continue
  val=sum(z3.RealVal(str(c))*zp**a*zq**b for (a,b),c in expr.terms())
  constraints.append(val>=0);locations.append({'vertex':[str(x) for x in v],'turn_index':i,'polynomial':str(expr.as_expr()),'triple':[[str(x) for x in poly[j%len(poly)]] for j in (i-1,i,i+1)]})
solver=z3.SolverFor('QF_NRA');solver.set(timeout=30000);solver.add(zp>0,zq>0,zp+zq<1)
for i,c in enumerate(constraints):solver.assert_and_track(c,'turn_'+str(i))
status=solver.check();out={'domain':'all 81 interior cells of same depth-3 pinwheel supertriangle; common center fractions p,q with p>0,q>0,p+q<1; common seam midpoints','turn_constraints':len(constraints),'status':str(status),'timeout_ms':30000,'z3_version':z3.get_version_string()}
if status==z3.unsat:
 core=[int(str(x).split('_')[1]) for x in solver.unsat_core()];out['unsat_core']=[locations[i] for i in core]
 # Explicit exact reduced-core replay; no claim of a formal proof certificate.
 small=z3.SolverFor('QF_NRA');small.add(zp>0,zq>0,zp+zq<1,*[constraints[i] for i in core]);assert small.check()==z3.unsat
elif status==z3.sat:out['model']=str(solver.model())
else:out['reason']=solver.reason_unknown()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
