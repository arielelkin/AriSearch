"""Independent bounded carrier audit; no search or producer imports."""
import json
from pathlib import Path
from sage.all import QQ, QuadraticField, matrix, vector, cos, sin, pi
R=Path(__file__).resolve().parents[2]
read=lambda name:json.loads((R/'research/certificates'/name).read_text())
c=read('hexagon-five-four-family-transfer-2026-10-19.json')
fixture=read('hexagon-five-four-second-periodic-2026-10-19.json')
grid=read('hexagon-five-four-angle-grid-2026-10-19.json')['distinct_representatives']
# Independent fixed side pairing recovered in the earlier fixture review.
pairs=[(0,0,3,4),(0,1,2,2),(0,2,1,2),(0,3,3,1),(0,4,2,5),(0,5,1,5),(1,0,2,4),(1,1,3,2),(1,3,2,1),(1,4,3,5),(2,0,3,0),(2,3,3,3)]
assert [e['stored'] for e in c['edge_pairs']]==[[[f,i],[g,j]] for f,i,g,j in pairs]
words=((0,1,2,0,3,4),(0,1,1,0,2,3))
K=QuadraticField(3,'r')
polys=[[vector(K,v) for v in f['vertices']] for f in fixture['representatives']]
L=matrix(K,fixture['periods']).transpose()
link={ (f,i):[] for f in range(4) for i in range(6)}
used=[]
for f,i,g,j in pairs:
 used.extend([(f,i),(g,j)])
 native=lambda f,i:i if f<2 else (4-i)%6
 assert words[f//2][native(f,i)]==words[g//2][native(g,j)]
 assert polys[f][(i+1)%6]-polys[f][i]==polys[g][j]-polys[g][(j+1)%6]
 assert all(z in QQ and z.denominator()==1 for z in L.inverse()*(polys[f][i]-polys[g][(j+1)%6]))
 for a,b in [((f,i),(g,(j+1)%6)),((f,(i+1)%6),(g,j))]:link[a].append(b);link[b].append(a)
assert len(set(used))==24
assert all(len(v)==2 for v in link.values())
cycles=[];remaining=set(link)
while remaining:
 start=min(remaining);v=start;prev=None;cy=[]
 while v not in cy:
  cy.append(v);nxt=next(w for w in link[v] if w!=prev);prev,v=v,nxt
 assert v==start
 remaining-=set(cy);cycles.append(cy)
assert [set(cy) for cy in cycles]==[set(tuple(x) for x in cy) for cy in c['vertex_links']]
assert len(cycles)==8
# Corner index: native vertex k is the end of native side k-1.
rows=[]
for cy in cycles:
 row=[0]*13;row[12]=-2
 for f,i in cy:row[6*(f//2)+((i-1)%6 if f<2 else (4-i)%6)]+=1
 rows.append(row)
assert rows==c['native_vertex_rows']
S=matrix(QQ,c['support_augmented_rows']);C=matrix(QQ,rows)
assert (S.rank(),C.rank(),S.stack(C).rank())==(5,4,6)
extra=[0]*13;extra[2]=1;extra[9]=-1
assert S.stack(matrix(QQ,[extra])).row_space()==S.stack(C).row_space()
assert any(row not in S.row_space() for row in C.rows())
selected=[]
for n,e in enumerate(grid):
 aa=e['angles']
 if aa[2]!=aa[9]:continue
 selected.append(n)
 lens=[K(a)+K(b)*K.gen() for a,b in e['lengths']]
 assert min(lens)>0 and len(set(lens))==5
 for w,angles in zip(words,(aa[:6],aa[6:])):
  p=[vector(K,[0,0])];h=0
  for col,angle in zip(w,angles):
   assert 0<angle<180
   p.append(p[-1]+lens[col]*vector(K,[cos(pi*h/180),sin(pi*h/180)]));h+=180-angle
  assert h==360 and p[-1]==p[0]
  for i in range(6):
   u=p[(i+1)%6]-p[i]
   for j in range(6):
    if j in (i,(i+1)%6):continue
    v=p[j]-p[i];assert u[0]*v[1]-u[1]*v[0]>0
 assert all(sum(row[i]*QQ(aa[i])/180 for i in range(12))+row[12]==0 for row in list(S.rows())+rows)
assert selected==[e['grid_index'] for e in c['grid_selected']]
assert len(selected)==18 and sum(not grid[n]['H1_species'] for n in selected)==13
print('PASS: independent fixed gluing, circular links, angle ranks, 18 exact metrics, 13 retained H1-empty labels')
