"""Fresh exact audit of all18 remaining Cairo native matrices/domain signs."""
from sage.all import *
from pathlib import Path
import json
K=QuadraticField(3,'w');w=K.gen();R=PolynomialRing(K,names=('a','b'));a,b=R.gens()
c=(3*w*a+b)/4;d=(a+w*b)/4;e=2*d
Qs={142:((3*w*a-b)/2,a,(11*a-3*w*b)/2,b,5*(w*a-b)/2),239:(4*b-w*a,a,3*w*b-2*a,b,2*b)}
carriers={fid:matrix(K,[[t.monomial_coefficient(v) for v in (a,b)] for t in (a,b,c,d)+Q[:4]+(e,Q[4])]) for fid,Q in Qs.items()}
base=Path('research/certificates');read=lambda p:json.loads((base/p).read_text())
old=read('partial-contact-cairo-mixed-quotient-flat-containment.json')
keys={(r['pattern'],r['flat_id']) for r in old['records'] if not r['maps']};assert len(keys)==18
source=read('partial-contact-cairo-remaining-two-cross-event-flats.json');sep=read('partial-contact-cairo-two-cross-event-flats.json')['separated']
cert=read('partial-contact-cairo-mixed-quotient-lower-flat-containment.json');records={(r['pattern'],r['flat_id']):r for r in cert['records']}
assert len(records)==len(cert['records'])==18 and set(records)==keys
counts={};remaining=[]
for key,out in records.items():
 pool=sep if key[0]=='separated' else source[key[0]]
 flat=next(r for r in pool['records'] if r['flat_id']==key[1]);dim=flat['dimension']
 E=matrix(K,flat['arm_forms']+flat['e_forms']);T=E[:2,:]
 assert out['dimension']==dim
 maps=[];complete=False;partial=False
 for fid,C in carriers.items():
  if C*T!=E:continue
  assert E.rank()==T.rank()==dim
  m={'carrier_flat_id':fid,'parameter_map_rows':[[str(t) for t in row] for row in T.rows()],'identical_native_rows':list(range(10))}
  if fid==142:m['scope']='full-positive-native-cone';complete=True
  else:
   cut=T[1]-T[0]/w;m['necessary_sufficient_domain_row']=[str(t) for t in cut];m['domain_relation']='>=0'
   if dim==1:
    point=vector(K,flat['positive_kernel_point']);sides=E*point
    assert all(t>0 for t in sides)
    val=cut.dot_product(point)
    # Rank1 native positivity fixes a single half-line, hence this sign is global.
    assert E.ncols()==1 and point[0]!=0
    m['positive_ray_kernel_point']=[str(t) for t in point];m['positive_ray_cut_value']=str(val);m['positive_ray_native_sides']=[str(t) for t in sides]
    if val>=0:m['scope']='whole-positive-ray';complete=True
    else:m['scope']='no-positive-ray-point-in-carrier-domain'
   else:
    assert dim==2 and cut!=0
    m['scope']='partial-metric-cone';partial=True
  maps.append(m)
 status='whole-periodic-escape' if complete else 'partial-periodic-escape' if partial else 'unmapped-necessary-stratum'
 assert out['maps']==maps and out['status']==status
 counts[status]=counts.get(status,0)+1
 if not complete:remaining.append((key,dim,status))
assert counts==cert['counts']=={'unmapped-necessary-stratum':6,'whole-periodic-escape':11,'partial-periodic-escape':1}
assert len(remaining)==cert['remaining_whole_strata']==7
assert sum(dim==2 for key,dim,status in remaining)==3
print('PASS all18 prior source keys, full142/high239 independent native identities/ranks and global positive-ray signs:11 wholeperiodic,1 partial239,6 unmapped;7 targets remain (3dim2/4dim1).')
print('REMAINING',remaining)
