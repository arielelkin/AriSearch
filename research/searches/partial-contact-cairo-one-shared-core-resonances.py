"""Generic strata on twelve exceptional one-shared-arm core hyperplanes."""
from sage.all import QuadraticField,matrix,vector,Polyhedron
from itertools import combinations_with_replacement,product,combinations
import json,argparse
K=QuadraticField(3,"w");w=K.gen();unit=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
base=[w*unit[0]+unit[1]-unit[2]-w*unit[3],w*unit[4]+unit[5]-unit[6]-w*unit[7],unit[0]-unit[7]]
E=-2*unit[0]+w*unit[2]+unit[3];F=-2*unit[4]+w*unit[6]+unit[7]
other=(1,0,3,2,5,4,7,6);corners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
records=[]
for name,L in(("cross-bank",unit[1]+unit[6]),("eP",E),("eQ",F)):
 for slot in(2,3,4,5):
  ns=matrix(K,base+[L-2*unit[slot]]).right_kernel().basis();q=lambda v:tuple(v.dot_product(x) for x in ns)
  arms=[q(x) for x in unit];es=[q(E),q(F)];rec={"resonance":[name,slot],"dimension":len(ns)}
  extras=[(i,j) for i,j in combinations(range(8),2) if arms[i]==arms[j] and(i,j)!=(0,7)]
  if extras:rec["status"]="forced-extra-arm";rec["extra_equalities"]=extras;records.append(rec);continue
  poly=Polyhedron(ieqs=[[-K(1)]+list(z) for z in arms+es],base_ring=K,backend="field")
  if poly.is_empty():rec["status"]="empty-positive-cone";records.append(rec);continue
  pt=poly.representative_point();val=lambda z:sum(a*b for a,b in zip(z,pt))
  rec["positive_arms"]=[str(val(z)) for z in arms];rec["positive_e"]=[str(val(z)) for z in es]
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
  rec["native_side_compatibility"]=sorted(compat)
  rec["status"]="generic-120-corner-obstruction" if absent else "generic-local-survivor"
  rec["arm_forms"]=[[str(t) for t in z] for z in arms];rec["e_forms"]=[[str(t) for t in z] for z in es]
  records.append(rec)
p=argparse.ArgumentParser();p.add_argument("--output");a=p.parse_args()
if a.output:
 with open(a.output,"w") as f:json.dump(records,f,indent=2);f.write("\n")
for r in records:print(r["resonance"],r["status"],r.get("absent_native_corners"),r.get("allowed_120_stars"))
