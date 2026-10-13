#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import permutations,product
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(360);q=K.gen();j=q**90
wedge=lambda p,r:(p.conjugate()*r-p*r.conjugate())/(2*j)
G=[1+q**67,q**126+q**185,q**239+q**293]
kernel=[wedge(G[1],G[2]),wedge(G[2],G[0]),wedge(G[0],G[1])]
L=[x/kernel[0] for x in kernel]
anglesA=(0,0,1,1,2,2);sideA=(0,0,1,1,2,2)
canon=lambda t:min(tuple(t[(i+s*k)%6] for k in range(6)) for i in range(6) for s in(-1,1))
words=sorted({canon(t) for t in permutations(anglesA)})
root=Path(__file__).resolve().parents[2]
data=json.loads((root/"research/certificates/terra-001122-b-neighbourhood.json").read_text())
assert [tuple(r["B_word"]) for r in data["B_rows"]]==words
# Independently reconstruct fan pairs by testing both spatial AA-edge choices.
for colour in range(3):
    possible=set()
    for i in range(6):
        for h in range(6):
            if anglesA[i]!=colour or anglesA[h]!=colour:continue
            ai=(sideA[(i-1)%6],sideA[i]);ah=(sideA[(h-1)%6],sideA[h])
            for t,u in product((0,1),repeat=2):
                if ai[t]==ah[u]:possible.add((ai[1-t],ah[1-u]))
    assert possible=={tuple(p) for p in data["fans"][colour]["ordered_pairs"]}
expectedpalette={(0,0):0,(0,1):0,(1,1):1,(1,2):1,(2,2):2,(0,2):2}
assert {(tuple(r["endpoint_pair"]),r["side_class"]) for r in data["palette"]}==set(expectedpalette.items())
closed=[]
for row in data["B_rows"]:
    bw=row["B_word"]
    metric=[expectedpalette[tuple(sorted((bw[i],bw[(i+1)%6])))] for i in range(6)]
    assert metric==row["forced_side_classes"]
    d=[sum(180-(134,118,108)[bw[t]] for t in range(1,i+1)) for i in range(6)]
    assert d==row["directions"]
    edges=[L[m]*q**e for m,e in zip(metric,d)]
    residue=sum(edges,K(0))
    assert (residue==0)==row["closes"]
    assert str(residue)==row["exact_residue_polynomial"]
    if residue==0:
        closed.append(tuple(bw));assert bw[:3]==bw[3:] and metric[:3]==metric[3:]
        vs=[sum(edges[:i],K(0)) for i in range(6)]
        h=K.hom([QQbar.zeta(360)],QQbar)
        assert all(AA(h(wedge(edges[i],vs[t]-vs[i])).real())>0 for i in range(6) for t in range(6) if t not in(i,(i+1)%6))
assert closed==[(0,1,2,0,1,2)]
print("PASS exact all11 fixedA necessaryB metrics:10 nonzero closures; sole positive convex central B012012 gives omission escape")
