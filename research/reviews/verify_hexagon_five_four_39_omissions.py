#!/usr/bin/env python3
"""Exact independent geometry and H1 carrier audit of 39 retained representatives."""
from sage.all import QQ,QuadraticField,vector,matrix
from pathlib import Path
import json
from collections import Counter
K=QuadraticField(3,"r");r=K.gen();root=Path(__file__).resolve().parents[1]
d=json.loads((root/"certificates/hexagon-five-four-angle-grid-2026-10-19.json").read_text())
rows=d["distinct_representatives"];assert len(rows)==39
assert len({tuple(x["angles"]) for x in rows})==39
D=((2,0),(r,1),(1,r),(0,2),(-1,r),(-r,1),(-2,0),(-r,-1),(-1,-r),(0,-2),(1,-r),(r,-1))
words=((0,1,2,0,3,4),(0,1,1,0,2,3));out=[]
def enc(x):return [str(x[0]),str(x[1])]
def cross(a,b):return matrix(K,[a,b]).det()
for row in rows:
 aa=row["angles"];ls=[K(QQ(x[0])+QQ(x[1])*r) for x in row["lengths"]]
 assert ls[0]==1 and min(ls)>0 and len(set(ls))==5
 assert all(x in (90,120,150) for x in aa) and sum(aa[:6])==sum(aa[6:])==720
 for st in ((0,7,6),(1,9,8),(2,3,10),(4,5,11)):assert sum(aa[i] for i in st)==360
 carriers=[];polygons=[]
 for f,word in enumerate(words):
  q=0;p=vector(K,[0,0]);vs=[]
  for j,c in enumerate(word):
   vs.append(p);p=p+ls[c]*vector(K,D[q%12])/2;q+=(180-aa[6*f+j])//30
  assert p==vector(K,[0,0]) and q==12
  polygons.append([[[str(x[0]),str(x[1])] for x in v] for v in vs])
  es=[vs[(j+1)%6]-vs[j] for j in range(6)]
  for j,e in enumerate(es):
   for k in range(6):
    if k not in (j,(j+1)%6):assert cross(e,vs[k]-vs[j])>0
  # Equal opposite side pairs; unique candidate in both words is 0,3.
  opposites=[j for j in range(3) if ls[word[j]]==ls[word[j+3]]]
  assert opposites==[0]
  # H2 has equal pairs (2,5) opposite and (1,3) distance two.
  # Enumerate all cyclic/reflected native side indexings.
  assert not any(ls[word[(off+sgn*2)%6]]==ls[word[(off+sgn*5)%6]] and ls[word[(off+sgn)%6]]==ls[word[(off+sgn*3)%6]] for off in range(6) for sgn in (1,-1))
  # H3 requires three equal adjacent pairs.
  assert not any(all(ls[word[(j+2*k)%6]]==ls[word[(j+2*k+1)%6]] for k in range(3)) for j in range(2))
  h1=es[0]==-es[3]
  assert h1==(sum(aa[6*f:6*f+3])==360)==(f in row["H1_species"])
  if h1:
   # Cyclically start at old vertex4 so e2=-e5, matching reviewed constructor.
   vv=[vs[(j+4)%6]-vs[4] for j in range(6)]
   assert vv[3]==vv[2]+vv[5]
   T=vv[1];a=vv[2];b=vv[3]+vv[4]-vv[1]
   area2=sum(cross(vs[j],vs[(j+1)%6]) for j in range(6))
   assert cross(a,b)==area2>0
   carriers.append({"species":f,"native_start_vertex":4,"halfturn_translation":[enc(x) for x in T],"periods":[[enc(x) for x in u] for u in (a,b)],"covolume":enc(area2)})
 out.append({"angles":aa,"lengths":row["lengths"],"H1_carriers":carriers,"vertices":polygons})
counts=Counter(tuple(x["species"] for x in z["H1_carriers"]) for z in out)
assert counts=={():18,(0,):8,(1,):8,(0,1):5}
result={"schema":"FIVE_FOUR_39_MONOHEDRAL_OMISSIONS_V1","domain":"39 distinct-length cones retained by the finite 90/120/150 support grid","constructor":"research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md","counts":{str(k):v for k,v in counts.items()},"rows":out}
retained=json.loads((root/"certificates/hexagon-five-four-39-omissions-2026-10-19.json").read_text())
assert retained==result
print("PASS:39 exact strict-convex pairs;21 pairs have explicit monohedral H1 carriers;18 escape these tests")
