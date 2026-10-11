"""Independent complete one-shared event arrangement audit in five free metrics.
No author imports or solvers. Positive witnesses and Gordan duals checked directly.
"""
from sage.all import QuadraticField,AA,matrix,vector,PolynomialRing
from itertools import product,combinations,combinations_with_replacement
from collections import Counter,deque
from pathlib import Path
import json,re
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
unit=[vector(K,[int(i==j) for j in range(5)]) for i in range(5)]
s,b,d,A,B=unit;c=b+w*s-w*d;C=B+w*A-w*s
arms=[s,b,c,d,A,B,C,s];es=[s+w*b-2*d,A+w*B-2*s];lengths=arms+es
cross=b+C;events=[2*x for x in arms[:7]]+[cross]
hyper=[cross-2*arms[i] for i in (0,2,3,4,5)]+[e-h for e in es for h in events]+[es[0]-es[1]]
assert len(hyper)==22
# All possible remaining event/event changes, after exact privacy exclusions.
labels=[0,1,2,3,4,5,6,0];perp=[1,0,3,2,5,4,7,6]
nativeevents={(tuple(sorted((labels[i],labels[j])))) for i,j in combinations_with_replacement(range(8),2) if labels[perp[i]]==labels[perp[j]]}
assert nativeevents=={(i,i) for i in range(7)}|{(1,6)}
L=matrix(K,arms)
def canon(rows):
 m=matrix(K,rows) if rows else matrix(K,0,5)
 return tuple(tuple(row) for row in m.echelon_form().rows() if any(row))
def M(rows):return matrix(K,rows) if rows else matrix(K,0,5)
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'certificates/partial-contact-cairo-one-shared-event-flats.json').read_text())
assert len(data['records'])==1639 and [r['flat_id'] for r in data['records']]==list(range(1639))
for expected,encoded in zip(hyper,data['hyperplane_rows']):assert vector(K,encoded)*L==expected
records={};counts=Counter();positives=0;duals=0;chambers=0;fixture_extra=0
base8=matrix(K,[[w,1,-1,-w,0,0,0,0],[0,0,0,0,w,1,-1,-w],[1,0,0,0,0,0,0,-1]])
for r in data['records']:
 encoded=matrix(K,r['constraint_rows'])
 assert encoded==encoded.echelon_form() and encoded.rank()==encoded.nrows()
 assert encoded.rank()==8-r['dimension']
 assert encoded.stack(base8).rank()==encoded.rank()
 restricted=[vector(K,row)*L for row in r['constraint_rows']];key=canon(restricted)
 assert key not in records;records[key]=r
 assert key==canon([hyper[i] for i in r['active_hyperplanes']])
 ns=M(key).right_kernel().basis();q=lambda v:vector(K,[v.dot_product(n) for n in ns])
 af=[q(a) for a in arms];ef=[q(e) for e in es]
 active=[i for i,h in enumerate(hyper) if not any(q(h))]
 assert active==r['active_hyperplanes'] and len(ns)==r['dimension']
 bad=any(af[i]==af[j] for i,j in combinations(range(8),2) if (i,j)!=(0,7))
 counts[r['status']]+=1
 if bad:assert r['status']=='forced-extra-arm';continue
 assert r['status']!='forced-extra-arm'
 if r['status']=='empty-positive-cone':
  weights=[K(z) for z in r['positive_cone_gordan_dual']]
  assert len(weights)==10 and all(z>=0 for z in weights) and sum(weights)==1
  weighted=sum((z*form for z,form in zip(weights,lengths)),vector(K,[0]*5))
  assert not any(q(weighted));duals+=1;continue
 vals=[K(z) for z in r['positive_arms']];evalues=[K(z) for z in r['positive_e']]
 assert all(z>=1 for z in vals+evalues)
 free=vector(K,[vals[i] for i in (0,1,3,4,5)])
 assert vals==[a.dot_product(free) for a in arms] and evalues==[a.dot_product(free) for a in es]
 assert all(row.dot_product(free)==0 for row in M(key).rows())
 positives+=1
 fixture_extra+=any(vals[i]==vals[j] for i,j in combinations(range(8),2) if(i,j)!=(0,7))
 # Exact native slot compatibility, including hosted e/arm and whole e/e rays.
 sums=[set() for _ in arms]
 for i,j in product(range(8),repeat=2):
  if af[perp[i]]==af[perp[j]]:sums[i].add(tuple(q(arms[i]+arms[j])))
 compat={(i,j) for i,j in product(range(8),repeat=2) if af[i]==af[j] or sums[i]&sums[j]}
 for H,e in enumerate(ef):
  for i in range(8):
   if tuple(e) in sums[i]:compat|={(8+H,i),(i,8+H)}
  for G,f in enumerate(ef):
   if e==f:compat.add((8+H,8+G))
 assert compat=={tuple(z) for z in r['native_side_compatibility']}
 corners=[(0,8),(1,2),(3,8),(4,9),(5,6),(7,9)];stars=set()
 # Independently enumerate ORDERED triples, rather than author's unordered domain.
 for trip in product(range(6),repeat=3):
  for flip in product((0,1),repeat=3):
   rays=[corners[k][::-1] if a else corners[k] for k,a in zip(trip,flip)]
   if all((rays[i][1],rays[(i+1)%3][0]) in compat for i in range(3)):
    stars.add(tuple(sorted(trip)));break
 assert stars=={tuple(z) for z in r['allowed_120_stars']}
 absent=sorted(set(range(6))-{i for star in stars for i in star});assert absent==r['absent_native_corners']
 core=all(any(q(h-2*arms[i])) for h in (cross,*es) for i in (2,3,4,5))
 status='generic-120-corner-obstruction' if absent else 'generic-forced-core-obstruction' if core else 'generic-local-survivor'
 assert status==r['status']
 if status!='generic-local-survivor':continue
 assert len(ns)==2
 parameter=next(i for i in range(1,8) if matrix(K,[af[0],af[i]]).det()!=0)
 assert parameter==r['normalized_parameter_native_arm']
 U=PolynomialRing(K,'u');u=U.gen();coeff=matrix(K,[af[0],af[parameter]]).inverse()*vector(U,[1,u])
 normalized=[sum(a*x for a,x in zip(q(z),coeff)) for z in lengths]
 assert normalized[:8]==[U(z) for z in r['normalized_arms']]
 assert normalized[8:]==[U(z) for z in r['normalized_e']]
 lower=[];upper=[]
 for a in normalized:
  if a[1]>0:lower.append(-a[0]/a[1])
  elif a[1]<0:upper.append(-a[0]/a[1])
  else:assert a[0]>0
 lo=max(lower);hi=min(upper) if upper else None
 assert [lo,hi]==[K(r['positive_ratio_interval'][0]),None if r['positive_ratio_interval'][1] is None else K(r['positive_ratio_interval'][1])]
 inside=lambda z:lo<z and (hi is None or z<hi)
 privacy=[];extraevents=[]
 for i,j in combinations(range(8),2):
  if(i,j)==(0,7):continue
  h=normalized[i]-normalized[j];assert h
  if h[1] and inside(-h[0]/h[1]):privacy.append((i,j,-h[0]/h[1]))
 for i,h in enumerate(hyper):
  normalized_h=sum(a*x for a,x in zip(q(h),coeff))
  assert bool(normalized_h)==(i not in active)
  if normalized_h[1] and inside(-normalized_h[0]/normalized_h[1]):extraevents.append((i,-normalized_h[0]/normalized_h[1]))
 assert set(privacy)=={(i,j,K(z)) for i,j,z in r['privacy_exclusions']}
 assert set(extraevents)=={(i,K(z)) for i,z in r['event_exclusions']}
 ends=[lo]+sorted({z[-1] for z in privacy+extraevents})+[hi]
 assert len(r['generic_arm_order_chambers'])==len(ends)-1
 for (left,right),ch in zip(zip(ends,ends[1:]),r['generic_arm_order_chambers']):
  assert [left,right]==[K(ch['interval'][0]),None if ch['interval'][1] is None else K(ch['interval'][1])]
  sample=K(ch['sample_parameter']);assert left<sample and(right is None or sample<right)
  values=[a(sample) for a in normalized];assert all(a>0 for a in values)
  assert values[:8]==[K(z) for z in ch['sample_arms']] and values[8:]==[K(z) for z in ch['sample_e']]
  assert all(values[i]!=values[j] for i,j in combinations(range(8),2) if(i,j)!=(0,7))
  assert all(sum(a*x for a,x in zip(q(h),coeff))(sample)!=0 for i,h in enumerate(hyper) if i not in active)
  assert sorted(range(8),key=lambda i:(values[i],i))==ch['native_arm_order'];chambers+=1
