#!/usr/bin/env python3
"""Finite AA22partner native sides0/1/2 (all01)*2 endpointorientations*4 thirdAoffers perend=96.
All64 AAA native cycles independently retained;all203 actual sidepartitions.
Ifevery two-endedcross forces monohedral H1/H2, geometry need not be searched;
otherwise group residual closure directions and test positivity beforegrowth.
"""
from itertools import product
from pathlib import Path
import argparse
import json
C=(0,1,0,1,2,2)
def canonical_partition(equalities):
 parent=list(range(6))
 def find(i):
  while parent[i]!=i:i=parent[i]
  return i
 for i,j in equalities:parent[find(i)]=find(j)
 names={};return tuple(names.setdefault(find(i),len(names))for i in range(6))
def refines(a,b):return all(a[i]!=a[j]or b[i]==b[j]for i in range(6)for j in range(i))
def mono(p):
 hits=[]
 for r,s in product(range(6),(1,-1)):
  cs=[C[(r+s*k)%6]for k in range(6)]
  es=[p[(r+k)%6]if s==1 else p[(r-k-1)%6]for k in range(6)]
  if len(set(cs[:3]))==3 and es[2]==es[5]:hits.append(['H1',r,s])
  if len({cs[0],cs[1],cs[3]})==3 and es[1]==es[3] and es[2]==es[5]:hits.append(['H2',r,s])
 return hits
AAA=[]
for corners in product((0,2),(1,3),(4,5)):
 for signs in product((1,-1),repeat=3):
  arms=[((c-1)%6,c)[::s]for c,s in zip(corners,signs)]
  eq=[(arms[k][1],arms[(k+1)%3][0])for k in range(3)]
  AAA.append(dict(corners=corners,arm_signs=signs,equalities=eq,required_partition=canonical_partition(eq)))
rows=[]
for j in range(3):
 for swap in(False,True):
  partner_corners=(j+1,j)if swap else(j,j+1)
  offers=[];endpoint_arms=[]
  for central,neighbor in zip((4,5),partner_corners):
   needed=3-C[central]-C[neighbor]
   offers.append([(c,s)for c in range(6)for s in(1,-1)if C[c]==needed])
   central_other=3 if central==4 else 5
   partner_other=(j-1)%6 if neighbor==j else(j+1)%6
   endpoint_arms.append((central_other,partner_other))
  for choices in product(*offers):
   eq=[(4,j)]
   for(c,s),pair in zip(choices,endpoint_arms):eq.extend(zip(((c-1)%6,c)[::s],pair))
   part=canonical_partition(eq)
   endpoint_star_ids=[]
   for central,neighbor,(third,sg)in zip((4,5),partner_corners,choices):
    cc=tuple(next(c for c in(central,neighbor,third)if C[c]==color)for color in range(3))
    ids=[i for i,st in enumerate(AAA)if st['corners']==cc and refines(st['required_partition'],part)]
    assert ids
    endpoint_star_ids.append(ids)
   rows.append(dict(partner_side=j,partner_endpoints_reversed=swap,third_A_corner_and_arm_signs=choices,endpoint_arms=endpoint_arms,equalities=eq,required_partition=part,monohedral_hits=mono(part),endpoint_AAA_star_ids=endpoint_star_ids))
def partitions(prefix=(0,)):
 if len(prefix)==6:yield prefix;return
 for i in range(max(prefix)+2):yield from partitions(prefix+(i,))
req=sorted(set(r['required_partition']for r in rows))
minimal=[p for p in req if not any(q!=p and refines(q,p)for q in req)]
all_partitions=list(partitions())
assert len(all_partitions)==203
actual=[]
for p in all_partitions:
 ids=[i for i,r in enumerate(rows)if refines(r['required_partition'],p)]
 if ids:actual.append(dict(partition=p,crosscase_ids=ids,monohedral_hits=mono(p)))
J=dict(scope=__doc__,native_A_word=C,AAA_native_cycles=AAA,cross_cases=rows,required_partitions=req,minimal_required_partitions=minimal,actual_partitions=actual,counts=dict(total_actual_partitions=len(all_partitions),AAA_cases=len(AAA),cross_cases=len(rows),required_partitions=len(req),minimal_partitions=len(minimal),actual_partitions=len(actual),nonmonohedral_cross_cases=sum(not r['monohedral_hits']for r in rows),nonmonohedral_actual_partitions=sum(not r['monohedral_hits']for r in actual)))
# These are proof obligations, not expected numerical outcomes chosen after sampling.
assert len(rows)==96 and len(AAA)==64
assert minimal==[(0,1,2,0,2,3),(0,1,2,3,0,2),(0,1,2,3,1,4)]
assert len(req)==36 and len(actual)==71
assert all(row['monohedral_hits'] for row in rows+actual)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check',type=Path,help='Compare complete regenerated certificate without writing.')
args=parser.parse_args()
certificate=Path('research/certificates/terra-five-one-010122-cross-22-gate.json')
if args.check:
 assert json.loads(args.check.read_text())==json.loads(json.dumps(J)), 'Certificate differs'
else:
 certificate.write_text(json.dumps(J,indent=2)+'\n')
print('PASS A010122: 64 AAA cycles; 96 two-ended used-AA22 cases; all 203 actual partitions; 71 compatible, all H1/H2; no closure residual')
