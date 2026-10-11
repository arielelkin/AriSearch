#!/usr/bin/env python3
"""Exact two-parameter four-face torus, plus irrational-parameter fixture.

The symbolic certificate checks linear identities on the b,c coefficient
basis and quadratic identities on (1,0),(0,1),(1,1). These are coefficient
checks, not sampled evidence. The algebraic fixture has a complete derived
integer lattice overlap domain, independently of the torus proof.
"""
from sage.all import AA,QQ,QQbar,CyclotomicField,PolynomialRing,RIF,ZZ,ceil,floor
from itertools import product
import json

K=CyclotomicField(10); z=K.gen(); phi=z+z**-1
PAIRS=((0,0,1,0),(0,1,1,1),(0,2,2,0),(0,3,3,0),(0,4,2,1),
       (1,2,3,2),(1,3,2,3),(1,4,3,3),(2,2,3,4),(2,4,3,1))
SHIFTS=((0,0),(1,0),(0,0),(0,0),(-1,0),(0,1),(0,1),(1,1),(1,0),(0,0))
ANGLES=((3,1,3,4,4),(3,1,3,4,4),(3,3,3,3,3),(3,3,3,3,3))


def normalized_cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def normalized_area(p):return sum(normalized_cross(p[j],p[(j+1)%5]) for j in range(5))/2

def geometry(b,c,root=z,golden=phi):
    A=golden**2*b+golden*c; H=golden**2*b-golden*c
    U=[0,A,b*(root+root**3)+c*root**2,c*root**2+b*root**3,b*root**3]
    W=[0,b,b*(1+root**2),b*(1+root**2)+H*root**4,
       b*(1+root**2)+H*root**4+c*root**6]
    assert W[4]+H*root**8==0
    motifs=[U,[A-q for q in U],[root*q+U[3] for q in W],
            [root**6*(W[(j+3)%5]-W[3])+U[4] for j in range(5)]]
    u=U[2];v=b*(4-root+2*root**2-5*root**3)-c*root**2
    return motifs,u,v


def coefficients(x):return [str(QQ(c)) for c in K(x).list()]+['0']*(4-len(K(x).list()))

def symbolic():
    bases=[geometry(K(1),K(0)),geometry(K(0),K(1))]
    for motifs,u,v in bases:
        for (i,a,j,b),(n,m) in zip(PAIRS,SHIFTS):
            assert motifs[i][a]==motifs[j][(b+1)%5]+n*u+m*v
            assert motifs[i][(a+1)%5]==motifs[j][b]+n*u+m*v
    for b,c in ((K(1),K(0)),(K(0),K(1)),(K(1),K(1))):
        motifs,u,v=geometry(b,c)
        assert normalized_area(motifs[0])==phi**3*b*b+2*phi**2*b*c+phi**2*c*c/2
        assert normalized_area(motifs[2])==phi**3*b*b-phi**2*c*c/2
        assert normalized_cross(u,v)==-4*phi**2*b*(phi*b+c)
        assert sum(normalized_area(p) for p in motifs)==-normalized_cross(u,v)
    involution={}
    for i,a,j,b in PAIRS:
        involution[(i,a)]=(j,b);involution[(j,b)]=(i,a)
    assert len(involution)==20
    permutation={x:(y[0],(y[1]+1)%5) for x,y in involution.items()}
    remaining=set(permutation);links=[]
    while remaining:
        start=min(remaining);cur=start;cycle=[]
        while cur not in cycle:
            cycle.append(cur);remaining.remove(cur);cur=permutation[cur]
        assert cur==start
        assert sum(ANGLES[f][v] for f,v in cycle)==10
        links.append([list(x) for x in cycle])
    assert len(links)==6 and 6-10+4==0
    return {'parameter_domain':'b>0, 0<c<phi*b',
            'formal_motif_coefficients_b_c':[[[coefficients(bases[0][0][i][j]),coefficients(bases[1][0][i][j])] for j in range(5)] for i in range(4)],
            'formal_lattice_coefficients_b_c':[[coefficients(bases[0][a]),coefficients(bases[1][a])] for a in (1,2)],
            'side_pairs':[list(p) for p in PAIRS], 'seam_integer_shifts':[list(p) for p in SHIFTS],
            'corner_links':links,'vertex_angles_in_pi_over_5':ANGLES,
            'normalized_area_U':'phi^3*b^2+2*phi^2*b*c+(phi^2/2)*c^2',
            'normalized_area_W':'phi^3*b^2-(phi^2/2)*c^2',
            'normalized_lattice_determinant':'-4*phi^2*b*(phi*b+c)'}


