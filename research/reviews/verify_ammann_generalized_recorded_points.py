#!/usr/bin/env python3
"""Independently check every retained real point, not enumeration completeness.

Replay: MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n
arisearch python3 research/reviews/verify_ammann_generalized_recorded_points.py
"""
import itertools
import argparse
import json
from fractions import Fraction
from pathlib import Path
from sage.all import AA, QQ, QQbar, PolynomialRing

w = QQbar.zeta(10)
ii = QQbar(-1).sqrt()
Qx = PolynomialRing(QQ,'x')


def decode(poly, printed):
    # The printed approximate value only selects among exact AA roots.
    target = QQ(Fraction(printed.replace('?','')))
    roots = [r for r,m in Qx(poly).roots(AA) if abs(r-target) < AA(QQ(1)/10**10)]
    assert len(roots)==1,(poly,printed,roots)
    return roots[0]


def vector(raw):
    return sum(QQ(c)*w**i for i,c in enumerate(raw))


def evaluate(forms, parameters):
    return [sum(vector(v)*(1 if k=='c' else parameters[int(k)]) for k,v in f.items()) for f in forms]


def det(a,b):
    q = a.conjugate()*b
    return AA((q-q.conjugate())/(2*ii))


def convex(P):
    if any(P[i]==P[i-1] for i in range(len(P))):
        return False
    if any(det(P[(i+1)%len(P)]-P[i],v-P[i])<0 for i in range(len(P)) for v in P):
        return False
    return sum(det(P[i],P[(i+1)%len(P)]) for i in range(len(P))) > 0


def reduce_flat(P):
    return [P[i] for i in range(len(P))
            if not (det(P[i]-P[i-1],P[(i+1)%len(P)]-P[i])==0
                    and AA(((P[i]-P[i-1]).conjugate()*(P[(i+1)%len(P)]-P[i])).real())>0)]


def norm(z):
    return z*z.conjugate()


def congruent(P,Q):
    if len(P)!=len(Q):
        return False
    n=len(P)
    return any(all(norm(P[i]-P[j])==norm(Q[(k+d*i)%n]-Q[(k+d*j)%n])
                   for i,j in itertools.combinations(range(n),2))
               for k in range(n) for d in (1,-1))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    cert=json.loads(Path('research/certificates/ammann-two-class-generalized.json').read_text())
    point_count=0
    surviving=set()
    for group,forms_record in zip(cert['stage4_group_search'],cert['stage3_pairwise']):
        assert (group['thin'],group['thick'])==(forms_record['thin'],forms_record['thick'])
        for combination in group['nonunit_complete_combinations']:
            assert combination['dim']==0
            for point in combination['real_points']:
                values=[decode(p,v) for p,v in zip(point['minpolys'],point['point'])]
                parameters={j:QQbar(values[2*i])+QQbar(values[2*i+1])*w for i,j in enumerate(group['params'])}
                polys=[evaluate(forms,parameters) for forms in forms_record['class_vertex_forms']]
                globally_convex=all(convex(P) for P in polys)
                reduced=[reduce_flat(P) for P in polys]
                reps=[]
                for P in reduced:
                    if not any(congruent(P,Q) for Q in reps):
                        reps.append(P)
                assert len(reps)==point['classes_at_point']
                assert globally_convex==point['all_tiles_weakly_convex']
                if globally_convex and len(reps)<=2:
                    hexagons=[P for P in reps if len(P)==6]
                    assert hexagons
                    P=hexagons[0]
                    assert all(P[i]+P[i+3]==P[0]+P[3] for i in range(3))
                    surviving.add((group['thin'],group['thick'],tuple(values[:-1])))
                point_count+=1
    assert len(surviving)==2
    report={'retained_real_point_rows_checked':point_count,'distinct_convex_two_class_points':len(surviving),
            'each_has_centrally_symmetric_hexagon':True,
            'scope':'All stored stage4 real points; does not certify missing/unit ideals, omitted graph cases, or completeness of roots.'}
    if args.output:
        Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
