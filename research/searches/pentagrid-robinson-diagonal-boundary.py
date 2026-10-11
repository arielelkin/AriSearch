#!/usr/bin/env python3
"""Mandatory source-diagonal completion of height-compatible boundaries.

All625/21801 words are checked; only unique forced boundary triangles are
placed. Interior assemblies and arrow rules are not inferred from survivors.
"""
import importlib.util
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(path))
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result
height=module("height","pentagrid-robinson-height-boundary.py")
geometry=module("geometry","pentagrid-golden-metric-robinson-partitions.py")
K,z,phi=geometry.K,geometry.z,geometry.phi


def contained(parent,tri):
    return all(geometry.real(geometry.cross(parent[(j+1)%5]-parent[j],p-parent[j]))>=0
               for j in range(5) for p in tri)


def certificate():
    fixtures={
      "U": ([(1,2),(1,2),(1,0),(1,0),(1,0)],[1,3,4,4,3],[0,4,6,7,8],
             [K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3],(7,9)),
      "V": ([(1,0),(1,3),(1,0),(0,2),(0,2)],[2,2,4,3,4],[0,3,6,7,9],
             [K(0),K(1),1+(1+3*phi)*z**3,2*phi**2*z**3,2*phi*z**4],(9,16)),
    }
    table={(a,b,n):height.boundary.fans(a,b,n)
           for a,b,n in product(height.boundary.LENGTHS,height.boundary.LENGTHS,range(1,6))}
    out={}
    for name,(lengths,angles,directions,parent,content) in fixtures.items():
        stages=Counter();first=None;survivors=[]
        for words in product(*(height.boundary.words(a,b) for a,b in lengths)):
            stages["all"]+=1
            end,q,vertices=height.lifted_boundary(words,directions)
            if any(end) or min(q)<0:continue
            tests=[]
            for i,word in enumerate(words):
                tests.extend((word[j],word[j+1],5) for j in range(len(word)-1))
                tests.append((word[-1],words[(i+1)%5][0],angles[i]))
            if not all(table[t] for t in tests):continue
            stages["height_wedge_fans"]+=1
            diag=Counter();forced=[]
            for side,(word,k) in enumerate(zip(words,directions)):
                x=parent[side]
                for symbol in word:
                    length={"u":K(1),"l":phi,"s":phi-1}[symbol]
                    y=x+length*z**k
                    if symbol!="u":
                        offsets=(-1,1) if symbol=="l" else (-2,2)
                        pair=tuple(sorted((k+d)%5 for d in offsets))
                        diag[pair]+=1
                        apex=x+z**(k+(1 if symbol=="l" else 2))
                        forced.append([x,y,apex])
                    x=y
                assert x==parent[(side+1)%5]
            if any(n<diag[p] or (n-diag[p])%2 for p,n in zip(height.PAIRS,q)):continue
            stages["diagonal_count_and_parity"]+=1
            if not all(contained(parent,t) for t in forced):continue
            stages["forced_triangles_contained"]+=1
            if not all(geometry.separated(a,b) for a,b in combinations(forced,2)):continue
            stages["forced_triangles_disjoint"]+=1
            survivors.append(words)
            if first is None:
                first={"side_words":words,"oriented_triangle_counts":q,
                       "boundary_diagonal_counts":[diag[p] for p in height.PAIRS],
                       "forced_triangles":[[geometry.metric.coefficients(p) for p in t] for t in forced]}
        out[name]={"stages":dict(stages),"first_witness":first,
                   "surviving_boundary_words":survivors}
    return {"scope":"necessary diagonal-pairing and uniquely forced boundary-triangle geometry only",
            "field":"Q(z), z=exp(pi*i/5), z^4-z^3+z^2-z+1=0",
            "fixtures":out}


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    print(json.dumps(certificate(),indent=2,sort_keys=True))
