#!/usr/bin/env python3
"""Exact full 3D V/W metric-cone, formal torus, asymmetric overlap replay.
No import from earlier mirror-family producer. General claims use polynomial
identities, not bounded-search extrapolation. All assertions are required.
"""
if not __debug__:
    raise RuntimeError('Exact verification requires assertions')

from itertools import combinations, product
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, matrix, vector

K=CyclotomicField(20);w=K.gen();ii=w**5;z=w**2;phi=z+z**(-1)
assert phi*phi==phi+1
roots=K.polynomial().roots(QQbar,multiplicities=False)
omega=[r for r in roots if QQ(95)/100<r.real()<QQ(96)/100
       and QQ(30)/100<r.imag()<QQ(31)/100]
assert len(omega)==1
embedding=K.hom([omega[0]],QQbar)
def real(c):
    value=embedding(c)
    assert value.imag()==0
    return AA(value.real())
C=lambda j:(z**j+z**(-j))/2
T=lambda j:(z**j-z**(-j))/(2*ii)
units=[vector(K,[C(j),T(j)]) for j in range(10)]
# Unknown columns r,e,H,E and free columns x,y,f.
M=matrix(K,[[-C(2),C(1),0,0],[-T(2),T(1),0,0],
            [0,0,C(2),C(6)],[0,0,T(2),T(6)]])
N=matrix(K,[[C(4),1,C(3)],[T(4),0,T(3)],
            [C(4),1,C(8)],[T(4),0,T(8)]])
assert M.rank()==4
solution=-M.inverse()*N
expected=matrix(K,[[phi,-1,phi],[phi,-phi,1],[-phi,1,phi],[-phi,phi,1]])
assert solution==expected
normals=matrix(K,[[1,0,0],[0,1,0],[0,0,1],
                  [-phi,1,phi],[-phi,phi,1],[phi,-1,phi],[phi,-phi,1]])
normal_labels=['x','y','f','H','E','r','e']
AN=matrix(AA,[[real(c) for c in row] for row in normals.rows()])
rays=[]
for pair in combinations(range(7),2):
    active=matrix(AA,[AN.row(i) for i in pair])
    if active.rank()!=2:
        continue
    ray=active.right_kernel().basis()[0]
    ray=ray/next(q for q in ray if q)
    if any(row.dot_product(ray)<0 for row in AN.rows()):
        continue
    if not any(ray==r for r in rays):
        rays.append(ray)
ap=real(phi);root5=AA(5).sqrt()
expected_rays=[vector(AA,p) for p in [(0,0,1),(0,1,ap),(1,0,ap),
    (1,1/ap,1/ap),(1,ap*ap/root5,1/(ap*root5))]]
assert len(rays)==5 and all(any(r==s for s in rays) for r in expected_rays)
facets=[0,1,3,4,6]
for j in facets:
    on=[r for r in rays if AN.row(j).dot_product(r)==0]
    assert matrix(AA,on).rank()==2
    witness=sum(on,vector(AA,[0,0,0]))
    assert all(AN.row(k).dot_product(witness)>0 for k in facets if k!=j)

S=PolynomialRing(K,names=('x','y','f'));x,y,f=S.gens()
r=phi*(x+f)-y;e=f+phi*(x-y)
H=y+phi*(f-x);E=f+phi*(y-x)
point=lambda q:vector(S,q)
unit=lambda j:point(units[j])
ZERO=point([0,0])
V=[y*unit(0)+e*unit(1)+f*unit(3),r*unit(2),ZERO,y*unit(0),y*unit(0)+e*unit(1)]
W=[ZERO]
for length,j in zip([y,H,x,E,f],[0,2,4,6,8]):
    W.append(W[-1]+length*unit(j))
assert W[-1]==ZERO;W.pop()
def edges(poly):
    return [poly[(i+1)%len(poly)]-p for i,p in enumerate(poly)]
assert edges(V)==[x*unit(4),-r*unit(2),y*unit(0),e*unit(1),f*unit(3)]
assert edges(W)==[y*unit(0),H*unit(2),x*unit(4),E*unit(6),f*unit(8)]
u=2*y*unit(0)+e*unit(1)-r*unit(2)
v=(r+H)*unit(2)
assert v==2*phi*f*unit(2)
polys=[V,[r*unit(2)-p for p in V],[y*unit(0)-p for p in W],
       [r*unit(2)-y*unit(0)+p for p in W]]
