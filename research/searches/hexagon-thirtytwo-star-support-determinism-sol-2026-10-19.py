#!/usr/bin/env python3
"""Exact finite side-neighbor and angle-residual audit; no torus enumeration."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'certificates/hexagon-thirtytwo-star-candidate-gate-sol-2026-10-19.json').read_text())
E=json.loads((R/'certificates/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.json').read_text())
S=[D['stars'][i] for i in D['star_indices']]
def sides(p):
 c,h=p; f,j=divmod(c,6)
 return (c,6*f+(j+1)%6) if h==1 else (6*f+(j+1)%6,c)
opts={}
for t in S:
 for i,p in enumerate(t):
  q=t[(i+1)%3]
  opts.setdefault((sides(p)[1],p[1]),set()).add((sides(q)[0],q[1]))
assert len(opts)==24 and all(len(v)==1 for v in opts.values())
# Both endpoints must induce the same involutive side-neighbor map.
M={k:next(iter(v)) for k,v in opts.items()}
assert all(M[M[k]]==k for k in M)
a=list(map(s.sympify,E['angle_derivatives']))
v=[s.simplify(sum(a[p[0]] for p in t)) for t in D['stars']]
assert [i for i,x in enumerate(v) if x==0]==D['star_indices']
assert all(s.simplify(sum(a[j] for j in inds))==0 for inds in ((0,1,8),(2,7,11),(3,6,10),(4,5,9)))
out=dict(schema='THIRTYTWO_STAR_SUPPORT_DETERMINISM_SOL_V1',support=D['star_indices'],neighbor_map=[dict(source=list(k),neighbor=list(M[k])) for k in sorted(M)],residual_derivatives=list(map(str,v)),zero_residual_indices=[i for i,x in enumerate(v) if x==0],domain='24 signed native sides and 32 signed atlas stars; end-corner convention',claim='Any ETE trivalent tiling restricted to this support satisfies finite intrinsic complete-placement determinism. On the corrected analytic branch, every other atlas star is excluded for all sufficiently small positive t.')
p=R/'certificates/hexagon-thirtytwo-star-support-determinism-sol-2026-10-19.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
