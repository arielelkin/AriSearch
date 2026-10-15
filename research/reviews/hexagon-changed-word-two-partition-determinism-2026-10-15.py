#!/usr/bin/env python3
"""Independent 2-support native-neighbor check; imports no source producer."""
from itertools import product
import json
WORDS=((0,1,0,2,3,4),(0,3,0,2,1,4))
SUPPORTS=(
 ((0,2,9),(1,5,10),(3,7,8),(4,6,11)),
 ((0,5,10),(1,2,9),(3,6,8),(4,7,11)),
)
def arms(c):
 f,i=divmod(c,6)
 return {WORDS[f][i],WORDS[f][(i+1)%6]}
def ends(f,i):return (6*f+(i-1)%6,6*f+i)
records=[]
for support in SUPPORTS:
 assert sorted(c for t in support for c in t)==list(range(12))
 for star in support:
  assert len(set.union(*(arms(c) for c in star)))==3
  assert len({frozenset(arms(c)) for c in star})==3
 table=[]
 for f,i in product(range(2),range(6)):
  matches=[]
  for g,j,reverse in product(range(2),range(6),range(2)):
   if WORDS[f][i]!=WORDS[g][j]:continue
   aa=ends(f,i);bb=ends(g,j)[::(-1 if reverse else 1)]
   completion=[]
   for a,b in zip(aa,bb):
    completion.append([t for t in support if a!=b and a in t and b in t])
   if all(completion):
    assert all(len(x)==1 for x in completion)
    matches.append({"guest_type":g,"guest_side":j,"reverse_endpoints":reverse,
      "endpoint_stars":[x[0] for x in completion]})
  assert len(matches)==1,(support,f,i,matches)
  table.append({"host_type":f,"host_side":i,**matches[0]})
 records.append({"support":support,"unique_native_neighbor_table":table})
print(json.dumps({"status":"PASS independent all24 native side states uniquely determined", "records":records},indent=2))
