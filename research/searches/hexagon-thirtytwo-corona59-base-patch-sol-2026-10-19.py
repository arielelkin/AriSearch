#!/usr/bin/env python3
"""Exact embedded base patch and native star certificate for corona59."""
import sympy as s,importlib.util,json,itertools,functools
from pathlib import Path
root=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('atlas',root/'research/searches/hexagon-five-four-forced-dimer-2026-10-19.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);r=m.build((0,1,2,0,3,1));corona=r['boundary_coronas'][59]
def zclean(z):return s.simplify(s.expand_complex(z))
def xy(z):return (s.re(z),s.im(z))
def cross(a,b):return s.simplify(s.im(s.conjugate(a)*b))
V=[s.Integer(0)]
for j,l in enumerate((2,1,1,2,1,1)):V.append(zclean(V[-1]+l*s.exp(s.I*j*s.pi/3)))
assert V[-1]==0;V=V[:6];Q=[zclean(V[5]-z) for z in V]
faces=[dict(name='P',f=0,h=1,v=V),dict(name='Q',f=0,h=1,v=Q)]
for k,((side,h),P,j) in enumerate(zip(corona[1:],[Q]*5+[V]*5,list(range(5))*2)):
 f,ss=divmod(side,6);v=V if h==1 else [s.conjugate(z) for z in V]
 a,b=P[j],P[(j+1)%6];aa,bb=(b,a) if h==1 else (a,b)
 rr=zclean((bb-aa)/(v[(ss+1)%6]-v[ss]));tt=zclean(aa-rr*v[ss]);vv=[zclean(rr*z+tt) for z in v]
 faces.append(dict(name=str(k),f=f,h=h,v=vv))
# Seam labels refer to one tile each, not multiple overlapping tiles.
assert faces[2]['v']==faces[11]['v'];assert faces[6]['v']==faces[7]['v']
faces=[a for a in faces if a['name'] not in ('5','9')]
assert len(faces)==10
edges={};vertices={}
for f in faces:
 for j,z in enumerate(f['v']):
  vertices.setdefault(z,[]).append((f['name'],6*f['f']+(j-1)%6,f['h']))
  key=tuple(sorted((z,f['v'][(j+1)%6]),key=lambda x:tuple(map(str,xy(x)))))
  edges.setdefault(key,[]).append((f['name'],j))
assert all(len(x)<=2 for x in edges.values())
words=((0,1,2,0,3,4),(0,1,2,0,3,1))
for inc in edges.values():
 if len(inc)==2:
  colors=[words[next(f['f'] for f in faces if f['name']==name)][j] for name,j in inc]
  assert colors[0]==colors[1]
internal=[v for v,inc in vertices.items() if len(inc)==3]
assert len(internal)==10 and len(vertices)==32 and len(edges)==41
support={2,5,13,15,17,20,22,23};star_records=[]
for z in internal:
 inc=vertices[z]
 assert any(name in ('P','Q') for name,c,h in inc)
 # Sort sectors clockwise by direction of the tile centroid from the vertex.
 def direction(q):return zclean(sum(next(f['v'] for f in faces if f['name']==q[0]))/6-z)
 def compare(p,q):
  a,b=direction(p),direction(q)
  ha=1 if s.im(a)<0 or (s.im(a)==0 and s.re(a)<0) else 0;hb=1 if s.im(b)<0 or (s.im(b)==0 and s.re(b)<0) else 0
  if ha!=hb:return ha-hb
  cr=cross(a,b);return -1 if cr>0 else (1 if cr<0 else 0)
 inc.sort(key=functools.cmp_to_key(compare),reverse=True)
 star=tuple((c,h) for _,c,h in inc);canon=m.canon(star)
 idx=r['fixed_stars'].index(canon);assert idx in support
 star_records.append(dict(vertex=str(z),incidence=inc,star_index=idx))
# Every pair of distinct convex tiles has a supporting separating axis.
# Record axes; classify contact by shared base vertices.
pairs=[]
for a,b in itertools.combinations(faces,2):
 sep=[]
 for f,g in ((a,b),(b,a)):
  for j,z in enumerate(f['v']):
   vals=[f['h']*cross(f['v'][(j+1)%6]-z,w-z) for w in g['v']]
   if all(x<=0 for x in vals):sep.append((f['name'],j,max(vals)))
 assert sep
 common=set(a['v'])&set(b['v']);assert len(common) in (0,2)
 if not common:assert any(x[2]<0 for x in sep)
 pairs.append(dict(tiles=[a['name'],b['name']],shared_vertices=len(common),separation_axes=[[n,j,str(v)] for n,j,v in sep]))
assert sum(p['shared_vertices']==2 for p in pairs)==19
out=dict(schema='CORONA59_BASE_EMBEDDING_SOL_V1',corona=corona,faces=[dict(name=f['name'],polygon=f['f'],hand=f['h'],vertices=list(map(str,f['v']))) for f in faces],identified_labels=[['0','9'],['4','5']],vertices=len(vertices),edges=len(edges),faces_count=len(faces),internal_vertices=star_records,edge_incidence=[dict(endpoints=list(map(str,k)),incidence=v) for k,v in edges.items()],pair_certificates=pairs)
p=root/'research/certificates/hexagon-thirtytwo-corona59-base-patch-sol-2026-10-19.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(faces=10,vertices=32,edges=41,internal_vertices=10,adjacent_pairs=19,nonadjacent_pairs=26,star_indices=sorted({x['star_index'] for x in star_records}))))
