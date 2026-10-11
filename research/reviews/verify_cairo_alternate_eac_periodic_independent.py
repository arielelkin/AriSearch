#!/usr/bin/env python3
"""Reconstruct an exact eight-face flat torus and its Euclidean development."""
from pathlib import Path
from collections import deque
import json
from sage.all import QuadraticField,AA,vector,matrix,identity_matrix
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
ROOT=Path(__file__).resolve().parents[2]
C=json.loads((ROOT/'research/certificates/partial-contact-cairo-alternate-eac-eight-face-lift.json').read_text())
a=K(1);b=1+4*w/3;c=w/3;d=2+w/3;e=1+w/3;f=2+4*w/3
unit=[vector(K,u)for u in((1,0),(0,1),(-w/2,K(1)/2),(-K(1)/2,-w/2),(K(1)/2,-w/2))]
def polygon(word):
 out=[];z=vector(K,[0,0])
 for t,u in zip(word,unit):out.append(z);z+=t*u
 assert z==0
 return out
P=polygon((a,b,c,d,e));Q=polygon((a,d,b,c,f))
for F in(P,Q):
 for i,x in enumerate(F):
  y=F[(i+1)%5];delta=y-x
  for j,z in enumerate(F):
   if j not in(i,(i+1)%5):
    shift=z-x;assert delta[0]*shift[1]-delta[1]*shift[0]>0
P=[P[0],P[0]+c*unit[0],P[1],P[2],P[3],P[4],P[4]+c*unit[4]]
reflect=lambda z:vector(K,[z[0],-z[1]])
mirror=lambda face:[reflect(face[0])]+[reflect(z)for z in face[:0:-1]]
faces=[P,P,mirror(P),mirror(P),Q,Q,mirror(Q),mirror(Q)]
angles=[[120,180,90,120,90,120,180]]*2+[[120,180,120,90,120,90,180]]*2+[[120,90,120,90,120]]*2+[[120,120,90,120,90]]*2
pair={};graph={i:set()for i in range(8)}
for row in C['paired_edges']:
 x,y=map(tuple,row);assert x!=y and x not in pair and y not in pair
 pair[x]=y;pair[y]=x;graph[x[0]].add(y[0]);graph[y[0]].add(x[0])
 i,j=x;k,l=y
 v=faces[i][(j+1)%len(faces[i])]-faces[i][j];u=faces[k][(l+1)%len(faces[k])]-faces[k][l]
 assert v.dot_product(v)==u.dot_product(u)>0
assert len(pair)==48 and set(pair)=={(i,j)for i,F in enumerate(faces)for j in range(len(F))}
seen={0};todo=[0]
while todo:
 i=todo.pop()
 for j in graph[i]-seen:seen.add(j);todo.append(j)
assert len(seen)==8
# Actual circular links, not only vertex unions.
visited=set();links=[]
for start in pair:
 if start in visited:continue
 link=[];x=start
 while x not in visited:
  visited.add(x);link.append(x);k,l=pair[x];x=(k,(l+1)%len(faces[k]))
 assert x==start and sum(angles[i][j]for i,j in link)==360
 links.append(link)
assert len(links)==16 and 16-24+8==0
assert {frozenset(x)for x in links}=={frozenset(map(tuple,x))for x in C['vertex_classes']}
# BFS direct-isometry placement from endpoint equations.
M={0:identity_matrix(K,2)};t={0:vector(K,[0,0])};todo=deque([0])
while todo:
 i=todo.popleft()
 for j in range(len(faces[i])):
  k,l=pair[i,j]
  if k in M:continue
  start=M[i]*faces[i][j]+t[i];end=M[i]*faces[i][(j+1)%len(faces[i])]+t[i]
  x=faces[k][(l+1)%len(faces[k])];y=faces[k][l];u=y-x;v=end-start
  L=u.dot_product(u);cc=u.dot_product(v)/L;ss=(u[0]*v[1]-u[1]*v[0])/L
  R=matrix(K,[[cc,-ss],[ss,cc]]);assert R.det()==1 and R.transpose()*R==identity_matrix(K,2)
  M[k]=R;t[k]=start-R*x;todo.append(k)
placed=[[M[i]*z+t[i]for z in F]for i,F in enumerate(faces)]
U=vector(K,[2+w,2+w]);V=vector(K,[4*w/3,-4-10*w/3]);lattice=matrix(K,[[U[0],V[0]],[U[1],V[1]]]);inv=lattice.inverse()
holos=[]
for (i,j),(k,l) in pair.items():
 end=placed[i][(j+1)%len(placed[i])];start=placed[i][j]
 shift=start-placed[k][(l+1)%len(placed[k])]
 assert end-placed[k][l]==shift
 coordinates=inv*shift;assert all(z in __import__('sage.all',fromlist=['ZZ']).ZZ for z in coordinates)
 holos.append(tuple(int(z)for z in coordinates))
area=lambda F:sum(F[i][0]*F[(i+1)%len(F)][1]-F[i][1]*F[(i+1)%len(F)][0]for i in range(len(F)))/2
assert area(Q)==4+5*w/3 and area(P)==K(3)/2+5*w/3
assert abs(lattice.det())==sum(area(F)for F in placed)==22+40*w/3
# Every rank-two integer cycle translation is in this lattice; verify they
# generate the whole lattice, independent of author HNF implementation.
from math import gcd
minors=[abs(x[0]*y[1]-x[1]*y[0])for x in holos for y in holos]
assert gcd(*minors)==1
print('PASS eac:8 exact convex/reflected augmented faces,24 full piece seams,16 actual circular360links,connected orientable flat torus,all seam translations integral,full rank2 lattice,exact area/covolume identity;no producer imports')
