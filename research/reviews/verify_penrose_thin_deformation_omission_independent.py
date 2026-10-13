#!/usr/bin/env python3
"""Independent algebraic pentagon convexity and all150 angle-only exclusions.
No producer or family-filter imports; necessary angle rows from Rao Table2.
"""
import json
from pathlib import Path
from collections import defaultdict
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(10);w=K.gen();h=K.hom([QQbar.zeta(10)],QQbar)
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/penrose-dual-fusion-thin-deformation.json").read_text())
P=[sum(K(q)*w**j for j,q in enumerate(v)) for v in c["polygon"]]
cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
assert all(AA(h(cross(P[(i+1)%5]-P[i],P[j]-P[i])))>0
           for i in range(5) for j in range(5) if j not in (i,(i+1)%5))
source=json.loads((root/"research/certificates/penrose-centered-dual-single-fusion-source.json").read_text())
V=[sum(K(q)*w**j for j,q in enumerate(v)) for v in source["verts"]]
pts=[]
for kind,ids,frame in source["rhombs"]:
    pts.append(sum(V[i] for i in ids)/4+(K(1)/100*w**frame if kind=="thin" else 0))
assert P==[pts[i] for i in (3,5,58,6,7)]
positive=lambda x:AA(h(x))>0
edgeowners=defaultdict(list)
for r,(_,ids,_) in enumerate(source["rhombs"]):
    area=sum(cross(V[ids[i]],V[ids[(i+1)%4]]) for i in range(4))
    orient=1 if positive(area) else -1
    assert all(positive(orient*cross(V[ids[(i+1)%4]]-V[ids[i]],pts[r]-V[ids[i]])) for i in range(4))
    for i in range(4):edgeowners[tuple(sorted((ids[i],ids[(i+1)%4])))].append(r)
for (i,j),rs in edgeowners.items():
    if len(rs)!=2:continue
    a,b=pts[rs[0]],pts[rs[1]];v,u=V[i],V[j]
    assert positive(-cross(u-v,a-v)*cross(u-v,b-v))
    assert positive(-cross(b-a,v-a)*cross(b-a,u-a))
for ids in ((3,6,7),(3,5,58,6)):
    Q=[pts[i] for i in ids];n=len(Q)
    assert all(positive(cross(Q[(i+1)%n]-Q[i],Q[j]-Q[i])) for i in range(n) for j in range(n) if j not in (i,(i+1)%n))
Q=[pts[i] for i in c["untouched_quad_rhombs"]]
assert Q==[sum(K(q)*w**j for j,q in enumerate(v)) for v in c["untouched_quad_coordinates"]]
assert all(positive(cross(Q[(i+1)%4]-Q[i],Q[j]-Q[i])) for i in range(4) for j in range(4) if j not in (i,(i+1)%4))
ph=[]
for i in range(5):
    ratio=h((P[i-1]-P[i])/(P[(i+1)%5]-P[i]))
    ph.append(ratio/QQbar((ratio*ratio.conjugate()).real()).sqrt())
    assert ph[-1].imag()>0
# Rows are lists of corner index multisets; target pi only where specified.
rows={
1:[((0,1,2),1)],2:[((0,1,3),1)],
3:[((4,4,4),1),((3,4,4),1),((1,4,4),1)],
4:[((0,1,3),1),((4,4),-1)],
5:[((4,4,4),1),((0,1,3),1)],
6:[((3,4,4),1),((0,2,3),1)],
7:[((3,4,4),1),((0,2,2),1)],
8:[((3,4,4),1),((1,1,2),1)],
9:[((3,4,4),1),((0,0,2),1)],
10:[((2,2,3),1),((1,2,4),1),((0,1,1),1)],
11:[((2,3,3),1),((1,3,4),1),((0,1,1),1)],
12:[((2,3,3),1),((1,3,4),1),((0,1,1),1)],
13:[((1,3,3),1),((0,1,3),1),((4,4),-1)],
14:[((2,3,3),1),((1,3,4),1),((0,1,1),1)],
15:[((2,3,3),1),((1,1,4),1),((0,0,3),1),((4,4),-1)],
}
records={(r["type"],r["epsilon"],r["offset"]):r for r in c["family_tests"]}
assert len(records)==150
for typ,equations in rows.items():
    for epsilon in (1,-1):
        for offset in range(5):
            failures=[]
            for index,(indices,target) in enumerate(equations):
                phase=QQbar(1)
                for i in indices:phase*=ph[(offset+epsilon*i)%5]
                if phase!=target:failures.append({"angle_equation":index})
            assert failures and records[typ,epsilon,offset]["failures"]==failures
assert c["compatible_family_tests"]==[]
print("PASS: independent15-row Rao angle reconstruction, all150 reflected relabellings fail; exact source pentagon and strict supports")
