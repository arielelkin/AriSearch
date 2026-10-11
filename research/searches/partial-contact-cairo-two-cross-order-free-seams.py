"""Necessary order-free seams on exact two-cross event-flat survivors."""
import argparse,json,runpy
from pathlib import Path
helper=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-one-shared-optional-seam-balance.py')))
p=argparse.ArgumentParser();p.add_argument('--source',default='research/certificates/partial-contact-cairo-two-cross-event-flats.json');p.add_argument('--output');a=p.parse_args()
D=json.loads(Path(a.source).read_text());out=[]
for name,group in D.items():
 for r in group['records']:
  if r['status']!='generic-local-survivor':continue
  rec=helper['balance'](r,{'sample_parameter':'0','interval':[None,None]},True)
  rec['pattern']=name;rec['dimension']=r['dimension'];out.append(rec)
if a.output:Path(a.output).write_text(json.dumps({'scope':'necessary order-free optional refined seam relaxation; complete supplied two-cross survivor domain; exact Fraction verification, no existence inferred','source':a.source,'records':out},indent=2)+'\n')
