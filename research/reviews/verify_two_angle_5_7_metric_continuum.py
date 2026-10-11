#!/usr/bin/env python3
"""Fresh exact audit of the 5/7 cone, formal quotient, and generic geometry.

Does not import the producer. Closure is solved from independent unit-vector
rows; certificate rays/facets are checked by AA linear algebra; circular
links use a CCW corner permutation; generic coordinates have a complete
lattice-overlap check. Shape-only uniqueness is reviewed in the companion
Markdown proof audit rather than inferred from finitely many coordinates.
"""
if not __debug__:
    raise RuntimeError('Exact verification requires assertions')

from itertools import combinations, product
from pathlib import Path
import json
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, matrix, vector

ROOT=Path(__file__).resolve().parents[2]
data=json.loads((ROOT/'research/certificates/two-angle-5-7-metric-continuum.json').read_text())
K=CyclotomicField(28);w=K.gen();ii=w**7;z=w**4
roots=K.polynomial().roots(QQbar,multiplicities=False)
omegas=[r for r in roots if QQ(97)/100<r.real()<QQ(98)/100
        and QQ(22)/100<r.imag()<QQ(23)/100]
assert len(omegas)==1
embedding=K.hom([omegas[0]],QQbar)
t=w**2+w**(-2)
assert t**3-t**2-2*t+1==0
real=lambda x:AA(embedding(x).real())
assert QQ(18)/10<real(t)<QQ(181)/100
assert data['field']['polynomial_coefficients']==['1','-2','-1','1']

def decode(row):
    return sum(K(QQ(c))*t**i for i,c in enumerate(row))

normals=[vector(K,[decode(q) for q in row]) for row in data['cone']['strict_inequality_normals']]
cos=lambda j:(z**j+z**(-j))/2
sin=lambda j:(z**j-z**(-j))/(2*ii)
# Solve H closure and the requirement e1-e3+e5-e6=p*(1,0).
unknown=matrix(K,[[1,cos(3),cos(5),0],[0,sin(3),sin(5),0],
                  [0,-cos(3),cos(5),-1],[0,-sin(3),sin(5),0]])
known=matrix(K,[[cos(1),cos(2),cos(4),cos(6)],
                [sin(1),sin(2),sin(4),sin(6)],
                [cos(1),0,0,-cos(6)],[sin(1),0,0,-sin(6)]])
assert unknown.rank()==4
solution=-unknown.inverse()*known
assert list(solution.rows()) == normals[4:]
assert normals[:4] == list(matrix.identity(K,4).rows())

# Independent exact complete extreme-ray enumeration, 56 triple-active sets.
N=matrix(AA,[[real(q) for q in row] for row in normals])
found=[]
for triple in combinations(range(8),3):
    active=matrix(AA,[N.row(i) for i in triple])
    if active.rank()!=3:
        continue
    r=active.right_kernel().basis()[0]
    r=r/next(q for q in r if q)
    if any(n.dot_product(r)<0 for n in N.rows()):
        continue
    if not any(r==s for s in found):
        found.append(r)
encoded_rays=[vector(AA,[real(decode(q)) for q in row['parameters']])
              for row in data['cone']['extreme_rays']]
assert len(found)==len(encoded_rays)==9
assert all(any(r==s for s in found) for r in encoded_rays)
for j,facet in enumerate(data['cone']['irredundant_facets']):
    witness=vector(AA,[real(decode(q)) for q in facet['facet_relative_interior_witness']])
    assert N.row(j).dot_product(witness)==0
    assert all(N.row(k).dot_product(witness)>0 for k in range(8) if k!=j)

S=PolynomialRing(K,names=('a','b','c','d'));params=S.gens()
linear=lambda row:sum(c*p for c,p in zip(row,params))
ls=[linear(normals[i]) for i in [4,0,1,5,2,6,3]]
private=linear(normals[7])
H=[vector(S,[0,0])]
for j,l in enumerate(ls):
    H.append(H[-1]+vector(S,[l*cos(j),l*sin(j)]))
assert H[-1]==vector(S,[0,0]);H.pop()
P=[H[6]]
for step in [vector(S,[ls[6]*cos(6),ls[6]*sin(6)]),
             vector(S,[-ls[1]*cos(1),-ls[1]*sin(1)]),
             vector(S,[ls[3]*cos(3),ls[3]*sin(3)]),
             vector(S,[-ls[5]*cos(5),-ls[5]*sin(5)])]:
    P.append(P[-1]+step)
