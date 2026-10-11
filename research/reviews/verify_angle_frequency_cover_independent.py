#!/usr/bin/env python3
"""Independent exact replay of every retained angle-cover certificate.

No producer or solver imports. Frequency witnesses use fractions.Fraction;
geometry uses exact cyclotomic/real-algebraic arithmetic. The finite domain
is independently reconstructed from multiplicity vectors, not read from the
producer or trusted from certificate counters.
"""
import argparse
from fractions import Fraction
from itertools import product
import json
from math import gcd
from pathlib import Path
from sage.all import AA, QQbar, CyclotomicField

DOMAIN = tuple(range(100, 171, 10))


def multiplicities(total, places):
    if places == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in multiplicities(total-first, places-1):
                yield (first,)+rest


def expand(counts):
    return tuple(v for v, count in zip(DOMAIN, counts) for _ in range(count))


def check_frequency(data):
    words = sorted(expand(c) for c in multiplicities(6, len(DOMAIN))
                   if sum(v*n for v,n in zip(DOMAIN,c)) == 720)
    full_stars = sorted(expand(c) for c in multiplicities(3, len(DOMAIN))
                        if sum(v*n for v,n in zip(DOMAIN,c)) == 360)
    assert len(words) == 46 and len(full_stars) == 7
    all_pairs = {(a,b) for i,a in enumerate(words) for b in words[i:]}
    assert len(all_pairs) == 1081
    covered = {}
    for a,b in all_pairs:
        present = set(a+b)
        legal = [t for t in full_stars if set(t) <= present]
        if set(v for t in legal for v in t) == present:
            covered[a,b] = legal
    assert len(covered) == 692
    assert data['angle_domain'] == list(DOMAIN)
    assert data['angle_multisets'] == len(words)
    assert data['unordered_pair_domain'] == len(all_pairs)
    assert data['angle_covered_pairs'] == len(covered)
    assert data['infeasible_pairs'] == 11
    accepted, rejected = data['certified_feasible'], data['certified_rejections']
    assert len(accepted) == 681 and len(rejected) == 11
    seen = set()
    for is_rejected, rows in ((False,accepted), (True,rejected)):
        for entry in rows:
            a,b = tuple(entry['A']),tuple(entry['B'])
            key = a,b
            assert key in covered and key not in seen
            seen.add(key)
            legal = covered[key]
            assert entry['stars'] == [list(t) for t in legal]
            present = set(a+b)
            if not is_rejected:
                fa,fb = Fraction(entry['fa']),Fraction(entry['fb'])
                xs = [Fraction(v) for v in entry['star_frequencies']]
                assert len(xs) == len(legal)
                assert fa>=0 and fb>=0 and fa+fb==1
                assert all(x>=0 for x in xs)
                for v in present:
                    assert sum(t.count(v)*x for t,x in zip(legal,xs)) == a.count(v)*fa+b.count(v)*fb
            else:
                raw = entry['separating_weights']
                assert set(raw) == {str(v) for v in present}
                w = {v:Fraction(raw[str(v)]) for v in present}
                assert all(sum(w[v] for v in t)>=0 for t in legal)
                assert sum(w[v] for v in a)<=-1
                assert sum(w[v] for v in b)<=-1
    assert seen == set(covered)
    return words,full_stars,covered


def dot(u,v):
    return sum(x*y for x,y in zip(u,v))


def sub(u,v):
    return tuple(x-y for x,y in zip(u,v))


def det(u,v):
    return u[0]*v[1]-u[1]*v[0]


