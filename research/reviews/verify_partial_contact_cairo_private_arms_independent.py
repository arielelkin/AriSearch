"""Independent exact finite checks for the private-arm Cairo contact lemma.
Domain: two fixtures, five side vectors/corners/supports apiece, all native
stars with up to four corners and two straight sectors, all doubled e/arm
comparisons. No global tiling or shape-forcing proof is automated here.
"""
from itertools import product
from sage.all import AA, QuadraticField, vector

F = QuadraticField(3, 's', embedding=AA(3).sqrt())
s = F.gen()
dirs = tuple(vector(F, v) for v in ((1, 0), (0, 1),
                                      (-s/2, F(1)/2),
                                      (-F(1)/2, -s/2),
                                      (F(1)/2, -s/2)))

def det(u, v):
    return u[0]*v[1]-u[1]*v[0]

def build(c, d, e):
    # Solve the two closure equations directly for the first two sides,
    # using the other three already assigned vector lengths.
    v = -(F(c)*dirs[2] + F(d)*dirs[3] + F(e)*dirs[4])
    lens = (v[0], v[1], F(c), F(d), F(e))
    assert all(t > 0 for t in lens)
    sides = tuple(t*u for t, u in zip(lens, dirs))
    points = [vector(F, (0, 0))]
    for edge in sides:
        points.append(points[-1]+edge)
    assert points[-1] == points[0]
    points.pop()
    for i in range(5):
        assert sides[i].dot_product(sides[i]) == lens[i]**2
        for j in range(5):
            if j not in (i, (i+1)%5):
                assert det(sides[i], points[j]-points[i]) > 0
        # Cosine of the interior angle AFTER side i: 0 at the two right
        # corners, and -1/2 at the three 120 degree corners.
        cosine = F(0) if i in (0,2) else -F(1)/2
        assert (-sides[i]).dot_product(sides[(i+1)%5]) == cosine*lens[i]*lens[(i+1)%5]
    assert len(set(lens)) == 5
    return lens

P = build(1, 2, 3)
Q = build(4, 5, 6)
assert len(set(P[:4]+Q[:4])) == 8
for e, arm in product((P[4], Q[4]), P[:4]+Q[:4]):
    assert e != 2*arm
stars = {(u,v,w) for u in range(5) for v in range(4) for w in range(3)
         if 90*u+120*v+180*w == 360 and u+v>0}
assert stars == {(4,0,0), (0,3,0), (2,0,1)}
assert set(P) != set(Q)
print('PASS independent Cairo private-arm audit: two exact convex closed fixtures; all native stars; eight unique arms; sixteen doubled-length exclusions.')