def encode(x):
    x=AA(x)
    if x in QQ:return {'rational':str(QQ(x))}
    p=x.minpoly();iv=x.interval(RIF);lo=iv.lower().exact_rational();hi=iv.upper().exact_rational()
    assert sum(lo<r<hi for r in p.roots(AA,multiplicities=False))==1
    return {'polynomial_coefficients':[str(QQ(a)) for a in p.list()],
            'isolating_interval':[str(lo),str(hi)]}


def fixture():
    root=QQbar.zeta(10); golden=AA((root+root**-1).real()); ratio=AA(2).sqrt()
    assert 1<ratio<golden
    motifs,u,v=geometry(QQbar(1),QQbar(ratio),root,QQbar(golden))
    def point(w):return (AA(QQbar(w).real()),AA(QQbar(w).imag()))
    polys=[[point(w) for w in p] for p in motifs];u,v=point(u),point(v)
    def cross(a,b):return a[0]*b[1]-a[1]*b[0]
    def sub(a,b):return (a[0]-b[0],a[1]-b[1])
    def area(p):return sum(cross(p[j],p[(j+1)%5]) for j in range(5))/2
    for p in polys:
        assert area(p)>0
        assert all(cross(sub(p[(j+1)%5],p[j]),sub(p[k],p[j]))>0
                   for j in range(5) for k in range(5) if k not in (j,(j+1)%5))
    det=cross(u,v);assert det<0
    lattice=[[(cross(p,v)/det,cross(u,p)/det) for p in poly] for poly in polys]
    def separate(a,b):
        for poly in (a,b):
            for j in range(5):
                e=sub(poly[(j+1)%5],poly[j]);normal=(-e[1],e[0])
                def project(p):return normal[0]*p[0]+normal[1]*p[1]
                x,y=[project(p) for p in a],[project(p) for p in b]
                if max(min(x),min(y))>=min(max(x),max(y)):return True
        return False
    domain=[]
    for i,j in product(range(4),repeat=2):
        bounds=[range(int(ceil(min(p[k] for p in lattice[i])-max(p[k] for p in lattice[j]))),
                      int(floor(max(p[k] for p in lattice[i])-min(p[k] for p in lattice[j])))+1) for k in (0,1)]
        for n,m in product(*bounds):
            if i==j and n==m==0:continue
            shifted=[(p[0]+n*u[0]+m*v[0],p[1]+n*u[1]+m*v[1]) for p in polys[j]]
            assert separate(polys[i],shifted),(i,j,n,m)
            domain.append([i,j,n,m])
    assert sum(area(p) for p in polys)==-det
    assert list(ratio.minpoly())==[QQ(-2),QQ(0),QQ(1)]
    # sqrt(2) is outside Q(sqrt(5)); the elementary coefficient proof is in the lemma.
    return {'b':encode(1),'c':encode(ratio),'motif':[[[encode(x) for x in p] for p in poly] for poly in polys],
            'lattice':[[encode(x) for x in p] for p in (u,v)],
            'areas':[encode(area(p)) for p in polys], 'determinant':encode(det),
            'complete_overlap_comparisons':domain,'comparison_count':len(domain)}


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Run without Python optimization.')
    print(json.dumps({'field':'Q(z), z^4-z^3+z^2-z+1=0, z=exp(pi*i/5)',
                      'symbolic_family':symbolic(),'irrational_fixture':fixture()},indent=2,sort_keys=True))
