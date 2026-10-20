#!/usr/bin/env python3
"""Exact literal carrier checker; no search, no solver, no metric assumption."""
import json
from pathlib import Path
W=((0,1,2,0,3,4),(0,1,1,0,2,3))
# Faces 0,1 are A positive; 2,3 are B negative. All indices native.
P=[(0,0,2,0),(1,0,3,0),(0,1,3,2),(1,1,2,2),
   (0,2,2,4),(1,2,3,4),(0,4,3,5),(1,4,2,5),
   (0,3,1,3),(0,5,1,5),(2,1,3,1),(2,3,3,3)]
H=(1,1,-1,-1)
assert sorted((f,i) for a in P for f,i in ((a[0],a[1]),(a[2],a[3])))==[(f,i) for f in range(4) for i in range(6)]
adj={i:[] for i in range(24)}; dual={f:set() for f in range(4)}
for f,i,g,j in P:
 assert W[f//2][i]==W[g//2][j]
 dual[f].add(g);dual[g].add(f)
 # Native side i starts at corner i-1 and ends at corner i.
 # Opposite signs: same native endpoints; equal signs: reverse endpoints.
 ends=[(i,j),((i-1)%6,(j-1)%6)] if H[f]!=H[g] else [(i,(j-1)%6),((i-1)%6,j)]
 for a,b in ends:adj[6*f+a].append(6*g+b);adj[6*g+b].append(6*f+a)
assert all(len(v)==2 for v in adj.values())
left=set(adj);links=[]
while left:
 start=min(left);cycle=[];prev=None;cur=start
 while cur not in cycle:
  cycle.append(cur);nxt=next(v for v in adj[cur] if v!=prev);prev,cur=cur,nxt
 assert cur==start
 left.difference_update(cycle);links.append(cycle)
T={(0,6,7),(1,8,9),(2,3,10),(4,5,11)}
triples=[tuple(sorted(6*(x//12)+x%6 for x in c)) for c in links]
assert len(links)==8 and all(len(c)==3 for c in links)
assert set(triples)==T and all(triples.count(t)==2 for t in T)
seen={0}
while True:
 nxt=seen|set().union(*(dual[f] for f in seen))
 if nxt==seen:break
 seen=nxt
assert len(seen)==4
assert len(links)-len(P)+4==0
out={"schema":"MASK33416_NATIVE_TORUS_V1","words":W,"handedness":H,"native_edge_pairs":P,"native_corner_links":[[[x//6,x%6] for x in c] for c in links],"unsigned_triples":triples,"topology":{"connected":True,"orientable":True,"V":8,"E":12,"F":4,"Euler":0},"scope":"One literal carrier; arbitrary closed strictly convex metrics satisfying four angle identities. No enumeration or solver."}
root=Path(__file__).resolve().parents[2]
(root/'research/certificates/hexagon-five-four-mask33416-carrier-sol-2026-10-19.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
