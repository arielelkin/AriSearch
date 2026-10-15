#!/usr/bin/env python3
"""Exact eight-word formal-ring/angle/endpoint gate; no placement search."""
from itertools import combinations,product
from collections import defaultdict,Counter
import json
from pathlib import Path
import z3
A=tuple(range(6))
REPS=[(0,2,0,3,6,4),(0,2,4,6,5,6),(0,2,0,3,5,6),
(0,2,0,3,1,4),(0,1,4,2,5,2),(0,1,5,2,4,2),
(0,1,0,2,5,3),(0,1,5,1,4,2)]
def corners(words):
 loc=defaultdict(list)
 for f,w in enumerate(words):
  for i in range(6):loc[frozenset((w[i],w[(i+1)%6]))].append(6*f+i)
 return loc

def stars(words):
 loc=corners(words);out=[]
 for tri in combinations(set().union(*map(set,words)),3):
  es=[frozenset(e) for e in combinations(tri,2)]
  if all(e in loc for e in es):out.extend(tuple(sorted(cs)) for cs in product(*(loc[e] for e in es)))
 return sorted(set(out))

def ring_choices(B):
 out=[]
 common=sorted(set(A)&set(B))
 for retained in combinations(common,4):
  for slots in product(*[[i for i,b in enumerate(B) if b==x] for x in retained]):
   aw=[('A',i) for i in range(6)];bw=[('B',i) for i in range(6)]
   for x,j in zip(retained,slots):aw[x]=bw[j]=('C',x)
   ss=stars((aw,bw))
   if len(ss)==4 and Counter(c for s in ss for c in s)==Counter(range(12)):
    out.append((tuple(zip(retained,slots)),ss))
 return out

def far_corner(c,symbol,words):
 f,i=divmod(c,6);w=words[f]
 if w[i]==symbol:return 6*f+(i-1)%6
 assert w[(i+1)%6]==symbol
 return 6*f+(i+1)%6

def run(B,endpoint,branching=False):
 words=(A,B);ss=stars(words);rings=ring_choices(B)
 solver=z3.Solver();solver.set(timeout=60000)
 angles=[z3.Real('angle%d'%i) for i in range(12)]
 active=[z3.Bool('active%d'%i) for i in range(len(ss))]
 eq=[sum(angles[c] for c in s)==2 for s in ss]
 solver.add(*(z3.And(a>0,a<1) for a in angles))
 solver.add(sum(angles[:6])==4,sum(angles[6:])==4)
 for a,e in zip(active,eq):solver.add(z3.Implies(a,e))
 for c in range(12):solver.add(z3.Or(*[a for a,s in zip(active,ss) if c in s]))
 for _,ring in rings:solver.add(z3.Not(z3.And(*[sum(angles[c] for c in s)==2 for s in ring])))
 if endpoint:
  for a,s in zip(active,ss):
   for c,d in combinations(s,2):
    fc,ic=divmod(c,6);fd,id_=divmod(d,6)
    shared=set((words[fc][ic],words[fc][(ic+1)%6]))&set((words[fd][id_],words[fd][(id_+1)%6]))
    assert len(shared)==1
    x,=shared;pair={far_corner(c,x,words),far_corner(d,x,words)}
    # If the two far corners have the same index, they are two actual
    # copies of that corner: no triangle-star can contain that twice.
    possible=[] if len(pair)<2 else [active[j] for j,t in enumerate(ss) if pair<=set(t)]
    solver.add(z3.Implies(a,z3.Or(*possible)))
 if branching:
  solver.add(z3.Or(*[z3.PbGe([(a,1) for a,s in zip(active,ss) if c in s],2) for c in range(12)]))
 status=solver.check();row={'B':list(B),'stars':[list(s) for s in ss],
 'rings':[{'matches':list(m),'stars':s} for m,s in rings],
 'endpoint_constraints':endpoint,'require_branching':branching,'status':str(status)}
 if status==z3.sat:
  model=solver.model();row['angles_pi']=[str(model.eval(a)) for a in angles]
  row['active']=[s for a,s in zip(active,ss) if z3.is_true(model.eval(a))]
 if status==z3.unknown:row['reason']=solver.reason_unknown()
 return row
def fourface_twists(B):
 """Explicit two-copy construction; no shapes/angles enumerated.
 Cross-type pair the four selected length slots, pair A-private slots
 across copies, and test the three perfect matchings of four repeated
 B-private side occurrences. Orientations are A forward and B reversed.
 """
 results=[]
 for matches,_ in ring_choices(B):
  retained={x for x,j in matches};bselected={j for x,j in matches}
  bp=[j for j in range(6) if j not in bselected]
  if B[bp[0]]!=B[bp[1]]:continue
  aprivate=[j for j in range(6) if j not in retained]
  # Side coordinates use ORIGINAL indices; next/previous vertex reverse
  # for B because its boundary orientation is reversed.
  def ends(f,j):return ((j-1)%6,j) if f<2 else (j,(j-1)%6)
  def node(f,c):return 6*f+c
  private_nodes=[(f,j) for f in (2,3) for j in bp]
  a,b,c,d=private_nodes
  matchings=[[(a,b),(c,d)],[(a,c),(b,d)],[(a,d),(b,c)]]
  for bits in product((0,1),repeat=4):
   for private in matchings:
    pairs=[((0,j),(1,j)) for j in aprivate]+private
    for (x,j),bit in zip(matches,bits):
     pairs.extend([((i,x),(2+(i^bit),j)) for i in (0,1)])
    par=list(range(24))
    def find(x):
     while par[x]!=x:par[x]=par[par[x]];x=par[x]
     return x
    def join(x,y):par[find(x)]=find(y)
    for (f,j),(g,k) in pairs:
     u,v=ends(f,j);w,z=ends(g,k)
     join(node(f,u),node(g,z));join(node(f,v),node(g,w))
    groups=defaultdict(list)
    for f in range(4):
     for j in range(6):groups[find(node(f,j))].append((f,j))
    if len(groups)!=8 or any(len(cs)!=3 for cs in groups.values()):continue
    adj={i:set() for i in range(4)}
    for (f,j),(g,k) in pairs:adj[f].add(g);adj[g].add(f)
    reached={0}
    for _ in range(4):reached|={v for u in reached for v in adj[u]}
    if len(reached)!=4:continue
    actual=Counter(tuple(sorted((0 if f<2 else 6)+j for f,j in cs)) for cs in groups.values())
    # Return only four triple kinds, each twice: the same input needed
    # by the standard four-triangle angle argument.
    if len(actual)==4 and set(actual.values())=={2}:
     results.append({'matches':matches,'bits':bits,'private_pairs':private,
       'pairs':pairs,'stars':sorted(actual)})
 return results

if __name__=='__main__':
 rows=[]
 for B in REPS:
  for endpoint,branching in ((False,False),(True,False),(True,True)):
   row=run(B,endpoint,branching);rows.append(row)
   print(B,'endpoint',endpoint,'branching',branching,'stars',len(row['stars']),'rings',len(row['rings']),row['status'],flush=True)
 Path('research/certificates/hexagon-six-five-angle-gate-2026-10-15.json').write_text(json.dumps({'domain':'eight specified D6 representatives, angle and endpoint overapproximation','rows':rows,'twisted_fourface':{','.join(map(str,B)):fourface_twists(B) for B in REPS}},indent=2)+'\n')
