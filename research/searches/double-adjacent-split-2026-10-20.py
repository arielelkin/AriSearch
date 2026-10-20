"""Exact rational double-adjacent-split local patch.

Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/double-adjacent-split-2026-10-20.py
"""
from fractions import Fraction as F
from itertools import product

from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from math import atan2, degrees
from sage.all import AA, QQ, RealIntervalField

src = Path(__file__).with_name('terra-p5p5-halfside-2026-10-20.py')
spec = spec_from_file_location('halfside', src)
g = module_from_spec(spec)
spec.loader.exec_module(g)

P = ((F(0), F(0)), (F(2), F(0)), (F(2), F(2)),
     (F(-1), F(3)), (F(-238, 169), F(240, 169)))
Q = ((F(0), F(0)), (F(1), F(0)), (F(1), F(1)),
     (F(1, 2), F(7, 5)), (F(-5, 13), F(12, 13)))


def all_outside(poly, target):
    out = []
    for j, edge in enumerate(g.edges(poly)):
        if g.norm2(g.sub(*edge)) != g.norm2(g.sub(*target)):
            continue
        for rev, refl in product((0, 1), repeat=2):
            t = target if not rev else target[::-1]
            placed = g.mapped(poly, edge, t, refl)
            if not g.interiors_intersect(P, placed):
                out.append((j, rev, refl, placed))
    return out


def point_angle_data(poly):
    return tuple((g.norm2(g.sub(poly[i-1], poly[i])),
                  g.norm2(g.sub(poly[(i+1)%len(poly)], poly[i])),
                  g.dot(g.sub(poly[i-1], poly[i]),
                        g.sub(poly[(i+1)%len(poly)], poly[i])))
                 for i in range(len(poly)))


def rao_screen(poly):
    """Certified angle interval plus exact length screen of Rao types 1-15."""
    rao_src=Path(__file__).with_name('convex-substitution-shapes.py')
    spec=spec_from_file_location('rao_for_double_split',rao_src)
    mod=module_from_spec(spec); spec.loader.exec_module(mod)
    R=RealIntervalField(100)
    angle=[]
    for i in range(5):
        u=g.sub(poly[i-1],poly[i]); v=g.sub(poly[(i+1)%5],poly[i])
        prod=g.norm2(u)*g.norm2(v); dp=g.dot(u,v)
        c=R(QQ(dp.numerator)/dp.denominator)/R(QQ(prod.numerator)/prod.denominator).sqrt()
        angle.append(c.arccos()*R(180)/R.pi())
    length=[AA(QQ(g.norm2(g.sub(b,a)).numerator)/
               g.norm2(g.sub(b,a)).denominator).sqrt() for a,b in g.edges(poly)]
    hits=[]; possible_angle=[]
    for typ,(aeqs,leqs) in mod.RAO.items():
        for sign in (1,-1):
            for off in range(5):
                amap=[(off+sign*i)%5 for i in range(5)]
                a=[angle[i] for i in amap]
                if not all(R(36*target) in sum((coef*x for coef,x in zip(row,a)),R(0))
                           for row,target in aeqs): continue
                possible_angle.append((typ,sign,off))
                smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
                if all(sum((coef*length[i] for coef,i in zip(row,smap)),AA(0))==0
                       for row in leqs): hits.append((typ,sign,off))
    return possible_angle,hits


