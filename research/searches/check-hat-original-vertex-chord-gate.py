#!/usr/bin/env python3
"""Independent obstruction checker: four reflex corners force a matching."""
import json,sys,itertools
from fractions import Fraction as F
from pathlib import Path
c=json.loads(Path(sys.argv[1]).read_text())
s=json.loads(Path(c['source']).read_text())['hat_outline']
p=[(2*F(a[0]),2*F(b[1])) for a,b in s]
assert p==[tuple(q) for q in c['outline']]
def turn(a,b,z):return (b[0]-a[0])*(z[1]-b[1])-(b[1]-a[1])*(z[0]-b[0])
r=[i for i in range(len(p)) if turn(p[i-1],p[i],p[(i+1)%len(p)])<0]
assert len(p)==13 and r==[0,4,8,11]
# At most two chords by 5(d+1)<=13+2d. Every reflex needs an incident cut.
# Thus both chords have reflex endpoints and the four endpoints are distinct.
a,b,d,e=r
matchings=[((a,b),(d,e)),((a,d),(b,e)),((a,e),(b,d))]
proof=[]
for edges in matchings:
 (u,v),(w,z)=edges
 crossing=(u<w<v<z) or (w<u<z<v)
 if crossing:proof.append(dict(cuts=edges,reason='alternating endpoints'));continue
 # Each chord cuts off its boundary interval if that interval has no other chord.
 intervals=[list(range(u,v+1)),list(range(w,z+1))]
 short=min(intervals,key=len)
 # Also inspect complementary original-boundary chain.
 for u,v in edges:
  for chain in (list(range(u,v+1)),list(range(v,13))+list(range(u+1))):
   other=[x for edge in edges if edge!=(u,v) for x in edge]
   if not any(x in chain[1:-1] for x in other) and len(chain)<5:
    proof.append(dict(cuts=edges,reason='leaf face has fewer than five original vertices',leaf=chain));break
  else:continue
  break
 else:raise AssertionError('unexcluded matching')
assert len(proof)==3 and c['accepted_partitions']==[] and c['two_class_partitions']==[]
assert c['combinatorial_dissection_counts']==[1,65,1365]
print(json.dumps(dict(status='VALID',reflex_vertices=r,independent_obstruction=proof),indent=2))
