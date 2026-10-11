#!/usr/bin/env python3
"""Small independent checker of two focused four-face periodic witnesses."""
from pathlib import Path
import json
from collections import defaultdict,Counter
C=Path(__file__).resolve().parents[2]/'research/certificates/hexagon-five-length-private-repeat-tori.json'

def main():
    c=json.loads(C.read_text());A=c['A'];B=c['B']
    assert A==[0,1,0,2,3,4] and B==[5,3,5,2,1,4]
    assert {m['choice'] for m in c['models']}=={0,1}
    for model in c['models']:
        flags=model['reflected'];words=[w[::-1] if f else list(w) for w,f in zip([A,A,B,B],flags)]
        parent=list(range(24))
        def find(x):
            while parent[x]!=x:x=parent[x]
            return x
        def join(x,y):parent[find(x)]=find(y)
        used=[];edges=[]
        for (f,i),(g,j) in model['pairs']:
            assert (f,i)!=(g,j) and words[f][i]==words[g][j]
            used.extend([(f,i),(g,j)]);edges.append((f,g))
            join(6*f+(i-1)%6,6*g+j);join(6*f+i,6*g+(j-1)%6)
        assert sorted(used)==[(f,i) for f in range(4) for i in range(6)]
        vs=defaultdict(list)
        for x in range(24):vs[find(x)].append(x)
        assert len(vs)==8 and all(len(v)==3 for v in vs.values())
        triples=[]
        for v in vs.values():
            row=[]
            for x in v:
                f,i=divmod(x,6)
                row.append(('A' if f<2 else 'B',(4-i)%6 if flags[f] else i))
            triples.append(tuple(sorted(row)))
        x=model['choice']
        expected=[(('A',x),('A',2),('B',3)),(('A',1-x),('A',5),('B',4)),
                  (('A',3),('B',x),('B',2)),(('A',4),('B',1-x),('B',5))]
        assert Counter(triples)==Counter({tuple(sorted(t)):2 for t in expected})
        seen={0}
        while True:
            next_seen=seen|{g for f,g in edges if f in seen}|{f for f,g in edges if g in seen}
            if next_seen==seen:break
            seen=next_seen
        assert len(seen)==4 and len(vs)-len(model['pairs'])+4==0
    checks=0
    for x in (0,1):
        for y in (0,1):
            legal=[Counter(t) for t in [(('A',x),('A',2),('B',3)),
                (('A',1-x),('A',5),('B',4)),(('A',3),('B',y),('B',2)),
                (('A',4),('B',1-y),('B',5))]]
            words={'A':A,'B':B}
            for n,w in words.items():
                for i,value in enumerate(w):
                    candidates=[]
                    for m,z in words.items():
                        for j,v in enumerate(z):
                            if v!=value:continue
                            for reversed_endpoints in (False,True):
                                checks+=1
                                ends=[(j-1)%6,j]
                                if reversed_endpoints:ends.reverse()
                                pairs=[Counter([(n,(i-1)%6),(m,ends[0])]),
                                       Counter([(n,i),(m,ends[1])])]
                                if all(any(not (pair-star) for star in legal) for pair in pairs):
                                    candidates.append((m,j,reversed_endpoints))
                    assert len(candidates)==1,(x,y,n,i,candidates)
    assert checks==192
    print('PASS: both private-repeat four-face tori; eight specified corner triples; connected orientable chi=0; all192 endpoint candidates give unique neighbors for four generic supports.')

if __name__=='__main__':main()
