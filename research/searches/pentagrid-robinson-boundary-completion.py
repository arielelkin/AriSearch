#!/usr/bin/env python3
"""Complete forced boundary halves outside each fixed parent source cluster.

No global rhomb extension, arrows or pentagon tiling is inferred.
"""
import importlib.util
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

spec=importlib.util.spec_from_file_location("geo",Path(__file__).with_name("pentagrid-golden-metric-robinson-partitions.py"))
geo=importlib.util.module_from_spec(spec);spec.loader.exec_module(geo)
K=geo.K
real=lru_cache(maxsize=None)(geo.real)


def separated(p,q):
    return any(all(real(geo.cross(a[(i+1)%len(a)]-a[i],w-a[i]))<=0 for w in b)
               for a,b in ((p,q),(q,p)) for i in range(len(a)))


def interior_vertex_on_side(p,q):
    for a,b in ((p,q),(q,p)):
        for w in a:
            for i,x in enumerate(b):
                e=b[(i+1)%len(b)]-x
                if geo.cross(e,w-x)==0 and 0<real((w-x)/e)<1:return True
    return False


def certificate():
    root=Path(__file__).parents[1]
    source=json.loads((root/"certificates"/"pentagrid-robinson-diagonal-boundary.json").read_text())
    out={}
    for name,record in source["fixtures"].items():
        stages={"diagonal_boundary_survivors":len(record["surviving_boundary_words"]),
                "complete_boundary_rhombs_disjoint":0,"also_no_partial_rhomb_contacts":0}
        survivors=[];first=None
        lengths=([(1,2),(1,2),(1,0),(1,0),(1,0)] if name=="U"
                 else [(1,0),(1,3),(1,0),(0,2),(0,2)])
        dirs=[0,4,6,7,8] if name=="U" else [0,3,6,7,9]
        parent=([K(0),geo.phi**3,geo.z+geo.z**2+geo.z**3,geo.z**2+geo.z**3,geo.z**3] if name=="U" else
                [K(0),K(1),1+(1+3*geo.phi)*geo.z**3,2*geo.phi**2*geo.z**3,2*geo.phi*geo.z**4])
        for words in record["surviving_boundary_words"]:
            rhombs=[]
            for side,(word,k) in enumerate(zip(words,dirs)):
                x=parent[side]
                for symbol in word:
                    length={"u":K(1),"l":geo.phi,"s":geo.phi-1}[symbol]
                    y=x+length*geo.z**k
                    if symbol!="u":
                        inside=x+geo.z**(k+(1 if symbol=="l" else 2))
                        outside=x+y-inside
                        poly=[x,outside,y,inside]
                        assert real(geo.area(poly))>0
                        assert all((poly[(j+1)%4]-poly[j])*(poly[(j+1)%4]-poly[j]).conjugate()==1 for j in range(4))
                        rhombs.append(poly)
                    x=y
                assert x==parent[(side+1)%5]
            if not all(separated(a,b) for a,b in combinations(rhombs,2)):continue
            stages["complete_boundary_rhombs_disjoint"]+=1
            if any(interior_vertex_on_side(a,b) for a,b in combinations(rhombs,2)):continue
            stages["also_no_partial_rhomb_contacts"]+=1
            survivors.append(words)
            if first is None:
                first={"side_words":words,
                       "completed_rhombs":[[geo.metric.coefficients(p) for p in r] for r in rhombs]}
        out[name]={"stages":stages,"surviving_boundary_words":survivors,"first_witness":first}
    return {"scope":"necessary whole-rhomb exterior completion of fixed source-cluster boundaries",
            "fixtures":out}


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    print(json.dumps(certificate(),indent=2,sort_keys=True))
