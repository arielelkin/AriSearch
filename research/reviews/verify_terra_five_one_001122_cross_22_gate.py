#!/usr/bin/env python3
"""Independent96 two-endednativecases/64AAAcycles/all203coarsenings.
No producer imports. Symbolic residual separator over QQ(U).
"""
from sage.all import QQ,PolynomialRing
from itertools import product
from pathlib import Path
import json
J=json.loads(Path('research/certificates/terra-five-one-001122-cross-22-gate.json').read_text())
C=(0,0,1,1,2,2)
def partition(edges):
 adjacency=[set()for _ in range(6)]
 for a,b in edges:adjacency[a].add(b);adjacency[b].add(a)
 blocks=[];seen=set()
 for start in range(6):
  if start in seen:continue
  block=set();pending=[start]
  while pending:
   x=pending.pop()
   if x in block:continue
   block.add(x);pending.extend(adjacency[x])
  seen.update(block);blocks.append(block)
 return tuple(next(i for i,B in enumerate(blocks)if v in B)for v in range(6))
def implies(p,q):return all(p[i]!=p[j]or q[i]==q[j]for i in range(6)for j in range(i))
def H2(p):return(p[0]==p[2]and p[1]==p[4])or(p[0]==p[3]and p[2]==p[4])or(p[0]==p[4]and p[2]==p[5])
assert len(J['AAA_native_cycles'])==64
allstars=[]
for cc in product((0,1),(2,3),(4,5)):
 for ss in product((1,-1),repeat=3):
  rays=[[(c-1)%6,c][::s]for c,s in zip(cc,ss)]
  equalities=[[rays[i][1],rays[(i+1)%3][0]]for i in range(3)]
  allstars.append(dict(corners=list(cc),arm_signs=list(ss),equalities=equalities,required_partition=list(partition(equalities))))
assert allstars==J['AAA_native_cycles']
expected=[]
for side in(0,1,2):
 for reverse in(False,True):
  endpoints=[side,(side+1)%6]
  if reverse:endpoints.reverse()
  offered=[];incident=[]
  for zcorner,partnercorner in zip((4,5),endpoints):
   thirdcolor=next(c for c in range(3)if c not in(C[zcorner],C[partnercorner]))
   offered.append([(c,s)for c in range(6)for s in(1,-1)if C[c]==thirdcolor])
   zother=next(e for e in((zcorner-1)%6,zcorner)if e!=4)
   pother=next(e for e in((partnercorner-1)%6,partnercorner)if e!=side)
   incident.append([zother,pother])
  for third in product(*offered):
   edges=[[4,side]]
   for(c,s),arms in zip(third,incident):
    edges.extend([list(e)for e in zip([(c-1)%6,c][::s],arms)])
   p=partition(edges)
   expected.append((side,reverse,[list(x)for x in third],incident,edges,list(p)))
assert len(expected)==96
for e,row in zip(expected,J['cross_cases']):
 assert e==(row['partner_side'],row['partner_endpoints_reversed'],row['third_A_corner_and_arm_signs'],row['endpoint_arms'],row['equalities'],row['required_partition'])
 assert bool(row['monohedral_hits'])==H2(e[-1])
 for stars in row['endpoint_AAA_star_ids']:
  assert stars and all(implies(allstars[i]['required_partition'],e[-1])for i in stars)
required=sorted(set(tuple(e[-1])for e in expected))
assert required==[tuple(p)for p in J['required_partitions']]
minimal=[p for p in required if not any(q!=p and implies(q,p)for q in required)]
assert minimal==[tuple(p)for p in J['minimal_required_partitions']]
assert minimal==[(0,1,0,2,1,3),(0,1,2,0,1,2),(0,1,2,0,2,3),(0,1,2,3,0,2)]
parts=[()]
for step in range(6):parts=[p+(c,)for p in parts for c in range(max(p,default=-1)+2)]
assert len(parts)==203
actual=[p for p in parts if any(implies(q,p)for q in required)]
assert actual==[tuple(r['partition'])for r in J['actual_partitions']]
assert len(actual)==41
assert [p for p in actual if not H2(p)]==[(0,1,2,0,1,2)]
for p,row in zip(actual,J['actual_partitions']):
 assert bool(row['monohedral_hits'])==H2(p)
 assert row['crosscase_ids']==[i for i,e in enumerate(expected)if implies(e[-1],p)]
# Independent native turn reconstruction from u,v,w coefficients;w=4u-180.
# v=360-5u, so Laurent exponents/signs derive cumulatively from vertices1..5.
R=PolynomialRing(QQ,'U');U=R.fraction_field().gen()
turns={0:(1,1),1:(-5,1),2:(4,-1)}
exponent=0;sign=1;D=[U**0]
for corner in C[1:]:
 e,s=turns[corner];exponent+=e;sign*=s;D.append(sign*U**exponent)
assert D==[1,U,U**-4,U**-9,-U**-5,U**-1]
G=[D[j]+D[j+3]for j in range(3)]
transformed=[g*U**6/(1+U**3)for g in G]
assert transformed==[U**3+U**-3-1,U**4-U,U**2]
# Exactdegreebounds establish each realpart strictlynegative for54<u<72:
# 3u in(162,216):2cos3u-1<0;2u in(108,144):cos2u<0;
# cos4u-cosu=-2sin(5u/2)sin(3u/2), positive sinefactors.
assert 90<3*54<3*72<270 and 90<2*54<2*72<180
assert 0<5*QQ(54)/2<5*QQ(72)/2<=180 and 0<3*QQ(54)/2<3*QQ(72)/2<180
# 1+U^3 onlyvanishes inthisrangeatu60, excludedx120.
assert 3*54<180<3*72 and 3*72<540
print('PASS64AAA,96 fulltwoendedcases,203 actualpartitions;41crosspartitions:40H2+1positiveclosureEMPTY;separator full108<x<126,x!=120')
