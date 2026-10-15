"""Exact symbolic verification for the entire rational Y-pentagon family.

No numerical sampling proves a sign or angle equality. No solver or geometric
patch enumeration is involved. All six-kind angle multisets of size <=5
and all complements of size <=2 are enumerated without symmetry assumptions.
"""
from itertools import combinations_with_replacement
import sympy as sp

T = sp.Symbol("t", real=True)
R = (4*T-2)/3
K = (T+1)/3
S2 = 2*K*K
L2 = 1+T*T
P = ((0,0),(R,0),(R+1,T),(T,R+1),(0,R))
Q = ((T,1),(T-K,1+K),(-T+K,1+K),(-T,1),(0,0))

def sub(a,b):
    return tuple(sp.expand(x-y) for x,y in zip(a,b))
def dot(a,b):
    return sp.expand(sum(x*y for x,y in zip(a,b)))
def cross(a,b):
    return sp.factor(a[0]*b[1]-a[1]*b[0])
def edges(poly):
    return [sub(poly[(i+1)%5],poly[i]) for i in range(5)]

ep,eq=edges(P),edges(Q)
assert all(sp.expand(dot(e,e)-z)==0 for e,z in zip(ep,(R*R,L2,S2,L2,R*R)))
assert all(sp.expand(dot(e,e)-z)==0 for e,z in zip(eq,(S2,R*R,S2,L2,L2)))
# Turn dot/cross pairs determine actual native angles, with positive cross.
# Every recorded identity is polynomial, preserving an exact positive scale.
def turn_table(es):
    return [(sp.factor(dot(es[i-1],es[i])),cross(es[i-1],es[i])) for i in range(5)]
pt=turn_table(ep); qt=turn_table(eq)
expected_p = [(0,(4*T-2)**2/9), (2*(2*T-1)/3, 2*T*(2*T-1)/3),
              ((T-1)*(T+1)/3, (T+1)**2/3),
              ((T-1)*(T+1)/3, (T+1)**2/3),
              (2*(2*T-1)/3, 2*T*(2*T-1)/3)]
expected_q = [(-(T-1)*(T+1)/3, (T+1)**2/3),
              (2*(T+1)*(2*T-1)/9,2*(T+1)*(2*T-1)/9),
              (2*(T+1)*(2*T-1)/9,2*(T+1)*(2*T-1)/9),
              (-(T-1)*(T+1)/3, (T+1)**2/3),
              (T**2-1,2*T)]
for actual, expected in ((pt,expected_p),(qt,expected_q)):
    assert all(sp.expand(a-b)==0 for row, target in zip(actual,expected) for a,b in zip(row,target))
# Every nonincident vertex lies strictly left of each oriented native edge.
# After t=x+1 every coefficient is nonnegative and the constant is positive;
# this proves all 30 strict support inequalities for every t>1.
X = sp.Symbol("x", positive=True)
for poly in (P,Q):
    for i,a in enumerate(poly):
        edge=sub(poly[(i+1)%5],a)
        for j,v in enumerate(poly):
            if j in (i,(i+1)%5):
                continue
            support=cross(edge,sub(v,a))
            shifted=sp.Poly(sp.expand(support.subs(T,X+1)),X)
            assert all(c>=0 for c in shifted.all_coeffs())
            assert shifted.eval(0)>0
# Interior-angle cotangents = negative turn cotangent. In order:
# P r,a,b,b,a; Q c,g,g,c,d. For theta=atan(t),
# cot(a)=-1/t, cot(b)=(1-t)/(1+t), cot(c)=(t-1)/(t+1),
# cot(g)=-1, cot(d)=(1-t^2)/(2t).
# The P b turn dot must be (t^2-1)/3, while Q c turn dot has opposite sign.
ANGLES={"r":(2,0),"a":(4,-1),"b":(1,1),"c":(3,-1),"g":(3,0),"d":(0,2)}
full=[]; flat=[]
for n in range(1,6):
    for word in combinations_with_replacement(ANGLES,n):
        total=tuple(sum(ANGLES[x][i] for x in word) for i in (0,1))
        if total==(8,0): full.append("".join(sorted(word)))
        if n<=2 and total==(4,0): flat.append("".join(sorted(word)))
assert sorted(full)==sorted(["ggr","aad","abg","rrrr","bcrr","ccdr","bbcc"])
assert sorted(flat)==["bc","rr"]
lo=(5+3*sp.sqrt(2))/7
hi=1+sp.sqrt(2)
assert sp.simplify(14*lo**2-20*lo+2)==0
assert lo>1 and hi>lo
polys=[-7*T*T+16*T+5,-T*T+16*T-1]
for p in polys:
    assert sp.diff(p,T,2)<0
    for end in (lo,hi):
        assert sp.simplify(p.subs(T,end))>0
assert sp.expand(9*(R*R-S2))==14*T*T-20*T+2
assert sp.expand(9*(L2-R*R))==polys[0]
assert sp.expand(9*(4*S2-L2))==polys[1]
assert sp.expand(4*L2-9*S2-2*(T-1)**2)==0
print("PASS: exact symbolic coordinates, complete angle stars, entire parameter interval")
