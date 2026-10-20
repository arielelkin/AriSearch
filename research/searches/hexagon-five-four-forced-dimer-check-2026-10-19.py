#!/usr/bin/env python3
"""Independent endpoint incidence and retained evidence checks."""
import json
from pathlib import Path
A=(0,1,2,0,3,4)
d=json.loads(Path('research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json').read_text())
assert len(d['rows'])==180
# A native side j has endpoints corners j-1 and j. The endpoint map
# is the involution exchanging those endpoints, independently of sign.
for f in range(2):
 for j in range(6):
  endpoints={6*f+(j-1)%6,6*f+j}
  for c in endpoints:
   other=next(iter(endpoints-{c}))
   formula=6*f+((j-1)%6 if c==6*f+j else j)
   assert other==formula
for r in d['rows']:
 W=(A,tuple(r['B']))
 assert all(w.count(3)==1 for w in W)
 assert not any(w[i]==w[(i+1)%6]==3 for w in W for i in range(6))
 S={tuple(map(tuple,t)) for t in r['fixed_stars']}
 def sides(p):
  c,h=p;f,i=divmod(c,6);z=(6*f+i,6*f+(i+1)%6)
  return z if h==1 else z[::-1]
 def other(p,s):
  c,h=p;f,j=divmod(s,6)
  endpoints={6*f+(j-1)%6,6*f+j}
  assert c in endpoints
  return (next(iter(endpoints-{c})),h)
 for t in S:
  for i,p in enumerate(t):
   q=t[(i+1)%3];s=sides(p)[1];v=sides(q)[0]
   assert W[s//6][s%6]==W[v//6][v%6]
   pair=(other(q,v),other(p,s))
   assert any(any((u[j],u[(j+1)%3])==pair for j in range(3)) for u in S)
   if s==v==5:assert p[1]==q[1] and {p[0],q[0]}=={4,5}
 for corona in r['boundary_coronas']:
  assert len(corona)==11 and corona[0]==corona[-1]
  for i,(slot,h) in enumerate(corona[:-1]):
   edge=(i-1)%5
   assert W[slot//6][slot%6]==A[edge]
fixture=next(r for r in d['rows'] if r['B']==[0,1,1,0,2,3])
assert len(fixture['fixed_stars'])==22
assert len(fixture['boundary_coronas'])==7
assert len(fixture['certain_transitions'])==2
print('PASS endpoint incidence, all180 fixed atlases, reflection obstruction, corona edge colors, explicit fixture')
