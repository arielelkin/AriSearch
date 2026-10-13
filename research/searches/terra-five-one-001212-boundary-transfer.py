#!/usr/bin/env python3
"""Finite2faces*12*12 native A pairs, length-free colour gate;12 one-row poses.
Question: can a saturated parallel B row have its required x-facing AAB
endpoint? Outcomes: no x-face plus no width1 strip excludes mixed field;
a surviving x-face would require metric graph and positive closure next.
"""
from itertools import product
from pathlib import Path
import json
C=(0,0,1,2,1,2)
P=[dict(rotation=r,sign=s,corners=[C[(r+s*k)%6]for k in range(6)],sides=[(r+k)%6 if s==1 else(r-k-1)%6 for k in range(6)])for r,s in product(range(6),(1,-1))]
rows=[]
for face,z,outer,inner in [('top',1,(2,0),(3,5)),('bottom',4,(3,5),(2,0))]:
 states=[i for i,p in enumerate(P)if p['corners'][z]==2];edges=[]
 for a,i in enumerate(states):
  for b,j in enumerate(states):
   x,y=P[i]['corners'],P[j]['corners'];o=(x[outer[0]],y[outer[1]]);q=(x[inner[0]],y[inner[1]])
   if o[0]==o[1]!=2 and q[0]!=q[1]:
    edges.append(dict(source=a,target=b,outer_AAB_colours=o,inner_AAA_colours=q,AA_metric_native_indices=(P[i]['sides'][2],P[j]['sides'][5])))
 assert len(states)==4 and len(edges)==4
 assert all(e['outer_AAB_colours']==(1,1)for e in edges)
 # Every bi-infinite path lies in cyclic SCCs, here only loops1,3.
 assert {(e['source'],e['target'])for e in edges}=={(0,1),(1,1),(3,2),(3,3)}
 assert all(e['AA_metric_native_indices'] in ((4,1),(1,4)) for e in edges if e['source']==e['target'])
 rows.append(dict(face=face,eligible_native_pose_ids=states,edges=edges,biinfinite_row_states=[1,3],necessary_biinfinite_metric_equality=[1,4]))
# Width1 A row only has AA in oppositeglobal slots2,5. Native private00,01
# sides0,1 bothmustAA since no B AB endpoint palette00/01 exists.
width1=[]
for i,p in enumerate(P):
 eligible=set(p['sides'][j]for j in (2,5))
 ok={0,1}<=eligible
 width1.append(dict(pose=i,row_AA_native_sides=sorted(eligible),both_private_AA_present=ok))
assert not any(r['both_private_AA_present']for r in width1)
J=dict(scope=__doc__,native_A_word=C,native_poses=P,boundary_faces=rows,width1_rows=width1,mixed_B_row_possible=False)
Path('research/certificates/terra-five-one-001212-boundary-transfer.json').write_text(json.dumps(J,indent=2)+'\n')
print('PASS2*144 poses:top/bottom graph4edges each;all outerAAB are y/y;0width1 poses;no mixed saturated B row')
