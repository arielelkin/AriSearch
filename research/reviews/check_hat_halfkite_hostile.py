#!/usr/bin/env python3
"""Fresh exact audit; global support lines and all 8192 eligible combinations."""
import json,itertools,importlib.util
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
c=json.loads(Path('research/certificates/hat-halfkite-convex-partition-gate.json').read_text())
s=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text())
def decode(p):
 assert F(p[0][1])==F(p[1][0])==0
 return tuple(int(2*F(x)) for x in (p[0][0],p[1][1]))
ks=[[decode(p) for p in k] for k in s['kites']]
ts=[[tuple(p) for p in t] for t in c['atoms']]
assert ts==[t for k in ks for t in ([k[0],k[1],k[2]],[k[0],k[2],k[3]])]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def cr(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+3*a[1]*b[1]
def ar(p):return sum(cr(a,b) for a,b in zip(p,p[1:]+p[:1]))
def boundary(polys):
 vs=set(v for p in polys for v in p);edges=Counter()
 for p in polys:
  for a,b in zip(p,p[1:]+p[:1]):
   v=sub(b,a);on=[q for q in vs if cr(v,sub(q,a))==0 and 0<=dot(sub(q,a),v)<=dot(v,v)]
   on.sort(key=lambda q:dot(sub(q,a),v));edges.update(zip(on,on[1:]))
 es=[e for e,n in edges.items() for _ in range(max(0,n-edges[e[::-1]]))]
 nxt=dict(es)
 if not es or len(nxt)!=len(es):return None
 p=[];v=min(nxt)
 while v not in p:
  p.append(v)
  if v not in nxt:return None
  v=nxt[v]
 if v!=p[0] or len(p)!=len(es):return None
 return [b for a,b,d in zip(p[-1:]+p[:-1],p,p[1:]+p[:1]) if cr(sub(b,a),sub(d,b))]
def clip(p,q):
 p=[tuple(map(F,v)) for v in p]
 for a,b in zip(q,q[1:]+q[:1]):
  out=[]
  for x,y in zip(p,p[1:]+p[:1]):
   fx=cr(sub(b,a),sub(x,a));fy=cr(sub(b,a),sub(y,a))
   if fx>=0:out.append(x)
   if fx*fy<0:
    t=fx/(fx-fy);out.append(tuple(x[i]+t*(y[i]-x[i]) for i in (0,1)))
  p=out
 return p
assert len(set(map(tuple,map(tuple,ts))))==16
assert all(ar(t)==4 for t in ts)
for a,b in itertools.combinations(ts,2):assert ar(clip(a,b))==0
full=boundary(ts);outline=[decode(p) for p in s['hat_outline']]
assert set(full)==set(outline) and ar(full)==ar(outline)==64
# 60/90/120/90 angles: squared cosine 1/4,0,1/4,0 with correct signs.
for k in ks:
 for i in range(4):
  u,v=sub(k[i-1],k[i]),sub(k[(i+1)%4],k[i]);z=dot(u,v)
  assert (z>0 if i==0 else z<0 if i==2 else z==0)
  assert (4*z*z==dot(u,u)*dot(v,v) if i%2==0 else z==0)
assert all(sorted(dot(sub(t[i],t[j]),sub(t[i],t[j])) for i,j in itertools.combinations(range(3),2))==[4,12,16] for t in ts)
# Audit elementary mesh: the simpler retained checker never needs segment splitting.
vs={v for t in ts for v in t}
assert all(not any(q not in (a,b) and cr(sub(b,a),sub(q,a))==0 and 0<dot(sub(q,a),sub(b,a))<dot(sub(b,a),sub(b,a)) for q in vs) for t in ts for a,b in zip(t,t[1:]+t[:1]))
counts=Counter();polys={}
for mask in range(1,1<<16):
 p=boundary([t for i,t in enumerate(ts) if mask>>i&1])
 if p and all(cr(sub(b,a),sub(v,a))>=0 for a,b in zip(p,p[1:]+p[:1]) for v in p):
  counts[len(p)]+=1
  if len(p) in (5,6):polys[mask]=p
assert dict(counts)=={int(k):v for k,v in c['convex_corner_counts'].items()}
assert set(polys)=={e['mask'] for e in c['eligible']} and len(polys)==13
covers=[]
for n in range(1,14):
 for comb in itertools.combinations(polys,n):
  if sum(m.bit_count() for m in comb)!=16:continue
  union=0
  for m in comb:
   if union&m:break
   union|=m
  else:
   if union==65535:covers.append(comb)
def eq(p,q):
 return len(p)==len(q) and any(all(dot(sub(p[i],p[j]),sub(p[i],p[j]))==dot(sub(q[(s+d*i)%len(q)],q[(s+d*j)%len(q)]),sub(q[(s+d*i)%len(q)],q[(s+d*j)%len(q)])) for i,j in itertools.combinations(range(len(p)),2)) for s in range(len(p)) for d in (-1,1))
rows={e['mask']:e for e in c['eligible']}
for a,b in itertools.combinations(polys,2):assert eq(polys[a],polys[b])==(rows[a]['shape_class']==rows[b]['shape_class'])
summary=[]
for comb in covers:
 classes={rows[m]['shape_class'] for m in comb}
 changed=any(any((m>>(2*i))&3 in (1,2) for i in range(8)) for m in comb)
 summary.append(dict(masks=comb,classes=sorted(classes),changed=changed))
assert not any(len(x['classes'])==2 for x in summary)
print(json.dumps(dict(status='VALID',atom_area='sqrt(3)/2',hat_area='8*sqrt(3)',convex_counts=dict(counts),all_eligible_covers=summary),indent=2))
