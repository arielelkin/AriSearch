#!/usr/bin/env python3
"""Independent all288 native-pair checks for each of two angle-only obstructions.
No producer imports; exact certificate comparison plus privateAA width1gate.
"""
from pathlib import Path
from itertools import product
import json
for word,private in [('010212',(0,1)),('012021',(5,0))]:
 C=tuple(map(int,word));poses=list(product(range(6),(1,-1)))
 J=json.loads(Path('research/certificates/five-one-'+word+'-boundary-interface.json').read_text())
 profiles=[];indices=[]
 for r,s in poses:
  v=[(r+s*k)%6 for k in range(6)]
  e=[v[k]if(v[(k+1)%6]-v[k])%6==1 else v[(k+1)%6]for k in range(6)]
  assert all((e[k]+1)%6 in(v[k],v[(k+1)%6])and e[k]in(v[k],v[(k+1)%6])for k in range(6))
  profiles.append([C[a]for a in v]);indices.append(e)
 assert profiles==[p['corners']for p in J['native_poses']]
 assert all(set((C[j],C[(j+1)%6]))<={0,1} for j in private)
 assert (private[0]-private[1])%6 in(1,5)
 assert not any(set(private)<={e[2],e[5]}for e in indices)
 for record,z,outer,inner in zip(J['orientations'],(1,4),((0,2),(5,3)),((5,3),(0,2))):
  eligible=[i for i,c in enumerate(profiles)if c[z]==2]
  assert eligible==record['eligible_pose_indices']
  matrix={}
  for ia,a in enumerate(profiles):
   for ib,b in enumerate(profiles):
    if ia not in eligible or ib not in eligible:continue
    o=[a[outer[0]],b[outer[1]]];q=[a[inner[0]],b[inner[1]]]
    outerok=o in([0,0],[1,1]);innerok=len(set(q))==2
    assert not(outerok and innerok)
    matrix[ia,ib]=dict(left_pose=ia,right_pose=ib,shared_native_sides=[indices[ia][5],indices[ib][2]],outer_A_colours=o,inner_A_colours=q,outer_AAB_legal=outerok,inner_AAA_possible=innerok)
  assert list(matrix.values())==record['rows']
  assert len(matrix)==16 and sum(x['outer_AAB_legal']for x in matrix.values())==8
 assert J['compatible_interface_pair_count']==0
 print('PASS',word,'288 direct pair checks;32 eligiblepairs;0 angle-compatible;12 width1poses excluded')
