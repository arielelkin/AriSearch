#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import product,permutations
root=Path(__file__).resolve().parents[2]
D=json.loads((root/"research/certificates/terra-010212-all-metric-native-rings.json").read_text())
C=(0,1,0,2,1,2);P=list(product(range(6),(1,-1)))
def profile(c,l,r,s):
    return [c[(r+s*k)%6] for k in range(6)],[l[(r+k)%6] if s==1 else l[(r-k-1)%6] for k in range(6)]
def mono(c,l):
    hits=[]
    for r,s in P:
        x,e=profile(c,l,r,s)
        if len(set(x[:3]))==3 and e[2]==e[5]:hits.append(["H1",r,s])
        if len({x[0],x[1],x[3]})==3 and e[1]==e[3] and e[2]==e[5]:hits.append(["H2",r,s])
    return hits

def main():
    can=lambda w:min(tuple(w[(r+s*k)%6] for k in range(6)) for r,s in P)
    allowed={(0,1),(1,2),(0,2)}
    words=sorted(w for w in {can(w) for w in permutations(C)} if all(tuple(sorted((w[k],w[(k+1)%6]))) in allowed for k in range(6)))
    assert [list(w) for w in words]==D["B_words"]
    A=[profile(C,list(range(6)),r,s) for r,s in P]
    for rec,(x,e) in zip(D["A_placements"],A):assert rec["corners"]==x and rec["sides"]==e
    expected=[]
    for wi,w in enumerate(words):
        for bi,(r,s) in enumerate(P):
            x,e=profile(w,list(range(6)),r,s)
            choices=[[i for i,(c,l) in enumerate(A) if c[(k+2)%6]==x[k] and c[(k+3)%6]==x[(k-1)%6]] for k in range(6)]
            expected.extend((wi,bi,tuple(t)) for t in product(*choices))
    raw=D["raw_rings"]
    assert len(raw)==3072 and [(r["B_word_index"],r["B_placement"],tuple(r["A_tuple"])) for r in raw]==expected
    for rec in raw:
        w=words[rec["B_word_index"]];br,bs=P[rec["B_placement"]];bc,be=profile(w,list(range(6)),br,bs);bl=[None]*6
        for k in range(6):bl[be[(k-1)%6]]=A[rec["A_tuple"][k]][1][(k+2)%6]
        assert bl==rec["B_native_A_side_sources"]
        for k in range(6):
            c,l=A[rec["A_tuple"][k]];d,m=A[rec["A_tuple"][(k+1)%6]]
            assert rec["AA_equalities"][k]==[l[(k+1)%6],m[(k+4)%6]]
            cs=[c[(k+1)%6],d[(k+5)%6]];arms=[l[k],m[(k+5)%6]];species="B" if cs[0]==cs[1] else"A";col=cs[0] if species=="B" else 3-sum(cs)
            cw,sw=(w,bl) if species=="B" else(C,list(range(6)))
            offers=[dict(slot=i,sign=s,arms=list((sw[(i-1)%6],sw[i])[::s])) for i in range(6) for s in(1,-1) if cw[i]==col]
            assert rec["outer"][k]==dict(colours=cs,arms=arms,species=species,colour=col,offers=offers)
    ps=[()]
    for _ in range(6):ps=[w+(j,) for w in ps for j in range(max(w,default=-1)+2)]
    assert len(ps)==203 and [tuple(r["A_partition"]) for r in D["records"]]==ps
    cases=set();idsbycase={}
    for p,row in zip(ps,D["records"]):
        aa=[];full=[];unc=[];am=mono(C,p);cache={}
        for i,rec in enumerate(raw):
            if any(p[x]!=p[y] for x,y in rec["AA_equalities"]):continue
            aa.append(i)
            if not all(any([p[x] for x in o["arms"]]==[p[x] for x in f["arms"]] for f in o["offers"]) for o in rec["outer"]):continue
            full.append(i);wi=rec["B_word_index"];b=tuple(p[x] for x in rec["B_native_A_side_sources"]);key=(wi,b)
            if key not in cache:cache[key]=mono(words[wi],b)
            if not am and not cache[key]:
                unc.append(i);case=(p,wi,b);cases.add(case);idsbycase.setdefault(case,[]).append(i)
        assert (aa,full,unc,am)==(row["AA_ring_ids"],row["full_ring_ids"],row["uncovered_full_ring_ids"],row["A_monohedral_matches"])
        assert [dict(B_word_index=k[0],B_actual_class_word=list(k[1]),matches=v) for k,v in sorted(cache.items())]==row["B_metric_monohedral_matches"]
    assert not cases and not D["uncovered_joint_metric_cases"]
    assert len(words)==4 and D["counts"]["raw_rings"]==3072
    assert D["counts"]["partitions"]==203 and D["counts"]["projections"]==623616
    assert sum(len(r["AA_ring_ids"]) for r in D["records"])==8976
    assert sum(len(r["full_ring_ids"]) for r in D["records"])==3360
    print("PASS all203A sidepartitions/3072native rings/623616projections;all3360outercompletecases giveAorB H1/H2 omission escape")
if __name__=="__main__":main()
