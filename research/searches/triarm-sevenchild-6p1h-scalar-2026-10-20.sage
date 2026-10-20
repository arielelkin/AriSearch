"""UNFINISHED / SUPERSEDED diagnostic. Do not use as a certificate.

The independently reviewed seven-child mixed-pentagon topology obstruction
excludes tP=6P+H before this scalar search. Its run was interrupted.
See research/reviews/seven-child-mixed-hostile-2026-10-20.md.
"""
from sage.all import *
from itertools import combinations
Qz=PolynomialRing(QQ,'z'); z=Qz.gen()
K=NumberField(z**4-6*z*z-3,'t',embedding=2.54); t=K.gen()
assert t>0 and t**4==6*t*t+3
eq={}
counts=[(i,j,k) for i in range(7) for j in range(7-i) for k in range(7-i-j)]
assert len(counts)==84
for target in ('one','a','b'):
    rows=[]
    for i,j,k in counts:
        for h in range(3):
            c0,ca,cb=K(i),K(j),K(k)
            if h==1: cb+=1/t
            if h==2: ca+=2/t
            if target=='one': c0-=t
            elif target=='a': ca-=t
            else: cb-=t
            rows.append((c0,ca,cb))
    eq[target]=rows
    assert len(rows)==252
def key(e):
    q=next(c for c in e if c)
    return tuple(c/q for c in e)
assert not set(map(key,eq['one'])).intersection(map(key,eq['a'])).intersection(map(key,eq['b']))
def solve(e,f):
    u,v,w=e; U,V,W=f; d=v*W-V*w
    if d==0: return None
    return ((-u*W+U*w)/d,(-v*U+V*u)/d)
q3=AA(3).sqrt()
def feasible(a,b):
    af,bf=float(a),float(b)
    if af < -1e-8 or bf < -1e-8 or af+bf < 3**0.5-1e-8 or abs(af-bf)>3**0.5+1e-8:
        return False
    ar,br=AA(a),AA(b)
    return ar>0 and br>0 and ar+br>=q3 and abs(ar-br)<=q3
metrics=set()
for p,q in combinations(eq,2):
    third=next(s for s in eq if s not in (p,q))
    for e in eq[p]:
        for f in eq[q]:
            ab=solve(e,f)
            if ab is None or not feasible(*ab): continue
            a,b=ab
            if any(u+v*a+w*b==0 for u,v,w in eq[third]): metrics.add(ab)
print('positive circle-feasible scalar metrics',len(metrics))
q3=AA(3).sqrt()
R=lambda p:(-p[0]/2-q3*p[1]/2,q3*p[0]/2-p[1]/2)
add=lambda p,q:(p[0]+q[0],p[1]+q[1]);sub=lambda p,q:(p[0]-q[0],p[1]-q[1])
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
def convex(poly):
    return all(cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))>0 for i in range(len(poly)))
convex_metrics=[]
for a,b in sorted(metrics,key=lambda q:(float(AA(q[0])),float(AA(q[1])))):
    ar,br=AA(a),AA(b); y=(ar*ar+3-br*br)/(2*q3); x2=ar*ar-y*y
    branches=[]
    for s in ((1,) if x2==0 else (-1,1)):
        v=(s*x2.sqrt(),y);O=(AA(0),AA(0));S=(AA(1),AA(0));T=R(S)
        V=add(S,v);W=sub(T,R(v));P=[O,S,V,W,T]
        G=[V,W,R(V),R(W),R(R(V)),R(R(W))]
        if convex(P) and convex(G): branches.append(s)
    if branches:
        convex_metrics.append((a,b,branches))
        print('SURVIVOR',a,b,branches)
print('strictly convex scalar metrics',len(convex_metrics))
