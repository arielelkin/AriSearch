#!/usr/bin/env python3
"""Independent boundary-cancellation replay; no convex-hull producer import."""
import json,sys,itertools
from pathlib import Path
c=json.loads(Path(sys.argv[1]).read_text());ts=[[tuple(v) for v in t] for t in c['atoms']]
# Independently bind the atoms to the reviewed eight-kite source certificate.
from fractions import Fraction
src=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())
ks=[]
for kite in src['kites']:
 k=[]
 for p in kite:
  assert Fraction(p[0][1])==Fraction(p[1][0])==0
  x,y=2*Fraction(p[0][0]),2*Fraction(p[1][1])
  assert x.denominator==y.denominator==1
  k.append((int(x),int(y)))
 ks.append(k)
assert ts==[t for k in ks for t in ([k[0],k[1],k[2]],[k[0],k[2],k[3]])]
def turn(a,b,d):return (b[0]-a[0])*(d[1]-b[1])-(b[1]-a[1])*(d[0]-b[0])
def boundary(mask):
 edges=set()
 for i,t in enumerate(ts):
  if not mask>>i&1:continue
  for a,b in zip(t,t[1:]+t[:1]):
   if (b,a) in edges:edges.remove((b,a))
   else:edges.add((a,b))
 nxt={}
 for a,b in edges:
  if a in nxt:return None
  nxt[a]=b
 if not nxt:return None
 start=min(nxt);p=[start];v=nxt[start]
 while v!=start:
  if v in p or v not in nxt:return None
  p.append(v);v=nxt[v]
 if len(p)!=len(edges):return None
 corners=[]
 for i,b in enumerate(p):
  z=turn(p[i-1],b,p[(i+1)%len(p)])
  if z<0:return None
  if z>0:corners.append(b)
 return corners
polys={}
for mask in range(1,65536):
 p=boundary(mask)
 if p and len(p) in (5,6):polys[mask]=p
assert set(polys)=={e['mask'] for e in c['eligible']}
for e in c['eligible']:assert set(polys[e['mask']])=={tuple(p) for p in e['polygon']}
def dist(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2
def eq(p,q):
 if len(p)!=len(q):return False
 n=len(p)
 return any(all(dist(p[i],p[j])==dist(q[(s+e*i)%n],q[(s+e*j)%n]) for i,j in itertools.combinations(range(n),2)) for s in range(n) for e in (-1,1))
reps=[];cl={}
for m,p in polys.items():
 found=next((i for i,q in enumerate(reps) if eq(p,q)),None)
 if found is None:found=len(reps);reps.append(p)
 cl[m]=found
for a,b in itertools.combinations(c['eligible'],2):assert (a['shape_class']==b['shape_class'])==(cl[a['mask']]==cl[b['mask']])
# Enumerate each exact cover in increasing least-uncovered-atom order.
stack=[(65535,(),frozenset())];found=set()
while stack:
 rem,chosen,used=stack.pop()
 if not rem:
  if len(used)==2 and any(any((m>>(2*i))&3 in (1,2) for i in range(8)) for m in chosen):found.add(chosen)
  continue
 first=rem&-rem
 for m in polys:
  u=used|{cl[m]}
  if m&first and m&rem==m and len(u)<=2:stack.append((rem^m,chosen+(m,),u))
assert found=={tuple(x['masks']) for x in c['two_class_changed_covers']}
print('VALID: independent directed-boundary enumeration of 65535 subsets;',len(polys),'eligible;',len(reps),'classes;',len(found),'two-class changed covers')
