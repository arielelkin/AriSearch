#!/usr/bin/env python3
"""Finite12*12 native poses; lengths and partitions never assumed.
Both A copies have top ABedges1,2 meeting a z corner. SharedAA edges0/3;
outer endpointAAB requires equal A colours, innerAAA requires distinct.
"""
from itertools import product
from pathlib import Path
import json
C=(0,0,2,1,1,2)
poses=[dict(rotation=r,sign=s,corners=[C[(r+s*k)%6]for k in range(6)])for r,s in product(range(6),(1,-1))]
rows=[]
for ia,a in enumerate(poses):
 for ib,b in enumerate(poses):
  x,y=a['corners'],b['corners']
  if x[2]!=2 or y[2]!=2:continue
  # Two adjacent AB sides must be incident to native A z corner2 or5.
  assert x[0]==x[1] and x[3]==x[4]
  assert y[0]==y[1] and y[3]==y[4]
  outer=(x[1],y[3]);inner=(x[0],y[4])
  assert outer==inner
  row=dict(A_left_pose=ia,A_right_pose=ib,outer_AAB_A_colours=outer,inner_AAA_A_colours=inner,outer_AAB_legal=outer[0]==outer[1],inner_AAA_possible=inner[0]!=inner[1])
  rows.append(row)
assert len(rows)==16
assert sum(r['outer_AAB_legal']for r in rows)==8
assert not any(r['outer_AAB_legal']and r['inner_AAA_possible']for r in rows)
J=dict(scope=__doc__,native_poses=poses,eligible_boundary_pair_count=16,outer_AAB_pair_count=8,compatible_interface_pair_count=0,rows=rows)
p=Path('research/certificates/terra-five-one-002112-boundary-interface.json')
if '--write' in __import__('sys').argv:p.write_text(json.dumps(J,indent=2)+'\n')
else:assert json.loads(p.read_text())==json.loads(json.dumps(J))
print('PASS12*12 poses;16 eligible pairs;8 outerAAB pairs;0 innerAAA-compatible pairs, independent of ALL side lengths')
