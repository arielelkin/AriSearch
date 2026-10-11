#!/usr/bin/env python3
"""Exact residual6/9-rhomb peeling for fixed source-cluster boundaries.

Depth is forced by area, not a guessed patch bound. SAT is finite cluster
existence only; no Penrose arrows or global partition is tested.
"""
import argparse
import importlib.util
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import time


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(path))
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result
completion=module("completion","pentagrid-robinson-boundary-completion.py")
height=module("height","pentagrid-robinson-height-boundary.py")
geo=completion.geo;K,z,phi=geo.K,geo.z,geo.phi
real=completion.real
PAIRS=height.PAIRS
UNIT={z**k:k for k in range(10)}


def pointkey(p):return tuple(p.list())


def polygonkey(poly):
    keys=[pointkey(p) for p in poly]
    return min(tuple(keys[i:]+keys[:i]) for i in range(len(keys)))


def edge(a,b):
    ka,kb=pointkey(a),pointkey(b)
    return ((ka,kb),1) if ka<kb else ((kb,ka),-1)


def add_edges(boundary,poly,sign):
    result=boundary.copy()
    for a,b in zip(poly,poly[1:]+poly[:1]):
        key,sgn=edge(a,b);result[key]=result.get(key,0)+sign*sgn
        if result[key]==0:del result[key]
    assert all(abs(n)==1 for n in result.values())
    return result


@lru_cache(maxsize=None)
def disjoint(a,b):
    return completion.separated([K(list(p)) for p in a],[K(list(p)) for p in b])


@lru_cache(maxsize=None)
def ete(a,b):
    return not completion.interior_vertex_on_side([K(list(p)) for p in a],[K(list(p)) for p in b])


def solve(name,words,deadline):
    parent=([K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3] if name=="U" else
            [K(0),K(1),1+(1+3*phi)*z**3,2*phi**2*z**3,2*phi*z**4])
    dirs=[0,4,6,7,8] if name=="U" else [0,3,6,7,9]
    end,q,_=height.lifted_boundary(words,dirs);assert not any(end)
    boundary={};forced=[];rhombs=[];diags=Counter();unit_boundary=[]
    for i,(word,k) in enumerate(zip(words,dirs)):
        x=parent[i]
        for symbol in word:
            length={"u":K(1),"l":phi,"s":phi-1}[symbol];y=x+length*z**k
            key,sgn=edge(x,y);assert key not in boundary;boundary[key]=sgn
            if symbol=="u":unit_boundary.append([x,y])
            else:
                apex=x+z**(k+(1 if symbol=="l" else 2));forced.append([x,y,apex])
                rhombs.append([x,x+y-apex,y,apex])
                offsets=(-1,1) if symbol=="l" else (-2,2)
                diags[tuple(sorted((k+d)%5 for d in offsets))]+=1
            x=y
        assert x==parent[(i+1)%5]
    for tri in forced:boundary=add_edges(boundary,tri,-1)
    remaining=tuple((n-diags[p])//2 for p,n in zip(PAIRS,q))
    assert min(remaining)>=0 and sum(remaining)==(6 if name=="U" else 9)
    outside=tuple(polygonkey(r) for r in rhombs)
    unit_vertices=tuple(p for segment in unit_boundary for p in segment)
    stats={"nodes":0,"memo_hits":0};failed=set()

    @lru_cache(maxsize=None)
    def base_candidates(a_key,b_key):
        a,b=K(list(a_key)),K(list(b_key));k=UNIT[b-a];out=[]
        for d in range(1,5):
            v=z**(k+d);poly=[a,b,b+v,a+v];pk=polygonkey(poly)
            pair=tuple(sorted((k%5,(k+d)%5)));index=PAIRS.index(pair)
            if not all(real(geo.cross(parent[(j+1)%5]-parent[j],p-parent[j]))>=0
                       for j in range(5) for p in poly):continue
            if not all(disjoint(pk,rk) and ete(pk,rk) for rk in outside):continue
            bad=False
            for p in unit_vertices:
                for j,x in enumerate(poly):
                    e=poly[(j+1)%4]-x
                    if geo.cross(e,p-x)==0 and 0<real((p-x)/e)<1:bad=True
            if bad:continue
            out.append((index,poly,pk))
        return tuple(out)

    def visit(bdry,counts,placed):
        if time.monotonic()>deadline:raise TimeoutError
        stats["nodes"]+=1
        if not any(counts):
            assert not bdry
            return list(placed)
        key=(tuple(sorted(bdry.items())),counts)
        if key in failed:stats["memo_hits"]+=1;return None
        choices=None
        for (ka,kb),sgn in sorted(bdry.items()):
            a_key,b_key=(ka,kb) if sgn==1 else (kb,ka)
            candidates=[]
            for index,poly,pk in base_candidates(a_key,b_key):
                if not counts[index]:continue
                if not all(disjoint(pk,rk) and ete(pk,rk) for rk in placed):continue
                candidates.append((index,poly,pk))
            if not candidates:failed.add(key);return None
            if choices is None or len(candidates)<len(choices):choices=candidates
            if len(choices)==1:break
        for index,poly,pk in choices:
            nextcounts=list(counts);nextcounts[index]-=1
            answer=visit(add_edges(bdry,poly,-1),tuple(nextcounts),placed+(pk,))
            if answer is not None:return answer
        failed.add(key);return None

    answer=visit(boundary,remaining,())
    return {"verdict":"SAT finite unit-rhomb cluster" if answer is not None else "UNSAT complete residual domain",
            "side_words":words,"nodes":stats["nodes"],"memo_hits":stats["memo_hits"],
            "residual_rhomb_counts":remaining,
            "whole_rhombs":None if answer is None else [[geo.metric.coefficients(K(list(p))) for p in pk] for pk in answer]}


def certificate(seconds):
    source=json.loads((Path(__file__).parents[1]/"certificates"/"pentagrid-robinson-boundary-completion.json").read_text())
    deadline=time.monotonic()+seconds;out={};complete=True
    for name,record in source["fixtures"].items():
        results=[];first=None
        for words in record["surviving_boundary_words"]:
            try:r=solve(name,words,deadline)
            except TimeoutError:complete=False;break
            results.append(r)
            if first is None and r["whole_rhombs"] is not None:first=r
        out[name]={"boundary_domain":len(record["surviving_boundary_words"]),
                   "completed_boundaries":len(results),"SAT_count":sum(r["whole_rhombs"] is not None for r in results),
                   "total_nodes":sum(r["nodes"] for r in results),"first_witness":first,
                   "results":results}
        if not complete:break
    return {"scope":"fixed actual-rhomb source-cluster geometry, residual6/9 whole rhombs; no arrows or global partition",
            "completion":"complete" if complete else "UNKNOWN timeout",
            "wall_time_limit_seconds":seconds,"fixtures":out}


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    parser=argparse.ArgumentParser();parser.add_argument("--seconds",type=float,default=120)
    args=parser.parse_args();print(json.dumps(certificate(args.seconds),indent=2,sort_keys=True))
