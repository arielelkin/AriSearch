#!/usr/bin/env python3
"""Exact four-motif witness for regular heptagon and its all-obtuse pentagon.

Fixed algebraic coordinates, no search domain. Exhaustive lattice-overlap
bounds are computed from each pair's exact lattice-coordinate bounding boxes.
All decisions use AA/QQbar; rational polynomial/root encodings are retained.
"""
from sage.all import AA,QQ,QQbar,RIF,vector,matrix,ceil,floor
from itertools import product
import json


def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(p):return sum(cross(p[j],p[(j+1)%len(p)]) for j in range(len(p)))/2 if len(p)>=3 else AA(0)


def clip(a,b):
    a=list(a)
    for j in range(len(b)):
        if not a:break
        old,a=a,[]
        edge=b[(j+1)%len(b)]-b[j]
        prev=old[-1];hp=cross(edge,prev-b[j])
        for cur in old:
            hc=cross(edge,cur-b[j])
            if (hp>=0)!=(hc>=0):a.append(prev+(cur-prev)*hp/(hp-hc))
            if hc>=0:a.append(cur)
            prev,hp=cur,hc
    return a


def exact(x):
    x=AA(x)
    if x in QQ:return {'rational':str(QQ(x))}
    iv=x.interval(RIF)
    lo,hi=iv.lower().exact_rational(),iv.upper().exact_rational()
    poly=x.minpoly()
    assert sum(lo<r<hi for r in poly.roots(AA,multiplicities=False))==1
    return {'polynomial_coefficients':[str(QQ(c)) for c in poly.list()],
            'isolating_interval':[str(lo),str(hi)]}


def points(poly):return [[exact(c) for c in p] for p in poly]


def main():
    if not __debug__:raise RuntimeError('Run without Python optimization.')
    z=QQbar.zeta(14)
    sin=AA(z.imag());cos=AA(z.real())
    D=cos/sin;R=1/(2*sin)
    def point(w):return vector(AA,[w.real(),w.imag()])
    centers=[QQbar(0),QQbar(D),D*(1+z**3),D*(1+z**3+z**6),
             D*(z**3+z**6),D*z**6]
    u=point(centers[2]);v=point(centers[4]);C=point(centers[3])
    Q=[point(R*z**(2*j+1)) for j in range(7)]
    Q1=[point(D)-q for q in Q]
    k=[0,3,6,7,10,13]
    h=[point(centers[j]+R*z**(k[j]+1)) for j in range(6)]
    a=point(R*z**3);b=C-a
    P=[a,h[0],h[1],h[2],b]
    P1=[C-p for p in P]
    motif=[Q,Q1,P,P1]
    for poly in motif:
        assert area(poly)>0
        assert all(cross(poly[(j+1)%len(poly)]-poly[j],poly[l]-poly[j])>0
                   for j in range(len(poly)) for l in range(len(poly))
                   if l not in (j,(j+1)%len(poly)))
    L=sin/AA((QQbar.zeta(28)**3).imag())
    alpha_cos=AA((z**4).real())
    beta_cos=AA((z**5).real())
    gamma_cos=AA((QQbar.zeta(28)**9).real())
    for poly,expected in ((Q,[beta_cos]*7),(P,[gamma_cos,alpha_cos,alpha_cos,alpha_cos,gamma_cos])):
        edges=[poly[(j+1)%len(poly)]-poly[j] for j in range(len(poly))]
        lengths2=[e.dot_product(e) for e in edges]
        if len(poly)==7:assert lengths2==[AA(1)]*7
        else:assert lengths2[:4]==[AA(1)]*4 and lengths2[4]==L*L and 0<L<1
        angles=[-edges[j-1].dot_product(edges[j])/(lengths2[j-1]*lengths2[j]).sqrt()
                for j in range(len(poly))]
        assert angles==expected
    basis=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    assert basis.det()>0
    coordinates=[[basis.inverse()*p for p in poly] for poly in motif]
    comparisons=[]
    for i,j in product(range(4),repeat=2):
        bounds=[]
        for axis in range(2):
            lo=ceil(min(p[axis] for p in coordinates[i])-max(p[axis] for p in coordinates[j]))
            hi=floor(max(p[axis] for p in coordinates[i])-min(p[axis] for p in coordinates[j]))
            bounds.append(range(int(lo),int(hi)+1))
        for n,m in product(*bounds):
            if i==j and n==m==0:continue
            assert area(clip(motif[i],[p+n*u+m*v for p in motif[j]]))==0,(i,j,n,m)
            comparisons.append([i,j,n,m])
    assert sum(area(poly) for poly in motif)==basis.det()
    data={'scope':'fixed whole-plane four-motif witness, exact complete overlap domain and area density',
          'motif':[points(poly) for poly in motif],
          'lattice':[points([u])[0],points([v])[0]],
          'P_private_length':exact(L),
          'P_angle_cosines':[exact(c) for c in [gamma_cos,alpha_cos,alpha_cos,alpha_cos,gamma_cos]],
          'area_Q':exact(area(Q)),'area_P':exact(area(P)),
          'lattice_covolume':exact(basis.det()),
          'complete_overlap_comparisons':comparisons}
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=='__main__':main()
