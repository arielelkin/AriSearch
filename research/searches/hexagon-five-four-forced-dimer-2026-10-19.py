#!/usr/bin/env python3
"""Exact native oriented upper atlas, with repeated corners allowed."""
import itertools as I,json,argparse
from pathlib import Path
from collections import Counter
A=(0,1,2,0,3,4)
def canon(t):return min(t[i:]+t[:i] for i in range(3))
def build(B):
 W=(A,B)
 def sides(p):
  c,h=p;f,j=divmod(c,6)
  return (6*f+j,6*f+(j+1)%6) if h==1 else (6*f+(j+1)%6,6*f+j)
 def col(s):return W[s//6][s%6]
 def far(p,s):
  c,h=p;f,j=divmod(s,6)
  return (6*f+((j-1)%6 if c==s else j),h)
 ports=list(I.product(range(12),(1,-1)))
 stars={canon(t) for t in I.product(ports,repeat=3) if all(col(sides(t[i])[1])==col(sides(t[(i+1)%3])[0]) for i in range(3))}
 initial=len(stars);rounds=[]
 def index(S):
  out={}
  for t in S:
   for i in range(3):out.setdefault((t[i],t[(i+1)%3]),set()).add(t)
  return out
 def needs(t,i):
  p,q=t[i],t[(i+1)%3]
  return (far(q,sides(q)[0]),far(p,sides(p)[1]))
 while True:
  ix=index(stars);nxt={t for t in stars if all(needs(t,i) in ix for i in range(3))}
  if nxt==stars:break
  rounds.append([len(stars),len(nxt)]);stars=nxt
 ix=index(stars);seams=[]
 for t in sorted(stars):
  for i in range(3):
   p,q=t[i],t[(i+1)%3]
   seams.append(dict(star=t,sector=i,slots=[sides(p)[1],sides(q)[0]],opposite_stars=sorted(ix[needs(t,i)])))
 dimers=[dict(first=x['star'],sector=x['sector'],second=u) for x in seams if x['slots']==[5,5] for u in x['opposite_stars']]
 opts={}
 for x in seams:
  t=x['star'];i=x['sector'];p,q=t[i],t[(i+1)%3]
  opts.setdefault((x['slots'][0],p[1]),set()).add((x['slots'][1],q[1]))
 certain=[dict(side=k,neighbor=next(iter(v))) for k,v in sorted(opts.items()) if len(v)==1]
 # Full combinatorial boundary corona: ten cyclic vertices, two seams
 # junctions and eight ordinary A corners. States record the external
 # tile native side and handedness; equality propagates that frame across
 # both endpoints of each dimer boundary edge.
 factors=[set() for _ in range(5)]
 for t in stars:
  for i,p in enumerate(t):
   prev=t[(i-1)%3];nxt=t[(i+1)%3]
   if p[1]==1 and 0<=p[0]<=3:
    factors[p[0]+1].add(((sides(prev)[1],prev[1]),(sides(nxt)[0],nxt[1])))
   if p==(4,1) and nxt==(5,1):
    third=t[(i+2)%3]
    factors[0].add(((sides(third)[1],third[1]),(sides(third)[0],third[1])))
 sequence=factors+factors
 coronas=[]
 def extend(k,first,last,states):
  if k==10:
   if last==first:coronas.append(states)
   return
  for left,right in sorted(sequence[k]):
   if left==last:extend(k+1,first,right,states+[right])
 for left,right in sorted(sequence[0]):extend(1,left,right,[left,right])
 # The same external tile may be represented on more than one boundary
 # edge; no global identification or polygon overlap test is asserted.
 return dict(boundary_coronas=coronas,B=B,initial_stars=initial,pruning_rounds=rounds,fixed_stars=sorted(stars),covered_corners=sorted({p[0] for t in stars for p in t}),endpoint_microstates=seams,dimer_endpoint_coronas=dimers,certain_transitions=certain)
def main():
 rows=[build(b) for b in sorted(set(I.permutations((0,0,1,1,2,3))))]
 assert len(rows)==180
 out=dict(schema='FIVE_FOUR_ORIENTED_NATIVE_UPPER_ATLAS_V1',A=A,domain='180 permutations 001123; 24 signed corner ports; cyclic triples allowing repetition; both handednesses; no angle constraints',rows=rows,summary=dict(words=180,full_corner_cover=sum(len(r['covered_corners'])==12 for r in rows),fixed_star_histogram=dict(sorted(Counter(len(r['fixed_stars']) for r in rows).items())),dimer_corona_histogram=dict(sorted(Counter(len(r['dimer_endpoint_coronas']) for r in rows).items()))))
 p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args()
 if a.output:Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out['summary'],sort_keys=True))
if __name__=='__main__':main()
