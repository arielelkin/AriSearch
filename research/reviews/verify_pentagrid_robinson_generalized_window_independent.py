#!/usr/bin/env python3
"""Independent complete generalized-source gate certificate check.

No generalized producer, LP, polyhedron or circuit-enumeration imports.
Reuses the independently reviewed native graph/facet reconstruction only.
"""
from collections import Counter
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("proper_independent",Path(__file__).with_name(
    "verify_pentagrid_robinson_penrose_window_independent.py"))
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
F=w.F

def main():
    directory=ROOT/"research/certificates"
    c=json.loads((directory/"pentagrid-robinson-generalized-window.json").read_text())
    completion=json.loads((directory/"pentagrid-robinson-boundary-completion.json").read_text())
    residual=json.loads((directory/"pentagrid-robinson-residual-rhombs.json").read_text())
    facets=w.derive_facets()
    retained=tuple(tuple(F(x) for x in row) for row in c["window_facets"])
    assert len(retained)==len(facets)==20
    assert all(sum(w.equal_ray(a,b) for a in facets)==1 for b in retained)
    assert all(sum(w.equal_ray(a,b) for b in retained)==1 for a in facets)
    positive_count=dual_count=width_count=0
    for domain in ("mandatory","full"):
        source=completion if domain=="mandatory" else residual
        for label,rec in c["domains"][domain].items():
            objects=(source["fixtures"][label]["surviving_boundary_words"] if domain=="mandatory"
                     else source["fixtures"][label]["results"])
            required=(set(range(len(objects))) if domain=="mandatory" else
                      {i for i,obj in enumerate(objects) if obj["whole_rhombs"] is not None})
            seen=set();counts=Counter()
            for obj in rec["results"]:
                ix=obj["source_index"];assert ix not in seen;seen.add(ix)
                words=objects[ix] if domain=="mandatory" else objects[ix]["side_words"]
                assert words==obj["side_words"]
                rhombs=None if domain=="mandatory" else objects[ix]["whole_rhombs"]
                _,N=w.lifts(label,words,rhombs)
                assert len(N)==obj["vertex_count"]
                lo,hi=min(map(sum,N.values())),max(map(sum,N.values()))
                assert [lo,hi]==obj["layer_interval"]
                gate=obj["window_gate"];verdict=gate["verdict"];counts[verdict]+=1
                if verdict=="fails strict five-layer-width necessity":
                    assert hi-lo>=5;width_count+=1
                    continue
                assert hi-lo<5
                rows=[(h0+hk*k+ha*a+ht*t,-hk,-ha,-ht)
                      for k,a,t in map(w.projected,N.values()) for h0,hk,ha,ht in facets]
                if verdict=="strict shifted-window witness":
                    shift=tuple(F(x) for x in gate["internal_shift"])
                    slacks=[r[0]+sum(r[j+1]*shift[j] for j in range(3)) for r in rows]
                    assert all(w.sign(x)>0 for x in slacks)
                    assert min(slacks)==F(gate["minimum_facet_slack"])
                    from sage.all import QQ
                    assert gate["integer_intercept_sum"]==(shift[0] in QQ and QQ(shift[0]).denominator()==1)
                    positive_count+=1
                else:
                    assert verdict=="no strict shifted-window witness"
                    dual=gate["dual_obstruction"]
                    selected=[tuple(F(x) for x in r) for r in dual["selected_rows"]]
                    weights=[F(x) for x in dual["positive_weights"]]
                    assert len(selected)==len(weights) in (2,3,4)
                    assert all(w.sign(x)>=0 for x in weights) and any(w.sign(x)>0 for x in weights)
                    assert all(r in rows for r in selected)
                    assert all(sum(weight*r[j] for weight,r in zip(weights,selected))==0 for j in (1,2,3))
                    constant=sum(weight*r[0] for weight,r in zip(weights,selected))
                    assert constant==F(dual["constant_sum"]) and w.sign(constant)<=0
                    assert len(dual["facet_indices"])==len(selected)==len(dual["selected_vertex_lifts"])
                    for index,n,row in zip(dual["facet_indices"],dual["selected_vertex_lifts"],selected):
                        assert tuple(n) in N.values()
                        k,a,t=w.projected(n);h0,hk,ha,ht=retained[index]
                        assert row==(h0+hk*k+ha*a+ht*t,-hk,-ha,-ht)
                    dual_count+=1
            assert seen==required and len(seen)==rec["object_count"]
            assert dict(counts)==rec["counts"]
            print(domain,label,len(seen),dict(counts),flush=True)
    assert (positive_count,dual_count,width_count)==(6,113,290)
    print("PASS: all409 objects;6 strict witnesses,113 exact3D dual obstructions,290 width failures.",flush=True)

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Assertions required")
    main()
