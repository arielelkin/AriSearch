#!/usr/bin/env python3
"""Independent hostile checker: no author-module imports; integers/Fraction only."""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
from fractions import Fraction
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'research/certificates/hexagon-five-noncommon-gate-2026-10-15.json').read_text())
T=json.loads((ROOT/'research/certificates/hexagon-five-noncommon-fourface-2026-10-15.json').read_text())

def normalized(p,s):
    w=list(p);w.insert(s,p[0]);return tuple(w)

def native_data(words):
    # Construct the two endpoint occurrences of EACH side directly.
    ends={};arms={}
    for f,w in enumerate(words):
        for i,col in enumerate(w):
            ends[6*f+i]=(6*f+(i-1)%6,6*f+i)
        for i in range(6):arms[6*f+i]={w[i]:6*f+i,w[(i+1)%6]:6*f+(i+1)%6}
    assert all(len(a)==2 for a in arms.values())
    full=set()
    for tri in combinations(range(12),3):
        # Three distinct two-element ray sets on exactly three rays.
        pairs=[set(arms[c]) for c in tri]
        if len(set.union(*pairs))==3 and all(pairs[i]!=pairs[j] for i,j in combinations(range(3),2)):
            full.add(tri)
    mixed={t for t in full if min(t)<6<=max(t)}
    need={};seams={}
    for tri in mixed:
        need[tri]=set();seams[tri]=set()
        for a,b in combinations(tri,2):
            ray,=set(arms[a])&set(arms[b]);u,v=arms[a][ray],arms[b][ray]
            x,=set(ends[u])-{a};y,=set(ends[v])-{b}
            need[tri].add(tuple(sorted((x,y))))
            seams[tri].add(tuple(sorted((u,v))))
    remain=set(mixed)
    while True:
        available={ab for t in remain for ab in combinations(t,2)}
        remove={t for t in remain if not need[t]<=available}
        if not remove:break
        remain-=remove
    edges=set.union(*(seams[t] for t in remain)) if remain else set()
    unseen=set(range(12));components=[]
    while unseen:
        todo=[min(unseen)];comp=set(todo)
        for x in todo:
            for ab in edges:
                if x in ab:
                    for y in ab:
                        if y not in comp:comp.add(y);todo.append(y)
        unseen-=comp;components.append(tuple(sorted(comp)))
    components.sort()
    covered={c for t in remain for c in t}
    return full,mixed,remain,need,edges,components,covered

def closed_subsets(stars,need):
    seq=sorted(stars);out=[]
    for bits in product((False,True),repeat=len(seq)):
        chosen=tuple(t for t,b in zip(seq,bits) if b)
        if set(c for t in chosen for c in t)!=set(range(12)):continue
        p={ab for t in chosen for ab in combinations(t,2)}
        if all(need[t]<=p for t in chosen):out.append(chosen)
    return set(out)

def triples(v):return {tuple(t) for t in v}

def component_key(v):return sorted(tuple(c) for c in v)

summ=defaultdict(Counter);hard={};raw=0
for sa,sb in product((2,3),repeat=2):
    A=normalized(range(5),sa)
    for k in range(5):
        for shared in combinations(range(5),k):
            palette=shared+tuple(range(5,10-k))
            for perm in permutations(palette):
                B=normalized(perm,sb);raw+=1
                full,mixed,remain,need,edges,components,covered=native_data((A,B))
                joined=all(any({o,o+s}<=set(c) for c in components) for o,s in ((0,sa),(6,sb)))
                status='no_cover' if len(covered)<12 else ('hard' if joined else 'six_color_escape')
                summ[f'A{sa}_B{sb}_shared{k}'][status]+=1
                if status=='hard':hard[A,B]=(full,mixed,remain,need,edges,components)
