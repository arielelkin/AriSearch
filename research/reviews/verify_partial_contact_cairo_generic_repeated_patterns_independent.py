"""Independent738-pattern audit using reduced union-find length classes.
No author imports, no polyhedral solver. Explicit positive native witnesses
prove cone nonemptiness; all identity tests are exact reduced closure algebra.
"""
from sage.all import QuadraticField,AA,matrix,vector
from itertools import product,combinations,combinations_with_replacement
from collections import Counter
from pathlib import Path
import json
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
blocks={'D':[(0,),(1,),(2,),(3,)],'R01':[(0,1),(2,),(3,)],
 'R23':[(0,),(1,),(2,3)],'S':[(0,3),(1,2)]}
# Independent recursive enumeration of all injections from a subset ofPblocks.
def matchings(np,nq):
 def walk(i,used,pairs):
  if i==np:yield tuple(pairs);return
  yield from walk(i+1,used,pairs)
  for j in range(nq):
   if j not in used:yield from walk(i+1,used|{j},pairs+[(i,j)])
 yield from walk(0,set(),[])
expected={(p,q,m) for p,q in product(blocks,repeat=2) for m in matchings(len(blocks[p]),len(blocks[q]))}
assert len(expected)==738
path=Path(__file__).resolve().parents[1]/'certificates'/'partial-contact-cairo-generic-repeated-patterns.json'
data=json.loads(path.read_text())
assert [r['pattern_id'] for r in data['records']]==list(range(738))
records={(r['internal_types'][0],r['internal_types'][1],tuple(tuple(p) for p in r['cross_block_matches'])):r for r in data['records']}
assert len(records)==738 and set(records)==expected
bases={'swapped-arm-cone':{(0,2),(2,0)},'reviewed-Y-cone':{(1,3),(2,0)}}
def reflect_swap(pattern,ra,rb,swap):
 out={(3-i if ra else i,3-j if rb else j) for i,j in pattern}
 return {(j,i) for i,j in out} if swap else out
orbit={(name,tuple(sorted(reflect_swap(p,ra,rb,sw)))) for name,p in bases.items() for ra,rb,sw in product([0,1],repeat=3)}
assert len(orbit)==8
counts=Counter();ranks=Counter();verified_positive=0;verified_maps=0;non_generic_fixtures=0
for key in sorted(expected):
 tp,tq,crossmatches=key;rec=records[key]
 parent=list(range(8))
 def find(i):
  while parent[i]!=i:i=parent[i]
  return i
 def join(i,j):parent[find(j)]=find(i)
 for offset,typ in [(0,tp),(4,tq)]:
  for block in blocks[typ]:
   for i in block[1:]:join(offset+block[0],offset+i)
 for ip,iq in crossmatches:join(blocks[tp][ip][0],4+blocks[tq][iq][0])
 classes=sorted({find(i) for i in range(8)});labels=[classes.index(find(i)) for i in range(8)]
 length=len(classes);units=[vector(K,[int(j==labels[i]) for j in range(length)]) for i in range(8)]
 closure=[w*units[0]+units[1]-units[2]-w*units[3],w*units[4]+units[5]-units[6]-w*units[7]]
 M=matrix(K,closure);ns=M.right_kernel().basis();ranks[M.rank()]+=1
 assert len(ns)==rec['dimension']
 quotient=lambda form:tuple(form.dot_product(v) for v in ns)
 arms=[quotient(u) for u in units]
 ef=[quotient(-2*units[s]+w*units[s+2]+units[s+3]) for s in (0,4)]
 extra=any(arms[i]==arms[j] and labels[i]!=labels[j] for i,j in combinations(range(8),2))
 if extra:
  assert rec['status']=='forced-extra-arm-equality'
  counts[rec['status']]+=1;continue
 assert rec['status']!='forced-extra-arm-equality'
 # Independent explicit native witnesscheck, avoiding author'skernelbasis.
 vals=[K(v) for v in rec['positive_arms']];ev=[K(v) for v in rec['positive_e']]
 assert all(v>=1 for v in vals+ev)
 assert all(vals[i]==vals[j] for i,j in combinations(range(8),2) if labels[i]==labels[j])
 for s in (0,4):
  assert w*vals[s]+vals[s+1]-vals[s+2]-w*vals[s+3]==0
  assert ev[s//4]==w*vals[s+2]+vals[s+3]-2*vals[s]
 non_generic_fixtures+=any(vals[i]==vals[j] and labels[i]!=labels[j] for i,j in combinations(range(8),2))
 verified_positive+=1
 # Actual native90 banks/perpendiculars retained, even withincollapsedblocks.
 perpendicular=[1,0,3,2,5,4,7,6]
 sums=[set() for i in range(8)];all_events=set()
 for i,j in combinations_with_replacement(range(8),2):
  if arms[perpendicular[i]]==arms[perpendicular[j]]:
   form=quotient(units[i]+units[j]);all_events.add(form)
   sums[i].add(form);sums[j].add(form)
 forced=[s for s in range(2) if ef[s] in all_events]
 assert forced==rec['forced_e_event_species']==[]
 compat={(i,j) for i,j in product(range(8),repeat=2) if arms[i]==arms[j] or bool(sums[i]&sums[j])}
 assert compat=={tuple(p) for p in rec['native_slot_compatibility']}
 allowed=[]
 for h,g,rev in product(range(2),repeat=3):
  if ef[h]!=ef[g]:continue
  endpointpairs=[(4*h+3,4*g+(0 if rev else 3)),(4*h,4*g+(3 if rev else 0))]
  def filler(pair):
   i,j=pair
   return any(((i,4*t+1) in compat and(j,4*t+2) in compat) or((i,4*t+2) in compat and(j,4*t+1) in compat) for t in range(2))
  if all(filler(pair) for pair in endpointpairs):allowed.append((h,g,rev))
 assert set(allowed)=={tuple(t) for t in rec['allowed_e_seams']}
 survivor=all(any(a[0]==h for a in allowed) for h in range(2))
 expected_status='generic-periodic-survivor' if survivor else 'generic-beta-obstruction'
 assert rec['status']==expected_status
 counts[expected_status]+=1
 nativecross={(i,j) for i,j in product(range(4),repeat=2) if arms[i]==arms[4+j]}
 covered=[(name,pat) for name,pat in orbit if set(pat)<=nativecross]
 assert bool(covered)==survivor
 if survivor:
  name=rec['periodic_family'];pat={tuple(p) for p in rec['sufficient_native_pattern']}
  ra,rb,sw=rec['native_reflection_and_swap']
  assert pat==reflect_swap(bases[name],ra,rb,sw) and pat<=nativecross
  # Inverseactualspecies/nativeoperations putthisgivenpairin canonicalcone.
  normalized={(j,i) for i,j in nativecross} if sw else nativecross
  normalized={(3-i if ra else i,3-j if rb else j) for i,j in normalized}
  assert bases[name]<=normalized
  verified_maps+=1
assert counts==Counter(data['counts'])==Counter({'forced-extra-arm-equality':70,'generic-beta-obstruction':517,'generic-periodic-survivor':151})
print('PASS:independent738 recursivepatterns;70 forcedextras;668 nativepositivewitnesses;517 exactnative-slot obstructions;151 actualinversecarrier maps;no identicallyforced e/event metric.')
print('Reduced closure ranks:',dict(ranks),'positivefixtures withincidentalextraarm equalities:',non_generic_fixtures)
