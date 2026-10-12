#!/usr/bin/env python3
"""Independent retained-support/refinement verifier; never calls CP-SAT.
No producer imports. Also verifies a future RESIDUAL_FINITE_PATCH certificate.
"""
import argparse,hashlib,itertools,json
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
D=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
LABELS=[(q,r,s) for q in range(2) for s in (1,-1) for r in range(6)]
TRIPLES=tuple(itertools.combinations_with_replacement(range(12),3))
BASE=((1,)*6+(0,)*6+(720,),(0,)*6+(1,)*6+(720,))
def corner(v,k):
 q,r,s=LABELS[v];return 6*q+(r+s*k)%6

def side_from_endpoints(cm,i):
 endpoints={cm[i],cm[(i+1)%6]}
 return next(j for j in range(6) if endpoints=={j,(j+1)%6})
def side(v,k):
 q,r,s=LABELS[v];cm=[(r+s*i)%6 for i in range(6)]
 return 6*q+side_from_endpoints(cm,k)
def groups():
 G=[]
 for ra,sa,rb,sb,swap in itertools.product(range(6),(1,-1),range(6),(1,-1),(0,1)):
  cm=[];sm=[]
  for q,r,s in ((0,ra,sa),(1,rb,sb)):
   local=[(r+s*i)%6 for i in range(6)];cm.extend(6*(q^swap)+i for i in local)
   sm.extend(6*(q^swap)+side_from_endpoints(local,i) for i in range(6))
  assert sorted(cm)==sorted(sm)==list(range(12));G.append((tuple(cm),tuple(sm)))
 assert len(set(G))==288
 return G
G=groups()
def row(t):
 c=[0]*13
 for x in t:c[x]+=1
 c[-1]=360;return tuple(c)
@lru_cache(None)
def basis(U):
 # Incremental echelon dictionary avoids producer's RREF implementation.
 B={}
 for r in BASE+tuple(row(t) for t in U):
  r=list(map(Q,r))
  for p in sorted(B):
   factor=r[p]
   if factor:r=[x-factor*y for x,y in zip(r,B[p])]
  pivot=next((i for i,x in enumerate(r) if x),None)
  if pivot is not None:
   scale=r[pivot];B[pivot]=tuple(x/scale for x in r)
 return tuple(sorted(B.items()))
def implies(U,t):
 r=list(map(Q,row(t)))
 for p,b in basis(tuple(sorted(U))):
  f=r[p]
  if f:r=[x-f*y for x,y in zip(r,b)]
 return not any(r)
def closure(U):return {t for t in TRIPLES if implies(U,t)}
def equality(E):
 graph={i:{i} for i in range(12)}
 for a,b in E:graph[a].add(b);graph[b].add(a)
 components=[];todo=set(range(12))
 while todo:
  start=min(todo);C={start};stack=[start]
  while stack:
   for x in graph[stack.pop()]:
    if x not in C:C.add(x);stack.append(x)
  todo-=C;components.append(C)
 pairs={p for C in components for p in itertools.combinations(sorted(C),2)}
 return pairs,components

def used(lab,lat=None):
 U=set();E=set()
 def neighbour(z,d):
  x,y=z[0]+d[0],z[1]+d[1]
  if lat:
   n,s,m=lat;q=y//m;return ((x-s*q)%n,y-q*m)
  return x,y
 for z,v in lab.items():
  assert 0<=v<24
  for k in (0,1):
   b,c=neighbour(z,D[k]),neighbour(z,D[k+1])
   if b in lab and c in lab:U.add(tuple(sorted((corner(v,k),corner(lab[b],k+2),corner(lab[c],k+4)))))
  for k in range(6):
   b=neighbour(z,D[(k+1)%6])
   if b in lab:
    p,q=side(v,k),side(lab[b],(k+3)%6)
    if p!=q:E.add(tuple(sorted((p,q))))
 return U,E

