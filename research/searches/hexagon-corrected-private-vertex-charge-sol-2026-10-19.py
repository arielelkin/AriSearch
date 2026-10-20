"""Exact corner-incidence balance, not a plane extension model."""
from itertools import combinations_with_replacement, product
from pathlib import Path
import json,z3
W=((5,3,3,4,4,2),(1,3,3,2,2,4))
C=[(t,i,tuple(sorted((w[i-1],w[i])))) for t,w in enumerate(W) for i in range(6)]
# Star ray lengths x,y,z; corner pairs (x,y),(y,z),(z,x).
stars=set()
for x,y,z in combinations_with_replacement(range(1,6),3):
 pairs=[tuple(sorted(p)) for p in ((x,y),(y,z),(z,x))]
 domains=[[j for j,(_,_,p) in enumerate(C) if p==pair] for pair in pairs]
 for corners in product(*domains): stars.add(tuple(sorted(corners)))
stars=sorted(stars)
v=[z3.Real('v%d'%i) for i in range(len(stars))]; counts=[z3.Real('A'),z3.Real('B')]
s=z3.Solver(); s.add(counts[0]>0,counts[1]>0,counts[0]+counts[1]==1)
s.add(*[a>=0 for a in v])
for j,(t,i,pair) in enumerate(C): s.add(z3.Sum([star.count(j)*a for star,a in zip(stars,v)])==counts[t])
# A private-edge dimer has either two mixed endpoint stars, or one
# doubled-corner-0 and one doubled-corner-1 endpoint star.
for j in (0,6):
 s.add(z3.Sum([a for star,a in zip(stars,v) if star.count(j)==2])==z3.Sum([a for star,a in zip(stars,v) if star.count(j+1)==2]))
answer=s.check(); out=dict(words=W,corners=C,star_count=len(stars),answer=str(answer),z3_version=z3.get_version_string())
if answer==z3.sat:
 m=s.model(); out['tile_counts']=[str(m.eval(x)) for x in counts]
 out['nonzero_stars']=[dict(corners=[C[j][:2] for j in star],weight=str(m.eval(a))) for star,a in zip(stars,v) if m.eval(a).numerator_as_long()!=0]
 from fractions import Fraction
 tally={(t,i):Fraction(0) for t in range(2) for i in range(6)}
 for entry in out['nonzero_stars']:
  weight=Fraction(entry['weight']); assert weight>0
  for corner in entry['corners']: tally[tuple(corner)]+=weight
 assert all(tally[t,i]==Fraction(out['tile_counts'][t]) for t in range(2) for i in range(6))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
