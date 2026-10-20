#!/usr/bin/env python3
"""Independent exact witness checker; no cone search or imported producer."""
from sage.all import QQ, QuadraticField, vector, matrix
from pathlib import Path
import json
K=QuadraticField(3, "r"); r=K.gen()
p=Path(__file__).resolve().parents[1]/"certificates/hexagon-five-four-angle-grid-2026-10-19.json"
d=json.loads(p.read_text());w=d["witness"]
def dec(x): return K(QQ(x[0])+QQ(x[1])*r)
lengths=[dec(x) for x in w["lengths"]]
assert lengths[0]==1 and all(x>0 for x in lengths) and len(set(lengths))==5
V=[[vector(K,[dec(x) for x in v]) for v in vs] for vs in w["vertices"]]
angles=w["angles"]
assert all(x in (90,120,150) for x in angles)
assert sum(angles[:6])==sum(angles[6:])==720
for s in ((0,7,6),(1,9,8),(2,3,10),(4,5,11)):assert sum(angles[i] for i in s)==360
# Check side lengths, exact interior angle cosines, and strict halfplanes.
cosines={90:K(0),120:K(-1)/2,150:-r/2}
for f,word in enumerate(((0,1,2,0,3,4),(0,1,1,0,2,3))):
 vs=V[f];edges=[vs[(j+1)%6]-vs[j] for j in range(6)]
 for j,e in enumerate(edges):
  assert e.dot_product(e)==lengths[word[j]]**2
  nxt=edges[(j+1)%6]
  assert -e.dot_product(nxt)==lengths[word[j]]*lengths[word[(j+1)%6]]*cosines[angles[6*f+j]]
  for k in range(6):
   if k not in (j,(j+1)%6):assert matrix(K,[e,vs[k]-vs[j]]).det()>0
# Distinct congruence classes: differing side-length multisets.
assert sorted(lengths[c] for c in (0,1,2,0,3,4))!=sorted(lengths[c] for c in (0,1,1,0,2,3))
print("PASS: exact pair, five distinct positive lengths, native angles, four stars, strict convexity")
