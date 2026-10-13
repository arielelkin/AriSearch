#!/usr/bin/env python3
"""No producer imports: exhaustive native profile and finite relation verification."""
import json
from pathlib import Path
from itertools import product,permutations
from collections import Counter
root=Path(__file__).resolve().parents[2]
D=json.loads((root/"research/certificates/terra-001122-all-metric-native-rings.json").read_text())
F=json.loads((root/"research/certificates/terra-001122-residual-functional-actions.json").read_text())
AC=(0,0,1,1,2,2);PS=list(product(range(6),(1,-1)))
def profile(c,l,r,s):
    corners=[c[(r+s*k)%6] for k in range(6)]
    sides=[l[(r+k)%6] if s==1 else l[(r-k-1)%6] for k in range(6)]
    return corners,sides

def partitions():
    out=[()]
    for _ in range(6):out=[w+(j,) for w in out for j in range(max(w,default=-1)+2)]
    return out

def mono(c,l):
    hits=[]
    for r,s in PS:
        x,e=profile(c,l,r,s)
        if len(set(x[:3]))==3 and e[2]==e[5]:hits.append(["H1",r,s])
        if len({x[0],x[1],x[3]})==3 and e[1]==e[3] and e[2]==e[5]:hits.append(["H2",r,s])
    return hits

def main():
    canonical=lambda t:min(tuple(t[(h+s*i)%6] for i in range(6)) for h in range(6) for s in(-1,1))
    words=sorted({canonical(w) for w in permutations(AC)});assert len(words)==11
    assert [tuple(b["word"]) for b in D["B_words"]]==words
    A=[profile(AC,tuple(range(6)),r,s) for r,s in PS]
    for a,(cs,ls) in zip(D["A_placements"],A):assert a["corners"]==cs and a["sides"]==ls
    endpoint={tuple(sorted((AC[i],AC[(i+1)%6]))):i for i in range(6)}
    expected=[]
    for wi,(bw,b) in enumerate(zip(words,D["B_words"])):
        side=[endpoint[tuple(sorted((bw[i],bw[(i+1)%6])))] for i in range(6)];assert side==b["sides"]
        for bi,(r,s) in enumerate(PS):
            cs,ls=profile(bw,side,r,s);assert b["placements"][bi]["corners"]==cs and b["placements"][bi]["sides"]==ls
            possible=[[i for i,(c,l) in enumerate(A) if c[(k+2)%6]==cs[k] and c[(k+3)%6]==cs[(k-1)%6]] for k in range(6)]
            expected.extend((wi,bi,tuple(t)) for t in product(*possible))
    actual=[(r["B_word_index"],r["B_placement"],tuple(r["A_tuple"])) for r in D["raw_rings"]]
    assert actual==expected and len(expected)==360
    for r in D["raw_rings"]:
        bw=words[r["B_word_index"]];bl=D["B_words"][r["B_word_index"]]["sides"]
        b=D["B_words"][r["B_word_index"]]["placements"][r["B_placement"]]
        for k in range(6):
            c,l=A[r["A_tuple"][k]];d,m=A[r["A_tuple"][(k+1)%6]]
            assert l[(k+2)%6]==b["sides"][(k-1)%6]
            assert r["AA_equalities"][k]==[l[(k+1)%6],m[(k+4)%6]]
            colours=[c[(k+1)%6],d[(k+5)%6]];arms=[l[k],m[(k+5)%6]];o=r["outer"][k]
            sp="B" if colours[0]==colours[1] else "A";colour=colours[0] if sp=="B" else 3-sum(colours)
            cw,sw=(bw,bl) if sp=="B" else (AC,tuple(range(6)))
            offers=[dict(slot=i,sign=s,arms=list((sw[(i-1)%6],sw[i])[::s])) for i in range(6) for s in(1,-1) if cw[i]==colour]
            assert o==dict(colours=colours,arms=arms,species=sp,colour=colour,offers=offers)
    pairs=[(p,wi) for p in partitions() for wi in range(11)]
    assert len(pairs)==2233 and [(tuple(r["A_partition"]),r["B_word_index"]) for r in D["records"]]==pairs
    residual=[]
    for rec,(p,wi) in zip(D["records"],pairs):
        aa=[];full=[]
        for i,r in enumerate(D["raw_rings"]):
            if r["B_word_index"]!=wi or any(p[x]!=p[y] for x,y in r["AA_equalities"]):continue
            aa.append(i)
            if all(any([p[x] for x in o["arms"]]==[p[x] for x in f["arms"]] for f in o["offers"]) for o in r["outer"]):full.append(i)
        am=mono(AC,p);bm=mono(words[wi],[p[x] for x in D["B_words"][wi]["sides"]])
        assert (aa,full,am,bm)==(rec["AA_ring_ids"],rec["full_ring_ids"],rec["A_monohedral_matches"],rec["B_monohedral_matches"])
        if full and not am and not bm:residual.append(wi)
    assert len(residual)==369 and set(residual)=={5,9,10}
    for row in F["records"]:
        wi=row["B_word_index"];raw=[r for r in D["raw_rings"] if r["B_word_index"]==wi]
        ts=sorted({tuple(r["A_tuple"]) for r in raw});assert [list(t) for t in ts]==row["A_tuples"] and len(ts)==6
        assert all(all(x==y for x,y in r["AA_equalities"]) and all(o["species"]=="B" for o in r["outer"]) for r in raw)
        fibres=[[i for i,r in enumerate(raw) if tuple(r["A_tuple"])==t] for t in ts];assert fibres==row["raw_state_fibres"] and all(len(f)==2 for f in fibres)
        maps=[]
        for k in range(6):
            successors=[[j for j,v in enumerate(ts) if t[k]==v[(k+4)%6] and t[(k+1)%6]==v[(k+3)%6]] for t in ts]
            assert all(len(x)==1 for x in successors);maps.append([x[0] for x in successors])
        assert maps==row["successor_maps"]
        assert all(maps[k+3]==maps[k] for k in range(3))
        assert all(maps[k][maps[k][i]]==i for k in range(6) for i in range(6))
        assert all(maps[0][maps[1][i]]==maps[1][maps[0][i]]==maps[2][i] for i in range(6))
    assert {tuple(r["B_word"]) for r in F["records"]}=={words[wi] for wi in residual}
    print("PASS all203A partitions,360rawrings,73080 projections;369nonmonohedralresiduals in3words; allouterAAB and sixstatefunctional finiteactions")
if __name__=="__main__":main()
