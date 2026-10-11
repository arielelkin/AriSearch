"""Fresh root complete two-orbit flat audit using independent physical5-coordinates."""
import json
from itertools import product,combinations
from collections import deque,Counter
from sage.all import QuadraticField,AA,matrix,vector
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
z=[vector(K,[int(i==j) for j in range(5)]) for i in range(5)]
perp=(1,0,3,2,5,4,7,6)
corners=((0,8),(1,2),(3,8),(4,9),(5,6),(7,9))
D=json.load(open('research/certificates/partial-contact-cairo-other-one-shared-event-flats.json'))
def canon(rows):
 if not rows:return ()
 return tuple(tuple(t) for t in matrix(K,rows).echelon_form() if any(t))
for name,pair in (('mixed',(0,5)),('isolated',(1,6))):
 s,a,c,A,B=z
 if name=='mixed':
  # z1 is Pb; z4 is Qc in this orbit.
  fs=[s,a,c,s+(a-c)/w,A,s,B,A+(s-B)/w]
 else:fs=[a,s,c,a+(s-c)/w,A,B,s,A+(B-s)/w]
 fs += [w*fs[2]+fs[3]-2*fs[0],w*fs[6]+fs[7]-2*fs[4]]
 source=D[name];assert tuple(source['native_cross_match'])==pair
 sharedP,sharedQ=pair
 reps=[i for i in range(8) if i!=sharedQ]
 banks={perp[sharedP],perp[sharedQ]};cross=fs[perp[sharedP]]+fs[perp[sharedQ]]
 # Derive arrangement from actual bank/perpendicular slots, no author matrix.
 hypers=[cross-2*fs[i] for i in reps if i not in banks]
 sums=[2*fs[i] for i in reps]+[cross]
 hypers += [g-h for g in fs[8:] for h in sums]+[fs[8]-fs[9]]
 assert len(hypers)==22
 for retained,actual in zip(source['hyperplane_rows'],hypers):
  assert sum((K(t)*fs[j] for j,t in enumerate(retained)),vector(K,5))==actual
 lookup={};counts=Counter();survivors=[]
 for r in source['records']:
  native=matrix(K,[[K(t) for t in row] for row in r['constraint_rows']])
  assert tuple(tuple(t) for t in native)==canon(list(native))
  assert native.rank()==8-r['dimension']
  # Both physical closure forms and specified shared arm are included.
  closure=matrix(K,[[w,1,-1,-w,0,0,0,0],[0,0,0,0,w,1,-1,-w],
      [K(int(j==sharedP)-int(j==sharedQ)) for j in range(8)]])
  assert native.stack(closure).rank()==native.rank()
  reduced=canon([sum((t*fs[j] for j,t in enumerate(row)),vector(K,5)) for row in native])
  assert reduced not in lookup;lookup[reduced]=r
  kernel=matrix(K,list(reduced)).right_kernel().basis() if reduced else matrix(K,0,5).right_kernel().basis()
  assert len(kernel)==r['dimension']
  q=lambda f:tuple(f.dot_product(k) for k in kernel)
  vs=[q(f) for f in fs]
  active=[j for j,h in enumerate(hypers) if not any(q(h))]
  assert active==r['active_hyperplanes'] and canon([hypers[j] for j in active])==reduced
  privacy=any(vs[i]==vs[j] for i,j in combinations(range(8),2) if (i,j)!=pair)
  if privacy:assert r['status']=='forced-extra-arm';counts[r['status']]+=1;continue
  if r['status']=='empty-positive-cone':
   weights=list(map(K,r['positive_cone_gordan_dual']))
   assert len(weights)==10 and all(v>=0 for v in weights) and sum(weights)==1
   assert all(sum(a*f[j] for a,f in zip(weights,vs))==0 for j in range(len(kernel)))
   counts[r['status']]+=1;continue
  point=list(map(K,r['positive_arms']));es=list(map(K,r['positive_e']))
  assert all(v>=1 for v in point+es)
  assert point[1]-point[2]==w*(point[3]-point[0])
  assert point[5]-point[6]==w*(point[7]-point[4]) and point[sharedP]==point[sharedQ]
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
 print('PASS',name,len(seen),'all canonical flats, actual22form arrangement, safe full BFS, exact positive/Gordan proofs and orderednative120 inventory; counts',dict(counts),'survivors',survivors)
print('PASS two other sole-cross orbits: full relative-stratum coverage; no generic-only root assumption or unreviewed core import')
