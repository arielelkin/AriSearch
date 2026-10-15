"""Independent exhaustive mixed-separation audit; no producer imports."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
C=json.loads((ROOT/'certificates/hexagon-mixed-separation-repeat-gate-2026-10-15.json').read_text())
A=(0,1,0,2,3,4); B=(2,0,3,2,4,1)

def incidence(words):
 ends={6*f+j:frozenset((6*f+(j-1)%6,6*f+j)) for f in range(2) for j in range(6)}
 colors={6*f+j:words[f][j] for f in range(2) for j in range(6)}
 ports={v:{colors[e]:e for e in ends if v in ends[e]} for v in range(12)}
 assert all(len(p)==2 for p in ports.values())
 stars=set()
 for triple in combinations(range(5),3):
  arms=list(map(frozenset,combinations(triple,2)))
  for cs in product(*(tuple(v for v,p in ports.items() if frozenset(p)==arm) for arm in arms)):
   stars.add(tuple(sorted(cs)))
 stars=sorted(stars)
 requirements={}
 for t in stars:
  req=[]
  for v,w in combinations(t,2):
   r,=ports[v].keys()&ports[w].keys()
   e,f=ports[v][r],ports[w][r]
   x,=ends[e]-{v}; y,=ends[f]-{w}
   req.append((v,w,r,x,y))
  requirements[t]=req
 return ends,colors,ports,stars,requirements

def completions(stars,x,y):
 return [t for t in stars if x!=y and {x,y}<=set(t)]
def fixed(words):
 ends,colors,ports,initial,req=incidence(words)
 current=initial; rounds=[]
 while True:
  nxt=[t for t in current if all(completions(current,x,y) for v,w,r,x,y in req[t])]
  if current==nxt:break
  rounds.append({'input':[list(t) for t in current],'output':[list(t) for t in nxt]}); current=nxt
 return ends,colors,ports,initial,req,current,rounds

def comps(edges):
 unseen=set(range(12)); blocks=[]
 while unseen:
  block={min(unseen)}
  while True:
   nxt=block|{v for e in edges if block&set(e) for v in e}
   if nxt==block:break
   block=nxt
  blocks.append(tuple(sorted(block))); unseen-=block
 return sorted(blocks)
raw=[(p,q[0],q[1],p,q[2],q[3]) for p in range(5) for q in permutations([x for x in range(5) if x!=p])]
assert len(raw)==120 and len(C['word_records'])==120
counts=[0,0,0]
for word,record in zip(raw,C['word_records']):
 ends,colors,ports,initial,req,stars,rounds=fixed((A,word))
 covered=sorted({v for t in stars for v in t})
 edges=sorted({tuple(sorted((ports[v][r],ports[w][r]))) for t in stars for v,w,r,x,y in req[t]})
 blocks=comps(edges)
 joined=[any({v,w}<=set(block) for block in blocks) for v,w in ((0,2),(6,9))]
 assert record['B']==list(word)
 assert record['initial_atlas']==list(map(list,initial))
 assert record['pruning_rounds']==rounds
 assert record['fixed_atlas']==list(map(list,stars))
 assert record['covered_corners']==covered
 assert record['fixed_seams']==list(map(list,edges))
 assert record['fixed_components']==list(map(list,blocks))
 assert record['repeated_joined']==joined
 if len(covered)<12:counts[0]+=1;assert record['hard_class_equivalence'] is None
 elif not all(joined):
  counts[1]+=1;assert record['hard_class_equivalence'] is None
  assert all(len({colors[e] for e in block})==1 for block in blocks)
  assert len({tuple(block) for block in blocks if set(block)&set(range(6))})>=5
  assert len({tuple(block) for block in blocks if set(block)&set(range(6,12))})>=5
 else:
  counts[2]+=1; eq=record['hard_class_equivalence'];assert eq is not None
  mapping={int(k):v for k,v in eq['color_map'].items()}
  assert set(mapping)==set(range(5))==set(mapping.values())
  assert tuple(mapping[A[(eq['A_shift']+eq['A_direction']*i)%6]] for i in range(6))==A
  assert tuple(mapping[word[(eq['B_shift']+eq['B_direction']*i)%6]] for i in range(6))==B
assert counts==[96,16,8]
print('PASS all120 words:96 no cover,16 disconnected repeated slots,8 explicitly equivalent hard words.')
ends,colors,ports,initial,req,stars,rounds=fixed((A,B))
assert len(stars)==12 and C['representative_fixed_atlas']==list(map(list,stars))
supports=[]
for bits in product((0,1),repeat=len(stars)):
 chosen=[t for t,b in zip(stars,bits) if b]
 if {v for t in chosen for v in t}!=set(range(12)):continue
 if all(completions(chosen,x,y) for t in chosen for v,w,r,x,y in req[t]):
  mask=sum(b<<i for i,b in enumerate(bits))
  supports.append((mask,chosen))
supports.sort()
assert len(supports)==30
assert C['representative_supports']==[dict(mask=m,stars=list(map(list,s))) for m,s in supports]
print('PASS independent2^12 exhaustive actual-support test:30 endpoint-closed full-corner covers.')

# Pairings generated from permutations, not the producer recursion.
def pairings(items):
 result=set()
 for p in permutations(items):
  pairs=tuple(sorted(tuple(sorted(p[i:i+2])) for i in range(0,len(p),2)))
  result.add(pairs)
 return sorted(result)

def topology(signs,pairs):
 alpha={a:b for a,b in pairs for a,b in ((a,b),(b,a))}
 sigma={6*f+k:6*f+(k+1)%6 for f in range(4) for k in range(6)}
 reached={0}
 while True:
  nxt=reached|{alpha[d]//6 for f in reached for d in range(6*f,6*f+6)}
  if nxt==reached:break
  reached=nxt
 if len(reached)<4:return None
 # Darts begin at their vertex. Across a reversed oriented edge, the
 # opposite dart begins at the far vertex, so next(alpha(d)) is same vertex.
 vertexperm={d:sigma[alpha[d]] for d in alpha}
 unseen=set(range(24));cycles=[]
 while unseen:
  orbit=[];d=min(unseen)
  while d not in orbit:
   orbit.append(d);d=vertexperm[d]
  assert d==orbit[0]
  unseen-=set(orbit);cycles.append(orbit)
 if len(cycles)!=8 or any(len(v)!=3 for v in cycles):return False
 native=[]
 for orbit in cycles:
  triple=[]
  for dart in orbit:
   f,k=divmod(dart,6)
   triple.append(6*(f//2)+(signs[f]*k-1)%6)
  native.append(tuple(sorted(triple)))
 return tuple(sorted(set(native))),sorted(native)
patterns=set();alln=connected=valid=0
for tail in product((1,-1),repeat=3):
 signs=(1,)+tail
 groups=[[6*f+k for f in range(4) for k in range(6) if (A,B)[f//2][k if signs[f]==1 else (-k-1)%6]==r] for r in range(5)]
 for pp in product(*(pairings(g) for g in groups)):
  alln+=1;pairs=sum(pp,())
  result=topology(signs,pairs)
  if result is None:continue
  connected+=1
  if result is False:continue
  valid+=1;patterns.add(result[0])
assert alln==48600 and valid==6 and len(patterns)==3
T=C['torus_atlas']
assert T['counts']==dict(all_pairings=alln,connected_pairings=connected,trivalent_tori=valid)
assert T['distinct_angle_supports']==3
assert {tuple(map(tuple,w['angle_support'])) for w in T['witnesses']}==patterns
for witness in T['witnesses']:
 signs=witness['signs']; pairs=witness['edge_pairs']
 assert len(pairs)==12 and sorted(v for p in pairs for v in p)==list(range(24))
 for a,b in pairs:
  f,k=divmod(a,6);g,l=divmod(b,6)
  assert (A,B)[f//2][k if signs[f]==1 else (-k-1)%6]==(A,B)[g//2][l if signs[g]==1 else (-l-1)%6]
 result=topology(signs,pairs)
 assert result and result[0]==tuple(map(tuple,witness['angle_support']))
 assert result[1]==list(map(tuple,witness['vertex_triples']))
print('PASS all48600 independent signed face-pairings, connected vertex-cycle topology,6 tori/3patterns.')

def row(t):return [Q(t.count(i)) for i in range(12)]+[Q(2)]
poly=[[Q(i//6==f) for i in range(12)]+[Q(4)] for f in range(2)]
lookup=dict(supports);seen=set();nrows=0
for record in C['covered_supports']:
 source=record['source'];m=source['mask'];ss=lookup[m]
 assert m not in seen and source['stars']==list(map(list,ss));seen.add(m)
 rows=poly+[row(t) for t in ss]
 target=T['witnesses'][record['torus_index']]['angle_support']
 assert len(target)==len(record['row_combinations'])==4
 for t,coeff in zip(target,record['row_combinations']):
  assert len(coeff)==len(rows)
  assert [sum(Q(c)*r[j] for c,r in zip(coeff,rows)) for j in range(13)]==row(t)
  nrows+=1
partition=[(0,2,11),(1,5,10),(3,6,7),(4,8,9)]
exception=[]
for record in C['exceptional_supports']:
 source=record['source'];m=source['mask'];ss=lookup[m]
 assert m not in seen and source['stars']==list(map(list,ss));seen.add(m);exception.append(ss)
assert len(seen)==30 and nrows==112
assert exception==[partition,partition+[(6,7,8),(9,10,11)]]
assert sorted(v for t in partition for v in t)==list(range(12))
for edge in range(12):
 v=edge; color=colors[edge]
 star,=[t for t in partition if v in t]
 candidates=[w for w in star if w!=v and color in ports[w]]
 w,=candidates;mate=ports[w][color]
 x,=ends[edge]-{v};y,=ends[mate]-{w}
 assert len(completions(partition,x,y))==1
# Opposite repeated B sides bound the two complementary pure-B angle triples.
assert B[0]==B[3] and len(set(B))==5
assert [(i in (6,7,8))+(i in (9,10,11)) for i in range(6,12)]==[1]*6
print('PASS112 Fraction identities, exhaustive30-cover partition,12 indexed native maps, complementary pureB triples.')

# Explicit mono-B two-face torus: independently compute all vertex links.
pairs=[(0,3),(6,9)]+[(j,6+j) for j in (1,2,4,5)]
alpha={a:b for a,b in pairs for a,b in ((a,b),(b,a))}
sigma={6*f+k:6*f+(k+1)%6 for f in range(2) for k in range(6)}
vp={d:sigma[alpha[d]] for d in range(12)}
unseen=set(range(12));cycles=[]
while unseen:
 d=min(unseen);orb=[]
 while d not in orb:orb.append(d);d=vp[d]
 assert d==orb[0];unseen-=set(orb);cycles.append(orb)
assert len(cycles)==4 and all(len(t)==3 for t in cycles)
assert sorted(tuple(sorted((d-1)%6 for d in t)) for t in cycles)==[(0,1,2),(0,1,2),(3,4,5),(3,4,5)]
assert all(B[a%6]==B[b%6] for a,b in pairs)
print('PASS monoB2face torus:4 circular triple links,exact complementary angles,V4E6F2.')
