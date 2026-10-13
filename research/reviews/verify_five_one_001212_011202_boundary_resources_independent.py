#!/usr/bin/env python3
"""Fresh boundary resources; independently reversed seam orientation."""
from itertools import product
P=list(product(range(6),(1,-1)))
def co(W,p,k):return W[(p[0]+p[1]*k)%6]
def si(p,k):
 e={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 return next(j for j in range(6) if {j,(j+1)%6}==e)
for word,res,metric in [('001212',1,{1,4}),('011202',0,{0,3})]:
 W=tuple(map(int,word))
 for top in [True,False]:
  zslot=1 if top else 4;outer=(0,2) if top else (5,3);inner=(5,3) if top else (0,2)
  eligible=[p for p in P if co(W,p,zslot)==2];assert len(eligible)==4
  edges=[]
  for p,q in product(P,repeat=2):
   if p not in eligible or q not in eligible:continue
   oc=(co(W,p,outer[0]),co(W,q,outer[1]));ic=(co(W,p,inner[0]),co(W,q,inner[1]))
   if oc not in [(0,0),(1,1)] or ic[0]==ic[1]:continue
   assert oc==(res,res)
   edges.append((eligible.index(p),eligible.index(q)))
  assert len(edges)==4
  reach={i:{j for a,j in edges if a==i} for i in range(4)}
  for k in range(4):
   for i in range(4):
    if k in reach[i]:reach[i]|=reach[k]
  cycles={i for i in range(4) if i in reach[i]}
  viable={i for i in range(4) if any(i==j or i in reach[j] for j in cycles) and any(i==j or j in reach[i] for j in cycles)}
  assert len(viable)==2 and viable==cycles
  assert {(a,b) for a,b in edges if a in viable and b in viable}=={(i,i) for i in viable}
  for i in viable:assert {si(eligible[i],5),si(eligible[i],2)}==metric
 print('PASS',word,'bothface288pairs;uniformresource',res,'truebiinfinitepathsconstant;nativeequality',sorted(metric))
