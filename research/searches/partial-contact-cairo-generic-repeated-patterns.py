"""Exact collapsed-internal-label Cairo cross patterns; necessary generic tests."""
import argparse,json
from collections import Counter,defaultdict
from itertools import combinations,permutations,product,combinations_with_replacement
from sage.all import QuadraticField,matrix,vector,Polyhedron
K=QuadraticField(3,"w");w=K.gen();unit=[vector(K,[int(i==j) for j in range(8)]) for i in range(8)]
base=[w*unit[0]+unit[1]-unit[2]-w*unit[3],w*unit[4]+unit[5]-unit[6]-w*unit[7]]
Erow=-2*unit[0]+w*unit[2]+unit[3];Frow=-2*unit[4]+w*unit[6]+unit[7];other=(1,0,3,2,5,4,7,6)
types={'D':((0,),(1,),(2,),(3,)),'R01':((0,1),(2,),(3,)),'R23':((0,),(1,),(2,3)),'S':((0,3),(1,2))}
mono_slot={'R01':0,'R23':3,'S':0}
periodic_bases={'swapped-arm-cone':((0,2),(2,0)),'reviewed-Y-cone':((1,3),(2,0))};orbits={}
for name,basepat in periodic_bases.items():
 for ra,rb,swap in product((0,1),repeat=3):
  pairs=[(3-i if ra else i,3-j if rb else j) for i,j in basepat]
  if swap:pairs=[(j,i) for i,j in pairs]
  orbits[tuple(sorted(pairs))]=(name,ra,rb,swap)
assert len(orbits)==8
records=[]
for typeP,typeQ in product(types,repeat=2):
 partsP,partsQ=types[typeP],types[typeQ]
 blockP={i:k for k,b in enumerate(partsP) for i in b};blockQ={i:k for k,b in enumerate(partsQ) for i in b}
 internal=[]
 for offset,parts in ((0,partsP),(4,partsQ)):
  internal += [unit[offset+i]-unit[offset+b[0]] for b in parts for i in b[1:]]
 for k in range(min(len(partsP),len(partsQ))+1):
  for aa in combinations(range(len(partsP)),k):
   for bb in combinations(range(len(partsQ)),k):
    for perm in permutations(bb):
     pairs=list(zip(aa,perm));declared=set(pairs)
     rows=base+internal+[unit[partsP[i][0]]-unit[4+partsQ[j][0]] for i,j in pairs]
     ns=matrix(K,rows).right_kernel().basis();q=lambda x:tuple(x.dot_product(v) for v in ns)
     arms=[q(x) for x in unit];e,f=q(Erow),q(Frow)
     rec={'internal_types':[typeP,typeQ],'cross_block_matches':[list(z) for z in pairs],'dimension':len(ns)}
     bad=False
     for i,j in combinations(range(8),2):
      wanted=(blockP[i]==blockP[j] if j<4 else blockQ[i-4]==blockQ[j-4] if i>=4 else(blockP[i],blockQ[j-4]) in declared)
      if (arms[i]==arms[j])!=wanted:bad=True
     if bad:rec['status']='forced-extra-arm-equality';records.append(rec);continue
     positive=Polyhedron(ieqs=[[-K(1)]+list(z) for z in arms+[e,f]],base_ring=K,backend='field')
     if positive.is_empty():rec['status']='empty-positive-cone';records.append(rec);continue
     point=positive.representative_point();values=lambda z:sum(t*x for t,x in zip(z,point))
     assert all(values(z)>=1 for z in arms+[e,f])
     rec['positive_kernel_point']=[str(z) for z in point];rec['positive_arms']=[str(values(z)) for z in arms];rec['positive_e']=[str(values(z)) for z in(e,f)]
     nativecross={(i,j) for i,j in product(range(4),repeat=2) if arms[i]==arms[4+j]}
     containing=[(pat,meta) for pat,meta in orbits.items() if set(pat)<=nativecross]
     if containing:
      pat,meta=min(containing);rec['periodic_family']=meta[0];rec['sufficient_native_pattern']=[list(x) for x in pat];rec['native_reflection_and_swap']=list(meta[1:])
     mono=[]
     for H,tp in enumerate((typeP,typeQ)):
      if tp in mono_slot and (e,f)[H]==tuple(2*x for x in arms[4*H+mono_slot[tp]]):mono.append(H)
     if mono:rec['mono_periodic_species']=mono
     events=[(q(unit[i]+unit[j]),(i,j)) for i,j in combinations_with_replacement(range(8),2) if arms[other[i]]==arms[other[j]]]
     forced_e=[H for H,g in enumerate((e,f)) if g in {s for s,banks in events}]
     rec['forced_e_event_species']=forced_e
     if forced_e:
      rec['status']=('mono-periodic' if mono else 'known-partner-periodic' if containing else 'forced-e-event-unclassified');records.append(rec);continue
     assert not mono
     sums_by_slot=[{q(unit[i]+unit[j]) for j in range(8) if arms[other[i]]==arms[other[j]]} for i in range(8)]
     compat={(i,j) for i,j in product(range(8),repeat=2) if arms[i]==arms[j] or sums_by_slot[i]&sums_by_slot[j]}
     allowed=[]
     for H,G,orient in product(range(2),repeat=3):
      if(e,f)[H]!=(e,f)[G]:continue
      endpoints=[(4*H+3,4*G+(3 if orient==0 else 0)),(4*H,4*G+(0 if orient==0 else 3))]
      if all(any(((i,4*T+1) in compat and(j,4*T+2) in compat) or((i,4*T+2) in compat and(j,4*T+1) in compat) for T in range(2)) for i,j in endpoints):allowed.append([H,G,orient])
     survivor=all(any(z[0]==H for z in allowed) for H in range(2))
     rec['allowed_e_seams']=allowed;rec['native_slot_compatibility']=[list(z) for z in sorted(compat)]
     rec['status']=('generic-periodic-survivor' if containing else 'generic-local-survivor-uncovered') if survivor else 'generic-beta-obstruction'
     assert not containing or survivor,(typeP,typeQ,pairs)
     rec['arm_forms']=[[str(x) for x in z] for z in arms];rec['e_forms']=[[str(x) for x in z] for z in(e,f)]
     records.append(rec)
assert len(records)==738
counts=Counter(r['status'] for r in records)
assert counts=={'forced-extra-arm-equality':70,'generic-beta-obstruction':517,'generic-periodic-survivor':151}
for number,rec in enumerate(records):rec['pattern_id']=number
bytypes=defaultdict(Counter)
for r in records:bytypes[tuple(r['internal_types'])][r['status']]+=1
result={'scope':'738 ordered collapsed-internal-label cross patterns over D,R01,R23,S; positive exact quotient cones; generic e/event exclusions; necessary native-slot contact filters only','records':records,'counts':dict(counts),'counts_by_internal_type_pair':{'/'.join(k):dict(v) for k,v in bytypes.items()}}
ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
if args.output:
 with open(args.output,'w') as out:json.dump(result,out,indent=2);out.write('\n')
print(json.dumps(result['counts'],sort_keys=True))
print(json.dumps(result['counts_by_internal_type_pair'],sort_keys=True))
print('UNCOVERED',[(r['internal_types'],r['cross_block_matches'],r['status']) for r in records if r['status'] in ('generic-local-survivor-uncovered','forced-e-event-unclassified')])
