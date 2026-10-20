#!/usr/bin/env python3
"""Exact four-support rowspace gate; no solver or geometric search."""
import importlib.util,itertools,json
from pathlib import Path
from sage.all import QQ,matrix,vector
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("atlas",root/"research/searches/hexagon-five-four-forced-dimer-2026-10-19.py")
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
stars=a.build((0,1,1,0,2,3))["fixed_stars"]
fixtures=json.loads((root/"research/certificates/hexagon-five-four-39-omissions-2026-10-19.json").read_text())["rows"]
for mask in (33416,41032,20774,22550):
 rows=[[int(i//6==f) for i in range(12)]+[4] for f in range(2)]
 rows += [[sum(p[0]==i for p in stars[k]) for i in range(12)]+[2] for k in range(len(stars)) if mask>>k&1]
 M=matrix(QQ,rows);V=M.row_space();triples=[];equalities=[]
 for f in range(2):
  tt=[];ee=[]
  for inds in itertools.combinations(range(6),3):
   if vector(QQ,[int(i//6==f and i%6 in inds) for i in range(12)]+[2]) in V:tt.append(inds)
  for j,k in itertools.combinations(range(6),2):
   if vector(QQ,[int(i==6*f+j)-int(i==6*f+k) for i in range(12)]+[0]) in V:ee.append((j,k))
  triples.append(tt);equalities.append(ee)
 if mask in (33416,41032):
  assert triples==[[],[]] and equalities==[[],[]]
  fixture=fixtures[1]
  assert M*vector(QQ,[QQ(x)/180 for x in fixture["angles"]]+[-1])==0
  assert not fixture["H1_carriers"]
 elif mask==20774:assert triples==[[(0,1,2),(3,4,5)],[]]
 else:assert triples==[[(0,1,2),(3,4,5)],[(0,1,2),(3,4,5)]]
 print(mask,"triples",triples,"equalities",equalities)
words=((0,1,2,0,3,4),(0,1,1,0,2,3))
for w in words:
 assert [j for j in range(3) if w[j]==w[j+3]]==[0]
 assert not any(w[(o+s*2)%6]==w[(o+s*5)%6] and w[(o+s)%6]==w[(o+s*3)%6] for o in range(6) for s in (1,-1))
 assert not any(all(w[(j+2*k)%6]==w[(j+2*k+1)%6] for k in range(3)) for j in range(2))
print("PASS: universal A H1 on20774; universal A,B H1 on22550;33416,41032 remain unresolved")
