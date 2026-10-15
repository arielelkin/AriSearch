#!/usr/bin/env python3
"""Exact finite adjacent-repeat length/corner classification.
Finite certificate supporting the separately written geometric theorem.
"""
from itertools import combinations,combinations_with_replacement,permutations,product
from collections import defaultdict,Counter
import json
import argparse
import sys
from pathlib import Path
A=tuple(range(6))
def canonical(w):return min(tuple(v[i:]+v[:i]) for v in (list(w),list(reversed(w))) for i in range(6))
def orbit(w):return min(canonical(tuple((s*x+h)%6 if x<6 else x for x in w)) for s in(-1,1) for h in range(6))
def edge(w,i):return tuple(sorted((w[i],w[(i+1)%6])))
def atlas(B):
 loc=defaultdict(list)
 for f,w in enumerate((A,B)):
  for i in range(6):loc[edge(w,i)].append(6*f+i)
 stars=set()
 for rays in combinations_with_replacement(sorted(set(A)|set(B)),3):
  es=[tuple(sorted((rays[i],rays[(i+1)%3]))) for i in range(3)]
  if all(e in loc for e in es):
   for cs in product(*(loc[e] for e in es)):stars.add(tuple(sorted(cs)))
 return sorted(stars)
def far(c,side):
 f,i=divmod(c,6)
 if side==i:return f*6+(i-1)%6
 assert side==(i+1)%6
 return f*6+(i+1)%6

def assignments(st,B):
 words=(A,B);out=set()
 for flips in product((0,1),repeat=3):
  left=[];right=[]
  for c,flip in zip(st,flips):
   f,i=divmod(c,6);sides=(i,(i+1)%6)
   left.append((f,sides[flip]));right.append((f,sides[1-flip]))
  if not all(words[right[i][0]][right[i][1]]==words[left[(i+1)%3][0]][left[(i+1)%3][1]] for i in range(3)):continue
  pairs=[]
  for i in range(3):
   j=(i+1)%3
   pairs.append(tuple(sorted((far(st[i],right[i][1]),far(st[j],left[j][1])))))
  out.add(tuple(sorted(pairs)))
 return sorted(out)
def endpoint_supported(stars,B):
 possible={st:assignments(st,B) for st in stars}
 remaining=set(stars)
 while True:
  keep=set()
  for st in remaining:
   if any(all(any(not(Counter(pair)-Counter(other)) for other in remaining) for pair in assignment) for assignment in possible[st]):keep.add(st)
  if keep==remaining:return sorted(remaining)
  remaining=keep

def rings(B):
 found=[]
 for slots in combinations(range(6),4):
  shared=[B[i] for i in slots]
  if len(set(shared))!=4 or not set(shared)<=set(A):continue
  formal=tuple(B[i] if i in slots else 100+i for i in range(6))
  loc=defaultdict(list)
  for f,w in enumerate((A,formal)):
   for i in range(6):loc[edge(w,i)].append(6*f+i)
  if len(loc)!=12:continue
  ts=[]
  for tr in combinations(sorted(set(A)|set(formal)),3):
   es=[tuple(sorted(e)) for e in combinations(tr,2)]
   if all(e in loc for e in es):ts.append(tuple(sorted(loc[e][0] for e in es)))
  if len(ts)==4 and Counter(c for st in ts for c in st)==Counter(range(12)):found.append(sorted(ts))
 return found

def support_check(B,ss):
 models=rings(B);covers=0;closed=[];failures=[]
 for mask in range(1<<len(ss)):
  selected=[st for i,st in enumerate(ss) if mask>>i&1]
  if set(c for st in selected for c in st)!=set(range(12)):continue
  covers+=1
  if endpoint_supported(selected,B)!=selected:continue
  closed.append(selected)
  if not any(set(ring)<=set(selected) for ring in models):failures.append(selected)
 return {'rings':models,'covers_after_pruning':covers,'endpoint_closed_supports':closed,'ring_failures':failures}

def main():
 records={};rawcounts={};survivors=Counter()
 for k in range(6):
  raw=0
  for shared in combinations(A,k):
   vals=shared+tuple(range(6,11-k))
   for p,q,r,s,t in permutations(vals):
    if q>t:continue
    B=(p,p,q,r,s,t);raw+=1;ss=atlas(B)
    if set(c for st in ss for c in st)!=set(range(12)):continue
    survivors[k]+=1;key=(k,orbit(B))
    if key not in records:
     word=key[1];stars=atlas(word);supported=endpoint_supported(stars,word)
     records[key]={'k':k,'B':word,'orbit_count':0,'stars':stars,
      'arm_assignments':{','.join(map(str,st)):assignments(st,word) for st in stars},
      'maximal_endpoint_supported':supported,'endpoint_covers_all':set(c for st in supported for c in st)==set(range(12))}
    records[key]['orbit_count']+=1
  rawcounts[k]=raw
  print('k',k,'raw',raw,'survivors',survivors[k],flush=True,file=sys.stderr)
 rows=list(records.values())
 for r in rows:
  if r['endpoint_covers_all']:r.update(support_check(tuple(r['B']),[tuple(st) for st in r['maximal_endpoint_supported']]))
 for r in rows:print(r['k'],r['B'],'orbit',r['orbit_count'],'stars',len(r['stars']),'closed',len(r['maximal_endpoint_supported']),'covers',r['endpoint_covers_all'],'closed_supports',len(r.get('endpoint_closed_supports',[])),'ring_failures',len(r.get('ring_failures',[])),flush=True,file=sys.stderr)
 data={'rawcounts':rawcounts,'survivors':dict(survivors),'records':rows}
 assert [rawcounts[k] for k in range(6)]==[60,360,900,1200,900,360]
 assert [survivors[k] for k in range(6)]==[0,0,0,0,42,90]
 assert sum(len(r.get('endpoint_closed_supports',[])) for r in rows)==11
 assert all(not r.get('ring_failures') for r in rows)
 parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
 if args.output:Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(data,sort_keys=True))
if __name__=='__main__':main()
