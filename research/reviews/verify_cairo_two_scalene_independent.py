#!/usr/bin/env python3
"""Independent Cairo coordinates, circular links, and translation holonomy."""
from collections import Counter
from pathlib import Path
import hashlib
import json
from sage.all import AA, QQ, QuadraticField, PolynomialRing, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "research/certificates/cairo-two-scalene-torus.json"
K = QuadraticField(3, "w", embedding=AA(3).sqrt())
w = K.gen()
assert w*w == 3 and 1 < w < 2


def det(u, v):
    return u[0]*v[1] - u[1]*v[0]


def vertices(p, q, r):
    # Derive from side directions 0,90,150,240,300 degrees.
    edges = [vector([q, 0]), vector([0, p]), vector([-w*p/2, p/2]),
             vector([-q/2, -w*q/2]), vector([r/2, -w*r/2])]
    verts = [vector([p*0, p*0])]
    for e in edges:
        verts.append(verts[-1]+e)
    assert verts[-1] == verts[0]
    return verts[:-1], edges


def family_check():
    R = PolynomialRing(K, names=("p", "r"))
    p, r = R.gens()
    q = w*p-r
    v, edges = vertices(p, q, r)
    # Ordered nonadjacent support determinants, grouped by supporting side.
    expected = [[p*q, 3*p*q/2, w*q*r/2],
                [p*q, w*p*p/2, p*(q+r/2)],
                [p*(w*p+q)/2, w*p*p/2, p*q],
                [w*q*r/2, 3*p*q/2, p*q],
                [w*r*q/2, r*(p+w*q)/2, w*r*q/2]]
    for i in range(5):
        actual = [det(edges[i], v[j]-v[i]) for j in range(5)
                  if j not in (i, (i+1) % 5)]
        assert actual == expected[i]
    # The B formula is obtained from the same identities by p<->q, r->s.
    s = 2*p-w*r
    assert p+s == w*q
    vertices(q, p, s)


