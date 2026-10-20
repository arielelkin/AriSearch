"""Exact polynomial checks only; the analytic proof is in the lemma artifact."""
import json
from pathlib import Path
import sympy as s
ux,uy,vx,vy,wx,wy=s.symbols('ux uy vx vy wx wy', real=True)
u=s.Matrix([ux,uy]); v=s.Matrix([vx,vy]); w=s.Matrix([wx,wy])
zero=s.zeros(2,1)
p=[zero,u,u+v,u+v+w,v+w,w]
det=lambda x,y:s.det(s.Matrix.hstack(x,y))
area=s.expand(sum(det(p[i],p[(i+1)%6]) for i in range(6))/2)
a=u+v; b=v+w
assert s.expand(det(a,b)-area)==0
for i,t in enumerate([b,b-a,-a]):
    assert p[i]+t==p[(i+4)%6]
    assert p[i+1]+t==p[i+3]
F,Vb,VT,Vf,X,pn=s.symbols('F Vb VT Vf X pn')
N=pn+2*Vb+2*VT+3*Vf+X
E=(N+pn+Vb+VT)/2
F_expr=s.expand(1-(pn+Vb+VT+Vf)+E)
assert s.expand(6*F_expr-N-(6-pn+Vb+VT+2*X))==0
out={'status':'exact symbolic identities passed','domain':'all real u,v,w; geometry requires strict convexity','hexagon_area':str(area),'periods':['u+v','v+w'],'side_pair_translations':['v+w','w-u','-u-v'],'dissection_identity':'sum(6-n)=6-p+V_b+V_T+2X','scope':'identity certificate only; no source tiling enumeration or aperiodicity claim'}
path=Path('research/certificates/convex-parallelogram-fusion-2026-10-19.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
