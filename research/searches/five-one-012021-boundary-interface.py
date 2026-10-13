#!/usr/bin/env python3
"""Exact native-colour obstruction: A012021 B5+1 boundary rows.
Finite domain: all12 indexed A placements, two boundary orientations,16pairs
perorientation. No metric, geometry sample, solver or search bound.
"""
import argparse,json
from itertools import product
from pathlib import Path
W=(0,1,2,0,2,1)
poses=list(product(range(6),(1,-1)))
def colour(p,k):return W[(p[0]+p[1]*k)%6]
def native_side(p,k):
 ends={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 return next(j for j in range(6) if {j,(j+1)%6}==ends)
orientations=[]
for name,zslot,outer,inner in [('B_above',1,(0,2),(5,3)),('B_below',4,(5,3),(0,2))]:
 eligible=[i for i,p in enumerate(poses) if colour(p,zslot)==2]
 assert len(eligible)==4
 rows=[]
 for l,r in product(eligible,repeat=2):
  p,q=poses[l],poses[r]
  oc=[colour(p,outer[0]),colour(q,outer[1])]
  ic=[colour(p,inner[0]),colour(q,inner[1])]
  assert all(v in (0,1) for v in oc)
  assert ic==[{0:2,1:0}[v] for v in oc]
  outer_ok=oc[0]==oc[1]
  inner_ok=ic[0]!=ic[1]
  assert not(outer_ok and inner_ok)
  rows.append(dict(left_pose=l,right_pose=r,shared_native_sides=[native_side(p,5),native_side(q,2)],outer_A_colours=oc,inner_A_colours=ic,outer_AAB_legal=outer_ok,inner_AAA_possible=inner_ok))
 assert sum(row['outer_AAB_legal'] for row in rows)==8
 orientations.append(dict(name=name,z_slot=zslot,eligible_pose_indices=eligible,rows=rows,compatible_pair_count=0))
out=dict(native_A_word='012021',native_poses=[dict(rotation=r,sign=s,corners=[colour((r,s),k) for k in range(6)]) for r,s in poses],orientations=orientations,total_boundary_pairs=32,outer_AAB_legal_count=16,compatible_interface_pair_count=0,scope='necessaryangleconditions for ArownextBrowwithAonotherside;allactualmetrics/reflections;notinfiniteexistence')
a=argparse.ArgumentParser();a.add_argument('--check',type=Path);a.add_argument('--output',type=Path);args=a.parse_args()
if args.check:
 assert json.loads(args.check.read_text())==out
 print('PASS A012021 all12poses;2orientations;32boundarypairs;16outerAABlegal;zero compatibleinnerAAA')
elif args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
else:print(json.dumps(out,indent=2))
