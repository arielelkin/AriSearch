#!/usr/bin/env python3
"""Exact first gate for a fixed corner-mean site in a genuine Spectre source.
Author recurrence: https://cs.uwaterloo.ca/~csk/spectre/spectre.js
Only Q3 scalar/matrix primitives are borrowed from the retained Hat utility.
"""
import importlib.util, json, hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import Voronoi
P=Path(__file__).parent
assert hashlib.sha256((P.parent/'sources/spectre-author-2026-10-19.js').read_bytes()).hexdigest()=='d4d7758f268e2e5f3f56deb771f6f783e519f5351b46f8e6e05c0f629d2f6df1'
sp=importlib.util.spec_from_file_location('q',P/'source-decoration-hat-patch.py')
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
Q=h.Q3; z=Q(0); r=Q(0,1); I=h.IDENT
def pt(x,y):return (h.q3(x),h.q3(y))
v=[pt(0,0),pt(1,0),pt(F(3,2),-r/2),pt((3+r)/2,(1-r)/2),
   pt((3+r)/2,(3-r)/2),pt((5+r)/2,(3-r)/2),pt((6+r)/2,F(3,2)),
   pt(3,2),pt((6-r)/2,F(3,2)),pt((5-r)/2,(3+r)/2),
   pt((3-r)/2,(3+r)/2),pt((1-r)/2,(3+r)/2),pt(-r/2,F(3,2)),pt(0,1)]
c=tuple(sum((a[k] for a in v),z)/14 for k in (0,1))
assert h.point_in_poly(c,v)
def sub(a,b):return h.psub(a,b)
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm(a):return dot(a,a)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
corners=[a for b,a,d in zip(v[-1:]+v[:-1],v,v[1:]+v[:1]) if cross(sub(a,b),sub(d,a)).sign()!=0]
sym=[]
for shift in range(len(corners)):
 for direction in (1,-1):
  image=[corners[(shift+direction*k)%len(corners)] for k in range(len(corners))]
  if all(norm(sub(a,b))==norm(sub(image[i],image[j])) for i,a in enumerate(corners) for j,b in enumerate(corners)):
   sym.append((shift,direction))
assert sym==[(0,1)] # nonstraight corner set has trivial isometry group
def dseg(p,a,b):
 d=sub(b,a);w=sub(p,a);t=dot(w,d)/norm(d)
 if t.sign()<0:t=z
 if (t-1).sign()>0:t=Q(1)
 return norm(sub(w,tuple(t*x for x in d)))
