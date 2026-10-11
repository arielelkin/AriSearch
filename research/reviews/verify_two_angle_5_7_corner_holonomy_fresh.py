#!/usr/bin/env python3
"""Fresh complex-native-walk corner/holonomy audit, independent of author code.

Complements the earlier full-domain checker by rebuilding native clockwise
P from side vectors and retaining exact zero lattice holonomy of CCW links.
"""
import json
from pathlib import Path
from sage.all import CyclotomicField, PolynomialRing, QQ, QQbar

K=CyclotomicField(14)
zeta=K.gen()
z=zeta**2
t=zeta+zeta**-1
assert QQbar(zeta).imag()>0 and QQ(18)/10<QQbar(t).real()<QQ(181)/100
R=PolynomialRing(K,("a","b","c","d"))
a,b,c,d=R.gens()
l3=t*d-(t*t-1)*b/2+c/2
l5=(t-1)*a+b/2+(-t*t+t+1)*c/2
l0=(-t*t+t+1)*a+(t*t/2-t-K(1)/2)*b+(t-K(1)/2)*c+d
p=(t*t-t-1)*a-(t*t-1)*b/2+c/2+d
lengths=[l0,a,b,l3,c,l5,d]
H=[R(0)]
for j,length in enumerate(lengths):
    H.append(H[-1]+length*z**j)
assert H.pop()==0
P=[H[6]]
for length,direction in zip([d,a,l3,l5,p],[12,9,6,3,0]):
    P.append(P[-1]+length*zeta**direction)
assert P.pop()==H[6]
ds={j:H[j]+H[(j+1)%7] for j in(0,2,4)}
u,v=ds[2]-ds[0],ds[4]-ds[0]
q=ds[0]-ds[2]+ds[4]
faces=[H,[ds[0]-w for w in H],P,[q-w for w in P]]
# Normalize clockwise native P lists to CCW while fixing native vertex0.
ccw=[faces[j] if j<2 else [faces[j][-k%5] for k in range(5)] for j in range(4)]
def conj(poly):
    return R({tuple(m):c.conjugate() for m,c in R(poly).dict().items()})
def normalized_cross(x,y):
    return (conj(x)*y-x*conj(y))/(zeta-zeta.conjugate())
def normalized_area(p):
    return sum(normalized_cross(p[j],p[(j+1)%len(p)]) for j in range(len(p)))/2
assert sum(map(normalized_area,ccw))==normalized_cross(u,v)
seams=json.loads((Path(__file__).parents[1]/"certificates"/"two-angle-5-7-metric-continuum.json").read_text())["formal_geometry"]["seam_table"]
mate,shifts={},{}
for i,h,j,g,n,m,reverse in seams:
    aa=[faces[i][h],faces[i][(h+1)%len(faces[i])]]
    bb=[faces[j][g]+n*u+m*v,faces[j][(g+1)%len(faces[j])]+n*u+m*v]
    if reverse:
        bb.reverse()
    assert aa==bb
    hi=h if i<2 else(-h-1)%5
    gj=g if j<2 else(-g-1)%5
    assert ccw[i][hi]==ccw[j][(gj+1)%len(ccw[j])]+n*u+m*v
    assert ccw[i][(hi+1)%len(ccw[i])]==ccw[j][gj]+n*u+m*v
    mate[i,hi],mate[j,gj]=(j,gj),(i,hi)
    shifts[i,hi],shifts[j,gj]=(n,m),(-n,-m)
unseen,links=set(mate),[]
while unseen:
    start=min(unseen)
    current,link,shift=start,[],[0,0]
    while current not in link:
        assert current in unseen
        unseen.remove(current)
        link.append(current)
        shift=[shift[k]+shifts[current][k] for k in range(2)]
        j,g=mate[current]
        current=j,(g+1)%len(ccw[j])
    assert current==start and shift==[0,0]
    assert sorted(5 if i<2 or h==0 else 4 for i,h in link)==[4,5,5]
    links.append(link)
assert len(links)==8 and all(len(link)==3 for link in links)
print("PASS fresh native P closure, full polynomial area identity,8 actual circular links and zero lattice holonomy")
