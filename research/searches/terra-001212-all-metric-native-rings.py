#!/usr/bin/env python3
from itertools import product,permutations
from pathlib import Path
import json
C=(0,0,1,2,1,2);S=tuple(range(6));P=list(product(range(6),(1,-1)))
def parts():
    out=[()]
    for _ in range(6):out=[w+(i,) for w in out for i in range(max(w,default=-1)+2)]
    return out

def profile(c,l,r,s):
    return dict(rotation=r,sign=s,corners=tuple(c[(r+s*k)%6] for k in range(6)),
        sides=tuple(l[(r+k)%6] if s==1 else l[(r-k-1)%6] for k in range(6)))
def mono(c,l):
    ans=[]
    for r,s in P:
        a=profile(c,l,r,s);x=a["corners"];e=a["sides"]
        if len(set(x[:3]))==3 and e[2]==e[5]:ans.append(("H1",r,s))
        if len({x[0],x[1],x[3]})==3 and e[1]==e[3] and e[2]==e[5]:ans.append(("H2",r,s))
    return ans

def main():
    can=lambda w:min(t[k:]+t[:k] for t in(w,w[::-1]) for k in range(6))
    words=sorted({can(w) for w in permutations(C)});allowed={(0,0),(0,1),(1,2),(0,2)}
    survivors=[w for w in words if all(tuple(sorted((w[i],w[(i+1)%6]))) in allowed for i in range(6))]
    assert survivors==[(0,0,1,2,1,2),(0,1,0,2,1,2),(0,1,2,0,1,2),(0,1,2,0,2,1),(0,1,2,1,0,2)]
    A=[profile(C,S,r,s) for r,s in P];raw=[]
    for wi,bw in enumerate(survivors):
        for bi,(br,bs) in enumerate(P):
            B=profile(bw,S,br,bs);choices=[[ai for ai,a in enumerate(A) if a["corners"][(k+2)%6]==B["corners"][k]
                and a["corners"][(k+3)%6]==B["corners"][(k-1)%6]] for k in range(6)]
            for ring in product(*choices):
                bl=[None]*6
                for k in range(6):
                    side=(k-1)%6;native=B["sides"][side]
                    bl[native]=A[ring[k]]["sides"][(k+2)%6]
                eq=[];outer=[]
                for k in range(6):
                    a=A[ring[k]];d=A[ring[(k+1)%6]]
                    eq.append((a["sides"][(k+1)%6],d["sides"][(k+4)%6]))
                    cs=(a["corners"][(k+1)%6],d["corners"][(k+5)%6]);arms=(a["sides"][k],d["sides"][(k+5)%6])
                    species="B" if cs[0]==cs[1] else "A";colour=cs[0] if species=="B" else 3-sum(cs)
                    cw,sw=(bw,bl) if species=="B" else (C,S)
                    offers=[dict(slot=i,sign=s,arms=tuple((sw[(i-1)%6],sw[i])[::s])) for i in range(6) for s in(1,-1) if cw[i]==colour]
                    outer.append(dict(colours=cs,arms=arms,species=species,colour=colour,offers=offers))
                raw.append(dict(B_word_index=wi,B_placement=bi,A_tuple=ring,B_native_A_side_sources=bl,AA_equalities=eq,outer=outer))
    assert len(raw)==1080
    records=[]
    for p in parts():
        am=mono(C,p);aa=[];full=[];uncovered=[];bmcache={}
        for ri,r in enumerate(raw):
            if any(p[x]!=p[y] for x,y in r["AA_equalities"]):continue
            aa.append(ri)
            if not all(any([p[x] for x in o["arms"]]==[p[x] for x in f["arms"]] for f in o["offers"]) for o in r["outer"]):continue
            full.append(ri);bmetric=tuple(p[x] for x in r["B_native_A_side_sources"])
            if (r["B_word_index"],bmetric) not in bmcache:bmcache[(r["B_word_index"],bmetric)]=mono(survivors[r["B_word_index"]],bmetric)
            if not am and not bmcache[(r["B_word_index"],bmetric)]:uncovered.append(ri)
        records.append(dict(A_partition=p,A_monohedral_matches=am,AA_ring_ids=aa,full_ring_ids=full,
            B_metric_monohedral_matches=[dict(B_word_index=k[0],B_actual_class_word=k[1],matches=v) for k,v in sorted(bmcache.items())],uncovered_full_ring_ids=uncovered))
    metriccases={(tuple(r["A_partition"]),raw[i]["B_word_index"],tuple(r["A_partition"][x] for x in raw[i]["B_native_A_side_sources"])) for r in records for i in r["uncovered_full_ring_ids"]}
    out=dict(scope="Genericfive-star A001212 allsixAsidepartitions;fiveBwords byendpointpalette;1080rawnativeB/A rings*203=219240 metricprojections;nativeAA and outerAAA/AAB gates;H1H2 sufficient escapes",A_placements=A,B_words=survivors,raw_rings=raw,records=records,
        counts=dict(partitions=203,raw_rings=1080,projections=219240,AA=sum(len(r["AA_ring_ids"]) for r in records),full=sum(len(r["full_ring_ids"]) for r in records),
        nonmonohedral_full=sum(len(r["uncovered_full_ring_ids"]) for r in records),nonmonohedral_joint_metric_cases=len(metriccases)),
        uncovered_joint_metric_cases=sorted(metriccases))
    Path("research/certificates/terra-001212-all-metric-native-rings.json").write_text(json.dumps(out,indent=2)+"\n")
    print(out["counts"])
    from collections import Counter
    print("uncoveredrank",dict(Counter(len(set(p)) for p,wi,b in metriccases)))
    print("uncovered byword",dict(Counter(survivors[wi] for p,wi,b in metriccases)))
    print("outerAAAcounts",dict(Counter(sum(o["species"]=="A" for o in raw[i]["outer"]) for r in records for i in r["uncovered_full_ring_ids"])))
if __name__=="__main__":main()
