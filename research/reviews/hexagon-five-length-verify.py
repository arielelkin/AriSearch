#!/usr/bin/env python3
"""Independent replay of the <=3 shared values five-length result.
No import from its generator; full multiset-permutation enumeration, explicit
four-face endpoint gluing, and rational abstract-angle counterexample.
"""
from itertools import permutations, combinations
from collections import Counter,defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
A=(0,1,0,2,3,4)

def normal(word):
    return min(tuple(w[j:]+w[:j]) for w in [list(word),list(word)[::-1]] for j in range(6))

def corner_edges(word):
    return {tuple(sorted((word[j-1],word[j]))) for j in range(6)}

def valid(word):
    es=corner_edges(A)|corner_edges(word)
    ts=[t for t in combinations(sorted(set(A)|set(word)),3) if all(e in es for e in combinations(t,2))]
    return all(any(set(e)<=set(t) for t in ts) for e in es)

def check_torus(b, expected):
    a=(0,1,2,3,4,5); retained={0,1,2,4}
    ring=[0,1,2,4]
    common=[x for x in b if x in retained]
    cyclic=lambda x,y:any(x==y[j:]+y[:j] for j in range(4))
    original=b
    if cyclic(ring,common):b=tuple(reversed(b))
    assert cyclic(ring,list(reversed([x for x in b if x in retained])))
    words={'A':a,'B':b}
    corners={(n,i,j):(n,i,j) for n in ('A','B') for i in (0,1) for j in range(6)}
    def find(x):
        while corners[x]!=x:x=corners[x]
        return x
    def union(x,y):corners[find(x)]=find(y)
    pairings=[];used=set()
    def pair(n,i,j,m,k,l):
        x=(n,i,j);y=(m,k,l)
        assert x not in used and y not in used and x!=y
        assert words[n][j]==words[m][l]
        used.update([x,y]);pairings.append(((n,i),(m,k)))
        union((n,i,(j-1)%6),(m,k,l))
        union((n,i,j),(m,k,(l-1)%6))
    for n in ('A','B'):
        for j,x in enumerate(words[n]):
            if x not in retained:pair(n,0,j,n,1,j)
    for j,x in enumerate(ring):
        for i in (0,1):pair('A',i,a.index(x),'B',i^(j%2),b.index(x))
    assert len(used)==24 and len(pairings)==12
    vs=defaultdict(list)
    for c in corners:vs[find(c)].append(c)
    assert len(vs)==8 and all(len(v)==3 for v in vs.values())
    lookup={(n,frozenset((w[j],w[(j+1)%6]))):(n,j) for n,w in [('A',a),('B',original)] for j in range(6)}
    triples=[]
    for v in vs.values():
        triples.append(tuple(sorted(lookup[(n,frozenset((words[n][j],words[n][(j+1)%6])))] for n,i,j in v)))
    assert Counter(triples)==Counter({tuple(sorted(t)):2 for t in expected})
    reached={('A',0)}
    while True:
        new=reached|{y for x,y in pairings if x in reached}|{x for x,y in pairings if y in reached}
        if new==reached:break
        reached=new
    assert len(reached)==4 and len(vs)-len(pairings)+4==0

def main():
    cert=json.loads((ROOT/'research/certificates/hexagon-five-length-classification.json').read_text())
    assert tuple(cert['A'])==A
    raw=0;counts=[];survivors=[]
    for k in range(4):
        domain=set()
        for shared in combinations(range(5),k):
            vals=shared+tuple(range(5,10-k))
            for repeated in vals:
                for word in permutations(vals+(repeated,)):
                    raw+=1
                    at=[j for j,x in enumerate(word) if x==repeated]
                    if (at[1]-at[0]) not in (2,4):continue
                    domain.add(normal(word))
        good={w for w in domain if valid(w)}
        counts.append((k,len(domain),len(good)))
        survivors.extend((k,w) for w in good)
    assert counts==[(c['k'],c['domain'],c['survivors']) for c in cert['counts']]
    assert survivors==[(3,normal((0,3,0,5,1,6)))]
    assert raw==93600
    case1=[(('A',0),('B',2),('B',3)),(('A',1),('B',4),('B',5)),
           (('A',2),('A',3),('B',0)),(('A',4),('A',5),('B',1))]
    case2=[(('A',1),('B',2),('B',3)),(('A',0),('B',4),('B',5)),
           (('A',2),('A',3),('B',1)),(('A',4),('A',5),('B',0))]
    check_torus((2,4,0,6,1,7),case1)
    check_torus((0,4,2,6,1,7),case2)
    a=list(map(Q,['7/10','3/5','7/10','7/10','13/20','13/20']))
    b=list(map(Q,['7/10','3/5','13/20','13/20','7/10','7/10']))
    assert sum(a)==sum(b)==4 and all(Q(1,2)<x<1 for x in a+b)
    kinds=[[(('A',i),('B',2),('B',3)) for i in (0,1)],
           [(('A',i),('B',4),('B',5)) for i in (0,1)],
           [(('A',2),('A',3),('B',i)) for i in (0,1)],
           [(('A',4),('A',5),('B',i)) for i in (0,1)]]
    angle=lambda star:sum((a if n=='A' else b)[j] for n,j in star)
    legal={tuple(sorted(s)) for row in kinds for s in row if angle(s)==2}
    assert len(legal)==4
    assert Counter(c for s in legal for c in s)==Counter((n,i) for n in ('A','B') for i in range(6))
    assert not all(tuple(sorted(t)) in legal for t in case1)
    assert not all(tuple(sorted(t)) in legal for t in case2)
    assert a[4]+a[5]+b[1]==Q(19,10) # other end of forced A-slot0 / B-slot2 contact
    print('PASS: 93600 raw words / 1560 normalized words; unique k=3 survivor; '
          '2 four-face endpoint gluings; rational angle-only selection counterexample.')

if __name__=='__main__':main()
