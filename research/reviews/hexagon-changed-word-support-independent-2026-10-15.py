"""Independent exhaustive source-support audit. Stdlib/Fraction; no producer imports."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORDS=((0,1,0,2,3,4),(0,3,0,2,1,4))
# Maps ACTUAL side indices to its endpoint corner indices.
ends={6*f+i: frozenset((6*f+(i-1)%6,6*f+i)) for f in range(2) for i in range(6)}
labels={6*f+i:WORDS[f][i] for f in range(2) for i in range(6)}
ports={c:tuple(side for side in ends if c in ends[side]) for c in range(12)}
arms={c:frozenset(labels[e] for e in ports[c]) for c in ports}
assert all(len(a)==2 for a in arms.values())
# Build stars by choosing three distinct ray labels and actual corners
# on their three label pairs, rather than filtering native-corner triples.
stars=set()
for rays in combinations(range(5),3):
 pairs=tuple(map(frozenset,combinations(rays,2)))
 for corners in product(*(tuple(c for c in range(12) if arms[c]==pair) for pair in pairs)):
  assert len(set(corners))==3
  stars.add(tuple(sorted(corners)))
stars=sorted(stars)
assert len(stars)==16
index={s:i for i,s in enumerate(stars)}
def mask(ss):return sum(1<<index[tuple(sorted(s))] for s in set(tuple(sorted(s)) for s in ss))
def selected(m):return [s for i,s in enumerate(stars) if m&(1<<i)]
def completions(a,b):return [s for s in stars if a!=b and a in s and b in s]

rslots=tuple(side for side in labels if labels[side]==0)
assert rslots==(0,2,6,8)
seams={}
for a,b in combinations(rslots,2):
 modes=[]
 for mapping in permutations(sorted(ends[b])):
  options=[completions(x,y) for x,y in zip(sorted(ends[a]),mapping)]
  if all(options):
   assert all(len(o)==1 for o in options)
   modes.append(tuple(o[0] for o in options))
 assert len(modes)==1
 seams[a,b]=mask(modes[0])

def connected(edges,vertices):
 reached={min(vertices)}
 while True:
  more=reached|{x for edge in edges if set(edge)&reached for x in edge}
  if more==reached:return reached==set(vertices)
  reached=more

trees=[]
for es in combinations(seams,3):
 if connected(es,rslots):
  m=0
  for e in es:m|=seams[e]
  trees.append((es,m))
assert len(trees)==16
required=[]
for star in stars:
 targets=[]
 for c,d in combinations(star,2):
  common=arms[c]&arms[d]
  assert len(common)==1
  ray=next(iter(common))
  ce=next(e for e in ports[c] if labels[e]==ray)
  de=next(e for e in ports[d] if labels[e]==ray)
  farc=next(iter(ends[ce]-{c}));fard=next(iter(ends[de]-{d}))
  targets.append(mask(completions(farc,fard)))
 required.append(targets)
valid=[]
all_valid=[]
for m in range(1<<len(stars)):
 chosen=selected(m)
 if set(c for s in chosen for c in s)!=set(range(12)):continue
 if not all(m&target for i in range(16) if m&(1<<i) for target in required[i]):continue
 all_valid.append(m)
 if any(m&forced==forced for _,forced in trees):valid.append(m)
validset=set(valid)
minimal=[]
for m in valid:
 # Any smaller accepted subset is sufficient to reject minimality.
 if not any(v!=m and v&m==v for v in valid):minimal.append(m)
assert len(valid)==144 and len(minimal)==12

def rref(rows):
 rows=[list(map(F,row)) for row in rows]
 pivot=0
 for col in range(13):
  candidates=[i for i in range(pivot,len(rows)) if rows[i][col]]
  if not candidates:continue
  i=candidates[0];rows[pivot],rows[i]=rows[i],rows[pivot]
  divisor=rows[pivot][col]
  rows[pivot]=[x/divisor for x in rows[pivot]]
  for j in range(len(rows)):
   if j==pivot:continue
   factor=rows[j][col]
   rows[j]=[a-factor*b for a,b in zip(rows[j],rows[pivot])]
  pivot+=1
 return tuple(tuple(row) for row in rows if any(row))
polygon_rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
flats={}
for m in minimal:
 rr=rref(polygon_rows+[[int(i in star) for i in range(12)]+[2] for star in selected(m)])
 assert not any(not any(row[:12]) and row[12] for row in rr)
 flats.setdefault(rr,[]).append(m)
keys=list(flats)
assert len(keys)==11
parents=[[j for j,l in enumerate(keys) if j!=i and len(rref(k+l))==len(k)] for i,k in enumerate(keys)]
maximal=[i for i,p in enumerate(parents) if not p]
assert maximal==[0,2,5,6,7,8,10]

cert=json.loads((ROOT/'certificates/hexagon-changed-word-connected-support-gate-2026-10-15.json').read_text())
assert cert['words']==[list(w) for w in WORDS]
assert cert['full_star_atlas']==[list(s) for s in stars]
assert cert['r_slots']==list(rslots)
assert cert['r_seams']==[dict(slots=list(e),endpoint_stars=[list(s) for s in selected(m)]) for e,m in seams.items()]
assert cert['trees']==[dict(edges=[list(e) for e in es],forced_stars=[list(s) for s in selected(m)]) for es,m in trees]
assert cert['far_end_requirements']==[[[list(s) for s in selected(m)] for m in targets] for targets in required]
assert cert['connected_corner_covering_endpoint_closed_masks']==valid
assert cert['minimal_supports']==[dict(mask=m,stars=[list(s) for s in selected(m)]) for m in minimal]
for i,(record,rr) in enumerate(zip(cert['angle_flats'],keys)):
 assert record['id']==i and record['minimal_support_masks']==flats[rr]
 assert tuple(tuple(F(v) for v in row) for row in record['rref_augmented_rows'])==rr
 assert record['containing_flat_ids']==parents[i]
assert len(cert['angle_flats'])==11 and cert['maximal_flat_ids']==maximal
print('PASS source:16 actual stars,6 unique r-seam modes,16 trees,144 closed corner covers,12 minimal supports,11 consistent Fraction RREFs,7 maximal affine flats.')

def form(terms):
 out=[F(0)]*13
 for i,c in terms:out[i]+=c
 return tuple(out)
D=form(((0,1),(1,-1)));E=form(((6,1),(7,-1)))
Fdiff=form(((2,1),(8,-1)));G=form(((5,1),(11,-1)))
def difference(a,b):return tuple(x-y for x,y in zip(a,b))
def consequence(i,row):assert len(rref(keys[i]+(row,)))==len(keys[i])
for i in (2,5,6):consequence(i,Fdiff);consequence(i,G)
for i in (0,8,10):consequence(i,D);consequence(i,E)
consequence(7,difference(D,G))
consequence(7,tuple(x+y for x,y in zip(D,E)))
consequence(7,tuple(x+y for x,y in zip(D,Fdiff)))
for triple in ((0,2,9),(1,5,10),(3,6,8),(4,7,11)):
 consequence(5,tuple(F(int(i in triple)) for i in range(12))+(F(2),))
print('PASS ancillary source prose: seven-flat D/E/F/G trichotomy and flat5 four-star consequence.')

all_minimal=[m for m in all_valid if not any(v!=m and v&m==v for v in all_valid)]
assert len(all_valid)==171 and len(all_minimal)==8
assert cert['all_endpoint_closed_cornercover_masks']==all_valid
assert cert['all_minimal_supports']==[dict(mask=m,stars=[list(s) for s in selected(m)]) for m in all_minimal]
print('PASS expanded source scope:171 closed corner covers,8 inclusion-minimal, NO connected-r hypothesis.')

coverage=json.loads((ROOT/'certificates/hexagon-changed-word-torus-coverage-2026-10-15.json').read_text())
atlas=json.loads((ROOT/'certificates/hexagon-shared-repeat-four-face-atlas-2026-10-15.json').read_text())
assert coverage['source_domain_key']=='all_endpoint_closed_cornercover_masks'
assert coverage['source_support_count']==171
lookup={m:selected(m) for m in all_valid}
covered_masks=set();uncovered_masks=set()
def star_row(st):return tuple(F(st.count(i)) for i in range(12))+(F(2),)
for record in coverage['covered']:
 m=record['source_mask']
 assert m in lookup and m not in covered_masks
 covered_masks.add(m)
 assert record['source_stars']==[list(t) for t in lookup[m]]
 witness=atlas['witnesses'][record['torus_index']]
 assert record['target_stars']==witness['angle_support']
 source=polygon_rows+[star_row(t) for t in lookup[m]]
 assert len(record['row_combinations'])==len(record['target_stars'])
 for target,coefficients in zip(record['target_stars'],record['row_combinations']):
  weights=list(map(F,coefficients))
  assert len(weights)==len(source)
  result=tuple(sum(weight*row[j] for weight,row in zip(weights,source)) for j in range(13))
  assert result==star_row(target)
for record in coverage['uncovered']:
 m=record['mask']
 assert m in lookup and m not in uncovered_masks
 uncovered_masks.add(m)
 assert record['stars']==[list(t) for t in lookup[m]]
 source=polygon_rows+[star_row(t) for t in lookup[m]]
 rank=len(rref(source))
 assert not any(len(rref(source+[star_row(t) for t in witness['angle_support']]))==rank for witness in atlas['witnesses'])
assert not covered_masks&uncovered_masks and covered_masks|uncovered_masks==set(all_valid)
assert len(covered_masks)==169 and uncovered_masks=={18465,33810}
for m in uncovered_masks:
 assert sorted(c for t in selected(m) for c in t)==list(range(12))
print('PASS all-source row coverage:169 positive torus witnesses with exact raw-star weighted identities;2 four-star partitions for intrinsic-determinism escape.')

assert sum(len(r['target_stars']) for r in coverage['covered'])==676
for m in uncovered_masks:
 support=selected(m)
 for hostside in range(12):
  hostcorner=hostside
  star=next(st for st in support if hostcorner in st)
  guests=[c for c in star if c!=hostcorner and labels[hostside] in arms[c]]
  assert len(guests)==1
  guestcorner=guests[0]
  guestsides=[e for e in ports[guestcorner] if labels[e]==labels[hostside]]
  assert len(guestsides)==1
  guestside=guestsides[0]
  farhost=next(iter(ends[hostside]-{hostcorner}))
  farguest=next(iter(ends[guestside]-{guestcorner}))
  assert len([st for st in support if farhost!=farguest and farhost in st and farguest in st])==1
print('PASS676 weighted identities and24 formal-color native neighbor maps, including both endpoints; no physical length injectivity used.')
