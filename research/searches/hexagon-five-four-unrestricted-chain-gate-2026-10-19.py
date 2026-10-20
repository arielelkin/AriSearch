#!/usr/bin/env python3
"""Exact local flat-host obstruction to unrestricted AA full-seam decoding.
Domain: five retained rows, four exterior right-corner species assignments.
No finite-patch extension claim, randomness, solver, or collar search.
"""
from sage.all import QuadraticField, vector, matrix
from pathlib import Path
import json
K=QuadraticField(3,'r');r=K.gen()
root=Path(__file__).resolve().parents[1]
src=json.loads((root/'certificates/hexagon-five-four-39-omissions-2026-10-19.json').read_text())
def scalar(a):return K(a[0])+K(a[1])*r
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def encode(a):return [str(x) for x in a]
results=[]
for ri in (15,16,23,26,31):
 ps=[[vector(K,[scalar(x) for x in v]) for v in p] for p in src['rows'][ri]['vertices']]
 A=ps[0]; a,b=A[5],A[0];u=b-a;J=lambda v:vector(K,[-v[1],v[0]])
 # Outward right normal: host A lies in the left halfplane.
 n=-J(u); m=(a+b)/2
 corners=[]
 for p in ps:
  candidates=[i for i in range(6) if (p[i-1]-p[i]).dot_product(p[(i+1)%6]-p[i])==0]
  assert candidates
  corners.append(candidates[0])
 for left in (0,1):
  for right in (0,1):
   transforms=[]; patches=[A]
   for f,sign in ((left,-1),(right,1)):
    p=ps[f];i=corners[f];v=p[i-1]-p[i];w=p[(i+1)%6]-p[i]
    # Map the two perpendicular inward rays to sign*u and the outward normal.
    V=matrix(K,[[v[0],w[0]],[v[1],w[1]]])
    tv=sign*u/(u.norm())*v.norm();tw=n/n.norm()*w.norm()
    M=matrix(K,[[tv[0],tw[0]],[tv[1],tw[1]]])*V.inverse()
    assert M.transpose()*M==matrix.identity(K,2)
    t=m-M*p[i];q=[M*x+t for x in p]
    # Full polygons occupy disjoint exterior quadrants. Their rays and host
    # therefore cover a complete sufficiently small disk around m.
    assert all((x-m).dot_product(n)>=0 and sign*(x-m).dot_product(u)>=0 for x in q)
    assert q[i]==m
    patches.append(q)
    transforms.append(dict(species=f,right_vertex=i,matrix=[encode(z) for z in M.rows()],translation=encode(t),determinant=str(M.det())))
   assert all(cross(u,x-a)>=0 for x in A)
   # m is a genuine side-interior subdivision: neither exterior tile can
   # contain the whole A5 seam because it stays on only one longitudinal side.
   assert m!=a and m!=b
   results.append(dict(row=ri,host_side=5,split=encode(m),exterior_species=[left,right],isometries=transforms,patch=[[encode(v) for v in p] for p in patches]))
out=dict(schema='RESIDUAL_HEXAGON_FLAT_HOST_LOCAL_V1',domain=dict(rows=[15,16,23,26,31],species_assignments=4,total=20),claim='locally disk-complete split A5 contacts; no plane extension asserted',results=results)
(root/'certificates/hexagon-five-four-unrestricted-chain-gate-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(results),'exact disk-complete flat-host patches; no global extension claim')
