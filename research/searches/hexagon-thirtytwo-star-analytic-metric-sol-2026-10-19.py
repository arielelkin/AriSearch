#!/usr/bin/env python3
"""Exact IFT certificate for metric feasibility; no corona or plane assertion."""
import json
from pathlib import Path
import sympy as s
C=s.zeros(6,12)
for f in range(2):
 for j in range(6): C[f,6*f+j]=1
for row,inds in enumerate(((0,1,8),(2,7,11),(3,6,10),(4,5,9)),2):
 for j in inds:C[row,j]=1
N=s.Matrix.hstack(*C.nullspace());J=s.zeros(4,12);L=s.zeros(4,5)
for f,w in enumerate(((0,1,2,0,3,4),(0,1,2,0,3,1))):
 for j,c in enumerate(w):
  L[2*f,c]+=s.cos(j*s.pi/3);L[2*f+1,c]+=s.sin(j*s.pi/3)
  for k in range(1,j+1):
   J[2*f,6*f+k]+=s.sin(j*s.pi/3)*(2 if c==0 else 1)
   J[2*f+1,6*f+k]-=s.cos(j*s.pi/3)*(2 if c==0 else 1)
T=J*N;D=T[:,:4]
# Lengths (2,1+t,1+2t,1+3t,1+4t), free angle coordinate x4=t,x5=x6=0.
d=-D.inv()*(L*s.Matrix([0,1,2,3,4])+T[:,4]);ad=(N*s.Matrix(list(d)+[1,0,0])).applyfunc(s.simplify)
h=[s.simplify(sum(ad[6*f:6*f+3])) for f in range(2)]
assert C.rank()==5 and D.det()==-3 and all(v!=0 for v in h)
out={'schema':'THIRTYTWO_STAR_ANALYTIC_METRIC_IFT_SOL_V1','support_rank':C.rank(),'nullspace':N.tolist(),'closure_angle_jacobian':T.tolist(),'solved_minor':D.tolist(),'minor_determinant':str(D.det()),'base_lengths':[2,1,1,1,1],'base_angles':'all 2*pi/3','length_path':'(2,1+t,1+2*t,1+3*t,1+4*t)','free_coordinates':'x4=t,x5=x6=0; solve x0..x3 by analytic IFT','angle_derivatives':list(ad),'H1_sum_derivatives':h,'claim':'For every sufficiently small t>0, analytic IFT supplies exact strictly convex closed common-length hexagons with five distinct positive lengths. Both avoid H1/H2/H3. No local corona or plane tiling established.'}
audit=[]
for f,w in enumerate(((0,1,2,0,3,4),(0,1,2,0,3,1))):
 for k in range(6):
  for rev in (False,True):
   ss=[(k+(-i if rev else i))%6 for i in range(6)]
   aa=[6*f+(j if rev else (j+1)%6) for j in ss];ll=[w[j] for j in ss]
   for name,match,idx in [('H1',ll[2]==ll[5],[5,0,1]),('H2',ll[1]==ll[3] and ll[2]==ll[5],[5,0,2])]:
    if match:
     dv=s.simplify(sum(ad[aa[i]] for i in idx));assert dv!=0
     audit.append(dict(polygon=f,offset=k,reverse=rev,system=name,angle_indices=[aa[i] for i in idx],sum_derivative=str(dv)))
   assert not(ll[0]==ll[1] and ll[2]==ll[3] and ll[4]==ll[5])
out['full_dihedral_monohedral_audit']=audit
p=Path(__file__).resolve().parents[1]/'certificates/hexagon-thirtytwo-star-analytic-metric-sol-2026-10-19.json';p.write_text(json.dumps(out,default=str,indent=2)+'\n');print(json.dumps(out,default=str,indent=2))
