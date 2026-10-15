#!/usr/bin/env python3
"""Exploratory FLOAT diagnostic only; no certificate or interval theorem.
Generate input with ammann-two-class-patchdata.py 5 /tmp/astra-1100-rhombs.json.
Domain: that 430-rhomb source, radius3, five stated weight values. Boundary
margins, side counts and intersections are floating and must be replaced by
exact arithmetic before any proof use. No import from a Voronoi producer.
"""
import json
import sys
from collections import Counter
from pathlib import Path
import numpy as np

path = Path(sys.argv[1] if len(sys.argv)>1 else '/tmp/astra-1100-rhombs.json')
D = json.loads(path.read_text())
z = np.exp(1j*np.pi/5)
v = np.array([sum(a*z**i for i,a in enumerate(cs)) for cs in D['verts']])
R = D['rhombs']
c = np.array([sum(v[ids])/4 for _,ids,_ in R])
w = np.array([1 if k=='thick' else 0 for k,_,_ in R])
e = Counter(tuple(sorted((ids[i],ids[(i+1)%4])))
            for _,ids,_ in R for i in range(4))
be = [(v[a],v[b]) for (a,b),ct in e.items() if ct==1]

def distseg(p,a,b):
    t=np.clip(((p-a)/(b-a)).real,0,1)
    return abs(p-a-t*(b-a))

ix=[i for i,p in enumerate(c)
    if min(distseg(p,a,b) for a,b in be)>3]

def cell(i,tau):
    P=[complex(-2,-2),complex(2,-2),complex(2,2),complex(-2,2)]
    for j,q in enumerate(c-c[i]):
        if i==j or abs(q)>3+1e-9:
            continue
        rhs=(abs(q)**2+tau*(w[i]-w[j]))/2
        out=[]
        for a,b in zip(P,P[1:]+P[:1]):
            fa=(q.conjugate()*a).real-rhs
            fb=(q.conjugate()*b).real-rhs
            if fa<=1e-9:
                out.append(a)
            if (fa<-1e-9 and fb>1e-9) or (fb<-1e-9 and fa>1e-9):
                out.append(a+(b-a)*fa/(fa-fb))
        P=out
        if not P:
            break
    return [p for j,p in enumerate(P) if abs(p-P[j-1])>1e-7]

print('EXPLORATORY FLOAT DIAGNOSTIC; NOT A PROOF')
print('rhombs',len(R),'numerically complete-radius3 centers',len(ix))
for t in [-.25,-.125,0,.125,.25]:
    counts=Counter(len(cell(i,t)) for i in ix)
    witness=next(((i,len(cell(i,t))) for i in ix if len(cell(i,t))<5),None)
    print('tau',t,'side counts',dict(counts),'small-cell witness',witness)
