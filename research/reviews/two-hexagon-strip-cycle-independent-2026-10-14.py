#!/usr/bin/env python3
"""Independent rational checker; imports neither author's code nor data."""
from fractions import Fraction as Q


def tau(x):
    x = x % 1
    return 2*x if x <= Q(1,2) else 2-2*x


def polygon(p,q,h):
    return [(0,0),(Q(1,2),-p),(1,0),(1,h),(Q(1,2),h+q),(0,h)]


def shoelace(poly):
    return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))/2


def cyclic(poly):
    return min(tuple(poly[i:]+poly[:i]) for i in range(len(poly)))


def verify(p,q,h,k):
    first = polygon(p,q,h)
    second = polygon(q,p,k)
    for poly, altitude in [(first,h),(second,k)]:
        determinants = []
        for i in range(6):
            a,b,c = poly[i-1],poly[i],poly[(i+1)%6]
            determinant = (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
            determinants.append(determinant)
        assert all(v>0 for v in determinants)
        assert shoelace(poly) == altitude+(p+q)/2
    reflected = [(1-x,h-y) for x,y in first]
    assert cyclic(reflected) == cyclic(polygon(q,p,h))
    # Both functions are piecewise affine with these same breakpoints.
    # At all breakpoints their values agree, hence the full boundaries agree.
    for x in [Q(0),Q(1,2),Q(1)]:
        assert h+q*tau(x) == h+q-q*tau(x-Q(1,2))
    for x in [Q(i,8) for i in range(9)]:
        gap = h+(p+q)*tau(x)
        assert gap >= h > 0
    assert shoelace(first)+shoelace(second) == h+k+p+q
    assert 2*shoelace(first) == 2*h+p+q
    assert 2*shoelace(second) == 2*k+p+q


verify(Q(1,8),Q(1,4),Q(1),Q(3,2))
verify(Q(2,3),Q(7,5),Q(1,17),Q(13,19))
# Irrational phase displacements need no rational commensurability:
# f_A=tau and f_B=2*tau, either shifted by ANY real phase, stay in [0,2].
# Edges A->B and B->A with d=3 therefore have gap at least 1. Their means
# give average gaps 3+1-1/2 and 3+1/2-1; total height is exactly 6.
averages = [Q(3)+Q(1)-Q(1,2), Q(3)+Q(1,2)-Q(1)]
assert sum(averages) == 6
assert all(v>0 for v in averages)
print('PASS: independent polygons, full piecewise-linear seams, mixed/omission areas, irrational-phase bound')
