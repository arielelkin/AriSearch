#!/usr/bin/env python3
"""Five-length hexagons, repetition at cyclic side-slot separation two.
Exact domain: k=0..3 shared values; 60*sum(binomial(5,k))=1560 words.
"""
import json
from itertools import combinations, permutations
from collections import Counter
A=(0,1,0,2,3,4)

def edges(w):
    return {frozenset((w[i],w[(i+1)%6])) for i in range(6)}

def run():
    counts=[]; survivors=[]
    for k in range(4):
        count=0;keep=0
        for shared in combinations(range(5),k):
            vals=shared+tuple(range(5,10-k))
            for repeated in vals:
                for leaf in vals:
                    if repeated==leaf:continue
                    other=tuple(x for x in vals if x not in (repeated,leaf))
                    for r,s,t in permutations(other):
                        if r>t:continue
                        B=(repeated,leaf,repeated,r,s,t)
                        count+=1
                        E=edges(A)|edges(B)
                        triangles=[tri for tri in combinations(sorted(set(A)|set(B)),3)
                                   if all(frozenset(e) in E for e in combinations(tri,2))]
                        if not all(any(e<=set(tri) for tri in triangles) for e in E):
                            continue
                        keep+=1
                        survivors.append({'k':k,'B':B,'triangles':triangles})
        counts.append({'k':k,'domain':count,'survivors':keep})
    assert [c['domain'] for c in counts]==[60,300,600,600]
    assert [c['survivors'] for c in counts]==[0,0,0,1]
    assert survivors[0]['B']==(0,3,0,5,1,6)
    print(json.dumps({'A':A,'counts':counts,'survivors':survivors},indent=2))

if __name__=='__main__':run()
