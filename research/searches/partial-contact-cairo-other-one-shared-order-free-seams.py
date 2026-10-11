"""Order-free necessary native seam LP for the other two single-cross orbits.
Finite scope is the generic-local-survivor strata of the explicitly supplied
complete orbit certificate. Independent flat/model audits remain required.
"""
import argparse,json,runpy
from pathlib import Path
helper=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-one-shared-optional-seam-balance.py')))
p=argparse.ArgumentParser();p.add_argument('--source',default='research/certificates/partial-contact-cairo-other-one-shared-event-flats.json');p.add_argument('--orbit',choices=('mixed','isolated','all'),default='all');p.add_argument('--flat',type=int,action='append');p.add_argument('--output');a=p.parse_args()
D=json.loads(Path(a.source).read_text());out=[]
for name,orbit in D.items():
 if a.orbit not in ('all',name):continue
 for r in orbit['records']:
  if r['status']!='generic-local-survivor' or(a.flat and r['flat_id'] not in a.flat):continue
  # No sample, dimensionality or order restriction enters this relaxation.
  ch={'sample_parameter':'0','interval':[None,None]}
  rec=helper['balance'](r,ch,True);rec['orbit']=name;rec['dimension']=r['dimension'];out.append(rec)
if a.output:Path(a.output).write_text(json.dumps({'scope':'order-free necessary refined corner/seam overapproximation, all survivors of specified two-orbit enumeration; exact duals or primals only; not an existence test','source':a.source,'records':out},indent=2)+'\n')
