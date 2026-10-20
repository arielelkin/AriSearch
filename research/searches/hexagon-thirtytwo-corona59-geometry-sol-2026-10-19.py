#!/usr/bin/env python3
"""Exact first-order development of two corona59 exterior neighbors."""
import sympy as s,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
alpha=list(map(s.sympify,json.loads((root/'research/certificates/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.json').read_text())['angle_derivatives']))
def clean(z):return s.simplify(s.expand_complex(z))
def add(a,b):return tuple(clean(x+y) for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return clean(a[0]*b[0]),clean(a[0]*b[1]+a[1]*b[0])
def div(a,b):return clean(a[0]/b[0]),clean((a[1]*b[0]-a[0]*b[1])/b[0]**2)
def conj(a):return tuple(s.conjugate(x) for x in a)
def cross(a,b):return tuple(clean(s.im(z)) for z in mul(conj(a),b))
VV=[]
for f,w in enumerate(((0,1,2,0,3,4),(0,1,2,0,3,1))):
 vs=[(s.Integer(0),s.Integer(0))]
 for j,c in enumerate(w):
  z=clean(s.exp(s.I*j*s.pi/3));ld=0 if c==0 else c;length=2 if c==0 else 1
  ed=(length*z,clean(z*(ld-s.I*length*sum(alpha[6*f:6*f+j]))))
  vs.append(add(vs[-1],ed))
 assert vs[-1]==(0,0)
 VV.append(vs[:6])
V=VV[0];Q=[sub(V[5],z) for z in V]
def neighbor(f,ss,j):
 # Both neighbors are positively oriented and attach to side j of Q.
 v=VV[f];a,b=Q[j],Q[(j+1)%6]
 rr=div(sub(a,b),sub(v[(ss+1)%6],v[ss]));tt=sub(b,mul(rr,v[ss]))
 return [add(mul(rr,z),tt) for z in v]
U=neighbor(0,1,1);W=neighbor(1,2,2)
mid=mul(add(U[0],U[1]),(s.Rational(1,2),0))
vals=[cross(sub(W[(k+1)%6],W[k]),sub(mid,W[k])) for k in range(6)]
out=dict(schema='CORONA59_NEIGHBOR_JETS_SOL_V1',U=[[str(a),str(b)] for a,b in U],W=[[str(a),str(b)] for a,b in W],midpoint=list(map(str,mid)),signed_cross_jets=[[str(a),str(b)] for a,b in vals])
p=root/'research/certificates/hexagon-thirtytwo-corona59-geometry-sol-2026-10-19.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
