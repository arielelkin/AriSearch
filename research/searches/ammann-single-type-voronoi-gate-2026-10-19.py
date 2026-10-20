#!/usr/bin/env python
"""Exact ordinary Voronoi obstruction for three single-source-type mean rules."""
import importlib.util,json,hashlib
from pathlib import Path
from sage.all import *
spec=importlib.util.spec_from_file_location('rec',Path(__file__).with_name('ammann-two-class-reconstruct.py'))
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
K,w=r.K,r.w
def decode(v):return sum((K(QQ(q))*w**i for i,q in enumerate(v)),K(0))
def enc(z):return [str(a) for a in z.vector()]
def norm(z):return r.real_K(z*z.conjugate())
def dot(z,v):return r.real_K((z*v.conjugate()+z.conjugate()*v)/2)
def xy(z):return vector(AA,[r.QQbar_of(z).real(),r.QQbar_of(z).imag()])
def segdist(z,a,b):
 d=b-a;t=max(AA(0),min(AA(1),dot(z-a,d)/norm(d)))
 return norm(z-a)-2*t*dot(z-a,d)+t*t*norm(d)
P=json.loads(Path('research/certificates/weighted-ammann-power-gate-2026-10-15.json').read_text())
S=[(decode(a['point']),a['type']) for a in P['source_sites']]
bnd=[tuple(map(decode,e)) for e in P['boundary_segments']]
ref=r.reference_tiles(QQ(1)/2,QQ(4)/5)
R2=max(norm(z-sum(p,K(0))/len(p)) for p in ref.values() for z in p)
# Independent finite clipping starts in an artificial square, later strictly redundant.
def clip(poly,n,b):
 out=[]
 for a,c in zip(poly,poly[1:]+poly[:1]):
  f=b-n.dot_product(a);g=b-n.dot_product(c)
  if f>=0:out.append(a)
  if (f<0 and g>0) or (f>0 and g<0):out.append((g*a-f*c)/(g-f))
 return out
results=[];cuts=[]
for typ in ['H6','P1','P2']:
 reps=[]
 candidates=sorted([i for i,(c,t) in enumerate(S) if t==typ],key=lambda i:float(norm(S[i][0])))
 for i in candidates:
  c=S[i][0];poly=[vector(AA,q) for q in [(-10,-10),(10,-10),(10,10),(-10,10)]]
  neighbors=[]
  for j,(p,t) in enumerate(S):
   if t!=typ or i==j or norm(p-c)>16:continue
   d=p-c;poly=clip(poly,2*xy(d),norm(d));neighbors.append(j)
  # Remove duplicates and straight points exactly.
  poly=[a for k,a in enumerate(poly) if a!=poly[k-1]]
  while len(poly)>=3:
   bad=next((k for k,a in enumerate(poly) if matrix(AA,[a-poly[k-1],poly[(k+1)%len(poly)]-a]).det()==0),None)
   if bad is None:break
   poly.pop(bad)
  if not poly or any(abs(q)==10 for a in poly for q in a):continue
  assert all(matrix(AA,[a-poly[k-1],poly[(k+1)%len(poly)]-a]).det()>0 for k,a in enumerate(poly))
  B2=max(a.dot_product(a) for a in poly);cut=2*B2.sqrt()
  if cut>=4:continue
  if min(segdist(c,a,b) for a,b in bnd)<=(cut+2*R2.sqrt())**2:continue
  # all omitted finite means and all means outside the source patch are redundant
  assert all(norm(p-c)>cut**2 for j,(p,t) in enumerate(S) if t==typ and j!=i and j not in neighbors)
  # Signature is the cyclic edge Gram matrix, up to dihedral permutation.
  ed=[poly[(k+1)%len(poly)]-a for k,a in enumerate(poly)]
  def congruent(other):
   if len(other)!=len(ed):return False
   for rev in [False,True]:
    ee=list(reversed(other)) if rev else other
    for shift in range(len(ed)):
     if all(ed[a].dot_product(ed[b])==ee[(a+shift)%len(ed)].dot_product(ee[(b+shift)%len(ed)]) for a in range(len(ed)) for b in range(len(ed))):return True
   return False
  if any(congruent(e) for e in reps):continue
  reps.append(ed)
  vertices=[[str(x.minpoly()),str(x.interval(RealIntervalField(200)))] for a in poly for x in a]
  rec={'site_index':i,'site_K':enc(c),'corners':len(poly),'vertices_AA':[list(map(str,a)) for a in poly],'vertices_exact_minpoly_interval':vertices,'neighbors':neighbors,'radius2_approx':float(B2),'cutoff_approx':float(cut)}
  results.append({'type':typ,'witness':rec});cuts.append(cut)
  print(typ,i,len(poly),'classes',len(reps),'cut',float(cut),flush=True)
  if len(poly)<5 or len(reps)>=3:break
 else:raise AssertionError('no obstruction for '+typ)
# Validate every retained corona occurs in ONE red supertile using reviewed delta.
E=json.loads(Path('research/certificates/weighted-ammann-power-source-embedding-2026-10-15.json').read_text())
delta=decode(E['translation_K']);rot=w**E['rotation_exponent']
tris=r.sun()
for _ in range(5):tris=r.subdivide(tris)
small=[]
for rh in r.rhombs(tris):
 k,p,_,_=r.place(rh,'B','B',QQ(1)/2,QQ(4)/5);p=[z*r.phi**5 for z in p]
 # radius cutoff <=4, plus tile diameter <=2R, plus rhomb diameter <2
 if any(min(norm(z-decode(a['witness']['site_K'])) for z in p)<=(exact_cut+2*R2.sqrt()+2+QQ(1)/1000)**2 for a,exact_cut in zip(results,cuts)):small.append((k,p[0],p[1]-p[0]))
tris=[r.sun()[0]]
for _ in range(9):tris=r.subdivide(tris)
lookup=set()
for rh in r.rhombs(tris):
 k,p,_,_=r.place(rh,'B','B',QQ(1)/2,QQ(4)/5);lookup.add((k,p[0]*r.phi**9,(p[1]-p[0])*r.phi**9))
assert all((k,delta+rot*o,rot*u) in lookup for k,o,u in small)
print('PASS embedded rhombs',len(small),flush=True)
out={'scope':'one source type mean sites, ordinary Voronoi; no aperiodicity transfer','source_certificate':str(Path('research/certificates/weighted-ammann-power-gate-2026-10-15.json')),'witnesses':results,'embedded_rhombs':len(small),'embedded_frames':[[k,enc(o),enc(u)] for k,o,u in small],'source_sha256':hashlib.sha256(Path('research/certificates/weighted-ammann-power-gate-2026-10-15.json').read_bytes()).hexdigest(),'density_radius':'2*phi^10: every level-10 Robinson half contains the embedded level-9 red supertile with all three types'}
Path('research/certificates/ammann-single-type-voronoi-gate-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
