#!/usr/bin/env python3
"""Independent actual-metric fibre/canonical-alias transfer and closure algebra."""
from pathlib import Path
from collections import Counter
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
D=json.loads((root/"research/certificates/terra-001212-all-metric-native-rings.json").read_text())
F=json.loads((root/"research/certificates/terra-001212-residual-functional-actions.json").read_text())
assert D["B_words"][3]==[0,1,2,0,2,1] and len(F["records"])==23
seen=set()
for f in F["records"]:
    p,b=tuple(f["A_partition"]),tuple(f["B_metric"])
    assert (p,b) not in seen;seen.add((p,b))
    ids=f["ring_ids"];assert len(ids)==12
    multiplicity=Counter(tuple(D["raw_rings"][i]["A_tuple"]) for i in ids)
    assert len(multiplicity)==6 and set(multiplicity.values())=={2}
    for i in ids:
        r=D["raw_rings"][i]
        assert r["B_word_index"]==3
        assert tuple(p[j] for j in r["B_native_A_side_sources"])==b
        assert all(p[x]==p[y] for x,y in r["AA_equalities"])
        for o in r["outer"]:
            assert o["species"]=="B" and o["colours"][0]==o["colours"][1]
            assert any([p[j] for j in o["arms"]]==[p[j] for j in offer["arms"]] for offer in o["offers"])
    # Any representative chosen within a full A tuple is thus actual-metric legal.
U,V=s.symbols("U V",nonzero=True);W=-1/(U*V);a,b=s.symbols("a b",positive=True)
word=(0,0,1,2,1,2);turn=(U,V,W);e=[s.Integer(1)]
for colour in word[1:]:e.append(s.cancel(e[-1]*turn[colour]))
assert e==[1,U,U*V,-1,-V,1/U]
closure=sum(q*r for q,r in zip((a,a,b,b,b,a),e))
assert s.cancel(closure-(a*(1+U+1/U)+b*(V*(U-1)-1)))==0
u,v=s.symbols("u v",real=True)
assert s.trigsimp(s.expand_trig(s.sin(u+v)-s.sin(v)-2*s.sin(u/2)*s.cos(v+u/2)))==0
print("PASS: all23 actual metric fibres preserve both aliases in every fullA tuple; native closure and imaginary-part identity independently reconstructed")
