"""Independent stdlib exact finite audit; no producer imports.
Domain: 3,780 normalized length-role words; all 3-corner indexed stars;
all star subsets; all equal-length side perfect matchings of four faces
in two uniform B chirality choices. No metric tiling search is performed.
"""
import itertools as it
import json
from collections import Counter,defaultdict
from pathlib import Path
A=tuple(range(6))

def edges(word): return [frozenset((word[i],word[(i+1)%6])) for i in range(6)]
def stars(B):
    es=edges(A)+edges(B)
    out=[]
    for triple in it.combinations(range(12),3):
        pairs=[es[c] for c in triple]
        symbols=set().union(*pairs)
        if len(symbols)==3 and len(set(pairs))==3 and all(len(e)==2 for e in pairs): out.append(triple)
    return out

def covered(B):
    return set(c for st in stars(B) for c in st)==set(range(12))

def canon(B):
    variants=[]
    for sign in [-1,1]:
        for shift in range(6):
            relabeled=[(sign*x+shift)%6 if x<6 else x for x in B]
            for orient in [relabeled,relabeled[::-1]]:
                for rotate in range(6):
                    w=orient[rotate:]+orient[:rotate]
                    private={}
                    out=[]
                    for x in w:
                        if x>=6:
                            if x not in private: private[x]=6+len(private)
                            x=private[x]
                        out.append(x)
                    variants.append(tuple(out))
    return min(variants)

words=[];survivors=defaultdict(list)
for k in range(6):
    for shared in it.combinations(range(6),k):
        labels=shared+tuple(range(6,11-k))
        assert len(labels)==5
        for p,q,r,s,t in it.permutations(labels):
            if r>=t: continue
            B=(p,q,p,r,s,t)
            words.append(B)
            if covered(B): survivors[k].append(B)
assert len(words)==3780
assert {k:len(v) for k,v in survivors.items()}=={4:30,5:60}
orbits={canon(B) for values in survivors.values() for B in values}
assert len(orbits)==8

certificate=json.loads(Path('research/certificates/hexagon-six-five-ring-support-2026-10-15.json').read_text())
records=certificate['records']
assert {canon(tuple(r['B'])) for r in records}==orbits
assert len({canon(B) for B in survivors[4]})==3
assert len({canon(B) for B in survivors[5]})==5

def far(c,length,B):
    words=(A,B)
    f,i=divmod(c,6)
    # Enumerate both side slots incident to this actual corner.
    candidates=[j for j in (i,(i+1)%6) if words[f][j]==length]
    assert len(candidates)==1
    j=candidates[0]
    return 6*f+((j-1)%6 if i==j else j)

def closes(S,B):
    es=edges(A)+edges(B)
    for st in S:
        for c,d in it.combinations(st,2):
            shared=es[c]&es[d]
            assert len(shared)==1
            x=next(iter(shared))
            a,b=far(c,x,B),far(d,x,B)
            if a==b or not any(a in other and b in other for other in S): return False
    return True

def matchings(xs):
    if not xs:
        yield []
    else:
        a=xs[0]
        for j in range(1,len(xs)):
            for rest in matchings(xs[1:j]+xs[j+1:]): yield [(a,xs[j])]+rest

def torus(B,S):
    # This is a different witness search from formal symbol splitting:
    # pair actual numerical-length slots, including every ambiguity.
    bylength=defaultdict(list)
    for f,w in enumerate([A,A,B,B]):
        for j,x in enumerate(w): bylength[x].append((f,j))
    classes=[list(matchings(xs)) for xs in bylength.values()]
    for bchirality in [-1,1]:
        for chosen in it.product(*classes):
            pairs=sum(chosen,[])
            parent=list(range(24))
            def find(x):
                while parent[x]!=x:
                    parent[x]=parent[parent[x]];x=parent[x]
                return x
            def join(a,b): parent[find(a)]=find(b)
            adj=[set() for _ in range(4)]
            for (f,j),(g,k) in pairs:
                # Actual corner i is between side slots i and i+1.
                u,v=(j-1)%6,j
                w,z=(k-1)%6,k
                if f>=2 and bchirality<0: u,v=v,u
                if g>=2 and bchirality<0: w,z=z,w
                join(6*f+u,6*g+z);join(6*f+v,6*g+w)
                adj[f].add(g);adj[g].add(f)
            groups=defaultdict(list)
            for f in range(4):
                for c in range(6): groups[find(6*f+c)].append((0 if f<2 else 6)+c)
            if len(groups)!=8 or any(len(v)!=3 for v in groups.values()):continue
            if not all(tuple(sorted(v)) in S for v in groups.values()):continue
            reached={0}
            for _ in range(4):reached|=set.union(*(adj[f] for f in reached))
            if len(reached)!=4:continue
            assert 8-12+4==0
            return pairs
    return None

def deterministic(S,B):
    if Counter(c for st in S for c in st)!=Counter(range(12)):return False
    es=edges(A)+edges(B)
    for c in range(12):
        st=next(st for st in S if c in st)
        for x in es[c]:
            candidates=[d for d in st if d!=c and x in es[d]]
            assert len(candidates)==1
            d=candidates[0]
            a,b=far(c,x,B),far(d,x,B)
            farstar=next(st for st in S if a in st)
            # Both actual endpoints agree with the same native neighbor side.
            assert b in farstar
            assert next(d2 for d2 in farstar if d2!=a and x in es[d2])==b
    return True

count=ringcount=detcount=0
for r in records:
    B=tuple(r['B']);ss=stars(B)
    assert ss==[tuple(st) for st in r['stars']]
    endpoint=[]
    for bits in it.product([False,True],repeat=len(ss)):
        S=tuple(st for st,yes in zip(ss,bits) if yes)
        if set(c for st in S for c in st)!=set(range(12)):continue
        if closes(S,B):endpoint.append(S)
    assert len(endpoint)==len(r['endpoint_supports'])
    retained={tuple(sorted(tuple(st) for st in v['stars'])) for v in r['endpoint_supports']}
    assert set(endpoint)==retained
    for S in endpoint:
        count+=1
        witness=torus(B,S)
        if witness is not None:ringcount+=1
        else:
            assert deterministic(S,B)
            detcount+=1
assert count==16
print(json.dumps(dict(status='PASS',words=len(words),survivors={k:len(v) for k,v in survivors.items()},orbits=len(orbits),endpoint_supports=count,direct_fourface_tori=ringcount,deterministic_residuals=detcount),sort_keys=True))
