#!/usr/bin/env python3
"""Independent native-state grouping; allow all B-neighbour phases."""
from itertools import product
ST=list(product(range(6),(1,-1)));B=(3,4,4,4,4,4)
def co(W,p,k):return W[(p[0]+p[1]*k)%6]
def si(p,k):
 e={(p[0]+p[1]*k)%6,(p[0]+p[1]*(k+1))%6}
 return next(j for j in range(6) if {j,(j+1)%6}==e)
BS=[p for p in ST if {si(p,2),si(p,5)}=={1,4}]
BP={h:[p for p in BS if co(B,p,1 if h==0 else 4)==3] for h in (0,1)}
assert all(len(t)==2 for t in BP.values())
legal={tuple(sorted(t)) for t in ((0,0,4),(1,1,3),(2,4,4))}
expected={'002112':(1,0,0),'012012':(1,1,1),'012102':(0,0,1)}
count=0
for word,answer in expected.items():
 A=tuple(map(int,word));AS=[p for p in ST if {si(p,2),si(p,5)}=={0,3}]
 profile=lambda p:tuple(co(A,p,k) for k in range(6))
 p0=profile((1,1));AP={0:[p for p in AS if profile(p)==p0],1:[p for p in AS if profile(p)!=p0]}
 assert all(len(t)==2 for t in AP.values()) and len({profile(p) for p in AP[1]})==1
 horizontal=set()
 for h,l in product((0,1),repeat=2):
  matches=[co(A,p,0)==co(A,q,2) and co(A,p,5)==co(A,q,3) for p,q in product(AP[h],AP[l])]
  assert all(matches) or not any(matches)
  if all(matches):horizontal.add(h^l)
 assert len(horizontal)==1
 flip=horizontal.pop();assert flip==answer[0]
 phase_relations=set()
 for lo,hi,bp in product((0,1),repeat=3):
  outcomes=[]
  for b,left,right,upper0,upper1,lower0,lower1 in product(BP[bp],BS,BS,AP[hi],AP[hi^flip],AP[lo],AP[lo^flip]):
   neighbours=(left,upper0,upper1,right,lower0,lower1);words=(B,A,A,B,A,A)
   stars=[tuple(sorted((co(B,b,k),co(words[k],neighbours[k],k+2),co(words[(k+1)%6],neighbours[(k+1)%6],k+4)))) for k in range(6)]
   outcomes.append(all(t in legal for t in stars));count+=1
  assert all(outcomes) or not any(outcomes)
  if all(outcomes):phase_relations.add((hi^lo,bp^lo))
 assert phase_relations=={answer[1:]}
print('PASS endpoint-derived3 angle fibres;12288 native wheels with independentB-neighbour phases;all horizontal/vertical/offset relations')
