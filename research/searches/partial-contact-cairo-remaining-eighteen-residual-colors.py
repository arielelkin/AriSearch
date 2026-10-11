"""Generic full residual-length seam colors on fourdim3 and twoseparated Cairo families."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import argparse,json,inspect,runpy
from sage.all import vector,PolynomialRing
h=runpy.run_path(str(Path(__file__).with_name("partial-contact-cairo-one-shared-optional-seam-balance.py")));K=h["K"]
source=inspect.getsource(h["model"])
old="sample=K(chamber['sample_parameter']);value=lambda f:f[0]+f[1]*sample"
new="point=tuple(map(K,chamber['sample_kernel_point']));value=lambda f:sum(x*y for x,y in zip(f,point))"
assert source.count(old)==source.count("colour=(count,parts[j] if count else ())")==1
namespace=h["balance"].__globals__;exec(source.replace(old,new).replace("colour=(count,parts[j] if count else ())","colour=(count,parts[j])"),namespace)
M=namespace["model"]
ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);a=ap.parse_args();a.scope="remaining18"
F=json.loads(Path("research/certificates/partial-contact-cairo-remaining-two-cross-event-flats.json").read_text())
A=json.loads(Path("research/certificates/partial-contact-cairo-two-cross-event-flats.json").read_text())["separated"]
remaining={(r["pattern"],r["flat_id"]) for r in json.loads(Path("research/certificates/partial-contact-cairo-mixed-quotient-flat-containment.json").read_text())["records"] if not r["maps"]}
assert len(remaining)==18
cases=[]
for dim in(1,2):
 D=json.loads(Path(f"research/certificates/partial-contact-cairo-two-cross-dim{dim}-order-chambers.json").read_text());assert D["completion"]=="complete"
 for rec in D["records"]:
  name,fid=rec["pattern"],rec["flat_id"]
  if(name,fid) not in remaining:continue
  flat=F[name]["records"][fid]
  for chamber in rec["chambers"]:cases.append((name,flat,chamber,F[name]["hyperplane_rows"]))
R=PolynomialRing(K,"u")
for fid in(46,49):
 flat=dict(A["records"][fid]);forms=[R(t) for t in flat["normalized_arms"]+flat["normalized_e"]]
 flat["arm_forms"]=[[str(t[0]),str(t[1])] for t in forms[:8]];flat["e_forms"]=[[str(t[0]),str(t[1])] for t in forms[8:]]
 for cid,chamber in enumerate(flat["generic_arm_order_chambers"]):
  chamber=dict(chamber);chamber["order_chamber_id"]=cid;chamber["sample_kernel_point"]=["1",chamber["sample_parameter"]]
  cases.append(("separated",flat,chamber,A["hyperplane_rows"]))
records=[];stats=Counter()
for name,flat,original,hyperplanes in cases:
 forms=[vector(K,list(map(K,z))) for z in flat["arm_forms"]+flat["e_forms"]];dim=len(forms[0]);point=vector(K,list(map(K,original["sample_kernel_point"])))
 raw,edges,*_=M(flat,original)
 residuals={}
 for eid,(key,colour) in enumerate(edges):
  if colour[0]:continue
  species,native,parts,piece=key;assert native<4 and len(parts)==2
  host=4*species+native;cut=next(i for i in range(8) if tuple(forms[i])==parts[1-piece])
  expression=vector(K,[int(i==host)-int(i==cut) for i in range(8)])
  assert sum((expression[i]*forms[i] for i in range(8)),vector(K,[0]*dim))==vector(K,colour[1])
  residuals.setdefault(tuple(colour[1]),{"native_expression":[str(t) for t in expression],"edge_id":eid})
 proper={}
 for left,right in combinations(sorted(residuals),2):
  delta=vector(K,left)-vector(K,right);pivot=next(t for t in delta if t);canonical=tuple(delta/pivot)
  rawrow=(vector(K,list(map(K,residuals[left]["native_expression"]))) - vector(K,list(map(K,residuals[right]["native_expression"]))))/pivot
  proper.setdefault(canonical,{"reduced_row":[str(t) for t in canonical],"native_row":[str(t) for t in rawrow],"residual_pair":[[str(t) for t in left],[str(t) for t in right]]})
 old=[]
 for row in hyperplanes:
  red=sum((K(t)*forms[i] for i,t in enumerate(row)),vector(K,[0]*dim))
  if any(red):old.append(red)
 avoid=old+[vector(K,z) for z in proper]
 constraints=list(forms)
 for i,j in combinations(range(8),2):
  difference=forms[i]-forms[j]
  if any(difference):constraints.append(difference if difference.dot_product(point)>0 else -difference)
 if name=="separated":
  left,right=original["interval"]
  if left is not None:constraints.append(vector(K,[-K(left),1]))
  if right is not None:constraints.append(vector(K,[K(right),-1]))
 assert all(z.dot_product(point)>0 for z in constraints)
 seed=0
 while True:
  direction=vector(K,[K(seed)**j for j in range(dim)])
  if all(z.dot_product(direction)!=0 for z in avoid):break
  seed+=1
 eps=min(z.dot_product(point) for z in constraints)/(2*max([K(1)]+[abs(z.dot_product(direction)) for z in constraints]))
 for n in range(1,len(avoid)+2):
  generic=point+eps*K(n)/K(len(avoid)+2)*direction
  if all(z.dot_product(generic)!=0 for z in avoid):break
 else:raise AssertionError("finite proper-plane avoidance failed")
 assert all(z.dot_product(generic)>0 for z in constraints)
 chamber=dict(original);chamber["sample_kernel_point"]=[str(t) for t in generic];chamber["sample_parameter"]="0"
 balance=h["balance"](flat,chamber);stats[balance["result"]]+=1
 rec={"pattern":name,"flat_id":flat["flat_id"],"dimension":dim,"source_order_chamber_id":original["order_chamber_id"],"source_interval":original["interval"],"arm_forms":flat["arm_forms"],"e_forms":flat["e_forms"],"sample_kernel_point":chamber["sample_kernel_point"],"sample_arms":[str(z.dot_product(generic)) for z in forms[:8]],"sample_e":[str(z.dot_product(generic)) for z in forms[8:]],"residual_forms":[{"form":[str(t) for t in form],**value} for form,value in sorted(residuals.items())],"additional_proper_residual_planes":list(proper.values()),"seam_balance":balance}
 records.append(rec)
 if a.output:Path(a.output).write_text(json.dumps({"scope":"full residual-length colors necessary only outside retained additional proper residual equality planes; no complete flat kill","completion":"partial","selection":a.scope,"requested_chambers":len(cases),"completed_chambers":len(records),"records":records},indent=2)+"\n")
 print("CHAMBER",name,flat["flat_id"],original["order_chamber_id"],"additionalplanes",len(proper),balance["result"],flush=True)
if a.output:Path(a.output).write_text(json.dumps({"scope":"full residual-length colors necessary only outside retained additional proper residual equality planes; no complete flat kill","completion":"complete","selection":a.scope,"requested_chambers":len(cases),"completed_chambers":len(records),"records":records},indent=2)+"\n")
print("FINAL",len(records),dict(stats),flush=True)
