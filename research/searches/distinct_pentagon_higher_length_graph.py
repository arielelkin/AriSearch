"""Finite length-graph domains for all-obtuse, internally distinct (5,n) pairs.
Native side symbols within each polygon are distinct. Private symbols are
isolated in any triangle-covered graph; derive n<=10 from shared k<=5.
Enumerate every common cycle and every placement of isolated private symbols.
"""
from itertools import combinations,permutations,product
import json
A=tuple(range(5))
def edges(w): return {tuple(sorted((w[i],w[(i+1)%len(w)]))) for i in range(len(w))}
def canonical(w):
    candidates=[]
    for v in (w,w[::-1]):
        j=v.index(min(v)); candidates.append(v[j:]+v[:j])
    return min(candidates)
def bword(common,insert):
    w=[]; private=5
    for j,a in enumerate(common):
        w.append(a)
        if j in insert:
            w.append(private); private+=1
    # Private numerical labels have no identity relative to A; canonicalize them
    # independently after choosing each orientation/anchor.
    variants=[]
    for t in (w,w[::-1]):
        j=t.index(min(common)); t=t[j:]+t[:j]; names={}; nxt=5; out=[]
        for a in t:
            if a>=5:
                if a not in names: names[a]=nxt; nxt+=1
                a=names[a]
            out.append(a)
        variants.append(tuple(out))
    return min(variants)
def normal_private(w):
    out=[]
    for t in (list(w),list(w)[::-1]):
        j=t.index(min(q for q in t if q<5));t=t[j:]+t[:j];names={};nxt=5;v=[]
        for a in t:
            if a>=5:
                if a not in names:names[a]=nxt;nxt+=1
                a=names[a]
            v.append(a)
        out.append(tuple(v))
    return min(out)
def orbitrep(w):
    return min(normal_private([(sig*q+d)%5 if q<5 else q for q in w])
        for sig in (-1,1) for d in range(5))
def stars(a,b):
    occurrences={}
    for off,w in [(0,a),(len(a),b)]:
        for j in range(len(w)):
            e=tuple(sorted((w[j-1],w[j])))
            occurrences.setdefault(e,[]).append(off+j)
    graph=set(occurrences);vv=sorted(set(a)|set(b));out=[]
    for t in combinations(vv,3):
        ee=[tuple(sorted(e)) for e in combinations(t,2)]
        if all(e in graph for e in ee):
            out.extend(tuple(sorted(v)) for v in product(*(occurrences[e] for e in ee)))
    return sorted(set(out))
def rings(b):
    shared=sorted(set(A)&set(b));out=[]
    for keep in combinations(shared,4):
        bb=tuple(q if q in keep or q not in shared else q+20 for q in b)
        ss=stars(A,bb)
        if len(ss)==4 and sorted(t for row in ss for t in row)==list(range(5+len(b))):
            out.append({"keep_common":list(keep),"formal_B":list(bb),"corner_triples":[list(row) for row in ss]})
    return out
aedges=edges(A); record=[]
for n in range(7,11):
    for k in range(max(3,(n+1)//2),6):
        words=set()
        for shared in combinations(A,k):
            for tail in permutations(shared[1:]):
                common=(shared[0],)+tail
                for ins in combinations(range(k),n-k):
                    words.add(bword(common,ins))
        survivors=[]
        for b in sorted(words):
            graph=aedges|edges(b)
            vertices=sorted(set(A)|set(b))
            tris=[t for t in combinations(vertices,3) if all(tuple(sorted(e)) in graph for e in combinations(t,2))]
            if all(any(set(e)<=set(t) for t in tris) for e in graph):
                survivors.append({"B":list(b),"triangles":[list(t) for t in tris],"representative":list(orbitrep(b)),"corner_stars":[list(t) for t in stars(A,b)],"rings":rings(b) if n==7 else []})
        record.append({"n":n,"shared":k,"domain_count":len(words),"survivor_count":len(survivors),"survivors":survivors})
print(json.dumps({"A":list(A),"records":record,"scope":"triangle-covering necessary condition only"},indent=2,sort_keys=True))
