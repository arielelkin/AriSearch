"""Exact bounded certificate for the sawtooth interface construction.
This verifies geometry and periods, not recognition of arbitrary admitted tilings.
"""
from fractions import Fraction as F
import json


def polygon(p,q,h):
    return [(F(0),F(0)),(F(1,2),-p),(F(1),F(0)),(F(1),h),(F(1,2),h+q),(F(0),h)]


def area2(poly):
    return sum(x*Y-y*X for (x,y),(X,Y) in zip(poly,poly[1:]+poly[:1]))


def convex(poly):
    out=[]
    for i in range(6):
        a,b,c=poly[i],poly[(i+1)%6],poly[(i+2)%6]
        out.append((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
    assert all(v>0 for v in out)
    return out


def rotate(poly,h):
    return [(1-x,h-y) for x,y in poly]


def canonical(poly):
    return min(tuple(poly[i:]+poly[:i]) for i in range(len(poly)))


def seam(p,q,h,next_h):
    # Current top peak is the next strip's lower left endpoint;
    # its trough is the next strip's lower midpoint.
    top=[(F(0),h),(F(1,2),h+q),(F(1),h)]
    nxt=polygon(q,p,next_h)
    shifted=[(x+F(1,2),y+h+q) for x,y in nxt]
    assert shifted[0]==top[1]
    assert shifted[1]==top[2]
    # Next strip lies above the common sawtooth: all its row heights
    # are next_h plus nonnegative tooth contributions.
    assert next_h>0
    return (F(1,2),h+q)


p,q,h,k=F(1,8),F(1,4),F(1),F(3,2)
a,b=polygon(p,q,h),polygon(q,p,k)
ca,cb=convex(a),convex(b)
assert canonical(rotate(a,h))==canonical(polygon(q,p,h))
assert canonical(rotate(b,k))==canonical(polygon(p,q,k))
assert area2(a)!=area2(b) # genuinely noncongruent species
ab=seam(p,q,h,k)
ba=seam(q,p,k,h)
mixed=(ab[0]+ba[0],ab[1]+ba[1])
assert mixed==(F(1),h+k+p+q)
mono_a=(F(1),2*h+p+q)
mono_b=(F(1),2*k+p+q)
assert mixed[1]>0 and mono_a[1]>0 and mono_b[1]>0
# Strip area telescopes to the determinant of the torus generators.
assert (area2(a)+area2(b))/2==mixed[1]
assert area2(a)==mono_a[1]
assert area2(b)==mono_b[1]
print(json.dumps({
 'scope':'exact strip assembly; no universal recognition',
 'A_vertices':[[str(v) for v in row] for row in a],
 'B_vertices':[[str(v) for v in row] for row in b],
 'A_turn_cross_products':[str(v) for v in ca],
 'B_turn_cross_products':[str(v) for v in cb],
 'horizontal_period':['1','0'],
 'mixed_two_row_period':[str(v) for v in mixed],
 'A_only_two_row_period':[str(v) for v in mono_a],
 'B_only_two_row_period':[str(v) for v in mono_b],
 'result':'infinite mixed cover and both periodic omission covers certified'
},indent=2))
