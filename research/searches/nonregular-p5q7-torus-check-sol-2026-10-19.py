"""Independent exact four-polygon flat-torus certificate checker. No solver."""
import json
from pathlib import Path
A=[5,16,21,12,17,0,23,14,19,10,9,18,3,20,7,22,1,4,11,8,13,2,15,6]
words=[[115,115,100,110,100]]*2+[[130,130,130,125,125,125,135]]*2
lengths=[['L','1','1','1','1']]*2+[['1','a','1','b','1','1','1']]*2
angles=sum(words,[]);labels=sum(lengths,[])
rho=[];start=0
for w in words:
 rho += [start+(i+1)%len(w) for i in range(len(w))]
 start+=len(w)
assert sorted(A)==list(range(24))
for i,j in enumerate(A):assert i!=j and A[j]==i and labels[i]==labels[j]
v=[rho[A[i]] for i in range(24)]
cycles=[];unseen=set(range(24))
while unseen:
 i=min(unseen);cy=[i];j=v[i]
 while j!=i:
  assert j not in cy
  cy.append(j);j=v[j]
 assert len(cy)==3 and sum(angles[x] for x in cy)==360
 unseen.difference_update(cy);cycles.append(cy)
assert len(cycles)==8 and len(words)-12+len(cycles)==0
seen={0}
while True:
 nxt=seen|{rho[i] for i in seen}|{A[i] for i in seen}
 if nxt==seen:break
 seen=nxt
assert len(seen)==24
print(json.dumps({'status':'verified connected oriented flat torus combinatorics','alpha':A,'rho':rho,'vertices':cycles,'F':4,'E':12,'V':8},indent=2))
