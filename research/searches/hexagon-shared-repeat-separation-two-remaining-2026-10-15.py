#!/usr/bin/env python3
"""Exact canonical-domain and three new endpoint obstructions.
Domain: same five distinct labels, repeated r on both hexagons, repeat separation2.
No floating point, solvers, metric search, or periodic quotient enumeration.
Default stdout is the complete deterministic certificate.
"""
from itertools import permutations,combinations
from functools import reduce
from pathlib import Path
import argparse,json
A=(0,1,0,2,3,4)
SIGMA={0:0,1:1,2:4,3:3,4:2}
NEW=((0,2,0,1,3,4),(0,2,0,1,4,3),(0,3,0,1,2,4))
def canon(p):
 m,a,b,c=p
 return min(p,(m,c,b,a))
def word(p):return (0,p[0],0,*p[1:])
def dihedral(w):
 return {v[k:]+v[:k] for v in (tuple(w),tuple(reversed(w))) for k in range(6)}
def arms(words,c):
 f,i=divmod(c,6)
 return frozenset((words[f][i],words[f][(i+1)%6]))
def atlas(words):
 result=[]
 for t in combinations(range(12),3):
  edges={arms(words,c) for c in t}
  if len(edges)==3 and all(len(e)==2 for e in edges) and len(set().union(*edges))==3:
   result.append(t)
 return result
def far(words,c,r):
 f,i=divmod(c,6)
 assert (words[f][i]==r)!=(words[f][(i+1)%6]==r)
 return 6*f+((i-1)%6 if words[f][i]==r else (i+1)%6)
def obstruction(B):
 words=(A,B);stars=atlas(words);current=stars;rounds=[]
 while True:
  survivors=[];removed=[]
  for t in current:
   failure=None
   for c,d in combinations(t,2):
    common=arms(words,c)&arms(words,d)
    assert len(common)==1
    ray=next(iter(common));pair=(far(words,c,ray),far(words,d,ray))
    choices=[u for u in current if pair[0]!=pair[1] and all(v in u for v in pair)]
    if not choices:
     failure={"star":t,"seam_corners":(c,d),"ray":ray,"far_corners":pair};break
   if failure is None:survivors.append(t)
   else:removed.append(failure)
  if not removed:break
  rounds.append({"input_stars":current,"removed":removed,"survivors":survivors})
  current=survivors
 assert not current
 # Independently finite-filter the full ORIGINAL atlas, retaining coverage.
 # All selected stars must possess all three far-end continuations.
 accepted=[]
 for mask in range(1<<len(stars)):
  selected=[t for i,t in enumerate(stars) if mask>>i&1]
  if set(c for t in selected for c in t)!=set(range(12)):continue
  valid=True
  for t in selected:
   for c,d in combinations(t,2):
    ray=next(iter(arms(words,c)&arms(words,d)))
    cc,dd=far(words,c,ray),far(words,d,ray)
    if cc==dd or not any(cc in u and dd in u for u in selected):valid=False;break
   if not valid:break
  if valid:accepted.append(mask)
 assert accepted==[]
 return {"B":B,"complete_star_atlas":stars,"pruning_rounds":rounds,
         "pruning_sizes":[len(stars)]+[len(r["survivors"]) for r in rounds],
         "endpoint_closed_cornercover_masks":accepted,"enumerated_support_masks":1<<len(stars)}
def build():
 permutations4=list(permutations((1,2,3,4)))
 canonical=sorted({canon(p) for p in permutations4})
 assert len(canonical)==12
 stabilizers=[]
 for p in permutations4:
  relabel={0:0,**dict(zip((1,2,3,4),p))}
  if A in dihedral(tuple(relabel[c] for c in A)):stabilizers.append(p)
 assert stabilizers==[(1,2,3,4),(1,4,3,2)]
 orbits=[];seen=set()
 for p in canonical:
  if p in seen:continue
  orbit=sorted({p,canon(tuple(SIGMA[c] for c in p))});seen.update(orbit)
  rep=orbit[0];B=word(rep)
  if rep[0]==1:
   status="pendant x: A corners0,1 occur in no native star"
   assert all(0 not in t and 1 not in t for t in atlas((A,B)))
  elif B==(0,2,0,3,1,4):status="previously certified endpoint untileability"
  elif B==(0,3,0,2,1,4):status="previously reviewed periodic escape"
  else:
   assert B in NEW
   status="new complete endpoint-pruning untileability"
  orbits.append({"representative_B":B,"normalized_permutations":orbit,"status":status})
 assert len(orbits)==7 and len(seen)==12
 results=[obstruction(B) for B in NEW]
 assert [r["pruning_sizes"] for r in results]==[[0],[8,0],[12,1,0]]
 return {"schema":"SHARED_REPEAT_SEPARATION_TWO_REMAINING_V1",
   "A":A,"labels":"r=0,x=1,y=2,z=3,t=4, all five physically distinct",
   "full_B_permutation_domain":permutations4,"B_reflection_canonical_domain":canonical,
   "A_label_stabilizers":stabilizers,"canonical_orbits":orbits,
   "new_word_obstructions":results,
   "scope":"Three new exact untileability proofs plus exhaustive cyclic-word reduction. Prior two nonpendant branches are separate dependencies."}
if __name__=="__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
 encoded=json.dumps(build(),sort_keys=True,indent=2)+"\n"
 if args.output:Path(args.output).write_text(encoded)
 print(encoded,end="")
