"""Independent finite verification of the stated infinite orbit, not a search."""
from pathlib import Path
import json
from sage.all import QuadraticField, vector, floor

K=QuadraticField(3,'r'); r=K.gen()
base=Path(__file__).resolve().parents[1]/'certificates'
load=lambda name:json.loads((base/name).read_text())
source=load('hexagon-five-four-39-omissions-2026-10-19.json')
coronas=load('hexagon-five-four-five-residual-coronas-2026-10-19.json')
claim=load('hexagon-five-four-corona-translation-2026-10-19.json')
key=lambda p:tuple(sorted(tuple(x) for x in p))
def separate(p,q):
    for poly in (p,q):
        for a,b in zip(poly,poly[1:]+poly[:1]):
            e=b-a; normal=vector(K,[-e[1],e[0]])
            u=[normal.dot_product(x) for x in p]
            w=[normal.dot_product(x) for x in q]
            if max(u)<=min(w) or max(w)<=min(u): return True
    return False
for record,reported in zip(coronas['rows'],claim['rows']):
    idx=record['row_index']; assert idx==reported['row_index']
    A=[vector(K,[K(a)+K(b)*r for a,b in x]) for x in source['rows'][idx]['vertices'][0]]
    patch=[[vector(K,[K(x) for x in p]) for p in poly] for poly in record['results'][6]['patch']]
    h3=A[3]+A[4]; h5=A[5]+A[0]; v=h3-h5; norm=v.dot_product(v)
    assert norm>0 and list(map(str,v))==reported['translation']
    assert key([h3-x for x in A]) in list(map(key,patch))
    assert key([h5-x for x in A]) in list(map(key,patch))
    dots=[v.dot_product(x) for p in patch for x in p]
    width=max(dots)-min(dots)
    assert 2*norm<width<=3*norm
    same=[]
    for n in range(3):
        for i,p in enumerate(patch):
            for j,q in enumerate(patch):
                moved=[x+n*v for x in q]
                if key(p)==key(moved):
                    if n:same.append([n,i,j])
                else:assert separate(p,moved),(idx,n,i,j)
    assert same==reported['identifications']
    def canonical(p):
        n=floor(min(v.dot_product(x) for x in p)/norm)
        return key([x-n*v for x in p])
    orbits={}
    for i,p in enumerate(patch):orbits.setdefault(canonical(p),[]).append(i)
    assert len(orbits)==reported['fundamental_tiles']==6
    # Exact whole-side matching in the quotient, independent of stored incidences.
    edges={}
    for indices in orbits.values():
        p=patch[indices[0]]
        for a,b in zip(p,p[1:]+p[:1]):edges.setdefault(canonical([a,b]),0); edges[canonical([a,b])]+=1
    assert set(edges.values())=={1,2}
    boundary={e for e,count in edges.items() if count==1}
    expected={key([vector(K,[K(x) for x in p]) for p in e['endpoints']]) for e in reported['boundary']}
    assert boundary==expected and len(boundary)==8
    # Connectivity of each corona by complete shared edges.
    reached={0}
    while True:
        new={j for i in reached for j,q in enumerate(patch) if any(
            {tuple(a),tuple(b)}=={tuple(c),tuple(d)}
            for a,b in zip(patch[i],patch[i][1:]+patch[i][:1])
            for c,d in zip(q,q[1:]+q[:1]))}
        if new<=reached:break
        reached|=new
    assert len(reached)==10
    assert any(n==1 for n,i,j in same) # Consecutive connected coronas meet.
    print('PASS',idx,'tile orbit indices',list(orbits.values()),'eight exposed side orbits')
