#!/usr/bin/env python3
"""Independent exact four-face two-run torus and full-curve angle identities."""
from pathlib import Path
from collections import deque
import json
from sage.all import NumberField,PolynomialRing,QQ,AA,vector,matrix,identity_matrix
x=PolynomialRing(QQ,'x').gen()
K=NumberField(x**4-10*x*x+1,'g',embedding=AA(2).sqrt()+AA(3).sqrt());g=K.gen()
h2=(g-1/g)/2;h3=(g+1/g)/2
assert h2*h2==2 and h3*h3==3 and AA(h2)>0 and AA(h3)>0
ROOT=Path(__file__).resolve().parents[2]
C=json.loads((ROOT/'research/certificates/branching-hexagon-new-two-run-four-face-periodic.json').read_text())
cp=(h2*h3+h2)/4;sp=(h2*h3-h2)/4
R=matrix(K,[[cp,-sp],[sp,cp]])
assert R.transpose()*R==identity_matrix(K,2) and R**24==identity_matrix(K,2)
def polygon(lengths,degrees):
 out=[];z=vector(K,[0,0])
 for L,deg in zip(lengths,degrees):
  out.append(z);z+=L*(R**(deg//15))*vector(K,[1,0])
 assert z==0
 return out
A=polygon([cp,1,cp,1,cp,1],[0,75,120,195,240,315])
B=polygon([cp,cp,cp,1,1,1],[0,60,120,165,255,285])
faces=[A,A,B,B]
angles=[[135,105,135,105,135,105]]*2+[[105,120,120,135,90,150]]*2
# Affine angle forms(constant,delta coefficient) for the entire0<delta<30 curve.
forms=[[(120,1),(120,-1)]*3]*2+[[(120,-1),(120,0),(120,0),(120,1),(120,-2),(120,2)]]*2
for F in(A,B):
 for i,z in enumerate(F):
  edge=F[(i+1)%6]-z
  for j,y in enumerate(F):
   if j not in(i,(i+1)%6):
    v=y-z;assert edge[0]*v[1]-edge[1]*v[0]>0
pair={};graph={i:set()for i in range(4)}
for row in C['paired_edges']:
 x,y=map(tuple,row);assert x!=y and x not in pair and y not in pair
 pair[x]=y;pair[y]=x;graph[x[0]].add(y[0]);graph[y[0]].add(x[0])
 i,j=x;k,l=y
 v=faces[i][(j+1)%len(faces[i])]-faces[i][j];u=faces[k][(l+1)%len(faces[k])]-faces[k][l]
 assert v.dot_product(v)==u.dot_product(u)>0
assert len(pair)==24 and set(pair)=={(i,j)for i,F in enumerate(faces)for j in range(len(F))}
seen={0};todo=[0]
while todo:
 i=todo.pop()
 for j in graph[i]-seen:seen.add(j);todo.append(j)
assert len(seen)==4
# Actual circular links, not only vertex unions.
visited=set();links=[]
for start in pair:
 if start in visited:continue
 link=[];x=start
 while x not in visited:
  visited.add(x);link.append(x);k,l=pair[x];x=(k,(l+1)%len(faces[k]))
 assert x==start and sum(angles[i][j]for i,j in link)==360
 assert sum(forms[i][j][0]for i,j in link)==360 and sum(forms[i][j][1]for i,j in link)==0
 links.append(link)
assert len(links)==8 and 8-12+4==0
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
U=vector(K,[(h2*h3+3*h2)/4,(-3*h2*h3-7*h2)/4]);V=vector(K,[h2*h3/2,h2*h3/2+h2]);lattice=matrix(K,[[U[0],V[0]],[U[1],V[1]]]);inv=lattice.inverse()
holos=[]
for (i,j),(k,l) in pair.items():
 end=placed[i][(j+1)%len(placed[i])];start=placed[i][j]
 shift=start-placed[k][(l+1)%len(placed[k])]
 assert end-placed[k][l]==shift
 coordinates=inv*shift;assert all(z in __import__('sage.all',fromlist=['ZZ']).ZZ for z in coordinates)
 holos.append(tuple(int(z)for z in coordinates))
area=lambda F:sum(F[i][0]*F[(i+1)%len(F)][1]-F[i][1]*F[(i+1)%len(F)][0]for i in range(len(F)))/2
assert area(A)==K(15)/16+7*h3/8 and area(B)==K(21)/16+5*h3/8
assert abs(lattice.det())==sum(area(F)for F in placed)==K(9)/2+3*h3
# Every rank-two integer cycle translation is in this lattice; verify they
# generate the whole lattice, independent of author HNF implementation.
from math import gcd
minors=[abs(x[0]*y[1]-x[1]*y[0])for x in holos for y in holos]
assert gcd(*minors)==1
print('PASS cos15 two-run:4 strictly convex exact faces,12 seams,8 actual circular links,exact primitiveperiod lattice,area/covolume;all8 angle-link identities hold symbolically throughout0<delta<30;no producer imports')
