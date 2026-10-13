#!/usr/bin/env python3
"""Finite42 actual AAA partitions times64 native stars; exact equality gate.
Question: can every native A corner be AAA, or can any consecutive three be?
No3-run would rule out two adjacentA rows in parallelB-row geometry;
otherwise retain bounded-strip obligation, without spatial/SFT inference.
"""
import json
from pathlib import Path
J=json.loads(Path('research/certificates/terra-five-one-002112-chebyshev-gate.json').read_text())
S=json.loads(Path('research/certificates/terra-five-one-002112-rational-geometry.json').read_text())['AAA_native_cases']
rows=[]
for r in J['rows']:
 p=r['partition']
 live=[s for s in S if all(s['required_side_partition'][a]!=s['required_side_partition'][b] or p[a]==p[b] for a in range(6)for b in range(a))]
 corners=sorted(set(i for s in live for i in s['corners']))
 runs=[i for i in range(6)if all((i+j)%6 in corners for j in range(3))]
 rows.append(dict(partition=p,k=r['k'],AAA_allowed_native_corners=corners,consecutive3_starts=runs,legal_native_stars=live))
 print(''.join(map(str,p)),corners,'3runs',runs)
Path('research/certificates/terra-five-one-002112-aaa-corner-strip-gate.json').write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n')
print('no3runs',sum(not r['consecutive3_starts']for r in rows),'all6corners',sum(len(r['AAA_allowed_native_corners'])==6 for r in rows))
