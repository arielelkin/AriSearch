#!/usr/bin/env python3
"""Independent exact four-motif audit, using SAT rather than clipping.

No producer imports. The full integer overlap domain is derived afresh
from lattice-coordinate bounds. All retained algebraic numbers are decoded
from their minimal polynomials and strict rational isolating intervals.
"""
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, PolynomialRing, ceil, floor

if not __debug__:
    raise RuntimeError('Assertions are required')

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'research/certificates/all-obtuse-pentagon-regular-heptagon-witness.json'
R=PolynomialRing(QQ,'x')
W=QQbar.zeta(28); Z=W**2
assert W**12-W**10+W**8-W**6+W**4-W**2+1==0
assert W.real()>0 and W.imag()>0 and W**7==QQbar.gen()
assert Z**6-Z**5+Z**4-Z**3+Z**2-Z+1==0
assert QQ(9)/10<Z.real()<QQ(91)/100 and QQ(43)/100<Z.imag()<QQ(44)/100


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(c,p): return (c*p[0],c*p[1])
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def edges(poly): return [(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))]
def area(poly): return sum(cross(a,b) for a,b in edges(poly))/2
def point_complex(z): return (AA(z.real()),AA(z.imag()))


@lru_cache(None)
def algebraic(coeffs,lo,hi):
    f=R([QQ(c) for c in coeffs]); a,b=QQ(lo),QQ(hi)
    assert a<b and f.is_monic() and f.is_irreducible()
    roots=[x for x,m in f.roots(AA) if a<x<b and m==1]
    assert len(roots)==1 and roots[0].minpoly()==f
    return roots[0]


def number(d):
    if 'rational' in d:
        assert set(d)=={'rational'}
        return AA(QQ(d['rational']))
    assert set(d)=={'polynomial_coefficients','isolating_interval'}
    return algebraic(tuple(d['polynomial_coefficients']),*d['isolating_interval'])


def point(d): return tuple(number(x) for x in d)


def strict_convex(poly):
    assert area(poly)>0
    for i,(a,b) in enumerate(edges(poly)):
        for j,p in enumerate(poly):
            if j not in (i,(i+1)%len(poly)):
                assert cross(sub(b,a),sub(p,a))>0


def separated(a,b):
    # A separating edge normal of either convex polygon is sufficient and
    # necessary for disjoint interiors. Equality includes boundary contacts.
    for p,q in edges(a)+edges(b):
        e=sub(q,p); n=(-e[1],e[0])
        x=[dot(n,v) for v in a]; y=[dot(n,v) for v in b]
        if max(min(x),min(y))>=min(max(x),max(y)): return True
    return False


def audit():
    c=json.loads(CERT.read_text())
    motif=[[point(p) for p in poly] for poly in c['motif']]
    assert list(map(len,motif))==[7,7,5,5]
    for p in motif: strict_convex(p)
    Q,Q1,P,P1=motif
    sine=AA(Z.imag()); cosine=AA(Z.real())
    radius=1/(2*sine); spacing=cosine/sine
    expected_Q=[point_complex(radius*Z**(2*j+1)) for j in range(7)]
    assert Q==expected_Q
    assert all(add(a,b)==(spacing,0) for a,b in zip(Q,Q1))
    centers=[QQbar(0),QQbar(spacing),spacing*(1+Z**3),
             spacing*(1+Z**3+Z**6),spacing*(Z**3+Z**6),spacing*Z**6]
    ks=[0,3,6,7,10,13]
    hs=[point_complex(centers[j]+radius*Z**(ks[j]+1)) for j in range(6)]
    aa=point_complex(radius*Z**3); cc=point_complex(centers[3])
    assert P==[aa,hs[0],hs[1],hs[2],sub(cc,aa)]
    p_center=add(P[0],P1[0])
    assert all(add(a,b)==p_center for a,b in zip(P,P1))
    private_length=sine/AA((W**3).imag())
    assert 0<private_length<1 and number(c['P_private_length'])==private_length
    alpha,beta,gamma=AA((Z**4).real()),AA((Z**5).real()),AA((W**9).real())
    assert [number(x) for x in c['P_angle_cosines']]==[gamma,alpha,alpha,alpha,gamma]
    for p,angles in ((Q,[beta]*7),(P,[gamma,alpha,alpha,alpha,gamma])):
        es=[sub(b,a) for a,b in edges(p)]; ss=[dot(e,e) for e in es]
        assert ss==([AA(1)]*7 if len(p)==7 else [AA(1)]*4+[private_length**2])
        for j,theta_cos in enumerate(angles):
            assert -dot(es[j-1],es[j])/(ss[j-1]*ss[j]).sqrt()==theta_cos
    assert area(Q1)==area(Q) and area(P1)==area(P)
    assert number(c['area_Q'])==area(Q) and number(c['area_P'])==area(P)

    u,v=[point(x) for x in c['lattice']]; det=cross(u,v)
    assert det>0 and det==number(c['lattice_covolume'])
    # Check the stated carrier-center formula as well as the certificate.
    assert u==point_complex(spacing*(1+Z**3))
    assert v==point_complex(spacing*(Z**3+Z**6))
    assert p_center==point_complex(spacing*(1+Z**3+Z**6))
    def coordinates(p): return (cross(p,v)/det,cross(u,p)/det)
    lattice_polys=[[coordinates(p) for p in poly] for poly in motif]
    domain=[]
    for i,a in enumerate(motif):
        for j,b in enumerate(motif):
            bounds=[]
            for k in (0,1):
                lo=ceil(min(p[k] for p in lattice_polys[i])-max(p[k] for p in lattice_polys[j]))
                hi=floor(max(p[k] for p in lattice_polys[i])-min(p[k] for p in lattice_polys[j]))
                bounds.append(range(int(lo),int(hi)+1))
            for m,n in product(*bounds):
                if i==j and m==n==0: continue
                t=add(scale(m,u),scale(n,v))
                assert separated(a,[add(p,t) for p in b]),(i,j,m,n)
                domain.append([i,j,m,n])
    assert domain==c['complete_overlap_comparisons'] and len(domain)==26
    assert sum(area(p) for p in motif)==det
    print('VALID: regular unit Q, exact P*, two half-turn copies, all strict support inequalities;')
    print('26 complete lattice overlap tests pass by separating axes; motif area equals positive covolume.')


if __name__=='__main__': audit()
