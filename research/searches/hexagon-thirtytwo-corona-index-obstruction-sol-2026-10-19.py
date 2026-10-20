#!/usr/bin/env python3
"""Exact first-order audit of actual builder corner angles; no search."""
import importlib.util,json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('atlas',root/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
r=m.build((0,1,2,0,3,1))
C=s.zeros(6,12)
for f in range(2):
 for j in range(6):C[f,6*f+j]=1
for row,inds in enumerate(((0,1,8),(2,7,11),(3,6,10),(4,5,9)),2):
 for i in inds:C[row,i]=1
N=s.Matrix.hstack(*C.nullspace());J=s.zeros(4,12);L=s.zeros(4,5)
for f,w in enumerate((m.A,r['B'])):
 for j,c in enumerate(w):
  L[2*f,c]+=s.cos(j*s.pi/3);L[2*f+1,c]+=s.sin(j*s.pi/3)
  for k in range(1,j+1):
   J[2*f,6*f+k]+=s.sin(j*s.pi/3)*(2 if c==0 else 1)
   J[2*f+1,6*f+k]-=s.cos(j*s.pi/3)*(2 if c==0 else 1)
T=J*N;D=T[:,:4];assert D.det()==-3
v=-D.inv()*(L*s.Matrix([0,1,2,3,4])+T[:,4])
ad=(N*s.Matrix(list(v)+[1,0,0])).applyfunc(s.simplify)
records=[]
for k,star in enumerate(r['fixed_stars']):
 actual=[6*(c//6)+(c+1)%6 for c,h in star]
 residual=s.simplify(sum(ad[i] for i in actual))
 assert residual!=0
 records.append(dict(index=k,star=star,actual_angle_indices=actual,residual_derivative=str(residual)))
assert len(records)==32 and len(r['boundary_coronas'])==100
out=dict(schema='THIRTYTWO_CORONA_INDEX_OBSTRUCTION_SOL_V1',angle_derivatives=list(map(str,ad)),stars=records,star_count=32,formal_corona_count=100,corona59=r['boundary_coronas'][59],claim='All 32 builder stars and therefore all 100 builder coronas fail actual angle compatibility for sufficiently small nonzero t in the specified IFT family. A corrected corner-indexed IFT family is outside this certificate.')
p=root/'research/certificates/hexagon-thirtytwo-corona-index-obstruction-sol-2026-10-19.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(stars_checked=32,zero_residual_derivatives=0,formal_coronas_excluded=100)))
