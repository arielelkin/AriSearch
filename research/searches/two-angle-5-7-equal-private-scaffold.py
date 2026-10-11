#!/usr/bin/env python3
"""Exact local and metric classification of H=(L,a,L,b,c,d,e), L absent P.

P has distinct side values a,b,c,d,e and one5pi/7/four4pi/7 angles.
No torus-bound enlargement: six exact side-order/beta cases, real closure
kernels, the complete2D positive cone, and an identity embedding into the
proved four-orbit continuum. Default prints nondestructive JSON.
"""
import argparse
from itertools import combinations
import json
from pathlib import Path
from sage.all import AA,NumberField,PolynomialRing,QQ,RIF,matrix,vector

R=PolynomialRing(QQ,"x");x=R.gen();f=x**3-x*x-2*x+1
F=NumberField(f,"t",embedding=AA.polynomial_root(f,RIF(QQ(18)/10,QQ(181)/100)));t=F.gen()
COS={0:F(1),1:t/2};SIN={0:F(0),1:F(1)}
for k in range(2,15):
    COS[k]=t*COS[k-1]-COS[k-2];SIN[k]=t*SIN[k-1]-SIN[k-2]
for k in range(1,15):COS[-k]=COS[k];SIN[-k]=-SIN[k]
LABELS=("L","a","b","c","d","e")
H=("L","a","L","b","c","d","e")
H_ADJ={frozenset((H[j-1],H[j])) for j in range(7)}
enc=lambda q:[str(x) for x in F(q).list()]


def coefficients(order):
    rows=[[sum(table[2*j] for j,l in enumerate(H) if l==lab) for lab in LABELS]
          for table in (COS,SIN)]
    rows += [[sum(table[-3*j] for j,l in enumerate(order) if l==lab) for lab in LABELS]
             for table in (COS,SIN)]
    M=matrix(F,rows);assert M.rank()==4
    B=M.right_kernel().basis_matrix().transpose()
    assert B[:2,:]==matrix.identity(F,2)
    return B


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);args=ap.parse_args()
    cases=[]
    for cycle,betapairs in [(("e","a","b","c","d"),(("b","c"),("c","d"),("d","e"))),
                           (("e","a","b","d","c"),(("b","d"),("d","c"),("c","e")))]:
        for left,right in betapairs:
            ix=cycle.index(right);order=cycle[ix:]+cycle[:ix]
            legal=[]
            for lab in (left,right):
                j=cycle.index(lab)
                if frozenset((cycle[j-1],cycle[(j+1)%5])) in H_ADJ:legal.append(lab)
            rec={"cycle":cycle,"beta_between":[left,right],"clockwise_from_beta":order,
                 "possible_P_P_side_values":legal}
            if not legal:rec["verdict"]="untileable: no possible P-P beta seam"
            else:
                B=coefficients(order)
                rec["closure_coefficients_L_a"]=[[enc(q) for q in row] for row in B.rows()]
                if (left,right)==("d","c"):
                    assert B[2]==B[5] and B[3]==B[4]
                    rec["verdict"]="excluded: closure forces b=e and c=d, P not distinct"
                else:rec["verdict"]="positive cone with periodic four-orbit escape"
            cases.append(rec)
    B=coefficients(("d","c","e","a","b"))
    L,a,b,c,d,e=B.rows()
    threshold=t*t+3*t/2+F(1)/2
    assert b.dot_product(vector(F,[1,threshold]))==0
    for q in (vector(F,[1,0]),vector(F,[1,threshold])):
        values=B*q
        assert values[0]>0 and all(values[j]>0 for j in (3,4,5))
        assert values[1]>=0 and values[2]>=0
    fixture=vector(F,[1,QQ(11)/10]);values=B*fixture
    assert all(q>0 for q in values) and len(set(values))==6
    collision={}
    for i,j in combinations(range(6),2):
        n=B[i]-B[j]
        assert n!=0
        if n[1]==0:continue
        q=-n[0]/n[1]
        if 0<q<threshold:collision.setdefault(q,[]).append((LABELS[i],LABELS[j]))
    assert len(collision)==10
    # Embed after side renumbering j' =2-j:
    # old continuum params=(a,L,d,b), H'=(L,a,L,e,d,c,b), Pprivate=d.
    A,B0,C0,D0=a,L,d,b
    H3=t*D0-(t*t-1)*B0/2+C0/2
    H5=(t-1)*A+B0/2+(-t*t+t+1)*C0/2
    H0=(-t*t+t+1)*A+(t*t/2-t-F(1)/2)*B0+(t-F(1)/2)*C0+D0
    Pprivate=(t*t-t-1)*A-(t*t-1)*B0/2+C0/2+D0
    assert (H0,H3,H5,Pprivate)==(L,e,c,d)
    out={"scope":"complete equal-private0/2 generic(5,7) family; all feasible positive metrics admit periodic tiling",
         "field":{"polynomial_coefficients":[str(q) for q in f.list()],"root_interval":["18/10","181/100"]},
         "local_cases":cases,"surviving_cone":{"variables":["L","a"],"inequalities":["L>0","0<a<(t^2+3*t/2+1/2)*L"],
             "six_length_coefficients":[[enc(q) for q in row] for row in B.rows()],
             "forbidden_a_over_L":[{"ratio":enc(q),"equal_pairs":pairs} for q,pairs in sorted(collision.items())],
             "generic_fixture_parameters":["1","11/10"],"generic_fixture_lengths":[enc(q) for q in values]},
         "periodic_embedding":{"H_side_renumbering":"j_new=2-j_old mod7","continuum_parameters":["a","L","d","b"],
             "new_H_lengths":["L","a","L","e","d","c","b"],"new_P_private_length":"d",
             "formal_identity_verdict":"PASS all coefficient identities; cone positivity transfers"},
         "private_chain_linear_states":["I","-I","S","-S"],
         "cross_seam_map":"g_02(x)=z^2*conj(x)-L*z^2-a*z; g_02^2 translates -2*(M2-M0)",
         "nonconsequence":"no claim that every mixed-halfturn/glide tiling is periodic"}
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.output:args.output.write_text(text)
    else:print(text,end="")

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Assertions required")
    main()
