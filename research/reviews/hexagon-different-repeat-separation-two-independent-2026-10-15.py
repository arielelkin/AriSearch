"""Independent exhaustive different-repeat source/contact audit.
Stdlib only; no producer imports, numerical lengths, solver or quotient search.
"""
from itertools import combinations,permutations,product
from pathlib import Path
import json
A=(0,1,0,2,3,4)

def normalize(B,p):
 views={tuple(B[(i+d*k)%6] for k in range(6)) for i,d in product(range(6),(-1,1))}
 candidates=[w for w in views if w[0]==w[2]==p]
 assert len(candidates)==2
 return min(candidates)
raw={(p,q[0],p,*q[1:]) for p in (1,2,3,4) for q in permutations(tuple(c for c in range(5) if c!=p))}
normalized=sorted({normalize(w,w[0]) for w in raw})
assert len(raw)==96 and len(normalized)==48
ROOT=Path(__file__).resolve().parents[1]
cert=json.loads((ROOT/'certificates/hexagon-different-repeat-separation-two-gate-2026-10-15.json').read_text())
assert cert['A']==list(A) and cert['colors']==list(range(5))
assert len(cert['raw_words'])==96 and {tuple(w) for w in cert['raw_words']}==raw
assert cert['normalized_words']==[list(w) for w in normalized]
assert len(cert['records'])==48

survivors=empty=support_count=0
for B,record in zip(normalized,cert['records']):
 assert record['B']==list(B)
 words=(A,B)
 labels={6*f+i:words[f][i] for f in range(2) for i in range(6)}
 endpoints={6*f+i:frozenset((6*f+(i-1)%6,6*f+i)) for f in range(2) for i in range(6)}
 ports={corner:tuple(side for side in endpoints if corner in endpoints[side]) for corner in range(12)}
 arms={c:frozenset(labels[side] for side in ports[c]) for c in ports}
 assert all(len(pair)==2 for pair in arms.values())
 # Build from three ray colors and the actual slot choices on their pairs.
 atlas=set()
 for rays in combinations(range(5),3):
  pairs=tuple(map(frozenset,combinations(rays,2)))
  for corners in product(*(tuple(c for c in range(12) if arms[c]==pair) for pair in pairs)):
   assert len(set(corners))==3
   atlas.add(tuple(sorted(corners)))
 atlas=sorted(atlas)
 assert all(any(c<6 for c in s) and any(c>=6 for c in s) for s in atlas)
 assert record['initial_atlas']==[list(t) for t in atlas]
 def demand(c,d):
  color,=arms[c]&arms[d]
  first,=tuple(side for side in ports[c] if labels[side]==color)
  second,=tuple(side for side in ports[d] if labels[side]==color)
  cc,=endpoints[first]-{c}
  dd,=endpoints[second]-{d}
  return (c,d,color,cc,dd),tuple(sorted((first,second)))
 def possible(star,current):
  for c,d in combinations(star,2):
   q,_=demand(c,d);cc,dd=q[3:]
   if cc==dd or not any(cc in t and dd in t for t in current):return False
  return True
 current=atlas;sizes=[len(atlas)]
 for step in record['pruning_rounds']:
  assert step['input']==[list(t) for t in current]
  after=[t for t in current if possible(t,current)]
  assert step['output']==[list(t) for t in after]
  assert len(step['removed'])==len(current)-len(after)
  assert {tuple(x['star']) for x in step['removed']}==set(current)-set(after)
  for removed in step['removed']:
   star=tuple(removed['star']);q=tuple(removed['failed_demand'])
   c,d=q[:2]
   assert c!=d and c in star and d in star and q==demand(c,d)[0]
   cc,dd=q[3:]
   assert cc==dd or not any(cc in t and dd in t for t in current)
  current=after;sizes.append(len(current))
 assert all(possible(t,current) for t in current)
 assert record['pruning_sizes']==sizes
 assert record['fixed_point']==[list(t) for t in current]
 covered=sorted(set(c for t in current for c in t))
 assert record['covered_corners']==covered
 def graph(stars):
  edges=sorted({demand(c,d)[1] for t in stars for c,d in combinations(t,2)})
  adjacency={i:set() for i in range(12)}
  for a,b in edges:
   assert labels[a]==labels[b]
   adjacency[a].add(b);adjacency[b].add(a)
  components=[];unseen=set(range(12))
  while unseen:
   reached={min(unseen)}
   while True:
    bigger=reached|{v for u in reached for v in adjacency[u]}
    if bigger==reached:break
    reached=bigger
   assert len({labels[i] for i in reached})==1
   components.append(tuple(sorted(reached)));unseen-=reached
  components=sorted(components)
  joins=[any(a in group and b in group for group in components) for a,b in ((0,2),(6,8))]
  return edges,components,joins
 edges,components,joins=graph(current)
 assert record['fixed_point_seams']==[list(e) for e in edges]
 assert record['fixed_point_components']==[list(g) for g in components]
 assert record['fixed_point_repeated_joined']==joins
 if current:
  survivors+=1
  assert covered==list(range(12)) and not all(joins)
 else:empty+=1
 accepted=[]
 for mask in range(1<<len(current)):
  selected=[t for i,t in enumerate(current) if mask&(1<<i)]
  if {c for t in selected for c in t}!=set(range(12)):continue
  if not all(possible(t,selected) for t in selected):continue
  es,cs,js=graph(selected)
  assert not all(js)
  accepted.append(dict(mask_in_fixed_point=mask,stars=[list(t) for t in selected],seams=[list(e) for e in es],components=[list(g) for g in cs],A_repeated_joined=js[0],B_repeated_joined=js[1]))
 assert record['endpoint_closed_corner_cover_supports']==accepted
 support_count+=len(accepted)
assert (survivors,empty,support_count)==(8,40,36)
assert cert['summary']==dict(raw_words=96,normalized_words=48,empty_fixed_points=40,covering_fixed_points=8,actual_support_candidates=36)
print('PASS:96 raw words,48 full-dihedral normalized forms,40 empty fixed points,8 complete native seam graphs with repeated-pair disconnection,36 exact endpoint-closed corner covers. Includes all side colors and loops; no physical length injectivity used.')
