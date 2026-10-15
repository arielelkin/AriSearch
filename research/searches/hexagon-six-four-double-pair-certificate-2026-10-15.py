#!/usr/bin/env python3
"""Deterministic stdlib-only proof certificate for A6/B(2,2,1,1).

Exactly 2160 raw B words, 192 B-dihedral representatives. All retained
endpoint-closed covers carry direct formal-ring or exact row-combination
witnesses. JSON goes to stdout; only --output PATH writes a file.
No solver, Sage, geometry approximation, seed, or placement search.
"""
from itertools import combinations, combinations_with_replacement, product
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import json
A=tuple(range(6))
def canonical(w):return min(tuple(v[i:]+v[:i]) for v in (list(w),list(reversed(w))) for i in range(6))

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

def all_closed_covers(B,ss,models):
    possible={st:assignments(st,B) for st in ss}
    pair_masks={pair:sum(1<<j for j,st in enumerate(ss)
                         if not(Counter(pair)-Counter(st)))
                for choices in possible.values() for microstate in choices
                for pair in microstate}
    records=[]
    for mask in range(1<<len(ss)):
        selected=[st for j,st in enumerate(ss) if mask>>j&1]
        if set(c for st in selected for c in st)!=set(range(12)):continue
        if not all(any(all(mask & pair_masks[pair] for pair in microstate)
                       for microstate in possible[st]) for st in selected):continue
        direct=next((ring for ring in models if set(ring)<=set(selected)),None)
        if direct is not None:witness={'kind':'direct_ring','ring':direct}
        else:
            certificate=span_ring(selected,models)
            assert certificate is not None, (B,selected)
            witness={'kind':'rational_span','certificate':certificate}
        records.append({'stars':selected,'witness':witness})
    return records


def build_certificate():
    cases=[];totals=Counter()
    for private in ((0,2),(0,3)):
        alphabet=sorted(set(A)-set(private));raw=[]
        for word in product(alphabet,repeat=6):
            if sorted(Counter(word).values())==[1,1,2,2]:raw.append(word)
        assert len(raw)==1080
        domain=sorted({canonical(word) for word in raw})
        assert len(domain)==96
        stats=Counter();records=[]
        for B in domain:
            initial=atlas(B)
            if set(c for st in initial for c in st)!=set(range(12)):
                stats['missing_initial_corner']+=1;continue
            pruned=endpoint_supported(initial,B)
            if set(c for st in pruned for c in st)!=set(range(12)):
                stats['missing_pruned_corner']+=1;continue
            assert len(pruned)<=12
            models=rings(B)
            covers=all_closed_covers(B,pruned,models)
            assert covers
            records.append({'B':B,'initial_stars':initial,'pruned_stars':pruned,
                'microstates_far_pairs':{','.join(map(str,st)):assignments(st,B) for st in initial},
                'formal_rings':models,'endpoint_closed_covers':covers})
            stats['feasible_words']+=1
            stats['closed_covers']+=len(covers)
            for cover in covers:stats[cover['witness']['kind']]+=1
        assert stats['feasible_words']==12
        assert stats['closed_covers']==(27 if private==(0,2) else 66)
        assert stats['direct_ring']==(27 if private==(0,2) else 44)
        assert stats['rational_span']==(0 if private==(0,2) else 22)
        assert stats['missing_initial_corner']+stats['missing_pruned_corner']+len(records)==96
        cases.append({'A_private':private,'B_alphabet':alphabet,'raw_words':1080,
            'cyclic_words':96,'statistics':dict(stats),'records':records})
        totals.update(stats)
    assert totals['feasible_words']==24 and totals['closed_covers']==93
    assert totals['direct_ring']==71 and totals['rational_span']==22
    return {'schema':'HEXAGON_A6_B2211_ALL_SHARED_V1','status':'complete_finite_certificate',
        'domain':{'A':A,'A_private_pairs':[(0,2),(0,3)],
            'B_multiplicities':[2,2,1,1],'B_lengths':'all four shared with A',
            'raw_words':2160,'cyclic_words':192,
            'corner_convention':'after side i, between side i and i+1; A0..5/B6..11',
            'equation_convention':'angles in pi units; star coefficients count multiplicity; RHS2; hexagon RHS4'},
        'statistics':dict(totals),'cases':cases}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    data=build_certificate();encoded=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.output:Path(args.output).write_text(encoded)
    print(encoded,end='')

if __name__=='__main__':main()
