#!/usr/bin/env python3
"""Independent exact fixture and universal side-gluing audit.

No author imports. SAT replaces clipping. Endpoint identities are checked
coefficientwise for arbitrary ell and rho=exp(-ip), not sampled parameters.
Corner cycles are derived from a fixed-point-free edge involution.
"""
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar, PolynomialRing, ceil, floor

if not __debug__: raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'research/certificates/obtuse-pentagon-regular-dodecagon-witness.json'
RING=PolynomialRing(QQ,'x')
Z=QQbar.zeta(24); I=QQbar.gen(); OMEGA=Z**8
assert Z**8-Z**4+1==0 and Z.real()>0 and Z.imag()>0
assert Z**6==I and OMEGA**2+OMEGA+1==0
S=AA(Z.imag()); C=AA(Z.real()); RADIUS=1/(2*S)
SQRT3=AA(3).sqrt()
assert RADIUS==2*C


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(c,p): return (c*p[0],c*p[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def edges(p): return [(p[i],p[(i+1)%len(p)]) for i in range(len(p))]
def area(p): return sum(cross(a,b) for a,b in edges(p))/2
def point(z): return (AA(z.real()),AA(z.imag()))


@lru_cache(None)
def algebraic(coeffs,lo,hi):
    f=RING([QQ(c) for c in coeffs]); a,b=QQ(lo),QQ(hi)
    assert a<b and f.is_irreducible() and f.is_monic()
    roots=[x for x,m in f.roots(AA) if a<x<b and m==1]
    assert len(roots)==1 and roots[0].minpoly()==f
    return roots[0]


def number(d):
    if 'rational' in d:
        assert set(d)=={'rational'}; return AA(QQ(d['rational']))
    assert set(d)=={'polynomial_coefficients','isolating_interval'}
    return algebraic(tuple(d['polynomial_coefficients']),*d['isolating_interval'])
def decode_point(p): return tuple(number(x) for x in p)


def strict_convex(p):
    assert area(p)>0
    for i,(a,b) in enumerate(edges(p)):
        assert all(cross(sub(b,a),sub(v,a))>0
                   for j,v in enumerate(p) if j not in (i,(i+1)%len(p)))


def separated(a,b):
    for p,q in edges(a)+edges(b):
        e=sub(q,p); n=(-e[1],e[0])
        x=[dot(n,p) for p in a]; y=[dot(n,p) for p in b]
        if max(min(x),min(y))>=min(max(x),max(y)): return True
    return False


# Complex affine forms in the independent symbols ell,rho.
ZERO=(QQbar(0),QQbar(0))
def fadd(a,b): return (a[0]+b[0],a[1]+b[1])
def fneg(a): return (-a[0],-a[1])
def fscale(c,a): return (c*a[0],c*a[1])
def fsub(a,b): return fadd(a,fneg(b))


Q_TABLE=[(1,1,(0,0)),(3,3,(0,0)),(6,1,(-1,1)),(5,3,(-1,1)),
         (2,1,(-1,0)),(1,3,(-1,0)),(4,1,(-1,0)),(6,3,(-1,0)),
         (3,1,(0,-1)),(2,3,(0,-1)),(5,1,(0,0)),(4,3,(0,0))]


def universal_gluing():
    ell=(QQbar(1),QQbar(0)); rho=(QQbar(0),QQbar(1))
    e1=fscale(Z**5,rho); e3=fscale(Z**15,rho)
    pc=[ZERO,ell,fadd(ell,e1),fsub(fscale(OMEGA,ell),e3),fscale(OMEGA,ell)]
    qc=fadd(ell,fscale(QQbar(RADIUS),rho))
    zc=fscale(1+OMEGA,qc); u=fscale(OMEGA-1,qc); v=fscale(OMEGA**2-1,qc)
    assert fadd(pc[2],pc[3])==zc
    assert fsub(pc[2],qc)==fscale(QQbar(QQ(1)/2)+I*QQbar(C/(2*S)),e1)
    assert fsub(pc[4],fscale(OMEGA,qc))==fscale(OMEGA,fsub(pc[1],qc))
    Q=[fadd(qc,fscale(Z**(2*j),fsub(pc[2],qc))) for j in range(12)]
    faces=[Q]+[[fscale(OMEGA**j,p) for p in pc] for j in range(3)]
    faces += [[fsub(zc,fscale(OMEGA**j,p)) for p in pc] for j in range(3)]
    def period(n,m): return fadd(fscale(n,u),fscale(m,v))
    pairing={}
    def pair(f,e,g,k,offset):
        assert (f,e) not in pairing and (g,k) not in pairing and (f,e)!=(g,k)
        t=period(*offset)
        assert faces[f][e]==fadd(faces[g][(k+1)%len(faces[g])],t)
        assert faces[f][(e+1)%len(faces[f])]==fadd(faces[g][k],t)
        pairing[f,e]=(g,k); pairing[g,k]=(f,e)
    for j in range(3):
        pair(1+j,4,1+(j+1)%3,0,(0,0))
        pair(4+j,4,4+(j+1)%3,0,(0,0))
        pair(1+j,2,4+j,2,[(0,0),(0,1),(-1,1)][j])
    for r,(face,side,offset) in enumerate(Q_TABLE): pair(0,r,face,side,offset)
    assert len(pairing)==42
    assert all(pairing[pairing[d]]==d for d in pairing)
    # Corner rotation: cross the incoming edge to the paired edge's start.
    cycles=[]; seen=set()
    for f,face in enumerate(faces):
        for vertex in range(len(face)):
            if (f,vertex) in seen: continue
            corner=(f,vertex); cycle=[]
            while corner not in seen:
                seen.add(corner); cycle.append(corner)
                g,k=corner
                corner=pairing[g,(k-1)%len(faces[g])]
            assert corner==cycle[0]; cycles.append(cycle)
    assert len(cycles)==14 and all(len(c)==3 for c in cycles)
    labels=[(120,0,0),(0,1,0),(0,0,1),(210,0,-1),(210,-1,0)]
    ppp=qpp=0
    for cyc in cycles:
        weights=[(150,0,0) if f==0 else labels[k] for f,k in cyc]
        assert tuple(sum(w[i] for w in weights) for i in range(3))==(360,0,0)
        if all(f!=0 for f,k in cyc):
            ppp+=1; assert all(k==0 for f,k in cyc)
        else:
            qpp+=1; assert sum(f==0 for f,k in cyc)==1
    assert (ppp,qpp)==(2,12)
    # Face adjacency is connected; reversed edge maps make it orientable.
    reached={0}
    while True:
        enlarged=reached|{g for (f,e),(g,k) in pairing.items() if f in reached}
        if enlarged==reached: break
        reached=enlarged
    assert len(reached)==7 and len(cycles)-len(pairing)//2+len(faces)==0

    # Universal area identity, coefficientwise before imposing x^2+y^2=1.
    T=PolynomialRing(AA,names=('l','x','y')); l,x,y=T.gens()
    def evaluate(form):
        a,b=form
        return (AA(a.real())*l+AA(b.real())*x+AA(b.imag())*y,
                AA(a.imag())*l+AA(b.imag())*x-AA(b.real())*y)
    # rho=x-i*y, so the displayed real coefficient has +Im(b)*y.
    pp=[[evaluate(p) for p in face] for face in faces]
    raw_area=lambda p:sum(a[0]*b[1]-a[1]*b[0] for a,b in edges(p))/2
    determinant=lambda a,b:a[0]*b[1]-a[1]*b[0]
    raw_P=raw_area(pp[1]); raw_Q=raw_area(pp[0])
    expected_P=SQRT3*l*l/4+SQRT3*l*RADIUS*x/2-(x*x+y*y)/4
    assert raw_P==expected_P
    assert raw_Q==3*C/S*(x*x+y*y)
    assert sum(raw_area(p) for p in pp)==determinant(evaluate(u),evaluate(v))
    assert determinant(evaluate(u),evaluate(v))==3*SQRT3/2*((l+RADIUS*x)**2+(RADIUS*y)**2)
    print('Universal: 21 reversed edge pairs, 14 ordered trivalent vertex cycles, connected torus;')
    print('all endpoint/gluing and area identities hold coefficientwise for the full family.')


def fixed_fixture():
    c=json.loads(CERT.read_text()); motif=[[decode_point(p) for p in poly] for poly in c['motif']]
    assert list(map(len,motif))==[12]+[5]*6
    for p in motif: strict_convex(p)
    ell=number(c['parameters']['ell']); sp=number(c['parameters']['sin_p']); cp=number(c['parameters']['cos_p'])
    assert ell==2 and sp==QQ(1)/8 and cp==AA(63).sqrt()/8 and sp*sp+cp*cp==1
    # Exact positive-p branch and the strict parameter threshold.
    assert 0<sp<S and cp>0
    sin_h_minus_p=S*cp-C*sp
    assert sin_h_minus_p>0 and SQRT3*ell*sin_h_minus_p>2*S*S
    rho=QQbar(cp)-I*QQbar(sp)
    e1=Z**5*rho; e3=Z**15*rho
    pc=[QQbar(0),QQbar(ell),ell+e1,ell*OMEGA-e3,ell*OMEGA]
    qc=ell+RADIUS*rho; zc=(1+OMEGA)*qc
    expected=[[point(qc+(pc[2]-qc)*Z**(2*j)) for j in range(12)]]
    expected += [[point(OMEGA**j*p) for p in pc] for j in range(3)]
    expected += [[point(zc-OMEGA**j*p) for p in pc] for j in range(3)]
    assert motif==expected
    Q,P=motif[:2]; pes=[sub(b,a) for a,b in edges(P)]; ss=[dot(e,e) for e in pes]
    assert ss[0]==ss[4]==ell**2 and ss[1]==ss[3]==1 and ss[2]>0
    assert ss==[number(x) for x in c['P_side_squared_lengths']]
    angles=[-dot(pes[j-1],pes[j])/(ss[j-1]*ss[j]).sqrt() for j in range(5)]
    assert angles==[number(x) for x in c['P_angle_cosines']]
    assert angles[0]==-QQ(1)/2 and all(-QQ(1)/2<a<0 for a in angles[1:])
    assert angles[1]!=angles[4] and angles[2]!=angles[3]
    qes=[sub(b,a) for a,b in edges(Q)]
    assert all(dot(e,e)==1 for e in qes)
    assert all(-dot(qes[j-1],qes[j])==-(SQRT3/2) for j in range(12))
    assert area(P)==SQRT3*ell**2/4+SQRT3*ell*RADIUS*cp/2-QQ(1)/4==number(c['area_P'])
    assert area(Q)==3*C/S==number(c['area_Q'])
    u,v=[decode_point(p) for p in c['lattice']]
    assert u==point((OMEGA-1)*qc) and v==point((OMEGA**2-1)*qc)
    det=cross(u,v); assert det>0 and det==number(c['lattice_covolume'])
    coords=lambda p:(cross(p,v)/det,cross(u,p)/det)
    lattice=[[coords(p) for p in poly] for poly in motif]
    domain=[]
    for i,a in enumerate(motif):
        for j,b in enumerate(motif):
            bounds=[]
            for k in (0,1):
                low=ceil(min(p[k] for p in lattice[i])-max(p[k] for p in lattice[j]))
                high=floor(max(p[k] for p in lattice[i])-min(p[k] for p in lattice[j]))
                bounds.append(range(int(low),int(high)+1))
            for n,m in product(*bounds):
                if i==j and n==m==0: continue
                t=add(scale(n,u),scale(m,v))
                assert separated(a,[add(p,t) for p in b]),(i,j,n,m)
                domain.append([i,j,n,m])
    assert domain==c['complete_overlap_comparisons'] and len(domain)==62
    assert sum(area(p) for p in motif)==det
    print('Fixture: exact asymmetric parameters and 7 motifs; all support, angle and side checks pass;')
    print('62 complete SAT overlap comparisons pass, and motif area equals positive covolume.')


if __name__=='__main__':
    universal_gluing()
    fixed_fixture()