assert P[0]-P[-1] == vector(S,[private,0])
ds={j:H[j]+H[j+1] for j in [0,2,4]}
u,v=ds[2]-ds[0],ds[4]-ds[0]
q=ds[0]-ds[2]+ds[4]
polys=[H,[ds[0]-p for p in H],P,[q-p for p in P]]
det=lambda a,b:a[0]*b[1]-a[1]*b[0]
area2=lambda poly:sum(det(p,poly[(i+1)%len(poly)]) for i,p in enumerate(poly))
assert det(u,v)==area2(H)-area2(P)

# Verify actual seam endpoints and normalized CCW circular links.
twin={};faceadj={f:set() for f in range(4)}
sideindex=lambda f,j:j if f<2 else (-j-1)%5
for f,j,g,k,m,n,reverse in data['formal_geometry']['seam_table']:
    shift=m*u+n*v
    a=[polys[f][j],polys[f][(j+1)%len(polys[f])]]
    b=[polys[g][k]+shift,polys[g][(k+1)%len(polys[g])]+shift]
    if reverse:
        b.reverse()
    assert a==b
    i,h=sideindex(f,j),sideindex(g,k)
    assert (f,i) not in twin and (g,h) not in twin
    twin[f,i]=(g,h);twin[g,h]=(f,i)
    faceadj[f].add(g);faceadj[g].add(f)
domain={(f,j) for f in range(4) for j in range(len(polys[f]))}
assert set(twin)==domain
successor={a:(b[0],(b[1]+1)%len(polys[b[0]])) for a,b in twin.items()}
unseen=set(domain);cycles=[]
while unseen:
    start=min(unseen);cycle=[];cur=start
    while cur not in cycle:
        cycle.append(cur);cur=successor[cur]
    assert cur==start
    unseen.difference_update(cycle);cycles.append(cycle)
assert len(cycles)==8 and all(len(c)==3 for c in cycles)
for cycle in cycles:
    assert sorted(5 if f<2 or j==0 else 4 for f,j in cycle)==[4,5,5]
seen={0}
while seen != set(range(4)):
    expanded=seen|{g for f in seen for g in faceadj[f]}
    assert expanded != seen
    seen=expanded
assert 8-12+4==0

# Concrete generic fixture: geometry, forced-corner uniqueness, whole plane.
fixture=[QQ(1),QQ(11)/10,QQ(6)/5,QQ(9)/10]
evalpoint=lambda p:vector(AA,[real(c(*fixture)) for c in p])
actual=[[evalpoint(p) for p in poly] for poly in polys]
u0,v0=evalpoint(u),evalpoint(v)
lengths=[real(linear(n)(*fixture)) for n in normals]
assert min(lengths)>0 and len(set(lengths))==8
length_map={i:real(ls[i](*fixture)) for i in range(7)}
pvalue=real(private(*fixture))
Pcornerpairs=[(pvalue,length_map[6]),(length_map[6],length_map[1]),
              (length_map[1],length_map[3]),(length_map[3],length_map[5]),
              (length_map[5],pvalue)]
assert [i for i,pair in enumerate(Pcornerpairs) if set(pair)=={length_map[6],length_map[1]}]==[1]
assert all(a!=b for a,b in Pcornerpairs)
assert set(Pcornerpairs[0])!={length_map[5],length_map[6]}
areas=[]
for f,poly in enumerate(actual):
    orientation=1 if f<2 else -1
    for i,p in enumerate(poly):
        edge=poly[(i+1)%len(poly)]-p
        assert all(orientation*det(edge,poly[j]-p)>0 for j in range(len(poly))
                   if j not in (i,(i+1)%len(poly)))
    areas.append(orientation*area2(poly)/2)
assert sum(areas)==det(u0,v0)>0
M=matrix(AA,[[u0[0],v0[0]],[u0[1],v0[1]]]);inv=M.inverse()
boxes=[]
for poly in actual:
    coords=[inv*p for p in poly]
    boxes.append([(min(p[d] for p in coords),max(p[d] for p in coords)) for d in [0,1]])
def separated(a,b):
    for poly in [a,b]:
        for i,p in enumerate(poly):
            edge=poly[(i+1)%len(poly)]-p
            aa=[det(edge,z) for z in a];bb=[det(edge,z) for z in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):
                return True
    return False
comparisons=0
for f,g in product(range(4),repeat=2):
    ranges=[range(int((boxes[f][d][0]-boxes[g][d][1]).ceil()),
                  int((boxes[f][d][1]-boxes[g][d][0]).floor())+1) for d in [0,1]]
    for m,n in product(*ranges):
        if f==g and m==n==0:
            continue
        shifted=[p+m*u0+n*v0 for p in actual[g]]
        assert separated(actual[f],shifted),(f,g,m,n)
        comparisons+=1
print('PASS independent 4D closure; 56 active triples/9 rays; 8 irredundant facets;')
print('PASS formal seams/area identity; 8 actual circular links; generic exact convexity;',
      comparisons,'complete overlap comparisons; exact density 1')
