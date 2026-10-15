#!/usr/bin/env python3
"""Small independent arithmetic checker for retained rational row combinations.
Does not trust Gaussian elimination, Sage, Z3, or the certificate producer.
The finite support enumeration is a separate verification obligation.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'research/certificates/hexagon-six-four-double-pair-certificate-2026-10-15.json'
A=tuple(range(6))
def equation(st):return [F(st.count(i)) for i in range(12)]+[F(-2)]
def formal_rings(B):
 out=set()
 for chosen in combinations(range(6),4):
  matched=[B[j] for j in chosen]
  if len(set(matched))<4:continue
  wa=[('C',x) if x in matched else ('A',x) for x in A]
  wb=[('C',x) if j in chosen else ('B',j) for j,x in enumerate(B)]
  slots=defaultdict(list)
  for base,w in ((0,wa),(6,wb)):
   for j in range(6):slots[frozenset((w[j],w[(j+1)%6]))].append(base+j)
  if len(slots)!=12 or any(len(v)!=1 for v in slots.values()):continue
  triangles=[]
  for xyz in combinations(set(wa)|set(wb),3):
   pairs=[frozenset(e) for e in combinations(xyz,2)]
   if all(p in slots for p in pairs):triangles.append(tuple(sorted(slots[p][0] for p in pairs)))
  if len(triangles)==4 and Counter(c for t in triangles for c in t)==Counter(range(12)):
   out.add(tuple(sorted(triangles)))
 return out

def main():
 data=json.loads(CERT.read_text());checked=direct=records=0
 assert data['schema']=='HEXAGON_A6_B2211_ALL_SHARED_V1'
 for case in data['cases']:
  for record in case['records']:
   records+=1;rings=formal_rings(record['B'])
   assert sorted(Counter(record['B']).values())==[1,1,2,2]
   assert {tuple(sorted(tuple(t) for t in ring)) for ring in record['formal_rings']}==rings
   for cover in record['endpoint_closed_covers']:
    stars=[tuple(st) for st in cover['stars']];witness=cover['witness']
    assert all(st in [tuple(x) for x in record['pruned_stars']] for st in stars)
    if witness['kind']=='direct_ring':
     ring=tuple(sorted(tuple(st) for st in witness['ring']))
     assert ring in rings and set(ring)<=set(stars)
     direct+=1;continue
    assert witness['kind']=='rational_span'
    cert=witness['certificate'];assert stars==[tuple(st) for st in cert['source_stars']]
    actual=tuple(sorted(tuple(st) for st in cert['ring']));assert actual in rings
    rows=[[F(int(i<6)) for i in range(12)]+[F(-4)],
          [F(int(i>=6)) for i in range(12)]+[F(-4)]]+[equation(st) for st in stars]
    assert len(cert['row_combinations'])==4
    for st,coefficients in zip(cert['ring'],cert['row_combinations']):
     coefficients=list(map(F,coefficients));assert len(coefficients)==len(rows)
     assert [sum(c*r[j] for c,r in zip(coefficients,rows)) for j in range(13)]==equation(st)
    checked+=1
 assert (records,direct,checked)==(24,71,22)
 print('PASS: 24 words, 71 direct-ring supports, 22 exact rational ring-equation certificates; formal ring slots independently reconstructed from narrow stdlib-only proof record.')
if __name__=='__main__':main()
