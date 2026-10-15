"""Independent common-five both-opposite audit; no author-module imports."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
C=json.loads((ROOT/'certificates/hexagon-both-opposite-repeat-gate-2026-10-15.json').read_text())
A=(0,1,2,0,3,4)
REPS=((0,1,2,0,3,4),(0,1,2,0,4,3),(0,1,3,0,2,4),(0,1,4,0,3,2))
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
 current=[t for t in initial if len({v//6 for v in t})==2]; rounds=[]
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
@lru_cache(None)
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

raw=[(p,q[0],q[1],p,q[2],q[3]) for p in range(5) for q in permutations([x for x in range(5) if x!=p])]
assert len(raw)==len(C['word_records'])==120
assert C['A']==list(A)
assert C['hard_representatives']==list(map(list,REPS))
counts=[0,0,0];hardcounts=[0]*4
for word,record in zip(raw,C['word_records']):
 ends,colors,ports,full,req,stars,rounds=fixed((A,word))
 mixed=[t for t in full if len({v//6 for v in t})==2]
 assert [t for t in full if len({v//6 for v in t})==1]==[(0,1,2),(3,4,5),(6,7,8),(9,10,11)]
 covered=sorted({v for t in stars for v in t})
 edges=sorted({tuple(sorted((ports[v][r],ports[w][r]))) for t in stars for v,w,r,x,y in req[t]})
 blocks=comps(edges)
 joined=[any({v,w}<=set(block) for block in blocks) for v,w in ((0,3),(6,9))]
 assert record['B']==list(word)
 assert record['full_atlas']==list(map(list,full))
 assert record['mixed_atlas']==list(map(list,mixed))
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
  assert all(len([block for block in blocks if set(block)&set(range(6*f,6*f+6))])>=5 for f in range(2))
 else:
  counts[2]+=1;eq=record['hard_class_equivalence'];target=record['hard_representative']
  assert eq is not None and target in range(4);hardcounts[target]+=1
  mapping={int(k):v for k,v in eq['color_map'].items()}
  assert set(mapping)==set(range(5))==set(mapping.values())
  assert tuple(mapping[A[(eq['A_shift']+eq['A_direction']*i)%6]] for i in range(6))==A
  assert tuple(mapping[word[(eq['B_shift']+eq['B_direction']*i)%6]] for i in range(6))==REPS[target]
assert counts==[80,24,16] and hardcounts==[4,4,4,4]
def readings(word):
 return {tuple(word[(shift+direction*i)%6] for i in range(6)) for shift in range(6) for direction in (1,-1)}
orbits=[]
for rep in REPS:
 orbit=set()
 for cmap in permutations(range(5)):
  if A in readings(tuple(cmap[v] for v in A)):
   orbit|=readings(tuple(cmap[v] for v in rep))&set(raw)
 assert len(orbit)==4;orbits.append(orbit)
assert all(not x&y for x,y in combinations(orbits,2))
assert set.union(*orbits)=={tuple(r['B']) for r in C['word_records'] if r['hard_representative'] is not None}
print('PASS all120 raw opposite-repeat words,full/mixed atlases,pruning,seams,80/24/16 split,explicit4class equivalences.')

def row(t):return [Q(t.count(i)) for i in range(12)]+[Q(2)]
poly=[[Q(i//6==f) for i in range(12)]+[Q(4)] for f in range(2)]
nrows=0;supportcounts=[];coveredcounts=[];exceptioncounts=[]
for ci,(B,cl) in enumerate(zip(REPS,C['classes'])):
 assert cl['B']==list(B)
 ends,colors,ports,full,req,stars,rounds=fixed((A,B))
 assert cl['fixed_atlas']==list(map(list,stars))
 supports=[]
 for m in range(1<<len(stars)):
  chosen=[t for i,t in enumerate(stars) if m>>i&1]
  if {v for t in chosen for v in t}!=set(range(12)):continue
  if all(completions(chosen,x,y) for t in chosen for v,w,r,x,y in req[t]):supports.append((m,chosen))
 assert cl['supports']==[dict(mask=m,stars=list(map(list,s))) for m,s in supports]
 supportcounts.append(len(supports))
 T=cl['torus_atlas']
 if T is not None:
  patterns=set();alln=connected=valid=0
  for tail in product((1,-1),repeat=3):
   signs=(1,)+tail
   groups=[tuple(6*f+k for f in range(4) for k in range(6) if (A,B)[f//2][k if signs[f]==1 else (-k-1)%6]==r) for r in range(5)]
   for pp in product(*(pairings(g) for g in groups)):
    alln+=1;pairs=sum(pp,())
    result=topology(signs,pairs)
    if result is None:continue
    connected+=1
    if result is False:continue
    valid+=1;patterns.add(result[0])
  assert alln==68040
  assert T['counts']==dict(all_pairings=alln,connected_pairings=connected,trivalent_tori=valid)
  assert T['distinct_angle_supports']==len(patterns)
  assert {tuple(map(tuple,w['angle_support'])) for w in T['witnesses']}==patterns
  for witness in T['witnesses']:
   signs=witness['signs'];pairs=witness['edge_pairs']
   assert len(pairs)==12 and sorted(v for p in pairs for v in p)==list(range(24))
   for a,b in pairs:
    f,k=divmod(a,6);g,l=divmod(b,6)
    assert (A,B)[f//2][k if signs[f]==1 else (-k-1)%6]==(A,B)[g//2][l if signs[g]==1 else (-l-1)%6]
   result=topology(signs,pairs)
   assert result and result[0]==tuple(map(tuple,witness['angle_support']))
   assert result[1]==list(map(tuple,witness['vertex_triples']))
  print('PASS class',ci,'all68040 independent pairings,',valid,'tori/',len(patterns),'angle patterns')
 else:assert len(stars)==4
 lookup=dict(supports);seen=set()
 for record in cl['covered_supports']:
  source=record['source'];m=source['mask'];ss=lookup[m]
  assert m not in seen and source['stars']==list(map(list,ss));seen.add(m)
  rows=poly+[row(t) for t in ss]
  target=T['witnesses'][record['torus_index']]['angle_support']
  assert len(target)==len(record['row_combinations'])==4
  for t,coeff in zip(target,record['row_combinations']):
   assert len(coeff)==len(rows)
   assert [sum(Q(c)*r[j] for c,r in zip(coeff,rows)) for j in range(13)]==row(t)
   nrows+=1
 coveredcounts.append(len(cl['covered_supports']))
 for record in cl['exceptional_supports']:
  source=record['source'];m=source['mask'];ss=lookup[m]
  assert m not in seen and source['stars']==list(map(list,ss));seen.add(m)
  escape=record['frame_escape']
  cnt=[sum(v in t for t in ss) for v in range(12)]
  if escape['kind']=='all_native_corners_unique':
   assert cnt==[1]*12
   for edge in range(12):
    v=edge;color=colors[edge];star,=[t for t in ss if v in t]
    w,=[w for w in star if w!=v and color in ports[w]]
    mate=ports[w][color]
    x,=ends[edge]-{v};y,=ends[mate]-{w}
    assert len(completions(ss,x,y))==1
  else:
   assert escape['kind']=='all_AAB_with_unique_singleton_species_corners'
   unique=escape['unique_species'];other=1-unique
   assert all(sum(v//6==unique for v in t)==1 for t in ss)
   assert cnt[6*unique:6*unique+6]==[1]*6
   # All unique-species sides meet other-species tiles, with complete
   # deterministic indexed maps at both endpoints, not merely colors.
   for e in range(6*unique,6*unique+6):
    color=colors[e];guests=[]
    for v in sorted(ends[e]):
     star,=[t for t in ss if v in t]
     w,=[w for w in star if w!=v and color in ports[w]]
     assert w//6==other;guests.append((w,ports[w][color]))
    assert guests[0][1]==guests[1][1] and guests[0][0]!=guests[1][0]
   maps=[]
   for local in range(6):
    e=6*other+local;color=colors[e];guests=[]
    for v in (6*other+(local-1)%6,6*other+local):
     possible={(w,ports[w][color]) for t in ss if v in t for w in t if w//6==unique and color in ports[w]}
     assert len(possible)==1;guests.append(next(iter(possible)))
    assert guests[0][1]==guests[1][1] and guests[0][0]!=guests[1][0]
    maps.append(dict(other_side=local,guest_side=guests[0][1],guest_endpoint_corners=list(map(list,guests))))
   assert escape['conditional_other_to_unique_maps']==maps
   assert escape['other_state']=='parity of alternating sides incident to unique species'
  print('PASS class',ci,'exceptionmask',m,escape['kind'],'native endpoint maps')
 exceptioncounts.append(len(cl['exceptional_supports']))
 assert seen==set(lookup)
assert supportcounts==[141,1,27,57] and coveredcounts==[139,0,25,57] and exceptioncounts==[2,1,2,0]
assert nrows==C['summary']['exact_row_identities']==884
# Recheck universal opposite-repeat monohedral torus topology separately.
pairs=[(0,3),(6,9)]+[(j,6+j) for j in (1,2,4,5)]
alpha={a:b for a,b in pairs for a,b in ((a,b),(b,a))}
sigma={6*f+k:6*f+(k+1)%6 for f in range(2) for k in range(6)}
vp={d:sigma[alpha[d]] for d in range(12)};unseen=set(range(12));cycles=[]
while unseen:
 d=min(unseen);orb=[]
 while d not in orb:orb.append(d);d=vp[d]
 assert d==orb[0];unseen-=set(orb);cycles.append(orb)
assert len(cycles)==4 and all(len(t)==3 for t in cycles)
assert sorted(tuple(sorted((d-1)%6 for d in t)) for t in cycles)==[(0,1,2),(0,1,2),(3,4,5),(3,4,5)]
for word in (A,)+REPS:assert all(word[a%6]==word[b%6] for a,b in pairs)
print('PASS226 exhaustive supports,221 torus escapes,884 exact Fraction row identities,5 frame escapes,and monohedral torus.')
