#!/usr/bin/env python3
"""Finite 90/120/150 interior-angle witness search; exact Sage field arithmetic."""
from sage.all import *
from itertools import product
from pathlib import Path
import json,time,hashlib
A=(0,1,2,0,3,4); B=(0,1,1,0,2,3)
stars=((0,7,6),(1,9,8),(2,3,10),(4,5,11))
K=QuadraticField(3,"r");r=K.gen()
# Directions in multiples of 30 degrees, exact doubled coordinates.
D=((2,0),(r,1),(1,r),(0,2),(-1,r),(-r,1),(-2,0),(-r,-1),(-1,-r),(0,-2),(1,-r),(r,-1))
seq=[a for a in product((90,120,150),repeat=6) if sum(a)==720]
start=time.monotonic();count=0;positive=0;distinct=0;digest=hashlib.sha256();witness=None;representatives=[]
for aa in seq:
 for bb in seq:
  angles=aa+bb
  if any(sum(angles[i] for i in s)!=360 for s in stars):continue
  count+=1;digest.update(bytes(x//30 for x in angles))
  rows=[]
  for f,word in enumerate((A,B)):
   direction=0;xy=[[K(0)]*5 for _ in range(2)]
   for j,c in enumerate(word):
    for q in range(2):xy[q][c]+=K(D[direction%12][q])/2
    direction+=(180-angles[6*f+j])//30
   assert direction==12
   rows.extend(xy)
  M=matrix(K,rows)
  # Cone l>=0, M l=0. A positive point exists iff sum of rays is positive.
  P=Polyhedron(ieqs=[[0]+[int(i==j) for i in range(5)] for j in range(5)],eqns=[[0]+list(row) for row in M],base_ring=K,backend="field")
  rays=[vector(K,v) for v in P.rays_list()]
  if not rays:continue
  total=sum(rays,vector(K,[0]*5))
  if not all(x>0 for x in total):continue
  positive+=1
  if any(all(v[i]==v[j] for v in rays) for i in range(5) for j in range(i)):continue
  distinct+=1
  # Each difference is a nonzero polynomial degree <=len(rays)-1; finite avoidance.
  for t in range(1,10*max(1,len(rays)-1)+2):
   lengths=sum((v*t**j for j,v in enumerate(rays)),vector(K,[0]*5))
   if len(set(lengths))==5:break
  else:raise AssertionError("finite avoidance failed")
  lengths/=lengths[0]
  vertices=[]
  for f,word in enumerate((A,B)):
   direction=0;p=vector(K,[0,0]);vs=[]
   for j,c in enumerate(word):
    vs.append(p);p+=lengths[c]*vector(K,D[direction%12])/2
    direction+=(180-angles[6*f+j])//30
   assert p==vector(K,[0,0]), (angles,lengths,M*lengths,p,rows)
   for j in range(6):
    edge=vs[(j+1)%6]-vs[j]
    for k in range(6):
     if k not in (j,(j+1)%6):assert matrix(K,[edge,vs[k]-vs[j]]).det()>0
   vertices.append(vs)
  def encode(x):return [str(x[0]),str(x[1])]
  representatives.append({"angles":angles,"lengths":[encode(x) for x in lengths],"H1_species":[f for f in range(2) if sum(angles[6*f:6*f+3])==360]})
  if witness is None:witness={"angles":angles,"lengths":[encode(x) for x in lengths],"vertices":[[[encode(x) for x in v] for v in vs] for vs in vertices]}

out={"schema":"FIVE_FOUR_ANGLE_GRID_V1","domain":"12 native interiors in {90,120,150}; each total720; stars (0,7,6),(1,9,8),(2,3,10),(4,5,11) total360","native_sequences":len(seq),"angle_assignments_tested":count,"tested_sha256":digest.hexdigest(),"positive_closure_cones":positive,"distinct_closure_cones":distinct,"status":"witness" if witness else "complete_bounded_exclusion","witness":witness,"seconds":time.monotonic()-start,"runtime_predeclared_seconds":120,"distinct_representatives":representatives}
path=Path(__file__).resolve().parents[1]/"certificates/hexagon-five-four-angle-grid-2026-10-19.json"
path.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
