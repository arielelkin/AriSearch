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
D=json.loads(Path('research/searches/penrose-weighted-center-first-gate-sol-2026-10-19.json').read_text())
def real(p): return F(QQ(p[0])+QQ(p[1])*phi)
def point(p): return tuple(real(v) for v in p)
V=[(point(p['constant']),point(p['delta_coefficient'])) for p in D['vertices_affine_xy']]
lo,hi=map(real,D['finite_constraint_interval'])
assert lo==-QQ(1)/4 and hi==QQ(1)/4+phi/3
idx=D['source_index']; c=centers[idx]; assert idx==23 and rh[idx][0]==D['source_type']==0
# Base lengths distinguish actual thin (acute angle 36 degrees) and thick
# (acute angle 72 degrees) rhombs; this is not an assumed color convention.
assert norm(sub(rh[idx][1][1],rh[idx][1][3]))==2-phi
supports=D['supports']; assert supports==[21,68,18,22]
# All 1720 affine residuals: check endpoints and recover the exact maximal
# interval of their simultaneous validity, including every limiting pair.
lower=[]; upper=[]; hits=[[],[]]
for vi,(a,b) in enumerate(V):
    for j,q in enumerate(centers):
        d=sub(q,c); wt=rh[idx][0]-rh[j][0]
        A=norm(d)-2*dot(d,a); B=wt-2*dot(d,b)
        assert sg(A+B*lo)>=0 and sg(A+B*hi)>=0
        if B:
            root=-A/B
            (lower if sg(B)>0 else upper).append(root)
            if root==lo and sg(B)>0: hits[0].append([vi,j])
            if root==hi and sg(B)<0: hits[1].append([vi,j])
assert max(lower,key=AA)==lo and min(upper,key=AA)==hi
assert hits==D['limiting_vertex_site_pairs']
for k,j in enumerate(supports):
    d=sub(centers[j],c); wt=rh[idx][0]-rh[j][0]
    for vi in (k,(k+1)%4):
        a,b=V[vi]
        assert 2*dot(d,a)==norm(d) and 2*dot(d,b)==wt
# Direct quadratic minimum test, independent of producer's Bernstein test.
for k in range(4):
    aa=sub(V[(k+1)%4][0],V[k][0]); ab=sub(V[(k+1)%4][1],V[k][1])
    ba=sub(V[(k+2)%4][0],V[(k+1)%4][0]); bb=sub(V[(k+2)%4][1],V[(k+1)%4][1])
    C=det(aa,ba); B=det(aa,bb)+det(ab,ba); A=det(ab,bb)
    f=lambda t:A*t*t+B*t+C
    assert sg(f(lo))>0 and sg(f(hi))>=0
    if sg(A)>0:
        critical=-B/(2*A)
        if sg(critical-lo)>0 and sg(hi-critical)>0: assert sg(f(critical))>0
assert len(set(add(a,scale(b,lo)) for a,b in V))==4
assert len(set(add(a,scale(b,hi)) for a,b in V))<4
assert all(sg(1-norm(add(a,scale(b,t))))>0 for a,b in V for t in (lo,hi))
edges=Counter(frozenset((v[k],v[(k+1)%4])) for _,v in rh for k in range(4))
assert set(edges.values())=={1,2}
def distance(a,b):
    ab=sub(b,a); ac=sub(c,a); t=dot(ac,ab)/norm(ab)
    if sg(t)<0: return norm(ac)
    if sg(t-1)>0: return norm(sub(c,b))
    return norm(sub(ac,scale(ab,t)))
margin=min((distance(*tuple(e)) for e,n in edges.items() if n==1),key=AA)
assert margin==real(D['source_boundary_distance_squared'])==7+37*phi/4
assert sg(margin-9)>0 and sg(lo+1)>0 and sg(1-hi)>0
print('PASS: independent 1720 residuals, maximal support interval, strict turns, endpoints, geometric types and collar')
