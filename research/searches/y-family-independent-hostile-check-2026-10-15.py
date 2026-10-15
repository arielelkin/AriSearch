"""Independent exact audit: no imports from producer scripts.
Finite domain: six angle kinds, multisets of sizes 1..5 (full) and 1..2
(flat); rational-function native geometry; polynomial roots on one exact
algebraic interval. This checks finite inputs to the written geometric
proof, not the infinite tiling theorem by computation.
Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/y-family-independent-hostile-check-2026-10-15.py
"""
from itertools import combinations_with_replacement
from sage.all import QQ, AA, PolynomialRing

K = PolynomialRing(QQ, 't')
t = K.gen()
F = K.fraction_field()
lo = (5 + 3*AA(2).sqrt())/7
hi = 1 + AA(2).sqrt()
assert 1 < lo < 2 < hi
angles = {'r': (2,0), 'a': (4,-1), 'b': (1,1),
          'c': (3,-1), 'g': (3,0), 'd': (0,2)}

def census(target, maximum):
    found = set()
    for n in range(1, maximum+1):
        for word in combinations_with_replacement(sorted(angles), n):
            v = tuple(sum(angles[x][j] for x in word) for j in (0,1))
            if v == target:
                found.add(''.join(word))
    return found

assert census((8,0),5) == {'ggr','aad','abg','rrrr','bcrr','ccdr','bbcc'}
assert census((4,0),2) == {'rr','bc'}

R = (4*t-2)/3
k = (t+1)/3
S2 = 2*k*k
L2 = 1+t*t
P = [(0,0),(R,0),(R+1,t),(t,R+1),(0,R)]
Q = [(t,1),(t-k,1+k),(-t+k,1+k),(-t,1),(0,0)]
P = [tuple(F(v) for v in point) for point in P]
Q = [tuple(F(v) for v in point) for point in Q]
cots = {'r':0, 'a':-1/t, 'b':(1-t)/(1+t),
        'c':(t-1)/(t+1), 'g':-1, 'd':(1-t*t)/(2*t)}

def positive_open(expr):
    expr = F(expr)
    for poly in (expr.numerator(),expr.denominator()):
        assert not any(lo < root < hi for root,_ in poly.roots(AA))
    assert expr(AA(2)) > 0

def geometry(points, labels, lengths2):
    edges = [tuple(points[(i+1)%5][j]-points[i][j] for j in (0,1)) for i in range(5)]
    for i in range(5):
        incoming, outgoing = edges[(i-1)%5], edges[i]
        cross = incoming[0]*outgoing[1]-incoming[1]*outgoing[0]
        dot = sum(incoming[j]*outgoing[j] for j in (0,1))
        positive_open(cross)
        assert -dot/cross == F(cots[labels[i]])
        assert sum(v*v for v in outgoing) == F(lengths2[i])
    # All directed supporting lines place the other vertices on the left:
    # this verifies genuine global convexity, rather than local turns alone.
    for i,e in enumerate(edges):
        for j,p in enumerate(points):
            if j not in (i,(i+1)%5):
                v = tuple(p[z]-points[i][z] for z in (0,1))
                positive_open(e[0]*v[1]-e[1]*v[0])

geometry(P, 'rabba', [R*R,L2,S2,L2,R*R])
geometry(Q, 'cggcd', [S2,R*R,S2,L2,L2])
assert 9*(R*R-S2) == 14*t*t-20*t+2
assert 9*(L2-R*R) == -7*t*t+16*t+5
assert 9*(4*S2-L2) == -t*t+16*t-1
assert 4*L2-9*S2 == 2*(t-1)**2
for expr in [R, k, R*R-S2, L2-R*R,4*S2-L2,4*L2-9*S2]:
    positive_open(expr)
# 2R != 3S follows for rational t since R and k are positive rational,
# while S=k sqrt(2). Both transition exceptions are directly false at t=2.
assert (4*R*R-9*S2)(2) != 0
assert (4*L2-9*S2)(2) != 0
# Rational-tangent roots-of-unity candidates reconstructed algebraically.
for u in [-2,-1,0,1,2]:
    roots = (2*(1-t*t)-u*(1+t*t)).roots(QQ)
    assert all(not (lo < root < hi) for root,_ in roots)
print('PASS: independent stars, native convex geometry, all interval identities/signs, and rational-angle exclusions')
