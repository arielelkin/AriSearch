"""Independent 24/12/7 word action and complete native pruning verifier.
No producer imports, metrics, solvers or quotient search; exact integer sets.
"""
from itertools import combinations,permutations,product
from pathlib import Path
import json
A=(0,1,0,2,3,4)
NEW=((0,2,0,1,3,4),(0,2,0,1,4,3),(0,3,0,1,2,4))
OLD=(0,2,0,3,1,4)
SURVIVOR=(0,3,0,2,1,4)

def dihedral(w):
 return {tuple(w[(start+sign*j)%6] for j in range(6)) for start,sign in product(range(6),(-1,1))}
def normalize(w):
 candidates=[image for image in dihedral(w) if image[0]==image[2]==0]
 assert len(candidates)==2
 return min(candidates)
def parameters(w):return (w[1],w[3],w[4],w[5])

# Independently derive allowed color renamings from the 12 native A views,
# rather than assuming the sigma action or testing S4 permutations.
renamings=set()
for image in dihedral(A):
 mapping={};valid=True
 for old,new in zip(image,A):
  if old in mapping and mapping[old]!=new:valid=False;break
  mapping[old]=new
 if valid and len(set(mapping.values()))==5 and mapping[0]==0:
  renamings.add(tuple(mapping[c] for c in range(5)))
assert renamings=={(0,1,2,3,4),(0,1,4,3,2)}
full=tuple(permutations((1,2,3,4)))
canonical=sorted({normalize((0,p[0],0,*p[1:])) for p in full})
assert len(full)==24 and len(canonical)==12
orbits=[];unseen=set(canonical)
while unseen:
 representative=min(unseen)
 orbit=sorted({normalize(tuple(rename[c] for c in representative)) for rename in renamings})
 assert set(orbit)<=unseen
 unseen-=set(orbit)
 orbits.append(orbit)
assert len(orbits)==7 and sum(map(len,orbits))==12

ROOT=Path(__file__).resolve().parents[1]
cert=json.loads((ROOT/'certificates/hexagon-shared-repeat-separation-two-remaining-2026-10-15.json').read_text())
assert cert['A']==list(A)
assert set(tuple(p) for p in cert['full_B_permutation_domain'])==set(full)
assert len(cert['full_B_permutation_domain'])==24
assert cert['B_reflection_canonical_domain']==[list(parameters(w)) for w in canonical]
assert cert['A_label_stabilizers']==[list(p[1:]) for p in sorted(renamings)]
assert len(cert['canonical_orbits'])==7
for record,orbit in zip(cert['canonical_orbits'],orbits):
 assert record['representative_B']==list(orbit[0])
 assert record['normalized_permutations']==[list(parameters(w)) for w in orbit]

def prepare(B):
 words=(A,B)
 label={6*f+i:words[f][i] for f in range(2) for i in range(6)}
 ends={6*f+i:frozenset((6*f+(i-1)%6,6*f+i)) for f in range(2) for i in range(6)}
 ports={c:tuple(e for e in ends if c in ends[e]) for c in range(12)}
 arms={c:frozenset(label[e] for e in ports[c]) for c in range(12)}
 assert all(len(a)==2 for a in arms.values())
 stars=set()
 for rays in combinations(range(5),3):
  pairs=tuple(map(frozenset,combinations(rays,2)))
  for corners in product(*(tuple(c for c in range(12) if arms[c]==pair) for pair in pairs)):
   assert len(set(corners))==3
   stars.add(tuple(sorted(corners)))
 stars=sorted(stars)
 # Neither single color graph admits a triangle.
 assert all(any(c<6 for c in s) and any(c>=6 for c in s) for s in stars)
 def far_pair(c,d):
  common=arms[c]&arms[d]
  assert len(common)==1
  color=next(iter(common))
  ec=next(e for e in ports[c] if label[e]==color)
  ed=next(e for e in ports[d] if label[e]==color)
  return color,next(iter(ends[ec]-{c})),next(iter(ends[ed]-{d}))
 return stars,far_pair

def admissible(star,current,far_pair):
 for c,d in combinations(star,2):
  _,cc,dd=far_pair(c,d)
  if cc==dd or not any(cc in t and dd in t for t in current):return False
 return True

def prune(B):
 stars,far_pair=prepare(B)
 current=stars;sizes=[len(stars)]
 while True:
  after=[s for s in current if admissible(s,current,far_pair)]
  if after==current:return stars,current,sizes
  sizes.append(len(after));current=after

# Check all seven representatives independently, including the older killed
# word rather than trusting its prior certificate for this review.
for orbit in orbits:
 B=orbit[0]
 stars,current,sizes=prune(B)
 if B[1]==1:
  assert all(0 not in s and 1 not in s for s in stars)
 elif B==SURVIVOR:
  assert len(stars)==16 and current==stars and sizes==[16]
 elif B==OLD:assert sizes==[12,1,0] and not current
 else:
  assert B in NEW and not current

records=cert['new_word_obstructions']
assert len(records)==3
for B,record,expected_sizes in zip(NEW,records,([0],[8,0],[12,1,0])):
 assert record['B']==list(B)
 stars,far_pair=prepare(B)
 assert record['complete_star_atlas']==[list(s) for s in stars]
 current=stars;sizes=[len(stars)]
 for step in record['pruning_rounds']:
  assert step['input_stars']==[list(s) for s in current]
  after=[s for s in current if admissible(s,current,far_pair)]
  assert step['survivors']==[list(s) for s in after]
  failures=step['removed']
  assert len(failures)==len(current)-len(after)
  assert {tuple(r['star']) for r in failures}==set(current)-set(after)
  for failure in failures:
   s=tuple(failure['star']);c,d=failure['seam_corners']
   assert c!=d and c in s and d in s
   color,cc,dd=far_pair(c,d)
   assert failure['ray']==color and failure['far_corners']==[cc,dd]
   assert cc==dd or not any(cc in t and dd in t for t in current)
  current=after;sizes.append(len(current))
 assert not current and sizes==expected_sizes==record['pruning_sizes']
 accepted=[]
 for mask in range(1<<len(stars)):
  chosen=[s for j,s in enumerate(stars) if mask&(1<<j)]
  if set(c for s in chosen for c in s)!=set(range(12)):continue
  if all(admissible(s,chosen,far_pair) for s in chosen):accepted.append(mask)
 assert accepted==record['endpoint_closed_cornercover_masks']==[]
 assert record['enumerated_support_masks']==1<<len(stars)
print('PASS:24 B permutations,12 independent-reflection forms,2 A color stabilizers,7 complete orbits;2 pendant exclusions;new pruning0/8-0/12-1-0;older pruning12-1-0;all4353 new support masks exhausted. Source colors need not have distinct physical lengths.')
