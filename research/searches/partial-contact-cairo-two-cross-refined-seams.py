"""Actual arm-order optional seams for the two order-free-primal ratio flats."""
import argparse,json,runpy
from pathlib import Path
from sage.all import PolynomialRing
h=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-one-shared-optional-seam-balance.py')))
p=argparse.ArgumentParser();p.add_argument('--flat',type=int,action='append');p.add_argument('--output');a=p.parse_args()
D=json.loads(Path('research/certificates/partial-contact-cairo-two-cross-event-flats.json').read_text())['separated'];out=[]
R=PolynomialRing(h['K'],'u')
for r in D['records']:
 if r['flat_id'] not in (a.flat or(46,49)):continue
 r=dict(r);norm=[R(t) for t in r['normalized_arms']+r['normalized_e']]
 r['arm_forms']=[[str(t[0]),str(t[1])] for t in norm[:8]];r['e_forms']=[[str(t[0]),str(t[1])] for t in norm[8:]]
 for ch in r['generic_arm_order_chambers']:out.append(h['balance'](r,ch))
if a.output:Path(a.output).write_text(json.dumps({'scope':'necessary complete optional arm-order refinement on separated two-cross ratio flats46/49; primal is not existence','records':out},indent=2)+'\n')
