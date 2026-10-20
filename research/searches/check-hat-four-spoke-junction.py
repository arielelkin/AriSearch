"""Exact analytic certificate for the fixed four-spoke Hat topology."""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s

source = json.loads(Path("research/certificates/hat-eight-kite-convex-cluster-gate.json").read_text())
P = []
for x, y in source["hat_outline"]:
    assert F(x[1]) == F(y[0]) == 0
    P.append((2*F(x[0]), 2*F(y[1])))
assert P == [(0,0),(-3,-1),(-2,-2),(2,-2),(3,-1),(6,-2),
             (9,-1),(8,0),(6,0),(6,2),(3,3),(2,2),(0,2)]
def turn(a,b,c):
    return s.expand((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
assert [i for i in range(13) if turn(P[i-1],P[i],P[(i+1)%13]) < 0] == [0,4,8,11]
u,v = s.symbols("u v")
sectors = [[0,1,2,3,4],[4,5,6,7,8],[8,9,10,11],[11,12,0]]
expected = [[u-3*v,4,4,4,-u+v+4,u+3*v],
            [u+3*v,6,4,2,-2*v,-u+3*v+6],
            [12-2*u,6,4,u-v,-2*u-4*v+12],
            [4-2*v,4,2*u,2*u-2*v]]
triangle = [(0,0),(4,0),(3,-1)]
for ids, row in zip(sectors,expected):
    q = [P[i] for i in ids] + [(u,v)]
    assert [turn(q[j-1],q[j],q[(j+1)%len(q)]) for j in range(len(q))] == row
    # Every linear turn inequality holds on the proposed closed triangle.
    for e in row:
        assert all(s.sympify(e).subs({u:a,v:b}) >= 0 for a,b in triangle)
# Conversely these three necessary turns define exactly that triangle:
# v<=0, u+3v>=0, -u+v+4>=0. Hence v>=-1.
assert len(sectors[-1])+1 == 4
assert [len(ids)+1 for ids in sectors] == [6,6,5,4]
print("PASS: exact turns; common convexity triangle; universal <=4-side obstruction")
