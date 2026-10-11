"""Independent rational native geometry and affine-link proof for open2D cone.
No author imports. Positive closed ordered directions imply strict convexity.
"""
from sage.all import QuadraticField,PolynomialRing,AA
from pathlib import Path
from itertools import product
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,['t','u']);t,u=R.gens();F=R.fraction_field()
cd=F(1-t*t)/F(1+t*t);sd=F(2*t)/F(1+t*t)
cg=F(1-u*u)/F(1+u*u);sg=F(2*u)/F(1+u*u)
p=2*cd/(1+2*cg)
def rot(v,C,S):return (C*v[0]-S*v[1],S*v[0]+C*v[1])
def add(x,y):return tuple(a+b for a,b in zip(x,y))
A=[]
for C,S in [(1,0),(-K(1)/2,w/2),(-K(1)/2,-w/2)]:A.extend([rot((p,0),C,S),rot(rot((K(1)/2,w/2),cd,sd),C,S)])
B=[(p,0),rot((p,0),cg,sg),rot((p,0),cg*cg-sg*sg,2*cg*sg),rot(rot((-K(1)/2,w/2),cd,-sd),cg,sg),rot(rot((-1,0),cd,sd),cg,sg),rot(rot((-K(1)/2,-w/2),cd,-sd),cg,sg)]
for typ,edges in enumerate((A,B)):
 assert tuple(sum(e[k] for e in edges) for k in (0,1))==(0,0)
 for i,e in enumerate(edges):
  norm=p if (i%2==0 if typ==0 else i<3) else 1
  assert sum(a*a for a in e)==norm*norm
# Native affine angles and successive turns independently from actual direction words.
D=[[(0,0,0),(60,1,0),(120,0,0),(180,1,0),(240,0,0),(300,1,0)],[(0,0,0),(0,0,1),(0,0,2),(120,-1,1),(180,1,1),(240,-1,1)]]
angles=[];turns=[]
for word in D:
 angles.append([(180+word[i-1][0]-word[i][0]-(360 if i==0 else 0),word[i-1][1]-word[i][1],word[i-1][2]-word[i][2]) for i in range(6)])
 turns.append([(word[(i+1)%6][0]-word[i][0]+(360 if i==5 else 0),word[(i+1)%6][1]-word[i][1],word[(i+1)%6][2]-word[i][2]) for i in range(6)])
verts=[(0,0),(30,0),(30,90),(0,120)];bounds=[]
for typ,tw in enumerate(turns):
 assert tuple(sum(a[k] for a in tw) for k in range(3))==(360,0,0)
 for a in tw:
  values=[a[0]+a[1]*d+a[2]*g for d,g in verts]
  assert min(values)>=0 and 0<max(values)<180
  bounds.append((min(values),max(values)))
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'certificates/branching-hexagon-new-two-run-two-parameter-periodic-cone.json').read_text())
for typ,name in enumerate(('A','B')):
 assert [list(a) for a in angles[typ]]==r[name+'_angles']
 assert [list(a) for a in D[typ]]==r[name+'_edge_directions']
 assert [list(a) for a in turns[typ]]==r[name+'_turns']
assert r['closed_parameter_polygon_vertices']==[list(v) for v in verts]
assert bounds==[(x['closed_domain_min'],x['closed_domain_max']) for x in r['turn_bounds']]
# Obtain actual corner-link cycles directly from seam successor; no author class logic.
fs=r['faces'];pairs=r['paired_edges'];assert len(fs)==8 and len(pairs)==24
assert [(f['species'],f['mirror']) for f in fs]==[('A',False)]*2+[('A',True)]*2+[('B',False)]*2+[('B',True)]*2
labels=[['p','q']*3,['p']*3+['q']*3];fa=[];fl=[]
for f in fs:
 typ=0 if f['species']=='A' else 1
 fa.append([angles[typ][(-i)%6] for i in range(6)] if f['mirror'] else angles[typ])
 fl.append(labels[typ][::-1] if f['mirror'] else labels[typ]);assert f['labels']==fl[-1]
succ={};dual=[set() for f in fs]
for (a,i),(b,j) in pairs:
 assert fl[a][i]==fl[b][j] # Exact even when numerical p=q.
 assert (a,i) not in succ and (b,j) not in succ
 succ[a,i]=(b,(j+1)%6);succ[b,j]=(a,(i+1)%6)
 dual[a].add(b);dual[b].add(a)
assert len(succ)==48 and len(set(succ.values()))==48
unseen=set(succ);links=[]
while unseen:
 start=min(unseen);a=start;link=[]
 while a not in link:link.append(a);unseen.remove(a);a=succ[a]
 assert a==start and len(link)==3
 assert tuple(sum(fa[a][i][k] for a,i in link) for k in range(3))==(360,0,0)
 links.append(frozenset(link))
assert len(links)==16 and set(links)=={frozenset(map(tuple,a)) for a in r['vertex_classes']}
assert all(a==[360,0,0] for a in r['angle_sums'])
seen={0};todo=[0]
while todo:
 for a in dual[todo.pop()]:
  if a not in seen:seen.add(a);todo.append(a)
assert len(seen)==8 and 16-24+8==0
print('PASS raw2variable rational closures and all12 squared edge norms;independent native affine angles/turns;all12strict turn bounds;48 unique equal-label seams;16actual circular360+0delta+0gamma links;connected orientable flat torus. Includes numerical p=q unchanged.')
