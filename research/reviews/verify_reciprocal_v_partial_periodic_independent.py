#!/usr/bin/env python3
"""Fresh reciprocal-V formal area and complete exact coordinate clipping.

No author imports. The independently reviewed Q3 checker supplies only exact
AA plane/cross/clipping utilities. Whole-cone native geometry and all
boundary-chain endpoints are independently verified symbolically. Five ratio
strata plus congruent ratio1 are independently constructed from native walks.
Normal replay writes nothing.
"""
from pathlib import Path
import importlib.util
from itertools import product
from sage.all import PolynomialRing, QQ, AA

spec=importlib.util.spec_from_file_location('root_exact_clipping',Path(__file__).with_name('verify_octagon_q3_equal_private_independent.py'))
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
K,z,phi=g.K,g.z,g.phi
R=PolynomialRing(K,names=('a','k'))
a,k=R.gens()

def conjugate(poly):
    return sum(c.conjugate()*a**i*k**j for (i,j),c in R(poly).dict().items())

def normalized_cross(x,y):
    return (conjugate(x)*y-x*conjugate(y))/(z-z.conjugate())

def formal_faces(a,k):
    r=phi*k+a/phi
    f=phi*a+k/phi
    J=r*z**2-a*z**4
    H=2*J+k
    A=[J,r*z**2,0*a,a,a+k*z]
    B=[J+k,J,J-f*z**3,J-f*z**3+k*z,J-f*z**3+k*z+a*z**2]
    faces=[A,[H-t for t in A],B,[H-t for t in B]]
    return faces,B[3],H-a


def whole_cone_boundary_audit(faces,u,v):
    r=phi*k+a/phi;f=phi*a+k/phi
    J=faces[0][0];H=faces[1][0]+faces[0][0]
    assert phi**2==phi+1 and r-f==k-a
    assert r-a==phi*k-a/phi**2 and k-f==k/phi**2-phi*a
    lengths=[[a,r,a,k,k]]*2+[[k,f,k,a,a]]*2
    powers=[[4,7,0,1,3],[9,2,5,6,8],[5,8,1,2,4],[0,3,6,7,9]]
    cosines=[-phi/2,(phi-1)/2,(phi-1)/2,-phi/2,(1-phi)/2]
    support_checks=0
    def strictly_positive_coefficients(poly):
        assert poly!=0
        for coefficient in poly.coefficients():
            value=g.embedding(coefficient)
            assert value.imag()==0 and value.real()>0
    for i,face in enumerate(faces):
        edges=[face[(j+1)%5]-face[j] for j in range(5)]
        assert edges==[length*z**power for length,power in zip(lengths[i],powers[i])]
        assert sum(edges)==0
        for j,origin in enumerate(face):
            incoming=-edges[j-1];outgoing=edges[j]
            dot=(conjugate(incoming)*outgoing+incoming*conjugate(outgoing))/2
            assert dot==cosines[j]*lengths[i][j-1]*lengths[i][j]
            for h,point in enumerate(face):
                if h not in (j,(j+1)%5):
                    strictly_positive_coefficients(normalized_cross(outgoing,point-origin))
                    support_checks+=1
    assert support_checks==60
    # All six full native seams, reconstructed from endpoint formulas only.
    full=[(0,0,3,4,0,0),(1,0,2,4,0,0),(2,0,3,0,0,0),
          (0,2,1,2,0,-1),(0,3,3,2,1,-1),(1,3,2,2,-1,1)]
    used=set()
    for i,j,h,b,n,m in full:
        shift=n*u+m*v
        assert faces[i][j]==faces[h][(b+1)%5]+shift
        assert faces[i][(j+1)%5]==faces[h][b]+shift
        assert (i,j) not in used and (h,b) not in used
        used.update(((i,j),(h,b)))
    # The remaining eight native sides appear once, with these independently
    # derived directed line coordinates. On each line the two opposite
    # decompositions have the same full interval, for every positive metric.
    line2=[(0,1,0,0,r,0),(2,3,-1,0,0,a),
           (1,1,-1,0,a,r+a),(3,3,0,0,r+a,r)]
    line3=[(0,4,0,0,-k,0),(2,1,0,0,0,-f),
           (1,4,1,-1,-f,-k-f),(3,1,1,-1,-k-f,-k)]
    for records,origin,direction in ((line2,0*a,z**2),(line3,J,z**3)):
        for i,j,n,m,tail,head in records:
            assert faces[i][j]+n*u+m*v==origin+tail*direction
            assert faces[i][(j+1)%5]+n*u+m*v==origin+head*direction
            assert (i,j) not in used
            used.add((i,j))
    assert used==set(product(range(4),range(5)))
    # Whole-stratum order/strict length checks. This is the complete analytic
    # five-stratum domain, with zero middle intervals omitted on boundaries.
    P=PolynomialRing(K,names=('s','t'));s,t=P.gens()
    cases=[({a:phi**3*s+t,k:s},[r,a-r,r,k,f-k,k]),
           ({a:s,k:phi**-3*s},[a,a,k,f-k,k]),
           ({a:s+t,k:phi**-3*s+phi**3*t},[a,r-a,a,k,f-k,k]),
           ({a:s,k:phi**3*s},[a,r-a,a,k,k]),
           ({a:s,k:phi**3*s+t},[a,r-a,a,f,k-f,f])]
    assert R(r-a).subs(cases[1][0])==0
    assert R(k-f).subs(cases[3][0])==0
    for substitution,segments in cases:
        for length in segments:
            strictly_positive_coefficients(P(R(length).subs(substitution)))
    # The imported monohedral filter uses the angle-after-side gates.
    assert lengths[0][2]-lengths[0][4]==a-k
    assert lengths[0][3]-lengths[0][0]==k-a
    assert lengths[2][2]-lengths[2][4]==k-a
    assert lengths[2][3]-lengths[2][0]==a-k
    return support_checks


