"""Fresh root two-cross flat audit in six length labels/four free coordinates.
No author imports or solvers. The independent event omissions are derived
from support of six-label difference forms before native closure, not the
producer's bank-case predicates. Contact-negative ancestors always expand.
"""
import argparse,json
from itertools import product,combinations
from collections import deque,Counter
from sage.all import QuadraticField,AA,matrix,vector
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
perp=(1,0,3,2,5,4,7,6)
corners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
ap=argparse.ArgumentParser();ap.add_argument('--source');a=ap.parse_args()
sources=[a.source] if a.source else ['research/certificates/partial-contact-cairo-two-cross-event-flats.json','research/certificates/partial-contact-cairo-remaining-two-cross-event-flats.json']
D={}
for source_path in sources:
 with open(source_path) as source_file: block=json.load(source_file)
 assert not set(D).intersection(block)
 D.update(block)
def canon(rows):
 if not rows:return ()
 return tuple(tuple(t) for t in matrix(K,rows).echelon_form() if any(t))
for name,source in D.items():
 pairs=list(map(tuple,source['native_cross_matches']));declared=set(pairs)
 assert len(pairs)==2 and len({i for i,j in pairs})==len({j for i,j in pairs})==2
 groups=[{i,j} for i,j in pairs]+[{i} for i in range(8) if all(i not in p for p in pairs)]
 groups=sorted(groups,key=min);assert len(groups)==6
 labels=[next(j for j,g in enumerate(groups) if i in g) for i in range(8)]
 unit=[vector(K,[int(j==labels[i]) for j in range(6)]) for i in range(8)]
 closure6=matrix(K,[w*unit[0]+unit[1]-unit[2]-w*unit[3],w*unit[4]+unit[5]-unit[6]-w*unit[7]])
 k6=closure6.right_kernel().basis();nfree=len(k6);assert nfree==4
 fs=[vector(K,[t[labels[i]] for t in k6]) for i in range(8)]
 fs += [w*fs[2]+fs[3]-2*fs[0],w*fs[6]+fs[7]-2*fs[4]]
 reps=[min(g) for g in groups]
 bankclasses=sorted({tuple(sorted((reps[labels[i]],reps[labels[j]]))) for i,j in product(range(8),repeat=2) if fs[perp[i]]==fs[perp[j]]})
 assert bankclasses==list(map(tuple,source['event_bank_classes']))
 events=[fs[i]+fs[j] for i,j in bankclasses];events6=[unit[i]+unit[j] for i,j in bankclasses]
 for row,f in zip(source['event_rows'],events):assert sum((K(t)*fs[j] for j,t in enumerate(row)),vector(K,nfree))==f
 hypers=[];omitted=[]
 for i,j in combinations(range(len(events)),2):
  diff6=events6[i]-events6[j];support=[t for t in diff6 if t]
  assert support
  if len(support)==2 and sum(support)==0:omitted.append([i,j])
  else:hypers.append(events[i]-events[j])
 assert omitted==source['omitted_event_differences_forcing_extra_arm']
 hypers += [g-h for g in fs[8:] for h in events]+[fs[8]-fs[9]]
 assert len(hypers)==len(source['hyperplane_rows'])
 for row,f in zip(source['hyperplane_rows'],hypers):assert sum((K(t)*fs[j] for j,t in enumerate(row)),vector(K,nfree))==f
 lookup={};counts=Counter();survivors=[]
 for r in source['records']:
  native=matrix(K,[[K(t) for t in row] for row in r['constraint_rows']])
  assert tuple(tuple(t) for t in native)==canon(list(native))
  assert native.rank()==8-r['dimension']
  # Both physical closure forms and specified shared arm are included.
  closure=matrix(K,[[w,1,-1,-w,0,0,0,0],[0,0,0,0,w,1,-1,-w],
      *[ [K(int(j==i)-int(j==k)) for j in range(8)] for i,k in pairs]])
  assert native.stack(closure).rank()==native.rank()
  reduced=canon([sum((t*fs[j] for j,t in enumerate(row)),vector(K,nfree)) for row in native])
  assert reduced not in lookup;lookup[reduced]=r
  kernel=matrix(K,list(reduced)).right_kernel().basis() if reduced else matrix(K,0,nfree).right_kernel().basis()
  assert len(kernel)==r['dimension']
  q=lambda f:tuple(f.dot_product(k) for k in kernel)
  vs=[q(f) for f in fs]
  active=[j for j,h in enumerate(hypers) if not any(q(h))]
  assert active==r['active_hyperplanes'] and canon([hypers[j] for j in active])==reduced
  privacy=any(vs[i]==vs[j] for i,j in combinations(range(8),2) if (i,j) not in declared)
  if privacy:assert r['status']=='forced-extra-arm';counts[r['status']]+=1;continue
  if r['status']=='empty-positive-cone':
   weights=list(map(K,r['positive_cone_gordan_dual']))
   assert len(weights)==10 and all(v>=0 for v in weights) and sum(weights)==1
   assert all(sum(a*f[j] for a,f in zip(weights,vs))==0 for j in range(len(kernel)))
   counts[r['status']]+=1;continue
  point=list(map(K,r['positive_arms']));es=list(map(K,r['positive_e']))
  assert all(v>=1 for v in point+es)
  assert point[1]-point[2]==w*(point[3]-point[0])
  assert point[5]-point[6]==w*(point[7]-point[4]) and all(point[i]==point[j] for i,j in pairs)
  assert es==[w*point[2]+point[3]-2*point[0],w*point[6]+point[7]-2*point[4]]
  assert native*vector(K,point)==0
  nativebasis=native.right_kernel().basis()
  assert [list(map(K,f)) for f in r['arm_forms']]==[[t[j] for t in nativebasis] for j in range(8)]
  assert [list(map(K,f)) for f in r['e_forms']]==[[w*t[2]+t[3]-2*t[0] for t in nativebasis],[w*t[6]+t[7]-2*t[4] for t in nativebasis]]
  assert [sum(a*b for a,b in zip(map(K,f),map(K,r['positive_kernel_point']))) for f in r['arm_forms']+r['e_forms']]==point+es
  ev=[(i,j,tuple(x+y for x,y in zip(vs[i],vs[j]))) for i,j in product(range(8),repeat=2) if vs[perp[i]]==vs[perp[j]]]
  totals=[{t for i,j,t in ev if i==h or j==h} for h in range(8)]
  def match(i,j):
   if i<8 and j<8:return vs[i]==vs[j] or bool(totals[i]&totals[j])
   if i>=8 and j>=8:return vs[i]==vs[j]
   if i>=8:i,j=j,i
   return vs[j] in totals[i]
  assert list(map(tuple,r['native_side_compatibility']))==[(i,j) for i,j in product(range(10),repeat=2) if match(i,j)]
  allowed=set()
  for trip in product(range(6),repeat=3):
   for bits in product((0,1),repeat=3):
    cc=[corners[t][::(-1 if flip else 1)] for t,flip in zip(trip,bits)]
    if all(match(cc[i][1],cc[(i+1)%3][0]) for i in range(3)):allowed.add(tuple(sorted(trip)))
  assert sorted(allowed)==list(map(tuple,r['allowed_120_stars']))
  absent=sorted(set(range(6))-{t for star in allowed for t in star})
  assert absent==r['absent_native_corners']
  expected='generic-120-corner-obstruction' if absent else 'generic-local-survivor'
  assert r['status']==expected;counts[expected]+=1
  if not absent:survivors.append((r['flat_id'],r['dimension']))
 # Independent BFS never prunes any native/contact negative node.
 root=();queue=deque([root]);seen={root}
 while queue:
  flat=queue.popleft();assert flat in lookup
  r=lookup[flat]
  if r['status'] in ('forced-extra-arm','empty-positive-cone') or r['dimension']<=1:continue
  for h in hypers:
   child=canon(list(flat)+[h])
   if child not in seen:seen.add(child);queue.append(child)
 assert seen==set(lookup) and dict(counts)==source['counts']
 print('PASS',name,len(seen),'all canonical flats, complete actual event arrangement, safe full BFS, exact positive/Gordan proofs and orderednative120 inventory; counts',dict(counts),'survivors',survivors)
print('PASS complete specified two-cross flat domains; no unreviewed core/LP or tiling-existence import')
