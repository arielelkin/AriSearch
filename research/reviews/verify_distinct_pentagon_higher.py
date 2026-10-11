"""Independent full cyclic-domain, angle-span, and flat torus checker."""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as F
import json
root=Path(__file__).resolve().parents[2]
c=json.loads((root/'research/certificates/distinct_pentagon_higher_length_graph.json').read_text())
a=tuple(range(5))
assert c['A']==list(a)
assert [(t['n'],t['shared']) for t in c['records']]==[(7,4),(7,5),(8,4),(8,5),(9,5),(10,5)]
def normalize(w):
    candidates=[]
    for v in (list(w),list(reversed(w))):
        j=v.index(min(t for t in v if t<5));v=v[j:]+v[:j];names={};out=[]
        for t in v:
            if t>=5:
                if t not in names:names[t]=5+len(names)
                t=names[t]
            out.append(t)
        candidates.append(tuple(out))
    return min(candidates)
def graph(w):return {frozenset((w[i-1],w[i])) for i in range(len(w))}
def star_rows(a,b):
    slots={}
    for off,w in [(0,a),(len(a),b)]:
        for i in range(len(w)):slots.setdefault(frozenset((w[i-1],w[i])),[]).append(off+i)
    result=[]
    for t in combinations(sorted(set(a)|set(b)),3):
        es=[frozenset(e) for e in combinations(t,2)]
        if all(e in slots for e in es):
            result.extend(tuple(sorted(q)) for q in product(*(slots[e] for e in es)))
    return sorted(set(result))
def basis(rows):
    bb={}
    for raw in rows:
        q=list(map(F,raw))
        for i,v in sorted(bb.items()):
            if q[i]:
                z=q[i];q=[t-z*s for t,s in zip(q,v)]
        nz=next((i for i,z in enumerate(q) if z),None)
        if nz is not None:
            z=q[nz];bb[nz]=[t/z for t in q]
    return bb
def implied(bb,raw):
    q=list(map(F,raw))
    for i,v in sorted(bb.items()):
        z=q[i]
        if z:q=[t-z*s for t,s in zip(q,v)]
    return not any(q)
def equation(count,indices,rhs):
    out=[F(0)]*(count+1)
    for i in indices:out[i]+=1
    out[-1]=-F(rhs)
    return out
def audit_torus(b,keep):
    # Formal private renaming differs from generator; geometry still equal.
    shared=set(a)&set(b)
    b=tuple(t if t in keep or t not in shared else t+50 for t in b)
    common=[t for t in a if t in keep]
    bc=[t for t in b if t in keep];j=bc.index(common[0]);bc=bc[j:]+bc[:j]
    assert bc in (common,[common[0]]+list(reversed(common[1:])))
    bw=b[::-1] if bc==common else b
    words=[a,a,bw,bw]
    bits={t:i%2 for i,t in enumerate(common)}
    pairs=[]
    for t in set(a)-set(keep):pairs.append(((0,a.index(t)),(1,a.index(t))))
    for t in set(b)-set(keep):pairs.append(((2,words[2].index(t)),(3,words[3].index(t))))
    for t in keep:
        for bit in (0,1):pairs.append(((bit,a.index(t)),(2+(bit^bits[t]),words[2].index(t))))
    assert len(pairs)==12
    seen=set();parents={(f,i):(f,i) for f,w in enumerate(words) for i in range(len(w))}
    def find(t):
        while parents[t]!=t:t=parents[t]
        return t
    def union(u,v):parents[find(u)]=find(v)
    adjacency={f:set() for f in range(4)}
    for (f,i),(g,j) in pairs:
        assert (f,i) not in seen and (g,j) not in seen
        seen.update(((f,i),(g,j)));adjacency[f].add(g);adjacency[g].add(f)
        union((f,i),(g,(j+1)%len(words[g])))
        union((f,(i+1)%len(words[f])),(g,j))
    assert len(seen)==24
    classes={}
    for t in parents:classes.setdefault(find(t),[]).append(t)
    assert len(classes)==8 and all(len(q)==3 for q in classes.values())
    expected=star_rows(a,b)
    actual=[]
    # Corner indexing of reversed B must be matched by its actual length pair.
    def corner_id(f,i):
        w=words[f];e=frozenset((w[i-1],w[i]));source=a if f<2 else b
        j=next(j for j in range(len(source)) if frozenset((source[j-1],source[j]))==e)
        return j if f<2 else len(a)+j
    for group in classes.values():actual.append(tuple(sorted(corner_id(f,i) for f,i in group)))
    assert sorted(actual)==sorted(expected*2)
    reached={0}
    while True:
        r=reached|set().union(*(adjacency[t] for t in reached))
        if r==reached:break
        reached=r
    assert len(reached)==4
    return expected
