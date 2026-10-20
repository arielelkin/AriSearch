"""Fixed 125-site exact Sage Voronoi gate; no sampling or enlargement."""
import importlib.util,json
from pathlib import Path
from sage.all import QuadraticField,QQ
spec=importlib.util.spec_from_file_location('source',Path(__file__).with_name('pinwheel-barycentric-crossboundary-2026-10-19.py'))
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
K=QuadraticField(5,'r',embedding=QQ(5).sqrt());r=K.gen()
def vec(v):return tuple(K(x) for x in v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def enc(v):return [str(x) for x in v]
base=[vec(v) for v in g.base];ts=[g.base]
for _ in range(3):ts=[c for t in ts for c in g.subdivide(t)]
# In frame O,L,S: inradius rho=(3-sqrt5)*shortleg/2;
# coefficients along L-O and S-O are rho/(2 shortleg),rho/shortleg.
pcoef=(3-r)/4;qcoef=(3-r)/2
sites=[]
for t in ts:
 o,l,s=map(vec,g.ordered(t));sites.append(add(o,add(tuple(pcoef*x for x in sub(l,o)),tuple(qcoef*x for x in sub(s,o)))))
assert len(set(sites))==125

def clip(poly,a,b):
 out=[]
 for u,v in zip(poly,poly[1:]+poly[:1]):
  fu=b-dot(a,u);fv=b-dot(a,v)
  if fu>=0:out.append(u)
  if (fu>0 and fv<0) or (fu<0 and fv>0):
   z=fu/(fu-fv);out.append(add(u,tuple(z*x for x in sub(v,u))))
 clean=[]
 for x in out:
  if not clean or clean[-1]!=x:clean.append(x)
 if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
 return clean

def canonical(poly):
 vals=[]
 for seq in (poly,list(reversed(poly))):
  for j in range(len(seq)):
   q=seq[j:]+seq[:j]
   vals.append(tuple(dot(sub(a,b),sub(a,b)) for i,a in enumerate(q) for b in q[:i]))
 return min(vals)
records=[];classes={};boundary=[]
for i,p in enumerate(sites):
 poly=base[:]
 for j,q in enumerate(sites):
  if i!=j:poly=clip(poly,tuple(2*x for x in sub(q,p)),dot(q,q)-dot(p,p))
 assert len(poly)>=3
 # Remove all redundant collinear vertices, then verify strict turns.
 changed=True
 while changed:
  changed=False
  for k in range(len(poly)):
   if cross(sub(poly[k],poly[k-1]),sub(poly[(k+1)%len(poly)],poly[k]))==0:
    poly.pop(k);changed=True;break
 assert all(cross(sub(poly[k],poly[k-1]),sub(poly[(k+1)%len(poly)],poly[k]))>0 for k in range(len(poly)))
 touches=any(cross(sub(b,a),sub(v,a))==0 for v in poly for a,b in zip(base,base[1:]+base[:1]))
 if touches:boundary.append(i);continue
 key=canonical(poly)
 if key not in classes:classes[key]=len(classes)
 # Strict vertexwise radius clearance proves immunity to every added site outside T.
 robust=all(cross(sub(b,a),sub(v,a))**2>dot(sub(b,a),sub(b,a))*dot(sub(v,p),sub(v,p)) for v in poly for a,b in zip(base,base[1:]+base[:1]))
 records.append(dict(site_index=i,site=enc(p),triangle=[enc(vec(v)) for v in ts[i]],vertices=[enc(v) for v in poly],sides=len(poly),congruence_class=classes[key],outside_clearance=robust))
 print('cell',i,'sides',len(poly),'class',classes[key],'clear',robust,flush=True)
summary=dict(source_triangles=len(ts),finite_interior_cells=len(records),boundary_cells=len(boundary),classes=len(classes),side_histogram={str(n):sum(c['sides']==n for c in records) for n in sorted(set(c['sides'] for c in records))},robust_cells=sum(c['outside_clearance'] for c in records),robust_classes=len(set(c['congruence_class'] for c in records if c['outside_clearance'])))
out=dict(summary=summary,field='Q(r), r^2=5, r>0',site_coefficients=[str(pcoef),str(qcoef)],classes=[dict(id=cid,signature=[str(x) for x in key]) for key,cid in classes.items()],cells=records,boundary_site_indices=boundary)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary),flush=True)
