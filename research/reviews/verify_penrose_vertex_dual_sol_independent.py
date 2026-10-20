#!/usr/bin/env python3
"""Independent certificate audit; no producer import, SciPy, or clipping."""
import json
from collections import Counter,defaultdict
from sage.all import CyclotomicField, QQbar, AA, QQ
K=CyclotomicField(10); z=K.gen(); E=K.hom([QQbar.zeta(10)]); f=z+z**-1
sg=lambda a: AA(E(a)).sign()
dot=lambda a,b:(a*b.conjugate()+a.conjugate()*b)/2
N=lambda a:dot(a,a)
det=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def decode(v): return sum((QQ(x)*z**i for i,x in enumerate(v)),K(0))
T=[(0,K(0),z**(j+(j%2==0)),z**(j+(j%2!=0))) for j in range(10)]
seed=None
for level in range(5):
    U=[]
    for kind,a,b,c in T:
        if kind==0:
            p=a+(b-a)/f
            children=[(0,c,p,b),(1,p,c,a)]
        else:
            q=b+(a-b)/f; r=b+(c-b)/f
            children=[(1,r,c,a),(1,q,r,b),(0,r,q,a)]
        assert sum(sg(det(v-u,w-u))*det(v-u,w-u) for _,u,v,w in children)==sg(det(b-a,c-a))*det(b-a,c-a)
        U.extend(children)
    T=U
    if level==0: seed={(k,a*f,b*f,c*f) for k,a,b,c in T}
T=[(k,a*f**5,b*f**5,c*f**5) for k,a,b,c in T]
assert seed<=set(T)
G=defaultdict(list)
for t in T: G[frozenset(t[2:])].append(t)
R=[]
for group in G.values():
    assert len(group) in (1,2)
    if len(group)==1:
        _,a,b,c=group[0]
        assert any(det(f**5*z**((j+1)%10)-f**5*z**j,b-f**5*z**j)==0 and det(f**5*z**((j+1)%10)-f**5*z**j,c-f**5*z**j)==0 for j in range(10))
        continue
    (k,a,b,c),(l,d,e,g)=group
    assert k==l and (b,c)==(e,g)
    assert sg(det(c-b,a-b))*sg(det(c-b,d-b))==-1
    poly=[a,b,d,c]
    assert all(N(poly[(j+1)%4]-poly[j])==1 for j in range(4))
    R.append(poly)
S=set(v for p in R for v in p)
assert len(R)==430 and len(S)==476
edges=Counter(frozenset((p[j],p[(j+1)%4])) for p in R for j in range(4))
assert set(edges.values())<={1,2}
B=[tuple(e) for e,n in edges.items() if n==1]
def distance(c,a,b):
    t=dot(c-a,b-a)/N(b-a)
    t=K(0) if sg(t)<0 else K(1) if sg(t-1)>0 else t
    return N(c-a-t*(b-a))
D=json.load(open('research/searches/penrose-vertex-dual-gate-sol-2026-10-19.json'))
for W in D['witnesses']:
    c=decode(W['site']); P=list(map(decode,W['vertices_relative']))
    assert c in S and len(P)==W['sides'] and len(set(P))==len(P)
    margin=min((distance(c,a,b) for a,b in B),key=lambda x:AA(E(x)))
    assert margin==decode(W['boundary_distance_squared']) and sg(margin-9)>0
    assert all(sg(det(P[(j+1)%len(P)]-P[j],P[(j+2)%len(P)]-P[(j+1)%len(P)]))>0 for j in range(len(P)))
    # Every claimed edge is a genuine distinct site's bisector. Together with
    # all-site feasibility, these supports prove equality with the cell.
    supports=[]
    for a,b in zip(P,P[1:]+P[:1]):
        active=[q for q in S-{c} if 2*dot(q-c,a)==N(q-c) and 2*dot(q-c,b)==N(q-c)]
        assert len(active)==1
        supports.extend(active)
    assert len(set(supports))==len(P)
    assert all(sg(2*dot(q-c,v)-N(q-c))<=0 for q in S for v in P)
    assert all(sg(N(v)-1)<0 for v in P)
    assert [N(v) for v in P]==list(map(decode,W['radius_squared']))
    assert sum(sg(N(q-c)-9)<=0 for q in S-{c})==W['neighbors_checked']
    print('verified',len(P),'sides; active supports',len(supports),'margin',margin)
print('independent source reconstruction and three all-patch-site cells PASS')
