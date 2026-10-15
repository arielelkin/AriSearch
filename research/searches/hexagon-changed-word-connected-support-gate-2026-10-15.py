#!/usr/bin/env python3
"""Exact finite necessity gate for ONE changed shared-repeat hexagon word pair.
Enumerates the 2^16 subsets of its 16 native stars; no tilability inference.
"""
from itertools import combinations
import sympy as s
from collections import Counter
W=((0,1,0,2,3,4),(0,3,0,2,1,4));slots=(0,2,6,8)
def arms(c):f,i=divmod(c,6);return set((W[f][i],W[f][(i+1)%6]))
def ends(c):f,i=divmod(c,6);return [6*f+(i-1)%6,c]
def far(c,r):f,i=divmod(c,6);return 6*f+(i-1)%6 if W[f][i]==r else 6*f+(i+1)%6
S=[t for t in combinations(range(12),3) if len(set.union(*(arms(c) for c in t)))==3 and len({frozenset(arms(c)) for c in t})==3]
seams={}
for a,b in combinations(slots,2):
 for flip in (0,1):
  ea,eb=ends(a),ends(b)[::(-1 if flip else 1)]
  matches=[[t for t in S if x in t and y in t and x!=y] for x,y in zip(ea,eb)]
  if all(matches):seams[a,b]=sum(1<<S.index(t[0]) for t in matches)
requirements=[]
for t in S:
 rq=[]
 for c,d in combinations(t,2):
  r=next(iter(arms(c)&arms(d)));cc,dd=far(c,r),far(d,r)
  rq.append(sum(1<<i for i,u in enumerate(S) if cc!=dd and cc in u and dd in u))
 requirements.append(rq)
corner_masks=[sum(1<<i for i,t in enumerate(S) if c in t) for c in range(12)]
trees=[]
for edges in combinations(seams,3):
 seen={0}
 while True:
  new=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
  if new==seen:break
  seen=new
 if len(seen)==4:trees.append((edges, __import__("functools").reduce(int.__or__,(seams[e] for e in edges))))
valid=[]
all_valid=[]
for m in range(1<<16):
 if not all(m&c for c in corner_masks):continue
 if not all(all(m&r for r in requirements[i]) for i in range(16) if m>>i&1):continue
 all_valid.append(m)
 if any(m&t==t for _,t in trees):valid.append(m)
all_minimal=[m for m in all_valid if not any(v!=m and m&v==v for v in all_valid)]
minimal=[m for m in valid if not any(v!=m and m&v==v for v in valid)]
assert len(valid)==144 and len(minimal)==12
rows=[[int(i in range(6*f,6*f+6)) for i in range(12)]+[4] for f in range(2)]
def row(t):return [int(i in t) for i in range(12)]+[2]
flats={}
for m in minimal:
 M=s.Matrix(rows+[row(t) for i,t in enumerate(S) if m>>i&1]);R=M.rref()[0]
 key=tuple(tuple(R[i,:]) for i in range(R.rows) if any(R[i,:]))
 flats.setdefault(key,[]).append(m)

ks=list(flats)
parents=[]
for i,k in enumerate(ks):
    M=s.Matrix(k)
    parents.append([j for j,l in enumerate(ks) if j!=i and s.Matrix(l).col_join(M).rank()==M.rank()])
maximal=[i for i,p in enumerate(parents) if not p]
assert maximal==[0,2,5,6,7,8,10]
def stars_of(m):return [t for i,t in enumerate(S) if m>>i&1]
certificate={
 "schema":"CHANGED_WORD_CONNECTED_R_SUPPORT_V1",
 "words":W,"corner_convention":"corner i follows side i; B corners offset6",
 "full_star_atlas":S,"r_slots":slots,
 "r_seams":[{"slots":e,"endpoint_stars":stars_of(m)} for e,m in seams.items()],
 "trees":[{"edges":e,"forced_stars":stars_of(m)} for e,m in trees],
 "far_end_requirements":[[stars_of(r) for r in rq] for rq in requirements],
 "connected_corner_covering_endpoint_closed_masks":valid,
 "all_endpoint_closed_cornercover_masks":all_valid,
 "all_minimal_supports":[{"mask":m,"stars":stars_of(m)} for m in all_minimal],
 "minimal_supports":[{"mask":m,"stars":stars_of(m)} for m in minimal],
 "angle_flats":[{"id":i,"minimal_support_masks":flats[k],
       "rref_augmented_rows":[[str(v) for v in r] for r in k],
       "containing_flat_ids":parents[i]} for i,k in enumerate(ks)],
 "maximal_flat_ids":maximal,
 "angle_units":"pi; polygon sums4, native star sums2",
 "scope":"Necessary local systems only; no global existence or metric feasibility claim."
}
if __name__=="__main__":
    import argparse,json
    from pathlib import Path
    parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
    encoded=json.dumps(certificate,indent=2)+"\n"
    if args.output:Path(args.output).write_text(encoded)
    print(encoded,end="")
