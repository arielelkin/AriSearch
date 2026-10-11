"""Fresh complete native matching orbit audit, no author imports."""
from itertools import combinations,permutations
from pathlib import Path
import json

def normalize(p):return tuple(sorted(p))
def reflectP(p):return normalize((3-i,j) for i,j in p)
def reflectQ(p):return normalize((i,3-j) for i,j in p)
def swap(p):return normalize((j,i) for i,j in p)
def orbit(p):
 seen={p};todo=[p]
 while todo:
  a=todo.pop()
  for operation in (reflectP,reflectQ,swap):
   b=operation(a)
   if b not in seen:seen.add(b);todo.append(b)
 return seen
all_patterns={normalize(zip(ps,qs)) for ps in combinations(range(4),2) for qi in combinations(range(4),2) for qs in permutations(qi)}
assert len(all_patterns)==72
# The swap conjugates the two independent native reflections.
assert all(swap(reflectP(p))==reflectQ(swap(p)) for p in all_patterns)
assert all(reflectP(reflectQ(p))==reflectQ(reflectP(p)) for p in all_patterns)
assert any(swap(reflectP(p))!=reflectP(swap(p)) for p in all_patterns)
expected={};remaining=set(all_patterns)
while remaining:
 o=orbit(min(remaining));assert o<=all_patterns
 expected[min(o)]=o;remaining-=o
assert len(expected)==13
D=json.loads(Path('research/certificates/partial-contact-cairo-two-cross-native-orbits.json').read_text())
assert len(D)==13
retained={}
for record in D:
 c=normalize(tuple(p) for p in record['canonical']);ps={normalize(tuple(p) for p in pattern) for pattern in record['native_patterns']}
 assert c==min(ps) and c not in retained and len(ps)==len(record['native_patterns'])
 assert ps==expected[c];retained[c]=ps
assert retained==expected and sum(map(len,retained.values()))==72
assert min(orbit(((0,2),(2,0))))==((0,1),(2,3))
assert min(orbit(((1,3),(2,0))))==((0,1),(3,2))
print('PASS complete72 injective two-cross native matchings in13 exact retained symmetry orbits; orbit sizes',[len(expected[k]) for k in sorted(expected)],'; both named periodic representative orbit mappings.')
