"""Fresh reconstruction of the fixed 35 cases; no enumeration beyond them."""
from sage.all import QuadraticField, vector, matrix, Polyhedron
from pathlib import Path
import json
K=QuadraticField(3,"r"); r=K.gen(); root=Path(__file__).resolve().parents[1]
load=lambda name:json.loads((root/"certificates"/name).read_text())
src=load("hexagon-five-four-39-omissions-2026-10-19.json")
atlas=load("hexagon-five-four-forced-dimer-2026-10-19.json")
cert=load("hexagon-five-four-five-residual-coronas-2026-10-19.json")
states=next(z["boundary_coronas"] for z in atlas["rows"] if z["B"]==[0,1,1,0,2,3])
assert len(states)==7 and len(src["rows"])==39
key=lambda p:tuple(sorted(tuple(v) for v in p))
def angle(p,i):
 u=p[i-1]-p[i]; v=p[(i+1)%6]-p[i]; d=u*v; n=(u*u)*(v*v)
 if d==0:return 90
 assert d<0
 if 4*d*d==n:return 120
 assert 4*d*d==3*n
 return 150
for rec in cert["rows"]:
 idx=rec["row_index"]; row=src["rows"][idx]
 P=[[vector(K,[K(a)+r*K(b) for a,b in v]) for v in p] for p in row["vertices"]]
 assert [angle(p,(i+1)%6) for p in P for i in range(6)]==row["angles"]
 lengths=[K(a)+r*K(b) for a,b in row["lengths"]]
 assert all(x>0 for x in lengths) and len(set(lengths))==5
 for p,word in zip(P,[(0,1,2,0,3,4),(0,1,1,0,2,3)]):
  for i,color in enumerate(word):
   e=p[(i+1)%6]-p[i]
   assert e*e==lengths[color]**2
   assert all(e[0]*(p[j]-p[i])[1]-e[1]*(p[j]-p[i])[0]>0 for j in range(6) if j not in (i,(i+1)%6))
 A=P[0]; C=[A[0]+A[5]-v for v in A]; bd=A[:5]+C[:5]
 for ci,ss in enumerate(states):
  ns=[]; transforms=[]
  for k,(s,h) in enumerate(ss[1:]):
   f,j=divmod(s,6); p=P[f]; a,b=bd[k],bd[(k+1)%10]
   x,y=(b,a) if h==1 else (a,b)
   u=p[(j+1)%6]-p[j]; t=y-x
   # Solve the two endpoint equations directly for rotation/reflection coefficients.
   if h==1:
    aa=(u*t)/(u*u); bb=(u[0]*t[1]-u[1]*t[0])/(u*u)
    M=matrix(K,[[aa,-bb],[bb,aa]])
   else:
    aa=(u[0]*t[0]-u[1]*t[1])/(u*u); bb=(u[1]*t[0]+u[0]*t[1])/(u*u)
    M=matrix(K,[[aa,bb],[bb,-aa]])
   shift=x-M*p[j]; q=[M*v+shift for v in p]
   assert M.transpose()*M==matrix.identity(K,2) and M.det()==h
   assert q[j]==x and q[(j+1)%6]==y
   ns.append(q); transforms.append((f,j,h,M,shift))
  patch=list({key(p):p for p in [A,C]+ns}.values())
  z=rec["results"][ci]
  assert [k for k in (0,5) if key(ns[k-1])!=key(ns[k])]==z["identity_failures"]
  polys=[Polyhedron(vertices=p,base_ring=K) for p in patch]
  overlaps=[[i,j] for i in range(len(patch)) for j in range(i) if polys[i].intersection(polys[j]).dim()==2]
  assert overlaps==z["overlaps"]
  sums=[sum(angle(p,p.index(v)) for p in patch if v in p) for v in bd]
  assert sums==z["vertex_angle_sums"]
  assert len(patch)==z["unique_tiles"] and {key(p) for p in patch}=={key([vector(K,v) for v in p]) for p in z["patch"]}
  for t,(f,j,h,M,v) in zip(z["isometries"],transforms):
   assert (f,j,h)==(t["species"],t["native_side"],t["handedness"])
   assert M==matrix(K,t["matrix"]) and v==vector(K,t["translation"])
  assert z["valid"]==(ci==6)
  if ci==6:
   assert len(patch)==10 and not overlaps and sums==[360]*10
   assert [t[:3] for t in transforms]==[(1,0,-1),(1,2,-1),(1,4,-1),(0,3,1),(1,5,-1)]*2
  print(idx,ci,"identity",z["identity_failures"],"overlaps",overlaps,"angles",sums)
print("PASS all 35 reconstructions, all certificate fields and all five native angle vectors")
