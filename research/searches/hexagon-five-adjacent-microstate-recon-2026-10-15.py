#!/usr/bin/env python3
"""Exact finite adjacent-repeat native-state generation; independently audited.
Common5colors: A=(0,0,1,2,3,4), B doubled at0,bp, bp=1,2,3.
All120 raw B words per bp. Native vertex states carry all3 exact side-slot
seams and opposite endpoint multisets; no metric or torus search.
Default JSON retains every survivor state, not just counts. No file writes.
"""
from itertools import combinations_with_replacement,product,permutations
from collections import defaultdict,Counter
import json
A=(0,0,1,2,3,4)
def microstates(W):
 loc=defaultdict(list)
 for f,w in enumerate(W):
  for i in range(6):loc[tuple(sorted((w[i],w[(i+1)%6])))].append(f*6+i)
 stars=set()
 for rays in combinations_with_replacement(range(5),3):
  es=[tuple(sorted((rays[i],rays[(i+1)%3]))) for i in range(3)]
  if all(e in loc for e in es):
   for cs in product(*(loc[e] for e in es)):stars.add(tuple(sorted(cs)))
 out=set()
 def far(c,s):
  f,i=divmod(c,6);assert s//6==f and s%6 in(i,(i+1)%6)
  return f*6+((i-1)%6 if s%6==i else (i+1)%6)
 for cs in stars:
  for flip in product((0,1),repeat=3):
   left=[];right=[]
   for c,k in zip(cs,flip):
    f,i=divmod(c,6);sides=(6*f+i,6*f+(i+1)%6);left.append(sides[k]);right.append(sides[1-k])
   if any(W[right[i]//6][right[i]%6]!=W[left[(i+1)%3]//6][left[(i+1)%3]%6] for i in range(3)):continue
   rr=[]
   for i in range(3):
    j=(i+1)%3;a=right[i];b=left[j]
    rr.append((tuple(sorted((a,b))),tuple(sorted((cs[i],cs[j]))),tuple(sorted((far(cs[i],a),far(cs[j],b))))))
   out.add((cs,tuple(sorted(rr))))
 return out

def prune(M):
 while True:
  keys={(r[0],r[1]) for st,rr in M for r in rr}
  T={m for m in M if all((r[0],r[2]) in keys for r in m[1])}
  if T==M:return M
  M=T

def build():
 records=[];summaries=[]
 for bp in (1,2,3):
  stats=Counter()
  for p in range(5):
   for q in permutations(sorted(set(range(5))-{p})):
    B=[None]*6;B[0]=B[bp]=p
    for i,v in zip((j for j in range(6) if B[j] is None),q):B[i]=v
    W=(A,tuple(B));original=microstates(W);M=prune(original)
    cover=sorted({c for st,rr in M for c in st});parent=list(range(12))
    def find(i):
     while parent[i]!=i:i=parent[i]
     return i
    for st,rr in M:
     for r in rr:
      x,y=map(find,r[0]);parent[x]=y
    joined=[find(0)==find(1),find(6)==find(6+bp)]
    kind='no_cover' if cover!=list(range(12)) else ('both_joined' if all(joined) else 'color_escape')
    stats[kind]+=1
    records.append({'B_repeat_separation':bp,'B':B,'initial_states':sorted(original),'fixed_states':sorted(M),'covered_corners':cover,'repeated_joined':joined,'kind':kind})
  summaries.append({'B_repeat_separation':bp,'counts':dict(stats)})
 return {'status':'INDEPENDENTLY_AUDITED_NATIVE_GATE_ONLY','A':A,'raw_word_count':360,'records':records,'summary':summaries}
if __name__=='__main__':print(json.dumps(build(),sort_keys=True,indent=2))
