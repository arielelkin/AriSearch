"""Whole native metric maps into full142 and high239 exact periodic carriers."""
from sage.all import *
from pathlib import Path
from collections import Counter
import json
K=QuadraticField(3,'w');w=K.gen();base=Path('research/certificates')
source=json.loads((base/'partial-contact-cairo-mixed-quotient-flat-containment.json').read_text())
F=json.loads((base/'partial-contact-cairo-remaining-two-cross-event-flats.json').read_text());A=json.loads((base/'partial-contact-cairo-two-cross-event-flats.json').read_text())['separated']
carriers={}
for fid in(142,239):
 c=json.loads((base/f'partial-contact-cairo-mixed-quotient-orbit6-flat{fid}-ten-faces.json').read_text());C=matrix(K,c['arm_forms']+c['e_forms']);assert C.ncols()==2 and C[:2,:]==identity_matrix(K,2);carriers[fid]=C
records=[];stats=Counter()
for r in source['records']:
 if r['maps']:continue
 flat=F[r['pattern']]['records'][r['flat_id']] if r['pattern']!='separated' else A['records'][r['flat_id']]
 X=matrix(K,flat['arm_forms']+flat['e_forms']);U=X[:2,:];maps=[];complete=False;partial=False
 for fid,C in carriers.items():
  if C*U!=X:continue
  assert U.rank()==X.rank()==r['dimension']
  m={'carrier_flat_id':fid,'parameter_map_rows':[[str(t) for t in row] for row in U.rows()],'identical_native_rows':list(range(10))}
  if fid==142:m['scope']='full-positive-native-cone';complete=True
  else:
   cut=U[1]-U[0]/w;m['necessary_sufficient_domain_row']=[str(t)for t in cut];m['domain_relation']='>=0'
   if r['dimension']==1:
    pt=vector(K,flat['positive_kernel_point']);assert all(t>0 for t in X*pt);value=cut.dot_product(pt)
    m['positive_ray_kernel_point']=[str(t)for t in pt];m['positive_ray_cut_value']=str(value);m['positive_ray_native_sides']=[str(t)for t in X*pt]
    if value>=0:m['scope']='whole-positive-ray';complete=True
    else:m['scope']='no-positive-ray-point-in-carrier-domain'
   else:m['scope']='partial-metric-cone';partial=True
  maps.append(m)
 status='whole-periodic-escape' if complete else 'partial-periodic-escape' if partial else 'unmapped-necessary-stratum'
 stats[status]+=1
 records.append({**{k:r[k]for k in('pattern','flat_id','dimension')},'status':status,'maps':maps})
assert len(records)==18
print('OUTCOME',stats,'REMAINING',[(r['pattern'],r['flat_id'],r['dimension'],r['status'])for r in records if r['status']!='whole-periodic-escape'],flush=True)
result={'scope':'exact native identities plus explicit full142/high239 metric domain; ray sign fixes whole positive1Dcone; no cut sign extrapolated on2Dflat','source_inventory':18,'records':records,'counts':dict(stats),'remaining_whole_strata':sum(r['status']!='whole-periodic-escape'for r in records)}
(base/'partial-contact-cairo-mixed-quotient-lower-flat-containment.json').write_text(json.dumps(result,indent=2)+'\n')
