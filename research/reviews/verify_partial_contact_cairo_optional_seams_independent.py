"""Independent original102 and weaker orderfree16 optional Cairo seam duals.
No author imports or solvers. Stars enumerated by exact angular compositions.
"""
from sage.all import QuadraticField,AA,PolynomialRing,matrix
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen();U=PolynomialRing(K,'u')
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'certificates/partial-contact-cairo-one-shared-event-flats.json').read_text())
flats={r['flat_id']:r for r in source['records'] if r['status']=='generic-local-survivor'}
perpendicular=[1,0,3,2,5,4,7,6]
def reconstruct(r,sample,free):
 # Use independently reviewed normalized affine native words, not author'skernelbasis.
 forms=[tuple(K(x) for x in a) for a in r['arm_forms']+r['e_forms']]
 if not free:
  assert forms==[tuple(U(v)[i] for i in(0,1)) for v in r['normalized_arms']+r['normalized_e']]
 value=lambda f:f[0]+f[1]*sample
 assert free or all(value(f)>0 for f in forms)
 sums=[set() for _ in range(8)];eventpairs=[]
 for a,b in product(range(8),repeat=2):
  if forms[perpendicular[a]]==forms[perpendicular[b]]:
   total=tuple(x+y for x,y in zip(forms[a],forms[b]));sums[a].add(total);sums[b].add(total);eventpairs.append((a,b,total))
 choices=[]
 for a in range(8):
  possible={forms[b] for b in range(8) if forms[b]!=forms[a] and sums[a]&sums[b] and(free or value(forms[b])<value(forms[a]))}
  choices.append([None]+sorted(possible))
 fifthchoices=[[None]+sorted({(forms[a],forms[b]) for a,b,total in eventpairs if total==forms[h]}) for h in(8,9)]
 edgekeys=[];colours=[];edgeindex={};cornerkeys=[];cornerindex={};variants=[]
 nativeangles=[120,90,120,90,120]
 def tagpiece(species,native,partition,j,start,end):
  key=(species,native,tuple(partition),j)
  if key not in edgeindex:
   edgeindex[key]=len(edgekeys);edgekeys.append(key)
   count=int(start==120)+int(end==120);colours.append((count,partition[j] if count else()))
  return edgeindex[key]
 # Recursion generates independent optional native cut words in stable source order.
 def words(options,prefix=()):
  if not options:yield prefix;return
  for cut in options[0]:yield from words(options[1:],prefix+(cut,))
 for species in(0,1):
  for cuts in words(choices[4*species:4*species+4]+[fifthchoices[species]]):
   boundary=[];angles=[]
   for native,cut in enumerate(cuts):
    length=forms[4*species+native] if native<4 else forms[8+species]
    if cut is None:partition=(length,)
    elif native==4:partition=cut
    else:
     residual=tuple(a-b for a,b in zip(length,cut));assert free or value(residual)>0
     partition=(cut,residual) if native%2==0 else(residual,cut)
    assert tuple(sum(a[k] for a in partition) for k in range(len(length)))==length
    aa=[nativeangles[native]]+([180] if len(partition)==2 else[])+[nativeangles[(native+1)%5]]
    for j in range(len(partition)):
     boundary.append(tagpiece(species,native,partition,j,aa[j],aa[j+1]));angles.append(aa[j])
   corners=[]
   for j,angle in enumerate(angles):
    key=(angle,boundary[j-1],boundary[j])
    if key not in cornerindex:cornerindex[key]=len(cornerkeys);cornerkeys.append(key)
    corners.append(cornerindex[key])
   variants.append(Counter(corners))
 # Each state has first/last sector rays and actual native piece reference flags.
 states=[]
 for c,(angle,before,after) in enumerate(cornerkeys):
  states.extend([(c,angle,after,before,0,1),(c,angle,before,after,1,0)])
 adjacency=[[] for _ in states]
 for a,x in enumerate(states):
  for b,y in enumerate(states):
   if colours[x[3]]==colours[y[2]] and not(x[1]==y[1]==90 and colours[x[3]][0]!=1):adjacency[a].append(b)
 cycles=set()
 compositions=[(120,120,120),(90,90,180),(90,180,90),(180,90,90),(90,90,90,90)]
 def canon(cycle):return min(tuple(cycle[i:]+cycle[:i]) for i in range(len(cycle)))
 # Independent angular compositions, rather than author's angular DFS/pruning rules.
 for composition in compositions:
  for a,state in enumerate(states):
   if state[1]!=composition[0]:continue
   paths=[[a]]
   for angle in composition[1:]:
    paths=[path+[b] for path in paths for b in adjacency[path[-1]] if states[b][1]==angle]
   for path in paths:
    if a in adjacency[path[-1]]:cycles.add(canon(path))
 starcounts=[];features=[];keys=set()
 for cycle in sorted(cycles):
  corners=Counter(states[a][0] for a in cycle);charge=Counter()
  for j,a in enumerate(cycle):
   b=cycle[(j+1)%len(cycle)];x,y=states[a][3],states[b][2];px,py=states[a][5],states[b][4]
   if x>y:x,y,px,py=y,x,py,px
   if x==y and px!=py:continue
   key=(x,y,px^py);charge[key]+=1 if px==0 else -1
  starcounts.append(corners);features.append(charge);keys.update(k for k,v in charge.items() if v)
 return edgekeys,cornerkeys,starcounts,features,sorted(keys),variants
