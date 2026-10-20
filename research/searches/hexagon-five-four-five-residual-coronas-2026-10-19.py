#!/usr/bin/env python3
"""Independent exact embedding of exactly seven retained formal dimer coronas."""
from sage.all import QuadraticField, vector, matrix
import json
from pathlib import Path
K=QuadraticField(3,'r'); r=K.gen()
W=((0,1,2,0,3,4),(0,1,1,0,2,3)); L=(1,2,3,r,4)
angles=((90,120,150,120,90,150),(150,120,90,150,90,120))
D=((1,0),(r/2,K(1)/2),(K(1)/2,r/2),(0,1),(-K(1)/2,r/2),(-r/2,K(1)/2),(-1,0),(-r/2,-K(1)/2),(-K(1)/2,-r/2),(0,-1),(K(1)/2,-r/2),(r/2,-K(1)/2))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'certificates/hexagon-five-four-39-omissions-2026-10-19.json').read_text())
def scalar(x):return K(x[0])+K(x[1])*r
all_results=[]
for row_index in (15,16,23,26,31):
 row=source['rows'][row_index]
 polys=[[vector(K,[scalar(x) for x in v]) for v in p] for p in row['vertices']]
 for p in polys:
  assert all(cross(p[(i+1)%6]-p[i],p[j]-p[i])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
 A=polys[0]; mate=[A[5]+A[0]-v for v in A]
 boundary=A[:5]+mate[:5]
 def place(k,state):
  s,h=state;f,j=divmod(s,6);native=polys[f]
  a,b=boundary[k],boundary[(k+1)%10]
  # CCW neighbor traverses the shared edge backwards; CW neighbor forwards.
  target0,target1=(b,a) if h==1 else (a,b)
  u=native[(j+1)%6]-native[j];t=target1-target0
  J=lambda x:vector(K,[-x[1],x[0]])
  M=matrix(K,[[u[0],J(u)[0]],[u[1],J(u)[1]]])
  N=matrix(K,[[t[0],h*J(t)[0]],[t[1],h*J(t)[1]]])
  T=N*M.inverse();assert T.transpose()*T==matrix.identity(K,2)
  translation=target0-T*native[j]
  transforms.append(dict(species=f,native_side=j,handedness=h,matrix=[[str(x) for x in rr] for rr in T.rows()],translation=[str(x) for x in translation]))
  return [target0+T*(v-native[j]) for v in native]
 def key(p):return tuple(sorted(tuple(x) for x in p))
 def overlap(p,q):
  # Strict convex polygons: separating axis criterion, valid for either orientation.
  for poly,other in ((p,q),(q,p)):
   orient=1 if cross(poly[1]-poly[0],poly[2]-poly[1])>0 else -1
   for i in range(6):
    if all(orient*cross(poly[(i+1)%6]-poly[i],x-poly[i])<=0 for x in other):return False
  return True
 root=Path(__file__).resolve().parents[1]
 atlas=json.loads((root/'certificates/hexagon-five-four-forced-dimer-2026-10-19.json').read_text())
 coronas=next(x for x in atlas['rows'] if x['B']==list(W[1]))['boundary_coronas'];assert len(coronas)==7
 results=[]
 for idx,states in enumerate(coronas):
  transforms=[]
  neighbors=[place(k,states[k+1]) for k in range(10)]
  # Formal junctions require that adjacent edges with the same third sector
  # are occupied by the identical Euclidean tile, not just native state labels.
  bad_identity=[]
  for k in (0,5):
   if key(neighbors[(k-1)%10])!=key(neighbors[k]):bad_identity.append(k)
  unique={key(p):p for p in [A,mate]+neighbors};patch=list(unique.values())
  overlaps=[[i,j] for i in range(len(patch)) for j in range(i) if overlap(patch[i],patch[j])]
  # Gap-free iff exact angular sectors cover every central boundary vertex.
  # Convex sectors are disjoint after overlap check; angles computed from native incidence.
  sums=[]
  for v in boundary:
   total=0
   for p in patch:
    for i,x in enumerate(p):
     if x==v:
      u=p[i-1]-v;w=p[(i+1)%6]-v
      # Dot products identify 90/120/150 exactly.
      dot=u.dot_product(w);n2=u.dot_product(u)*w.dot_product(w)
      if dot==0:a=90
      elif dot<0 and 4*dot*dot==n2:a=120
      elif dot<0 and 4*dot*dot==3*n2:a=150
      else:raise AssertionError('unexpected angle')
      total+=a
   sums.append(total)
  results.append(dict(corona=idx,isometries=transforms,identity_failures=bad_identity,overlaps=overlaps,vertex_angle_sums=sums,unique_tiles=len(patch),valid=not bad_identity and not overlaps and sums==[360]*10,patch=[[[str(x) for x in v] for v in p] for p in patch]))
 all_results.append(dict(row_index=row_index,results=results))
out=dict(schema='FIVE_RESIDUAL_SEVEN_CORONA_EXACT_V1',field='Q(r), r^2=3, r>0',domain=dict(rows=[15,16,23,26,31],coronas_per_row=7,total_cap=35),rows=all_results)
(root/'certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
for row in all_results:
 print(row['row_index'],[(x['corona'],x['valid'],x['identity_failures'],x['overlaps'],x['vertex_angle_sums']) for x in row['results']])
