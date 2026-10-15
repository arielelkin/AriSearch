#!/usr/bin/env python3
"""Complete 48-word native endpoint/contact-component gate; integer only.
Distinct doubled formal colors, same five colors, separation two on both.
No import from previous research programs, metric solver, or torus search.
"""
from itertools import permutations, combinations
from pathlib import Path
import argparse, json
A=(0,1,0,2,3,4)

def arm(words,c):
 f,i=divmod(c,6)
 return frozenset((words[f][i],words[f][(i+1)%6]))

def slot(words,c,r):
 f,i=divmod(c,6)
 assert len(arm(words,c))==2 and r in arm(words,c)
 return 6*f+(i if words[f][i]==r else (i+1)%6)

def far(words,c,r):
 j=slot(words,c,r);f,i=divmod(j,6)
 return 6*f+(i-1)%6 if c==j else j

def atlas(words):
 return [t for t in combinations(range(12),3)
         if len({arm(words,c) for c in t})==3
         and len(set().union(*(arm(words,c) for c in t)))==3]

def demands(words,t):
 out=[]
 for c,d in combinations(t,2):
  common=arm(words,c)&arm(words,d)
  assert len(common)==1
  r=next(iter(common));cc,dd=far(words,c,r),far(words,d,r)
  out.append((c,d,r,cc,dd))
 return out

def choices(stars,cc,dd):
 return [t for t in stars if cc!=dd and cc in t and dd in t]

def components(words,stars):
 edges=set()
 for t in stars:
  for c,d,r,cc,dd in demands(words,t):
   edges.add(tuple(sorted((slot(words,c,r),slot(words,d,r)))))
 sets=[{c} for c in range(12)]
 for a,b in sorted(edges):
  union=sets[a]|sets[b]
  for c in union:sets[c]=union
 return sorted(edges),sorted({tuple(sorted(s)) for s in sets})

def analyze(B):
 W=(A,B);original=atlas(W);current=original;rounds=[]
 while True:
  removed=[];survive=[]
  for t in current:
   absent=[q for q in demands(W,t) if not choices(current,q[3],q[4])]
   if absent:removed.append({'star':t,'failed_demand':absent[0]})
   else:survive.append(t)
  if not removed:break
  rounds.append({'input':current,'removed':removed,'output':survive})
  current=survive
 covered=sorted({c for t in current for c in t})
 edges,comps=components(W,current)
 supports=[]
 # Enumerate fixed-point subsets, whose actual necessity follows by pruning.
 # Coverage and each of the three exact far-end requirements are checked.
 for mask in range(1<<len(current)):
  selected=[t for i,t in enumerate(current) if mask>>i&1]
  if {c for t in selected for c in t}!=set(range(12)):continue
  if not all(choices(selected,q[3],q[4]) for t in selected for q in demands(W,t)):continue
  es,cs=components(W,selected)
  joined_A=any(0 in c and 2 in c for c in cs)
  joined_B=any(6 in c and 8 in c for c in cs)
  assert not(joined_A and joined_B)
  supports.append({'mask_in_fixed_point':mask,'stars':selected,'seams':es,
                   'components':cs,'A_repeated_joined':joined_A,'B_repeated_joined':joined_B})
 joins=[any(a in c and b in c for c in comps) for a,b in ((0,2),(6,8))]
 if covered==list(range(12)):assert not all(joins)
 return {'B':B,'initial_atlas':original,'pruning_rounds':rounds,
         'pruning_sizes':[len(original)]+[len(r['output']) for r in rounds],
         'fixed_point':current,'covered_corners':covered,'fixed_point_seams':edges,
         'fixed_point_components':comps,'fixed_point_repeated_joined':joins,
         'endpoint_closed_corner_cover_supports':supports}

def build():
 raw=[(p,q[0],p,*q[1:]) for p in range(1,5)
      for q in permutations(sorted(set(range(5))-{p}))]
 normalized=sorted({min(w,(w[0],w[1],w[2],w[5],w[4],w[3])) for w in raw})
 assert len(raw)==96 and len(normalized)==48
 rows=[analyze(B) for B in normalized]
 survivors=[r for r in rows if r['covered_corners']==list(range(12))]
 assert len(survivors)==8
 assert sum(len(r['endpoint_closed_corner_cover_supports']) for r in rows)==36
 assert all(not r['fixed_point'] for r in rows if r not in survivors)
 return {'schema':'DIFFERENT_REPEAT_SEPARATION_TWO_CONTACT_SPLIT_V1','A':A,
         'colors':list(range(5)),'raw_words':raw,'normalized_words':normalized,
         'records':rows,'summary':{'raw_words':96,'normalized_words':48,
         'empty_fixed_points':40,'covering_fixed_points':8,'actual_support_candidates':36},
         'scope':'Exact finite necessary source gate; periodic implication uses formal-color theorem.'}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
 data=build();encoded=json.dumps(data,sort_keys=True,indent=2)+'\n'
 if args.output:Path(args.output).write_text(encoded)
 print(encoded,end="")
