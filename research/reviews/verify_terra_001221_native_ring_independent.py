#!/usr/bin/env python3
"""Independent edge-indexed B ring; no author imports, no solver.
Neighbour i is opposite central SIDE i, rather than producer neighbour k
opposite side k-1. Endpoint and seam flags are shifted correspondingly.
"""
from itertools import product
from pathlib import Path
import json
Acol=(0,0,1,1,2,2);Alen=(0,0,1,1,2,2)
Bcol=(0,0,1,2,2,1);Blen=(0,0,1,2,1,0)
placement=list(product(range(6),(1,-1)))
def vertex(c,p,g):return c[(p[0]+p[1]*g)%6]
def edge(l,p,g):return l[(p[0]+g)%6] if p[1]==1 else l[(p[0]-g-1)%6]
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/terra-001221-native-ring.json").read_text())
for cw,lw,key in ((Acol,Alen,"A_placements"),(Bcol,Blen,"B_placements")):
    assert len(c[key])==12
    for p,q in zip(placement,c[key]):
        assert (q["native_rotation"],q["native_sign"])==p
        assert q["corners"]==[vertex(cw,p,g) for g in range(6)]
        assert q["sides"]==[edge(lw,p,g) for g in range(6)]
assert len(c["rows"])==12
count=0
for bi,b in enumerate(placement):
    row=c["rows"][bi];assert row["B_native_placement"]==bi
    choices=[]
    for i in range(6):
        choices.append([ai for ai,a in enumerate(placement)
            if vertex(Acol,a,i+3)==vertex(Bcol,b,i+1)
            and vertex(Acol,a,i+4)==vertex(Bcol,b,i)
            and edge(Alen,a,i+3)==edge(Blen,b,i)])
    assert choices==[row["A_choices"][(i+1)%6] for i in range(6)]
    stored={tuple(q["A_native_tuple"]):q for q in row["states"]}
    assert len(stored)==4
    seen=set()
    for ns in product(*choices):
        old=(ns[5],)+ns[:5];seen.add(old);q=stored[old]
        bad=[];pairs=[]
        for i in range(6):
            a,d=placement[ns[i]],placement[ns[(i+1)%6]]
            aa,dd=edge(Alen,a,i+2),edge(Alen,d,i+5)
            if aa!=dd:bad.append((i+1)%6);pairs.append(tuple(sorted((aa,dd))))
        assert sorted(bad)==q["AA_bad_seams"] and len(bad)==2
        assert sorted(pairs)==[(0,2),(1,2)]
        assert q["survives"] is False
        count+=1
    assert seen==set(stored)
assert count==48
assert c["counts"]=={"AB_rings":48,"AA_seam_survivors":0,"outer_complete_survivors":0}
print("PASS: independent side-indexed48 complete reflected AB rings; each has exactly one a/c and one b/c AA mismatch; no seam-compatible B ring")
