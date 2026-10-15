#!/usr/bin/env python3
"""Independent exact counterfixture audit; no producer imports or floats.
Radical AA coordinates replace the producer's cyclotomic construction.
Convex polygon clipping independently verifies interior disjointness.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from sage.all import AA,QQ
R=AA(5).sqrt()
C36=(1+R)/4;S36=(AA(10)-2*R).sqrt()/4
C72=(R-1)/4;S72=(AA(10)+2*R).sqrt()/4
assert C36*C36+S36*S36==1
assert C72==2*C36*C36-1 and S72==2*C36*S36
r=QQ(1)/100
uX=(S36+r*C36)/(S36*(1-r*r)+2*r*C36)
uY=AA(QQ(2)/5)
parameters={}
for mark,u,k in (('X',uX,QQ(337)/1000),('Y',uY,QQ(708)/1000)):
 h=u*r;m=u+k*h
 assert 0<u<m<1 and h>0
 parameters[mark]=(u,h,m)
assert parameters['X'][1]/(1-uX)==(r+S36/C36)/(1-r*S36/C36)
assert 0<r<S36/C36 and 1-r*S36/C36>0
assert parameters['Y'][1]/(1-uY)==QQ(1)/150

def sub(p,q):return (p[0]-q[0],p[1]-q[1])
def add(p,q):return (p[0]+q[0],p[1]+q[1])
def times(k,p):return (k*p[0],k*p[1])
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def oriented_area(P):
 return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2 if len(P)>=3 else AA(0)
def strict_ccw(P):
 assert oriented_area(P)>0
 for i,p in enumerate(P):
  side=sub(P[(i+1)%len(P)],p)
  for j,q in enumerate(P):
   if j not in (i,(i+1)%len(P)):assert cross(side,sub(q,p))>0

def intersection(P,Q):
 """Clip P by Q's closed left half-planes. Zero area permits boundary contact."""
 out=list(P)
 for i,a in enumerate(Q):
  b=Q[(i+1)%len(Q)];side=sub(b,a);old=out;out=[]
  if not old:break
  for j,e in enumerate(old):
   s=old[j-1];ds=cross(side,sub(s,a));de=cross(side,sub(e,a))
   if (ds>=0)!=(de>=0):
    out.append(add(s,times(ds/(ds-de),sub(e,s))))
   if de>=0:out.append(e)
 return out

def disjoint(polys):
 for P,Q in combinations(polys,2):assert oriented_area(intersection(P,Q))==0