# Verify the human-readable sixteen-family record against independently checked data.
record=(root/'searches/partial-contact-cairo-one-shared-event-flats.md').read_text()
blocks=re.split(r'### Flat (\d+)\n',record)[1:]
byid={r['flat_id']:r for r in data['records'] if r['status']=='generic-local-survivor'}
assert set(map(int,blocks[::2]))==set(byid)
U=PolynomialRing(K,'u')
for flatid,body in zip(blocks[::2],blocks[1::2]):
 r=byid[int(flatid)]
 parameter=int(re.search(r'Parameter u=arm\[(\d+)\]/Pa',body).group(1))
 assert parameter==r['normalized_parameter_native_arm']
 for name,expected in [('P',r['normalized_arms'][:4]+r['normalized_e'][:1]),('Q',r['normalized_arms'][4:]+r['normalized_e'][1:])]:
  word=re.search(r'Normalized '+name+r': \((.*)\)\.',body).group(1)
  assert [U(a) for a in word.split(', ')]==[U(a) for a in expected]
 interval=re.search(r'Positivity interval: \((.*)\)\.',body).group(1).split(', ')
 assert [None if a in ('None','infinity') else K(a) for a in interval]==[None if a is None else K(a) for a in r['positive_ratio_interval']]
 roots=re.search(r'Excluded privacy or proper-event ratio values: (.*)\.',body).group(1).split(', ')
 assert {K(a) for a in roots}=={K(a[-1]) for a in r['privacy_exclusions']+r['event_exclusions']}
 assert int(re.search(r'Exact open arm-order chambers retained: (\d+)',body).group(1))==len(r['generic_arm_order_chambers'])
# Independently enumerate the full arrangement in reduced five-dimensional coordinates.
seen={()};queue=deque([()])
while queue:
 key=queue.popleft();assert key in records
 r=records[key]
 if r['status'] in ('forced-extra-arm','empty-positive-cone') or r['dimension']<=1:continue
 for h in hyper:
  child=canon(list(key)+[h])
  if child not in seen:seen.add(child);queue.append(child)
assert seen==set(records)
assert counts==Counter(data['counts'])==Counter({'forced-extra-arm':1270,'empty-positive-cone':34,'generic-120-corner-obstruction':318,'generic-forced-core-obstruction':1,'generic-local-survivor':16})
assert positives==335 and duals==34
print('PASS all1639 reduced-coordinate canonical flats and complete22-form recursion;1270 forced extra-arm strata;34 exact Gordan duals;335 direct positive witnesses;318 ordered-native-star exclusions;1 reviewed-core stratum;16 dimension2local survivors.')
print('PASS16 exact normalized families, privacy/event roots and',chambers,'generic chambers;positivity fixtures withincidental extra-arm equalities:',fixture_extra)
