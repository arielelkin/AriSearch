#!/usr/bin/env python3
"""Two specified B orbits only: exact species-purity stopping gate."""
import importlib.util,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',root/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
reps=((0,0,2,1,1,3),(0,1,0,2,1,3))
def orbit(b):
 return sorted({w[k:]+w[:k] for w in (b,b[::-1]) for k in range(6)})
records=[]
for b in reps:
 r=m.build(b);stars=r['fixed_stars']
 assert len(stars)==12 and len(r['boundary_coronas'])==1
 assert r['covered_corners']==list(range(12))
 assert all(len({p[0]//6 for p in t})==1 for t in stars)
 ob=orbit(b);assert len(ob)==12
 # Independently rerun the finite native atlas for each claimed relabeling.
 for w in ob:
  q=m.build(w)
  assert len(q['fixed_stars'])==12 and len(q['boundary_coronas'])==1
  assert q['covered_corners']==list(range(12))
  assert all(len({p[0]//6 for p in t})==1 for t in q['fixed_stars'])
 records.append(dict(B=b,orbit=ob,initial_star_count=r['initial_stars'],pruning_rounds=r['pruning_rounds'],signed_stars=stars,covered_corners=r['covered_corners'],formal_coronas=r['boundary_coronas'],species_star_counts=[sum(t[0][0]//6==f for t in stars) for f in range(2)],all_stars_species_pure=True))
assert not set(orbit(reps[0]))&set(orbit(reps[1]))
out=dict(schema='TWO_TWELVE_STAR_ONE_CORONA_PURITY_SOL_V1',A=m.A,records=records,arithmetic='integer combinatorics only',domain='two specified representatives and their 24 distinct dihedral B words; 24 signed ports, cyclic ordered triples allowing repeats, exact endpoint pruning',stopping_gate='all fixed stars species-pure; no mixed ETE trivalent plane tiling',not_run='support subset enumeration, metric query, larger patches, 32-star/100-corona orbit',scope='restricted mixed ETE impossibility; unrestricted periodic escape uses separately reviewed limit and monohedral dependencies')
p=root/'research/certificates/hexagon-two-twelve-star-one-corona-pure-sol-2026-10-19.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([dict(B=r['B'],stars=len(r['signed_stars']),coronas=len(r['formal_coronas']),species_counts=r['species_star_counts'],orbit_size=len(r['orbit']),pure=True) for r in records]))
