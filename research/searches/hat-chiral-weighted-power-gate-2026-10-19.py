#!/usr/bin/env python3
"""Exact fixed-site, chirality-weighted Hat power-cell finite witness gate.
All proof predicates use rational Q(sqrt(3)) arithmetic.
"""
import importlib.util,json,sys
from pathlib import Path
from fractions import Fraction as F
sp=importlib.util.spec_from_file_location('hat',Path(__file__).with_name('source-decoration-hat-patch.py'))
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def sub(a,b):return [a[k]-b[k] for k in (0,1)]
def exact_key(p):return tuple(z.key() for z in p)
ts=h.init()
for _ in range(3):ts=h.constructMetatiles(h.constructPatch(*ts))
out=[];h.expand(ts[0],h.IDENT,out)
frames=[t for _,t in out]
p0=(h.Q3(F(5,8)),h.Q3(0,F(5,8)))
s0=[tuple(2*z for z in h.transPt(t,p0)) for t in frames]
# Fixed-site finite domain, justified by weighted cutoff inequalities below.
near={i:[j for j in range(len(out)) if j!=i and (dot(sub(s0[j],s0[i]),sub(s0[j],s0[i]))-100).sign()<0] for i in (509,519,516)}
# Exact boundary of the union in native full-Hat units, from full kite edges.
boundary={}
rk=h.ref_kites()
centers=set()
edge_multiplicity={}
hex_origin=None
rots=[h.hexPt(2,0),h.hexPt(0,2),h.hexPt(-2,2),h.hexPt(-2,0),h.hexPt(0,-2),h.hexPt(2,-2)]
mids=[h.hexPt(1,1),h.hexPt(-1,2),h.hexPt(-2,1),h.hexPt(-1,-1),h.hexPt(1,-2),h.hexPt(2,-1)]
std={tuple(sorted(exact_key(v) for v in [h.pt(0,0),mids[k],rots[(k+1)%6],mids[(k+1)%6]])) for k in range(6)}

for t in frames:
 for k in rk:
  kk=[tuple(2*z for z in h.transPt(t,v)) for v in k]
  c=kk[0]
  if hex_origin is None:hex_origin=c
  dx,dy=h.psub(c,hex_origin)
  uu=dx/3;vv=(dy-h.R3*uu)/(2*h.R3)
  assert uu.b==vv.b==0 and uu.a.denominator==vv.a.denominator==1
  assert tuple(sorted(exact_key(h.psub(v,c)) for v in kk)) in std
  cen=tuple(sum((v[k] for v in kk),h.ZERO)/4 for k in (0,1))
  assert exact_key(cen) not in centers
  centers.add(exact_key(cen))
  for a,b in zip(kk,kk[1:]+kk[:1]):
   key=tuple(sorted((exact_key(a),exact_key(b))))
   edge_multiplicity[key]=edge_multiplicity.get(key,0)+1
   assert edge_multiplicity[key]<=2
   if key in boundary:del boundary[key]
   else:boundary[key]=(a,b)
def dist2seg(p,a,b):
 d=sub(b,a);w=sub(p,a);t=dot(w,d)/dot(d,d)
 t=h.ZERO if t.sign()<0 else h.ONE if (t-h.ONE).sign()>0 else t
 q=[a[k]+t*d[k] for k in (0,1)];e=sub(p,q);return dot(e,e)
assert h.point_in_poly(p0,h.hat_outline)
assert p0==tuple(sum((v[k] for v in rk[0]),h.ZERO)/4 for k in (0,1))
boundary_d2=[dist2seg(p0,a,b) for a,b in zip(h.hat_outline,h.hat_outline[1:]+h.hat_outline[:1])]
assert min(boundary_d2,key=float)==h.Q3(F(25,64))
vertex_d2=[dot(sub(p0,v),sub(p0,v)) for v in h.hat_outline]
assert max(vertex_d2,key=float)==h.Q3(F(301,16))
assert all((q-F(25,64)).sign()>=0 for q in boundary_d2)
assert all((F(301,16)-q).sign()>=0 for q in vertex_d2)
# The p0-centered radius 10 disk lies in this finite union iff its boundary
# is farther than 10 and its center is interior. Center is in its own Hat.
complete={i:all((dist2seg(s0[i],a,b)-100).sign()>0 for a,b in boundary.values()) for i in near}

