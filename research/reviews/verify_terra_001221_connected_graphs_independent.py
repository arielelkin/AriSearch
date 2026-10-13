#!/usr/bin/env python3
"""Independent side-indexed ring enumeration and BFS equality closure."""
from itertools import permutations,product
from collections import deque
from pathlib import Path
import json
word=(0,0,1,2,2,1);places=list(product(range(6),(1,-1)))
def corner(p,k):return word[(p[0]+p[1]*k)%6]
def side(p,k):return (p[0]+k)%6 if p[1]==1 else (p[0]-k-1)%6
canon=lambda q:min(t[k:]+t[:k] for t in (q,q[::-1]) for k in range(6))
words={canon(q) for q in permutations(word)}
allowed={frozenset((word[i],word[(i+1)%6])) for i in range(6)}
assert len(words)==11
assert {q for q in words if all(frozenset((q[i],q[(i+1)%6])) in allowed for i in range(6))}=={word}
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/terra-001221-all-metric-native-rings.json").read_text())
records={(r["B_placement"],tuple(r["A_tuple"])):r for r in c["raw_rings"]}
assert len(records)==768
seen=set();eqs={}
for bi,b in enumerate(places):
    options=[[ai for ai,a in enumerate(places) if corner(a,i+3)==corner(b,i+1)
              and corner(a,i+4)==corner(b,i)] for i in range(6)]
    assert [len(a) for a in options]==[2]*6
    local=0
    for ns in product(*options):
        old=(ns[5],)+ns[:5];key=(bi,old);seen.add(key);local+=1
        pairs=[];g=[set() for _ in range(6)]
        for i in range(6):
            x,y=side(places[ns[i]],i+2),side(places[ns[(i+1)%6]],i+5)
            pairs.append(((i+1)%6,[x,y]));g[x].add(y);g[y].add(x)
        eq=[p for k,p in sorted(pairs)]
        assert eq==records[key]["AA_equalities"]
        visited={0};queue=deque([0])
        while queue:
            x=queue.popleft()
            for y in g[x]-visited:visited.add(y);queue.append(y)
        assert visited==set(range(6))
        eqs[key]=eq
    assert local==64
assert seen==set(records)
ps=[()]
for _ in range(6):ps=[p+(j,) for p in ps for j in range(max(p,default=-1)+2)]
assert len(ps)==203 and [tuple(r["A_partition"]) for r in c["records"]]==ps
for p,r in zip(ps,c["records"]):
    ids=[i for i,q in enumerate(c["raw_rings"]) if all(p[x]==p[y] for x,y in eqs[q["B_placement"],tuple(q["A_tuple"])])]
    assert ids==r["AA_ring_ids"]
    assert len(ids)==(768 if len(set(p))==1 else 0)
# H1 after starting at native vertex1: colours0,1,2 and opposite sides3,0.
assert {word[i] for i in (1,2,3)}=={0,1,2}
orbit={canon(tuple(p[i] for i in word)) for p in permutations(range(3))}
assert orbit=={(0,0,1,2,2,1),(0,0,2,1,1,2),(0,1,1,0,2,2)}
print("PASS: all11 B bracelets leave001221; independent64 rings per12 placements have connected AA graphs; all203 metric partitions force equilateral A; S3 orbit has3 words")
