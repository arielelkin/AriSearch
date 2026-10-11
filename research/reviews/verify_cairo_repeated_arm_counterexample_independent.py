#!/usr/bin/env python3
"""Independent exact audit of one repeated-arm Cairo monohedral obstruction."""
from sage.all import QuadraticField,AA,vector
from itertools import combinations_with_replacement
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
word=[K(1),K(1),1+w/2,K(1)/2,w]
directions=[(1,0),(0,1),(-w/2,K(1)/2),(-K(1)/2,-w/2),(K(1)/2,-w/2)]
vertices=[];point=vector(K,[0,0])
for L,u in zip(word,directions):vertices.append(point);point=point+L*vector(K,u)
assert point==0
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
for i in range(5):
 edge=vertices[(i+1)%5]-vertices[i];assert edge.dot_product(edge)==word[i]**2
 for j in range(5):
  if j not in(i,(i+1)%5):assert cross(edge,vertices[j]-vertices[i])>0
other=[1,0,3,2];events=[]
for i,j in combinations_with_replacement(range(4),2):
 if word[i]==word[j]:
  assert word[other[i]]==word[other[j]]
  events.append(2*word[other[i]])
assert len(events)==5 and word[4] not in events
assert len(set(word[:4]))==3
# At any e/e endpoint the opposite ray lengths are these possibilities.
for rays in((word[0],word[0]),(word[3],word[3]),(word[0],word[3])):
 assert sorted(rays)!=sorted((word[1],word[2]))
print('PASS repeated-arm Cairo: exact closure,15 strict supports,5 squared side lengths,all5 same-perpendicular events,all e exclusions and e/e filler obstructions')
