"""Independent exact four-turn algebra check; source incidence is audited separately."""
import json
from pathlib import Path
import sympy as S
p,q=S.symbols('p q')
path=Path(__file__).with_name('pinwheel-barycentric-center-family-2026-10-19.json')
d=json.loads(path.read_text());wanted=[(['1/25','2/25'],0),(['1/25','2/25'],2),(['1/25','22/25'],6),(['1/5','1/5'],4)]
turns=[]
for vertex,index in wanted:
 r=next(r for r in d['unsat_core'] if r['vertex']==vertex and r['turn_index']==index)
 a,b,c=[S.Matrix([S.sympify(x,locals={'p':p,'q':q}) for x in point]) for point in r['triple']]
 turns.append(S.expand(S.det(S.Matrix.hstack(b-a,c-b))))
f=-4*p*p+3*p-q*q+q/2;g=-4*p*p+p-q*q+q/2
assert all(S.expand(t-e/125)==0 for t,e in zip(turns,[f,g,-g,-f]))
assert S.expand(f-g)==2*p
# All four turns >=0 forces f=g=0 and therefore p=0, contradicting p>0.
print('PASS: four exact determinant identities force p=0 under convexity, excluding every interior center')
