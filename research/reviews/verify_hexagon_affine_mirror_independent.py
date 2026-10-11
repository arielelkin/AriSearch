#!/usr/bin/env python3
"""Fresh exact audit: polygon clipping, lattice-coordinate bounds, full H systems.

This does not import or call the author's verifier. Coordinates are separately
constructed from the proof formulas and compared with every certificate entry.
Monohedral conclusions depend on Zhu--Wang--Yan 2508.01404v2 Main Theorem.
"""
from sage.all import AA, QQ, QQbar, vector, matrix, floor, ceil
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]


def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def area(poly):
    if len(poly) < 3:
        return AA(0)
    return sum(cross(poly[j], poly[(j+1) % len(poly)])
               for j in range(len(poly)))/2


def clip_polygon(subject, clipper):
    """Closed half-plane clipping; exact intersection area, no projection test."""
    result = list(subject)
    for j in range(len(clipper)):
        if not result:
            break
        origin = clipper[j]
        edge = clipper[(j+1) % len(clipper)] - origin
        old, result = result, []
        previous = old[-1]
        hp = cross(edge, previous-origin)
        for current in old:
            hc = cross(edge, current-origin)
            if (hp >= 0) != (hc >= 0):
                result.append(previous + (current-previous)*hp/(hp-hc))
            if hc >= 0:
                result.append(current)
            previous, hp = current, hc
    return result


def reinhardt_systems(poly):
    """All twelve dihedral labelings; exact angle sums via unit turn products.

For three strictly convex corners, the sum of exterior turns lies in (0,3pi).
Their unit-complex product is -1 precisely when this sum is pi, equivalent
here to the sum of interior angles being 2pi. Thus no floating angles enter.
"""
    hits = []
    I = QQbar.gen()
    for step in (-1, 1):
        for base in range(6):
            vs = [poly[(base+step*j) % 6] for j in range(6)]
            es = [vs[(j+1) % 6]-vs[j] for j in range(6)]
            norms2 = [e.dot_product(e) for e in es]
            turns = []
            interior_cos = []
            for j in range(6):
                previous, current = es[j-1], es[j]
                den = (norms2[j-1]*norms2[j]).sqrt()
                turns.append(QQbar(previous.dot_product(current)/den)
                             + I*QQbar(step*cross(previous, current)/den))
                interior_cos.append(-previous.dot_product(current)/den)
            h1 = (norms2[2] == norms2[5]
                  and turns[0]*turns[1]*turns[2] == -1)
            h2 = (norms2[1] == norms2[3] and norms2[2] == norms2[5]
                  and turns[0]*turns[1]*turns[3] == -1)
            h3 = (all(norms2[2*k] == norms2[2*k+1] for k in range(3))
                  and all(interior_cos[j] == -QQ(1)/2 for j in (0, 2, 4)))
            if h1 or h2 or h3:
                hits.append((base, step, h1, h2, h3))
    return hits


