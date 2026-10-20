#!/usr/bin/env python3
"""Fixed-site ordinary Voronoi gate after deleting either Hat chirality.
Replay with the repository AGENTS.md wrapper. Exact Q(sqrt3) predicates;
scipy proposes cells only. Finite hierarchy occurrence precedes cell work.
"""
import importlib.util,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import Voronoi
sp=importlib.util.spec_from_file_location('hat',Path(__file__).with_name('source-decoration-hat-patch.py'))
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p0=(h.Q3(F(5,8)),h.Q3(0,F(5,8)))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),h.ZERO)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def d2(a,b):return dot(sub(a,b),sub(a,b))
def sign(t):return (t[0]*t[4]-t[1]*t[3]).sign()
def enc(q):return [str(q.a),str(q.b)]
def ep(p):return [enc(q) for q in p]
def expand(g):
 o=[];h.expand(g,h.IDENT,o);return o
def mx(xs):
 best=xs[0]
 for x in xs[1:]:
  if (x-best).sign()>0:best=x
 return best
def mn(xs):return -mx([-x for x in xs])
# A level-one cluster is a union of actual hats, rather than its ideal
# metatile polygon. For every constituent hat, exhibit one retained site
# at distance <10 from ALL of that hat's vertices. Convexity of the disk
# then covers the entire hat (including its concave outline).
ts=h.constructMetatiles(h.constructPatch(*h.init()))
occ=[];cover=[]
for name,g in zip('HTPF',ts):
 o=expand(g);ss=[tuple(2*z for z in h.transPt(t,p0)) for _,t in o]
 for parent_sign in (-1,1):
  counts={str(c):sum(sign(t)*parent_sign==c for _,t in o) for c in (-1,1)}
  assert all(counts[str(c)]>0 for c in (-1,1))
  occ.append({'type':name,'parent_sign':parent_sign,'site_counts':counts})
  for keep in (-1,1):
   rows=[]
   for i,(_,t) in enumerate(o):
    vv=[tuple(2*z for z in h.transPt(t,v)) for v in h.hat_outline]
    candidates=[(j,mx([d2(v,ss[j]) for v in vv])) for j,(_,u) in enumerate(o) if sign(u)*parent_sign==keep]
    j,b=candidates[0]
    for jj,bb in candidates[1:]:
     if (bb-b).sign()<0:j,b=jj,bb
    assert (100-b).sign()>0
    rows.append({'hat':i,'retained_site':j,'max_vertex_distance_squared':enc(b)})
   cover.append({'type':name,'parent_sign':parent_sign,'retained_sign':keep,'hat_assignments':rows})
print('LEVEL_ONE_OCCURRENCE_AND_R10_COVER_PROVED',flush=True)
# Genuine depth-three H supertile, without the overlapping construction patch.
for _ in range(2):ts=h.constructMetatiles(h.constructPatch(*ts))
o=expand(ts[0]);frames=[t for _,t in o]
ss=[tuple(2*z for z in h.transPt(t,p0)) for t in frames]
chi=[sign(t) for t in frames]
# Boundary of the exact union via primitive full kite edges; shared edges
# cancel. All exposed edges suffice, even if a cluster had holes.
rk=h.ref_kites();boundary={};multiplicity={};centers=set();hex_origin=None
rots=[h.hexPt(2,0),h.hexPt(0,2),h.hexPt(-2,2),h.hexPt(-2,0),h.hexPt(0,-2),h.hexPt(2,-2)]
mids=[h.hexPt(1,1),h.hexPt(-1,2),h.hexPt(-2,1),h.hexPt(-1,-1),h.hexPt(1,-2),h.hexPt(2,-1)]
def key(p):return tuple(z.key() for z in p)
std={tuple(sorted(key(v) for v in [h.pt(0,0),mids[k],rots[(k+1)%6],mids[(k+1)%6]])) for k in range(6)}
for t in frames:
 for kite in rk:
  vv=[tuple(2*z for z in h.transPt(t,v)) for v in kite]
  c=vv[0]
  if hex_origin is None:hex_origin=c
  dx,dy=sub(c,hex_origin);u=dx/3;v=(dy-h.R3*u)/(2*h.R3)
  assert u.b==v.b==0 and u.a.denominator==v.a.denominator==1
  assert tuple(sorted(key(sub(z,c)) for z in vv)) in std
  ck=key(tuple(sum((v[k] for v in vv),h.ZERO)/4 for k in (0,1)))
  assert ck not in centers;centers.add(ck)
  for a,b in zip(vv,vv[1:]+vv[:1]):
   ek=tuple(sorted((key(a),key(b))))
   multiplicity[ek]=multiplicity.get(ek,0)+1;assert multiplicity[ek]<=2
   if ek in boundary:del boundary[ek]
   else:boundary[ek]=(a,b)
