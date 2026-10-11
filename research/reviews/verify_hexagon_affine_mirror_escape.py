#!/usr/bin/env python3
"""Exact direct lattice verification of two non-equilateral hexagons."""
from sage.all import NumberField,PolynomialRing,QQ,AA,vector,matrix,floor,ceil,ZZ
from itertools import product
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def area(vs):return sum(cross(vs[j],vs[(j+1)%len(vs)]) for j in range(len(vs)))/2

def interior_disjoint(a,b):
    for vs in (a,b):
        for j in range(len(vs)):
            e=vs[(j+1)%len(vs)]-vs[j]; n=vector(e.base_ring(),[-e[1],e[0]])
            ap=[n.dot_product(v) for v in a];bp=[n.dot_product(v) for v in b]
            if max(ap)<=min(bp) or max(bp)<=min(ap):return True
    return False

def main():
    data=json.loads((ROOT/'research/certificates/hexagon-affine-mirror-escape.json').read_text())
    X=PolynomialRing(QQ,'x').gen()
    K=NumberField(X**4-16*X**2+4,'g',embedding=AA(3).sqrt()+AA(5).sqrt())
    g=K.gen();w=(g-2/g)/2;h=(g+2/g)/2;p=w*h
    assert w*w==3 and h*h==5 and w>0 and h>0
    def elt(c):return sum(K(a)*b for a,b in zip(c,[K(1),w,h,p]))
    def vec(cs):return vector(K,[elt(c) for c in cs])
    A=[vec(v) for v in data['A_vertices']];B=[vec(v) for v in data['B_vertices']]
    t=vec(data['B_motif_translation']);u=vec(data['lattice'][0]);v=vec(data['lattice'][1])
    S=matrix(K,[[1,0],[0,-1]])
    motif=[A,[S*x for x in A],[x+t for x in B]]
    for vs in [A,B]:
        assert len(vs)==6
        assert all(cross(vs[(j+1)%6]-vs[j],vs[k]-vs[j])>0
                   for j in range(6) for k in range(6) if k not in (j,(j+1)%6))
    lengths=[[sum(z*z for z in vs[(j+1)%6]-vs[j]) for j in range(6)] for vs in [A,B]]
    assert lengths[0]==[4,(59-9*h)/32,K(7)/4,K(61)/16,K(7)/4,(59+9*h)/32]
    assert lengths[1]==[K(61)/16,(59+9*h)/32,(59+9*h)/32,K(61)/16,(59-9*h)/32,(59-9*h)/32]
    assert len(set(lengths[0]))==5 and len(set(lengths[1]))==3
    assert not any(lengths[0][j]==lengths[0][(j+3)%6] for j in range(3))
    assert [j for j in range(3) if lengths[1][j]==lengths[1][j+3]]==[0]
    assert cross(B[1]-B[0],B[4]-B[3])!=0
    # Both H2 and H3 require a repetition pattern absent in these words.
    for ls in lengths:
        assert not any(ls[(i+1)%6]==ls[(i+3)%6] and ls[(i+2)%6]==ls[(i+5)%6] for i in range(6))
        assert not any(all(ls[(i+2*k)%6]==ls[(i+2*k+1)%6] for k in range(3)) for i in range(6))
    # Recover and check the three source-oriented faces. These tests also
    # check every retained seam and the affine mirror identity, not just sets.
    D=matrix(K,[[2,0],[0,1]]);Z=matrix(K,[[p/4,-K(1)/4],[K(1)/4,p/4]])
    A0=[D.inverse()*x for x in A]
    B0=[Z.inverse()*D.inverse()*x for x in B]
    r=Z.inverse();t1=A0[1]-r*A0[3];t2=A0[1]-Z*B0[5]
    ccw=[A,[D*(r*x+t1) for x in A0],[D*(Z*x+t2) for x in B0]]
    assert set(tuple(x) for x in ccw[1])==set(tuple(x) for x in motif[1])
    assert ccw[2]==motif[2] and D*t2==t
    for ((f,j),(g,k)),(n,m) in zip(data['source_seams'],data['seam_translation_coefficients']):
        shift=n*u+m*v
        assert ccw[f][j]==ccw[g][(k+1)%6]+shift
        assert ccw[f][(j+1)%6]==ccw[g][k]+shift
    assert u[0]==v[0]>0 and u[1]==-v[1]>0
    L=u[0];H=u[1]; comparisons=0
    # Every possible intersecting lattice translate is captured by its exact bbox.
    for i,j in product(range(3),repeat=2):
        a=motif[i];b=motif[j]
        qlo=ceil(AA((min(x[0] for x in a)-max(x[0] for x in b))/L))
        qhi=floor(AA((max(x[0] for x in a)-min(x[0] for x in b))/L))
        klo=ceil(AA((min(x[1] for x in a)-max(x[1] for x in b))/H))
        khi=floor(AA((max(x[1] for x in a)-min(x[1] for x in b))/H))
        for q in range(int(qlo),int(qhi)+1):
            for k in range(int(klo),int(khi)+1):
                if (q-k)%2:continue
                n=(q+k)//2;m=(q-k)//2
                if i==j and n==m==0:continue
                assert interior_disjoint(a,[x+n*u+m*v for x in b]),(i,j,n,m)
                comparisons+=1
    assert sum(abs(area(m)) for m in motif)==abs(cross(u,v))==19*w/4+3*h
    assert area(B)/area(A)==p/2-1 and p*p==15
    # Rational angle between B's opposite edge directions would make this
    # rational trace of a root of unity an integer; it is not.
    e0=B[1]-B[0];e3=B[4]-B[3]
    assert e0==vector(K,[p/2,K(1)/4])
    assert e3==vector(K,[-p/2,K(1)/4])
    assert K(2)*((p/2)**2-(K(1)/4)**2)/((p/2)**2+(K(1)/4)**2)==K(118)/61
    assert K(118)/61 not in ZZ
    print(f'PASS: exact convex pair, five/three repeated lengths, {comparisons} exhaustive lattice overlap comparisons, area=det, non-monohedral Reinhardt gates, irrational direction trace and B/A area ratio.')

if __name__=='__main__':main()
