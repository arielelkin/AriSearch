#!/usr/bin/env python3
from itertools import product,permutations
from pathlib import Path
import json
Ac=(0,0,1,1,2,2);As=(0,0,1,1,2,2)
P=list(product(range(6),(1,-1)))
ALIASES=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
PALETTE={(0,0):0,(0,1):0,(1,1):1,(1,2):1,(2,2):2,(0,2):2}
canon=lambda w:min(v[k:]+v[:k] for v in(w,w[::-1]) for k in range(6))
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
    words=sorted({canon(w) for w in permutations(Ac)});records=[]
    for alias in ALIASES:
        al=tuple(alias[x] for x in As);A=[profile(Ac,al,r,s) for r,s in P];am=mono(Ac,al)
        for bw in words:
            raw=tuple(PALETTE[tuple(sorted((bw[i],bw[(i+1)%6])))] for i in range(6))
            bl=tuple(alias[x] for x in raw);B=[profile(bw,bl,r,s) for r,s in P];bm=mono(bw,bl)
            rows=[];cnt=0;aa=0;outergood=0
            for bi,b in enumerate(B):
                choices=[[ai for ai,a in enumerate(A) if a["corners"][(k+2)%6]==b["corners"][k]
                    and a["corners"][(k+3)%6]==b["corners"][(k-1)%6]
                    and a["sides"][(k+2)%6]==b["sides"][(k-1)%6]] for k in range(6)]
                rings=[]
                for ring in product(*choices):
                    cnt+=1;bad=[];outer=[]
                    for k in range(6):
                        a=A[ring[k]];d=A[ring[(k+1)%6]]
                        if a["sides"][(k+1)%6]!=d["sides"][(k+4)%6]:bad.append(k)
                        cs=(a["corners"][(k+1)%6],d["corners"][(k+5)%6])
                        arms=(a["sides"][k],d["sides"][(k+5)%6]);sp="B" if cs[0]==cs[1] else "A"
                        col=cs[0] if sp=="B" else 3-cs[0]-cs[1];cw,sw=(bw,bl) if sp=="B" else (Ac,al)
                        opts=[(slot,s) for slot in range(6) for s in(1,-1) if cw[slot]==col and tuple((sw[(slot-1)%6],sw[slot])[::s])==arms]
                        outer.append(dict(colours=cs,arms=arms,species=sp,completions=opts))
                    aa+=not bad;survive=not bad and all(o["completions"] for o in outer);outergood+=survive
                    rings.append(dict(A_tuple=ring,bad_AA_seams=bad,outer=outer,survives=survive))
                rows.append(dict(B_placement=bi,choices=choices,rings=rings))
            rec=dict(alias=alias,B_word=bw,B_raw_classes=raw,B_aliased_classes=bl,A_monohedral_matches=am,
                B_monohedral_matches=bm,counts=dict(AB=cnt,AA=aa,full=outergood),rows=rows)
            records.append(rec)
            if aa:print(alias,bw,rec["counts"],"Amono",bool(am),"Bmono",bool(bm),flush=True)
    out=dict(scope="Generic5stars; actual A001122 pairedsides; all5abc equalitypartitions*11Bnativebracelets*12Bplacements; complete AB rings and necessaryAA/outergates; H1H2 sufficient escapes checked using rainbowangleidentities",records=records,
        total_AB_rings=sum(r["counts"]["AB"] for r in records),
        uncovered_AA_records=[i for i,r in enumerate(records) if r["counts"]["AA"] and not r["A_monohedral_matches"] and not r["B_monohedral_matches"]],
        uncovered_full_records=[i for i,r in enumerate(records) if r["counts"]["full"] and not r["A_monohedral_matches"] and not r["B_monohedral_matches"]])
    Path("research/certificates/terra-001122-all-b-alias-rings.json").write_text(json.dumps(out,indent=2)+"\n")
    print("total",out["total_AB_rings"],"uncoveredAA",out["uncovered_AA_records"],"uncoveredfull",out["uncovered_full_records"])
if __name__=="__main__":main()
