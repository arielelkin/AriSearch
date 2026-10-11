"""Independent two-cross optional native seam models: no author imports/solvers.
The reconstruction uses independently enumerated angular compositions.
"""
from sage.all import QuadraticField,AA,PolynomialRing,matrix
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen();U=PolynomialRing(K,'u')
root=Path(__file__).resolve().parents[1]
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

def rawcheck(group,f):
 fs=[tuple(K(a) for a in row) for row in f['arm_forms']+f['e_forms']];n=len(fs[0])
 assert n==f['dimension'] and n in (1,2,3)
 J=matrix(K,fs[:8]);constraints=matrix(K,f['constraint_rows'])
 assert J.rank()==n and constraints.rank()==8-n and constraints*J==0
 for offset,h in ((0,8),(4,9)):
  assert all(w*fs[offset][j]+fs[offset+1][j]-fs[offset+2][j]-w*fs[offset+3][j]==0 for j in range(n))
  assert all(fs[h][j]==-2*fs[offset][j]+w*fs[offset+2][j]+fs[offset+3][j] for j in range(n))
 declared={tuple(p) for p in group['native_cross_matches']}
 assert {p for p in combinations(range(8),2) if fs[p[0]]==fs[p[1]]}==declared
 point=[K(a) for a in f['positive_kernel_point']]
 vals=[sum(a*b for a,b in zip(row,point)) for row in fs]
 assert vals==[K(a) for a in f['positive_arms']+f['positive_e']] and all(a>=1 for a in vals)
 return fs

def checkresult(rec,model):
 E,C,counts,seams,keys,variants=model
 assert (len(E),len(C),len(counts),len(keys),len(variants))==(rec['edge_count'],rec['corner_count'],rec['star_count'],rec['seam_count'],rec['variant_count'])
 if rec['result']=='exact-necessary-dual':
  W=[Fraction(a) for a in rec['corner_dual']];Y=[Fraction(a) for a in rec['seam_dual']]
  assert len(W)==len(C) and len(Y)==len(keys);yi=dict(zip(keys,Y))
  for corner,seam in zip(counts,seams):assert sum(W[i]*v for i,v in corner.items())+sum(yi.get(k,Fraction(0))*v for k,v in seam.items())>=0
  for variant in variants:assert sum(W[i]*v for i,v in variant.items())<=-1
  return 'dual',len(counts),len(variants)
 assert rec['result']=='exact-necessary-primal'
 X={int(i):Fraction(a) for i,a in rec['star_frequencies'].items()};T={int(i):Fraction(a) for i,a in rec['variant_frequencies'].items()}
 assert all(0<=i<len(counts) and a>0 for i,a in X.items())
 assert all(0<=i<len(variants) and a>0 for i,a in T.items()) and sum(T.values())==1
 for c in range(len(C)):
  assert sum(a*counts[i].get(c,0) for i,a in X.items())==sum(a*variants[i].get(c,0) for i,a in T.items())
 for key in keys:assert sum(a*seams[i].get(key,0) for i,a in X.items())==0
 return 'primal',len(C),len(keys)

source=json.loads((root/'certificates/partial-contact-cairo-remaining-two-cross-event-flats.json').read_text())
lookup={(name,r['flat_id']):r for name,g in source.items() for r in g['records'] if r['status']=='generic-local-survivor'}
D=json.loads((root/'certificates/partial-contact-cairo-remaining-two-cross-order-free-seams.json').read_text())
assert len(lookup)==len(D['records'])==591
seen=set();results=Counter();byorbit={};stars=variants=0;corners=seamchecks=0
for j,rec in enumerate(D['records']):
 key=(rec['pattern'],rec['flat_id']);assert key not in seen;seen.add(key)
 f=lookup[key];assert rec['order_free'] and rec['dimension']==f['dimension']
 rawcheck(source[key[0]],f)
 kind,a,b=checkresult(rec,reconstruct(f,K(0),True));results[kind]+=1
 byorbit.setdefault(key[0],Counter())[kind]+=1
 if kind=='dual':stars+=a;variants+=b
 else:corners+=a;seamchecks+=b
 if (j+1)%50==0:print('checked',j+1,'of591',dict(results),flush=True)
assert seen==set(lookup) and results==Counter({'dual':457,'primal':134})
expected=[(53,50),(51,1),(104,41),(40,0),(0,1),(55,1),(53,20),(93,20),(8,0)]
assert [tuple(byorbit['orbit'+str(i)][k] for k in ('dual','primal')) for i in range(9)]==expected
print('PASS all591 remaining two-cross orderfree models (dimensions1/2/3):457 exact duals',stars,'star and',variants,'negative-variant inequalities;134 exact relaxed primals',corners,'corner and',seamchecks,'seam equalities. NO tiling existence inferred; sourceflat completeness separately reviewed.')
