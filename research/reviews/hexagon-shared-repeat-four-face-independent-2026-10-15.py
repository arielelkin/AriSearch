"""Independent fixed 68,040 gluing atlas audit, using vertex-link permutations.
No producer imports, no geometric angle feasibility, no solver.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import json
WORDS=((0,1,0,2,3,4),(0,3,0,2,1,4))
# Generate perfect matchings by quotienting permutations, independently
# of the producer's recursive pair selection.
def pair_patterns(n):
 out=set()
 for p in permutations(range(n)):
  out.add(tuple(sorted(tuple(sorted(p[k:k+2])) for k in range(0,n,2))))
 return sorted(out)
P8=pair_patterns(8);P4=pair_patterns(4)
assert len(P8)==105 and len(P4)==3

def analyze(signs,pairs):
 mate={}
 adjacency={f:set() for f in range(4)}
 for a,b in pairs:
  assert a!=b and a not in mate and b not in mate
  mate[a]=b;mate[b]=a
  adjacency[a//6].add(b//6);adjacency[b//6].add(a//6)
 assert set(mate)==set(range(24))
 reached={0}
 while True:
  more=reached|{g for f in reached for g in adjacency[f]}
  if more==reached:break
  reached=more
 if len(reached)<4:return None
 unseen=set(range(24));links=[]
 while unseen:
  start=min(unseen);current=start;cycle=[]
  while current not in cycle:
   assert current in unseen
   unseen.remove(current);cycle.append(current)
   f,k=divmod(current,6)
   current=mate[6*f+(k-1)%6]
  assert current==start
  links.append(cycle)
 if len(links)!=8 or any(len(cycle)!=3 for cycle in links):return ()
 # All 24 vertex sectors accounted for, each circular link trivalent.
 # Orientable closed connected surface: 8-12+4=0, hence torus.
 triples=[]
 for cycle in links:
  corners=[]
  for c in cycle:
   f,k=divmod(c,6)
   corners.append(6*(f//2)+(signs[f]*k-1)%6)
  triples.append(tuple(sorted(corners)))
 return tuple(sorted(triples))

counts=Counter();signatures=set();gluings=set()
for tail in product((1,-1),repeat=3):
 signs=(1,)+tail
 groups={color:[] for color in range(5)}
 for face in range(4):
  for k in range(6):
   native_side=k if signs[face]==1 else (-k-1)%6
   groups[WORDS[face//2][native_side]].append(6*face+k)
 for patterns in product(P8,P4,P4,P4,P4):
  pairs=tuple((groups[color][a],groups[color][b]) for color,pattern in enumerate(patterns) for a,b in pattern)
  counts['all_pairings']+=1
  links=analyze(signs,pairs)
  if links is None:continue
  counts['connected_pairings']+=1
  if not links:continue
  counts['trivalent_tori']+=1
  signature=tuple(sorted(set(links)))
  signatures.add(signature)
  gluings.add((signs,tuple(sorted(tuple(sorted(p)) for p in pairs))))
assert counts==dict(all_pairings=68040,connected_pairings=67824,trivalent_tori=12)
assert len(signatures)==6
path=Path(__file__).resolve().parents[1]/'certificates/hexagon-shared-repeat-four-face-atlas-2026-10-15.json'
cert=json.loads(path.read_text())
assert cert['A']==list(WORDS[0]) and cert['B']==list(WORDS[1])
assert cert['counts']==dict(counts) and cert['distinct_angle_supports']==6
assert len(cert['witnesses'])==6
retained=set()
for witness in cert['witnesses']:
 signs=tuple(witness['signs']);pairs=tuple(tuple(p) for p in witness['edge_pairs'])
 assert (signs,tuple(sorted(tuple(sorted(p)) for p in pairs))) in gluings
 links=analyze(signs,pairs)
 assert links==tuple(tuple(t) for t in witness['vertex_triples'])
 signature=tuple(sorted(set(links)))
 assert signature==tuple(tuple(t) for t in witness['angle_support'])
 assert signature not in retained
 retained.add(signature)
assert retained==signatures
print('PASS fixed4face domain:68,040 pairings,67,824 connected,12 circular-link trivalent tori,6 native angle supports; all retained witnesses independently checked.')