def main():
    family_check()
    data = json.loads(CERT.read_text())
    assert data["field"] == {"polynomial": "x^2-3", "root_interval": ["1", "2"]}
    assert data["parameters"] == {"p": "1", "r": "1/2"}
    p, r = K(1), K(1)/2
    q, s = w*p-r, 2*p-w*r
    assert len({p,q,r,s}) == 4 and min(p,q,r,s) > 0
    lengths = {"A": [q,p,p,q,r], "B": [p,q,q,p,s]}
    verts = {}
    edges = {}
    for n, pars in (("A", (p,q,r)), ("B", (q,p,s))):
        verts[n], edges[n] = vertices(*pars)
        encoded = [vector(K, [QQ(a)+QQ(b)*w for a,b in row]) for row in data[n]]
        assert encoded == verts[n]
        for i, e in enumerate(edges[n]):
            assert e.dot_product(e) == lengths[n][i]**2
            assert all(det(e, verts[n][j]-verts[n][i]) > 0
                       for j in range(5) if j not in (i, (i+1) % 5))
            nxt = edges[n][(i+1) % 5]
            assert det(e, nxt) > 0
            assert e.dot_product(nxt) == (0 if i in (0,2)
                else lengths[n][i]*lengths[n][(i+1) % 5]/2)
    assert r not in lengths["B"] and s not in lengths["A"]

    faces = data["faces"]
    assert faces == ["A", "A", "B", "B"]
    pairs = data["reversed_endpoint_pairs"]
    assert len(pairs) == 10
    twin = {}
    adj = {f: [] for f in range(4)}
    for left, right in pairs:
        f,i = left
        g,j = right
        assert 0 <= f < 4 and 0 <= g < 4 and f != g
        assert 0 <= i < 5 and 0 <= j < 5
        assert (f,i) not in twin and (g,j) not in twin
        assert lengths[faces[f]][i] == lengths[faces[g]][j]
        twin[f,i] = (g,j)
        twin[g,j] = (f,i)
        adj[f].append((g,i,j))
        adj[g].append((f,j,i))
    domain = {(f,i) for f in range(4) for i in range(5)}
    assert set(twin) == domain
    succ = {(f,i): (twin[f,i][0], (twin[f,i][1]-1) % 5) for f,i in domain}
    assert set(succ.values()) == domain
    unseen = set(domain)
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = [start]
        nxt = succ[start]
        while nxt != start:
            assert nxt not in cycle
            cycle.append(nxt)
            nxt = succ[nxt]
        unseen.difference_update(cycle)
        cycles.append(cycle)
    assert Counter(map(len, cycles)) == {3:4, 4:2}
    angles = [90,120,90,120,120]
    assert all(sum(angles[i] for f,i in c) == 360 for c in cycles)
    expected = [((0,0),(1,0),(2,0),(3,0)), ((0,2),(1,2),(2,2),(3,2)),
                ((0,1),(2,3),(3,4)), ((0,3),(1,4),(3,1)),
                ((0,4),(1,3),(2,1)), ((1,1),(2,4),(3,3))]
    assert {tuple(sorted(c)) for c in cycles} == {tuple(sorted(c)) for c in expected}
    assert len(cycles)-len(pairs)+len(faces) == 0

    # Independently develop a dual spanning tree, then compute each seam's
    # exact affine holonomy.  All residual linear parts must be identity.
    ident = matrix(K, 2, 2, [1,0,0,1])
    zero = vector(K, [0,0])
    def compose(a, b):
        return a[0]*b[0], a[0]*b[1]+a[1]
    def inverse(a):
        m = a[0].inverse()
        return m, -m*a[1]
    def relative(f,i,g,j):
        src = edges[faces[g]][j]
        target = -edges[faces[f]][i]
        norm = src.dot_product(src)
        cosine, sine = src.dot_product(target)/norm, det(src,target)/norm
        rot = matrix(K, [[cosine,-sine],[sine,cosine]])
        shift = verts[faces[f]][(i+1) % 5] - rot*verts[faces[g]][j]
        assert rot.transpose()*rot == ident and rot.det() == 1
        assert rot*verts[faces[g]][(j+1) % 5]+shift == verts[faces[f]][i]
        return rot, shift
    placements = {0: (ident,zero)}
    queue = [0]
    while queue:
        f = queue.pop(0)
        for g,i,j in adj[f]:
            if g not in placements:
                placements[g] = compose(placements[f], relative(f,i,g,j))
                queue.append(g)
    assert len(placements) == 4
    rot90 = matrix(K, [[0,-1],[1,0]])
    assert placements[1] == (-ident, vector(K, [-r/2,w*r/2]))
    assert placements[2] == (rot90, vector(K, [q,-p]))
    assert placements[3] == (-rot90, vector(K, [-q-r/2,p+w*r/2]))
    periods = []
    for (f,i),(g,j) in pairs:
        hol = compose(compose(placements[f], relative(f,i,g,j)), inverse(placements[g]))
        assert hol[0] == ident
        if hol[1] != zero:
            periods.append(hol[1])
    assert any(det(u,v) != 0 for u in periods for v in periods)
    u = vector(K, [w,-3])
    v = vector(K, [2*w-K(3)/4,-w/4])
    assert u in periods and v in periods
    lattice = matrix(K, [[u[0],v[0]],[u[1],v[1]]])
    assert lattice.det() == 6*w-3 > 0
    lattice_inverse = lattice.inverse()
    for t in periods:
        assert all(a in QQ and QQ(a).denominator() == 1 for a in lattice_inverse*t)
    motif = [[placements[f][0]*z+placements[f][1] for z in verts[faces[f]]]
             for f in range(4)]
    area = sum(sum(det(poly[i],poly[(i+1) % 5]) for i in range(5))/2 for poly in motif)
    assert area == lattice.det()

    # All possible interior overlaps are included by exact lattice-coordinate
    # bounding boxes.  Supporting-edge separation is exact and suffices for
    # convex polygons; area equality then gives full coverage mathematically.
    boxes = []
    for poly in motif:
        coordinates = [lattice_inverse*z for z in poly]
        boxes.append([(min(c[d] for c in coordinates), max(c[d] for c in coordinates))
                      for d in (0,1)])
    def separated(poly, other):
        return any(all(det(poly[(i+1) % 5]-poly[i], z-poly[i]) <= 0 for z in other)
                   for i in range(5))
    comparisons = 0
    for f in range(4):
        for g in range(4):
            ranges = []
            for d in (0,1):
                low = int(AA(boxes[f][d][0]-boxes[g][d][1]).ceil())
                high = int(AA(boxes[f][d][1]-boxes[g][d][0]).floor())
                ranges.append(range(low,high+1))
            for a in ranges[0]:
                for b in ranges[1]:
                    if f == g and (a,b) == (0,0):
                        continue
                    shifted = [z+a*u+b*v for z in motif[g]]
                    assert separated(motif[f], shifted) or separated(shifted, motif[f]), (f,g,a,b)
                    comparisons += 1
    # Diagnostic only: a three-copy local beta-star can use partial p/q
    # contacts.  This is not a monohedral plane-tiling certificate.
    a = verts["A"]
    patch = [a, [-z+vector(K,[-r/2,w*r/2]) for z in a],
             [rot90*z+vector(K,[p,-q]) for z in a]]
    rays = [vector(K,[1,0]), vector(K,[-K(1)/2,w/2]),
            vector(K,[-K(1)/2,-w/2])]
    for k, poly in enumerate(patch):
        left, right = rays[k], rays[(k+1) % 3]
        assert all(det(left,z) >= 0 and det(z,right) >= 0 for z in poly)
    assert patch[0][0] == patch[1][4] == patch[2][2] == zero
    assert patch[0][1] == vector(K,[q,0]) and patch[2][1] == vector(K,[p,0])
    assert q > p
    assert patch[1][3] == vector(K,[-q/2,-w*q/2])
    assert patch[2][3] == vector(K,[-p/2,-w*p/2])
    print("PASS independent Cairo audit: exact positive-root closure; all supporting halfplanes; "
          "six circular angle-flat links; connected orientable chi=0; "
          "all seam holonomies translations with rank-two span.")
    print("nonzero seam periods:", sorted({tuple(t) for t in periods}))
    print("exact lattice area:", lattice.det(), "; bounded-domain overlap comparisons:", comparisons)
    print("certificate SHA-256:", hashlib.sha256(CERT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