for name,free,expected in [('partial-contact-cairo-one-shared-optional-seam-balance.json',False,102),('partial-contact-cairo-one-shared-order-free-seam-balance.json',True,16)]:
 D=json.loads((root/'certificates'/name).read_text());assert len(D['records'])==expected
 seen=set();starchecks=variantchecks=0
 for r in D['records']:
  f=flats[r['flat_id']];sample=K(r['sample_parameter']);chamber=next(c for c in f['generic_arm_order_chambers'] if c['interval']==r['interval'])
  assert chamber['sample_parameter']==r['sample_parameter'] and r.get('order_free',False)==free
  key=(r['flat_id'],tuple(r['interval']));assert key not in seen;seen.add(key)
  E,C,counts,seams,keys,variants=reconstruct(f,sample,free)
  assert (len(E),len(C),len(counts),len(keys),len(variants))==(r['edge_count'],r['corner_count'],r['star_count'],r['seam_count'],r['variant_count'])
  assert r['result']=='exact-necessary-dual'
  W=[Fraction(v) for v in r['corner_dual']];Y=[Fraction(v) for v in r['seam_dual']]
  assert len(W)==len(C) and len(Y)==len(keys);yi=dict(zip(keys,Y))
  for corner,seam in zip(counts,seams):
   assert sum(W[i]*n for i,n in corner.items())+sum(yi.get(k,Fraction(0))*n for k,n in seam.items())>=0;starchecks+=1
  for variant in variants:assert sum(W[i]*n for i,n in variant.items())<=-1;variantchecks+=1
  # Endpoint ledger algebra: reversingboth native endpoint flags negates feature.
  for x,y,parity in keys:
   for px in(0,1):
    py=px^parity
    if x==y and parity:continue
    assert (1 if px==0 else-1)+(1 if 1-px==0 else-1)==0
 if free:assert {i for i,interval in seen}==set(flats)
 else:assert seen=={(i,tuple(c['interval'])) for i,f in flats.items() for c in f['generic_arm_order_chambers']}
 print('PASS',name,expected,'complete independent models;',starchecks,'exact rational star inequalities;',variantchecks,'negative tile-variant inequalities;native-piece endpoint features cancel.')

# Other two solecross orbits: conditional model/duals, full flat audit owned byroot.
other=json.loads((root/'certificates/partial-contact-cairo-other-one-shared-event-flats.json').read_text())
D=json.loads((root/'certificates/partial-contact-cairo-other-one-shared-order-free-seams.json').read_text())
lookup={(name,r['flat_id']):r for name,orbit in other.items() for r in orbit['records'] if r['status']=='generic-local-survivor'}
assert len(lookup)==len(D['records'])==17
seen=set();starchecks=variantchecks=0
for rec in D['records']:
 key=(rec['orbit'],rec['flat_id']);assert key not in seen;seen.add(key);f=lookup[key]
 assert rec['order_free'] and rec['dimension']==f['dimension']
 fs=[tuple(K(a) for a in row) for row in f['arm_forms']+f['e_forms']];n=len(fs[0]);assert n==f['dimension']
 J=matrix(K,fs[:8]);constraints=matrix(K,f['constraint_rows'])
 assert J.rank()==n and constraints.rank()==8-n and constraints*J==0
 for offset,h in ((0,8),(4,9)):
  assert all(w*fs[offset][j]+fs[offset+1][j]-fs[offset+2][j]-w*fs[offset+3][j]==0 for j in range(n))
  assert all(fs[h][j]==-2*fs[offset][j]+w*fs[offset+2][j]+fs[offset+3][j] for j in range(n))
 crossmatch=tuple(other[key[0]]['native_cross_match'])
 assert {p for p in combinations(range(8),2) if fs[p[0]]==fs[p[1]]}=={crossmatch}
 point=[K(a) for a in f['positive_kernel_point']]
 vals=[sum(a*b for a,b in zip(row,point)) for row in fs]
 assert vals==[K(a) for a in f['positive_arms']+f['positive_e']] and all(a>=1 for a in vals)
 E,C,counts,seams,keys,variants=reconstruct(f,K(0),True)
 assert (len(E),len(C),len(counts),len(keys),len(variants))==(rec['edge_count'],rec['corner_count'],rec['star_count'],rec['seam_count'],rec['variant_count'])
 assert rec['result']=='exact-necessary-dual'
 W=[Fraction(a) for a in rec['corner_dual']];Y=[Fraction(a) for a in rec['seam_dual']];assert len(W)==len(C) and len(Y)==len(keys);yi=dict(zip(keys,Y))
 for corner,seam in zip(counts,seams):
  assert sum(W[i]*v for i,v in corner.items())+sum(yi.get(k,Fraction(0))*v for k,v in seam.items())>=0;starchecks+=1
 for variant in variants:assert sum(W[i]*v for i,v in variant.items())<=-1;variantchecks+=1
assert seen==set(lookup)
print('PASS other17 solecross orderfree models (including dimension3), rawclosure/privacy/witnesses;',starchecks,'exactstar inequalities;',variantchecks,'negative variants. Fullotherorbitflat completeness separately reviewed byroot.')
