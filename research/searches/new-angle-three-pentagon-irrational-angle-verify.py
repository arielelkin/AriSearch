#!/usr/bin/env python3
"""Exact radical geometry and endpoint certificate for a three-angle trial.

No numerical tolerances or denominators searched. Radical arithmetic is in
Q(sqrt(5),sqrt(21)); positivity uses proved rational intervals.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import defaultdict
from math import isqrt
import json

PRIMES=(5,21)
RADICANDS=tuple(__import__('functools').reduce(lambda x,y:x*y,
    (p for i,p in enumerate(PRIMES) if m & (1<<i)),1) for m in range(4))
class E:
    def __init__(self, x=0):
        self.c=x.c if isinstance(x,E) else tuple(x) if isinstance(x,tuple) else (F(x),)+(F(0),)*3
    def __add__(self,other):
        other=E(other);return E(tuple(a+b for a,b in zip(self.c,other.c)))
    __radd__=__add__
    def __neg__(self):return E(tuple(-a for a in self.c))
    def __sub__(self,other):return self+-E(other)
    def __rsub__(self,other):return E(other)+-self
    def __mul__(self,other):
        other=E(other);c=[F(0)]*4
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):
                c[i^j]+=a*b*RADICANDS[i&j]
        return E(tuple(c))
    __rmul__=__mul__
    def __truediv__(self,other):return E(tuple(a/F(other) for a in self.c))
    def __eq__(self,other):return self.c==E(other).c
    def interval(self,denominator=1<<20):
        lo=F(0);hi=F(0)
        for coefficient,radicand in zip(self.c,RADICANDS):
            if not coefficient:continue
            if radicand==1:l=h=F(1)
            else:
                floor=isqrt(radicand*denominator**2)
                l=F(floor,denominator);h=F(floor+1,denominator)
                assert l*l<radicand<h*h
            lo+=coefficient*(l if coefficient>0 else h)
            hi+=coefficient*(h if coefficient>0 else l)
        return lo,hi
    def encode(self):return {str(n):str(c) for n,c in zip(RADICANDS,self.c) if c}
def radical(mask):
    c=[F(0)]*4;c[mask]=F(1);return E(tuple(c))
r5,r21=map(radical,(1,2))
a=r21/5;b=E(F(17,20));c=r21/4
t=E(1);s=r5
x=(a*t+b*s,t,t/2+c*s,b*t+a*s,s,c*t+s/2)
assert all(v.interval()[0]>0 for v in x)
assert all(x[i]!=x[j] for i in range(6) for j in range(i))
P=(x[5],x[0],x[3],x[1],x[2]);Q=(x[2],x[3],x[0],x[4],x[5])
assert P[3]==1 and Q[3]==r5 and Q[3]*Q[3]==5
assert P!=Q
unit=((E(1),E(0)),(E(F(2,5)),r21/5),(-r21/5,E(F(2,5))),
      (-4*r21/25,E(-F(17,25))),(E(0),E(-1)))
assert all(u*u+v*v==1 for u,v in unit)
word=(0,1,0,1,2)  # Categories: right,theta,360-2theta.
expected_cosines=(E(0),E(-F(2,5)),E(0),E(-F(2,5)),E(-F(17,25)))
for i in range(5):
    previous,current=unit[(i-1)%5],unit[i]
    assert -(previous[0]*current[0]+previous[1]*current[1])==expected_cosines[i]
    assert (previous[0]*current[1]-previous[1]*current[0]).interval()[0]>0
assert F(4,25)<F(1,2)  # Gives90<theta<135 by cosine monotonicity.
assert F(-2,5)!=F(-1,2)  # theta!=120.
assert 8*F(2,5)**4-8*F(2,5)**2+1==F(-47,625) # theta!=112.5.
assert F(-4,5).denominator!=1 # Rational2cos(theta) is not an integer.

def cross(v,w):return v[0]*w[1]-v[1]*w[0]
def difference(v,w):return v[0]-w[0],v[1]-w[1]
geometry=[]
for name,L in (('P',P),('Q',Q)):
    vertices=[];position=(E(0),E(0));vectors=[]
    for length,(u,v) in zip(L,unit):
        vertices.append(position);edge=(length*u,length*v);vectors.append(edge)
        position=(position[0]+edge[0],position[1]+edge[1])
    assert position==(E(0),E(0))
    support=[]
    for i,edge in enumerate(vectors):
        for j,vertex in enumerate(vertices):
            if j in (i,(i+1)%5):continue
            determinant=cross(edge,difference(vertex,vertices[i]))
            lo,hi=determinant.interval()
            assert lo>0,(name,i,j,determinant.encode(),str(lo),str(hi))
            support.append({'side':i,'other_vertex':j,'determinant':determinant.encode(),
                            'strict_lower_bound':str(lo),'upper_bound':str(hi)})
    area=sum(cross(vertices[i],vertices[(i+1)%5]) for i in range(5))/2
    assert area.interval()[0]>0
    geometry.append({'name':name,'side_lengths':[v.encode() for v in L],
                     'vertices':[[u.encode(),v.encode()] for u,v in vertices],
                     'closure':[position[0].encode(),position[1].encode()],
                     'area':area.encode(),'strict_convex_support':support})

# Exhaustive analytic affine stars in theta, for theta in(90,135).
# Angles R=90, B=theta, G=360-2theta. Full valence3 or4; half valence1 or2.
affine=((90,0),(0,1),(360,-2))
permanent=[];exceptional=[]
for target,counts in ((180,(1,2)),(360,(3,4))):
    for count in counts:
        for triple in combinations_with_replacement(range(3),count):
            constant=sum(affine[i][0] for i in triple)
            slope=sum(affine[i][1] for i in triple)
            if slope==0:
                if constant==target:permanent.append({'target':target,'categories':list(triple)})
            else:
                root=F(target-constant,slope)
                if 90<root<135:exceptional.append({'target':target,'categories':list(triple),'theta':str(root)})
assert permanent==[{'target':180,'categories':[0,0]},
                   {'target':360,'categories':[1,1,2]},
                   {'target':360,'categories':[0,0,0,0]}]
assert sorted({F(r['theta']) for r in exceptional})==[F(225,2),F(120)]
# The chosen theta is irrational by the monic root-of-unity argument in the lemma.

# Four CCW faces P0,P1,Q0,Q1; sidej runs from cornerj to cornerj+1.
pairs=[((0,0),(2,4)),((0,2),(2,1)),((1,0),(3,4)),((1,2),(3,1)),
       ((2,0),(1,4)),((2,2),(1,1)),((3,0),(0,4)),((3,2),(0,1)),
       ((0,3),(1,3)),((2,3),(3,3))]
assert len({edge for pair in pairs for edge in pair})==20
parent=list(range(20))
def find(j):
    while parent[j]!=j:parent[j]=parent[parent[j]];j=parent[j]
    return j
def union(i,j):parent[find(i)]=find(j)
links=defaultdict(list);adjacency=defaultdict(set);seams=[]
face_lengths=(P,P,Q,Q)
for (f,j),(g,k) in pairs:
    assert face_lengths[f][j]==face_lengths[g][k]
    adjacency[f].add(g);adjacency[g].add(f)
    for u,v in (((f,j),(g,(k+1)%5)),((f,(j+1)%5),(g,k))):
        union(5*u[0]+u[1],5*v[0]+v[1]);links[u].append(v);links[v].append(u)
        seams.append([list(u),list(v)])
classes=defaultdict(list)
for f in range(4):
    for j in range(5):classes[find(5*f+j)].append((f,j))
classes=sorted(sorted(vs) for vs in classes.values())
assert len(classes)==6
assert sorted(map(len,classes))==[3,3,3,3,4,4]
for vs in classes:
    assert sum(affine[word[j]][0] for f,j in vs)==360
    assert sum(affine[word[j]][1] for f,j in vs)==0
    assert all(len(links[v])==2 and len(set(links[v]))==2 for v in vs)
    seen={vs[0]}
    while True:
        expanded=seen | {w for v in seen for w in links[v]}
        if expanded==seen:break
        seen=expanded
    assert seen==set(vs)
seen={0}
while True:
    expanded=seen | {g for f in seen for g in adjacency[f]}
    if expanded==seen:break
    seen=expanded
assert seen==set(range(4))
assert len(classes)-len(pairs)+4==0
print(json.dumps({'status':'PASS','radical_basis':RADICANDS,
 'radical_interval_denominator':1<<20,'t':'1','s':'sqrt(5)',
 'theta_cosine':'-2/5','theta_sine':'sqrt(21)/5',
 'native_angle_cosines':[v.encode() for v in expected_cosines],
 'theta_irrationality_reason':'2cos(theta)=-4/5 is rational nonintegral; rational angles would make it an algebraic integer',
 'six_distinct_positive_length_labels':[v.encode() for v in x],
 'prototype_geometry':geometry,'symbolic_permanent_stars':permanent,
 'symbolic_exceptional_parameter_rows':exceptional,
 'torus_pairings':[[list(u),list(v)] for u,v in pairs],
 'torus_seam_endpoints':seams,'torus_vertex_classes':[[list(v) for v in vs] for vs in classes],
 'torus_euler_characteristic':0,'torus_connected':True,
 'reference_reflections':[False]*4,
 'proof_dependencies_not_computed':['complete flat torus universal cover is the Euclidean plane']},indent=2,sort_keys=True))
