#!/usr/bin/env python3
from itertools import product,permutations
from pathlib import Path
import json
AC=(0,0,1,1,2,2);AS=tuple(range(6));P=list(product(range(6),(1,-1)))
PALETTE={tuple(sorted((AC[i],AC[(i+1)%6]))):i for i in range(6)}
canon=lambda w:min(t[k:]+t[:k] for t in(w,w[::-1]) for k in range(6))
def parts(n):
    out=[()]
    for _ in range(n):out=[w+(x,) for w in out for x in range(max(w,default=-1)+2)]
    return out

def profile(c,l,r,s):
    return dict(rotation=r,sign=s,corners=tuple(c[(r+s*k)%6] for k in range(6)),
        sides=tuple(l[(r+k)%6] if s==1 else l[(r-k-1)%6] for k in range(6)))
def mono(c,l):
    hits=[]
    for r,s in P:
        a=profile(c,l,r,s);x=a["corners"];e=a["sides"]
        if len(set(x[:3]))==3 and e[2]==e[5]:hits.append(("H1",r,s))
        if len({x[0],x[1],x[3]})==3 and e[1]==e[3] and e[2]==e[5]:hits.append(("H2",r,s))
    return hits

def main():
    words=sorted({canon(w) for w in permutations(AC)});A=[profile(AC,AS,r,s) for r,s in P]
    raw=[];bdata=[]
    for wi,bw in enumerate(words):
        bl=tuple(PALETTE[tuple(sorted((bw[i],bw[(i+1)%6])))] for i in range(6));B=[profile(bw,bl,r,s) for r,s in P]
        bdata.append(dict(word=bw,sides=bl,placements=B))
        for bi,b in enumerate(B):
            choices=[[ai for ai,a in enumerate(A) if a["corners"][(k+2)%6]==b["corners"][k]
                and a["corners"][(k+3)%6]==b["corners"][(k-1)%6]] for k in range(6)]
            for ring in product(*choices):
                eq=[];outer=[]
                for k in range(6):
                    a=A[ring[k]];d=A[ring[(k+1)%6]]
                    assert a["sides"][(k+2)%6]==b["sides"][(k-1)%6]
                    eq.append((a["sides"][(k+1)%6],d["sides"][(k+4)%6]))
                    cs=(a["corners"][(k+1)%6],d["corners"][(k+5)%6]);arms=(a["sides"][k],d["sides"][(k+5)%6])
                    species="B" if cs[0]==cs[1] else "A";colour=cs[0] if species=="B" else 3-cs[0]-cs[1]
                    cw,sw=(bw,bl) if species=="B" else (AC,AS)
                    offers=[dict(slot=i,sign=s,arms=tuple((sw[(i-1)%6],sw[i])[::s])) for i in range(6) for s in(1,-1) if cw[i]==colour]
                    outer.append(dict(colours=cs,arms=arms,species=species,colour=colour,offers=offers))
                raw.append(dict(B_word_index=wi,B_placement=bi,A_tuple=ring,AA_equalities=eq,outer=outer))
    assert len(raw)==360
    records=[]
    for p in parts(6):
        am=mono(AC,p)
        for wi,b in enumerate(bdata):
            bl=tuple(p[i] for i in b["sides"]);bm=mono(b["word"],bl)
            aa=[];full=[]
            for ri,r in enumerate(raw):
                if r["B_word_index"]!=wi:continue
                if not all(p[i]==p[j] for i,j in r["AA_equalities"]):continue
                aa.append(ri)
                if all(any(p[o["arms"][0]]==p[f["arms"][0]] and p[o["arms"][1]]==p[f["arms"][1]] for f in o["offers"]) for o in r["outer"]):full.append(ri)
            records.append(dict(A_partition=p,B_word_index=wi,A_monohedral_matches=am,B_monohedral_matches=bm,
                AA_ring_ids=aa,full_ring_ids=full))
    uncAA=[i for i,r in enumerate(records) if r["AA_ring_ids"] and not r["A_monohedral_matches"] and not r["B_monohedral_matches"]]
    uncfull=[i for i,r in enumerate(records) if r["full_ring_ids"] and not r["A_monohedral_matches"] and not r["B_monohedral_matches"]]
    out=dict(scope="ALL203 actualsixAsidepartitions*11Bbracelets;360 completeindexedrawABrings*203 projections; allAAseams and nativeouterAAA/AABcompletions; genericangleidentities; noactualclosure assumption inferred from formalpartitions",A_placements=A,B_words=bdata,raw_rings=raw,records=records,
        counts=dict(partitions=203,B_words=11,raw_indexed_AB_rings=360,projected_AB_rings=73080,
            records_with_AA=sum(bool(r["AA_ring_ids"]) for r in records),records_with_full=sum(bool(r["full_ring_ids"]) for r in records),uncovered_AA=len(uncAA),uncovered_full=len(uncfull)),
        uncovered_AA_record_ids=uncAA,uncovered_full_record_ids=uncfull)
    Path("research/certificates/terra-001122-all-metric-native-rings.json").write_text(json.dumps(out,indent=2)+"\n")
    print(out["counts"])
    from collections import Counter
    print("uncoveredfull byBword",{"".join(map(str,words[k])):v for k,v in Counter(records[i]["B_word_index"] for i in uncfull).items()})
if __name__=="__main__":main()
