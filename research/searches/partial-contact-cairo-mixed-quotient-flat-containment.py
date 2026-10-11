"""Exact native-side identity containment in full positive mixed-quotient carriers."""
from sage.all import *
from pathlib import Path
from collections import Counter
import json
K=QuadraticField(3,'w');w=K.gen()
base=Path('research/certificates')
flats=json.loads((base/'partial-contact-cairo-remaining-two-cross-event-flats.json').read_text())
initial=json.loads((base/'partial-contact-cairo-two-cross-event-flats.json').read_text())
carriers=[('orbit2',23,'mixed-quotient-periodic','partial-contact-cairo-mixed-quotient-four-faces.json'),('orbit7',12,'mixed-quotient-isolated-cross-periodic','partial-contact-cairo-mixed-quotient-orbit7-flat12.json'),('orbit0',11,'mixed-quotient-bank-transfer-periodic','partial-contact-cairo-mixed-quotient-orbit0-flat11-six-faces.json'),('orbit0',23,'mixed-quotient-double-bank-periodic','partial-contact-cairo-mixed-quotient-orbit0-flat23-six-faces.json')]
C=[]
for pat,fid,name,file in carriers:
 q=json.loads((base/file).read_text());rows=matrix(K,q['arm_forms']+q['e_forms']);assert rows.ncols()==3
 assert rows[:3,:]==identity_matrix(K,3)
 C.append((pat,fid,name,rows))
remaining=[]
for dim in(1,2,3):
 doc=json.loads((base/f'partial-contact-cairo-two-cross-dim{dim}-order-chambers.json').read_text())
 for r in doc['records']:
  if any(ch['seam_balance']['result']=='exact-necessary-primal' for ch in r['chambers']):
   source=next(z for z in flats[r['pattern']]['records'] if z['flat_id']==r['flat_id']);remaining.append((r['pattern'],source))
for r in json.loads((base/'partial-contact-cairo-two-cross-order-free-seams.json').read_text())['records']:
 if r['result']=='exact-necessary-primal':
  source=next(z for z in initial['separated']['records'] if z['flat_id']==r['flat_id']);remaining.append(('separated',source))
assert len(remaining)==117
records=[];count=Counter()
for pat,r in remaining:
 actual=matrix(K,r['arm_forms']+r['e_forms']);p=actual[:3,:];maps=[]
 for cpat,cfid,name,carrier in C:
  if carrier*p==actual:
   assert p.rank()==r['dimension'] and actual.rank()==r['dimension']
   maps.append({'carrier_pattern':cpat,'carrier_flat_id':cfid,'carrier_lemma':'partial-contact-cairo-'+name+'.md','parameter_map_rows':[[str(t) for t in row] for row in p.rows()],'identical_native_rows':list(range(10))})
 count['covered' if maps else 'remaining']+=1
 records.append({'pattern':pat,'flat_id':r['flat_id'],'dimension':r['dimension'],'status':'full-positive-periodic-carrier-contained' if maps else 'unmapped-necessary-stratum','maps':maps})
print('INVENTORY',count,'REMAINING_DIM',Counter(r['dimension'] for r in records if not r['maps']),'CARRIER_COUNTS',Counter(m['carrier_flat_id'] for r in records for m in r['maps']),flush=True)
result={'scope':'exact whole-native-side linear identity containment; sufficiency depends on independently reviewed complete carrier cone, no positivity/sample inference','source_inventory':117,'carrier_lemmas':[x[2] for x in carriers],'records':records,'counts':dict(count)}
(base/'partial-contact-cairo-mixed-quotient-flat-containment.json').write_text(json.dumps(result,indent=2)+'\n')
