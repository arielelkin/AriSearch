"""Independent stdlib adjacent-repeat audit, no producer imports.
Atlas encoding: connected even-degree three-edge multigraphs, including
loops and repeated actual corner indices. Arm microstates: all corner
orders and both native-arm choices; one simultaneous state supplies all
three far endpoint pairs. All decisions are exact finite combinatorics.
"""
import itertools as it,json,runpy
from functools import lru_cache
from collections import Counter,defaultdict
from pathlib import Path
D=runpy.run_path(str(Path(__file__).with_name('hexagon-six-five-independent-2026-10-15.py')))
A=D['A'];canon=D['canon'];torus=D['torus']
triples=list(it.combinations_with_replacement(range(12),3))

def atlas(B):
    es=[(w[i],w[(i+1)%6]) for w in (A,B) for i in range(6)]
    found=[]
    for st in triples:
        degree=Counter(x for c in st for x in es[c])
        if any(n%2 for n in degree.values()):continue
        # Euler's criterion: the three corner edges form one cyclic ray walk.
        reached={next(iter(degree))}
        for _ in range(3):
            for c in st:
                x,y=es[c]
                if x in reached or y in reached:reached.update((x,y))
        if reached==set(degree):found.append(st)
    return found

@lru_cache(None)
def states(B,st):
    words=(A,B);result=set()
    for ordered in set(it.permutations(st)):
        for choices in it.product([0,1],repeat=3):
            arms=[]
            for c,choice in zip(ordered,choices):
                f,i=divmod(c,6)
                slots=[i,(i+1)%6]
                if choice:slots.reverse()
                # Incoming and outgoing native slots with opposite corner.
                arms.append([(words[f][j],6*f+((j-1)%6 if i==j else j)) for j in slots])
            if any(arms[z][1][0]!=arms[(z+1)%3][0][0] for z in range(3)):continue
            result.add(tuple(sorted(tuple(sorted((arms[z][1][1],arms[(z+1)%3][0][1]))) for z in range(3))))
    assert result # Euler atlas and native-arm reconstruction must agree.
    return tuple(sorted(result))

def formal_rings(B):
    found=set()
    # Independently relabel each unmatched B occurrence, then use the
    # multigraph-Euler atlas rather than a numerical triangle routine.
    for keep in it.combinations(range(6),4):
        values=[B[j] for j in keep]
        if len(set(values))!=4 or not set(values)<=set(A):continue
        formal=tuple(B[j] if j in keep else 20+j for j in range(6))
        ss=atlas(formal)
        if len(ss)==4 and Counter(c for st in ss for c in st)==Counter(range(12)):
            found.add(tuple(ss))
    return found

def closed(S,B):
    multiplicities=[Counter(st) for st in S]
    for st in S:
        if not any(all(any(not(Counter(pair)-other) for other in multiplicities) for pair in state) for state in states(B,st)):
            return False
    return True

def prune(S,B):
    S=set(S)
    while True:
        new={
            st for st in S if any(all(any(not(Counter(pair)-Counter(other)) for other in S) for pair in state) for state in states(B,st))}
        if new==S:return sorted(S)
        S=new

def covers(S):return set(c for st in S for c in st)==set(range(12))

words=[];survivors=defaultdict(list)
for k in range(6):
    for common in it.combinations(range(6),k):
        values=common+tuple(range(6,11-k))
        for p,q,r,s,t in it.permutations(values):
            if q>=t:continue
            B=(p,p,q,r,s,t);words.append(B)
            if covers(atlas(B)):survivors[k].append(B)
assert len(words)==3780
assert {k:len(v) for k,v in survivors.items()}=={4:42,5:90}
records=json.loads(Path('research/certificates/hexagon-six-five-adjacent-gate-2026-10-15.json').read_text())['records']
orbits={canon(B) for group in survivors.values() for B in group}
assert len(orbits)==12 and orbits=={canon(tuple(r['B'])) for r in records}
assert len({canon(B) for B in survivors[4]})==4
assert len({canon(B) for B in survivors[5]})==8
count=0;supportcounts=[]
for record in records:
    B=tuple(record['B']);ss=atlas(B)
    assert ss==[tuple(st) for st in record['stars']]
    for st in ss:
        key=','.join(map(str,st))
        assert states(B,st)==tuple(tuple(tuple(pair) for pair in state) for state in record['arm_assignments'][key])
    maximal=prune(ss,B)
    assert maximal==[tuple(st) for st in record['maximal_endpoint_supported']]
    selected=[]
    rings=formal_rings(B)
    if covers(maximal):
        assert rings=={tuple(tuple(st) for st in ring) for ring in record.get('rings',[])}
    # Independent audit exhausts the ORIGINAL atlas, not just the pruned
    # subset, thereby testing that monotone pruning loses no closed cover.
    for bits in it.product([False,True],repeat=len(ss)):
        S=tuple(st for st,yes in zip(ss,bits) if yes)
        if covers(S) and closed(S,B):
            assert set(S)<=set(maximal)
            assert any(set(ring)<=set(S) for ring in rings)
            assert torus(B,S) is not None
            selected.append(S);count+=1
    expected={tuple(sorted(tuple(st) for st in S)) for S in record.get('endpoint_closed_supports',[])}
    assert set(selected)==expected
    supportcounts.append(len(selected))
assert count==11
print(json.dumps(dict(status='PASS adjacent',words=len(words),survivors={k:len(v) for k,v in survivors.items()},orbits=len(orbits),closed_supports=count,all_direct_tori=True,supportcounts=supportcounts),sort_keys=True))
