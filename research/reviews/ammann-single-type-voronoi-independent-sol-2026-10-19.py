#!/usr/bin/env python
"""Independent exact intersection verifier; does not run producer or change its evidence."""
import importlib.util,json,hashlib,itertools,math
from pathlib import Path
from sage.all import *
sp=importlib.util.spec_from_file_location('r','research/searches/ammann-two-class-reconstruct.py')
r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
K,w=r.K,r.w
D=lambda v:sum((K(QQ(x))*w**i for i,x in enumerate(v)),K(0))
N=lambda z:r.real_K(z*z.conjugate())
XY=lambda z:vector(AA,[r.QQbar_of(z).real(),r.QQbar_of(z).imag()])
C=json.loads(Path('research/certificates/ammann-single-type-voronoi-gate-2026-10-19.json').read_text())
raw=Path(C['source_certificate']).read_bytes();assert hashlib.sha256(raw).hexdigest()==C['source_sha256']
S=json.loads(raw);sites=[(D(x['point']),x['type']) for x in S['source_sites']]
refs=r.reference_tiles(QQ(1)/2,QQ(4)/5)
R2=max(N(v-sum(p,K(0))/len(p)) for p in refs.values() for v in p)
polys={}
for rec in C['witnesses']:
 t=rec['type'];a=rec['witness'];i=a['site_index'];c,typ=sites[i];assert typ==t and c==D(a['site_K'])
 constraints=[(2*XY(z-c),N(z-c)) for j,(z,u) in enumerate(sites) if u==t and j!=i and N(z-c)<=16]
 vertices=[]
 for (n,b),(m,d) in itertools.combinations(constraints,2):
  M=matrix(AA,[n,m])
  if M.det()==0:continue
  v=M.solve_right(vector(AA,[b,d]))
  if all(q.dot_product(v)<=e for q,e in constraints) and v not in vertices:vertices.append(v)
 assert len(vertices)==a['corners']
 vertices.sort(key=lambda z:math.atan2(float(z[1]),float(z[0])))
 assert all(matrix(AA,[v-vertices[k-1],vertices[(k+1)%len(vertices)]-v]).det()>0 for k,v in enumerate(vertices))
 B2=max(v.dot_product(v) for v in vertices);assert 4*B2<16
 for j,(z,u) in enumerate(sites):
  if u==t and j!=i:assert all(2*XY(z-c).dot_product(v)<=N(z-c) for v in vertices)
 for aa,bb in S['boundary_segments']:
  aa,bb=D(aa)-c,D(bb)-c;d=bb-aa
  h=max(AA(0),min(AA(1),XY(-aa).dot_product(XY(d))/N(d)))
  assert N(aa)+2*h*XY(aa).dot_product(XY(d))+h*h*N(d)>(2*B2.sqrt()+2*R2.sqrt())**2
 assert sorted(str(x.minpoly()) for v in vertices for x in v)==sorted(q[0] for q in a['vertices_exact_minpoly_interval'])
 polys.setdefault(t,[]).append(vertices)
 print('EXACT CELL',t,i,len(vertices),flush=True)
for t,pp in polys.items():
 for p,q in itertools.combinations(pp,2):
  if len(p)!=len(q):continue
  n=len(p)
  assert not any(all((p[i]-p[j]).dot_product(p[i]-p[j])==(q[(shift+sgn*i)%n]-q[(shift+sgn*j)%n]).dot_product(q[(shift+sgn*i)%n]-q[(shift+sgn*j)%n]) for i in range(n) for j in range(n)) for shift in range(n) for sgn in [-1,1])
 assert any(len(p)<5 for p in pp) or len(pp)>=3
# Rebuild BOTH patches and independently select the geometric neighborhood.
tris=r.sun()
for _ in range(5):tris=r.subdivide(tris)
small=[]
for rh in r.rhombs(tris):
 k,p,_,_=r.place(rh,'B','B',QQ(1)/2,QQ(4)/5);p=[v*r.phi**5 for v in p]
 keep=False
 for rec in C['witnesses']:
  c=D(rec['witness']['site_K']);vv=polys[rec['type']][[x['witness']['site_index'] for x in C['witnesses'] if x['type']==rec['type']].index(rec['witness']['site_index'])]
  cutoff=2*max(v.dot_product(v) for v in vv).sqrt()
  if min(N(v-c) for v in p)<=(cutoff+2*R2.sqrt()+2+QQ(1)/1000)**2:keep=True
 if keep:small.append((k,p[0],p[1]-p[0]))
assert set(small)==set((k,D(o),D(u)) for k,o,u in C['embedded_frames'])
E=json.loads(Path('research/certificates/weighted-ammann-power-source-embedding-2026-10-15.json').read_text());delta=D(E['translation_K']);rot=w**E['rotation_exponent']
tris=[r.sun()[0]]
for _ in range(9):tris=r.subdivide(tris)
lookup=set()
for rh in r.rhombs(tris):
 k,p,_,_=r.place(rh,'B','B',QQ(1)/2,QQ(4)/5);lookup.add((k,p[0]*r.phi**9,(p[1]-p[0])*r.phi**9))
assert all((k,delta+rot*o,rot*u) in lookup for k,o,u in small)
assert len(small)==C['embedded_rhombs']
print('PASS independent exact cells, vertex distance congruence, cutoff, neighborhood selection, embedded frames',len(small))
