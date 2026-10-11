#!/usr/bin/env python3
"""Fixed exact asymmetric all-obtuse P + regular Q12 periodic witness.

No parameter search: sin(p)=1/8, cos(p)=sqrt(63)/8, l=2.
All seven motifs and complete lattice overlap bounds are exact algebraic.
"""
from itertools import product
import json
from sage.all import AA,QQ,QQbar,RIF,vector,matrix,ceil,floor


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


def point(w):return vector(AA,[w.real(),w.imag()])
def points(poly):return [[exact(c) for c in p] for p in poly]


def main():
    if not __debug__:raise RuntimeError('Run without Python optimization.')
    z=QQbar.zeta(24);omega=z**8
    sine=AA(z.imag());cosine=AA(z.real())
    radius=1/(2*sine);apothem=cosine/(2*sine)
    rho=QQbar(AA(63).sqrt())/8-QQbar.gen()/8
    ell=QQbar(2)
    e1=z**5*rho;e3=z**15*rho
    pc=[QQbar(0),ell,ell+e1,ell*omega-e3,ell*omega]
    qc=ell+radius*rho
    assert pc[2]-qc==(QQbar(QQ(1)/2)+QQbar.gen()*apothem)*e1
    assert (1+omega)*qc==pc[2]+pc[3]
    q=[qc+(pc[2]-qc)*z**(2*j) for j in range(12)]
    sc=(1+omega)*qc
    uc=(omega-1)*qc;vc=(omega**2-1)*qc
    u,v=point(uc),point(vc)
    motif=[list(map(point,q))]
    motif += [[point(omega**j*p) for p in pc] for j in range(3)]
    motif += [[point(sc-omega**j*p) for p in pc] for j in range(3)]
    Q,P=motif[0],motif[1]
    for poly in motif:
        assert area(poly)>0
        assert all(cross(poly[(j+1)%len(poly)]-poly[j],poly[l]-poly[j])>0
                   for j in range(len(poly)) for l in range(len(poly))
                   if l not in (j,(j+1)%len(poly)))
    pes=[P[(j+1)%5]-P[j] for j in range(5)]
    lengths2=[e.dot_product(e) for e in pes]
    assert lengths2[0]==lengths2[4]==4 and lengths2[1]==lengths2[3]==1
    assert lengths2[2]>0
    angles=[-pes[j-1].dot_product(pes[j])/(lengths2[j-1]*lengths2[j]).sqrt()
            for j in range(5)]
    assert angles[0]==-QQ(1)/2 and all(-QQ(1)/2<c<0 for c in angles[1:])
    assert angles[1]!=angles[4] and angles[2]!=angles[3]
    assert angles[1]==-sine*AA(rho.real())-cosine/8
    assert angles[4]==-sine*AA(rho.real())+cosine/8
    qes=[Q[(j+1)%12]-Q[j] for j in range(12)]
    assert all(e.dot_product(e)==1 for e in qes)
    assert all(-qes[j-1].dot_product(qes[j])==-cosine**2+sine**2 for j in range(12))
    expected_area_P=AA(3).sqrt()+AA(3).sqrt()*radius*AA(rho.real())-QQ(1)/4
    assert area(P)==expected_area_P
    assert area(Q)==3*cosine/sine
    basis=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    assert basis.det()>0
    coordinates=[[basis.inverse()*p for p in poly] for poly in motif]
    comparisons=[]
    for i,j in product(range(7),repeat=2):
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
    data={'scope':'fixed asymmetric seven-motif Q12 witness, complete exact overlap domain and area density',
          'parameters':{'sin_p':exact(QQ(1)/8),'cos_p':exact(AA(63).sqrt()/8),'ell':exact(2)},
          'motif':[points(poly) for poly in motif],
          'lattice':[points([u])[0],points([v])[0]],
          'P_side_squared_lengths':[exact(c) for c in lengths2],
          'P_angle_cosines':[exact(c) for c in angles],
          'area_Q':exact(area(Q)),'area_P':exact(area(P)),
          'lattice_covolume':exact(basis.det()),
          'complete_overlap_comparisons':comparisons}
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=='__main__':main()
