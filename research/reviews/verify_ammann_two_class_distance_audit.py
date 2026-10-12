#!/usr/bin/env python3
"""Independent distance-matrix audit of the recorded Ammann collapse domain.

Uses neither the search's edge-proportionality equations nor its roots.
Replay: mise exec -- conda run --no-capture-output -n arisearch python3
  research/reviews/verify_ammann_two_class_distance_audit.py [OUTPUT.json]
"""
import itertools
import json
import sys
from sage.all import CyclotomicField, PolynomialRing, QQbar, AA

F = CyclotomicField(10)
w = F.gen()
R = PolynomialRing(F, ['s', 't'], order='lex')
s, t = R.gens()
embedding = F.hom([QQbar.zeta(10)])
ii = QQbar(-1).sqrt()


def bar(p):
    return R({m: c.conjugate() for m, c in R(p).dict().items()})


def norm(p):
    return R(p * bar(p))


z = s + t*w
jp = 1+w**4*(z-1)
jpp = w+w**6*(z-w)
kp = w**2+w**6*(z-1)
lp = 1+w**7*(z-1-w)
j2 = 1+w+w**2-z
tiles = {'H': list(map(R, [0,jp,1,z,w,jpp])),
         'P1': list(map(R, [0,jp,1,lp,kp])),
         'P2': list(map(R, [kp,lp,1+w**2,j2,w**2]))}


def cross(a, b):
    return R(bar(a)*b-a*bar(b))


def at(p, vals):
    return sum(embedding(c)*vals[0]**m[0]*vals[1]**m[1]
               for m,c in p.dict().items())


def convex(P):
    """Global supporting-half-plane test; rejects zero edges and zero area."""
    edges = [P[(i+1)%len(P)]-P[i] for i in range(len(P))]
    if any(e == 0 for e in edges):
        return False
    for i,e in enumerate(edges):
        for v in P:
            q = e.conjugate()*(v-P[i])
            if AA((q-q.conjugate())/(2*ii)) < 0:
                return False
    area = sum(P[i].conjugate()*P[(i+1)%len(P)] for i in range(len(P)))
    return AA((area-area.conjugate())/(2*ii)) > 0


def main():
    rows = []
    cases = [('P1-P2', tiles['P1'], tiles['P2'], [])]
    for m in range(6):
        H = tiles['H']
        straight = cross(H[m]-H[m-1], H[(m+1)%6]-H[m])
        for target in ('P1','P2'):
            cases.append(('H-delete-%d-%s'%(m,target),
                          [H[i] for i in range(6) if i != m],
                          tiles[target], [straight]))
    for label,P,Q,extra in cases:
        n = len(P)
        for direction in (1,-1):
            for shift in range(n):
                # All pair distances suffice for isometry, including mirrors.
                eqs = [norm(P[i]-P[j])-norm(Q[(shift+direction*i)%n]-Q[(shift+direction*j)%n])
                       for i,j in itertools.combinations(range(n),2)] + extra
                ideal = R.ideal(eqs)
                dimension = int(ideal.dimension())
                assert dimension <= 0, (label,direction,shift,dimension)
                row = {'case':label,'direction':direction,'shift':shift,
                       'dimension':dimension,'groebner_basis':list(map(str,ideal.groebner_basis())),
                       'real_points':[]}
                if dimension == 0:
                    for v in ideal.variety(QQbar):
                        vals = [v[s],v[t]]
                        if any(x.imag() != 0 for x in vals):
                            continue
                        polys = {key:[at(p,vals) for p in ps] for key,ps in tiles.items()}
                        row['real_points'].append({'s':str(AA(vals[0])), 't':str(AA(vals[1])),
                            'minpolys':[str(x.minpoly()) for x in vals],
                            'all_tiles_convex':all(convex(ps) for ps in polys.values())})
                rows.append(row)
        print(label, 'checked', flush=True)
    surviving = [p for row in rows for p in row['real_points'] if p['all_tiles_convex']]
    a = (AA(5)+AA(5).sqrt())/10
    assert len(surviving) == 1, surviving
    assert surviving[0]['s'] == str(a) and surviving[0]['t'] == str(a)
    report = {'scope':'13 pentagon correspondences, all five shifts, both directions; straightness imposed for H deletion; no <=4-side strata classified',
              'correspondences':len(rows),'surviving':surviving,'rows':rows}
    if len(sys.argv)>1:
        with open(sys.argv[1],'w') as f:
            json.dump(report,f,indent=2)
    print('PASS: 130 distance systems; one globally convex point', flush=True)


if __name__ == '__main__':
    main()
