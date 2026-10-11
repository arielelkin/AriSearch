"""Independent complete mixed-star eliminations; rational rays, no author imports."""
import json
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
from pathlib import Path
C=json.loads(Path('research/certificates/branching-hexagon-two-run-mixed-cover-hyperplanes.json').read_text())
assert C['coefficient_order']==['constant','delta','alpha','beta','chi','psi']
NAMES=['alpha','beta','chi','psi']
def ray(v):
 v=tuple(map(Q,v));first=next(x for x in v if x)
 return tuple(x/first for x in v)
def equation(constant,delta,terms):
 v=[Q(constant),Q(delta),Q(1),Q(1),Q(1),Q(1)]
 for index,coef in terms:v[index+2]-=coef
 assert any(v[2:])
 return ray(v)
# An actual mixed B corner has exactly one other mixed corner.
for rays in product((0,1),repeat=3):
 transitions=[rays[j]!=rays[(j+1)%3] for j in range(3)]
 assert sum(transitions) in (0,2)
# Derive corner values from sums rather than copying coefficient canonicalization.
alts=[]
for r in range(4):
 for partner,e in [('A_high',1),('A_low',-1),('self',0)]:
  val=[Q(0)]*6
  if partner=='self':val[0]=180;val[r+2]=-Q(1,2)
  else:val[0]=240;val[1]=-e;val[r+2]=-1
  alts.append((r,partner,tuple(val)))
assert len(C['mixed_value_alternatives'])==12
for actual,(r,partner,value) in zip(C['mixed_value_alternatives'],alts):
 assert actual['homogeneous_corner']==NAMES[r]
 assert actual['other_mixed_corner']==partner
 assert tuple(map(Q,actual['value_coefficients']))==value
raw=[]
for r in range(4):raw.append(equation(-360,0,[(r,Q(1))]))
for x,y in product(range(12),repeat=2):
 vals=[a+b for a,b in zip(alts[x][2],alts[y][2])]
 vals[0]-=720
 for j in range(2,6):vals[j]+=1
 raw.append(ray(vals))
assert len(raw)==148
assert len(C['all148_cover_eliminations'])==148
for index,(actual,expected) in enumerate(zip(C['all148_cover_eliminations'],raw)):
 assert ray(actual['hyperplane_coefficients'])==expected
 if index<4:
  assert actual['kind']=='opposite_B_mixed_joint' and actual['homogeneous_corner']==NAMES[index]
 else:
  x,y=divmod(index-4,12)
  assert actual['kind']=='separate_B0_B3_cover'
  assert (actual['B0_alternative'],actual['B3_alternative'])==(x,y)
# Independently enumerate theorem's three indexed families.
AA={equation(-240,-k,[(r,Q(1)),(s,Q(1))]) for r,s in combinations_with_replacement(range(4),2) for k in (-2,0,2)}
AS={equation(-300,-e,[(r,Q(1)),(s,Q(1,2))]) for r,s in product(range(4),repeat=2) for e in (-1,1)}
SS={equation(-360,0,[(r,Q(1,2)),(s,Q(1,2))]) for r,s in combinations_with_replacement(range(4),2)}
assert (len(AA),len(AS),len(SS))==(30,32,10)
assert len(AA|AS|SS)==72 and set(raw)==AA|AS|SS
assert all(raw[r] in SS for r in range(4))
retained={}
for item in C['canonical_hyperplanes']:
 k=ray(item['coefficients']);assert k not in retained
 ids=item['raw_record_indices'];assert ids==[j for j,v in enumerate(raw) if v==k]
 retained[k]=ids
assert len(retained)==C['distinct_hyperplane_count']==72
assert set(retained)==set(raw)
assert sorted(j for ids in retained.values() for j in ids)==list(range(148))
# Only compare eight supplied resonance vectors; do not import inventory conclusions.
hom=set()
for start in (2,4):
 for m in range(4):
  v=[Q(-360),Q(0),Q(0),Q(0),Q(0),Q(0)]
  v[start]=m;v[start+1]=3-m;hom.add(ray(v))
assert len(hom)==8 and not hom & set(raw)
assert {ray(v) for v in C['homogeneous_resonance_vectors_disjoint_from72']}==hom
print('PASS complete binary trivalent parity; all12 indexed values; all148 raw equations and exact record indices; independent30+32+10=72 proper distinct hyperplanes; all4 joint covers retained; 8 resonance vectors distinct from72.')
