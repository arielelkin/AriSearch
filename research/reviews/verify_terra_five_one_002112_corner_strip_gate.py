#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json
J=json.loads(Path('research/certificates/terra-five-one-002112-chebyshev-gate.json').read_text())
S=json.loads(Path('research/certificates/terra-five-one-002112-aaa-corner-strip-gate.json').read_text())
assert len(S['rows'])==42 and {tuple(r['partition'])for r in S['rows']}=={tuple(r['partition'])for r in J['rows']}
for row in S['rows']:
 p=row['partition'];stars=[];vertices=set()
 for cc in product((0,1),(3,4),(2,5)):
  for signs in product((1,-1),repeat=3):
   arms=[((c-1)%6,c)[::s]for c,s in zip(cc,signs)]
   if all(p[arms[j][1]]==p[arms[(j+1)%3][0]]for j in range(3)):
    stars.append((cc,signs));vertices.update(cc)
 assert vertices==set(row['AAA_allowed_native_corners'])
 assert {(tuple(s['corners']),tuple(s['arm_signs']))for s in row['legal_native_stars']}==set(stars)
 assert row['consecutive3_starts']==[i for i in range(6)if all((i+j)%6 in vertices for j in range(3))]
print('PASS42 partitions*64 stars; no3runs',sum(not r['consecutive3_starts']for r in S['rows']),'all6corners',sum(len(r['AAA_allowed_native_corners'])==6 for r in S['rows']))
