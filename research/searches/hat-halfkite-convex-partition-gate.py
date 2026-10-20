#!/usr/bin/env python3
"""Complete fixed 16-halfkite gate. Runtime cap: 300 seconds; exact integers."""
import json,sys,time,itertools
from pathlib import Path
from fractions import Fraction as F
start=time.monotonic()
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(ps):
 ps=sorted(set(ps));lo=[];hi=[]
 for seq,out in ((ps,lo),(ps[::-1],hi)):
  for p in seq:
   while len(out)>1 and cross(out[-2],out[-1],p)<=0:out.pop()
   out.append(p)
 return lo[:-1]+hi[:-1]
def area(p):return sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p)))
def d(a,b):return (a[0]-b[0])**2+3*(a[1]-b[1])**2
def canon(p):
 n=len(p)
 return min(tuple(d(p[(s+e*i)%n],p[(s+e*j)%n]) for i in range(n) for j in range(i+1,n)) for s in range(n) for e in (-1,1))
source=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())
def point(p):
 assert F(p[0][1])==F(p[1][0])==0
 a,b=2*F(p[0][0]),2*F(p[1][1]);assert a.denominator==b.denominator==1
 return (int(a),int(b))
kites=[[point(p) for p in k] for k in source['kites']]
atoms=[t for k in kites for t in ([k[0],k[1],k[2]],[k[0],k[2],k[3]])]
assert len(atoms)==16 and len(set(area(t) for t in atoms))==1
unit=area(atoms[0]);eligible=[];counts={};classes={}
for m in range(1,65536):
 if m%1024==0 and time.monotonic()-start>300:raise TimeoutError('300-second cap; incomplete')
 p=hull([v for i,t in enumerate(atoms) if m>>i&1 for v in t])
 if area(p)!=m.bit_count()*unit:continue
 counts[len(p)]=counts.get(len(p),0)+1
 if len(p) not in (5,6):continue
 key=canon(p)
 if key not in classes:classes[key]=len(classes)
 eligible.append(dict(mask=m,polygon=p,shape_class=classes[key],corners=len(p)))
bybit=[[e for e in eligible if e['mask']>>i&1] for i in range(16)]
covers=[];nodes=0
def visit(rem,chosen,used):
 global nodes
 nodes+=1
 if not rem:
  if len(used)==2:
   changed=any(any((e['mask']>>(2*i))&3 in (1,2) for i in range(8)) for e in chosen)
   if changed:covers.append(dict(masks=[e['mask'] for e in chosen],classes=sorted(used)))
  return
 bit=(rem&-rem).bit_length()-1
 for e in bybit[bit]:
  m=e['mask'];u=used|{e['shape_class']}
  if m&rem==m and len(u)<=2:visit(rem^m,chosen+[e],u)
visit(65535,[],set())
out=dict(status='COMPLETE',domain_nonempty_subsets=65535,runtime_cap_seconds=300,coordinate_map='(X,Y) -> (X/2,sqrt(3)*Y/2)',atoms=atoms,convex_corner_counts=counts,eligible=eligible,shape_class_count=len(classes),two_class_changed_covers=covers,cover_nodes=nodes,elapsed_seconds=time.monotonic()-start)
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('atoms','eligible','two_class_changed_covers')});print('covers',len(covers))