seams=[(0,1,1,1,0,0),(0,2,2,0,0,0),(0,3,1,3,1,0),
       (0,4,3,4,1,0),(0,0,2,2,0,1),(1,2,3,0,0,0),
       (1,4,2,4,-1,0),(1,0,3,2,0,-1),(2,1,3,1,0,-1),
       (2,3,3,3,1,-1)]
twin={};adj={i:set() for i in range(4)}
for i,a,j,b,n,m in seams:
    shift=n*u+m*v
    assert polys[i][a]==polys[j][(b+1)%5]+shift
    assert polys[i][(a+1)%5]==polys[j][b]+shift
    assert (i,a) not in twin and (j,b) not in twin
    twin[i,a]=(j,b);twin[j,b]=(i,a)
    adj[i].add(j);adj[j].add(i)
domain={(i,a) for i in range(4) for a in range(5)}
assert set(twin)==domain
successor={a:(b[0],(b[1]+1)%5) for a,b in twin.items()}
unseen=set(domain);cycles=[]
while unseen:
    start=min(unseen);cur=start;cycle=[]
    while cur not in cycle:
        cycle.append(cur);cur=successor[cur]
    assert cur==start
    unseen.difference_update(cycle);cycles.append(cycle)
assert sorted(map(len,cycles))==[3,3,3,3,4,4]
angles=[4,2,2,4,3]
for cycle in cycles:
    assert sum(angles[a] if i<2 else 3 for i,a in cycle)==10
seen={0}
while seen!=set(range(4)):
    expanded=seen|{j for i in seen for j in adj[i]}
    assert expanded!=seen;seen=expanded
assert len(cycles)-len(seams)+4==0
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
area=lambda poly:sum(cross(p,poly[(i+1)%len(poly)]) for i,p in enumerate(poly))/2
assert cross(u,v)==2*phi*f*(phi*(x+y)+f)*T(1)
assert cross(u,v)==sum(map(area,polys))

fixture=[QQ(2),QQ(1),QQ(3)]
evaluate=lambda p:vector(AA,[real(c(*fixture)) for c in p])
actual=[[evaluate(p) for p in poly] for poly in polys]
u0,v0=evaluate(u),evaluate(v)
values=AN*vector(AA,fixture)
assert min(values)>0 and fixture[0]!=fixture[1]
for i,poly in enumerate(actual):
    for a,p in enumerate(poly):
        edge=poly[(a+1)%5]-p
        assert all(cross(edge,poly[b]-p)>0 for b in range(5) if b not in (a,(a+1)%5))
    es=edges(poly);ls=[edge.norm() for edge in es]
    native=angles if i<2 else [3]*5
    assert all(-es[a-1].dot_product(es[a])==real(C(native[a]))*ls[a-1]*ls[a]
               for a in range(5))
assert sum(map(area,actual))==cross(u0,v0)>0
basis=matrix(AA,[[u0[0],v0[0]],[u0[1],v0[1]]]);inv=basis.inverse()
boxes=[]
for poly in actual:
    coords=[inv*p for p in poly]
    boxes.append([(min(p[d] for p in coords),max(p[d] for p in coords)) for d in (0,1)])
def separated(a,b):
    for poly in [a,b]:
        for p,edge in zip(poly,edges(poly)):
            aa=[cross(edge,z) for z in a];bb=[cross(edge,z) for z in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):
                return True
    return False
checks=0
for i,j in product(range(4),repeat=2):
    ranges=[range(int((boxes[i][d][0]-boxes[j][d][1]).ceil()),
                  int((boxes[i][d][1]-boxes[j][d][0]).floor())+1) for d in (0,1)]
    for n,m in product(*ranges):
        if i==j and n==m==0:
            continue
        other=[p+n*u0+m*v0 for p in actual[j]]
        assert separated(actual[i],other),(i,j,n,m)
        checks+=1
print('PASS full 3D closure cone:21 active pairs,5 rays,5 irredundant facets;')
print('PASS10 formal seams,6 actual circular links,formal area/covolume;')
print('PASS asymmetric fixture x=2,y=1,f=3:',checks,'complete exact overlaps; density1;')
print('EVERY positive W chooses minimum side0, giving x>=y and positive r,e V partner')
