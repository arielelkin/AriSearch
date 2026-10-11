#!/usr/bin/env python3
"""Small same-author certificate checker, no producer imports.

Derive the local cases from all permutations, trig closure rows directly
from zeta28, the full metric kernels, positivity endpoints and coincidence
ratios. Verify glide geometry and the repeated-length continuum embedding.
This is mechanical certificate replay, not a fresh hostile review.
"""
from itertools import permutations,combinations
import json
from pathlib import Path
from sage.all import AA,CyclotomicField,NumberField,PolynomialRing,QQ,RIF,matrix,vector

def main():
    root=Path(__file__).resolve().parents[2]
    c=json.loads((root/"research/certificates/two-angle-5-7-equal-private-scaffold.json").read_text())
    R=PolynomialRing(QQ,"x");x=R.gen();f=x**3-x*x-2*x+1
    assert c["field"]["polynomial_coefficients"]==[str(q) for q in f.list()]
    F=NumberField(f,"t",embedding=AA.polynomial_root(f,RIF(QQ(18)/10,QQ(181)/100)));t=F.gen()
    decode=lambda xs:F([QQ(q) for q in xs])
    K=CyclotomicField(28);w=K.gen();eta=w**2;z=eta**2;ii=w**7
    emb=F.hom([eta+1/eta],K)
    cosine=lambda n:(eta**n+eta**(-n))/2
    sine=lambda n:(eta**n-eta**(-n))/(eta-1/eta)
    labels=("L","a","b","c","d","e");H=("L","a","L","b","c","d","e")
    Hpairs={frozenset((H[j-1],H[j])) for j in range(7)}
    required={}
    for perm in permutations(("b","c","d")):
        cycle=("e","a")+perm
        if cycle[2]!="b":continue
        for j in range(3,6):
            left,right=cycle[(j-1)%5],cycle[j%5]
            legal=[]
            for side in (left,right):
                h=cycle.index(side)
                if frozenset((cycle[h-1],cycle[(h+1)%5])) in Hpairs:legal.append(side)
            required[(cycle,left,right)]=legal
    assert len(required)==6
    seen=set()
    for row in c["local_cases"]:
        cycle=tuple(row["cycle"]);left,right=row["beta_between"]
        key=(cycle,left,right);assert key in required and key not in seen;seen.add(key)
        assert row["possible_P_P_side_values"]==required[key]
        j=cycle.index(right);order=cycle[j:]+cycle[:j]
        assert list(order)==row["clockwise_from_beta"]
        if not required[key]:
            assert row["verdict"].startswith("untileable")
            continue
        B=matrix(F,[[decode(q) for q in rs] for rs in row["closure_coefficients_L_a"]])
        assert B[:2,:]==matrix.identity(F,2)
        M=matrix(K,[[sum(func(2*j) for j,side in enumerate(H) if side==lab) for lab in labels]
                    for func in (cosine,sine)]+[[sum(func(-3*j) for j,side in enumerate(order) if side==lab) for lab in labels]
                    for func in (cosine,sine)])
        assert M.rank()==4 and M*matrix(K,[[emb(q) for q in rs] for rs in B.rows()])==0
        if row["verdict"].startswith("excluded"):
            assert B[2]==B[5] and B[3]==B[4]
    assert seen==set(required)
    B=matrix(F,[[decode(q) for q in rs] for rs in c["surviving_cone"]["six_length_coefficients"]])
    r=t*t+3*t/2+F(1)/2
    assert B[2].dot_product(vector(F,[1,r]))==0 and B[2,1]<0
    for q in (vector(F,[1,0]),vector(F,[1,r])):
        values=B*q
        assert all(values[j]>0 for j in (0,3,4,5)) and values[1]>=0 and values[2]>=0
    collision={}
    for i,j in combinations(range(6),2):
        n=B[i]-B[j];assert n!=0
        if n[1]:
            q=-n[0]/n[1]
            if 0<q<r:collision.setdefault(q,[]).append((labels[i],labels[j]))
    actual={decode(row["ratio"]):[tuple(p) for p in row["equal_pairs"]]
            for row in c["surviving_cone"]["forbidden_a_over_L"]}
    assert actual==collision and len(actual)==10
    q=vector(F,[QQ(x) for x in c["surviving_cone"]["generic_fixture_parameters"]]);values=B*q
    assert all(v>0 for v in values) and len(set(values))==6
    assert [decode(q) for q in c["surviving_cone"]["generic_fixture_lengths"]]==list(values)
    L,a,b,cv,d,e=B.rows()
    # Direct old-continuum identities after j'=2-j; no source import.
    assert L==(-t*t+t+1)*a+(t*t/2-t-F(1)/2)*L+(t-F(1)/2)*d+b
    assert e==t*b-(t*t-1)*L/2+d/2
    assert cv==(t-1)*a+L/2+(-t*t+t+1)*d/2
    assert d==(t*t-t-1)*a-(t*t-1)*L/2+d/2+b
    S=PolynomialRing(K,names=("private_L","shared_a"));ll,aa=S.gens()
    M0=ll/2;M2=ll+aa*z+ll*z*z/2;D=M2-M0
    conjugate=lambda p:S({mon:coeff.conjugate() for mon,coeff in S(p).dict().items()})
    glide=lambda p:z*z*conjugate(p)-ll*z*z-aa*z
    assert D==z*(ll*(z+1/z)/2+aa)
    assert z*z*conjugate(D)==D and glide(M2)==M0
    assert glide(glide(S(0)))==-2*D
    print("PASS six local cases, three full closure kernels, complete positive cone/ten collision ratios, glide and periodic embedding.",flush=True)

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Assertions required")
    main()
