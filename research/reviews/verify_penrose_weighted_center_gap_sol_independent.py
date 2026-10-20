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

D=json.loads(Path('research/searches/penrose-weighted-center-gap-witness-sol-2026-10-19.json').read_text())
W=D['witness']; c=centers[25]; typ=rh[25][0]
def real(p): return F(QQ(p[0])+QQ(p[1])*phi)
def point(p): return tuple(real(v) for v in p)
V=[(point(v['constant']),point(v['delta_coefficient'])) for v in W['vertices_affine_xy']]
lo=-QQ(1)/4-phi/2; hi=-QQ(1)/44-2*phi/11; sample=-QQ(3)/4
assert D['scanned_indices']==[25] and sorted(range(430),key=lambda j:(AA(norm(centers[j])),j))[0]==25
assert typ==W['type']==1 and W['index']==25 and W['supports']==[26,70,328,374]
assert [real(t) for t in W['maximal_finite_affine_support_interval']]==[lo,hi]
exported=zero
for k,a in enumerate(W['center_cyclotomic']): exported=add(exported,scale(powers[k],QQ(a)))
assert exported==c
roots=[[],[]]
for k,(a,b) in enumerate(V):
    for j,q in enumerate(centers):
        d=sub(q,c); A=2*dot(d,a)-norm(d); B=2*dot(d,b)-(typ-rh[j][0])
        assert sg(A+B*sample)<=0
        assert all(sg(A+B*t)<=0 for t in (lo,hi))
        if B: roots[1 if sg(B)>0 else 0].append((-A/B,k,j))
assert max((t for t,k,j in roots[0]),key=AA)==lo
assert min((t for t,k,j in roots[1]),key=AA)==hi
assert [[[k,j] for t,k,j in row if t==bound] for row,bound in zip(roots,[lo,hi])]==W['limiting_pairs']
for k,j in enumerate(W['supports']):
    d=sub(centers[j],c)
    for t in (k,(k+1)%4):
        a,b=V[t]
        assert 2*dot(d,a)==norm(d) and 2*dot(d,b)==typ-rh[j][0]
def vertices(t): return [add(a,scale(b,t)) for a,b in V]
def turn(k,t):
    vs=vertices(t)
    return det(sub(vs[(k+1)%4],vs[k]),sub(vs[(k+2)%4],vs[(k+1)%4]))
for k in range(4):
    # Direct quadratic coefficients in normalized interval coordinate u.
    f0=turn(k,lo); fm=turn(k,(lo+hi)/2); f1=turn(k,hi)
    a=2*(f1+f0-2*fm); b=f1-f0-a
    assert f0==0 and sg(f1)>0 and sg(fm)>0
    # Factor u*(a*u+b): linear factor positive for 0<u<=1.
    assert sg(b)>=0 and sg(a+b)>0
    assert turn(k,sample)>0
assert len(set(vertices(hi)))==4
assert W['endpoint_included']==[False,True]
edges=Counter(frozenset((v[k],v[(k+1)%4])) for _,v in rh for k in range(4))
assert set(edges.values())=={1,2}
def distance(edge):
    a,b=tuple(edge); ab=sub(b,a); ac=sub(c,a); t=dot(ac,ab)/norm(ab)
    if sg(t)<0:return norm(ac)
    if sg(t-1)>0:return norm(sub(c,b))
    return norm(sub(ac,scale(ab,t)))
margin=min((distance(e) for e,n in edges.items() if n==1),key=AA)
assert margin==QQ(93)/4+149*phi/4==real(W['boundary_distance_squared']) and sg(margin-64)>0
assert all(sg(norm(v)-4)<0 for t in (lo,hi) for v in vertices(t))
assert all(sg(norm(v)-1)<0 for v in vertices(sample))
assert sg(lo+2)>0 and sg(2-hi)>0
A=-QQ(21)/44-9*phi/22
assert sg(lo-A)>0 and sg(-QQ(1)/4-hi)>0
print('PASS independent real-field source, all 1720 affine residuals at both endpoints, exact maximal roots, support facets, strict turns, endpoints, uniform tail and remaining gaps')
print('lower gap length',lo-A,'upper gap length',-QQ(1)/4-hi)
