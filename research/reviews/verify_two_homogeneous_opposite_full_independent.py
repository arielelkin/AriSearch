"""Fresh no-author-import audit of the full exceptional-curve elimination.
Exact finite domain: 24 oriented native corner states cubed, all 12 H/L
magnitude equations, six native indexings and five incidence equations.
The global concavity, compactness and boundary arguments are audited in the
associated whole-proof review; finite replay alone does not prove them.
"""
from collections import Counter
from itertools import product
from sage.all import QQ, PolynomialRing, SR, atan, sin, cos, diff, matrix, vector

# Native angle and ray data reconstructed independently by occurrence index.
words = ("pqpqpq", "pppqqq")
slots = (("H", "L") * 3, ("u", "a", "b", "v", "c", "e"))
slopes = ((2, -2) * 3, (-1, -1, 2, 3, -6, 3))
states = []
for shape in range(2):
    for j in range(6):
        rays = (words[shape][j - 1], words[shape][j])
        for mirror in range(2):
            states.append((shape, j, rays if not mirror else rays[::-1]))
all_binary = 0
candidate = Counter()
for triple in product(states, repeat=3):
    if any(triple[j][2][1] != triple[(j + 1) % 3][2][0] for j in range(3)):
        continue
    all_binary += 1
    assert sum(c[2][0] != c[2][1] for c in triple) in (0, 2)
    if sum(slopes[s][j] for s, j, rays in triple) != 0:
        continue
    assert sum(s == 0 for s, j, rays in triple) <= 1
    candidate[tuple(sorted(slots[s][j] for s, j, rays in triple))] += 1
expected = {tuple(sorted(t)) for t in
            (("a", "a", "b"), ("c", "e", "e"),
             ("u", "u", "b"), ("v", "v", "c"),
             ("H", "u", "a"), ("L", "v", "a"), ("L", "u", "e"))}
assert set(candidate) == expected
assert all_binary == 1664

# Exhaustively test positive/negative magnitude equalities on both curve signs.
R = PolynomialRing(QQ, ["x", "y"])
x, y = R.gens()
for sign in (1, -1):
    a, e = 120 - sign * x, 120 + sign * y
    covers = [360 - m - g - 120 for g in (a, 360 - 2*a, 360 - 2*e, e)
              for m in (a, e)]
    pos = {sign * k for k in covers if (sign * k)(x=1, y=2) > 0}
    neg = {-sign * k for k in covers if (sign * k)(x=1, y=2) < 0}
    assert pos == {2*x, x+2*y, y}
    assert neg == {y-x, x, 2*x+y, 2*y}
    matches = []
    for p, n in product(pos, neg):
        equation = p - n
        cx, cy = equation.monomial_coefficient(x), equation.monomial_coefficient(y)
        if cy:
            ratio = -cx/cy
            if ratio > 1:
                matches.append((ratio, p(x=1, y=ratio)))
        else:
            assert cx != 0
    assert matches == [(QQ(3), QQ(2))]

# Native B reflection and length-name swap preserves the opposite ordering;
# A reflection keeps its H-even display and alternating word after swapping.
old_b = ("u", "a", "b", "v", "c", "e")
assert tuple(old_b[j] for j in (0,5,4,3,2,1)) == ("u","e","c","v","b","a")
assert ''.join(words[1][j] for j in (5,4,3,2,1,0)) == 'qqqppp'
assert ''.join(words[0][j] for j in (1,0,5,4,3,2)) == 'qpqpqp'
assert tuple(slots[0][j] for j in (2,1,0,5,4,3)) == slots[0]

# Correct phase differentiation and high-alpha branch tangent at x=0.
z = SR.var('z')
rho = atan(2*sin(z))
d = 1+4*sin(z)**2
assert (diff(rho,z)-2*cos(z)/d).simplify_trig() == 0
assert (diff(rho,z,2)+2*sin(z)*(5+4*cos(z)**2)/d**2).simplify_trig() == 0
assert QQ(-1)/4 - 3*QQ(-1)/4 - 1 == -QQ(1)/2

# Exact dual incidence identity; columns NA,NB,h,t,l,Yp,Zbeta.
M = matrix(QQ, [[-3,0,1,0,0,0,0], [-3,0,0,1,1,0,0],
                [0,-1,1,1,0,2,0], [0,-1,0,0,0,1,1],
                [0,-1,1,0,1,0,2]])
weights = vector(QQ, [-2,-1,1,-2,1])
assert weights*M == vector(QQ, [9,0,0,0,0,0,0])
print('PASS: 1664 oriented binary stars; complete seven-type exceptional inventory; '
      'both signs of 12 H/L equations; genuine native reflection/length swap; '
      'exact phase derivatives/tangent; explicit 9 NA incidence dual.')