def sets(record):return {tuple(t) for t in record['U']},{tuple(p) for p in record['E']}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--certificate',default='research/certificates/two-hexagon-inherited-escape-radius3.json');ap.add_argument('--output');args=ap.parse_args()
 cp=Path(args.certificate);cert=json.loads(cp.read_text());grid=cert.get('angle_grid',0);assert type(grid) is int and grid>=0;lp=Path(cert['library']);assert hashlib.sha256(lp.read_bytes()).hexdigest()==cert['library_sha256']
 lib=json.loads(lp.read_text());direct=set();count=0
 for flat in lib['flats']:
  T={tuple(t) for t in flat['T']}
  for record in flat['tori']:
   n,s,m=record['lat'];assert n>0 and m>0
   lab={tuple(map(int,z.split(','))):v for z,v in record['sol'].items()}
   assert set(lab)=={(x,y) for x in range(n) for y in range(m)}
   U,E=used(lab,(n,s,m));assert E=={tuple(p) for p in record['E']}
   assert all(implies(T,t) for t in U)
   F={tuple(p) for p in record['F']};Ec,C=equality(F);assert E<=Ec
   assert all(record['cls'][a]==record['cls'][b] for a,b in E)
   direct.add((tuple(sorted(U)),tuple(sorted(E))));count+=1
 images=set()
 for U,E in direct:
  for cm,sm in G:
   V=tuple(sorted(tuple(sorted(cm[x] for x in t)) for t in U));F=tuple(sorted(tuple(sorted(sm[x] for x in p)) for p in E));images.add((V,F))
 assert count==cert['source_records'] and len(direct)==cert['distinct_direct_supports'] and len(images)==cert['distinct_symmetry_supports']
 for r in cert['refinements']:
  U,E=sets(r);S={tuple(t) for t in r['S']};implied={tuple(t) for t in r['implied']};V={tuple(t) for t in r['escape_U']};F={tuple(p) for p in r['escape_E']}
  assert S<=U and implied and implied<=V and implied.isdisjoint(U)
  assert all(implies(S,t) for t in implied)
  assert all(not all(implies(S-{s},t) for t in implied) for s in S),'Generating support is not inclusion minimal'
  assert (tuple(sorted(V)),tuple(sorted(F))) in images
  Ec,C=equality(E);assert F<=Ec and all(implies(U,t) for t in V)
  assert not any(set(V0)<=U and set(F0)<=Ec for V0,F0 in images),'Physical support already contains blocked torus'
 initial=0
 if 'resumed_from' in cert:
  rp=Path(cert['resumed_from']);previous=json.loads(rp.read_text());assert hashlib.sha256(rp.read_bytes()).hexdigest()==cert['resume_sha256']
  assert previous['library_sha256']==cert['library_sha256'] and previous['radius']==cert['radius']
  initial=len(previous['refinements']);assert cert['refinements'][:initial]==previous['refinements']
 analytic=None;regions=[]
 if 'analytic_empty_region' in cert:
  a=cert['analytic_empty_region'];sp=Path(a['source']);assert hashlib.sha256(sp.read_bytes()).hexdigest()==a['sha256']
  potential=tuple(map(Q,a['potential']));assert len(potential)==12 and all(x.denominator==1 for x in potential)
  assert potential==tuple(map(Q,json.loads(sp.read_text())['empty_potential']))
  assert sum(potential[:6])==sum(potential[6:])==-1 and min(potential)==-2
  region={t for t in TRIPLES if sum(potential[x] for x in t)>=0};assert len(region)==a['size']==195
  images_region=set()
  for cm,sm in G:
   image=frozenset(tuple(sorted(cm[x] for x in t)) for t in region);images_region.add(image)
   d=[None]*12
   for x in range(12):d[cm[x]]=potential[x]
   assert sum(d[:6])==sum(d[6:])==-1 and min(d)==-2
   assert image==frozenset(t for t in TRIPLES if sum(d[x] for x in t)>=0)
  regions=list(images_region)
  # Enumerate the radius-12 ball and complete-star corner incidences from
  # scratch; count each (cell,local corner) at most once.
  R=12;cells={(x,y) for x in range(-R,R+1) for y in range(-R,R+1) if max(abs(x),abs(y),abs(x+y))<=R}
  incidences=set();stars=0
  for z in cells:
   for k in (0,1):
    b,c=(z[0]+D[k][0],z[1]+D[k][1]),(z[0]+D[k+1][0],z[1]+D[k+1][1])
    if b in cells and c in cells:
     star={(z,k),(b,k+2),(c,k+4)};assert len(star)==3 and not star&incidences;incidences|=star;stars+=1
  leftover=6*len(cells)-len(incidences)
  assert (len(cells),stars,leftover)==(469,864,222) and len(cells)>2*leftover
  analytic={'region_size':len(region),'distinct_symmetry_regions':len(images_region),'radius12_cells':len(cells),'complete_stars':stars,'boundary_corner_incidences':leftover,'contradiction':[len(cells),2*leftover]}
 if grid:assert len(cert['refinements'])==initial,'Exact grid flags cannot require new rational-closure refinements'
 status=cert['status'];residual=False
 if status=='ITERATION_LIMIT':assert cert['queries']==cert['iterations_limit']==len(cert['refinements'])-initial
 elif status in ('RESIDUAL_FINITE_PATCH','RESIDUAL_FINITE_PATCH_IN_EMPTY_REGION'):
  R=cert['radius'];lab={tuple(map(int,z.split(','))):v for z,v in cert['patch'].items()}
  assert set(lab)=={(x,y) for x in range(-R,R+1) for y in range(-R,R+1) if max(abs(x),abs(y),abs(x+y))<=R}
  U,E=used(lab);assert (U,E)==sets(cert)
  if grid:
   angles=cert['angle_grid_numerators'];assert len(angles)==12 and all(type(a) is int and 0<a<180*grid for a in angles)
   assert sum(angles[:6])==sum(angles[6:])==720*grid
   T={t for t in TRIPLES if sum(angles[c] for c in t)==360*grid};assert U<=T
   assert closure(T)==T,'Exact grid angle type must be rationally closed'
  else:T=closure(U)
  assert T=={tuple(t) for t in cert['T']};Ec,C=equality(E)
  assert all((cert['classes'][a]==cert['classes'][b])==((a==b) or tuple(sorted((a,b))) in Ec) for a in range(12) for b in range(12))
  assert cert['rank']==len(basis(tuple(sorted(T))))-2
  assert cert['covers']==(len({x for t in T for x in t})==12)
  assert not any(set(V)<=T and set(F)<=Ec for V,F in images)
  empty_memberships=[i for i,(cm,sm) in enumerate(G) if T<=frozenset(tuple(sorted(cm[x] for x in t)) for t in region)] if analytic is not None else []
  if status=='RESIDUAL_FINITE_PATCH_IN_EMPTY_REGION':
   assert empty_memberships,'Diagnostic empty-region residual must belong to an analytic region'
   if 'empty_region_symmetry' in cert:assert cert['empty_region_symmetry'] in empty_memberships
  else:assert not empty_memberships,'Closed residual type is in inherited analytic empty region'
  assert cert['queries']==len(cert['refinements'])-initial+1;residual=True
 else:
  assert status in ('UNSAT','UNKNOWN') # Status alone has no independently checked solver proof.
  assert cert['queries']==len(cert['refinements'])-initial+1
 assert cert['workers']==1 and cert['random_seed']==1,'Expected corrected actual CP-SAT default seed metadata'
 result={'status':'PASSED','certificate_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'source_tori_checked':count,'direct_supports':len(direct),'symmetry_supports':len(images),'symmetries':len(G),'exact_refinements_checked':len(cert['refinements']),'query_status':status,'angle_grid':grid,'initial_refinements':initial,'new_refinements':len(cert['refinements'])-initial,'analytic_empty_region_checked':analytic,'finite_residual_checked':residual,'scope':'Retained torus supports and rational/equality implications only; no CP-SAT replay or plane-tilability claim'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