def distseg(p,a,b):
 d=sub(b,a);v=sub(p,a);t=dot(v,d)/dot(d,d)
 t=h.ZERO if t.sign()<0 else h.ONE if (t-h.ONE).sign()>0 else t
 return d2(p,tuple(a[k]+t*d[k] for k in (0,1)))
# A center belongs to its own hat interior. If every exposed boundary
# segment has distance >20, its closed 20-disk lies in this source union.
assert h.point_in_poly(p0,h.hat_outline)
floatss=np.array([[float(z) for z in p] for p in ss])
rows=[]
for keep in (-1,1):
 inds=[i for i,c in enumerate(chi) if c==keep]
 vor=Voronoi(floatss[inds]);local={i:k for k,i in enumerate(inds)}
 order=sorted(inds,key=lambda i:float(dot(ss[i],ss[i])))
 witnesses=[];seen=[]
 for i in order:
  reg=vor.regions[vor.point_region[local[i]]]
  if -1 in reg or not reg:continue
  # Cheap float rejection precedes exact completeness proof, never accepts.
  if min(float(distseg(ss[i],a,b)) for a,b in boundary.values())<=400:continue
  bd=mn([distseg(ss[i],a,b) for a,b in boundary.values()]);assert (bd-400).sign()>0
  near=[j for j in inds if j!=i and (d2(ss[i],ss[j])-400).sign()<=0]
  vv=vor.vertices[reg]
  if sum((a[0]*b[1]-a[1]*b[0]) for a,b in zip(vv,np.roll(vv,-1,axis=0)))<0:vv=vv[::-1]
  oo=[]
  for a,b in zip(vv,np.roll(vv,-1,axis=0)):
   m=(a+b)/2
   oo.append(min(near,key=lambda j:abs(np.dot(m-floatss[i],m-floatss[i])-np.dot(m-floatss[j],m-floatss[j]))))
  if len(set(oo))!=len(oo):continue
  vs=[]
  for a,b in zip(oo[-1:]+oo[:-1],oo):
   d=sub(ss[a],ss[i]);e=sub(ss[b],ss[i]);A,B=2*d[0],2*d[1];D,E=2*e[0],2*e[1]
   C,G=dot(d,d),dot(e,e);det=A*E-B*D;assert det.sign()!=0
   v=((C*E-B*G)/det,(A*G-C*D)/det)
   # Actual vertices must lie strictly within R=10.
   assert (100-dot(v,v)).sign()>0
   for j in near:
    w=sub(ss[j],ss[i]);slack=dot(w,w)-2*dot(w,v)
    assert slack.sign()>=0
    if j in (a,b):assert slack.sign()==0
   vs.append(v)
  # Remove any proposed zero sides; scipy's generic facet list must here
  # already be a strictly convex exact cycle.
  for u,v,w in zip(vs,vs[1:]+vs[:1],vs[2:]+vs[:2]):
   a,b=sub(v,u),sub(w,v);assert (a[0]*b[1]-a[1]*b[0]).sign()>0
  area=sum((u[0]*v[1]-u[1]*v[0] for u,v in zip(vs,vs[1:]+vs[:1])),h.ZERO)/2
  n=len(vs)
  if any(n==nn and area==aa for nn,aa in seen):continue
  seen.append((n,area))
  witnesses.append({'hat':i,'chirality':keep,'side_count':n,'area':enc(area),'relative_vertices':[ep(v) for v in vs],
   'edge_neighbors':oo,'all_cutoff_neighbors':near,'boundary_distance_squared':enc(bd)})
  print('witness',keep,i,n,enc(area),flush=True)
  if n<5 or len(witnesses)==3:break
 assert any(w['side_count']<5 for w in witnesses) or len(witnesses)==3,'bounded gate inconclusive'
 rows.append({'retained_sign':keep,'status':'SUB_FIVE_SIDE_OBSTRUCTION' if any(w['side_count']<5 for w in witnesses) else 'THREE_INCONGRUENT_CELLS','witnesses':witnesses})
r={'status':'BOTH_FIXED_CHIRALITY_RULES_EXCLUDED','native_site':['5/8','5sqrt(3)/8'],'coordinate_scale':2,
 'field_encoding':'[a,b] means a+b sqrt(3)','level':1,'oriented_occurrence_table':occ,'cover_assignments':cover,
 'uniform_cover_radius':10,'uniform_neighbor_cutoff':20,'primitive_kite_grid_and_disjointness_verified':True,'source_depth':3,'source_hats':len(o),'boundary_segments':len(boundary),
 'results':rows,'source_frames':[[enc(z) for z in t] for t in frames],
 'scope':'Fixed intrinsic site only. Hierarchical source existence assumed from retained genuine Hat substitution. No output aperiodicity transfer or decoder claim.'}
Path('research/certificates/hat-single-chirality-voronoi-gate-2026-10-19.json').write_text(json.dumps(r,indent=2)+'\n')
print(r['status'])
