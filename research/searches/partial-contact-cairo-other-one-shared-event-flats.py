"""Complete native120/contact flat enumeration for other sole-cross endpoint orbits."""
from sage.all import QuadraticField,matrix,vector,Polyhedron,PolynomialRing
from itertools import combinations_with_replacement,product,combinations
from collections import Counter,deque
import json,argparse
K=QuadraticField(3,"w");w=K.gen();unit=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
E=-2*unit[0]+w*unit[2]+unit[3];F=-2*unit[4]+w*unit[6]+unit[7]
other=(1,0,3,2,5,4,7,6);corners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
def canonical(rows):
 m=matrix(K,rows).echelon_form();return tuple(tuple(row) for row in m.rows() if any(row))
def key(rows):return tuple(tuple(str(t) for t in z) for z in rows)
def enumerate_orbit(name,crossmatch):
 sharedP,sharedQ=crossmatch
 base=[w*unit[0]+unit[1]-unit[2]-w*unit[3],w*unit[4]+unit[5]-unit[6]-w*unit[7],unit[sharedP]-unit[sharedQ]]
 cross=unit[other[sharedP]]+unit[other[sharedQ]]
 reps=[i for i in range(8) if i!=sharedQ]
 banks={other[sharedP],other[sharedQ]};remaining=[i for i in reps if i not in banks]
 assert len(reps)==7 and len(remaining)==5
 eventforms=[2*unit[i] for i in reps]+[cross]
 hyperplanes=[cross-2*unit[i] for i in remaining]+[g-h for g in(E,F) for h in eventforms]+[E-F]
 assert len(hyperplanes)==22
 names=["cross=2arm"+str(i) for i in remaining]+[str(g)+"=event"+str(j) for g in("eP","eQ") for j in range(8)]+["eP=eQ"]
 records=[];stats=Counter()
 root=canonical(base);queue=deque([root]);seen={key(root)};records=[];stats=Counter()
 while queue:
  rows=queue.popleft();ns=matrix(K,rows).right_kernel().basis();q=lambda v:tuple(v.dot_product(x) for x in ns)
  arms=[q(x) for x in unit];es=[q(E),q(F)];active=[j for j,h in enumerate(hyperplanes) if not any(q(h))]
  rec={"flat_id":len(records),"dimension":len(ns),"active_hyperplanes":active,"constraint_rows":key(rows)}
  bad=any(arms[i]==arms[j] for i,j in combinations(range(8),2) if(i,j)!=crossmatch)
  if bad:rec["status"]="forced-extra-arm";records.append(rec);stats[rec["status"]]+=1;continue
  poly=Polyhedron(ieqs=[[-K(1)]+list(z) for z in arms+es],base_ring=K,backend="field")
  if poly.is_empty():
   lengths=arms+es
   dual=Polyhedron(eqns=[[0]+[z[j] for z in lengths] for j in range(len(ns))]+[[-1]+[1]*10],ieqs=[[0]+[int(i==j) for j in range(10)] for i in range(10)],base_ring=K,backend="field")
   assert not dual.is_empty()
   weights=list(dual.representative_point())
   assert all(x>=0 for x in weights) and sum(weights)==1
   assert all(sum(a*z[j] for a,z in zip(weights,lengths))==0 for j in range(len(ns)))
   rec["positive_cone_gordan_dual"]=[str(x) for x in weights]
   rec["status"]="empty-positive-cone";records.append(rec);stats[rec["status"]]+=1;continue
  pt=poly.representative_point();val=lambda z:sum(a*b for a,b in zip(z,pt))
  rec["positive_arms"]=[str(val(z)) for z in arms];rec["positive_e"]=[str(val(z)) for z in es];rec["positive_kernel_point"]=[str(x) for x in pt]
  sums=[{q(unit[i]+unit[j]) for j in range(8) if arms[other[i]]==arms[other[j]]} for i in range(8)]
  compat={(i,j) for i,j in product(range(8),repeat=2) if arms[i]==arms[j] or sums[i]&sums[j]}
  for H,g in enumerate(es):
   for i in range(8):
    if g in sums[i]:compat.add((8+H,i));compat.add((i,8+H))
   for G,h in enumerate(es):
    if g==h:compat.add((8+H,8+G))
  stars=[]
  for trip in combinations_with_replacement(range(6),3):
   for signs in product((0,1),repeat=3):
    banks=[corners[t] if not r else corners[t][::-1] for t,r in zip(trip,signs)]
    if all((banks[i][1],banks[(i+1)%3][0]) in compat for i in range(3)):
     stars.append(trip);break
  absent=sorted(set(range(6))-{i for t in stars for i in t})
  rec["allowed_120_stars"]=stars;rec["absent_native_corners"]=absent
  # Avoid a double-negation in the mathematical predicate: no core resonance
  # is an identity of this flat. Proper resonances are excluded in its stratum.
  rec["status"]="generic-120-corner-obstruction" if absent else "generic-local-survivor"
  rec["native_side_compatibility"]=sorted(compat)
  rec["arm_forms"]=[[str(t) for t in z] for z in arms];rec["e_forms"]=[[str(t) for t in z] for z in es]
  if rec["status"]=="generic-local-survivor" and len(ns)==2:
   parameter=next(i for i in range(8) if matrix(K,[arms[sharedP],arms[i]]).det()!=0)
   U=PolynomialRing(K,"u");u=U.gen();coordinates=matrix(K,[arms[sharedP],arms[parameter]]).inverse()*vector(U,[1,u])
   normal=lambda z:sum(t*x for t,x in zip(z,coordinates))
   normalized=[normal(z) for z in arms+es]
   lower=[];upper=[]
   for z in normalized:
    if z[1]>0:lower.append(-z[0]/z[1])
    elif z[1]<0:upper.append(-z[0]/z[1])
    else:assert z[0]>0
   lo=max(lower);hi=min(upper) if upper else None
   assert hi is None or lo<hi
   privacy=[];eventroots=[]
   for i,j in combinations(range(8),2):
    if(i,j)==crossmatch:continue
    delta=normalized[i]-normalized[j]
    assert delta!=0
    if delta[1]!=0:
     root=-delta[0]/delta[1]
     if lo<root and(hi is None or root<hi):privacy.append([i,j,str(root)])
   for j,h in enumerate(hyperplanes):
    delta=normal(q(h))
    if not delta:assert j in active;continue
    if delta[1]!=0:
     root=-delta[0]/delta[1]
     if lo<root and(hi is None or root<hi):eventroots.append([j,str(root)])
   cutroots=sorted({K(z[-1]) for z in privacy+eventroots});ends=[lo]+cutroots+[hi];chambers=[]
   for left,right in zip(ends,ends[1:]):
    sample=(left+right)/2 if right is not None else left+1
    values=[z(sample) for z in normalized]
    assert all(v>0 for v in values)
    assert all(values[i]!=values[j] for i,j in combinations(range(8),2) if(i,j)!=crossmatch)
    assert all(normal(q(h))(sample)!=0 for j,h in enumerate(hyperplanes) if j not in active)
    chambers.append({"interval":[str(left),None if right is None else str(right)],"sample_parameter":str(sample),"sample_arms":[str(v) for v in values[:8]],"sample_e":[str(v) for v in values[8:]],"native_arm_order":sorted(range(8),key=lambda i:(values[i],i))})
   rec["normalization_native_arm"]=sharedP
   rec["normalized_parameter_native_arm"]=parameter
   rec["normalized_arms"]=[str(z) for z in normalized[:8]];rec["normalized_e"]=[str(z) for z in normalized[8:]]
   rec["positive_ratio_interval"]=[str(lo),None if hi is None else str(hi)]
   rec["privacy_exclusions"]=privacy;rec["event_exclusions"]=eventroots;rec["generic_arm_order_chambers"]=chambers
  records.append(rec);stats[rec["status"]]+=1
  if len(ns)<=1:continue
  for j,h in enumerate(hyperplanes):
   if j in active:continue
   child=canonical(list(rows)+[h]);childkey=key(child)
   if childkey not in seen:seen.add(childkey);queue.append(child)
  if len(records)%100==0:print("CHECKPOINT",len(records),len(queue),dict(stats),flush=True)
 result={"scope":"complete positive privacy-preserving event/e intersection strata; native120 filter only, no imported old core obstruction", "native_cross_match":list(crossmatch),"hyperplane_names":names,"hyperplane_rows":[[str(t) for t in h] for h in hyperplanes],"counts":dict(stats),"records":records}
 print("FINAL",name,len(records),dict(stats),flush=True)
 print("SURVIVORS",name,[(r["flat_id"],r["dimension"],r["active_hyperplanes"]) for r in records if r["status"]=="generic-local-survivor"],flush=True)
 return result
