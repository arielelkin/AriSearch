"""Exact209 cross-arm patterns; conditional generic contact necessities only.
Run nondestructively; --output explicitly retains JSON.
"""
import argparse,json
from itertools import combinations,permutations,product,combinations_with_replacement
from collections import Counter
from sage.all import QuadraticField,matrix,vector,Polyhedron
K=QuadraticField(3,"w");w=K.gen()
unit=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
base=[vector(K,[w,1,-1,-w,0,0,0,0]),vector(K,[0,0,0,0,w,1,-1,-w])]
mates=[1,0,3,2,5,4,7,6]
Erow=-2*unit[0]+w*unit[2]+unit[3]
Frow=-2*unit[4]+w*unit[6]+unit[7]
records=[]
for k in range(5):
    for aa in combinations(range(4),k):
        for bb in combinations(range(4),k):
            for perm in permutations(bb):
                pairs=list(zip(aa,perm))
                rows=base+[unit[i]-unit[j+4] for i,j in pairs]
                ns=matrix(K,rows).right_kernel().basis()
                q=lambda row:tuple(row.dot_product(v) for v in ns)
                arms=[q(x) for x in unit]
                declared=set(pairs)
                bad=False
                for i,j in combinations(range(8),2):
                    wanted=(i<4<=j and(i,j-4) in declared)
                    if (arms[i]==arms[j])!=wanted:bad=True
                rec={"cross_matches":[list(x) for x in pairs],"dimension":len(ns)}
                if bad:
                    rec["status"]="forced-extra-arm-equality";rec["anchored_status"]=rec["status"];records.append(rec);continue
                events=[]
                for i,j in combinations_with_replacement(range(8),2):
                    if arms[i]==arms[j]:
                        banks=(mates[i],mates[j])
                        events.append((q(unit[banks[0]]+unit[banks[1]]),banks))
                e,f=q(Erow),q(Frow)
                positive=Polyhedron(ieqs=[[-K(1)]+list(z) for z in arms+[e,f]],base_ring=K,backend="field")
                if positive.is_empty():
                    rec["status"]="empty-positive-cone";records.append(rec);continue
                point=positive.representative_point()
                assert all(sum(t*x for t,x in zip(z,point))>=1 for z in arms+[e,f])
                rec["positive_parameter_point"]=[str(x) for x in point]
                rec["positive_arm_values"]=[str(sum(t*x for t,x in zip(z,point))) for z in arms]
                rec["positive_e_values"]=[str(sum(t*x for t,x in zip(z,point))) for z in(e,f)]
                if e in [x[0] for x in events] or f in [x[0] for x in events]:
                    rec["status"]="forced-e-event-sum";records.append(rec);continue
                compat={(x,x) for x in arms}
                for ev in {t for t,banks in events}:
                    bankvals={arms[j] for t,banks in events if t==ev for j in banks}
                    compat.update(product(bankvals,repeat=2))
                evalues=[e,f]
                allowed=[]
                isolated=[(arms[1],arms[2]),(arms[5],arms[6])]
                for H in range(2):
                    for G in range(2):
                        if evalues[H]!=evalues[G]:continue
                        for orient in (0,1):
                            endpoints=[(arms[4*H+3],arms[4*G+(3 if orient==0 else 0)]),
                                       (arms[4*H],arms[4*G+(0 if orient==0 else 3)])]
                            if all(any(((x,u) in compat and(y,v) in compat) or((x,v) in compat and(y,u) in compat) for u,v in isolated) for x,y in endpoints):
                                allowed.append([H,G,orient])
                rec["allowed_e_seams"]=allowed
                if all(any(x[0]==H for x in allowed) for H in(0,1)):
                    rec["status"]="local-survivor"
                else:rec["status"]="generic-beta-obstruction"
                # Native slot anchoring: bank arm i can participate only in
                # perpendicular seams matching its own90-complement mates[i].
                sums_by_slot=[{q(unit[i]+unit[j]) for j in range(8)
                               if arms[mates[i]]==arms[mates[j]]} for i in range(8)]
                slotcompat={(i,j) for i,j in product(range(8),repeat=2)
                            if arms[i]==arms[j] or sums_by_slot[i]&sums_by_slot[j]}
                anchored_allowed=[]
                for H,G,orient in product(range(2),range(2),range(2)):
                    if evalues[H]!=evalues[G]:continue
                    endpoints=[(4*H+3,4*G+(3 if orient==0 else 0)),
                               (4*H,4*G+(0 if orient==0 else 3))]
                    if all(any(((i,4*T+1) in slotcompat and(j,4*T+2) in slotcompat)
                               or((i,4*T+2) in slotcompat and(j,4*T+1) in slotcompat)
                               for T in range(2)) for i,j in endpoints):
                        anchored_allowed.append([H,G,orient])
                rec["anchored_allowed_e_seams"]=anchored_allowed
                rec["anchored_slot_compatibility"]=[list(z) for z in sorted(slotcompat)]
                rec["anchored_status"]=("local-survivor" if all(any(z[0]==H for z in anchored_allowed) for H in range(2))
                                         else "generic-beta-obstruction")
                rec["arms"]=[[str(x) for x in arm] for arm in arms]
                rec["e_forms"]=[[str(x) for x in z] for z in(e,f)]
                records.append(rec)
assert len(records)==209
# Test which locally surviving patterns contain a sufficient periodic
# two-equality pattern under native Cairo reflection and species exchange.
bases={"swapped-arm-cone":((0,2),(2,0)),"reviewed-Y-cone":((1,3),(2,0))}
orbits={}
for name,base in bases.items():
    for ra,rb,swap in product((0,1),repeat=3):
        pairs=[(3-i if ra else i,3-j if rb else j) for i,j in base]
        if swap:pairs=[(j,i) for i,j in pairs]
        key=tuple(sorted(pairs));orbits[key]=(name,ra,rb,swap)
assert len(orbits)==8
for rec in records:
    if rec["status"]!="local-survivor":continue
    actual=set(map(tuple,rec["cross_matches"]))
    containing=[(pat,meta) for pat,meta in orbits.items() if set(pat).issubset(actual)]
    if not containing:
        rec["periodic_family"]="anchored-beta-obstruction"
        continue
    pat,meta=min(containing)
    rec["sufficient_periodic_pattern"]=[list(z) for z in pat]
    rec["periodic_family"]=meta[0]
    rec["native_reflection_and_swap"]=[meta[1],meta[2],meta[3]]
assert sum(r.get("periodic_family")=="anchored-beta-obstruction" for r in records)==8
assert sum(r.get("periodic_family") in bases for r in records)==32
assert Counter(r["anchored_status"] for r in records)=={"forced-extra-arm-equality":22,"generic-beta-obstruction":155,"local-survivor":32}
assert all(r["anchored_status"]!="local-survivor" or r.get("periodic_family") in bases for r in records)
result={"scope":"209 exact cross-arm equality patterns; generic event/e equalities; necessary contact rules only; exact positive cones checked", "records":records,"counts":dict(Counter(x["status"] for x in records)),"anchored_counts":dict(Counter(x["anchored_status"] for x in records))}
ap=argparse.ArgumentParser();ap.add_argument("--output");args=ap.parse_args()
if args.output:
    with open(args.output,"w") as out:json.dump(result,out,indent=2);out.write("\n")
print(json.dumps(result["counts"],sort_keys=True))
print("anchored",json.dumps(result["anchored_counts"],sort_keys=True))
print("survivors",[x["cross_matches"] for x in records if x["status"]=="local-survivor"])
