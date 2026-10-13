#!/usr/bin/env python3
"""Separate brute equivalence-relation checker, no producer imports."""
import json
from itertools import product
from pathlib import Path

def words(n):
    result=[()]
    for _ in range(n):
        result=[w+(k,) for w in result for k in range(max(w,default=-1)+2)]
    return result

def allows(w,cs,sg):
    incoming=[];outgoing=[]
    for i,s in zip(cs,sg):
        a,b=w[(i-1)%6],w[i]
        if s==-1:a,b=b,a
        incoming.append(a);outgoing.append(b)
    return outgoing[0]==incoming[1] and outgoing[1]==incoming[2] and outgoing[2]==incoming[0]

def refines(a,b):
    return all(a[i]!=a[j] or b[i]==b[j] for i in range(len(a)) for j in range(len(a)))

def main():
    root=Path(__file__).resolve().parents[2]
    cert=json.loads((root/"research/certificates/terra-ternary-aaa-equalities.json").read_text())
    all6=words(6);all5=words(5)
    assert len(all6)==203 and len(all5)==52
    rows=cert["unrestricted_cycles"]
    expected=list(product(product((0,3),(1,4),(2,5)),product((1,-1),repeat=3)))
    assert [(tuple(r["corners"]),tuple(r["arm_reversals"])) for r in rows]==expected
    direct=0
    for r in rows:
        cs,sg,p=r["corners"],r["arm_reversals"],r["required_partition"]
        assert tuple(p) in all6
        # Full203-partition truth table independently establishes required equivalence relation.
        assert all(allows(w,cs,sg)==refines(p,w) for w in all6)
        opp=[i for i in range(3) if p[i]==p[i+3]]
        assert opp==r["opposite_equalities"]
        if opp:direct+=1
        else:
            sig=r["signed_difference_relation"]
            assert len(sig)==3 and all(s in (-1,1) for s in sig)
            for label in set(p):
                assert sum(sig[i]*((p[i]==label)-(p[i+3]==label)) for i in range(3))==0
    records=cert["base_partition_records"]
    assert [tuple(r["partition"]) for r in records]==all5
    base=(0,0,1,2,3,4)
    for r in records:
        w=tuple(r["partition"][i] for i in base)
        assert tuple(r["side_word"])==w
        assert r["AAA_cycle_indices"]==[k for k,(cs,sg) in enumerate(expected) if allows(w,cs,sg)]
    valid=[r for r in records if r["AAA_cycle_indices"]]
    minimal=[r for r in valid if not any(q!=r and refines(q["partition"],r["partition"]) for q in valid)]
    assert minimal==cert["minimal_AAA_records"]
    residual=[r for r in valid if all(r["side_word"][i]!=r["side_word"][i+3] for i in range(3))]
    assert residual==cert["AAA_records_without_opposite_equality"]
    assert direct==56 and len(valid)==34 and len(minimal)==5 and len(residual)==2
    print("PASS independently reconstructed64 AAA cases over203 equivalence relations;52 base specializations,34 admitting,5 minimal;56 opposite and8 signed-kernel cases")
if __name__=="__main__":main()