ap=argparse.ArgumentParser();ap.add_argument("--orbit",choices=("mixed","isolated","all"),default="all");ap.add_argument("--output");args=ap.parse_args()
orbits={"mixed":(0,5),"isolated":(1,6)}
result={name:enumerate_orbit(name,pair) for name,pair in orbits.items() if args.orbit in(name,"all")}
if "mixed" in result:
 for rec in result["mixed"]["records"]:
  if rec["status"]!="generic-local-survivor" or rec["dimension"]!=3:continue
  assert rec["flat_id"]==121
  UV=PolynomialRing(K,names=("u","v"));u,v=UV.gens()
  arms=[UV(1),u,(3*w-u)/2,(w*u-1)/2,v,UV(1),w*v+(w*u-1)/2,(w-u)/2]
  es=[UV(2),u+v];allforms=arms+es
  for row in rec["constraint_rows"]:assert sum(K(t)*z for t,z in zip(row,arms))==0
  rec["normalization_native_arm"]=0;rec["normalized_two_parameter_native_arms"]=[1,4]
  rec["normalized_arms"]=[str(z) for z in arms];rec["normalized_e"]=[str(z) for z in es]
  rec["positive_two_parameter_region"]=["u>1/w","u<w","v>0"]
  rec["privacy_exclusion_forms"]=[[i,j,str(arms[i]-arms[j])] for i,j in combinations(range(8),2) if(i,j)!=(0,5)]
  rec["event_exclusion_forms"]=[[j,str(sum(K(t)*z for t,z in zip(row,arms)))] for j,row in enumerate(result["mixed"]["hyperplane_rows"]) if j not in rec["active_hyperplanes"]]
  generic=(K(4)/5,K(2));values=[z(*generic) for z in allforms]
  assert all(z>0 for z in values)
  assert all(UV(text)(*generic)!=0 for i,j,text in rec["privacy_exclusion_forms"])
  assert all(UV(text)(*generic)!=0 for j,text in rec["event_exclusion_forms"])
  rec["generic_two_parameter_fixture"]={"parameters":[str(z) for z in generic],"arms":[str(z) for z in values[:8]],"e":[str(z) for z in values[8:]]}
if args.output:
 with open(args.output,"w") as f:json.dump(result,f,indent=2);f.write("\n")
