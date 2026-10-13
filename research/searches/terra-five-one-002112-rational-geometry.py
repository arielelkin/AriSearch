#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json
from sage.all import QuadraticField,QQ,AA,QQbar,matrix,vector
K=QuadraticField(-1,"i");i=K.gen();U=(8+15*i)/17
cross=lambda p,q:(p.conjugate()*q-p*q.conjugate())/(2*i)
real=lambda q:QQ(q.real())
# Exact angle bound54<u<67.5 by decreasing cosine.
c54=AA((QQbar.zeta(360)**54).real());c675=(AA(2)-AA(2).sqrt()).sqrt()/2
assert c675<QQ(8)/17<c54 and U!=QQbar.zeta(6)
Adirs=(K(1),U,-U**5,K(-1),-U**-5,U**-1)
G=(Adirs[0]+Adirs[1],Adirs[2]+Adirs[3],Adirs[4]+Adirs[5])
v=(cross(G[1],G[2]),cross(G[2],G[0]),cross(G[0],G[1]))
Aclasses=tuple(real(x/v[0]) for x in v);a,b,c=Aclasses
assert min(Aclasses)>0 and len(set(Aclasses))==3
Alen=(a,a,b,b,c,c)
def polygon(ls,ds):
    vs=[K(0)]
    for l,d in zip(ls,ds):vs.append(vs[-1]+l*d)
    assert vs[-1]==0
    assert all(cross(vs[j]-vs[k],vs[t]-vs[k])>0 for k in range(6) for j in((k+1)%6,) for t in range(6) if t not in(k,(k+1)%6))
    return vs[:-1]
Averts=polygon(Alen,Adirs)
# AAA corners0,4,2, all arm reversals -1.
arms=[(Alen[(j-1)%6],Alen[j])[::-1] for j in(0,4,2)]
assert all(arms[j][1]==arms[(j+1)%3][0] for j in range(3)) and a!=b
E=-U**-2;Bdirs=tuple(E**j for j in range(6));M=matrix(QQ,[[real(Bdirs[j]) for j in(1,4)],[real(Bdirs[j]/i) for j in(1,4)]])
assert M.det()!=0
rows=[]
for AB in product((1,2),(0,2),(0,2),(1,2)):
    sides=[None]*6
    for side,choice in zip((0,2,3,5),AB):sides[side]=Aclasses[choice]
    R=-sum((sides[j]*Bdirs[j] for j in(0,2,3,5)),K(0))
    p,q=M.solve_right(vector(QQ,[real(R),real(R/i)]));sides[1]=p;sides[4]=q
    status="positive strict convex" if p>0 and q>0 else"nonpositive BB closure length"
    if p>0 and q>0:polygon(sides,Bdirs)
    rows.append(dict(AB_class_choices=AB,BB_lengths=[str(p),str(q)],status=status))
AAA=[]
for corners in product((0,1),(3,4),(2,5)):
    for signs in product((1,-1),repeat=3):
        parent=list(range(6))
        def find(t):
            while parent[t]!=t:t=parent[t]
            return t
        rays=[((t-1)%6,t)[::sign] for t,sign in zip(corners,signs)]
        for t in range(3):parent[find(rays[t][1])]=find(rays[(t+1)%3][0])
        seen={};part=tuple(seen.setdefault(find(t),len(seen)) for t in range(6))
        AAA.append(dict(corners=corners,arm_signs=signs,required_side_partition=part,forces_H1=part[0]==part[3]))
assert len(AAA)==64 and sum(r["forces_H1"] for r in AAA)==32
result=dict(scope="Oneexactrational A002112 on B5+1line; legalnonmonohedralAAA;16 centralABfan Bclosure choices beforechainendpoint tests",
 U="(8+15i)/17",A_class_lengths=[str(x) for x in Aclasses],A_vertices=[str(x) for x in Averts],
 AAA_native_cases=AAA,AAA_corners=[0,4,2],AAA_arm_signs=[-1,-1,-1],B_closure_rows=rows)
Path("research/certificates/terra-five-one-002112-rational-geometry.json").write_text(json.dumps(result,indent=2)+"\n")
print("Aclasses",Aclasses,"Bpositive",sum(r["status"]=="positive strict convex" for r in rows))
for row in rows:
 if row["status"]=="positive strict convex":print(row)
