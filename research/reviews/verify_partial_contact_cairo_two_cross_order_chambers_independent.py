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
 assert len(sample)==len(forms[0])
 value=lambda f:sum(x*y for x,y in zip(f,sample))
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

from itertools import permutations
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--dimension',type=int,action='append',choices=(1,2,3));args=parser.parse_args()
source=json.loads((root/'certificates/partial-contact-cairo-remaining-two-cross-event-flats.json').read_text())
primal=json.loads((root/'certificates/partial-contact-cairo-remaining-two-cross-order-free-seams.json').read_text())
selected={(r['pattern'],r['flat_id']):r for r in primal['records'] if r['result']=='exact-necessary-primal' and (r['pattern'],r['flat_id'])!=('orbit4',20)}
expected={1:(78,78,14,64),2:(51,318,20,298),3:(4,158,0,158)}
for dimension in args.dimension or(1,2,3):
 D=json.loads((root/('certificates/partial-contact-cairo-two-cross-dim'+str(dimension)+'-order-chambers.json')).read_text())
 assert D['completion']=='complete' and not D['chambers_only']
 assert D['selection']=={'dimension':dimension,'pattern':None,'flat_id':None,'include_reviewed_periodic_carrier':False}
 domain={key:r for key,r in selected.items() if r['dimension']==dimension}
 assert len(domain)==D['requested_primal_flats']==D['completed_primal_flats']==len(D['records'])==expected[dimension][0]
 seen=set();results=Counter();emptycount=0;stars=variants=0;cornerchecks=seamchecks=0
 for group in D['records']:
  key=(group['pattern'],group['flat_id']);assert key in domain and key not in seen;seen.add(key)
  flat=next(f for f in source[key[0]]['records'] if f['flat_id']==key[1]);assert flat['dimension']==dimension and group['dimension']==dimension
  forms=rawcheck(source[key[0]],flat)
  reps=[]
  for i,f in enumerate(forms[:8]):
   if f not in forms[:i]:reps.append(i)
  assert len(reps)==6
  pairs=list(combinations(reps,2));assert len(pairs)==15 and group['native_comparison_pairs']==[list(p) for p in pairs]
  diffs=[tuple(a-b for a,b in zip(forms[i],forms[j])) for i,j in pairs]
  rejected={}
  for item in group['empty_sign_prefixes']:
   prefix=tuple(item['sign_prefix']);assert len(prefix)<=15 and all(a in(-1,1) for a in prefix) and prefix not in rejected
   rows=forms+[tuple(sign*a for a in diff) for sign,diff in zip(prefix,diffs)]
   weights=list(map(K,item['gordan_dual']));assert len(weights)==len(rows) and all(a>=0 for a in weights) and sum(weights)==1
   assert all(sum(a*r[j] for a,r in zip(weights,rows))==0 for j in range(dimension))
   rejected[prefix]=True;emptycount+=1
  leaves={}
  for j,ch in enumerate(group['chambers']):
   assert ch['order_chamber_id']==j
   signs=tuple(ch['signs']);assert len(signs)==15 and signs not in leaves and all(a in(-1,1) for a in signs)
   point=tuple(map(K,ch['sample_kernel_point']));assert len(point)==dimension
   values=[sum(a*b for a,b in zip(f,point)) for f in forms]
   assert all(a>0 for a in values) and values==list(map(K,ch['sample_arms']+ch['sample_e']))
   assert all(sign*sum(a*b for a,b in zip(diff,point))>0 for sign,diff in zip(signs,diffs))
   assert sorted(range(8),key=lambda i:(values[i],i))==ch['native_arm_order']
   for row in source[key[0]]['hyperplane_rows']:
    reduced=tuple(sum(K(a)*forms[i][j] for i,a in enumerate(row)) for j in range(dimension))
    if any(reduced):assert sum(a*b for a,b in zip(reduced,point))!=0
   rec=ch['seam_balance'];assert rec['pattern']==key[0] and rec['flat_id']==key[1] and rec['dimension']==dimension and rec['order_chamber_id']==j and not rec['order_free'] and rec['sample_kernel_point']==ch['sample_kernel_point']
   kind,a,b=checkresult(rec,reconstruct(flat,point,False));results[kind]+=1
   if kind=='dual':stars+=a;variants+=b
   else:cornerchecks+=a;seamchecks+=b
   leaves[signs]=True
  # Full binary tree cover, with no omitted or overlapping terminal prefixes.
  terminals=set(rejected)|set(leaves);assert len(terminals)==len(rejected)+len(leaves)
  assert all(not any(t[:k] in terminals for k in range(len(t))) for t in terminals)
  def covered(prefix=()):
   if prefix in terminals:return
   assert len(prefix)<15,('uncoveredbinaryorder',key,prefix)
   covered(prefix+(-1,));covered(prefix+(1,))
  covered()
  assert sum(2**(15-len(t)) for t in terminals)==2**15
  # Independent720 permutation-domain confirmation (not just binary sign count).
  perm_signs=[]
  for order in permutations(reps):
   rank={slot:i for i,slot in enumerate(order)}
   signs=tuple(1 if rank[i]>rank[j] else -1 for i,j in pairs);perm_signs.append(signs)
   if signs not in leaves:assert any(signs[:len(prefix)]==prefix for prefix in rejected)
  assert len(set(perm_signs))==720 and set(leaves)<=set(perm_signs)
  if len(seen)%10==0:print('dimension',dimension,'checked',len(seen),'of',len(domain),'flats',dict(results),flush=True)
 assert seen==set(domain) and (len(seen),sum(results.values()),results['dual'],results['primal'])==expected[dimension]
 if dimension==3:assert emptycount==742 and [len(r['chambers']) for r in D['records']]==[45,50,37,26]
 print('PASS dimension',dimension,'completeactualorderflats',len(seen),'chambers',sum(results.values()),'duals/primals',results['dual'],results['primal'],'exactempty-prefixGordan',emptycount,'dualstar/variantineq',stars,variants,'primalcorner/seameq',cornerchecks,seamchecks,';all15 comparisons/720permutationdomain,positivegenericfixtures,rawsymbolicnativepiecesandactualcuttests. NOtilingexistenceinferred.',flush=True)
