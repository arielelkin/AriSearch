#!/usr/bin/env sage -python
"""Exact source reconstruction and power-cell witness gate."""
import importlib.util, json, sys
from pathlib import Path
from sage.all import *
spec=importlib.util.spec_from_file_location('rec',Path(__file__).with_name('ammann-two-class-reconstruct.py'))
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
K,w=rec.K,rec.w
s,t=QQ(1)/2,QQ(4)/5
ref=rec.reference_tiles(s,t)
def norm(z):return rec.real_K(z*z.conjugate())
def dot(z,v):return rec.real_K((z*v.conjugate()+z.conjugate()*v)/2)
def cross(z,v):return rec.turn(z,v)*AA(QQbar.zeta(10).imag())
def xy(z):return vector(AA,[AA(rec.QQbar_of(z).real()),AA(rec.QQbar_of(z).imag())])
def segdist2(z,a,b):
 d=b-a; lam=max(AA(0),min(AA(1),dot(z-a,d)/norm(d)))
 return norm(z-a)-2*lam*dot(z-a,d)+lam*lam*norm(d)
means={k:sum(p,K(0))/len(p) for k,p in ref.items()}
rho2=min(cross(p[(i+1)%len(p)]-p[i],means[k]-p[i])**2/norm(p[(i+1)%len(p)]-p[i]) for k,p in ref.items() for i in range(len(p)))
R2=max(norm(z-means[k]) for k,p in ref.items() for z in p)
C=(R2+rho2).sqrt(); L=C+(C*C+rho2).sqrt()
assert L+2*R2.sqrt()<3
print('constants',float(rho2),float(R2),float(L),flush=True)
tris=rec.sun();n=5
for _ in range(n):tris=rec.subdivide(tris)
rh=rec.rhombs(tris);scale=rec.phi**n
ecount={}
for r in rh:
 for i in range(4):
  e=frozenset([r[1][i]*scale,r[1][(i+1)%4]*scale]);ecount[e]=ecount.get(e,0)+1
bnd=[tuple(e) for e,m in ecount.items() if m==1]
segs=[]
for r in rh:segs += [(a*scale,b*scale) for a,b in rec.place(r,'B','B',s,t)[3]]
faces,adj=rec.faces_of(segs,bnd)
polys=[];sites=[]
for face in faces:
 if any(adj[a][b]=='bnd' for a,b in face):continue
 p=[a for a,b in face]
 if rec.area_sign(p)<=0:continue
 assert rec.strict_convex_ccw(p)
 typ=next((k for k,q in ref.items() if rec.direct_congruent(p,q) or rec.direct_congruent(rec.mirror(p),q)),None)
 assert typ is not None
 polys.append(p);sites.append((sum(p,K(0))/len(p),typ))
print('source',len(sites),flush=True)
# The finite graph tiles the complete rhomb union; boundary faces are discarded.
assert sum(rec.area2([a for a,b in f]) for f in faces if rec.area_sign([a for a,b in f])>0)==sum(rec.area2([z*scale for z in r[1]]) for r in rh)
assert sum(rec.area_sign([a for a,b in f])<0 for f in faces)==1
# Exact closed-box validation.  Intersections and every slack are affine in weights.
box=rho2/2
corners=[(a,b) for a in [-box,box] for b in [-box,box]]
def constraints(i,a,b):
 c,typ=sites[i]; wt={'H6':AA(0),'P1':a,'P2':b}
 return [(j,2*xy(d),norm(d)+wt[typ]-wt[k]) for j,(p,k) in enumerate(sites) if j!=i and norm(d:=p-c)<=L*L]
def vertices(cs):
 out=[]
 for h,(j,n,b) in enumerate(cs):
  for k,m,d in cs[h+1:]:
   A=matrix(AA,[n,m])
   if A.det()==0:continue
   v=A.inverse()*vector(AA,[b,d])
   if all(nn.dot_product(v)<=bb for jj,nn,bb in cs):
    if not any(v==vv for pp,vv in out):out.append((tuple(sorted([j,k])),v))
 return out
cert=[]
for i,expected in [(43,7),(44,6),(45,5)]:
 c,typ=sites[i]
 margin2=min(segdist2(c,a,b) for a,b in bnd)
 assert margin2>(L+2*R2.sqrt())**2
 assert margin2>9
 cs0=constraints(i,AA(0),AA(0));v0=vertices(cs0)
 pairs=[pair for pair,v in v0]
 # Order the zero-weight vertices by their actual active-side incidence.
 active=[{j for j,n,bb in cs0 if n.dot_product(v)==bb} for pair,v in v0]
 order=[0]
 while len(order)<len(v0):
  nxt=[j for j in range(len(v0)) if j not in order and active[order[-1]]&active[j]]
  assert nxt
  order.append(nxt[0])
 assert active[order[-1]]&active[order[0]]
 pairs=[pairs[j] for j in order]
 assert len(pairs)==expected
 vv0=[v0[j][1] for j in order]
 turns=[matrix(AA,[vv0[(z+1)%expected]-vv0[z],vv0[(z+2)%expected]-vv0[(z+1)%expected]]).det() for z in range(expected)]
 assert all(q>0 for q in turns) or all(q<0 for q in turns)
 slackmins=[];lengthmins=[]
 for a,b in corners:
  cs=constraints(i,a,b);D={j:(n,bb) for j,n,bb in cs}
  vv=[]
  for j,k in pairs:
   n,e=D[j];m,f=D[k]
   v=matrix(AA,[n,m]).inverse()*vector(AA,[e,f]);vv.append(v)
   assert v.dot_product(v)<=C*C
   slacks=[bb-nn.dot_product(v) for jj,nn,bb in cs if jj not in [j,k]]
   assert min(slacks)>=0
   slackmins.append(min(slacks))
  # Fixed normals, feasible affine vertices, and positive affine edge
  # projections preserve the exact strict corner cycle, including ties.
  assert len(vertices(cs))==expected
  for z in range(len(vv)):
   edge=vv[(z+1)%len(vv)]-vv[z]
   edge0=v0[order[(z+1)%len(vv)]][1]-v0[order[z]][1]
   assert edge.dot_product(edge0)>0
   lengthmins.append(edge.dot_product(edge0))
   assert matrix(AA,[edge,edge0]).det()==0
 print('EXACT',i,typ,expected,'margin2',float(margin2),'slackmin',float(min(slackmins)), 'pairs',pairs,flush=True)
 cert.append({'site':i,'source_type':typ,'corners':expected,'active_pairs':pairs,'site_K':[str(x) for x in c.vector()], 'neighbor_indices':[j for j,n,b in cs0], 'boundary_distance2_minpoly':str(margin2.minpoly()), 'minimum_edge_projection_approx':float(min(lengthmins))})
print('PASS: three actual cells have 7,6,5 strict corners throughout the CLOSED box',flush=True)
if '--output' in sys.argv:
 Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps({'source':{'sun_deflations':5,'thin_option':'B','thick_option':'B','s':'1/2','t':'4/5','scale':'phi^5'},'basis':'1,w,w^2,w^3; w=exp(i*pi/5)', 'source_polygons':[[[str(x) for x in z.vector()] for z in p] for p in polys], 'source_sites':[{'type':k,'point':[str(x) for x in c.vector()]} for c,k in sites], 'boundary_segments':[[[str(x) for x in z.vector()] for z in e] for e in bnd], 'witnesses':cert},indent=2)+'\n')