ARROWS={
 'thin':((0,1,'X'),(2,1,'X'),(2,3,'Y'),(0,3,'Y')),
 'thick':((0,1,'X'),(1,2,'Y'),(3,2,'Y'),(0,3,'X')),
}
# Distinct analytic endpoint contexts, including actual adjacent donor role.
EXPECTED={
 ('thin','X','tail'):(36,'Y','tail'),
 ('thin','X','head'):(144,'X','head'),
 ('thin','Y','tail'):(36,'X','tail'),
 ('thin','Y','head'):(144,'Y','head'),
 ('thick','X','tail'):(72,'X','tail'),
 ('thick','X','head'):(108,'Y','tail'),
 ('thick','Y','tail'):(108,'X','head'),
 ('thick','Y','head'):(72,'Y','head'),
}
records=[];cases=0;quads=central=0;contexts=Counter()
for species,cs,sn in (('thin',C36,S36),('thick',C72,S72)):
 V=[(AA(0),AA(0)),(AA(1),AA(0)),(1+cs,sn),(cs,sn)]
 assert oriented_area(V)==sn
 for parity in (0,1):
  donor_edges={j for j in range(4) if j%2==parity};nodes={};cells=[]
  for j in donor_edges:
   tail,head,Z=ARROWS[species][j];u,h,m=parameters[Z]
   tangent=sub(V[head],V[tail]);boundary=sub(V[(j+1)%4],V[j])
   inward=(-boundary[1],boundary[0])
   assert dot(tangent,tangent)==dot(inward,inward)==1 and dot(tangent,inward)==0
   nodes[j]=add(V[tail],add(times(u,tangent),times(h,inward)))
   cells.append([V[j],V[(j+1)%4],nodes[j]])
  receivers=sorted(set(range(4))-donor_edges)
  for j in receivers:cells.append([V[j],V[(j+1)%4],nodes[(j+1)%4],nodes[(j-1)%4]])
  for P in cells:
   strict_ccw(P)
   for a in P:
    for i in range(4):assert cross(sub(V[(i+1)%4],V[i]),sub(a,V[i]))>=0
  disjoint(cells)
  assert sum(oriented_area(P) for P in cells)==sn
  assembled=[]
  for j in receivers:
   tail,head,Z=ARROWS[species][j];u,h,m=parameters[Z]
   a=sub(V[head],V[tail]);edge=sub(V[(j+1)%4],V[j]);n=(-edge[1],edge[0])
   t=add(V[tail],add(times(u,a),times(-h,n)))
   M=add(V[tail],times(m,a));U=V[j];W=V[(j+1)%4]
   p=nodes[(j-1)%4];q=nodes[(j+1)%4]
   L=[U,t,M,p];H=[M,t,W,q];C=[M,q,p]
   for P in (L,H,C):strict_ccw(P)
   quads+=2;central+=1;assembled.extend((L,H,C))
   inner=[[U,M,p],[M,W,q],C]
   for P in inner:strict_ccw(P)
   disjoint(inner)
   assert sum(oriented_area(P) for P in inner)==oriented_area([U,W,q,p])
   assert oriented_area(L)==oriented_area([U,t,M])+oriented_area([U,M,p])
   assert oriented_area(H)==oriented_area([M,t,W])+oriented_area([M,W,q])
   for endpoint,node,adjacent in ((j,p,(j-1)%4),((j+1)%4,q,(j+1)%4)):
    role='tail' if endpoint==tail else 'head'
    dt,dh,DZ=ARROWS[species][adjacent];du,dheight,dm=parameters[DZ]
    donor_role='tail' if endpoint==dt else 'head'
    k=du if donor_role=='tail' else 1-du
    cost=cs if endpoint%2==0 else -cs
    sigma=(36 if endpoint%2==0 else 144) if species=='thin' else (72 if endpoint%2==0 else 108)
    f=k*cost+dheight*sn;g=k*sn-dheight*cost
    x=dot(sub(node,V[tail]),a);y=dot(sub(node,V[tail]),n)
    assert y==g>0 and x==(f if role=='tail' else 1-f)
    determinant=m*(y+h)-u*y-h*x
    # This is the ACTUAL M turn of [endpoint,t,M,node], divided by
    # the signed orthonormal arrow-frame determinant; head order is reversed.
    actual=cross(sub(M,t),sub(node,M))
    assert actual==cross(a,n)*determinant
    assert determinant>0 if role=='tail' else determinant<0
    assert EXPECTED[(species,Z,role)]==(sigma,DZ,donor_role)
    contexts[(species,Z,role)]+=1
    records.append({'species':species,'parity':parity,'receiver':j,'endpoint':endpoint,
      'mark':Z,'role':role,'adjacent_donor_mark':DZ,'adjacent_donor_endpoint':donor_role,
      'source_angle':sigma,'strict':True,'normalized_D_sign':1 if role=='tail' else -1})
  disjoint(assembled);cases+=1
assert (cases,quads,central)==(4,16,8)
assert set(contexts.values())=={2} and len(contexts)==8
for Z,(u,h,m) in parameters.items():
 t=(u,-h);v=sub((AA(0),AA(0)),t);w=sub((m,AA(0)),t)
 denominator=abs(cross(v,w));numerator=dot(v,w)
 assert denominator==h*m>0
 assert numerator==h*h-u*(m-u)
 expected_cot=QQ(-32700)/100337 if Z=='X' else QQ(-17450)/25177
 assert numerator/denominator==expected_cot
 # Compare cot(angle) to cot108, with positive denominators.
 assert numerator*S72 < -C72*denominator
cert=json.loads((Path(__file__).resolve().parents[1]/'certificates/offnormal-strict-m-determinants-2026-10-15.json').read_text())
assert cert['status']=='PASS' and cert['records']==records
assert {(r['species'],r['parity'],r['valid']) for r in cert['source_partitions']}=={(s,p,True) for s in ARROWS for p in (0,1)}
print('PASS: radical reconstruction; 4 contained exact-area source partitions with zero-area clipped intersections; 16 CCW strictly convex assembled quads; 8 central sector partitions; all16 actual-arrow M determinants; both tail half-apex angles >108; retained record matches.')
