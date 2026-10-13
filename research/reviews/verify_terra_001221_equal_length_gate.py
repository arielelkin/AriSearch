#!/usr/bin/env python3
from itertools import product,permutations
from pathlib import Path
import json
C=(0,0,1,2,2,1);placements=list(product(range(6),(1,-1)))
def corner(r,s,k):return C[(r+s*k)%6]
def side(r,s,k):return (r+k)%6 if s==1 else(r-k-1)%6

def main():
    root=Path(__file__).resolve().parents[2]
    D=json.loads((root/"research/certificates/terra-001221-all-metric-native-rings.json").read_text())
    can=lambda t:min(tuple(t[(r+s*k)%6] for k in range(6)) for r,s in placements)
    words={can(t) for t in permutations(C)};allowed={(0,0),(0,1),(1,2),(2,2)}
    assert len(words)==11
    assert {w for w in words if all(tuple(sorted((w[k],w[(k+1)%6]))) in allowed for k in range(6))}=={C}
    expected=[];graphs=[]
    for bi,(br,bs) in enumerate(placements):
        choices=[[ai for ai,(r,s) in enumerate(placements) if corner(r,s,k+2)==corner(br,bs,k)
            and corner(r,s,k+3)==corner(br,bs,k-1)] for k in range(6)]
        assert all(len(c)==2 for c in choices)
        for ring in product(*choices):
            expected.append((bi,ring));eq=[]
            for k in range(6):
                r,s=placements[ring[k]];u,v=placements[ring[(k+1)%6]]
                eq.append([side(r,s,k+1),side(u,v,k+4)])
            # Independent transitive closure via graph reachability, not DSU.
            reached={0}
            for _ in range(6):
                for x,y in eq:
                    if x in reached or y in reached:reached.update((x,y))
            assert reached==set(range(6));graphs.append(eq)
    assert len(expected)==768
    assert [(r["B_placement"],tuple(r["A_tuple"])) for r in D["raw_rings"]]==expected
    assert [r["AA_equalities"] for r in D["raw_rings"]]==graphs
    # Project all graphs independently through every actual-side partition.
    ps=[()]
    for _ in range(6):ps=[p+(k,) for p in ps for k in range(max(p,default=-1)+2)]
    assert len(ps)==203
    assert [tuple(r["A_partition"]) for r in D["records"]]==ps
    for p,row in zip(ps,D["records"]):
        ids=[i for i,eq in enumerate(graphs) if all(p[x]==p[y] for x,y in eq)]
        assert ids==row["AA_ring_ids"]
        assert bool(ids)==(len(set(p))==1)
    assert D["counts"]["AA"]==768 and D["counts"]["nonmonohedral_full"]==0
    print("PASS only B001221 endpoint-compatible; all768 exhaustive nativeAA graphs connected; all203partitions force equilateralA and H1 omission escape")
if __name__=="__main__":main()
