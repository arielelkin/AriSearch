#!/usr/bin/env python3
"""One B collar, exact arithmetic, finite domain declared before enumeration."""
from sage.all import QuadraticField,vector,matrix,floor,ceil
from pathlib import Path
from itertools import product
import json,time
K=QuadraticField(3,'r');r=K.gen();root=Path(__file__).resolve().parents[1]
src=json.loads((root/'certificates/hexagon-five-four-39-omissions-2026-10-19.json').read_text())
cor=json.loads((root/'certificates/hexagon-five-four-five-residual-coronas-2026-10-19.json').read_text())
bound=json.loads((root/'certificates/hexagon-five-four-strip-boundary-completion-2026-10-19.json').read_text())
CAP_SECONDS=180;start=time.monotonic()
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def key(p):return tuple(sorted(tuple(x) for x in p))
def ser(p):return [[str(z) for z in x] for x in p]
def overlap(p,q):
 for a,b in ((p,q),(q,p)):
  ori=1 if cross(a[1]-a[0],a[2]-a[1])>0 else -1
  for i in range(6):
   if all(ori*cross(a[(i+1)%6]-a[i],x-a[i])<=0 for x in b):return False
 return True
out=dict(schema='ONE_B_COLLAR_V1',domain='five exact rows; eight exposed orbits; all six B sides, both endpoint assignments and both determinants, exterior only; one layer',raw_assignment_bound_per_row=24**8,wall_cap_seconds=CAP_SECONDS,rows=[])
for ent,be in zip(cor['rows'],bound['rows']):
 idx=ent['row_index'];assert idx==be['row_index']
 def pt(x):return vector(K,[K(z) for z in x])
 B=[vector(K,[K(z[0])+K(z[1])*r for z in x]) for x in src['rows'][idx]['vertices'][1]]
 v=pt(be['period']);norm=v*v
 def canonical(p):return [x-int(floor(min(y*v for y in p)/norm))*v for x in p]
 patch=list({key(canonical(p)):canonical(p) for p in [[pt(x) for x in p] for p in ent['results'][6]['patch']]}.values())
 def conflict(p,q):
  # Exact projection intervals give ALL possibly overlapping period translates.
  lo=int(floor((min(x*v for x in p)-max(x*v for x in q))/norm))+1
  hi=int(ceil((max(x*v for x in p)-min(x*v for x in q))/norm))-1
  for n in range(lo,hi+1):
   qq=[x+n*v for x in q]
   if key(p)!=key(qq) and overlap(p,qq):return True
  return False
 candidates=[];details=[]
 for chain in be['chains']:
  vv=[pt(x) for x in chain['vertices']]
  for i in range(4):
   a,b=vv[i:i+2];target=b-a;choices={};raw=[]
   for s in range(6):
    u=B[(s+1)%6]-B[s]
    if u*u!=target*target:continue
    for reverse in (False,True):
     aa,bb=(b,a) if reverse else (a,b);d=bb-aa
     U=matrix(K,[[u[0],-u[1]],[u[1],u[0]]])
     for det in (1,-1):
      D=matrix(K,[[d[0],-det*d[1]],[d[1],det*d[0]]]);M=D*U.inverse();t=aa-M*B[s]
      p=[M*x+t for x in B]
      if any(cross(target,x-a)>0 for x in p):continue
      p=canonical(p);kk=key(p)
      if kk in choices:continue
      valid=not any(conflict(p,q) for q in patch) and not conflict(p,p)
      raw.append(dict(side=s,reverse=reverse,determinant=det,strip_compatible=valid,vertices=ser(p)))
      if valid:choices[kk]=p
   candidates.append(list(choices.values()));details.append(raw)
 result=dict(row_index=idx,attachment_cases=details,compatible_counts=list(map(len,candidates)),assignments_examined=0,valid_collars=[])
 out['rows'].append(result)
 # A zero candidate orbit proves finite failure without considering any products.
 if any(not x for x in candidates):result['status']='complete_finite_failure';print(idx,result['status'],result['compatible_counts'],flush=True);continue
 for selection in product(*candidates):
  if time.monotonic()-start>CAP_SECONDS:result['status']='wall_cap_incomplete';break
  result['assignments_examined']+=1
  new=list({key(p):p for p in selection}.values())
  if any(conflict(p,q) for i,p in enumerate(new) for q in new[i+1:]):continue
  allp=patch+new;edges={}
  for f,p in enumerate(allp):
   ori=1 if cross(p[1]-p[0],p[2]-p[1])>0 else -1
   for s in range(6):
    a,b=p[s],p[(s+1)%6]
    if ori<0:a,b=b,a
    sh=int(floor(min(a*v,b*v)/norm));ek=tuple(sorted((tuple(a-sh*v),tuple(b-sh*v))))
    edges.setdefault(ek,[]).append((f,s,a,b))
  assert all(len(x)<=2 for x in edges.values())
  residual=[es[0] for es in edges.values() if len(es)==1]
  result['valid_collars'].append(dict(new_tiles=[ser(p) for p in new],residual_edges=[dict(face=f,native_side=s,endpoints=ser([a,b])) for f,s,a,b in residual]))
  # A cylinder with no exposed edges is impossible for finite bounded-width packing.
  assert residual
 else:result['status']='complete_open_collars' if result['valid_collars'] else 'complete_finite_failure'
 print(idx,result['status'],result['compatible_counts'],result['assignments_examined'],len(result['valid_collars']),flush=True)
 if result['status']=='wall_cap_incomplete':break
out['completed_all_rows']=len(out['rows'])==5 and all(x['status']!='wall_cap_incomplete' for x in out['rows'])
(root/'certificates/hexagon-five-four-one-b-collar-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
