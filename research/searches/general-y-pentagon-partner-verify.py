#!/usr/bin/env python3
"""Exact checks of the central-hexagon partner construction for two Y metrics.

The analytic all-metrics proof is in general-y-pentagon-periodic-partner.md.
This finite coordinate check does not import earlier authors' arithmetic or
any periodic-quotient search. Complete overlap domain is derived from exact
lattice-coordinate bounds, not a fixed diagnostic window.
"""
from itertools import product
from sage.all import AA, QQ, matrix, vector

ZERO=vector(AA,[0,0])

def det(u,v):
    return u[0]*v[1]-u[1]*v[0]

def edges(poly):
    return [poly[(i+1)%len(poly)]-z for i,z in enumerate(poly)]

def area(poly):
    return sum(det(z,poly[(i+1)%len(poly)]) for i,z in enumerate(poly))/2

def convex(poly):
    for i,e in enumerate(edges(poly)):
        assert all(det(e,poly[j]-poly[i]) > 0 for j in range(len(poly))
                   if j not in (i,(i+1)%len(poly)))

def separated(poly,other):
    return any(all(det(e,z-poly[i]) <= 0 for z in other)
               for i,e in enumerate(edges(poly)))

def angle_cosines(poly):
    es=edges(poly)
    ls=[e.norm() for e in es]
    return [-es[i-1].dot_product(es[i])/(ls[i-1]*ls[i])
            for i in range(len(poly))]

def audit(k):
    h=(1-k*k).sqrt()
    d=1-2*k*k
    assert 0 < k < AA(2).sqrt()/2 and d > 0
    unit=[vector(AA,z) for z in [(1,0),(k,h),(-h,k),(-2*k*h,-d),(0,-1)]]
    assert all(e.dot_product(e)==1 for e in unit)
    L1,L2,L3=map(AA,[2,3,1])
    L0=h*L2+2*k*h*L3-k*L1
    L4=h*L1+k*L2-d*L3
    lengths=[L0,L1,L2,L3,L4]
    assert all(L > 0 for L in lengths)
    P=[ZERO]
    for L,e in zip(lengths,unit):
        P.append(P[-1]+L*e)
    assert P[-1] == ZERO
    P.pop()
    convex(P)
    assert angle_cosines(P)==[AA(0),-k,AA(0),-k,-d]
    b=d/(2*k)
    assert L2 != b*L3+h*(L1-h*L3)/b  # Outside old 2D closure subfamily.
    lam=sum(lengths)+k*L0/d
    delta2=(k*lam-k*L1+L0)/h
    delta4=(L1+d*lam-k*L0)/h
    assert delta2 > 0 and delta4 > 0 and lam > max(lengths)
    A=P[1]
    B=A+lam*vector(AA,[k,-h])
    C=(A+B)/2
    opposite=lambda z:2*C-z
    Q=[P[0],P[0]+delta4*unit[4],opposite(P[2]),B,A]
    assert edges(Q)==[delta4*unit[4],-delta2*unit[2],L1*unit[1],
                      -lam*vector(AA,[k,-h]),-L0*unit[0]]
    convex(Q)
    assert angle_cosines(Q)==[AA(0),-k,AA(0),-d,-k]
    assert lam not in lengths
    motif=[P,Q,list(map(opposite,P)),list(map(opposite,Q))]
    remaining=[]
    for poly in motif:
        for i,a in enumerate(poly):
            b=poly[(i+1)%len(poly)]
            if (b,a) in remaining:
                remaining.remove((b,a))
            else:
                remaining.append((a,b))
    boundary=[P[3],P[4],P[0],Q[1],opposite(P[2]),opposite(P[3]),
              opposite(P[4]),opposite(P[0]),opposite(Q[1]),P[2]]
    for i,a in enumerate(boundary):
        remaining.remove((a,boundary[(i+1)%len(boundary)]))
    assert not remaining  # Exact four-face boundary-chain cancellation.
    H=[P[3],P[4],Q[1],opposite(P[3]),opposite(P[4]),opposite(Q[1])]
    convex(H)
    assert angle_cosines(H)==[-k,-d,-k,-k,-d,-k]
    x=L3*unit[3]
    y=(L4+delta4)*unit[4]
    z=-(L2+delta2)*unit[2]
    assert edges(H)==[x,y,z,-x,-y,-z]
    assert all(det(s,t)>0 for s,t in [(x,y),(x,z),(y,z)])
    u,v=x+y,y+z
    M=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    assert M.det() == area(H) == sum(map(area,motif)) > 0
    inv=M.inverse()
    boxes=[]
    for poly in motif:
        coords=[inv*p for p in poly]
        boxes.append([(min(p[d] for p in coords),max(p[d] for p in coords))
                      for d in (0,1)])
    comparisons=0
    for f,g in product(range(4),repeat=2):
        ranges=[range(int((boxes[f][d][0]-boxes[g][d][1]).ceil()),
                      int((boxes[f][d][1]-boxes[g][d][0]).floor())+1)
                for d in (0,1)]
        for n,r in product(*ranges):
            if f==g and n==r==0:
                continue
            shifted=[p+n*u+r*v for p in motif[g]]
            assert separated(motif[f],shifted) or separated(shifted,motif[f]),(f,g,n,r)
            comparisons+=1
    # Exact quotient links for opposite carrier sides, independent of motif seams.
    twin={i:(i+3)%6 for i in range(6)}
    successor={i:(twin[i]+1)%6 for i in range(6)}
    for cycle in [[0,4,2],[1,5,3]]:
        assert [successor[i] for i in cycle]==cycle[1:]+cycle[:1]
    print('PASS k='+str(QQ(k))+': general 3D metric outside old family; distinct partner;',
          comparisons,'complete lattice-overlap comparisons; exact coverage density 1')

if __name__=='__main__':
    audit(AA(2)/5)
    audit(AA(1)/3)
