#!/usr/bin/env python3
"""Exact interval gate for finite witnessed Hat Voronoi side counts.
No numerical predicate is accepted as proof; scipy only proposes edge orders.
"""
import importlib.util,json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import Voronoi
sp=importlib.util.spec_from_file_location('hat',Path(__file__).with_name('source-decoration-hat-patch.py'))
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
class I:
 def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b)
 def __add__(a,b):
  b=ii(b);return I(a.a+b.a,a.b+b.b)
 __radd__=__add__
 def __neg__(a):return I(-a.b,-a.a)
 def __sub__(a,b):return a+-ii(b)
 def __rsub__(a,b):return ii(b)+-a
 def __mul__(a,b):
  b=ii(b);x=[a.a*b.a,a.a*b.b,a.b*b.a,a.b*b.b];return I(min(x),max(x))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=ii(b)
  if b.a<=0<=b.b:raise ZeroDivisionError
  return a*I(1/b.b,1/b.a)
def ii(x):return x if isinstance(x,I) else I(x)
rl=F(173205080756887729352744634150587236694280525381038,10**50)
assert rl*rl<3<(rl+F(1,10**50))**2
r3=I(rl,rl+F(1,10**50))
def qi(q):return q.a+q.b*r3
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def sub(a,b):return [a[k]-b[k] for k in (0,1)]
def site(t,u,v):
 p=[I(F(5,8))+u,F(5,8)*r3+v]
 return [2*(qi(t[0])*p[0]+qi(t[1])*p[1]+qi(t[2])),2*(qi(t[3])*p[0]+qi(t[4])*p[1]+qi(t[5]))]
def exact_key(p):return tuple(z.key() for z in p)
ts=h.init()
for _ in range(3):ts=h.constructMetatiles(h.constructPatch(*ts))
out=[];h.expand(ts[0],h.IDENT,out)
frames=[t for _,t in out]
p0=(h.Q3(F(5,8)),h.Q3(0,F(5,8)))
s0=[tuple(2*z for z in h.transPt(t,p0)) for t in frames]
# Finite neighborhood upper domain: any site <=2R at some p is <=2R+2rho
# from the central site at p0. Use rational 2R+2rho<10.
assert F(301,16)<F(35,8)**2
assert F(1734,100)**2<301 and (F(1734,400)+F(5,32))**2>20
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
float_sites=np.array([[float(z) for z in p] for p in s0]);vor=Voronoi(float_sites)
orders={}
for i in near:
 rr=vor.regions[vor.point_region[i]];assert -1 not in rr
 verts=vor.vertices[rr];area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(verts,np.roll(verts,-1,axis=0)))
 if area<0:verts=verts[::-1]
 order=[]
 for a,b in zip(verts,np.roll(verts,-1,axis=0)):
  mid=(a+b)/2;order.append(min(near[i],key=lambda j:abs(np.dot(mid-float_sites[i],mid-float_sites[i])-np.dot(mid-float_sites[j],mid-float_sites[j]))))
 assert len(order)==len(set(order));orders[i]=order
# Check each proposed vertex is strictly inside all nonincident halfplanes.
# Incident equalities are exact by the 2x2 formula. Positive oriented edge
# lengths ensure each proposed side survives and the convex cycle closes.
def boxcheck(i,box):
 u=I(box[0],box[1]);v=I(box[2],box[3]);base=site(frames[i],u,v)
 hs={}
 for j in near[i]:
  a=frames[j];b=frames[i];d=[]
  for k in (0,3):
   L=2*(a[k]-b[k]);M=2*(a[k+1]-b[k+1]);C=L*p0[0]+M*p0[1]+2*(a[k+2]-b[k+2])
   d.append(qi(C)+qi(L)*u+qi(M)*v)
  hs[j]=(2*d[0],2*d[1],dot(d,d))
 oo=orders[i];vs=[]
 try:
  for a,b in zip(oo[-1:]+oo[:-1],oo):
   A,B,C=hs[a];D,E,G=hs[b];det=A*E-B*D
   x=(C*E-B*G)/det;y=(A*G-C*D)/det
   if (x*x+y*y).b>=20:return False
   for j,(L,M,N) in hs.items():
    if j not in (a,b) and (L*x+M*y-N).b>=0:return False
   vs.append((x,y))
  for n,j in enumerate(oo):
   A,B,C=hs[j];d=sub(vs[(n+1)%len(vs)],vs[n])
   if (A*d[1]-B*d[0]).a<=0:return False
 except ZeroDivisionError:return False
 return True
rho=F(5,32)
result={'status':'INCOMPLETE','native_p0':['5/8','5sqrt(3)/8'],'delta':'5/8','rho':'5/32','separation_lower':'15/16','cover_radius':'sqrt(301)/4+5/32','primitive_kites_disjoint_on_one_grid':True,'boundary_segments':len(boundary),'depth':3,'hats':len(out),'neighborhood_complete_radius_10':complete,'cells':[]}
for i in near:
 pending=[(-rho,rho,-rho,rho,0)];passed=0;passed_domain=[];failed=[];maxdepth=0
 while pending:
  x0,x1,y0,y1,d=pending.pop();maxdepth=max(maxdepth,d)
  # Discard boxes disjoint from the closed disk, using rational arithmetic.
  x=min(abs(x0),abs(x1)) if x0*x1>0 else 0;y=min(abs(y0),abs(y1)) if y0*y1>0 else 0
  if x*x+y*y>rho*rho:continue
  if boxcheck(i,(x0,x1,y0,y1)):
   passed+=1;passed_domain.append([str(z) for z in (x0,x1,y0,y1)]);continue
  if d==18:failed.append([str(z) for z in (x0,x1,y0,y1)]);break
  if x1-x0>=y1-y0:
   m=(x0+x1)/2;pending.extend([(x0,m,y0,y1,d+1),(m,x1,y0,y1,d+1)])
  else:
   m=(y0+y1)/2;pending.extend([(x0,x1,y0,m,d+1),(x0,x1,m,y1,d+1)])
 row={'hat':i,'sides':len(orders[i]),'edge_neighbors':orders[i],'near_count':len(near[i]),'passed_boxes':passed,'parameter_boxes':passed_domain,'max_depth':maxdepth,'failed_box':failed,'proved':not failed and complete[i]}
 result['cells'].append(row);print({k:v for k,v in row.items() if k!='parameter_boxes'},flush=True)
if all(r['proved'] for r in result['cells']) and len(set(r['sides'] for r in result['cells']))==3:result['status']='UNIFORM_THREE_SIDE_COUNT_OBSTRUCTION'
result['frames']={str(i):[[str(z.a),str(z.b)] for z in frames[i]] for i in near}
Path('research/certificates/hat-voronoi-existence-gate-2026-10-19.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
