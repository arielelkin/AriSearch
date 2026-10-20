"""Exact one-P seam-neighborhood gate for the two branching P5/Q8 metrics.

Replay: mise exec -- conda run --no-capture-output -n arisearch sage research/searches/branching-p5q8-seam-transitions-2026-10-20.sage
"""
from sage.all import *
from itertools import product

PANG=(100,110,100,120,110)
QANG=(150,130,140,130,140,120,140,130)
Z=QQbar.zeta(36)
def cs(deg):
 w=Z**(deg//10); return vector(AA,(w.real(),w.imag()))
def directions(angles):
 d=0; out=[]
 for i in range(len(angles)):
  out.append(cs(d)); d+=180-angles[(i+1)%len(angles)]
 return out
PD,QD=directions(PANG),directions(QANG)
def lin_solve(cols,known,pair):
 rhs=-sum((known[i]*cols[i] for i in known),vector(AA,(0,0)))
 a,b=cols[pair[0]],cols[pair[1]]; det=a[0]*b[1]-a[1]*b[0]
 return ((rhs[0]*b[1]-rhs[1]*b[0])/det,(a[0]*rhs[1]-a[1]*rhs[0])/det)
def make_p(t):
 v={0:AA(t),3:AA(t),4:AA(1)}; v[1],v[2]=lin_solve(PD,v,(1,2));return [v[i] for i in range(5)]
def make_q(p,k,rev,freevals):
 v={0:AA(1),7:AA(1)}
 for j,x in {((k-1)%8):(p[2] if rev else p[1]),k:(p[1] if rev else p[2])}.items():
  assert j not in v or v[j]==x
  v[j]=x
 free=[i for i in range(8) if i not in v and i not in (4,5)]
 for i,x in zip(free,freevals):v[i]=AA(x)
 v[4],v[5]=lin_solve(QD,v,(4,5));return [v[i] for i in range(8)]
def vertices(lengths,dirs):
 v=[vector(AA,(0,0))]
 for l,d in zip(lengths,dirs):v.append(v[-1]+l*d)
 assert v[-1]==v[0];return v[:-1]
def reflected(v):return [vector(AA,(x[0],-x[1])) for x in v]
def place_on_edge(poly,idx,dst,dstnext):
 u,w=poly[idx],poly[(idx+1)%len(poly)];su=w-u;du=dstnext-dst
 if su.dot_product(su)!=du.dot_product(du):return None
 cr=su[0]*du[1]-su[1]*du[0];dot=su.dot_product(du);norm=su.dot_product(su)
 rot=matrix(AA,2,2,[dot,-cr,cr,dot])/norm
 return [dst+rot*(x-u) for x in poly]
def overlap_int(a,b):
 for poly in (a,b):
  for i in range(len(poly)):
   e=poly[(i+1)%len(poly)]-poly[i];axis=vector(AA,(-e[1],e[0]))
   aa=[axis.dot_product(x) for x in a];bb=[axis.dot_product(x) for x in b]
   if max(aa)<=min(bb) or max(bb)<=min(aa):return False
 return True
def corner_options(qv,angle,V,rays):
 """All Q images with selected corner at V and adjacent vertices on rays."""
 out=[]
 for j,a in enumerate(QANG):
  if a!=angle:continue
  for flip in (False,True):
   source=reflected(qv) if flip else qv
   for side_order in (0,1):
    r0,r1=rays if side_order==0 else rays[::-1]
    # Side j leads from corner j to j+1.
    cand=place_on_edge(source,j,V,r0)
    if cand is None or cand[(j-1)%8]!=r1:continue
    if cand not in out:out.append(cand)
 return out
def third_at_endpoint(pv,qv,base,a,neighbor,b,flip,end):
 ca=(a+end)%5
 cb=(b+end)%5 if flip else (b+1-end)%5
 V=base[ca]
 assert V==neighbor[cb]
 ra=base[(ca-1)%5] if end==0 else base[(ca+1)%5]
 rb=neighbor[(cb-1)%5] if cb==b else neighbor[(cb+1)%5]
 need=360-PANG[ca]-PANG[cb]
 return [x for x in corner_options(qv,need,V,(ra,rb)) if not overlap_int(x,base) and not overlap_int(x,neighbor)]

for k,rev,free in ((1,False,(QQ(1)/5,)*3),(7,True,(QQ(1)/5,QQ(1)/5,QQ(3)/2))):
 j=1
 p0,p1=make_p(0),make_p(1)
 t=(AA(1)-p0[j])/(p1[j]-p0[j]);p=make_p(t);q=make_q(p,k,rev,free)
 assert all(x>0 for x in p+q)
 pv,qv=vertices(p,PD),vertices(q,QD)
 assert all(x!=t for x in q)
 print('METRIC',k,rev,'t',t,'P',list(map(str,p)),'Q',list(map(str,q)),flush=True)
 for (b0,f0),(b3,f3) in product(product((0,3),(False,True)),repeat=2):
  n0=place_on_edge(reflected(pv) if f0 else pv,b0,*( (pv[0],pv[1]) if f0 else (pv[1],pv[0]) ))
  n3=place_on_edge(reflected(pv) if f3 else pv,b3,*( (pv[3],pv[4]) if f3 else (pv[4],pv[3]) ))
  assert n0 is not None and n3 is not None
  p_ok=not overlap_int(n0,n3)
  opts=[]
  for a,b,f,n in ((0,b0,f0,n0),(3,b3,f3,n3)):
   opts.extend([third_at_endpoint(pv,qv,pv,a,n,b,f,e) for e in (0,1)])
  print('NEIGHBORS',b0,f0,b3,f3,'P_nonoverlap',p_ok,'Q_options',list(map(len,opts)),flush=True)
  if f0 or f3:
   assert 0 in list(map(len,opts))
   continue
  if not p_ok or not all(opts):continue
  P=[pv,n0,n3]
  forced_conflicts=[]
  for i in range(4):
   for h in range(i+1,4):
    if all(x!=y and overlap_int(x,y) for x in opts[i] for y in opts[h]):
     forced_conflicts.append((i,h))
  print('FORCED_Q_CONFLICT_PAIRS',b0,b3,forced_conflicts,flush=True)
  assert (1,2) in forced_conflicts
  valid=[]
  for choices in product(*[range(len(o)) for o in opts]):
   Q=[opts[i][choices[i]] for i in range(4)]
   if any(overlap_int(x,y) for x in Q for y in P):continue
   if any(Q[i]!=Q[h] and overlap_int(Q[i],Q[h]) for i in range(4) for h in range(i+1,4)):continue
   valid.append(choices)
  print('COMPLETE_ONE_P_STARS',b0,f0,b3,f3,len(valid),'sample',valid[:1],flush=True)
  assert not valid
