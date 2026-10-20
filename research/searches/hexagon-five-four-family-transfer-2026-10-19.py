#!/usr/bin/env python3
"""Recover fixed four-face gluing and exact augmented rational angle gate.
No nonlinear solver or carrier search. Uses only retained input certificates.
"""
from pathlib import Path
import json
from sage.all import QuadraticField, vector, matrix, QQ, ZZ
root=Path(__file__).resolve().parents[2]
read=lambda p:json.loads((root/p).read_text())
d=read("research/certificates/hexagon-five-four-second-periodic-2026-10-19.json")
atlas=read("research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json")
a=next(x for x in atlas["rows"] if x["B"]==[0,1,1,0,2,3])
stars=a["fixed_stars"]
K=QuadraticField(3,"r")
polys=[[vector(K,v) for v in f["vertices"]] for f in d["representatives"]]
L=matrix(K,[vector(K,v) for v in d["periods"]]).transpose()
# Validate native vertex maps independently by distances. Stored B boundaries
# reverse native indices because the corresponding copies are reflected.
vertex_maps=[list(range(6)),list(range(6)),[(5-i)%6 for i in range(6)],[(5-i)%6 for i in range(6)]]
for f,p in enumerate(polys):
 q=[vector(K,v) for v in d["prototile_vertices"][d["representatives"][f]["type"]]]
 z=vertex_maps[f]
 assert all((p[i]-p[j]).norm()**2==(q[z[i]]-q[z[j]]).norm()**2 for i in range(6) for j in range(6))
def corner(f,i):return 6*d["representatives"][f]["type"]+(vertex_maps[f][i]-1)%6
def side(f,i):return i if f<2 else (4-i)%6
edges=[];adj={i:set() for i in range(24)};faces={f:set() for f in range(4)}
for f,p in enumerate(polys):
 for i in range(6):
  matches=[]
  for g,q in enumerate(polys):
   for j in range(6):
    z=L.inverse()*(p[i]-q[(j+1)%6])
    if p[(i+1)%6]-p[i]==q[j]-q[(j+1)%6] and all(x in ZZ for x in z):matches.append((g,j,z))
  assert len(matches)==1
  g,j,z=matches[0]
  if (f,i)<(g,j):
   edges.append({"stored":[[f,i],[g,j]],"native_sides":[side(f,i),side(g,j)],"handedness":[1 if f<2 else -1,1 if g<2 else -1],"offset":[int(x) for x in z]})
   faces[f].add(g);faces[g].add(f)
   for u,v in [(6*f+i,6*g+(j+1)%6),(6*f+(i+1)%6,6*g+j)]:adj[u].add(v);adj[v].add(u)
words=[[0,1,2,0,3,4],[0,1,1,0,2,3]]
for e in edges:
 (f,i),(g,j)=e["stored"]
 assert words[d["representatives"][f]["type"]][side(f,i)]==words[d["representatives"][g]["type"]][side(g,j)]
assert len(edges)==12
# Link graph nodes are face corners; each joined endpoint identifies the two
# neighboring corner sectors. Degree two plus connectivity is precisely circle.
assert all(len(v)==2 for v in adj.values())
remaining=set(adj);links=[]
while remaining:
 start=min(remaining);cycle=[];prev=None;cur=start
 while cur not in cycle:
  cycle.append(cur);nxt=next(v for v in sorted(adj[cur]) if v!=prev);prev,cur=cur,nxt
 assert cur==start
 remaining.difference_update(cycle);links.append(cycle)
assert len(links)==8 and 8-12+4==0
seen={0}
while True:
 new=seen|set().union(*(faces[f] for f in seen))
 if new==seen:break
 seen=new
assert len(seen)==4
# All polygons CCW and edge identifications reverse their boundary directions:
# orientations extend, while the circular links establish a closed surface.
def row(cs,total):
 v=[0]*13
 for c in cs:v[c]+=1
 v[-1]=-total
 return v
