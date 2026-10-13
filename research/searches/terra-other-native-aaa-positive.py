#!/usr/bin/env python3
from itertools import permutations,product
from collections import Counter
from sage.all import CyclotomicField,QQbar,AA
import json
from pathlib import Path
K=CyclotomicField(360);z=K.gen();emb=K.hom([QQbar.zeta(360)],QQbar)
angles=(113,121,126)
def canonical(w):return min(v[k:]+v[:k] for v in (w,w[::-1]) for k in range(6))
def eqpart(cs,sg):
    p=list(range(6))
    def f(i):
        while p[i]!=i:i=p[i]
        return i
    r=[((i-1)%6,i)[::s] for i,s in zip(cs,sg)]
    for k in range(3):p[f(r[k][1])]=f(r[(k+1)%3][0])
    seen={};return tuple(seen.setdefault(f(i),len(seen)) for i in range(6))

def main():
    words=sorted({canonical(w) for w in permutations((0,0,1,1,2,2))}-{(0,1,2,0,1,2)})
    assert len(words)==10
    records=[];witnesses=[];counts=Counter()
    for w in words:
        print("native", w, flush=True)
        dirs=[0]
        for i in range(1,6):dirs.append(dirs[-1]+180-angles[w[i]])
        choices=[tuple(i for i,c in enumerate(w) if c==j) for j in range(3)]
        for cs in product(*choices):
            for sg in product((1,-1),repeat=3):
                p=eqpart(cs,sg);r=max(p)+1;counts["cycles"]+=1
                rec=dict(word=w,corners=cs,reversals=sg,partition=p,classes=r)
                if r!=3:
                    rec["status"]="outside rank-three closure query";records.append(rec);continue
                counts["rank_three_cycles"]+=1
                sums=[sum((z**dirs[i] for i in range(6) if p[i]==j),K(0)) for j in range(3)]
                cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(2*z**90)
                v=[cross(sums[1],sums[2]),cross(sums[2],sums[0]),cross(sums[0],sums[1])]
                val=lambda x:AA(emb(x).real())
                if not any(x!=0 for x in v):
                    rec["status"]="degenerate closure rank; outside one-dimensional query";records.append(rec);counts["degenerate_rank_cycles"]+=1;continue
                if all(val(x)<0 for x in v):v=[-x for x in v]
                if not all(val(x)>0 for x in v):
                    rec["status"]="no strictly positive closure";records.append(rec);continue
                v=[x/v[0] for x in v];ls=[v[p[i]] for i in range(6)]
                vs=[K(0)]
                for l,d in zip(ls,dirs):vs.append(vs[-1]+l*z**d)
                assert vs[-1]==0
                support=[cross(vs[i+1]-vs[i],vs[j]-vs[i]) for i in range(6) for j in range(6) if j not in (i,(i+1)%6)]
                assert all(val(s)>0 for s in support)
                central=all(ls[i]==ls[i+3] for i in range(3))
                rec.update(status="positive closed strictly convex",central=central,
                    directions=dirs,class_lengths_approx=[str(val(x)) for x in v],
                    grouped_direction_exponents=[[dirs[i] for i in range(6) if p[i]==j] for j in range(3)],
                    exact_length_definition="Si=sum z^d over grouped exponents; v=(cross(S1,S2),cross(S2,S0),cross(S0,S1)); normalize v/v0; z=exp(2pi i/360)")
                counts["positive_cycles"]+=1;counts["central_cycles"]+=central
                records.append(rec)
                if not central and not any(q["word"]==w for q in witnesses):witnesses.append(rec)
    out=dict(scope="10 remaining native A words times64 AAA cases; exact closure queried only for three equality classes; fixture angles113,121,126",counts=dict(counts),first_noncentral_by_word=witnesses,records=records)
    Path("research/certificates/terra-other-native-aaa-positive.json").write_text(json.dumps(out,indent=2)+"\n")
    print(dict(counts))
    for r in witnesses:print(r["word"],r["partition"],r["class_lengths_approx"],r["corners"],r["reversals"])
if __name__=="__main__":main()
