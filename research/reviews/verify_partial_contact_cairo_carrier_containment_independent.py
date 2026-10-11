"""Independently verify complete native identity containment in four proved cones.
No author module/carrier-side certificate/solver imported.
"""
from sage.all import *
from pathlib import Path
import json
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(K,names=('a','b','c'));a,b,c=R.gens()
d=a+(b-c)/w;e=w*c+d-2*a
# Each carrier is freshly defined by the native equations in its proved lemma.
g=(d-c+2*a)/(w-1)
words=[(a,g+w*(c-a),g,c,g+d),
       (e-b,a,c,e-b+(a-c)/w,w*c+(e-b+(a-c)/w)-2*(e-b)),
       (a,-3*w*a+2*b+2*c,b,e-a,w*b+(e-a)-2*a),
       (a,3*w*a-2*c,b,3*a-e,2*d)]
names=[('orbit2',23,'mixed-quotient-periodic'),('orbit7',12,'mixed-quotient-isolated-cross-periodic'),('orbit0',11,'mixed-quotient-bank-transfer-periodic'),('orbit0',23,'mixed-quotient-double-bank-periodic')]
carrier=[]
for Q in words:
 rows=(a,b,c,d)+Q[:4]+(e,Q[4])
 carrier.append(matrix(K,[[t.monomial_coefficient(v) for v in (a,b,c)] for t in rows]))
base=Path('research/certificates')
read=lambda name:json.loads((base/name).read_text())
source=read('partial-contact-cairo-remaining-two-cross-event-flats.json')
initial=read('partial-contact-cairo-two-cross-event-flats.json')
expected={}
for dimension in (1,2,3):
 for record in read(f'partial-contact-cairo-two-cross-dim{dimension}-order-chambers.json')['records']:
  if any(ch['seam_balance']['result']=='exact-necessary-primal' for ch in record['chambers']):
   key=(record['pattern'],record['flat_id']);assert key not in expected
   expected[key]=next(r for r in source[key[0]]['records'] if r['flat_id']==key[1])
for record in read('partial-contact-cairo-two-cross-order-free-seams.json')['records']:
 if record['result']=='exact-necessary-primal':
  key=('separated',record['flat_id']);assert key not in expected
  expected[key]=next(r for r in initial['separated']['records'] if r['flat_id']==key[1])
assert len(expected)==117
cert=read('partial-contact-cairo-mixed-quotient-flat-containment.json')
actual={(r['pattern'],r['flat_id']):r for r in cert['records']}
assert len(actual)==len(cert['records'])==117 and set(actual)==set(expected)
counts={'covered':0,'remaining':0};dimensions={}; remaining=[]
for key,r in expected.items():
 E=matrix(K,r['arm_forms']+r['e_forms']);parameter=E[:3,:]
 out=actual[key];assert out['dimension']==r['dimension']
 maps=[]
 for C,(pat,fid,name) in zip(carrier,names):
  if C*parameter==E:
   assert E.rank()==parameter.rank()==r['dimension']
   maps.append({'carrier_pattern':pat,'carrier_flat_id':fid,'carrier_lemma':'partial-contact-cairo-'+name+'.md','parameter_map_rows':[[str(t) for t in row] for row in parameter.rows()],'identical_native_rows':list(range(10))})
 assert out['maps']==maps
 assert out['status']==('full-positive-periodic-carrier-contained' if maps else 'unmapped-necessary-stratum')
 if maps:counts['covered']+=1
 else:
  counts['remaining']+=1;dimensions[r['dimension']]=dimensions.get(r['dimension'],0)+1;remaining.append(key)
assert counts==cert['counts']=={'covered':99,'remaining':18}
assert dimensions=={1:14,2:4}
print('PASS all117 reviewed necessary strata, four freshly defined full native carriers, all10 side identities and every parameter rank; 99 periodically covered,18 remaining (4dim2/14dim1).')
print('REMAINING',remaining)
