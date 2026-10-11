"""Complete strict native-arm order chambers of the134 remaining two-cross seam primals."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import argparse,json,runpy,inspect
from sage.all import matrix,vector,Polyhedron
import numpy as np
from scipy.optimize import linprog
h=runpy.run_path(str(Path(__file__).with_name("partial-contact-cairo-one-shared-optional-seam-balance.py")))
K=h["K"]
# Preserve full symbolic forms; only numerical ordering evaluation is generalized.
source=inspect.getsource(h["model"])
old="sample=K(chamber['sample_parameter']);value=lambda f:f[0]+f[1]*sample"
new="point=tuple(map(K,chamber['sample_kernel_point']));value=lambda f:sum(x*y for x,y in zip(f,point))"
assert source.count(old)==1
namespace=h["balance"].__globals__;exec(source.replace(old,new),namespace)
F=Path("research/certificates/partial-contact-cairo-remaining-two-cross-event-flats.json")
S=Path("research/certificates/partial-contact-cairo-remaining-two-cross-order-free-seams.json")
ap=argparse.ArgumentParser();ap.add_argument("--dimension",type=int,choices=(1,2,3));ap.add_argument("--pattern");ap.add_argument("--flat",type=int);ap.add_argument("--chambers-only",action="store_true");ap.add_argument("--include-periodic-carrier",action="store_true");ap.add_argument("--output");a=ap.parse_args()
flats=json.loads(F.read_text());primals=[z for z in json.loads(S.read_text())["records"] if z["result"]=="exact-necessary-primal"]
selected=[p for p in primals if (a.dimension is None or p["dimension"]==a.dimension) and (a.pattern is None or p["pattern"]==a.pattern) and (a.flat is None or p["flat_id"]==a.flat) and (a.include_periodic_carrier or (p["pattern"],p["flat_id"])!=("orbit4",20))]
results=[];stats=Counter()
def output(complete):
 if a.output:Path(a.output).write_text(json.dumps({"scope":"complete strict native-arm order arrangements of supplied order-free primal flats; optional two-ended seam balance is necessary only","completion":"complete" if complete else "partial","selection":{"dimension":a.dimension,"pattern":a.pattern,"flat_id":a.flat,"include_reviewed_periodic_carrier":a.include_periodic_carrier},"flat_source":str(F),"primal_source":str(S),"requested_primal_flats":len(selected),"completed_primal_flats":len(results),"chambers_only":a.chambers_only,"records":results},indent=2)+"\n")
for p in selected:
 name,fid=p["pattern"],p["flat_id"]
 flat=flats[name]["records"][fid];assert flat["status"]=="generic-local-survivor"
 forms=[tuple(map(K,t)) for t in flat["arm_forms"]+flat["e_forms"]];dim=flat["dimension"]
 reps=[i for i in range(8) if forms[i] not in forms[:i]];assert len(reps)==6
 pairs=list(combinations(reps,2));diffs=[tuple(x-y for x,y in zip(forms[i],forms[j])) for i,j in pairs]
 base=[vector(K,z) for z in forms]
 proper=[]
 for row in flats[name]["hyperplane_rows"]:
  raw=list(map(K,row));red=vector(K,[sum(raw[i]*forms[i][j] for i in range(8)) for j in range(dim)])
  if any(red):proper.append(red)
 tests=[];leaves=[]
 def feasible(rows,signs):
  poly=Polyhedron(ieqs=[[-K(1)]+list(z) for z in rows],base_ring=K,backend="field")
  if not poly.is_empty():return vector(K,poly.representative_point())
  # Float optimization only proposes a sparse support; exact K reconstruction
  # and validation below is the complete proof-relevant certificate.
  coefficients=matrix(K,[[z[j] for z in rows] for j in range(dim)]+[[K(1)]*len(rows)])
  target=vector(K,[K(0)]*dim+[K(1)])
  proposal=linprog(np.zeros(len(rows)),A_eq=np.array(coefficients,dtype=float),b_eq=np.array(target,dtype=float),bounds=(0,None),method="highs")
  weights=None
  if proposal.success:
   support=[i for i,t in enumerate(proposal.x) if t>1e-9]
   try:
    exact=coefficients.matrix_from_columns(support).solve_right(target)
    candidate=[K(0)]*len(rows)
    for i,t in zip(support,exact):candidate[i]=t
    if all(t>=0 for t in candidate) and coefficients*vector(K,candidate)==target:weights=candidate
   except (ValueError,ArithmeticError):pass
  if weights is None:
   dual=Polyhedron(eqns=[[0]+[z[j] for z in rows] for j in range(dim)]+[[-1]+[1]*len(rows)],ieqs=[[0]+[int(i==j) for j in range(len(rows))] for i in range(len(rows))],base_ring=K,backend="field")
   assert not dual.is_empty();weights=list(dual.representative_point())
  assert all(t>=0 for t in weights) and sum(weights)==1
  assert all(sum(t*z[j] for t,z in zip(weights,rows))==0 for j in range(dim))
  tests.append({"sign_prefix":signs,"gordan_dual":[str(t) for t in weights]});return None
 def generic_sample(point,rows):
  if not proper:return point
  seed=0
  while True:
   direction=vector(K,[K(seed)**j for j in range(dim)])
   if all(z.dot_product(direction)!=0 for z in proper):break
   seed+=1
  eps=1/(2*max([K(1)]+[abs(z.dot_product(direction)) for z in rows]))
  for n in range(1,len(proper)+2):
   candidate=point+eps*K(n)/K(len(proper)+2)*direction
   if all(z.dot_product(candidate)!=0 for z in proper):
    assert all(z.dot_product(candidate)>0 for z in rows);return candidate
  raise AssertionError("finite proper hyperplane avoidance failed")
 def descend(depth,rows,signs):
  point=feasible(rows,signs)
  if point is None:return
  if depth==len(diffs):
   point=generic_sample(point,rows);values=[vector(K,z).dot_product(point) for z in forms]
   assert all(v>0 for v in values)
   assert all(values[i]!=values[j] for i,j in pairs)
   assert all(sign*vector(K,delta).dot_product(point)>0 for sign,delta in zip(signs,diffs))
   chamber={"order_chamber_id":len(leaves),"signs":signs,"sample_kernel_point":[str(t) for t in point],"sample_arms":[str(t) for t in values[:8]],"sample_e":[str(t) for t in values[8:]],"native_arm_order":sorted(range(8),key=lambda i:(values[i],i)),"sample_parameter":"0","interval":[None,None]}
   if not a.chambers_only:
    balance=h["balance"](flat,chamber);balance["pattern"]=name;balance["dimension"]=dim;balance["order_chamber_id"]=chamber["order_chamber_id"];balance["sample_kernel_point"]=chamber["sample_kernel_point"];chamber["seam_balance"]=balance;stats[balance["result"]]+=1
   leaves.append(chamber);return
  for sign in(-1,1):descend(depth+1,rows+[sign*vector(K,diffs[depth])],signs+[sign])
 descend(0,base,[])
 assert leaves
 results.append({"pattern":name,"flat_id":fid,"dimension":dim,"native_comparison_pairs":[list(z) for z in pairs],"empty_sign_prefixes":tests,"chambers":leaves})
 print("COMPLETE",name,fid,"dimension",dim,"order chambers",len(leaves),"exactempty branches",len(tests),dict(stats),flush=True)
 output(False)
output(True)
print("FINAL",len(results),"primalflats",sum(len(z["chambers"]) for z in results),"orderchambers",dict(stats),flush=True)
