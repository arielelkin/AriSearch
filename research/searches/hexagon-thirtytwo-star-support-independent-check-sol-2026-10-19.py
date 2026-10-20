#!/usr/bin/env python3
"""Independent upper atlas, BOTH endpoint mate sets, and exact tangent audit."""
import itertools,json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[1]
D=json.loads((root/'certificates/hexagon-thirtytwo-star-candidate-gate-sol-2026-10-19.json').read_text())
C=json.loads((root/'certificates/hexagon-thirtytwo-star-support-determinism-sol-2026-10-19.json').read_text())
words=((0,1,2,0,3,4),(0,1,2,0,3,1))
ports=list(itertools.product(range(12),(-1,1)))
def before(p):
 c,h=p;return c if h==1 else c//6*6+(c%6+1)%6
def after(p):
 c,h=p;return c//6*6+(c%6+1)%6 if h==1 else c
def color(j):return words[j//6][j%6]
def other(p,j):return (j//6*6+(j%6-1)%6 if p[0]==j else j,p[1])
def canon(t):return min(t,t[1:]+t[:1],t[2:]+t[:2])
atlas={canon(t) for t in itertools.product(ports,repeat=3) if all(color(after(t[k]))==color(before(t[(k+1)%3])) for k in range(3))}
while True:
 pairs={(t[k],t[(k+1)%3]) for t in atlas for k in range(3)}
 new={t for t in atlas if all((other(t[(k+1)%3],before(t[(k+1)%3])),other(t[k],after(t[k]))) in pairs for k in range(3))}
 if new==atlas:break
 atlas=new
assert sorted(atlas)==[tuple(map(tuple,t)) for t in D['stars']]
S={2,5,13,15,17,20,22,23}
opts={(i,h):set() for i in range(12) for h in (-1,1)}
for k in S:
 t=sorted(atlas)[k]
 for j,p in enumerate(t):
  q=t[(j+1)%3]
  u=(after(p),p[1]);v=(before(q),q[1])
  opts[u].add(v);opts[v].add(u)
assert all(len(v)==1 for v in opts.values())
m={k:next(iter(v)) for k,v in opts.items()}
assert all(m[m[k]]==k for k in m)
assert m=={tuple(r['source']):tuple(r['neighbor']) for r in C['neighbor_map']}
z=s.sqrt(3)
a=[-2*z-1,4+3*z,-4-z,2,-z,-1+z,-2,4+z,-3-z,1,0,0]
res=[s.expand(sum(a[c] for c,h in t)) for t in sorted(atlas)]
assert {i for i,r in enumerate(res) if r==0}==S
assert res==list(map(s.sympify,C['residual_derivatives']))
# Differentiate closure directly in native end-corner convention.
for f,w in enumerate(words):
 dx=dy=0
 for j,col in enumerate(w):
  phi=s.pi*j/3;turn=-sum(a[f*6:f*6+j]);length=2 if col==0 else 1
  dx+=col*s.cos(phi)-length*s.sin(phi)*turn
  dy+=col*s.sin(phi)+length*s.cos(phi)*turn
 assert s.simplify(dx)==s.simplify(dy)==0
assert all(sum(a[c] for c in inds)==0 for inds in ((0,1,8),(2,7,11),(3,6,10),(4,5,9)))
print('PASS: independent 32-star upper atlas; both-endpoint 24-state mate map; all 32 residual derivatives; direct differentiated closure')
