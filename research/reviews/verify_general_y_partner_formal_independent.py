#!/usr/bin/env python3
"""Fresh formal all-metrics Y-partner audit, no author imports.
Scale coordinates by h to keep polynomial arithmetic; reduce by h^2+k^2=1.
Reconstruct native positive walks and cancel actual oriented boundary edges.
"""
from collections import Counter
from sage.all import PolynomialRing, QQ
R=PolynomialRing(QQ,('k','h','l1','l2','l3','lam'))
k,h,l1,l2,l3,lam=R.gens();ideal=R.ideal(h*h+k*k-1)
red=lambda a:ideal.reduce(R(a))
pt=lambda a,b:(red(a),red(b))
add=lambda a,b:pt(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:pt(a[0]-b[0],a[1]-b[1])
scale=lambda a,c:pt(a[0]*c,a[1]*c)
cross=lambda a,b:red(a[0]*b[1]-a[1]*b[0])
zero=pt(0,0)

def chain(edges):
    vertices=[zero]
    for edge in edges:vertices.append(add(vertices[-1],edge))
    assert vertices.pop()==zero
    return vertices

def main():
    d=1-2*k*k
    units=[pt(1,0),pt(k,h),pt(-h,k),pt(-2*k*h,-d),pt(0,-1)]
    assert all(red(a*a+b*b)==1 for a,b in units)
    l0=h*l2+2*k*h*l3-k*l1
    l4=h*l1+k*l2-d*l3
    P=chain([scale(u,h*length) for u,length in zip(units,[l0,l1,l2,l3,l4])])
    hd2=k*lam-k*l1+l0;hd4=l1+d*lam-k*l0
    # Native Q directions are e4,-e2,e1,-w,-e0.
    Q=chain([scale(units[4],hd4),scale(units[2],-hd2),
             scale(units[1],h*l1),pt(-h*k*lam,h*h*lam),scale(units[0],-h*l0)])
    assert Q[4]==P[1] and Q[3]==add(P[1],pt(h*k*lam,-h*h*lam))
    center_twice=add(Q[3],Q[4]);star=lambda p:sub(center_twice,p)
    motifs=[P,Q,list(map(star,P)),list(map(star,Q))]
    edges=Counter((poly[i],poly[(i+1)%5]) for poly in motifs for i in range(5))
    canceled=0
    for a,b in list(edges):
        count=min(edges[a,b],edges[b,a]);edges[a,b]-=count;edges[b,a]-=count;canceled+=count
    assert canceled==5
    boundary=[edge for edge,count in edges.items() for _ in range(count)]
    assert len(boundary)==10
    successor=dict(boundary);assert len(successor)==10 and set(successor)==set(successor.values())
    cycle=[P[3]]
    while successor[cycle[-1]]!=cycle[0]:
        nxt=successor[cycle[-1]];assert nxt not in cycle;cycle.append(nxt)
    assert len(cycle)==10
    carrier=[cycle[i] for i in range(10) if cross(sub(cycle[i],cycle[i-1]),sub(cycle[(i+1)%10],cycle[i]))!=0]
    assert carrier==[P[3],P[4],Q[1],star(P[3]),star(P[4]),star(Q[1])]
    x=scale(units[3],h*l3)
    y=scale(units[4],h*l4+hd4)
    z=scale(units[2],-h*l2-hd2)
    assert [sub(carrier[(i+1)%6],carrier[i]) for i in range(6)]==[x,y,z,scale(x,-1),scale(y,-1),scale(z,-1)]
    u,v=add(x,y),add(y,z)
    area=lambda poly:red(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2)
    assert area(carrier)==cross(u,v)==sum(area(poly) for poly in motifs)
    assert cross(u,v)==red(cross(x,y)+cross(x,z)+cross(y,z))
    # Direct exact opposite side translations and the actual two vertex links.
    for i,j,n,t in [(0,3,0,-1),(1,4,1,-1),(2,5,1,0)]:
        shift=add(scale(u,n),scale(v,t))
        assert carrier[i]==add(carrier[(j+1)%6],shift)
        assert carrier[(i+1)%6]==add(carrier[j],shift)
    print('PASS independent formal Y walks,5 canceled seams,10-edge exterior cycle,positive-direction carrier identities,area determinant and opposite-side periods')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