def check_geometry(concrete):
    K = CyclotomicField(36)
    z = K.gen()
    root = QQbar.zeta(36)
    assert root**12-root**6+1 == 0
    assert K.degree() == 12
    # Explicitly verify uniqueness of the exact isolating rectangle among
    # all twelve roots of Phi_36, not just that the chosen root lies there.
    candidates = [root**k for k in range(36) if gcd(k,36)==1]
    in_box = [q for q in candidates
              if AA(98)/100<q.real()<AA(99)/100
              and AA(17)/100<q.imag()<AA(18)/100]
    assert in_box == [root] and len(candidates)==12
    assert z**12-z**6+1 == 0
    embed = K.hom([root],QQbar)
    def coeffs(seq):
        assert len(seq)<=12
        return sum(K(Fraction(s))*z**j for j,s in enumerate(seq))
    def real_coord(seq):
        q = embed(coeffs(seq))
        assert q.imag()==0
        return AA(q.real())
    def normal(degree):
        assert degree % 10 == 0
        q = root**(degree//10)
        return AA(q.real()),AA(q.imag())
    expected = {'A':(100,100,100,140,140,140),
                'B':(100,100,110,130,140,140)}
    for name,angles in expected.items():
        row = concrete[name]
        assert tuple(row['angles_degrees']) == angles
        theta = [0]
        for angle in angles[1:]:
            theta.append(theta[-1]+180-angle)
        assert row['normal_degrees'] == theta
        ns = [normal(t) for t in theta]
        assert all(dot(n,n)==1 for n in ns)
        raw = row['coordinates_in_zeta36']
        assert len(raw)==6 and all(len(p)==2 for p in raw)
        points = [tuple(real_coord(c) for c in p) for p in raw]
        assert len(set(points)) == 6
        for j,p in enumerate(points):
            for k,n in enumerate(ns):
                if k in {(j-1)%6,j}:
                    assert dot(n,p)==1
                else:
                    assert dot(n,p)<1
            # Derive the actual vertex angle from its two incident edge
            # vectors, independently of the producer's normal dot test.
            prev_ray = sub(points[j-1],p)
            next_ray = sub(points[(j+1)%6],p)
            norm_product = (dot(prev_ray,prev_ray)*dot(next_ray,next_ray)).sqrt()
            assert norm_product>0
            assert dot(prev_ray,next_ray)/norm_product == normal(angles[j])[0]
            incoming = sub(p,points[j-1])
            assert det(incoming,next_ray)>0
        twice_area = sum(det(points[j],points[(j+1)%6]) for j in range(6))
        assert twice_area>0
        # Normals and supplied vertices therefore define six genuine
        # supporting sides around the unit disk, with strict convexity.
        assert all(dot(n,(AA(0),AA(0)))<1 for n in ns)
    assert sorted(expected['A']) != sorted(expected['B'])
    present = sorted(set(expected['A']+expected['B']))
    stars = sorted(t for t in product(present,repeat=3)
                   if tuple(sorted(t))==t and sum(t)==360)
    assert stars == [(100,130,130),(110,110,140)]
    assert concrete['stars'] == [list(t) for t in stars]
    weights = {int(k):Fraction(v) for k,v in concrete['weights'].items()}
    assert weights == {100:Fraction(2),110:Fraction(-1),130:Fraction(-1),140:Fraction(2)}
    assert set(v for t in stars for v in t)==set(present)
    assert all(sum(weights[v] for v in t)==0 for t in stars)
    charges = [sum(weights[v] for v in expected[name]) for name in ('A','B')]
    assert charges == [12,6] and concrete['tile_charges'] == charges
    return expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate',nargs='?',
                        default='research/certificates/angle-frequency-cover-counterexample.json')
    args = parser.parse_args()
    assert __debug__, 'Assertions must be enabled'
    data = json.loads(Path(args.certificate).read_text())
    words,stars,covered = check_frequency(data)
    shapes = check_geometry(data['concrete_obstruction'])
    # The exhibited pair must occur among the independently checked rejects.
    key = tuple(sorted(shapes['A'])),tuple(sorted(shapes['B']))
    assert any((tuple(row['A']),tuple(row['B']))==key
               for row in data['certified_rejections'])
    print('PASS independent angle-frequency audit: 46 multisets, 1081 pairs, 692 covered; all 681 rational primals and 11 rational duals; unique cyclotomic root; both exact convex six-vertex shapes and all actual corner angles; charges 12, 6.')


if __name__=='__main__':
    main()