full_domains=0;support_cases=0;gluings=0
for record in c['records']:
    n,k=record['n'],record['shared'];allwords=set()
    # Enumerate ALL placements of common/private symbols, allowing adjacent
    # private symbols; then apply graph triangle coverage directly.
    for shared in combinations(a,k):
        for tail in permutations(shared[1:]):
            common=(shared[0],)+tail
            for positions in combinations(range(1,n),k-1):
                loc=(0,)+positions;bypos=dict(zip(loc,common));nxt=5;w=[]
                for i in range(n):
                    if i in bypos:w.append(bypos[i])
                    else:w.append(nxt);nxt+=1
                allwords.add(normalize(w))
    full_domains+=len(allwords)
    survivors=[]
    for b in allwords:
        gg=graph(a)|graph(b);ts=[frozenset(t) for t in combinations(sorted(set(a)|set(b)),3)
            if all(frozenset(e) in gg for e in combinations(t,2))]
        if all(any(e<=t for t in ts) for e in gg):survivors.append(b)
    retained={tuple(t['B']):t for t in record['survivors']}
    assert set(survivors)==set(retained)
    assert len(retained)==record['survivor_count']==len(record['survivors'])
    # Verify stated isolated-private domain independently.
    isolated=[b for b in allwords if all(not(b[i]>=5 and b[(i+1)%n]>=5) for i in range(n))]
    assert len(isolated)==record['domain_count']
    for b,entry in retained.items():
        ss=star_rows(a,b);assert [list(t) for t in ss]==entry['corner_stars']
        gg=graph(a)|graph(b)
        tris=[list(t) for t in combinations(sorted(set(a)|set(b)),3)
              if all(frozenset(e) in gg for e in combinations(t,2))]
        assert tris==entry['triangles']
        rep=min(normalize([(sig*t+d)%5 if t<5 else t for t in b]) for sig in (-1,1) for d in range(5))
        assert list(rep)==entry['representative']
        count=5+n
        base=[equation(count,range(5),3),equation(count,range(5,count),n-2)]
        ringrows=[]
        if n==7:
            expected_keep=[]
            for keep in combinations(sorted(set(a)&set(b)),4):
                formal=tuple(t if t in keep or t not in a else t+50 for t in b)
                rings=star_rows(a,formal)
                if len(rings)==4 and sorted(t for s in rings for t in s)==list(range(count)):
                    expected_keep.append(keep);verified=audit_torus(b,keep);gluings+=1
                    ringrows.append([equation(count,row,2) for row in verified])
            assert expected_keep==[tuple(t['keep_common']) for t in entry['rings']]
            for r in entry['rings']:
                formal=tuple(t if t in r['keep_common'] or t not in a else t+20 for t in b)
                assert list(formal)==r['formal_B']
                assert [list(t) for t in star_rows(a,formal)]==r['corner_triples']
        for mask in range(1<<len(ss)):
            selected=[row for i,row in enumerate(ss) if mask>>i&1]
            if set(q for row in selected for q in row)!=set(range(count)):continue
            support_cases+=1;bb=basis(base+[equation(count,row,2) for row in selected])
            if n==7:
                assert any(all(implied(bb,row) for row in rr) for rr in ringrows)
            elif n==8:
                # Every corner-covering angle support forces at least one A right angle.
                assert any(implied(bb,equation(count,[i],F(1,2))) for i in range(5))
            elif n==10:
                assert implied(bb,[F(0)]*count+[F(1)])
            else:assert False
print(json.dumps({"verdict":"PASS","full_normalized_word_domain":full_domains,
    "retained_survivors":sum(t['survivor_count'] for t in c['records']),
    "audited_four_face_torus_maps":gluings,"corner_covering_supports":support_cases},indent=2,sort_keys=True))
