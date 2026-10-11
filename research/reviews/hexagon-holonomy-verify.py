#!/usr/bin/env python3
"""Independent integer/rational audit; does not import the search program.
Checks the complete side-word domain, proposed splittings, exact angle-support
selection, and all four-face torus endpoint gluings. Assertions must be enabled.
"""
import json
from pathlib import Path
from itertools import permutations, combinations, product
from fractions import Fraction
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'research/certificates/hexagon-holonomy-classification.json'
A = (0,1,2,3,4,5)

def normalize(w):
    options=[]
    for forward in (list(w), list(w)[::-1]):
        for _ in range(6):
            options.append(tuple(forward))
            forward.append(forward.pop(0))
    return min(options)

def edges(w):
    return {tuple(sorted((w[j-1],w[j]))) for j in range(6)}

def triangle_set(w):
    es=edges(A)|edges(w)
    ts=[]
    for a,b,c in combinations(sorted(set(A)|set(w)),3):
        if (a,b) in es and (a,c) in es and (b,c) in es:
            ts.append((a,b,c))
    return ts

def survives(w):
    ts=triangle_set(w)
    counts=Counter(e for t in ts for e in combinations(t,2))
    return all(counts[e]>0 for e in edges(A)|edges(w))

def corner_stars(w):
    locations=defaultdict(list)
    for name,word in [('A',A),('B',w)]:
        for i in range(6):
            locations[tuple(sorted((word[i],word[(i+1)%6])))].append((name,i))
    possible=set()
    for tri in triangle_set(w):
        for corners in product(*(locations[e] for e in combinations(tri,2))):
            assert len({c[0] for c in corners})==2
            possible.add(tuple(sorted(corners)))
    return sorted(possible)

def split_stars(w, retained):
    # Reconstruct the ring directly from formal private/common symbols.
    loc=defaultdict(list)
    formal={}
    for name,word in [('A',A),('B',w)]:
        formal[name]=tuple(('C',x) if x in retained else (name,x) for x in word)
        for i in range(6):
            edge=tuple(sorted((formal[name][i],formal[name][(i+1)%6])))
            loc[edge].append((name,i))
    if any(len(v)!=1 for v in loc.values()):
        return None
    triangles=[]
    for tri in combinations(sorted(set(formal['A'])|set(formal['B'])),3):
        es=list(combinations(tri,2))
        if all(e in loc for e in es):
            triangles.append(tuple(sorted(loc[e][0] for e in es)))
    if Counter(c for t in triangles for c in t)!=Counter((n,i) for n in ('A','B') for i in range(6)):
        return None
    assert len(triangles)==4
    return sorted(triangles)

def torus(w, retained, expected):
    # Actual edge endpoint union-find; not a graph triangle-count substitute.
    ar=[x for x in A if x in retained]
    bw=list(w)
    br=[x for x in bw if x in retained]
    def cyclic_equal(x,y):
        return any(x==y[j:]+y[:j] for j in range(4))
    if cyclic_equal(ar,br):
        bw.reverse()
        br=[x for x in bw if x in retained]
    assert cyclic_equal(ar,list(reversed(br)))
    words={'A':A,'B':tuple(bw)}
    parity={x:j%2 for j,x in enumerate(ar)}
    faces=[(n,i) for n in ('A','B') for i in (0,1)]
    all_corners=[(n,i,j) for n,i in faces for j in range(6)]
    parent={x:x for x in all_corners}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def join(x,y):
        parent[find(x)]=find(y)
    paired={}
    face_edges=[]
    def pair(f,j,g,k):
        sj=f+(j,);sk=g+(k,)
        assert sj!=sk and sj not in paired and sk not in paired
        assert words[f[0]][j]==words[g[0]][k]
        paired[sj]=sk;paired[sk]=sj
        # Side j goes from corner j-1 to corner j. Reverse its endpoints.
        join(f+((j-1)%6,), g+(k,))
        join(f+(j,),g+((k-1)%6,))
        face_edges.append((f,g))
    for n in ('A','B'):
        for j,x in enumerate(words[n]):
            if x not in retained:
                pair((n,0),j,(n,1),j)
    for x in retained:
        for i in (0,1):
            pair(('A',i),words['A'].index(x),('B',i^parity[x]),words['B'].index(x))
    assert len(paired)==24 and len(face_edges)==12
    reachable={faces[0]}
    while True:
        bigger=reachable|{g for f,g in face_edges if f in reachable}|{f for f,g in face_edges if g in reachable}
        if bigger==reachable:break
        reachable=bigger
    assert reachable==set(faces)
    vertices=defaultdict(list)
    for corner in all_corners:
        vertices[find(corner)].append(corner)
    assert len(vertices)==8 and all(len(v)==3 for v in vertices.values())
    source_lookup={}
    for n,word in [('A',A),('B',w)]:
        for j in range(6):
            source_lookup[(n,frozenset((word[j],word[(j+1)%6])))]=(n,j)
    actual=[]
    for corners in vertices.values():
        row=[]
        for n,i,j in corners:
            # Corner j in the gluing is between side j and side j+1.
            word=words[n]
            row.append(source_lookup[(n,frozenset((word[j],word[(j+1)%6])))])
        actual.append(tuple(sorted(row)))
    assert Counter(actual)==Counter({tuple(t):2 for t in expected})
    assert len(vertices)-len(face_edges)+len(faces)==0
    return len(vertices)

