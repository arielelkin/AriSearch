"""Independent fixed-certificate and actual-arrow audit. No producer imports.
All rows are affine forms in six H angles, constant LAST. Inequalities >0.
The exact domain is 203 required-value partitions * 2 signs, plus 72 aliases.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ARROWS={
 "thin":((0,1,"X"),(2,1,"X"),(2,3,"Y"),(0,3,"Y")),
 "thick":((0,1,"X"),(1,2,"Y"),(3,2,"Y"),(0,3,"X")),
}
# Formal endpoint forms in (constant,Xtail,Xhead,Ytail,Yhead).
base={('X','tail'):1,('X','head'):2,('Y','tail'):3,('Y','head'):4}
a=(36,1,0,-1,0); b=(36,-1,0,1,0)
c=(108,0,-1,1,0); d=(108,0,1,-1,0)
fixed=lambda x:(x,0,0,0,0)
xtail=Counter();audited=0
for species,arrows in ARROWS.items():
 for parity in (0,1):
  forms=[]
  for receiver in range(4):
   if receiver%2==parity:continue
   t,h,z=arrows[receiver]
   for vertex in (receiver,(receiver+1)%4):
    outgoing=(vertex-1)%4 if vertex==receiver else vertex
    assert outgoing%2==parity
    ot,oh,oz=arrows[outgoing]
    assert vertex in (ot,oh)
    incoming_role='tail' if vertex==t else 'head'
    outgoing_role='tail' if vertex==ot else 'head'
    sigma=((36,144,36,144) if species=='thin' else (72,108,72,108))[vertex]
    form=[sigma,0,0,0,0]
    form[base[z,incoming_role]]+=1
    form[base[oz,outgoing_role]]-=1
    form=tuple(form);forms.append(form);audited+=1
    if (z,incoming_role)==('X','tail'):
     assert form==(a if species=='thin' else fixed(72))
     xtail[species,parity]+=1
  expected=(a,b,fixed(144),fixed(144)) if species=='thin' else (c,d,fixed(72),fixed(72))
  assert Counter(forms)==Counter(expected)
assert audited==16 and all(xtail[s,p]>0 for s in ARROWS for p in (0,1))
assert tuple(x+y for x,y in zip(a,b))==fixed(72)
assert tuple(x+y for x,y in zip(c,d))==fixed(216)

# Recover all equality partitions independently by normalizing arbitrary maps
# from six required labels to six slots; avoid the producer recursion.
def canonical(mapping):
 names={};out=[]
 for item in mapping:
  if item not in names:names[item]=len(names)
  out.append(names[item])
 return tuple(out)
partitions={canonical(m) for m in product(range(6),repeat=6)}
assert len(partitions)==203

def affine(constant=0,terms=()):
 coeff=[F(0)]*6
 for variable,value in terms:coeff[variable]+=F(value)
 return tuple(coeff)+(F(constant),)

def rows(key):
 eq=[affine(-720,((j,1) for j in range(6)))]
 iq=[affine(0,((j,1),)) for j in range(6)]
 iq += [affine(180,((j,-1),)) for j in range(6)]
 if key[0]=='separation':
  _,p,sign=key
  fixed144,fixed72,aa,bb,cc,dd=p
  eq += [affine(-144,((fixed144,1),)),affine(-72,((fixed72,1),)),
         affine(-72,((aa,1),(bb,1))),affine(-216,((cc,1),(dd,1)))]
  iq += [affine(0,((aa,sign),(bb,-sign)))]
 else:
  _,i,step,k=key
  eq += [affine(-36,((0,1),)),affine(-72,((i,1),)),
         affine(0,(((i+step)%6,1),(1,-1))),
         affine(0,(((i+2*step)%6,1),(2,-1))),affine(-144,((k,1),))]
  iq += [affine(-180,((1,1),(2,1))),affine(270,((1,-1),(2,-1)))]
 return eq,iq

expected={('separation',p,sign) for p in partitions for sign in (-1,1)}
expected|={('pair',i,step,k) for i in range(6) for step in (-1,1) for k in range(6)}
assert len(expected)==478
path=Path(__file__).resolve().parents[1]/'certificates'/'unequal-cap-minimal-angle-2026-10-15.json'
records=json.loads(path.read_text())['records']
assert len(records)==478
seen=set();kinds=Counter()
for record in records:
 case=record['case']
 key=(case[0],tuple(case[1]),case[2]) if case[0]=='separation' else tuple(case)
 assert key in expected and key not in seen
 seen.add(key)
 equal,strict=rows(key)
 proof=record['certificate']
 coefficients=[F(value) for value in proof['equal']]
 assert len(coefficients)==len(equal)
 combined=[sum(weight*form[j] for weight,form in zip(coefficients,equal)) for j in range(7)]
 if proof['kind']=='equality':
  assert all(value==0 for value in combined[:6]) and combined[6]!=0
 else:
  assert proof['kind']=='strict'
  weights=[F(value) for value in proof['weights']]
  assert len(weights)==len(strict) and min(weights)>=0 and max(weights)>0
  combined=[combined[j]+sum(weight*form[j] for weight,form in zip(weights,strict)) for j in range(7)]
  assert all(value==0 for value in combined[:6]) and combined[6]<=0
 kinds[proof['kind']]+=1
assert seen==expected
print('PASS: actual 16 arrow endpoint forms; correct thin/thick X-tail aliases; all 203 equality partitions; all 406+72 exact weighted-row contradictions.',dict(kinds))
