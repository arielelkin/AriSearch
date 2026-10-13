#!/usr/bin/env python3
"""Independent no-producer-import checker for the exact boundary certificate."""
import json
from pathlib import Path
from itertools import product
J=json.loads(Path('research/certificates/terra-five-one-001212-boundary-transfer.json').read_text())
C=(0,0,1,2,1,2)
assert tuple(J['native_A_word'])==C and len(J['native_poses'])==12
poses=[]
for r,s in product(range(6),(1,-1)):
 native_vertices=[(r+s*k)%6 for k in range(6)]
 native_edges=[]
 for i in range(6):
  a,b=native_vertices[i],native_vertices[(i+1)%6]
  assert (b-a)%6 in(1,5)
  native_edges.append(a if (b-a)%6==1 else b)
 poses.append(dict(rotation=r,sign=s,corners=[C[v]for v in native_vertices],sides=native_edges))
assert poses==J['native_poses']
for record in J['boundary_faces']:
 upper=record['face']=='top';z=1 if upper else 4
 outward=(2,0)if upper else(3,5);inward=(3,5)if upper else(2,0)
 indices=[i for i,p in enumerate(poses)if p['corners'][z]==2]
 assert indices==record['eligible_native_pose_ids']
 edges=[]
 # Directly inspect all144 pairs, not only the producer's reduced4*4 list.
 for ia,a in enumerate(poses):
  for ib,b in enumerate(poses):
   if ia not in indices or ib not in indices:continue
   outward_pair=[a['corners'][outward[0]],b['corners'][outward[1]]]
   inward_pair=[a['corners'][inward[0]],b['corners'][inward[1]]]
   if outward_pair not in([0,0],[1,1]) or len(set(inward_pair))!=2:continue
   assert outward_pair==[1,1]
   edges.append(dict(source=indices.index(ia),target=indices.index(ib),outer_AAB_colours=outward_pair,inner_AAA_colours=inward_pair,AA_metric_native_indices=[a['sides'][2],b['sides'][5]]))
 assert edges==record['edges']
 # Graph reachability: no nonloop cycle and the only cyclic states are1,3.
 adjacency={i:{e['target']for e in edges if e['source']==i}for i in range(4)}
 cyclic=[]
 for root in range(4):
  seen=set();pending=list(adjacency[root])
  while pending:
   x=pending.pop()
   if x in seen:continue
   seen.add(x);pending.extend(adjacency[x])
  if root in seen:cyclic.append(root)
 assert cyclic==record['biinfinite_row_states']==[1,3]
 assert adjacency[1]=={1} and adjacency[3]=={2,3} and not adjacency[2]
 for e in edges:
  if e['source']==e['target']:assert set(e['AA_metric_native_indices'])=={1,4}
 assert record['necessary_biinfinite_metric_equality']==[1,4]
for i,p in enumerate(poses):
 aa=sorted(p['sides'][k]for k in(2,5))
 assert (aa[1]-aa[0])%6==3 and not {0,1}<=set(aa)
 assert J['width1_rows'][i]==dict(pose=i,row_AA_native_sides=aa,both_private_AA_present=False)
assert J['mixed_B_row_possible']is False
print('PASS288 direct pair tests;both faces requirey/y;12 width1 poses impossible;full native cycles only1 or3 witha1=a4')