def main():
    cert = json.loads((ROOT/'research/certificates/hexagon-affine-mirror-escape.json').read_text())
    w, h = AA(3).sqrt(), AA(5).sqrt()
    p, g = w*h, w+h
    assert g**4-16*g**2+4 == 0 and QQ(39)/10 < g < 4
    assert (g-2/g)/2 == w and (g+2/g)/2 == h
    assert cert['field']['primitive_polynomial'] == 'g^4-16*g^2+4'
    assert cert['field']['coordinate_basis'] == ['1', 'w', 'h', 'w*h']
    assert cert['source_parameter'] == {'cos_a': 'w*h/4', 'sin_a': '1/4'}
    assert cert['affine_matrix'] == [['2', '0'], ['0', '1']]
    def point(x, y):
        return vector(AA, [x, y])
    A = [point(0,0), point(2,0), point(2+(p-w)/4,(3*h+1)/8),
         point(1+(p-w)/4,(4*w+3*h+1)/8),
         point(1-(p+w)/4,(4*w+3*h-1)/8), point(-(p+w)/4,(3*h-1)/8)]
    B = [point(0,0), point(p/2,QQ(1)/4), point((3*p+w)/4,(3*h+1)/8),
         point(p/2,3*h/4), point(0,(3*h+1)/4), point((-p+w)/4,(3*h+1)/8)]
    t = point(2+(p-w)/4,-(3*h+1)/8)
    u = point(1+p/2,(2*w+3*h)/4)
    v = point(1+p/2,-(2*w+3*h)/4)
    def decode_point(cs):
        assert len(cs) == 2 and all(len(c) == 4 for c in cs)
        return vector(AA, [sum(QQ(a)*b for a,b in zip(c,[1,w,h,p])) for c in cs])
    assert [decode_point(z) for z in cert['A_vertices']] == A
    assert [decode_point(z) for z in cert['B_vertices']] == B
    assert decode_point(cert['B_motif_translation']) == t
    assert [decode_point(z) for z in cert['lattice']] == [u,v]
    S = matrix(AA,[[1,0],[0,-1]])
    D = matrix(AA,[[2,0],[0,1]])
    Z = matrix(AA,[[p/4,-QQ(1)/4],[QQ(1)/4,p/4]])
    assert D*S == S*D and Z.transpose()*Z == matrix.identity(AA,2)
    assert QQ(1)/p < QQ(1)/w
    A0 = [D.inverse()*z for z in A]
    B0 = [Z.inverse()*D.inverse()*z for z in B]
    for source in (A0,B0):
        assert all((source[(j+1)%6]-source[j]).norm() == 1 for j in range(6))
    t1 = A0[1]-Z.inverse()*A0[3]
    t2 = A0[1]-Z*B0[5]
    assert set(tuple(D*(Z.inverse()*z+t1)) for z in A0) == set(tuple(S*z) for z in A)
    assert D*t2 == t
    source_motif = [A,[D*(Z.inverse()*z+t1) for z in A0], [D*(Z*z+t2) for z in B0]]
    seams = cert['source_seams']
    shifts = cert['seam_translation_coefficients']
    assert len(seams) == len(shifts) == 9
    assert sorted(tuple(side) for seam in seams for side in seam) == list(product(range(3),range(6)))
    for ((f,j),(g,k)),(n,m) in zip(seams,shifts):
        delta = n*u+m*v
        assert source_motif[f][j] == source_motif[g][(k+1)%6]+delta
        assert source_motif[f][(j+1)%6] == source_motif[g][k]+delta
    for polygon in (A,B):
        assert area(polygon) > 0
        for j in range(6):
            e = polygon[(j+1)%6]-polygon[j]
            assert all(cross(e,polygon[k]-polygon[j]) > 0
                       for k in range(6) if k not in (j,(j+1)%6))
    lengths = [[(poly[(j+1)%6]-poly[j]).norm()**2 for j in range(6)] for poly in (A,B)]
    assert len(set(lengths[0])) == 5 and len(set(lengths[1])) == 3
    assert all(len(set(ls)) > 1 for ls in lengths)
    # Full systems, including required angle equations, in every cyclic/reversed labeling.
    assert reinhardt_systems(A) == []
    assert reinhardt_systems(B) == []
    assert area(A) == w+3*h/2 and area(B) == 11*w/4
    ratio = area(B)/area(A)
    assert ratio == p/2-1 and p*p == 15
    assert ratio not in QQ
    trace = 2*((p/2)**2-(QQ(1)/4)**2)/((p/2)**2+(QQ(1)/4)**2)
    assert trace == QQ(118)/61 and QQ(trace).denominator() != 1
    motifs = [A,list(reversed([S*z for z in A])),[z+t for z in B]]
    lattice = matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    assert lattice.det() != 0
    coordinates = [[lattice.inverse()*z for z in motif] for motif in motifs]
    comparisons = 0
    for first, second in product(range(3),repeat=2):
        bounds = []
        for axis in range(2):
            lo = ceil(min(z[axis] for z in coordinates[first])-max(z[axis] for z in coordinates[second]))
            hi = floor(max(z[axis] for z in coordinates[first])-min(z[axis] for z in coordinates[second]))
            bounds.append(range(int(lo),int(hi)+1))
        for n,m in product(*bounds):
            if first == second and n == m == 0:
                continue
            translated = [z+n*u+m*v for z in motifs[second]]
            intersection = clip_polygon(motifs[first],translated)
            assert area(intersection) == 0,(first,second,n,m)
            comparisons += 1
    assert sum(area(m) for m in motifs) == abs(lattice.det()) == 19*w/4+3*h
    print(f'PASS: separate exact coordinates, all 24 dihedral labelings fail full Reinhardt systems, {comparisons} lattice-coordinate clipping comparisons, motif-area=covolume, two classes, irrational area ratio and direction.')


if __name__ == '__main__':
    main()
