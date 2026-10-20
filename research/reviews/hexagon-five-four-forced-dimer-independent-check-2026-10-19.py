#!/usr/bin/env python3
"""Independent complete finite reconstruction; does not import producer."""
import itertools
import json
from pathlib import Path
D=json.loads(Path("research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json").read_text())
A=(0,1,2,0,3,4)
words=set(itertools.permutations((0,0,1,1,2,3)))
assert {tuple(r["B"]) for r in D["rows"]}==words and len(D["rows"])==180
def canonical(t): return min(t,t[1:]+t[:1],t[2:]+t[:2])
for row in D["rows"]:
    W=A+tuple(row["B"])
    P=tuple(itertools.product(range(12),(-1,1)))
    entry={}; departure={}; endpoints={}
    for f in range(2):
        for j in range(6):
            s=6*f+j
            endpoints[s]={6*f+(j-1)%6,s}
            entry[s,1]=s; departure[s,1]=6*f+(j+1)%6
            entry[s,-1]=6*f+(j+1)%6; departure[s,-1]=s
    def remote(p,s): return (next(iter(endpoints[s]-{p[0]})),p[1])
    candidates=set()
    for p,q,r in itertools.product(P,repeat=3):
        if (W[departure[p]]==W[entry[q]] and W[departure[q]]==W[entry[r]] and W[departure[r]]==W[entry[p]]):
            candidates.add(canonical((p,q,r)))
    assert len(candidates)==row["initial_stars"]
    rounds=[]
    while True:
        pairs={(t[i],t[(i+1)%3]) for t in candidates for i in range(3)}
        rejected=set()
        for t in candidates:
            for i in range(3):
                p,q=t[i],t[(i+1)%3]
                if (remote(q,entry[q]),remote(p,departure[p])) not in pairs:
                    rejected.add(t);break
        if not rejected:break
        rounds.append([len(candidates),len(candidates)-len(rejected)])
        candidates-=rejected
    assert rounds==row["pruning_rounds"]
    assert candidates=={tuple(map(tuple,t)) for t in row["fixed_stars"]}
    assert sorted({p[0] for t in candidates for p in t})==row["covered_corners"]
    def edge_state(p,s):return(s,p[1])
    factors=[]
    for corner in (None,0,1,2,3)*2:
        F=set()
        for t in candidates:
            for i in range(3):
                p,q,r=t[i],t[(i+1)%3],t[(i+2)%3]
                if corner is None:
                    if p==(4,1) and q==(5,1):
                        F.add((edge_state(r,departure[r]),edge_state(r,entry[r])))
                elif p==(corner,1):
                    F.add((edge_state(r,departure[r]),edge_state(q,entry[q])))
        factors.append(F)
    paths={(a,b) for a,b in factors[0]}
    for F in factors[1:]:
        paths={p+(b,) for p in paths for a,b in F if p[-1]==a}
    cycles={p for p in paths if p[-1]==p[0]}
    assert cycles=={tuple(map(tuple,p)) for p in row["boundary_coronas"]}
    opts={}
    for t in candidates:
        for i in range(3):
            p,q=t[i],t[(i+1)%3]
            opts.setdefault(edge_state(p,departure[p]),set()).add(edge_state(q,entry[q]))
    certain={(k,next(iter(v))) for k,v in opts.items() if len(v)==1}
    assert certain=={(tuple(x["side"]),tuple(x["neighbor"])) for x in row["certain_transitions"]}
print("PASS independently reconstructed all 180 greatest fixed atlases, pruning rounds, corner coverage, certain transitions and ten-edge corona sets")