# New gate: p fixed; weight lambda iff determinant negative.
# All affine halfplane predicates are checked at both interval endpoints.
L=F(1,4)
assert all(complete.values())
chi=[]
for t in frames:
 det=t[0]*t[4]-t[1]*t[3]
 assert det in (h.Q3(F(1,4)),h.Q3(F(-1,4)))
 chi.append(int(det.sign()<0))
orders={509:[507,510,516,480,523],519:[518,516,508,511,513,517],516:[509,510,508,519,518,520,480]}
# Check that unmarked Hat has trivial Euclidean stabilizer, including reflection.
V=h.hat_outline
sym=[]
a,b=V[:2];ab=sub(b,a);n=dot(ab,ab)
for c in V:
 for d in V:
  cd=sub(d,c)
  if dot(cd,cd)!=n:continue
  for reflect in (False,True):
   def image(v):
    q=sub(v,a);u=dot(q,ab)/n;w=(ab[0]*q[1]-ab[1]*q[0])/n
    if reflect:w=-w
    return (c[0]+u*cd[0]-w*cd[1],c[1]+u*cd[1]+w*cd[0])
   if set(map(image,V))==set(V):sym.append((c==a,d==b,reflect))
assert sym==[(True,True,False)],sym
rows=[]
for i,oo in orders.items():
 hs={j:(2*sub(s0[j],s0[i])[0],2*sub(s0[j],s0[i])[1],dot(sub(s0[j],s0[i]),sub(s0[j],s0[i]))) for j in near[i]}
 endpoint=[]
 for lam in (-L,L):
  vs=[]
  for a,b in zip(oo[-1:]+oo[:-1],oo):
   A,B,C=hs[a];D,E,G=hs[b];C+=lam*(chi[i]-chi[a]);G+=lam*(chi[i]-chi[b]);det=A*E-B*D
   assert det.sign()!=0
   x=(C*E-B*G)/det;y=(A*G-C*D)/det
   assert (20-x*x-y*y).sign()>0
   for j,(U,W,N) in hs.items():
    if j not in (a,b):assert (N+lam*(chi[i]-chi[j])-U*x-W*y).sign()>0,(i,j,lam)
   vs.append((x,y))
  for k,j in enumerate(oo):
   A,B,_=hs[j];dd=sub(vs[(k+1)%len(vs)],vs[k]);assert (A*dd[1]-B*dd[0]).sign()>0
  endpoint.append({'lambda':str(lam),'vertices_relative':[[[str(z.a),str(z.b)] for z in v] for v in vs]})
 rows.append({'target':i,'chirality':chi[i],'sides':len(oo),'edge_neighbors':oo,'near_count':len(near[i]),'endpoints':endpoint})
# Global weighted radius C=sqrt(305)/4. For d>=10: d^2-2Cd-1/4>0.
assert F(305,16)<20
assert (F(399,4))**2>400*20
# All sites retain a cell: separation >=5/4 and weight spread <=1/4.
assert F(25,16)>L
result={'status':'EXACT_WEIGHTED_THREE_SIDE_COUNT_OBSTRUCTION','parameter_interval':['-1/4','1/4'],'intrinsic_site':['5/8','5sqrt(3)/8'],'weight_rule':'lambda iff native full-size frame has negative determinant, otherwise 0','reference_hat_stabilizer':'identity only (all ordered vertex-pair isometries, both determinants)','source_dependency':'same genuine level-3 H source occurrence and primary hierarchy theorem as prior reviewed gate','source_hats':len(frames),'actual_boundary_radius_10_complete':complete,'finite_neighbor_cutoff':'10','weighted_cover_radius':'sqrt(305)/4','combinatorial_transitions_in_interval':[],'partition':[{'closed_interval':['-1/4','1/4'],'side_counts':[5,6,7]}],'surviving_parameters':[],'cells':rows,'frames':{str(i):[[str(z.a),str(z.b)] for z in frames[i]] for i in orders}}
# Assess first algebraic cycle failure beyond declared gate; do not extend gate.
roots=[]
for i,oo in orders.items():
 hs={j:(2*sub(s0[j],s0[i])[0],2*sub(s0[j],s0[i])[1],dot(sub(s0[j],s0[i]),sub(s0[j],s0[i]))) for j in near[i]}
 vals=[]
 for lam in (0,1):
  vs=[];sl=[]
  for a,b in zip(oo[-1:]+oo[:-1],oo):
   A,B,C=hs[a];D,E,G=hs[b];C+=lam*(chi[i]-chi[a]);G+=lam*(chi[i]-chi[b]);det=A*E-B*D
   x=(C*E-B*G)/det;y=(A*G-C*D)/det;vs.append((x,y))
   for j,(U,W,N) in hs.items():
    if j not in (a,b):sl.append((('slack',a,b,j),N+lam*(chi[i]-chi[j])-U*x-W*y))
  for k,j in enumerate(oo):
   A,B,_=hs[j];dd=sub(vs[(k+1)%len(vs)],vs[k]);sl.append((('edge',j),A*dd[1]-B*dd[0]))
  vals.append(sl)
 for (key,a),(key2,b) in zip(*vals):
  assert key==key2 and a.sign()>0
  if (b-a).sign():
   r=-a/(b-a)
   assert (r-L).sign()>0 or (r+L).sign()<0
   roots.append({'target':i,'predicate':key,'root':[str(r.a),str(r.b)]})
