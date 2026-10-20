"""Independent exact replay of precisely the retained one-B collar domain."""
from sage.all import QuadraticField, vector, floor, ceil
from pathlib import Path
from itertools import product
import json
R=Path(__file__).resolve().parents[1]; K=QuadraticField(3,'r'); r=K.gen()
def read(s): return json.loads((R/'certificates'/('hexagon-five-four-'+s+'-2026-10-19.json')).read_text())
metrics=read('39-omissions'); corona=read('five-residual-coronas'); boundary=read('strip-boundary-completion'); cert=read('one-b-collar')
def pt(x):return vector(K,[K(z) for z in x])
def sig(p):return tuple(sorted(tuple(x) for x in p))
def J(x):return vector(K,[-x[1],x[0]])
def area(p):return sum(p[i][0]*p[(i+1)%6][1]-p[i][1]*p[(i+1)%6][0] for i in range(6))
def intersect(p,q):
 for poly in (p,q):
  for i in range(6):
   n=J(poly[(i+1)%6]-poly[i]); a=[x*n for x in p];b=[x*n for x in q]
   if max(a)<=min(b) or max(b)<=min(a):return False
 return True
assert cert['completed_all_rows']
for co,bd,ce in zip(corona['rows'],boundary['rows'],cert['rows']):
 idx=co['row_index'];assert idx==bd['row_index']==ce['row_index']
 v=pt(bd['period']);N=v*v
 def canon(p):
  k=floor(min(x*v for x in p)/N);return [x-k*v for x in p]
 def conflict(p,q):
  # Deliberately wider CLOSED interval, then exact SAT.
  lo=floor((min(x*v for x in p)-max(x*v for x in q))/N)
  hi=ceil((max(x*v for x in p)-min(x*v for x in q))/N)
  return any(sig(p)!=sig(qq) and intersect(p,qq) for n in range(int(lo),int(hi)+1) for qq in [[x+n*v for x in q]])
 patch=list({sig(canon([pt(x) for x in p])):canon([pt(x) for x in p]) for p in co['results'][6]['patch']}.values());assert len(patch)==6
 B=[vector(K,[K(z[0])+K(z[1])*r for z in x]) for x in metrics['rows'][idx]['vertices'][1]]
 choices=[]; cases=[]
 for chain in bd['chains']:
  vv=[pt(x) for x in chain['vertices']]
  for a,b in zip(vv,vv[1:]):
   d=b-a;found={};allfound=set()
   for s in range(6):
    u=B[(s+1)%6]-B[s]
    if u*u!=d*d:continue
    for reverse in (False,True):
     aa,bb=(b,a) if reverse else (a,b);w=bb-aa
     for det in (1,-1):
      p=[aa+((x-B[s])*u)/(u*u)*w+det*((x-B[s])*J(u))/(u*u)*J(w) for x in B]
      # Interior centroid is outside; convexity and edge attachment suffice.
      if J(d)*(sum(p,vector(K,[0,0]))/6-a)>=0:continue
      assert all(J(d)*(x-a)<=0 for x in p)
      p=canon(p);ss=sig(p);valid=not conflict(p,p) and not any(conflict(p,q) for q in patch)
      allfound.add((ss,valid))
      if valid:found[ss]=p
   choices.append(list(found.values()));cases.append(allfound)
 for reconstructed,stored in zip(cases,ce['attachment_cases']):
  assert reconstructed==set((sig([pt(x) for x in z['vertices']]),z['strip_compatible']) for z in stored)
 assert list(map(len,choices))==ce['compatible_counts']
 count=0;legal=0
 for selection in product(*choices):
  count+=1; new=list({sig(p):p for p in selection}.values())
  if not any(conflict(p,q) for i,p in enumerate(new) for q in new[i+1:]):legal+=1
 assert count==ce['assignments_examined'] and legal==0 and ce['valid_collars']==[]
 assert ce['status']=='complete_finite_failure'
 print(idx,'PASS',list(map(len,choices)),count,flush=True)
