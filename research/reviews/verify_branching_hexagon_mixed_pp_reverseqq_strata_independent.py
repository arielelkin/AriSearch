"""Fresh complete intersection-lattice and native seam dual audit, no author imports/solvers."""
from sage.all import QQ,matrix,vector
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
D=json.loads(Path('research/certificates/branching-hexagon-two-run-mixed-pp-reverseqq-strata-slot-balance.json').read_text())
I=json.loads(Path('research/certificates/branching-hexagon-two-run-mixed-pp-reverseqq-exceptional-stars.json').read_text())
planes=[tuple(map(QQ,r['coefficients'])) for r in I['remaining21exception_curves']]
assert D['planes']==[list(map(int,p)) for p in planes] and len(planes)==21

def canonical(A):return tuple(tuple(x for x in row) for row in A.row_space().basis_matrix().rows())
def M(key):return matrix(QQ,key) if key else matrix(QQ,0,4)
def consistent(A):return A.rank()==A[:,1:].rank()
# Independent recursive lattice closure; unlike author's size0..3 subset generation.
origin=();allflats={origin};todo=[origin]
while todo:
 key=todo.pop()
 for row in planes:
  a=matrix(QQ,list(key)+[row]);
  if not consistent(a):continue
  k=canonical(a)
  if k not in allflats:allflats.add(k);todo.append(k)
assert len(allflats)==99
# Check complete source470 generator metadata by independent normalization.
generators={};total=0
for size in range(4):
 for subset in combinations(range(21),size):
  total+=1;a=matrix(QQ,[planes[j] for j in subset]) if subset else M(())
  if consistent(a):generators.setdefault(canonical(a),[]).append(list(subset))
assert total==D['generator_subset_count']==1562 and set(generators)==allflats and D['consistent_flat_count']==99
rejected=D['linear_envelope_infeasible_flats'];records=D['records']
assert len(rejected)==6 and len(records)==93
keys=set()
for r in rejected+records:
 key=tuple(tuple(QQ(a) for a in row) for row in r['flat_basis']);assert key not in keys;keys.add(key)
 assert key==canonical(M(key)) and r['generating_subsets']==generators[key]
 if r in rejected:
  # All four negative envelopes independently prove delta=0, no feasibility solver required.
  assert vector(QQ,(0,1,0,0)) in M(key).row_space()
 else:
  delta,alpha,rho=map(QQ,r['linear_envelope_sample'])
  assert 0<delta<30 and 90<alpha<180 and 0<rho<90 and alpha-rho-delta<120
  assert M(key)*vector(QQ,(1,delta,alpha,rho))==0
assert keys==allflats
names=['AH','AL']*3+['B0','alpha','beta','B3','chi','psi']
# These raw native angles were independently derived from directions in inventory audit.
angleforms={'AH':(120,1,0,0),'AL':(120,-1,0,0),'B0':(60,1,0,1),'alpha':(0,0,1,0),'beta':(360,0,-2,0),'B3':(60,-1,1,-1),'chi':(120,2,0,0),'psi':(120,-2,0,0)}
forms=[angleforms[n] for n in names]
slots=[(s,j) for s in(0,1) for j in range(6)];words=[('p','q')*3,('p',)*3+('q',)*3]
states=[]
for c,(s,j) in enumerate(slots):states.extend([(c,(s,j),(s,(j-1)%6),0,1),(c,(s,(j-1)%6),(s,j),1,0)])
def cyclic(path):return min(path[i:]+path[:i] for i in range(3))
def reconstruct(space):
 allowed=set()
 for trip in product(range(12),repeat=3):
  row=[sum(forms[c][j] for c in trip) for j in range(4)];row[0]-=360
  if vector(QQ,row) in space:allowed.add(trip)
 stars=set()
 for path in product(range(24),repeat=3):
  if tuple(states[i][0] for i in path) not in allowed:continue
  if all(words[states[path[j]][2][0]][states[path[j]][2][1]]==words[states[path[(j+1)%3]][1][0]][states[path[(j+1)%3]][1][1]] for j in range(3)):stars.add(cyclic(path))
 stars=sorted(stars);counts=[];seams=[];keys=set()
 for path in stars:
  cc=Counter(states[i][0] for i in path);ss=Counter()
  for j,a in enumerate(path):
   b=path[(j+1)%3];x,y=states[a][2],states[b][1];px,py=states[a][4],states[b][3]
   if x>y:x,y,px,py=y,x,py,px
   if x==y and px!=py:continue
   key=(x,y,px^py);ss[key]+=1 if px==0 else -1
  counts.append(cc);seams.append(ss);keys.update(ss)
 return stars,counts,seams,sorted(keys)
results=Counter();dualstars=0;primalcorners=primalseams=0
simple=[vector(QQ,a) for a in ((-120,0,1,0),(-180,0,1,1),(180,0,-2,1))]
for index,r in enumerate(records):
 assert r['index']==index
 basis=M(tuple(tuple(QQ(a) for a in row) for row in r['flat_basis']));space=basis.row_space()
 assert r['active_exception_equations']==[i for i,p in enumerate(planes) if vector(QQ,p) in space]
 stars,counts,seams,keys=reconstruct(space)
 assert [list(s) for s in stars]==r['oriented_stars']
 assert [{str(c):n for c,n in cc.items()} for cc in counts]==r['star_corner_counts']
 assert [[list(x),list(y),parity] for x,y,parity in keys]==r['seam_keys']
 assert [[ss.get(k,0) for k in keys] for ss in seams]==r['star_seam_counts']
 if r['status']=='unsat':
  assert r['dual_status']=='sat';W=list(map(Fraction,r['corner_dual']));Y=list(map(Fraction,r['seam_dual']))
  assert len(W)==12 and len(Y)==len(keys) and sum(W[:6])<=-1 and sum(W[6:])<=-1
  for C,S in zip(counts,seams):assert sum(W[c]*n for c,n in C.items())+sum(y*S.get(k,0) for k,y in zip(keys,Y))>=0
  dualstars+=len(stars)
 else:
  assert r['status']=='sat'
  freq=list(map(Fraction,r['species_frequencies']));X=list(map(Fraction,r['star_frequencies']))
  assert len(freq)==2 and len(X)==len(stars) and sum(freq)==1 and min(freq+X)>=0
  assert freq==[Fraction(1,2)]*2 and r['mixed_status']=='sat'
  for c in range(12):assert sum(x*C.get(c,0) for x,C in zip(X,counts))==freq[c//6]
  for k in keys:assert sum(x*S.get(k,0) for x,S in zip(X,seams))==0
  primalcorners+=12;primalseams+=len(keys)
  assert any(v in space for v in simple)
 results[r['status']]+=1
 if (index+1)%12==0:print('checked',index+1,'of93',dict(results),flush=True)
assert results==Counter({'unsat':71,'sat':22}) and dict(results)==D['counts']
print('PASS reverseqq complete recursive21-plane arrangement99 flats/all1562 generator metadata;6 exactdelta0 rejects/93 rational positive-envelope witnesses;allactual native oriented stars and retainedcolumns;71 strong exact duals',dualstars,'star inequalities;22 exact necessaryprimals',primalcorners,'corner and',primalseams,'seam equalities;everyprimalflatforces alpha120 ORalpha+rho180 ORrho2alpha-180. Metricphase elimination separately reviewed.')