positive=[h.Q3(*r['root']) for r in roots if h.Q3(*r['root']).sign()>0]
negative=[h.Q3(*r['root']) for r in roots if h.Q3(*r['root']).sign()<0]
pfirst=h.Q3(F(226,69));nfirst=h.Q3(F(-249,68))
assert pfirst in positive and nfirst in negative
assert all((r-pfirst).sign()>=0 for r in positive)
assert all((nfirst-r).sign()>=0 for r in negative)
# The cutoff itself permits |lambda|<=249/68: 100-M>20 sqrt(301/16+M).
M=F(249,68)
assert (100-M)**2>400*(F(301,16)+M)
result['outside_gate_assessment']={'all_incumbent_cycle_predicate_roots':roots,'first_positive_root':'226/69','first_negative_root':'-249/68','radius_10_cutoff_valid_through_absolute_weight':'249/68','universal_nonempty_cell_bound_proved_only_for':'abs(lambda)<25/16','status':'ALGEBRAIC_CYCLE_EVENTS_ONLY_NOT_AN_ENLARGED_GATE'}
# Exact local samples around first events. These do not extend the global nonempty-site gate.
def clip(poly,A,B,C):
 out=[]
 for u,v in zip(poly,poly[1:]+poly[:1]):
  fu=C-A*u[0]-B*u[1];fv=C-A*v[0]-B*v[1]
  if fu.sign()>=0:out.append(u)
  if fu.sign()*fv.sign()<0:
   t=fu/(fu-fv);out.append(tuple(u[k]+t*(v[k]-u[k]) for k in (0,1)))
 clean=[]
 for v in out:
  if not clean or v!=clean[-1]:clean.append(v)
 if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
 return clean
samples=[]
for lam in (F(226,69)-F(1,100),F(226,69),F(226,69)+F(1,100),F(-249,68)-F(1,100),F(-249,68),F(-249,68)+F(1,100)):
 counts=[];areas=[]
 for i in orders:
  poly=[h.pt(-5,-5),h.pt(5,-5),h.pt(5,5),h.pt(-5,5)]
  for j in near[i]:
   d=sub(s0[j],s0[i]);poly=clip(poly,2*d[0],2*d[1],dot(d,d)+lam*(chi[i]-chi[j]))
  assert len(poly)>=3
  # Remove collinear split vertices to count intrinsic polygon sides.
  changed=True
  while changed:
   changed=False
   for k,v in enumerate(poly):
    a=sub(v,poly[k-1]);b=sub(poly[(k+1)%len(poly)],v)
    if (a[0]*b[1]-a[1]*b[0]).sign()==0:poly.pop(k);changed=True;break
  assert all((F(365,16)-dot(v,v)).sign()>0 for v in poly)
  counts.append(len(poly))
  area2=sum((u[0]*v[1]-u[1]*v[0] for u,v in zip(poly,poly[1:]+poly[:1])),h.ZERO)
  assert area2.sign()>0
  areas.append(area2)
 if lam==F(226,69):assert areas[1]!=areas[2]
 if lam==F(-249,68):assert areas[0]!=areas[1]
 samples.append({'lambda':str(lam),'side_counts_509_519_516':counts,'doubled_areas_509_519_516':[[str(a.a),str(a.b)] for a in areas]})
# M=4: cutoff10 remains valid; these bounded polygons are the actual local cells.
assert (100-4)**2>400*F(365,16)
result['outside_gate_assessment']['exact_local_samples']=samples
result['outside_gate_assessment']['sample_scope']='actual three source cells only; no assertion that all source sites retain cells'
Path('research/certificates/hat-chiral-weighted-power-gate-2026-10-19.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