def main():
    assert min(g.turns(P)) > 0 and min(g.turns(Q)) > 0
    assert g.area2(P) != g.area2(Q)
    for name, poly in (('P', P), ('Q', Q)):
        angles=[]
        for i in range(5):
            u=g.sub(poly[i-1],poly[i]); v=g.sub(poly[(i+1)%5],poly[i])
            angles.append(degrees(atan2(abs(float(g.cross(u,v))),float(g.dot(u,v)))))
        print(name, 'vertices', poly)
        print(name, 'area2', g.area2(poly), 'turns', g.turns(poly),
              'sides2', tuple(g.norm2(g.sub(b,a)) for a,b in g.edges(poly)),
              'angle_data', point_angle_data(poly),
              'angles_degrees_recon',angles,
              'supplementary', g.consecutive_supplementary(poly))
        print(name,'Rao angle possible / full hits',rao_screen(poly))
    O=P[0]
    host_ends=(P[1], P[4])
    firsts=[]; lasts=[]
    for E in host_ends:
        M=((O[0]+E[0])/2, (O[1]+E[1])/2)
        # Use native side 0, beta angle at native vertex 0.
        first=[r for r in all_outside(Q,(O,M)) if r[0]==0 and r[3][0]==O]
        last=[r for r in all_outside(Q,(M,E)) if r[0]==0 and r[3][1]==M]
        print('side',E,'mid',M,'first options',[(x[0],x[1],x[2]) for x in first],
              'last options',[(x[0],x[1],x[2]) for x in last])
        assert len(first)==len(last)==1
        firsts.append(first[0][3]); lasts.append(last[0][3])
    patch=(P,firsts[0],lasts[0],firsts[1],lasts[1])
    assert all(not g.interiors_intersect(a,b) for a,b in product(patch,repeat=2) if a is not b)
    for i,t in enumerate(patch): print('patch',i,t)
    # Two exact distinct one-tile continuations of the same exposed Q side.
    continuation=[]
    for h,host in enumerate(patch):
        for k,target in enumerate(g.edges(host)):
            # Skip occupied sides; the intersection gate will also reject
            # placements inside the present patch.
            cont=[]
            for species,poly in (('P',P),('Q',Q)):
                for j,e in enumerate(g.edges(poly)):
                    if g.norm2(g.sub(*e))!=g.norm2(g.sub(*target)): continue
                    for rev,refl in product((0,1),repeat=2):
                        t=target if not rev else target[::-1]
                        cand=g.mapped(poly,e,t,refl)
                        if all(not g.interiors_intersect(cand,z) for z in patch):
                            if cand not in patch: cont.append((species,j,rev,refl,cand))
            if cont:
                continuation.append((h,k,cont))
                print('continuations',h,k,[(c[:4]) for c in cont])
    assert continuation
    branch=[c for h,k,c in continuation if (h,k)==(1,3)][0]
    assert len({c[4] for c in branch})==2
    assert not any((h,k)==(1,2) for h,k,_ in continuation)
    print('side 1:3 has two distinct Q branches; side 1:2 has zero whole-edge branches')
    # Midpoint outgoing nonhost rays must coincide for a completed flat star.
    for E,a,b in zip(host_ends,firsts,lasts):
        M=((O[0]+E[0])/2,(O[1]+E[1])/2)
        u=g.open_ray(a,M,g.sub(E,O)); v=g.open_ray(b,M,g.sub(E,O))
        print('midpoint seam',M,u,v,'closed',g.cross(u,v)==0 and g.dot(u,v)>0)
        assert g.cross(u,v)==0 and g.dot(u,v)>0
    # At O, the two Q copies share a unit native edge by construction.
    common=set(firsts[0]).intersection(firsts[1])
    print('first-Q common vertices',common)
    assert len(common)>=2 and O in common
    # P reflected across either split host side collides with the other first Q.
    for E,other in zip(host_ends,firsts[::-1]):
        reflected=[]
        for j,e in enumerate(g.edges(P)):
            if g.norm2(g.sub(*e))!=g.norm2(g.sub(E,O)): continue
            for rev,refl in product((0,1),repeat=2):
                pp=g.mapped(P,e,(O,E) if not rev else (E,O),refl)
                if pp==P or g.interiors_intersect(P,pp): continue
                reflected.append((j,rev,refl,pp,g.interiors_intersect(pp,other)))
        print('P/P across side',E,'options/interference',[(x[:3],x[4]) for x in reflected])
        # The simple mirror of P through its same side is one of these options.
        native_side=0 if E==host_ends[0] else 4
        assert any(x[0]==native_side and x[4] for x in reflected)
    print('scope: exact five-tile local patch only; no plane existence or universal forcing')


if __name__=='__main__': main()