def vector(star):
    row=[Fraction(0) for _ in range(13)]
    for name,i in star:
        row[i+(0 if name=='A' else 6)]+=1
    row[-1]=-2
    return row

def row_basis(rows):
    basis={}
    for row in rows:
        r=list(map(Fraction,row))
        for pivot,b in sorted(basis.items()):
            if r[pivot]:
                m=r[pivot]
                r=[x-m*y for x,y in zip(r,b)]
        pivot=next((j for j,x in enumerate(r) if x),None)
        if pivot is not None:
            m=r[pivot];basis[pivot]=[x/m for x in r]
    return basis

def in_span(row,basis):
    r=list(row)
    for pivot,b in sorted(basis.items()):
        if r[pivot]:
            m=r[pivot]
            r=[x-m*y for x,y in zip(r,b)]
    return not any(r)

def angle_selection(w, choices):
    possible=corner_stars(w)
    target={(n,i) for n in ('A','B') for i in range(6)}
    hex_rows=[]
    for n in ('A','B'):
        r=[Fraction(int((j<6)==(n=='A'))) for j in range(12)]+[Fraction(-4)]
        hex_rows.append(r)
    checked=0
    for bits in range(1<<len(possible)):
        legal=[s for j,s in enumerate(possible) if bits>>j&1]
        if {c for star in legal for c in star}!=target:
            continue
        checked+=1
        basis=row_basis(hex_rows+[vector(s) for s in legal])
        assert any(all(in_span(vector(s),basis) for s in stars) for stars in choices)
    assert checked
    return checked

def main():
    cert=json.loads(CERT.read_text())
    assert cert['domain']=={'k5':360,'k6':60}
    # Enumerate every linear permutation, THEN quotient rotations/reflections.
    # This independently visits 5,040 words rather than the search's 420 representatives.
    enumerated={}
    raw=0
    for k in (5,6):
        sets=[tuple(x for x in A if x!=private)+(6,) for private in A] if k==5 else [A]
        domain=set()
        for vals in sets:
            for w in permutations(vals):
                raw+=1
                domain.add(normalize(w))
        assert len(domain)==(360 if k==5 else 60)
        for w in domain:
            if survives(w):enumerated[(k,w)]=triangle_set(w)
    recorded={(r['k'],tuple(r['B'])):r for r in cert['survivors']}
    assert len(recorded)==len(cert['survivors'])==30
    assert set(recorded)==set(enumerated)
    gluing_count=0
    representatives={}
    for key,r in recorded.items():
        k,w=key
        assert r['triangles']==[list(t) for t in enumerated[key]]
        assert r['shared_corner_edges']==len(edges(A)&edges(w))
        actual=[]
        for retained in combinations(sorted(set(A)&set(w)),4):
            stars=split_stars(w,set(retained))
            if stars is not None:actual.append((retained,stars))
        saved=[(tuple(c['retained']),sorted(tuple(tuple(v) for v in s) for s in c['stars'])) for c in r['splittings']]
        assert actual==saved
        for retained,stars in actual:
            torus(w,set(retained),stars);gluing_count+=1
        # Check orbit claims rather than assuming a canonical representative.
        transformed=[]
        for sign in (-1,1):
            for shift in range(6):
                transformed.append(normalize(tuple((sign*x+shift)%6 if x<6 else x for x in w)))
        assert tuple(r['orbit'])==min(transformed)
        representatives[(k,tuple(r['orbit']))]=w
    counts=Counter((k,tuple(r['orbit'])) for (k,w),r in recorded.items())
    assert counts==Counter({(r['k'],tuple(r['representative'])):r['count'] for r in cert['orbit_counts']})
    assert sorted(counts.values())==[3,3,12,12]
    angular_cases=0
    for key,w in representatives.items():
        choices=[stars for retained in combinations(sorted(set(A)&set(w)),4)
                 if (stars:=split_stars(w,set(retained))) is not None]
        angular_cases+=angle_selection(w,choices)
    assert raw==5040
    print(f'PASS: {raw} raw words / 420 normalized words; 30 survivors; '
          f'{gluing_count} four-face torus gluings; {angular_cases} covering angle-support cases.')

if __name__=='__main__':
    main()
