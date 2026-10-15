#!/usr/bin/env python3
"""Exploratory bounded six-distinct/four-distinct all-shared gate.
No global tiling or periodicity inference is made from a retained support.
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

def angle_witness(selected,models):
 import z3
 xs=[z3.Real('a%d'%i) for i in range(12)];solver=z3.Solver()
 solver.add(*(z3.And(x>0,x<1) for x in xs))
 solver.add(sum(xs[:6])==4,sum(xs[6:])==4)
 solver.add(*(sum(xs[c] for c in st)==2 for st in selected))
 for ring in models:solver.add(z3.Not(z3.And(*(sum(xs[c] for c in st)==2 for st in ring))))
 result=solver.check()
 return {'status':str(result),'angles_pi':[str(solver.model().eval(x)) for x in xs] if result==z3.sat else None}

def span_ring(selected,models):
 from fractions import Fraction as F
 def row(st):return [F(st.count(i)) for i in range(12)]+[F(-2)]
 rows=[[F(int(i<6)) for i in range(12)]+[F(-4)],
       [F(int(i>=6)) for i in range(12)]+[F(-4)]]+[row(st) for st in selected]
 basis={};n=len(rows)
 for index,r in enumerate(rows):
  r=list(r);combo=[F(i==index) for i in range(n)]
  for p,(b,bc) in sorted(basis.items()):
   if r[p]:
    m=r[p];r=[x-m*y for x,y in zip(r,b)];combo=[x-m*y for x,y in zip(combo,bc)]
  pivot=next((i for i,x in enumerate(r) if x),None)
  if pivot is not None:
   m=r[pivot];basis[pivot]=([x/m for x in r],[x/m for x in combo])
 for ring in models:
  certificates=[]
  for st in ring:
   r=row(st);combo=[F(0)]*n
   for p,(b,bc) in sorted(basis.items()):
    if r[p]:
     m=r[p];r=[x-m*y for x,y in zip(r,b)];combo=[x+m*y for x,y in zip(combo,bc)]
   if any(r):break
   certificates.append([str(c) for c in combo])
  if len(certificates)==4:return {'ring':ring,'source_stars':selected,'row_combinations':certificates}
 return None

def local_neighbor_maps(B,selected):
 maps=defaultdict(set);words=(A,B)
 for st in selected:
  for flips in product((0,1),repeat=3):
   left=[];right=[]
   for c,flip in zip(st,flips):
    f,i=divmod(c,6);sides=(i,(i+1)%6)
    left.append((f,sides[flip]));right.append((f,sides[1-flip]))
   if not all(words[right[i][0]][right[i][1]]==words[left[(i+1)%3][0]][left[(i+1)%3][1]] for i in range(3)):continue
   triples=[]
   for i in range(3):
    j=(i+1)%3;pair=(far(st[i],right[i][1]),far(st[j],left[j][1]))
    triples.append((i,j,pair))
   if not all(any(not(Counter(pair)-Counter(other)) for other in selected) for i,j,pair in triples):continue
   for i,j,pair in triples:
    maps[(st[i],right[i][1])].add((st[j],left[j][1]))
    maps[(st[j],left[j][1])].add((st[i],right[i][1]))
 return {'all_corner_side_maps_singleton':len(maps)==24 and all(len(v)==1 for v in maps.values()),
  'ambiguous':[{'host_corner':c,'host_side':side,'neighbors':sorted(values)} for (c,side),values in sorted(maps.items()) if len(values)!=1]}

def support_scan(B,ss,cap=16):
 models=rings(B)
 if len(ss)>cap:return {'status':'SKIPPED_ATLAS_CAP','cap':cap,'rings':models}
 possible={st:assignments(st,B) for st in ss}
 pairs={pair:[j for j,st in enumerate(ss) if not(Counter(pair)-Counter(st))]
        for v in possible.values() for a in v for pair in a}
 covers=closed=failures=0;examples=[];partitions=0;span_forced=0;residuals=[];span_certificates=[]
 for mask in range(1<<len(ss)):
  selected=[st for i,st in enumerate(ss) if mask>>i&1]
  if set(c for st in selected for c in st)!=set(range(12)):continue
  covers+=1
  if not all(any(all(any(mask>>j&1 for j in pairs[pair]) for pair in assn) for assn in possible[st]) for st in selected):continue
  closed+=1
  if any(set(ring)<=set(selected) for ring in models):continue
  failures+=1
  ispartition=Counter(c for st in selected for c in st)==Counter(range(12))
  partitions+=ispartition
  forced=span_ring(selected,models)
  if forced is not None:span_forced+=1;span_certificates.append(forced);continue
  residuals.append(selected)
  if len(examples)<3:
   witness=angle_witness(selected,models)
   if witness['status']=='sat':examples.append({'stars':selected,'angle_witness':witness,
      'actual_corner_partition':ispartition,'pure_B_stars':[st for st in selected if min(st)>=6],
      'all_A_stars_AAB':all(sum(c<6 for c in st)==2 for st in selected if min(st)<6)})
 return {'status':'COMPLETE','atlas_cap':cap,'rings':models,'corner_covers':covers,
  'endpoint_closed_covers':closed,'no_ring_covers':failures,'no_ring_partitions':partitions,
  'span_forced_ring_covers':span_forced,'span_ring_certificates':span_certificates,'no_span_ring_supports':residuals,'residual_neighbor_maps':[local_neighbor_maps(B,st) for st in residuals],'angle_feasible_examples':examples}

def main():
 records=[]
 for private in ((0,2),(0,3)):
  labels=set(A)-set(private);linear=0;normalized=set()
  for word in product(sorted(labels),repeat=6):
   if set(word)!=labels:continue
   linear+=1;normalized.add(canonical(word))
  assert linear==1560
  stats=Counter()
  for B in sorted(normalized):
   ss=atlas(B)
   if set(c for st in ss for c in st)!=set(range(12)):stats['missing_corner']+=1;continue
   supported=endpoint_supported(ss,B)
   if set(c for st in supported for c in st)!=set(range(12)):stats['endpoint_pruned_missing_corner']+=1;continue
   row={'A_private':private,'B':B,'initial_stars':ss,'pruned_stars':supported,
    'arm_assignments':{','.join(map(str,st)):assignments(st,B) for st in supported}}
   row.update(support_scan(B,supported));records.append(row)
   stats[row['status']]+=1
   stats['no_ring_patterns']+=int(row.get('no_ring_covers',0)>0)
   print(private,B,'stars',len(ss),'pruned',len(supported),row['status'],
     'closed',row.get('endpoint_closed_covers'),'no_ring',row.get('no_ring_covers'),flush=True,file=sys.stderr)
  print('SUMMARY',private,'linear',linear,'cyclic',len(normalized),dict(stats),flush=True,file=sys.stderr)
 data={'domain':{'A':A,'A_private_pairs':[(0,2),(0,3)],'linear_words_per_private_pair':1560,
  'B_words':'all surjective six-words over the other four A labels, modulo B dihedral only',
  'atlas_cap':16,'subset_search':'all subsets of endpoint-pruned atlas when size<=16'},'records':records}
 parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
 if args.output:Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(data,sort_keys=True))
if __name__=='__main__':main()
