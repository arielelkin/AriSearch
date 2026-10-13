#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import product
from sage.all import QuadraticField,QQ,AA
K=QuadraticField(-1,"i");i=K.gen();U=(8+15*i)/17
cross=lambda a,b:QQ((a.conjugate()*b-a*b.conjugate())/(2*i))
D=json.loads((Path(__file__).resolve().parents[2]/"research/certificates/terra-five-one-002112-rational-geometry.json").read_text())
assert (AA(2)-AA(2).sqrt()).sqrt()/2<QQ(8)/17<(AA(10)-2*AA(5).sqrt()).sqrt()/4
assert U.real()!=QQ(1)/2
edges=(K(1),U,-U**5,K(-1),-U**-5,U**-1)
a=QQ(1);b=QQ(383444911)/476356015;c=QQ(1419857)/1561823
assert [str(x) for x in(a,b,c)]==D["A_class_lengths"] and a>c>b>0
assert c==U**5*(1+U)/(1+U**11)
assert b==U**4*(1+U)*(1+U**7)/((1+U**5)*(1+U**11))
ls=(a,a,b,b,c,c);vs=[K(0)]
for l,e in zip(ls,edges):vs.append(vs[-1]+l*e)
assert vs[-1]==0 and [str(x) for x in vs[:-1]]==D["A_vertices"]
assert all(cross(vs[j+1]-vs[j],vs[k]-vs[j])>0 for j in range(6) for k in range(6) if k not in(j,(j+1)%6))
arms=[(ls[(k-1)%6],ls[k])[::-1] for k in(0,4,2)]
assert all(arms[k][1]==arms[(k+1)%3][0] for k in range(3))
C=(0,0,2,1,1,2)
for r,s in product(range(6),(1,-1)):
    colours=[C[(r+s*k)%6] for k in range(6)]
    lengths=[ls[(r+k)%6] if s==1 else ls[(r-k-1)%6] for k in range(6)]
    assert not(len(set(colours[:3]))==3 and lengths[2]==lengths[5])
    assert not(len({colours[0],colours[1],colours[3]})==3 and lengths[1]==lengths[3] and lengths[2]==lengths[5])
E=-U**-2;den=cross(E,E**4);assert den>0
choices=list(product((1,2),(0,2),(0,2),(1,2)))
assert [tuple(row["AB_class_choices"]) for row in D["B_closure_rows"]]==choices and len(choices)==16
for ch,row in zip(choices,D["B_closure_rows"]):
    classes=(a,b,c);target=-sum((classes[t]*E**j for t,j in zip(ch,(0,2,3,5))),K(0))
    p=cross(target,E**4)/den;q=cross(E,target)/den
    assert [str(p),str(q)]==row["BB_lengths"]
    assert p<=-2*c*QQ(E.real())<0 and q<=-2*c*QQ(E.real())<0
    assert row["status"]=="nonpositive BB closure length"
# Independently verify all64 native equality constraints on all203 partitions.
ps=[()]
for _ in range(6):ps=[w+(j,) for w in ps for j in range(max(w,default=-1)+2)]
expected=list(product(product((0,1),(3,4),(2,5)),product((1,-1),repeat=3)))
assert [(tuple(r["corners"]),tuple(r["arm_signs"])) for r in D["AAA_native_cases"]]==expected
for rec,(cs,sg) in zip(D["AAA_native_cases"],expected):
    part=rec["required_side_partition"]
    for w in ps:
        rays=[(w[(j-1)%6],w[j])[::sign] for j,sign in zip(cs,sg)]
        legal=all(rays[k][1]==rays[(k+1)%3][0] for k in range(3))
        refines=all(part[j]!=part[k] or w[j]==w[k] for j in range(6) for k in range(6))
        assert legal==refines
    assert rec["forces_H1"]==(part[0]==part[3])
assert sum(r["forces_H1"] for r in D["AAA_native_cases"])==32
print("PASS exactrational nonmonohedral A002112 AAA polygon;16necessarycentralBfan closures bothBB lengthsnegative with common exactseparator")
