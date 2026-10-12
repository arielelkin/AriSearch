#!/usr/bin/env python3
"""Twelve exact necessary area/perimeter gates for H -> two prescribed pentagons.
This does not enumerate attachment graphs or assert a dissection exists.
Zero-dimensional ideals cannot yield varying angles of the prescribed shapes.
"""
import argparse
import fcntl
import hashlib
import json
import time
from pathlib import Path
from sage.all import AA, CyclotomicField, PolynomialRing, QuadraticField

K = CyclotomicField(10)
w = K.gen()
F = QuadraticField(5, 'sqrt5', embedding=AA(5).sqrt())
phi = (1+F.gen())/2
R = PolynomialRing(F, names=('s','t','a','b','r','c'))
s,t,a,b,r,c = R.gens()


def split(z):
    z0,z1,z2,z3 = K(z).vector()
    return R(F(z0-z2)-phi*z3), R(F(z1)+phi*(z2+z3))


def add(x,y):
    return x[0]+y[0],x[1]+y[1]


def sub(x,y):
    return x[0]-y[0],x[1]-y[1]


def mul(x,y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]+phi*x[1]*y[1]


def norm(x):
    return x[0]**2+phi*x[0]*x[1]+x[1]**2


def cross(x,y):
    return x[0]*y[1]-x[1]*y[0]


def area(poly):
    # Twice area divided by Im(w), common positive scale for every polygon.
    return sum(cross(x,y) for x,y in zip(poly,poly[1:]+poly[:1]))


def geometry():
    zero,one,W = split(0),split(1),split(w)
    J=(s,t)
    KK=add(split(w**2),mul(split(w**6),sub(J,one)))
    LL=add(one,mul(split(w**7),sub(sub(J,one),W)))
    Jp=add(one,mul(split(w**4),sub(J,one)))
    Jpp=add(W,mul(split(w**6),sub(J,W)))
    J2=sub(split(1+w+w**2),J)
    H=[zero,Jp,one,J,W,Jpp]
    P1=[zero,Jp,one,LL,KK]
    P2=[KK,LL,split(1+w**2),J2,split(w**2)]
    norms={'a':norm(sub(J,split(1+w))), 'b':norm(sub(J,one)),
           'r':norm(sub(J,W)), 'c':norm(sub(KK,LL))}
    for poly, word in [(H,'abbrra'),(P1,'abaca'),(P2,'crrab')]:
        assert all(norm(sub(poly[(i+1)%len(poly)],v)) == norms[letter]
                   for i,(v,letter) in enumerate(zip(poly,word)))
    return H,P1,P2,norms


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    path=Path(args.output)
    lock=path.with_suffix(path.suffix+'.lock').open('a+')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    H,P1,P2,norms=geometry()
    areaH,area1,area2=map(area,(H,P1,P2))
    base=[a*a-norms['a'],b*b-norms['b'],r*r-norms['r'],c*c-norms['c']]
    cases=[('P1+P2','b',areaH-area1-area2,b-a-c),
           ('P1+P2','r',areaH-area1-area2,r-a-c),
           ('2P1','a',areaH-2*area1,2*a+c-r-a),
           ('2P1','b',areaH-2*area1,2*a+c-r-b),
           ('2P1','c',areaH-2*area1,2*a+c-r-c),
           ('2P2','a',areaH-2*area2,r+c-a),
           ('2P2','b',areaH-2*area2,r+c-b)]
    cases += [('2P1 negative orientation','a',areaH+2*area1,2*a+c-r-a),
              ('2P1 negative orientation','b',areaH+2*area1,2*a+c-r-b),
              ('2P1 negative orientation','c',areaH+2*area1,2*a+c-r-c),
              ('2P2 negative orientation','a',areaH+2*area2,r+c-a),
              ('2P2 negative orientation','b',areaH+2*area2,r+c-b)]
    assert areaH==2 and area1+area2==1+F.gen() and F.gen()>1
    result={'status':'twelve necessary area/perimeter gates; absolute-area signs included',
            'mixed_absolute_area_obstruction':'abs(A1)+abs(A2) >= abs(A1+A2) = 1+sqrt5 > 2 = abs(AH)',
            'mixed_two_ideal_rows_role':'original positive-orientation controls; universal mixed exclusion uses absolute-area inequality',
            'same_shape_area_signs_checked':[1,-1],
            'domain':'one straight cut of strict H into P1+P2,2P1,or2P2, prescribed Ammann P1(J),P2(J)',
            'coordinates_source':'research/lemmas/ammann-two-class-reconstruction.md',
            'field':'Q(sqrt(5)), positive embedding',
            'variables':list(R.variable_names()),
            'side_norms':{k:str(v) for k,v in norms.items()},
            'scaled_areas':{'H':str(areaH),'P1':str(area1),'P2':str(area2)},
            'base_equations':list(map(str,base)),
            'necessary_only':True,'sign_and_convexity_not_imposed':True,
            'zero_dimensional_specializations_not_classified':True,
            'rows':[]}
    for family, shared, ae, pe in cases:
        start=time.monotonic()
        I=R.ideal(base+[ae,pe]);G=I.groebner_basis();d=int(I.dimension())
        pure_powers={}
        if d==0:
            for g in G:
                powers=g.lm().exponents()[0]
                live=[i for i,x in enumerate(powers) if x]
                if len(live)==1:
                    pure_powers[str(R.gen(live[0]))]=int(powers[live[0]])
            assert len(pure_powers)==6
        row={'family':family,'shared_side':shared,'area_equation':str(ae),
             'perimeter_equation':str(pe),'ideal_dimension':d,
             'groebner_basis':list(map(str,G)),
             'pure_power_leading_monomials':pure_powers,
             'varying_angle_family_excluded':d<=0,
             'elapsed_seconds':round(time.monotonic()-start,4)}
        result['rows'].append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='groebner_basis'}),flush=True)
        path.write_text(json.dumps(result,indent=2)+'\n')
    result['complete']=True
    result['free_angle_route_excluded']=all(x['varying_angle_family_excluded'] for x in result['rows'])
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['replay']='conda run --no-capture-output -n arisearch python research/searches/boundary-attachment-ammann-h-gate.py --output '+args.output
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'complete':True,'free_angle_route_excluded':result['free_angle_route_excluded']}),flush=True)


if __name__=='__main__':
    main()