carrier=[row([corner(*divmod(c,6)) for c in cyc],2) for cyc in links]
mask=33416;indices=[i for i in range(len(stars)) if mask>>i&1]
support=[row([c for c,h in stars[i]],2) for i in indices]+[row(range(6),4),row(range(6,12),4)]
S=matrix(QQ,support);C=matrix(QQ,carrier)
basis=S.row_space().basis_matrix();extra=[]
for i,v in enumerate(C.rows()):
 if v not in basis.row_space():
  extra.append({"vertex":i,"row":list(v)});basis=basis.stack(v).row_space().basis_matrix()
coefficients=[]
for v in C.rows():
 coefficients.append(list(S.transpose().solve_right(v)) if v in S.row_space() else None)
extra_equality=[0]*13
extra_equality[2]=1;extra_equality[9]=-1
assert matrix(QQ,support+[extra_equality]).row_space()==S.stack(C).row_space()
# Conditional transfer applies exactly to this retained subset of the grid.
grid=read("research/certificates/hexagon-five-four-angle-grid-2026-10-19.json")
selected=[]
for index,entry in enumerate(grid["distinct_representatives"]):
 angles=entry["angles"]
 if angles[2]!=angles[9]:continue
 lengths=[K(x[0])+K(x[1])*K.gen() for x in entry["lengths"]]
 assert all(x>0 for x in lengths) and len(set(lengths))==5
 for word,aa in zip(([0,1,2,0,3,4],[0,1,1,0,2,3]),(angles[:6],angles[6:])):
  from sage.all import cos,sin,pi
  vertices=[vector(K,[0,0])];heading=0
  for color,angle in zip(word,aa):
   direction=vector(K,[K(cos(pi*heading/180)),K(sin(pi*heading/180))])
   vertices.append(vertices[-1]+lengths[color]*direction);heading+=180-angle
  assert vertices[-1]==vertices[0] and heading==360
  cross=lambda u,v:u[0]*v[1]-u[1]*v[0]
  assert all(cross(vertices[(i+1)%6]-vertices[i],vertices[j]-vertices[i])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
 assert all(sum(row[i]*QQ(angles[i])/180 for i in range(12))+row[-1]==0 for row in support+carrier)
 selected.append({"grid_index":index,"angles_degrees":angles,"lengths":entry["lengths"],"prior_H1_species":entry["H1_species"]})
assert len(selected)==18 and sum(not x["prior_H1_species"] for x in selected)==13
output={"angle_units":"pi; augmented final coordinate is negative RHS","support_mask":mask,"support_star_indices":indices,"support_signed_stars":[stars[i] for i in indices],"edge_pairs":edges,"vertex_links":[[[c//6,c%6] for c in cyc] for cyc in links],"native_vertex_rows":carrier,"support_augmented_rows":support,"support_rank":S.rank(),"carrier_rank":C.rank(),"combined_rank":S.stack(C).rank(),"extra_codimension":S.stack(C).rank()-S.rank(),"independent_extra_rows":extra,"rational_coefficients":coefficients,"span_passes":all(v in S.row_space() for v in C.rows()),"conditional_extra_equality":extra_equality,"grid_selected":selected,"grid_nonmonohedral_selected":sum(not x["prior_H1_species"] for x in selected),"topology":{"F":4,"E":12,"V":8,"connected":True,"orientable":True,"all_links_circles":True,"surface":"torus"}}
# JSON encode rational values exactly, never as floats.
def enc(x):
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 if x in ZZ and not isinstance(x,(str,bool)):return int(x)
 return str(x) if x in QQ else x
path=root/"research/certificates/hexagon-five-four-family-transfer-2026-10-19.json"
path.write_text(json.dumps(enc(output),indent=2)+"\n")
print("Topology: connected orientable torus F=4 E=12 V=8; all links circles")
print("Augmented ranks:",S.rank(),C.rank(),S.stack(C).rank(),"extra codimension",len(extra))
print("Independent extra rows:",extra)
print("PASS" if output["span_passes"] else "STOP: angle implication fails")
