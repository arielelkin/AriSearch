#!/usr/bin/env python3
"""Exact geometric checker for the retained marked-rhomb three-star fixture."""
import json
from pathlib import Path
from sage.all import CyclotomicField, QQbar, AA

K=CyclotomicField(10)
w=K.gen()
emb=K.hom([QQbar.zeta(10)])
def decode(v):
    return sum(K(c)*w**i for i,c in enumerate(v))
def cross(a,b):
    return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(z):
    return AA(emb(z))

data=json.loads(Path('research/reviews/penrose-boundary-dual-trivalent-star.json').read_text())
v=decode(data['central_vertex'])
polys=[[decode(x) for x in r['vertices']] for r in data['rhombs']]
centers=[sum(P)/4 for P in polys]
assert len(set(centers))==3
for record,P in zip(data['rhombs'],polys):
    assert P[record['central_corner']]==v
    assert all((P[(i+1)%4]-P[i])*(P[(i+1)%4]-P[i]).conjugate()==1 for i in range(4))
    assert P[0]+P[2]==P[1]+P[3]
    assert all(sign(cross(P[i]-P[i-1],P[(i+1)%4]-P[i]))>0 for i in range(4))
    j=record['central_corner']
    a=P[j-1]-v
    b=P[(j+1)%4]-v
    cosine=(a.conjugate()*b+a*b.conjugate())/2
    phi=w+w**-1
    assert cosine==(-phi/2 if record['kind']=='thin' else (phi-1)/2)

# Each pair shares one radial source edge; midpoint centers intersect it
# strictly between both centers and strictly inside the source edge.
crossings=[]
for i,j in ((0,1),(1,2),(2,0)):
    common=set(polys[i])&set(polys[j])
    assert len(common)==2 and v in common
    b=next(x for x in common if x!=v)
    a=centers[i]
    d=centers[j]-a
    e=b-v
    assert sign(cross(e,centers[i]-v))*sign(cross(e,centers[j]-v))<0
    lam=cross(v-a,e)/cross(d,e)
    q=a+lam*d
    mu=cross(a-v,d)/cross(e,d)
    assert q==v+mu*e
    assert 0<sign(lam)<1 and 0<sign(mu)<1
    crossings.append(q)

orient=sign(cross(centers[1]-centers[0],centers[2]-centers[0]))
assert orient!=0
assert all(sign(cross(centers[(i+1)%3]-centers[i],v-centers[i]))*orient>0 for i in range(3))
print('PASS: exact legal three-rhomb fixture; centered dual cell is a genuine triangle containing the source vertex.')
