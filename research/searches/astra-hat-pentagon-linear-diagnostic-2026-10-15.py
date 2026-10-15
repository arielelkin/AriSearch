#!/usr/bin/env python3
"""Exploratory exact fixed-frame two-prototype realization gate, not a theorem."""
import importlib.util,itertools,json,sys
from collections import defaultdict,deque
from sage.all import QuadraticField,matrix,vector
spec=importlib.util.spec_from_file_location('hat','research/searches/source-decoration-hat-patch.py')
hat=importlib.util.module_from_spec(spec);spec.loader.exec_module(hat)
K=QuadraticField(3,'r');r=K.gen()
def k(x):return K(x.a)+K(x.b)*r
def pt(p):return vector(K,[k(x) for x in p])
h=[pt(p) for p in hat.hat_outline];V=vector(K,[2,0])
P=[h[:5],[h[0],h[4],V,h[11],h[12]],[h[4],h[5],h[6],h[7],V],[V,h[8],h[9],h[10],h[11]]]
C=P[0]
# Choose lexicographically first dihedral correspondence from canonical prototype.
frames=[]
for Q in P:
 good=[]
 for eps in (1,-1):
  for sh in range(5):
   D=[Q[(sh+eps*i)%5] for i in range(5)]
   if any((C[i]-C[j]).dot_product(C[i]-C[j])!=(D[i]-D[j]).dot_product(D[i]-D[j]) for i in range(5) for j in range(5)):continue
   X=matrix(K,[(C[1]-C[0]),(C[2]-C[0])]).transpose()
   Y=matrix(K,[(D[1]-D[0]),(D[2]-D[0])]).transpose()
   R=Y*X.inverse();t=D[0]-R*C[0]
   assert R.transpose()*R==matrix.identity(K,2)
   assert all(R*C[i]+t==D[i] for i in range(5))
   good.append((eps,sh,R,t))
 assert good
 frames.append(good[0])
print('local_frames',[(e,s) for e,s,R,t in frames],flush=True)
meta=hat.init()
meta=hat.constructMetatiles(hat.constructPatch(*meta))
out=[];hat.expand(meta[0],hat.IDENT,out)
placements=[]
for lab,T in out:
 H=matrix(K,[[k(T[0]),k(T[1])],[k(T[3]),k(T[4])]])
 tr=vector(K,[k(T[2]),k(T[5])])
 for j,(eps,sh,R,t) in enumerate(frames):
  M=H*R;z=H*t+tr
  pts=[M*x+z for x in C]
  placements.append((j,M,pts))
# Atomic node occurrences include every true corner in the whole patch,
# and its exact parameter when it lies in any other pentagon's side.
vertices={tuple(p) for j,M,ps in placements for p in ps}
inc=defaultdict(list)
for tid,(j,M,ps) in enumerate(placements):
 for key in vertices:
  x=vector(K,key)
  for i in range(5):
   d=ps[(i+1)%5]-ps[i];v=x-ps[i]
   if d[0]*v[1]-d[1]*v[0]:continue
   t=v.dot_product(d)/d.dot_product(d)
   if 0<=t<1 and ('--native-only' not in sys.argv or t==0):
    inc[key].append((tid,i,t));break
neighbors=defaultdict(list)
for key,L in inc.items():
 for item in L:neighbors[item[0]].append((key,item))
results=[]
nproto=4 if '--four-free' in sys.argv else 2
nvar=10*nproto
for mask in ([None] if nproto==4 else range(1,8)):
 colors=list(range(4)) if nproto==4 else [(mask>>j)&1 for j in range(4)]
 def expr(item):
  tid,i,t=item;j,M,ps=placements[tid];c=colors[j]
  E=matrix(K,2,nvar)
  for a in range(2):
   for b in range(2):
    E[a,10*c+2*i+b]+=(1-t)*M[a,b]
    E[a,10*c+2*((i+1)%5)+b]+=t*M[a,b]
  return E
 pos={0:matrix(K,2,nvar)};q=deque([0]);rows=[]
 while q:
  u=q.popleft()
  for key,item in neighbors[u]:
   val=pos[u]+expr(item)
   for other in inc[key]:
    v=other[0];new=val-expr(other)
    if v not in pos:pos[v]=new;q.append(v)
    else:rows.extend((pos[v]-new).rows())
 assert len(pos)==len(placements)
 L=matrix(K,rows)
 # Four prototype translation gauges and one original uniform scale always survive.
 base=vector(K,list(C[0])+list(C[1])+list(C[2])+list(C[3])+list(C[4]))
 assert L*vector(K,list(base)*nproto)==0
 ker=L.right_kernel();dim=ker.dimension()
 # Gauge both canonical first vertices to zero for transparent shape coordinates.
 gauges=matrix(K,2*nproto,nvar)
 for a,idx in enumerate([10*c+a for c in range(nproto) for a in (0,1)]):gauges[a,idx]=1
 shapedim=L.stack(gauges).right_kernel().dimension()
 row={'mask':mask,'colors':colors,'tiles':len(placements),'nodes':len(inc),'rank':int(L.rank()),'kernel_dimension':int(dim),'shape_dimension':int(shapedim)}
 results.append(row);print(row,flush=True)
 if nproto==4:
  print('gauge_fixed_kernel_basis', [[str(v) for v in row] for row in L.stack(gauges).right_kernel().basis()],flush=True)
print(json.dumps({'status':'EXPLORATORY_FIXED_FRAMES','native_only':'--native-only' in sys.argv,'four_free':'--four-free' in sys.argv,'results':results},indent=2))
