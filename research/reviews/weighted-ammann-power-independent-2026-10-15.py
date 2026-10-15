"""Independent exact power-cell audit. Only existing reviewed source generator imported."""
from collections import Counter
from functools import cmp_to_key
from itertools import combinations, product
from pathlib import Path
import importlib.util,json
from sage.all import AA,QQ,QQbar,vector,matrix
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reviewed_source',ROOT/'searches/ammann-two-class-reconstruct.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
K,w=rec.K,rec.w
cert=json.loads((ROOT/'certificates/weighted-ammann-power-gate-2026-10-15.json').read_text())
emb=K.hom([QQbar.zeta(10)])
def xy(z):return vector(AA,[emb(z).real(),emb(z).imag()])
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def norm(u):return u.dot_product(u)
def decode(co):return sum((QQ(c)*w**i for i,c in enumerate(co)),K(0))
def strict(p):return all(cross(p[i]-p[i-1],p[(i+1)%len(p)]-p[i])>0 for i in range(len(p)))
J=K(QQ(1)/2)+QQ(4)/5*w
jp=1+w**4*(J-1);jpp=w+w**6*(J-w)
kr=w**2+w**6*(J-1);lr=1+w**7*(J-1-w)
ref={'H6':[K(0),jp,K(1),J,w,jpp],'P1':[K(0),jp,K(1),lr,kr],'P2':[kr,lr,1+w**2,1+w+w**2-J,w**2]}
refxy={name:list(map(xy,p)) for name,p in ref.items()}
assert all(strict(p) for p in refxy.values())
means={name:sum(p,vector(AA,[0,0]))/len(p) for name,p in refxy.items()}
rho2=min(cross(p[(i+1)%len(p)]-p[i],means[name]-p[i])**2/norm(p[(i+1)%len(p)]-p[i]) for name,p in refxy.items() for i in range(len(p)))
R2=max(norm(v-means[name]) for name,p in refxy.items() for v in p)
assert rho2>0 and R2>0
C=(R2+rho2).sqrt();L=C+(C*C+rho2).sqrt();box=rho2/2
assert L+2*R2.sqrt()<3
print('exact independent rho2,R2,L',float(rho2),float(R2),float(L),flush=True)
tris=rec.sun()
for _ in range(5):tris=rec.subdivide(tris)
rh=rec.rhombs(tris);scale=rec.phi**5
edges=Counter(frozenset((p[i]*scale,p[(i+1)%4]*scale)) for col,p,b,c in rh for i in range(4))
bnd=[tuple(e) for e,n in edges.items() if n==1]
assert set(map(frozenset,bnd))=={frozenset(map(decode,edge)) for edge in cert['boundary_segments']}
segments=[(a*scale,b*scale) for r in rh for a,b in rec.place(r,'B','B',QQ(1)/2,QQ(4)/5)[3]]
# Exact polar sorting and face tracing: no floating angle order or producer geometry.
adj={}
for tag,es in [('dec',segments),('bnd',bnd)]:
 for a,b in es:adj.setdefault(a,{})[b]=tag;adj.setdefault(b,{})[a]=tag

def angular(a,b):
 u,v=xy(a),xy(b)
 h=lambda z:0 if z[1]>0 or z[1]==0 and z[0]>0 else 1
 if h(u)!=h(v):return -1 if h(u)<h(v) else 1
 c=cross(u,v)
 return -1 if c>0 else 1 if c<0 else 0
rotation={a:sorted(adj[a],key=cmp_to_key(lambda b,c:angular(b-a,c-a))) for a in adj}
seen=set();allfaces=[]
for a in adj:
 for b in adj[a]:
  if (a,b) in seen:continue
  start=(a,b);face=[]
  while (a,b) not in seen:
   seen.add((a,b));face.append((a,b));r=rotation[b];a,b=b,r[(r.index(a)-1)%len(r)]
  assert (a,b)==start;allfaces.append(face)
area=lambda p:sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))
def areaK(p):return sum(((p[i].conjugate()*p[(i+1)%len(p)]-p[i]*p[(i+1)%len(p)].conjugate())/(w-w.conjugate()) for i in range(len(p))),K(0))
assert sum((areaK([a for a,b in f]) for f in allfaces if AA(emb(areaK([a for a,b in f])))>0),K(0))==sum((areaK([z*scale for z in p]) for col,p,b,c in rh),K(0))
polys=[];sites=[]
for face in allfaces:
 p=[a for a,b in face];pp=list(map(xy,p))
 if any(adj[a][b]=='bnd' for a,b in face) or area(pp)<=0:continue
 assert strict(pp)
 def congruent(q):
  if len(q)!=len(pp):return False
  n=len(pp)
  return any(all(norm(pp[i]-pp[j])==norm(q[(shift+d*i)%n]-q[(shift+d*j)%n]) for i in range(n) for j in range(n)) for shift in range(n) for d in (-1,1))
 typ,=[name for name,q in refxy.items() if congruent(q)]
 polys.append(p);sites.append((sum(p,K(0))/len(p),typ))
assert polys==[[decode(co) for co in p] for p in cert['source_polygons']]
assert sites==[(decode(s['point']),s['type']) for s in cert['source_sites']]
assert len(sites)==650
print('PASS independently traced650 source faces,exact area,strict convexity,full distance-matrix congruence and mean sites',flush=True)

def clip(poly,n,b):
 out=[]
 for u,v in zip(poly,poly[1:]+poly[:1]):
  fu=n.dot_product(u)-b;fv=n.dot_product(v)-b
  if fu<=0:out.append(u)
  if (fu<0<fv) or (fv<0<fu):out.append(u+(v-u)*fu/(fu-fv))
 # Remove duplicate adjacent points and genuine collinear subdivisions.
 result=[]
 for v in out:
  if not result or v!=result[-1]:result.append(v)
 if len(result)>1 and result[0]==result[-1]:result.pop()
 while len(result)>2:
  redundant=[i for i in range(len(result)) if cross(result[i]-result[i-1],result[(i+1)%len(result)]-result[i])==0]
  if not redundant:break
  result.pop(redundant[0])
 return result

