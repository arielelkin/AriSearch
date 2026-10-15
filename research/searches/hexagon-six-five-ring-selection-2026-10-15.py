"""Finite exact corner-support classification for eight six/five-length hexagon words.
Complete finite inputs to the written periodicity theorem; no geometric search.
"""
from itertools import combinations,product
import json
import argparse
from pathlib import Path
A=tuple(range(6))
REPS=[(0,2,0,3,6,4),(0,2,4,6,5,6),(0,2,0,3,5,6),
      (0,2,0,3,1,4),(0,1,4,2,5,2),(0,1,5,2,4,2),
      (0,1,0,2,5,3),(0,1,5,1,4,2)]
def edge(w,i):return tuple(sorted((w[i],w[(i+1)%6])))
def atlas(B):
    D={}
    for base,w in ((0,A),(6,B)):
        for i in range(6):D.setdefault(edge(w,i),[]).append(base+i)
    stars=[]
    for tr in combinations(sorted(set(A)|set(B)),3):
        es=[tuple(sorted(e)) for e in combinations(tr,2)]
        if all(e in D for e in es):stars.extend(tuple(sorted(st)) for st in product(*(D[e] for e in es)))
    return sorted(set(stars))
def rings(B):
    found=set()
    for slots in combinations(range(6),4):
        shared=[B[i] for i in slots]
        if len(set(shared))!=4 or not set(shared)<=set(A):continue
        formal=tuple(B[i] if i in slots else 100+i for i in range(6))
        D={}
        for base,w in ((0,A),(6,formal)):
            for i in range(6):D.setdefault(edge(w,i),[]).append(base+i)
        if len(D)!=12:continue
        tris=[];covered=set()
        for tr in combinations(sorted(set(A)|set(formal)),3):
            es=[tuple(sorted(e)) for e in combinations(tr,2)]
            if all(e in D for e in es):
                tris.append(tuple(sorted(D[e][0] for e in es)));covered.update(es)
        if len(tris)==4 and len(covered)==12:found.add(tuple(sorted(tris)))
    return sorted(found)
def far_corner(c,symbol,B):
    f,i=divmod(c,6);word=(A,B)[f]
    if word[i]==symbol:return f*6+(i-1)%6
    assert word[(i+1)%6]==symbol
    return f*6+(i+1)%6

def endpoint_closed(selected,B):
    words=(A,B)
    for st in selected:
        for c,d in combinations(st,2):
            f,i=divmod(c,6);g,j=divmod(d,6)
            shared=set((words[f][i],words[f][(i+1)%6]))&set((words[g][j],words[g][(j+1)%6]))
            assert len(shared)==1
            symbol,=shared
            a,b=far_corner(c,symbol,B),far_corner(d,symbol,B)
            if a==b or not any(a in other and b in other for other in selected):return False
    return True

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    records=[]
    for B in REPS:
        stars=atlas(B);models=rings(B);covers=0;exceptional=[];support_records=[]
        for mask in range(1<<len(stars)):
            selected=[st for j,st in enumerate(stars) if mask>>j&1]
            if set(i for st in selected for i in st)!=set(range(12)):continue
            covers+=1
            if not endpoint_closed(selected,B):continue
            direct=next((model for model in models if all(st in selected for st in model)),None)
            if direct is None:
                assert len(selected)==4
                assert all(sum(i in st for st in selected)==1 for i in range(12))
                exceptional.append(selected)
            support_records.append(dict(stars=selected,direct_ring=direct,
                                        mechanism='ring' if direct is not None else 'deterministic'))
        records.append(dict(B=B,stars=stars,rings=models,corner_covers=covers,
                            endpoint_supports=support_records,deterministic_exceptions=exceptional))
    assert [len(r['endpoint_supports']) for r in records]==[1,3,1,1,0,3,0,7]
    assert [len(r['deterministic_exceptions']) for r in records]==[0,1,0,0,0,0,0,1]
    data=dict(domain='all actual-corner support subsets for eight explicitly listed six/five-length words',
              equivalence='corner index is the corner after side i, A=0..5, B=6..11',
              records=records)
    if args.output:Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,sort_keys=True))

if __name__=="__main__":main()