assert raw==14880 and len(hard)==20
assert {k:dict(v) for k,v in summ.items()}==D['summary']
assert {(tuple(r['A']),tuple(r['B'])) for r in D['hard_records']}==set(hard)
rawsupports=0;classes=Counter()
for r in D['hard_records']:
    A,B=tuple(r['A']),tuple(r['B']);full,mixed,remain,need,edges,components=hard[A,B]
    assert full==triples(r['full_atlas']) and mixed==triples(r['mixed_atlas'])
    assert remain==triples(r['fixed_atlas']) and edges=={tuple(e) for e in r['seams']}
    assert components==component_key(r['components'])
    ss=closed_subsets(remain,need);rawsupports+=len(ss)
    assert ss=={tuple(sorted(triples(s))) for s in r['supports']}
    w=r['class_equivalence'];mp={int(a):b for a,b in w['color_map'].items()}
    assert len(mp)==len(set(mp.values()))==len(set(A)|set(B))
    for word,target,shift,direction in ((A,A,w['A_shift'],w['A_direction']),(B,tuple(r['canonical_B']),w['B_shift'],w['B_direction'])):
        assert tuple(mp[word[(shift+direction*i)%6]] for i in range(6))==target
        # Independently verify induced corner reading preserves both incident slots.
        for i in range(6):
            c=(shift+i)%6 if direction==1 else (shift-i-1)%6
            assert {mp[word[c]],mp[word[(c+1)%6]]}=={target[i],target[(i+1)%6]}
    classes[A,tuple(r['canonical_B'])]+=1
assert rawsupports==64 and len(classes)==6
repsupports=0;deterministic=0
for r in D['hard_classes']:
    A,B=tuple(r['A']),tuple(r['B']);full,mixed,remain,need,edges,components=hard[A,B]
    assert classes[A,B]==r['raw_word_count']
    ss=closed_subsets(remain,need);repsupports+=len(ss)
    assert ss=={tuple(sorted(triples(s))) for s in r['supports']}
    if A[0]==A[3]:
        assert len(ss)==1
        support=next(iter(ss));assert Counter(c for t in support for c in t)==Counter(range(12))
        pairs={p for t in support for p in combinations(t,2)}
        words=(A,B)
        for f,i in product(range(2),range(6)):
            matches=[]
            for g,j,reverse in product(range(2),range(6),(False,True)):
                if words[f][i]!=words[g][j]:continue
                host=(6*f+(i-1)%6,6*f+i);guest=(6*g+(j-1)%6,6*g+j)
                if reverse:guest=guest[::-1]
                if all(tuple(sorted((a,b))) in pairs for a,b in zip(host,guest)):
                    matches.append((g,j,reverse))
            assert len(matches)==1,(A,B,f,i,matches)
            deterministic+=1
assert repsupports==22 and deterministic==36

