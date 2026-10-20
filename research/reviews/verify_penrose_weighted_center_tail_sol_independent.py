#!/usr/bin/env python3
"""Independent certificate verifier; no import of either producer.
Replay with the repository mise/conda wrapper and Python.
Uses real Q(sqrt(5)) coordinate pairs, not cyclotomic intersection code.
"""
import json
from collections import defaultdict, Counter
from pathlib import Path
from sage.all import QuadraticField, AA, QQ
F=QuadraticField(5, 'r', embedding=AA(5).sqrt()); r=F.gen()
phi=(1+r)/2; metric=(3-phi)/4
zero=(F(0),F(0))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(a,t): return (a[0]*t,a[1]*t)
def dot(a,b): return a[0]*b[0]+metric*a[1]*b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def norm(a): return dot(a,a)
def sg(a): return (AA(a)>0)-(AA(a)<0)
def mul_w(a): return (a[0]*phi/2-a[1]*metric,a[0]+a[1]*phi/2)
powers=[(F(1),F(0))]
for _ in range(10): powers.append(mul_w(powers[-1]))
assert powers[10]==powers[0]
tri=[]
for j in range(10):
    b,c=powers[j:j+2]
    if j%2==0: b,c=c,b
    tri.append((0,zero,b,c))
levels={}
for level in range(6):
    if level in (1,5): levels[level]=[(t,*(scale(v,phi**level) for v in (a,b,c))) for t,a,b,c in tri]
    nxt=[]
    for t,a,b,c in tri:
        if t==0:
            d=add(a,scale(sub(b,a),1/phi))
            nxt.extend([(0,c,d,b),(1,d,c,a)])
        else:
            d=add(b,scale(sub(a,b),1/phi)); e=add(b,scale(sub(c,b),1/phi))
            nxt.extend([(1,e,c,a),(1,d,e,b),(0,e,d,a)])
    tri=nxt
assert len(levels[1])==20 and len(levels[5])==890
assert set(levels[1])<=set(levels[5])
pairs=defaultdict(list)
for t,a,b,c in levels[5]:
    assert norm(sub(a,b))==norm(sub(a,c))==1
    assert norm(sub(b,c))==[2-phi,1+phi][t]
    pairs[frozenset((b,c))].append((t,a,b,c))
rh=[]
def onseg(p,a,b): return det(sub(b,a),sub(p,a))==0 and sg(dot(sub(p,a),sub(p,b)))<=0
outer=[scale(v,phi**5) for v in powers[:10]]
for pair in pairs.values():
    assert len(pair) in (1,2)
    if len(pair)==1:
        _,_,b,c=pair[0]
        assert any(onseg(b,x,y) and onseg(c,x,y) for x,y in zip(outer,outer[1:]+outer[:1]))
        continue
    t,a,b,c=pair[0]; u,d,e,f=pair[1]
    assert (t,b,c)==(u,e,f)
    assert sg(det(sub(c,b),sub(a,b)))*sg(det(sub(c,b),sub(d,b)))==-1
    v=[a,b,d,c]
    assert all(norm(sub(v[(j+1)%4],v[j]))==1 for j in range(4))
    rh.append((t,v))
assert len(rh)==430
centers=[scale(tuple(map(sum,zip(*v))),QQ(1)/4) for _,v in rh]
assert len(set(centers))==430

D=json.loads(Path('research/searches/penrose-weighted-center-tail-gate-sol-2026-10-19.json').read_text())
def real(p): return F(QQ(p[0])+QQ(p[1])*phi)
def point(p): return tuple(real(v) for v in p)
def intersection(d,e):
    A,B=d[0],metric*d[1]; C,E=e[0],metric*e[1]
    u,v=norm(d)/2,norm(e)/2
    return ((u*E-B*v)/(A*E-B*C),(A*v-u*C)/(A*E-B*C))
edges=Counter(frozenset((v[k],v[(k+1)%4])) for _,v in rh for k in range(4))
assert set(edges.values())=={1,2}
for cert,typ,idx,supports in zip(D['witnesses'],[1,0],[25,26],[[24,70,328,413],[29,72,116,374]]):
    assert cert['index']==idx and cert['type']==rh[idx][0]==typ
    order=sorted((i for i in range(430) if rh[i][0]==typ),key=lambda i:(AA(norm(centers[i])),i))
    assert order[0]==idx and D['scanned'][str(typ)]==[[idx,4]]
    c=centers[idx]
    # Check exported cyclotomic center by evaluating w powers in real coordinates.
    exported=zero
    for k,a in enumerate(cert['center_cyclotomic']): exported=add(exported,scale(powers[k],QQ(a)))
    assert exported==c
    assert cert['supports']==supports
    ds=[sub(centers[j],c) for j in supports]
    # Independent line intersection, not a replay of clipping.
    V=[intersection(ds[k-1],ds[k]) for k in range(4)]
    assert V==[point(p) for p in cert['vertices_xy']]
    assert len(set(V))==4
    assert all(sg(det(sub(V[(k+1)%4],V[k]),sub(V[(k+2)%4],V[(k+1)%4])))>0 for k in range(4))
    for k,j in enumerate(supports):
        assert rh[j][0]==typ
        assert all(2*dot(ds[k],V[t])==norm(ds[k]) for t in [k,(k+1)%4])
    assert all(sg(norm(sub(q,c))-2*dot(sub(q,c),v))>=0 for j,q in enumerate(centers) if rh[j][0]==typ for v in V)
    vals=[(2*dot(sub(q,c),v)-norm(sub(q,c)),k,j) for k,v in enumerate(V) for j,q in enumerate(centers) if rh[j][0]!=typ]
    worst=max((a for a,k,j in vals),key=AA)
    assert worst==real(cert['finite_worst_deficit'])
    assert [[k,j] for a,k,j in vals if a==worst]==cert['limiting_pairs']
    endpoint=real(cert['threshold']); assert endpoint==(worst if typ else -worst)
    assert sg(worst)>0
    assert all(sg(norm(sub(q,c))-2*dot(sub(q,c),v)+(typ-rh[j][0])*endpoint)>=0 for j,q in enumerate(centers) for v in V)
    radius=max(map(norm,V),key=AA); assert radius==real(cert['radius_squared'])
    def distance(edge):
        a,b=tuple(edge); ab=sub(b,a); ac=sub(c,a); t=dot(ac,ab)/norm(ab)
        if sg(t)<0:return norm(ac)
        if sg(t-1)>0:return norm(sub(c,b))
        return norm(sub(ac,scale(ab,t)))
    margin=min((distance(e) for e,n in edges.items() if n==1),key=AA)
    assert margin==real(cert['boundary_distance_squared']) and sg(margin-4*radius)>0
    print('PASS independent exact witness',idx,'type',typ,'endpoint',endpoint,'R2',radius,'M',margin)
assert real(D['witnesses'][0]['threshold'])==QQ(1)/4+phi/3
thin=real(D['witnesses'][1]['threshold']); assert thin==-QQ(21)/44-9*phi/22
assert sg(-QQ(1)/4-thin)>0
assert -QQ(1)/4-thin==QQ(5)/22+9*phi/22
assert D['uncovered_gaps']==[dict(lower=['-21/44','-9/22'],upper=['-1/4','0'],lower_included=False,upper_included=False)]
print('PASS source, ordering, all-site endpoints, exact gap and favorable tail signs')
