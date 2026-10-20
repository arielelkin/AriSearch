#!/usr/bin/env python3
"""Independent certificate check: no SciPy and no producer import."""
import importlib.util,json
from pathlib import Path
from fractions import Fraction as F
root=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('source',root/'research/searches/source-decoration-hat-patch.py')
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
c=json.loads((root/'research/certificates/hat-single-chirality-voronoi-gate-2026-10-19.json').read_text())
def q(x):return h.Q3(F(x[0]),F(x[1]))
def pt(x):return tuple(map(q,x))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),h.ZERO)
def d2(a,b):return dot(sub(a,b),sub(a,b))
def sg(t):return (t[0]*t[4]-t[1]*t[3]).sign()
def ky(p):return tuple(z.key() for z in p)
p0=(h.Q3(F(5,8)),h.Q3(0,F(5,8)))
def expanded(g):
 out=[];h.expand(g,h.IDENT,out);return [t for _,t in out]
def site(t):return tuple(2*z for z in h.transPt(t,p0))
ts=h.constructMetatiles(h.constructPatch(*h.init()))
for entry in c['oriented_occurrence_table']:
 fs=expanded(ts['HTPF'.index(entry['type'])]);assert entry['site_counts']=={str(s):sum(sg(t)*entry['parent_sign']==s for t in fs) for s in (-1,1)}
for entry in c['cover_assignments']:
 fs=expanded(ts['HTPF'.index(entry['type'])]);assert len(entry['hat_assignments'])==len(fs)
 assert sorted(r['hat'] for r in entry['hat_assignments'])==list(range(len(fs)))
 for r in entry['hat_assignments']:
  t=fs[r['hat']];u=fs[r['retained_site']];assert sg(u)*entry['parent_sign']==entry['retained_sign']
  vals=[d2(tuple(2*z for z in h.transPt(t,v)),site(u)) for v in h.hat_outline]
  b=q(r['max_vertex_distance_squared']);assert any(v==b for v in vals) and all((b-v).sign()>=0 for v in vals) and (100-b).sign()>0
for _ in range(2):ts=h.constructMetatiles(h.constructPatch(*ts))
fs=expanded(ts[0]);assert len(fs)==c['source_hats']==1156
assert fs==[list(map(q,t)) for t in c['source_frames']]
ss=list(map(site,fs));assert all(t[0]*t[0]+t[3]*t[3]==h.Q3(F(1,4)) and t[1]*t[1]+t[4]*t[4]==h.Q3(F(1,4)) and t[0]*t[1]+t[3]*t[4]==h.ZERO for t in fs)
edges={};kites=h.ref_kites()
for t in fs:
 for kite in kites:
  vs=[tuple(2*z for z in h.transPt(t,v)) for v in kite]
  for a,b in zip(vs,vs[1:]+vs[:1]):
   k=tuple(sorted((ky(a),ky(b))))
   if k in edges:del edges[k]
   else:edges[k]=(a,b)
assert len(edges)==c['boundary_segments']
def segdist(p,a,b):
 v=sub(b,a);u=dot(sub(p,a),v)/dot(v,v)
 if u.sign()<0:return d2(p,a)
 if (u-1).sign()>0:return d2(p,b)
 return d2(p,tuple(a[k]+u*v[k] for k in (0,1)))
for result in c['results']:
 keep=result['retained_sign'];invariants=[]
 for w in result['witnesses']:
  i=w['hat'];assert sg(fs[i])==keep
  ds=[segdist(ss[i],a,b) for a,b in edges.values()];bd=q(w['boundary_distance_squared'])
  assert bd in ds and all((v-bd).sign()>=0 for v in ds) and (bd-400).sign()>0
  near=[j for j,t in enumerate(fs) if j!=i and sg(t)==keep and (d2(ss[i],ss[j])-400).sign()<=0]
  assert near==w['all_cutoff_neighbors']
  poly=[(h.Q3(x),h.Q3(y)) for x,y in [(-10,-10),(10,-10),(10,10),(-10,10)]]
  for j in near:
   d=sub(ss[j],ss[i]);b=dot(d,d)
   def slack(v):return b-2*dot(d,v)
   new=[]
   for a,z in zip(poly,poly[1:]+poly[:1]):
    sa,sz=slack(a),slack(z)
    if sa.sign()>=0:new.append(a)
    if sa.sign()*sz.sign()<0:
     t=sa/(sa-sz);new.append(tuple(a[k]+t*(z[k]-a[k]) for k in (0,1)))
   poly=[]
   for v in new:
    if not poly or v!=poly[-1]:poly.append(v)
   if len(poly)>1 and poly[0]==poly[-1]:poly.pop()
  assert set(map(ky,poly))==set(map(ky,map(pt,w['relative_vertices'])))
  assert len(poly)==w['side_count']
  assert all((100-dot(v,v)).sign()>0 for v in poly)
  area=sum((a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])),h.ZERO)/2
  assert area==q(w['area']);invariants.append((len(poly),area.key()))
  print(keep,i,len(poly),area)
 assert len(set(invariants))==3
print('PASS: oriented covers, regenerated source, scale, clearance, cutoff, independent exact halfplane clipping and areas')
