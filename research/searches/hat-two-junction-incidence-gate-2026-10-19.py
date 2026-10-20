"""Complete side-incidence gate, not a geometric dissection search."""
import itertools,json
from pathlib import Path
b=[4,4,3,2];out=[]
for groups in [((0,1),(2,3)),((3,0),(1,2))]:
 incident=[];counts=[0]*4
 for u,v in groups:
  fs=sorted({u,(u-1)%4,v});incident.append(fs)
  for f in fs:counts[f]+=1
 nominal=[b[i]+1+counts[i] for i in range(4)]
 rows=[]
 for flats in itertools.product(*[[None]+fs for fs in incident]):
  for boundary_flats in itertools.product(*[[None,(i-1)%4,i] for i in range(4)]):
   sides=[nominal[i]-sum(f==i for f in flats+boundary_flats) for i in range(4)]
   if all(s in (5,6) for s in sides):rows.append(dict(flats=flats,boundary_flats=boundary_flats,sides=sides))
 out.append(dict(groups=groups,incident=incident,nominal=nominal,survivors=rows))
assert [len(x['survivors']) for x in out]==[32,0]
assert all(1 in r['flats']+r['boundary_flats'] for r in out[0]['survivors'])
payload=dict(status='COMPLETE',cases=2592,records=out)
Path('research/certificates/hat-two-junction-incidence-gate-2026-10-19.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload))
