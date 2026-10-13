#!/usr/bin/env python3
"""Exact finite equality classification, with no polygon or tiling search."""
from itertools import product
import json
from pathlib import Path

def canonical(w):
    seen={}; return tuple(seen.setdefault(x,len(seen)) for x in w)
def partitions(n):
    if n==0:
        yield (); return
    for w in partitions(n-1):
        for x in range(max(w,default=-1)+2): yield w+(x,)
def finer(a,b):
    return all(a[i]!=a[j] or b[i]==b[j] for i in range(len(a)) for j in range(len(a)))
def cycle_partition(cs,sg):
    parent=list(range(6))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    rays=[((i-1)%6,i)[::s] for i,s in zip(cs,sg)]
    for k in range(3):parent[find(rays[k][1])]=find(rays[(k+1)%3][0])
    return canonical(tuple(find(i) for i in range(6)))
def relation(w):
    # Signs sigma give identically sum sigma_i(a_i-a_{i+3})=0.
    for sig in product((-1,1),repeat=3):
        coeff=[0]*(max(w)+1)
        for i,s in enumerate(sig):coeff[w[i]]+=s;coeff[w[i+3]]-=s
        if not any(coeff):return sig
    return None

def main():
    rows=[]
    for cs in product((0,3),(1,4),(2,5)):
        for sg in product((1,-1),repeat=3):
            w=cycle_partition(cs,sg)
            opp=[i for i in range(3) if w[i]==w[i+3]]
            rel=relation(w)
            assert opp or rel is not None
            rows.append(dict(corners=cs,arm_reversals=sg,required_partition=w,
                             opposite_equalities=opp,signed_difference_relation=rel))
    assert len(rows)==64
    assert sum(bool(r["opposite_equalities"]) for r in rows)==56
    base=(0,0,1,2,3,4)
    records=[]
    for p in partitions(5):
        w=tuple(p[i] for i in base)
        hits=[k for k,r in enumerate(rows) if finer(r["required_partition"],w)]
        records.append(dict(partition=p,side_word=w,AAA_cycle_indices=hits))
    valid=[r for r in records if r["AAA_cycle_indices"]]
    minimal=[r for r in valid if not any(q!=r and finer(q["partition"],r["partition"]) for q in valid)]
    assert len(records)==52 and len(valid)==34 and len(minimal)==5
    assert {tuple(r["partition"]) for r in minimal}=={
        (0,1,0,2,3),(0,1,1,2,2),(0,1,2,0,3),(0,1,2,1,2),(0,1,2,3,1)}
    residual=[r for r in valid if all(r["side_word"][i]!=r["side_word"][i+3] for i in range(3))]
    assert len(residual)==2
    out=dict(scope="64 unrestricted oriented AAA native cases; all52 partitions coarsening a0=a1; combinatorial equalities only",
             unrestricted_cycles=rows,base_partition_records=records,minimal_AAA_records=minimal,
             AAA_records_without_opposite_equality=residual,
             counts=dict(cycles=64,direct_opposite_cases=56,signed_relation_cases=8,
                         base_partitions=52,AAA_admitting=34,AAA_absent=18,minimal_AAA=5))
    target=Path("research/certificates/terra-ternary-aaa-equalities.json")
    target.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out["counts"],sort_keys=True))
if __name__=="__main__":main()
