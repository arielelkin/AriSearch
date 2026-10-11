#!/usr/bin/env python3
"""Independent exact certificate and negative-domain audit of residual rhombs.

Imports only reviewer-owned geometry/height code, never producers. All SAT
witnesses are clipped/checked. The 17 reported negatives are replayed with
four native rhomb candidates, different branch order, and no failed-state memo.
No geometric bound is enlarged: depth is the forced remaining6/9 count.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
import importlib.util
import json
from pathlib import Path

_spec=importlib.util.spec_from_file_location("independent_geometry",Path(__file__).with_name(
    "verify_pentagrid_robinson_boundary_geometry_independent.py"))
g=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(g)
K,z,phi=g.K,g.z,g.phi
UNIT={z**k:k for k in range(10)}


def compatible(p,q):return not g.interior_overlap(p,q) and g.partial_contact(p,q) is None

def decode_poly(poly):return tuple(g.decode(c) for c in poly)

def pair_index(poly):
    g.strict_convex(poly)
    assert len(poly)==4
    edges=tuple(b-a for a,b in zip(poly,poly[1:]+poly[:1]))
    assert edges[0]==-edges[2] and edges[1]==-edges[3]
    assert all(e in UNIT and e*e.conjugate()==1 for e in edges)
    i,j=UNIT[edges[0]]%5,UNIT[edges[1]]%5
    assert i!=j
    return g.height.PAIRS.index(tuple(sorted((i,j))))


def unit_segments(name,words):
    P=g.parent(name);dirs=g.height.FIXTURES[name][1];out=[]
    for x,word,k in zip(P,words,dirs):
        for symbol in word:
            y=x+{"u":K(1),"l":phi,"s":phi-1}[symbol]*z**k
            if symbol=="u":out.append((x,y))
            x=y
    return out


def needed(name,words):
    H=g.height.boundary_lift(words,g.height.FIXTURES[name][1])
    assert H[-1]==(0,)*5
    q=g.height.shoelace(H)
    forced,parents,d=g.construct(name,words)
    assert all(n>=b and (n-b)%2==0 for n,b in zip(q,d))
    return forced,parents,tuple((n-b)//2 for n,b in zip(q,d))


def graph_height_consistent(polys):
    # An extra necessary source-height check, independent of geometric coverage.
    neighbors={}
    for p in polys:
        for a,b in zip(p,p[1:]+p[:1]):
            k=UNIT[b-a];delta=g.height.basis(k)
            neighbors.setdefault(a,[]).append((b,delta))
            neighbors.setdefault(b,[]).append((a,tuple(-v for v in delta)))
    heights={}
    for start in neighbors:
        if start in heights:continue
        heights[start]=(0,)*5;queue=deque([start])
        while queue:
            a=queue.popleft()
            for b,d in neighbors[a]:
                want=tuple(x+y for x,y in zip(heights[a],d))
                if b in heights:
                    if heights[b]!=want:return False
                else:heights[b]=want;queue.append(b)
    return True


def verify_positive(name,record):
    words=g.canonical(record["side_words"])
    forced,parents,counts=needed(name,words)
    residual=tuple(decode_poly(p) for p in record["whole_rhombs"])
    assert len(residual)==sum(counts)==(6 if name=="U" else 9)
    assert list(counts)==record["residual_rhomb_counts"]
    actual=Counter(pair_index(p) for p in residual)
    assert tuple(actual[j] for j in range(10))==counts
    for p in parents:pair_index(p)
    for p in residual:
        assert g.clipped_area2(p,g.parent(name))==g.area2(p)
    for a,b in combinations(tuple(parents)+residual,2):assert compatible(a,b)
    for t in forced:assert g.clipped_area2(t,g.parent(name))==g.area2(t)
    assert sum((g.area2(p) for p in tuple(forced)+residual),K(0))==g.area2(g.parent(name))
    # Containment, disjointness and area equality prove exact closed macro coverage.
    return graph_height_consistent(tuple(parents)+residual)


def subtract(boundary,poly):
    result=set(boundary)
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if (a,b) in result:result.remove((a,b))
        elif (b,a) in result:return None
        else:result.add((b,a))
    return frozenset(result)


def edge_sort(e):return (tuple(e[0]),tuple(e[1]))


def replay_negative(name,record):
    words=g.canonical(record["side_words"])
    forced,parents,counts=needed(name,words)
    P=g.parent(name);directions=g.height.FIXTURES[name][1]
    boundary=set()
    for x,word,k in zip(P,words,directions):
        for symbol in word:
            y=x+{"u":K(1),"l":phi,"s":phi-1}[symbol]*z**k
            assert (x,y) not in boundary
            boundary.add((x,y));x=y
    boundary=frozenset(boundary)
    for t in forced:
        boundary=subtract(boundary,t)
        assert boundary is not None
    native_vertices={v for e in unit_segments(name,words) for v in e}
    nodes=0

    @lru_cache(maxsize=None)
    def options(a,b):
        k=UNIT[b-a];out=[]
        # Reverse the author's candidate order; clipping rather than SAT.
        for offset in (4,3,2,1):
            v=z**(k+offset);poly=(a,b,b+v,a+v)
            index=pair_index(poly)
            if g.clipped_area2(poly,P)!=g.area2(poly):continue
            if not all(compatible(poly,r) for r in parents):continue
            if any(g.cross(y-x,w-x)==0 and g.sign(g.dot(w-x,w-y))<0
                   for w in native_vertices for x,y in zip(poly,poly[1:]+poly[:1])):continue
            out.append((index,poly))
        return tuple(out)

    def search(boundary,counts,placed):
        nonlocal nodes
        nodes+=1
        if not any(counts):return not boundary
        if not boundary:return False
        best=None
        for a,b in sorted(boundary,key=edge_sort):
            assert b-a in UNIT
            possible=[(i,p) for i,p in options(a,b) if counts[i]>0
                      and all(compatible(p,r) for r in placed)]
            if not possible:return False
            if best is None or len(possible)<len(best):best=possible
        for i,p in best:
            next_boundary=subtract(boundary,p)
            if next_boundary is None:continue
            left=list(counts);left[i]-=1
            if search(next_boundary,tuple(left),placed+(p,)):return True
        return False

    assert not search(boundary,counts,()),(name,words)
    return nodes


def main():
    # Recheck the entire prerequisite boundary domain by independent clipping.
    g.main()
    root=Path(__file__).parents[1]/"certificates"
    certificate=json.loads((root/"pentagrid-robinson-residual-rhombs.json").read_text())
    completion=json.loads((root/"pentagrid-robinson-boundary-completion.json").read_text())
    assert certificate["completion"]=="complete"
    for name,fixture in certificate["fixtures"].items():
        records=fixture["results"]
        domain={g.canonical(w) for w in completion["fixtures"][name]["surviving_boundary_words"]}
        assert len(records)==len(domain)==fixture["boundary_domain"]==fixture["completed_boundaries"]
        assert {g.canonical(r["side_words"]) for r in records}==domain
        positive=negative=negative_nodes=height_failures=0
        for record in records:
            if record["whole_rhombs"] is not None:
                assert record["verdict"]=="SAT finite unit-rhomb cluster"
                consistent=verify_positive(name,record)
                if not consistent:height_failures+=1
                positive+=1
            else:
                assert record["verdict"]=="UNSAT complete residual domain"
                negative_nodes+=replay_negative(name,record);negative+=1
        assert positive==fixture["SAT_count"]
        assert positive+negative==len(domain)
        assert verify_positive(name,fixture["first_witness"])
        print(name,"verified positive clusters",positive,"independently replayed negatives",negative,
              "negative search nodes",negative_nodes,"positive full-patch height failures",height_failures,flush=True)
    print("Independent residual certificate audit passed: finite cluster geometry only, no arrows/global extension.",flush=True)


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    main()
