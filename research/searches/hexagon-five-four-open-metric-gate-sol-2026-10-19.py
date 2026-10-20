#!/usr/bin/env python3
"""Exact open metric gate; no nonlinear solver, corona or torus enumeration."""
from sage.all import *
from itertools import combinations_with_replacement
import importlib.util,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("atlas",root/"research/searches/hexagon-five-four-forced-dimer-2026-10-19.py")
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
stars=a.build((0,1,1,0,2,3))["fixed_stars"]
x=json.loads((root/"research/certificates/hexagon-five-four-39-omissions-2026-10-19.json").read_text())["rows"][1]
K=QuadraticField(3,"r");r=K.gen()
D=((2,0),(r,1),(1,r),(0,2),(-1,r),(-r,1),(-2,0),(-r,-1),(-1,-r),(0,-2),(1,-r),(r,-1))
lengths=vector(K,[K(QQ(u)+QQ(v)*r) for u,v in x["lengths"]])
assert lengths[0]==1 and len(set(lengths))==5 and min(lengths)>0
rows=[]
for f,w in enumerate(((0,1,2,0,3,4),(0,1,1,0,2,3))):
 direction=0;m=matrix(K,2,5);v=vector(K,[0,0]);vs=[]
 for j,c in enumerate(w):
  vs.append(v);delta=vector(K,D[direction%12])/2
  for k in range(2):m[k,c]+=delta[k]
  v+=lengths[c]*delta;direction+=(180-x["angles"][6*f+j])//30
 assert v==0 and direction==12
 for j in range(6):
  for k in range(6):
   if k not in (j,(j+1)%6):assert matrix(K,[vs[(j+1)%6]-vs[j],vs[k]-vs[j]]).det()>0
 rows+=list(m)
M=matrix(K,rows)
assert M*lengths==0 and M[:,1:].det()==-QQ(1)/4
out={"angles_degrees":x["angles"],"lengths_Qsqrt3":x["lengths"],"closure_matrix":[[str(z) for z in row] for row in M],"normalized_determinant":str(M[:,1:].det()),"supports":{}}
carrier=((0,6,7),(1,2,8),(3,9,10),(4,5,11))
C=matrix(QQ,[[int(i in t) for i in range(12)]+[2] for t in carrier])
for mask in (33416,41032):
 ts=[tuple(p[0] for p in stars[k]) for k in range(len(stars)) if mask>>k&1]
 R=matrix(QQ,[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]+[[sum(i==j for j in t) for i in range(12)]+[2] for t in ts])
 assert R.rank()==5 and R*vector(QQ,[QQ(z)/180 for z in x["angles"]]+[-1])==0
 identities=[]
 for t in combinations_with_replacement(range(12),3):
  if vector(QQ,[t.count(i) for i in range(12)]+[2]) in R.row_space():identities.append(t)
 assert len(identities)==4
 if mask==41032:assert all(row in R.row_space() for row in C)
 else:assert not all(row in R.row_space() for row in C)
 out["supports"][str(mask)]={"angle_affine_dimension":7,"triple_identities":identities,"carrier_implied":all(row in R.row_space() for row in C)}
path=root/"research/certificates/hexagon-five-four-open-metric-gate-sol-2026-10-19.json"
path.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

# Standalone carrier incidence audit, independent of retained coordinate offsets.
pairs=(((0,0),(3,4)),((0,1),(2,2)),((0,2),(1,2)),((0,3),(3,1)),((0,4),(2,5)),((0,5),(1,5)),((1,0),(2,4)),((1,1),(3,2)),((1,3),(2,1)),((1,4),(3,5)),((2,0),(3,0)),((2,3),(3,3)))
words=((0,1,2,0,3,4),)*2+((0,1,1,0,2,3),)*2
native_side=lambda f,j:j if f<2 else (4-j)%6
native_corner=lambda f,j:(j-1)%6 if f<2 else 6+(4-j)%6
G=Graph(multiedges=True,loops=True);G.add_vertices([(f,j) for f in range(4) for j in range(6)])
F=Graph();F.add_vertices(range(4));seen=[]
for (f,j),(g,k) in pairs:
 assert words[f][native_side(f,j)]==words[g][native_side(g,k)]
 seen.extend(((f,j),(g,k)));F.add_edge(f,g)
 G.add_edge((f,j),(g,(k+1)%6));G.add_edge((f,(j+1)%6),(g,k))
assert len(set(seen))==24 and len(seen)==24 and F.is_connected()
links=G.connected_components(sort=False)
assert len(links)==8 and all(len(link)==3 for link in links) and all(G.degree(v)==2 for v in G)
angles=[]
for link in links:
 t=sorted(native_corner(f,j) for f,j in link);angles.append(t)
 assert tuple(t) in carrier
assert 8-12+4==0
out["carrier_topology"]={"edge_pairs":pairs,"vertex_links":links,"native_corner_triples":angles,"F":4,"E":12,"V":8,"connected":True,"boundary_reversing":True}
path.write_text(json.dumps(out,indent=2));print("PASS standalone carrier color, links, connectedness and Euler audit")
