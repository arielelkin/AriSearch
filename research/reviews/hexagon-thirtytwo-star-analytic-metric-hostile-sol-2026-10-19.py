#!/usr/bin/env python3
"""Independent exact review: confirms scalar IFT data and exposes native index mismatch."""
import json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
c=json.loads((root/'research/certificates/hexagon-thirtytwo-star-analytic-metric-sol-2026-10-19.json').read_text())
N=s.Matrix(c['nullspace']).applyfunc(s.sympify)
D=s.Matrix(c['solved_minor']).applyfunc(s.sympify)
x=s.symbols('x:7'); t=s.symbols('t',real=True)
a=s.ones(12,1)*2*s.pi/3+N*s.Matrix(x)
words=((0,1,2,0,3,4),(0,1,2,0,3,1)); lengths=[2,1+t,1+2*t,1+3*t,1+4*t]
F=[]
for f,w in enumerate(words):
    phi=0; real=0; imag=0
    for j,col in enumerate(w):
        if j: phi += s.pi-a[6*f+j]
        real += lengths[col]*s.cos(phi); imag += lengths[col]*s.sin(phi)
    F.extend([real,imag])
F=s.Matrix(F); zero={**dict.fromkeys(x,0),t:0}
assert F.subs(zero)==s.zeros(4,1)
Jac=F.jacobian(x).subs(zero).applyfunc(s.simplify)
assert Jac==s.Matrix(c['closure_angle_jacobian']).applyfunc(s.sympify)
assert Jac[:,:4]==D and s.simplify(D.det())==-3
v=-D.inv()*(F.diff(t).subs(zero)+Jac[:,4])
ad=(N*s.Matrix(list(v)+[1,0,0])).applyfunc(s.simplify)
assert ad==s.Matrix(c['angle_derivatives']).applyfunc(s.sympify)
rows=((0,1,8),(2,7,11),(3,6,10),(4,5,9))
C=s.Matrix([[int(j//6==f) for j in range(12)] for f in range(2)]+[[int(j in row) for j in range(12)] for row in rows])
assert C.rank()==5 and N.rank()==7 and C*N==s.zeros(6,7)
assert C*ad==s.zeros(6,1)
counts={}
for f,w in enumerate(words):
    counts[f]={'H1':0,'H2':0,'H3':0}
    for k in range(6):
        for direction in (1,-1):
            sides=[(k+direction*i)%6 for i in range(6)]
            corners=[j if direction==1 else (j+1)%6 for j in sides]
            ell=[w[j] for j in sides]
            for name,match,indices in [('H1',ell[2]==ell[5],(0,1,2)),('H2',ell[1]==ell[3] and ell[2]==ell[5],(0,1,3))]:
                if match:
                    counts[f][name]+=1
                    assert s.simplify(sum(ad[6*f+corners[i]] for i in indices))!=0
            if ell[0]==ell[1] and ell[2]==ell[3] and ell[4]==ell[5]:counts[f]['H3']+=1
assert counts=={0:{'H1':4,'H2':0,'H3':0},1:{'H1':4,'H2':2,'H3':0}}
# Builder native corner c is the END of side c, hence physical angle a[c+1].
wrong=[]
for row in rows:
    shifted=[6*(j//6)+(j+1)%6 for j in row]
    derivative=s.simplify(sum(ad[j] for j in shifted))
    assert derivative!=0
    wrong.append({'native_star':row,'physical_start_angles':shifted,'derivative':str(derivative)})
print(json.dumps({'scalar_IFT':'PASS','dihedral_matches':counts,'retained_native_support':'FAIL','native_star_residual_derivatives':wrong},indent=2))
