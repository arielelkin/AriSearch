"""Exact finite triangulation preflight for P parent 7P+Q7, five simple boundary children."""
from sage.all import Graph
from collections import deque
from itertools import combinations
G=Graph();G.add_cycle(range(7))
for i in range(7):G.add_edge(7,i);G.add_edge(8,i)
G=G.canonical_label();key=G.graph6_string();seen={key};queue=deque([G]);survivors=[]
while queue:
 G=queue.popleft()
 assert G.order()==9 and G.size()==21 and G.is_planar()
 for O in G:
  if G.degree(O)!=5:continue
  boundary=set(G.neighbors(O));interior=set(G)-boundary-{O}
  if any(G.degree(v)!=5 for v in interior):continue
  if sorted(G.degree(v) for v in boundary)!=[4,4,4,4,6]:continue
  Q=next(v for v in boundary if G.degree(v)==6)
  survivors.append((G.graph6_string(),O,Q,sorted(boundary),sorted(interior),G.edges(labels=False)))
 for u,v in G.edges(labels=False):
  cn=set(G.neighbors(u))&set(G.neighbors(v))
  for a,b in combinations(sorted(cn),2):
   if G.has_edge(a,b):continue
   H=G.copy();H.delete_edge(u,v);H.add_edge(a,b)
   if not H.is_planar():continue
   H=H.canonical_label();key=H.graph6_string()
   if key not in seen:seen.add(key);queue.append(H)
print('FLIP_CONNECTED_TRIANGULATIONS',len(seen))
print('ROOTED_SURVIVORS',len(survivors))
for record in survivors:print(record)
