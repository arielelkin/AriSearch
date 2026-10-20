#!/usr/bin/env python3
"""Independent equiangular matrix derivation and retained support checks.
Does not certify enumeration completeness or nonlinear UNSAT."""
import json
from pathlib import Path
import sympy as S
root=Path(__file__).resolve().parents[2]
c=json.loads((root/'research/certificates/hexagon-five-four-metric-gate-2026-10-19.json').read_text())
rows=[]
for word in (c['A'],c['B']):
 rows.append([S.simplify(sum(2*S.cos(S.pi*j/3) for j,k in enumerate(word) if k==a)) for a in range(5)])
 rows.append([S.simplify(sum(2*S.sin(S.pi*j/3)/S.sqrt(3) for j,k in enumerate(word) if k==a)) for a in range(5)])
assert rows==c['equiangular_matrix']
M=S.Matrix(rows);assert M.rank()==3
for v in c['equiangular_kernel']:assert M*S.Matrix(v)==S.zeros(4,1)
assert S.Matrix.hstack(*map(S.Matrix,c['equiangular_kernel'])).rank()==2
assert c['domain_subsets']==2**22
assert all(not(a!=b and a&b==a) for a in c['minimal_supports'] for b in c['minimal_supports'])
assert len(c['metric_results'])<=len(c['minimal_supports'])
if c['status']=='blocked':assert c['metric_results'][-1]['result']=='unknown'
print('PASS independently derived equiangular closure matrix and kernel; certificate status internally consistent. Support completeness and metric solver not independently certified.')