assert all((Q(F(25,4))-norm(sub(x,c))).sign()>0 for x in v) # rho=5/2
assert all(dseg(c,a,b).sign()>0 for a,b in zip(v,v[1:]+v[:1]))
assert all((dseg(c,a,b)-F(1,16)).sign()>0 for a,b in zip(v,v[1:]+v[:1]))
rules={
'Gamma':['Pi','Delta',None,'Theta','Sigma','Xi','Phi','Gamma'],
'Delta':['Xi','Delta','Xi','Phi','Sigma','Pi','Phi','Gamma'],
'Theta':['Psi','Delta','Pi','Phi','Sigma','Pi','Phi','Gamma'],
'Lambda':['Psi','Delta','Xi','Phi','Sigma','Pi','Phi','Gamma'],
'Xi':['Psi','Delta','Pi','Phi','Sigma','Psi','Phi','Gamma'],
'Pi':['Psi','Delta','Xi','Phi','Sigma','Psi','Phi','Gamma'],
'Sigma':['Xi','Delta','Xi','Phi','Sigma','Pi','Lambda','Gamma'],
'Phi':['Psi','Delta','Psi','Phi','Sigma','Pi','Phi','Gamma'],
'Psi':['Psi','Delta','Psi','Phi','Sigma','Psi','Phi','Gamma']}
rot30=[r/2,-Q(F(1,2)),z,Q(F(1,2)),r/2,z]
sys={lab:([I], [v[k] for k in (3,5,7,11)]) for lab in rules}
sys['Gamma']=([I,h.mul(h.ttrans(*v[8]),rot30)],sys['Gamma'][1])
for _ in range(3):
 quad=sys['Delta'][1];ts=[I];ang=0
 for a,fr,to in [(60,3,1),(0,2,0),(60,3,1),(60,3,1),(0,2,0),(60,3,1),(-120,3,3)]:
  ang+=a;rot=h.trot_k60(ang//60)
  t=h.psub(h.transPt(ts[-1],quad[fr]),h.transPt(rot,quad[to]))
  ts.append(h.mul(h.ttrans(*t),rot))
 ts=[h.mul([-Q(1),z,z,z,Q(1),z],t) for t in ts]
 nq=[h.transPt(ts[i],quad[j]) for i,j in [(6,2),(5,1),(3,2),(0,1)]]
 sys={lab:([h.mul(ts[i],g) for i,s in enumerate(rr) if s for g in sys[s][0]],nq) for lab,rr in rules.items()}
frames=sys['Delta'][0];polys=[[h.transPt(t,x) for x in v] for t in frames]
sites=[h.transPt(t,c) for t in frames]
assert len(set(sites))==len(sites)
edges={}
for poly in polys:
 for a,b in zip(poly,poly[1:]+poly[:1]):
  key=frozenset((a,b));edges.setdefault(key,[]).append((a,b))
assert all(len(es)<=2 for es in edges.values())
assert all(es[0]==tuple(reversed(es[1])) for es in edges.values() if len(es)==2)
boundary=[es[0] for es in edges.values() if len(es)==1]
xy=np.array([[float(x) for x in p] for p in sites]);vor=Voronoi(xy)
witness=[];counts=set()
for i,p in enumerate(sites):
 rr=vor.regions[vor.point_region[i]]
 if -1 in rr or not rr:continue
 n=len(rr)
 if n in counts:continue
 # Exact margin test; outside source sites cannot reach the 2R=8 disk.
 if not all((dseg(p,a,b)-13**2).sign()>0 for a,b in boundary):continue
 near=[j for j,q in enumerate(sites) if j!=i and (norm(sub(q,p))-64).sign()<=0]
 vv=vor.vertices[rr]
 if sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(vv,np.roll(vv,-1,axis=0)))<0:vv=vv[::-1]
 order=[]
 for a,b in zip(vv,np.roll(vv,-1,axis=0)):
  m=(a+b)/2
  order.append(min(near,key=lambda j:abs(np.dot(m-xy[i],m-xy[i])-np.dot(m-xy[j],m-xy[j]))))
 assert len(set(order))==n
 hs={j:(tuple(2*x for x in sub(sites[j],p)),norm(sub(sites[j],p))) for j in near}
 verts=[]
 for j,k in zip(order[-1:]+order[:-1],order):
  (a,b),C=hs[j];(d,e),G=hs[k];det=a*e-b*d
  assert det.sign()!=0
  x=((C*e-b*G)/det,(a*G-C*d)/det)
  assert (16-norm(x)).sign()>0
  assert all((N-dot(L,x)).sign()>0 for t,(L,N) in hs.items() if t not in (j,k))
  verts.append(x)
 assert all(cross(sub(b,a),sub(d,b)).sign()>0 for a,b,d in zip(verts,verts[1:]+verts[:1],verts[2:]+verts[:2]))
 counts.add(n);witness.append({'index':i,'sides':n,'neighbors':order,'vertices':verts})
 if len(counts)>=3:break
def enc(x):
 if isinstance(x,Q):return [str(x.a),str(x.b)]
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(y) for y in x]
 return x
result={'source':'author spectre.js recurrence reconstructed in Q(sqrt(3))','levels':3,'label':'Delta','tiles':len(frames),'site':c,'rho':'5/2','R':4,'margin':13,'boundary_edges':len(boundary),'witnesses':witness,'status':'three side counts' if len(counts)>=3 else 'incomplete gate'}
out=P.parent/'certificates/spectre-voronoi-first-gate-2026-10-19.json'
out.write_text(json.dumps(enc(result),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('site','witnesses')}));print([(w['index'],w['sides']) for w in witness])