def sd2(z,a,b):
 e=b-a;t=max(AA(0),min(AA(1),(z-a).dot_product(e)/norm(e)))
 return norm(z-a-t*e)
for witness in cert['witnesses']:
 i=witness['site'];z,typ=sites[i];zxy=xy(z)
 assert decode(witness['site_K'])==z and witness['source_type']==typ
 margin=min(sd2(zxy,xy(a),xy(b)) for a,b in bnd)
 assert margin>(L+2*R2.sqrt())**2
 neighbors=[j for j,(p,k) in enumerate(sites) if j!=i and norm(xy(p-z))<=L*L]
 assert neighbors==witness['neighbor_indices']
 def constraints(a,b,all_sites=False):
  weights={'H6':AA(0),'P1':a,'P2':b}
  return [(j,2*xy(sites[j][0]-z),norm(xy(sites[j][0]-z))+weights[typ]-weights[sites[j][1]]) for j in (range(len(sites)) if all_sites else neighbors) if j!=i]
 def polygon(cs):
  p=[vector(AA,[sx*2*C,sy*2*C]) for sx,sy in [(-1,-1),(1,-1),(1,1),(-1,1)]]
  for j,n,b in cs:p=clip(p,n,b)
  assert len(p)>=3 and strict(p)
  assert all(norm(v)<=C*C for v in p)
  return p
 cs0=constraints(AA(0),AA(0));p0=polygon(cs0)
 assert len(p0)==witness['corners']
 # Choose each vertex's first independent active-line pair without consulting certificate pairs.
 pairs=[]
 for v in p0:
  active=[j for j,n,b in cs0 if n.dot_product(v)==b]
  pair=next((j,k) for j,k in combinations(active,2) if cross(dict((jj,n) for jj,n,b in cs0)[j],dict((jj,n) for jj,n,b in cs0)[k])!=0)
  pairs.append(pair)
 persistent=[]
 for a,b in product((-box,box),repeat=2):
  cs=constraints(a,b);D={j:(n,h) for j,n,h in cs};vv=[]
  for j,k in pairs:
   n,h=D[j];m,e=D[k];v=matrix(AA,[n,m]).solve_right(vector(AA,[h,e]));vv.append(v)
   assert norm(v)<=C*C
   assert all(nn.dot_product(v)<=hh for jj,nn,hh in constraints(a,b,True))
  exactpoly=polygon(cs)
  assert len(exactpoly)==len(vv) and {tuple(v) for v in exactpoly}=={tuple(v) for v in vv}
  for k in range(len(vv)):
   edge=vv[(k+1)%len(vv)]-vv[k];old=p0[(k+1)%len(vv)]-p0[k]
   assert cross(edge,old)==0 and edge.dot_product(old)>0
  assert strict(vv)
 # Four-corner feasibility extends affinely over entirebox. Fixed edge
 # directions and positive affine projections retain all genuine corners.
 print('PASS cell',i,typ,len(p0),'genuine corners over CLOSED box;all650site constraints,fixed positive edges,C-disk and boundary margin',flush=True)
assert sorted(x['corners'] for x in cert['witnesses'])==[5,6,7]
print('PASS weighted power geometry:atleast3congruence classes throughout specified box.',flush=True)
# Independently verify the retained positive occurrence certificate; no search
# failure, centered-sun nesting, or author embedding module is used.
E=json.loads((ROOT/'certificates/weighted-ammann-power-source-embedding-2026-10-15.json').read_text())
assert E['single_seed']==0 and E['deflations']==9
centers=[decode(x['site_K']) for x in cert['witnesses']]
def data(r,sc):
 col,cyc,b,c=r
 placed=rec.place(r,'B','B',QQ(1)/2,QQ(4)/5)
 name,p,points,segments=placed
 return name,p[0]*sc,(p[1]-p[0])*sc,[z*sc for z in p]
small=[]
for r in rh:
 name,o,u,p=data(r,scale)
 assert all(norm(xy(a-b))<4 for a in p for b in p)
 if any(norm(xy(v-c))<=25 for v in p for c in centers):small.append((name,o,u))
assert len(small)==137
assert small==[(name,decode(o),decode(u)) for name,o,u in E['selected_rhombs']]
bigtris=[rec.sun()[0]]
for _ in range(9):bigtris=rec.subdivide(bigtris)
big={data(r,rec.phi**9)[:3] for r in rec.rhombs(bigtris)}
rot=w**E['rotation_exponent'];delta=decode(E['translation_K'])
assert all((name,delta+rot*o,rot*u) in big for name,o,u in small)
# Original patch boundary is outside each radius3 disk. Every original
# rhomb meeting that disk has diameter<2 and therefore some vertex within5;
# it is among the137 selected and its complete decoration frame is matched.
assert all(min(sd2(xy(c),xy(a),xy(b)) for a,b in bnd)>9 for c in centers)
print('PASS positive source occurrence:all137 decorated rhomb frames embed exactly in one ninth Robinson supertile;radius3 coronas complete.',flush=True)

red=rec.sun()[0]
children=rec.subdivide([red]);blue=next(t for t in children if t[0]==1)
assert Counter(t[0] for t in children)=={0:1,1:1}
assert Counter(t[0] for t in rec.subdivide([blue]))=={0:1,1:2}
print('PASS hierarchy occurrence bridge:both parentcolors have red child;level10 parent yields redlevel9 supertile inEVERY legal source.',flush=True)