def main():
    faces,u,v=formal_faces(a,k)
    support_checks=whole_cone_boundary_audit(faces,u,v)
    determinant=normalized_cross(u,v)
    total_area=sum(sum(normalized_cross(face[j],face[(j+1)%5]) for j in range(5))/2 for face in faces)
    assert determinant==phi**2*(a*a+4*a*k+k*k)==total_area
    native_areas=[sum(normalized_cross(face[j],face[(j+1)%5]) for j in range(5))/2
                  for face in (faces[0],faces[2])]
    assert native_areas==[(a*a+2*phi**2*a*k+phi*k*k)/2,
                         (k*k+2*phi**2*a*k+phi*a*a)/2]
    for face in faces:
        assert sum(face[(j+1)%5]-face[j] for j in range(5))==0
    cases=[('lower-open',phi**-4),('lower-boundary',phi**-3),
           ('middle-open',K(QQ(3)/2)),('upper-boundary',phi**3),
           ('upper-open',phi**4),('congruent-interior',K(1))]
    counts={}
    for label,ratio in cases:
        fs,Uc,Vc=formal_faces(K(1),ratio)
        polys=[[g.plane(p) for p in face] for face in fs]
        U,V=g.plane(Uc),g.plane(Vc)
        det=g.cross(U,V)
        assert det>0 and sum(g.area(poly) for poly in polys)==det
        for fidx,poly in enumerate(polys):
            for j,p in enumerate(poly):
                edge=poly[(j+1)%5]-p
                for h,q in enumerate(poly):
                    if h not in (j,(j+1)%5):assert g.cross(edge,q-p)>0
                incoming=poly[(j-1)%5]-p
                cosine=incoming.dot_product(edge)/(incoming.norm()*edge.norm())
                expected=[-g.phia/2,(g.phia-1)/2,(g.phia-1)/2,-g.phia/2,(1-g.phia)/2][j]
                assert cosine==expected
        def coords(p):return (g.cross(p,V)/det,g.cross(U,p)/det)
        boxes=[]
        for poly in polys:
            points=[coords(p) for p in poly]
            boxes.append([(min(t[h] for t in points),max(t[h] for t in points)) for h in (0,1)])
        comparisons=[]
        for i,j in product(range(4),repeat=2):
            ranges=[range(int((boxes[i][h][0]-boxes[j][h][1]).ceil()),
                          int((boxes[i][h][1]-boxes[j][h][0]).floor())+1) for h in (0,1)]
            for n,m in product(*ranges):
                if i==j and n==m==0:continue
                overlap=g.clipped(polys[i],[p+n*U+m*V for p in polys[j]])
                assert not overlap or g.area(overlap)==0,(label,i,j,n,m)
                comparisons.append((i,j,n,m))
        counts[label]=len(comparisons)
    print('PASS independent reciprocal-V whole-cone geometry: '+str(support_checks)+' supporting determinants,6 full seams,8 directed line occurrences,5 interval strata;')
    print('PASS independent reciprocal-V formal closure/area, all five ratio strata plus ratio1: '+str(counts))

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
