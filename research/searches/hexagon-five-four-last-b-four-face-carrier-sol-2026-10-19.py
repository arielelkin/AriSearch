#!/usr/bin/env python3
"""Exhaustive finite four-face carrier gate, native corner at side END.
No floating point, solver, geometry assumption, or larger-carrier conclusion.
"""
import itertools,json
W=((0,1,2,0,3,4),(0,1,2,0,3,1))
T={(0,1,8),(2,7,11),(3,6,10),(4,5,9)}
def matchings(xs):
 if not xs:yield [];return
 a=xs[0]
 for k in range(1,len(xs)):
  for rest in matchings(xs[1:k]+xs[k+1:]):yield [(a,xs[k])]+rest
G=[list(matchings([6*f+i for f in range(4) for i in range(6) if W[f//2][i]==c])) for c in range(5)]
n=0
for signs in itertools.product((1,-1),repeat=3):
 H=(1,)+signs
 for groups in itertools.product(*G):
  n+=1;P=sum(groups,[]);pa=list(range(24));adj=[[] for _ in range(24)]
  def root(x):
   while pa[x]!=x:x=pa[x]
   return x
  for x,y in P:
   f,i=divmod(x,6);g,j=divmod(y,6)
   ends=((i,j),((i-1)%6,(j-1)%6)) if H[f]!=H[g] else ((i,(j-1)%6),((i-1)%6,j))
   for a,b in ends:
    u,v=6*f+a,6*g+b;pa[root(u)]=root(v);adj[u].append(v);adj[v].append(u)
  C={}
  for x in range(24):C.setdefault(root(x),[]).append(x)
  if len(C)!=8 or any(len(c)!=3 for c in C.values()):continue
  rows=[tuple(sorted(6*(x//12)+x%6 for x in c)) for c in C.values()]
  if set(rows)!=T or any(rows.count(t)!=2 for t in T):continue
  seen={0}
  for _ in range(4):
   for x,y in P:
    f,g=x//6,y//6
    if f in seen or g in seen:seen.update((f,g))
  if len(seen)!=4:continue
  print(json.dumps(dict(count=n,H=H,pairs=P,links=list(C.values()))));raise SystemExit
assert n==113400
print('EXHAUSTED: 113400 labeled pairing/handedness candidates; no requested four-face carrier')