def positive_gluing(A,B,w):
    signs=w['signs'];pairs=w['edge_pairs'];assert len(signs)==4 and signs[0]==1
    assert sorted(x for ab in pairs for x in ab)==list(range(24))
    words=(A,A,B,B); graph={i:[] for i in range(24)};faces={f:set() for f in range(4)}
    def col(e):
        f,k=divmod(e,6);return words[f][k if signs[f]==1 else (-k-1)%6]
    for a,b in pairs:
        assert col(a)==col(b)
        f,i=divmod(a,6);g,j=divmod(b,6);faces[f].add(g);faces[g].add(f)
        for x,y in ((6*f+i,6*g+(j+1)%6),(6*f+(i+1)%6,6*g+j)):
            graph[x].append(y);graph[y].append(x)
    reach={0}
    while True:
        nxt=reach|set().union(*(faces[f] for f in reach))
        if nxt==reach:break
        reach=nxt
    assert len(reach)==4 and all(len(ns)==2 for ns in graph.values())
    unseen=set(range(24));stars=[]
    while unseen:
        seen={min(unseen)};todo=list(seen)
        for x in todo:
            for y in graph[x]:
                if y not in seen:seen.add(y);todo.append(y)
        assert len(seen)==3
        unseen-=seen;native=[]
        for x in seen:
            f,k=divmod(x,6);native.append(6*(f//2)+(signs[f]*k-1)%6)
        stars.append(tuple(sorted(native)))
    assert len(stars)==8 and sorted(stars)==[tuple(t) for t in w['vertex_triples']]
    assert set(stars)==triples(w['angle_support'])
    return set(stars)

def row(t):return tuple(Fraction(t.count(i)) for i in range(12))+(Fraction(2),)
identities=0;witnesses=0
for c in T['classes']:
    A=tuple(T['A']);B=tuple(c['B'])
    ss={tuple(sorted(triples(s))) for s in next(r for r in D['hard_classes'] if tuple(r['A'])==A and tuple(r['B'])==B)['supports']}
    assert {tuple(sorted(triples(s['source_support']))) for s in c['support_checks']}==ss
    for w in c['witnesses']:positive_gluing(A,B,w);witnesses+=1
    for s in c['support_checks']:
        rows=[tuple(Fraction(i<6) for i in range(12))+(Fraction(4),),tuple(Fraction(i>=6) for i in range(12))+(Fraction(4),)]+[row(t) for t in s['source_support']]
        z=s['positive_torus_implication'];w=c['witnesses'][z['torus_index']]
        assert len(z['row_combinations'])==len(w['angle_support'])
        for t,coeff in zip(w['angle_support'],z['row_combinations']):
            assert len(coeff)==len(rows)
            actual=tuple(sum(Fraction(x)*r[j] for x,r in zip(coeff,rows)) for j in range(13))
            assert actual==row(t);identities+=1
assert identities==40 and witnesses==5

def oriented_cycle_support(words,signs,pairing):
    # Walk the vertex permutation rather than unioning endpoint classes.
    def nxt(e):return 6*(e//6)+(e+1)%6
    unused=set(pairing);cycles=[]
    while unused:
        start=min(unused);cycle=[];x=start
        while x not in cycle:
            assert x in unused
            cycle.append(x);unused.remove(x);x=nxt(pairing[x])
        assert x==start
        cycles.append(cycle)
    return cycles

# Independently exhaust fixed positive-witness domains. Recursive involutions
# choose the greatest unused dart and only its equal-color partners.
for c in T['classes']:
    A=tuple(T['A']);B=tuple(c['B']);words=(A,A,B,B)
    count=Counter();supports=set()
    for tail in product((-1,1),repeat=3):
        signs=(1,)+tail
        colors={6*f+k:words[f][k if signs[f]==1 else (-k-1)%6] for f,k in product(range(4),range(6))}
        def involutions(unused,pairs):
            if not unused:
                yield pairs;return
            a=max(unused)
            for b in sorted(unused-{a}):
                if colors[a]==colors[b]:
                    yield from involutions(unused-{a,b},pairs+[(a,b)])
        for pairs in involutions(set(range(24)),[]):
            count['all_pairings']+=1
            adj={f:set() for f in range(4)}
            for a,b in pairs:adj[a//6].add(b//6);adj[b//6].add(a//6)
            reach={0};todo=[0]
            for f in todo:
                for g in adj[f]:
                    if g not in reach:reach.add(g);todo.append(g)
            if len(reach)!=4:continue
            count['connected']+=1
            pairing={a:b for a,b in pairs}|{b:a for a,b in pairs}
            cycles=oriented_cycle_support(words,signs,pairing)
            if len(cycles)!=8 or any(len(v)!=3 for v in cycles):continue
            count['trivalent_tori']+=1
            support=set()
            for v in cycles:
                native=[]
                for x in v:
                    f,k=divmod(x,6);native.append(6*(f//2)+(signs[f]*k-1)%6)
                support.add(tuple(sorted(native)))
            supports.add(tuple(sorted(support)))
    assert dict(count)==c['counts']
    assert supports=={tuple(sorted(triples(w['angle_support']))) for w in c['witnesses']}

# Pure opposite-repeat source stars: directly check the two-face escape.
w=(0,1,2,0,3,4);pairs=[(0,3),(6,9)]+[(i,6+i) for i in (1,2,4,5)]
assert sorted(x for ab in pairs for x in ab)==list(range(12))
assert all(w[a%6]==w[b%6] for a,b in pairs)
matching={a:b for a,b in pairs}|{b:a for a,b in pairs}
cycles=oriented_cycle_support((w,w),(1,1),matching)
assert len(cycles)==4 and all(len(v)==3 for v in cycles)
assert Counter(tuple(sorted((x-1)%6 for x in v)) for v in cycles)==Counter({(0,1,2):2,(3,4,5):2})
print('PASS: 14880 words, 20 residual maps, 22 representative/64 raw supports, 36 deterministic sides, all 30240 fixed-domain gluings, five positive tori, 40 exact augmented identities, pure-star torus')
