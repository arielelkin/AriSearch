#!/usr/bin/env python3
"""Complete five-direction height / wedge screen of fixed Robinson boundaries.

Necessary for an actual unit-rhomb source cut along specified diagonals.
It does not search triangle placements, arrows, or whole-plane partitions.
"""
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path

_spec=importlib.util.spec_from_file_location("boundary",Path(__file__).with_name("pentagrid-golden-metric-robinson-boundary.py"))
boundary=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(boundary)
PAIRS=list(combinations(range(5),2))
RELATION=[1,-1,1,-1,1]


def unit(k):
    k%=10
    return [int(i==k%5)*(1 if k<5 else -1) for i in range(5)]


def lift(symbol,k):
    if symbol=="u":return unit(k)
    offsets=(-1,1) if symbol=="l" else (-2,2)
    return [sum(unit(k+d)[i] for d in offsets) for i in range(5)]


def wedge(a,b):
    return [a[i]*b[j]-a[j]*b[i] for i,j in PAIRS]


def lifted_boundary(words,directions):
    h=[0]*5;q=[0]*10;vertices=[h[:]]
    for word,k in zip(words,directions):
        for symbol in word:
            delta=lift(symbol,k)
            q=[x+y for x,y in zip(q,wedge(h,delta))]
            h=[x+y for x,y in zip(h,delta)]
            vertices.append(h[:])
    return h,q,vertices


def certificate():
    table={(a,b,n):boundary.fans(a,b,n)
           for a,b,n in product(boundary.LENGTHS,boundary.LENGTHS,range(1,6))}
    fixtures={
      "U": ([(1,2),(1,2),(1,0),(1,0),(1,0)],[1,3,4,4,3],[0,4,6,7,8],(7,9),1),
      "V": ([(1,0),(1,3),(1,0),(0,2),(0,2)],[2,2,4,3,4],[0,3,6,7,9],(9,16),3),
    }
    result={}
    for name,(lengths,angles,directions,content,required_s) in fixtures.items():
        stages=dict(all=0,zero_height=0,zero_height_and_fans=0,
                    zero_height_and_nonnegative_wedge=0,all_necessary_conditions=0)
        first=None;wedge_hist={}
        for words in product(*(boundary.words(a,b) for a,b in lengths)):
            stages["all"]+=1
            end,q,vertices=lifted_boundary(words,directions)
            ns=sum(w.count("s") for w in words)
            signed=(ns-1) if name=="U" else (3-ns)
            assert end==[signed*x for x in RELATION]
            if any(end):continue
            stages["zero_height"]+=1
            assert ns==required_s
            tests=[]
            for i,word in enumerate(words):
                tests.extend((word[j],word[j+1],5) for j in range(len(word)-1))
                tests.append((word[-1],words[(i+1)%5][0],angles[i]))
            fans=all(table[t] for t in tests)
            if fans:stages["zero_height_and_fans"]+=1
            positive=all(x>=0 for x in q)
            if positive:stages["zero_height_and_nonnegative_wedge"]+=1
            if not fans or not positive:continue
            thin=sum(x for x,(i,j) in zip(q,PAIRS) if j-i in (1,4))
            fat=sum(q)-thin
            assert (thin,fat)==content
            stages["all_necessary_conditions"]+=1
            key=",".join(map(str,q));wedge_hist[key]=wedge_hist.get(key,0)+1
            edge_count=sum(map(len,words));interior=(sum(content)-edge_count+2)//2
            assert edge_count==(10 if name=="U" else 13)
            assert interior==(4 if name=="U" else 7)
            if first is None:
                first={"side_words":words,"lifted_vertices":vertices,
                       "oriented_triangle_counts":q,"thin_count":thin,"fat_count":fat,
                       "boundary_edges":edge_count,"required_interior_vertices":interior}
        result[name]={"side_lengths_basis_1_phi":lengths,"angle_after_side_pi_over_5":angles,
                      "directions_pi_over_5":directions,"stages":stages,
                      "required_total_short_diagonal_edges":required_s,
                      "wedge_histogram":wedge_hist,"first_witness":first}
    return {"scope":"complete necessary source-height / oriented-wedge boundary screen; no triangle arrangement or arrows",
            "height_relation":RELATION,"direction_pairs":PAIRS,"fixtures":result}


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    print(json.dumps(certificate(),indent=2,sort_keys=True))
