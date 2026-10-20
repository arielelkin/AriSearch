#!/usr/bin/env python3
"""Exact changed-site Penrose Voronoi gate: all intrinsic rhomb vertices."""
from pathlib import Path
import json
exec(Path('research/searches/penrose-center-voronoi-quadrilateral-2026-10-19.py').read_text().split('centers=')[0])
from scipy.spatial import Voronoi
import numpy as np
sites=sorted(set(v for _,poly in rh for v in poly),key=lambda z:tuple(z.vector()))
edges=Counter(frozenset((v[j],v[(j+1)%4])) for _,v in rh for j in range(4))
boundary=[tuple(e) for e,k in edges.items() if k==1]
def dist2(p,a,b):
    t=dot(p-a,b-a)/norm(b-a)
    if sign(t)<0: return norm(p-a)
    if sign(t-1)>0: return norm(p-b)
    return norm(p-a-t*(b-a))
xy=np.array([[complex(emb(z)).real,complex(emb(z)).imag] for z in sites])
voro=Voronoi(xy)
chosen={}
for i,c in enumerate(sites):
    if abs(complex(emb(c)))>3: continue
    reg=voro.regions[voro.point_region[i]]
    if -1 in reg: continue
    chosen.setdefault(len(reg),i)
    if len(chosen)>=3: break
assert len(chosen)>=3,chosen
witnesses=[]
h=(w-w.conjugate())/2
for expected,i in sorted(chosen.items()):
    c=sites[i]
    margin=min((dist2(c,a,b) for a,b in boundary),key=lambda x:AA(emb(x)))
    assert sign(margin-9)>0
    P=[K(-2)-2*h,K(2)-2*h,K(2)+2*h,K(-2)+2*h]
    # Only distance <=3 sites can affect the unit disk eventually verified below.
    nearby=[q for q in sites if q!=c and sign(norm(q-c)-9)<=0]
    for q in nearby:
        d=q-c; rhs=norm(d)/2; out=[]
        for a,b in zip(P,P[1:]+P[:1]):
            fa=dot(d,a)-rhs; fb=dot(d,b)-rhs
            if sign(fa)<=0: out.append(a)
            if sign(fa)*sign(fb)<0: out.append(a+(b-a)*fa/(fa-fb))
        P=[]
        for x in out:
            if not P or x!=P[-1]: P.append(x)
        if len(P)>1 and P[0]==P[-1]: P.pop()
        assert P
    while any(cross(P[k]-P[k-1],P[(k+1)%len(P)]-P[k])==0 for k in range(len(P))):
        P=[p for k,p in enumerate(P) if cross(p-P[k-1],P[(k+1)%len(P)]-p)!=0]
    assert len(P)==expected
    assert all(sign(cross(P[(k+1)%len(P)]-P[k],P[(k+2)%len(P)]-P[(k+1)%len(P)]))>0 for k in range(len(P)))
    assert all(sign(norm(v)-1)<0 for v in P)
    assert all(sign(dot(q-c,v)-norm(q-c)/2)<=0 for q in nearby for v in P)
    witnesses.append(dict(site=vec(c),sides=len(P),vertices_relative=[vec(v) for v in P],boundary_distance_squared=vec(margin),radius_squared=[vec(norm(v)) for v in P],neighbors_checked=len(nearby)))
D=dict(rule='One ordinary Voronoi site at every distinct intrinsic vertex of the unit Penrose rhomb source; weights zero.',field='CyclotomicField(10), embedded generator exp(2*pi*i/10)',source_deflations=5,source_rhombs=len(rh),sites=len(sites),witnesses=witnesses,scope='At least three incongruent strict convex cells in the retained source patch, robust to every exterior completion. No full class census or shape forcing.')
out=Path('research/searches/penrose-vertex-dual-gate-sol-2026-10-19.json')
if '--check' in __import__('sys').argv: assert json.loads(out.read_text())==D
else: out.write_text(json.dumps(D,indent=2)+'\n')
print(json.dumps(D,indent=2))
