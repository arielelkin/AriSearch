#!/usr/bin/env python
"""Exact embedding of the witness rhomb corona into one Robinson supertile."""
import importlib.util,json,sys
from pathlib import Path
from sage.all import QQ,AA
spec=importlib.util.spec_from_file_location('rec',Path(__file__).with_name('ammann-two-class-reconstruct.py'))
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
K,w=r.K,r.w
P=json.loads(Path('research/certificates/weighted-ammann-power-gate-2026-10-15.json').read_text())
centers=[sum((K(QQ(q))*w**j for j,q in enumerate(a['site_K'])),K(0)) for a in P['witnesses']]
def norm(z):return r.real_K(z*z.conjugate())
def data(rh,scale):
 k,cyc,_,_=r.place(rh,'B','B',QQ(1)/2,QQ(4)/5)
 return k,cyc[0]*scale,(cyc[1]-cyc[0])*scale,[p*scale for p in cyc]
t=r.sun()
for _ in range(5):t=r.subdivide(t)
source=[data(h,r.phi**5) for h in r.rhombs(t)]
# Every rhomb meeting the radius-3 witness disks has a vertex within5,
# since unit Penrose rhomb diameter<2. The selected patch covers those disks.
assert all(norm(a-b)<4 for k,o,u,p in source for a in p for b in p)
small=[(k,o,u) for k,o,u,p in source if min(norm(z-c) for z in p for c in centers)<=25]
print('selected',len(small),flush=True)
t=[r.sun()[0]]
for _ in range(9):t=r.subdivide(t)
big=[data(h,r.phi**9) for h in r.rhombs(t)]
lookup={(k,o,u) for k,o,u,p in big}
k0,o0,u0=small[0]
for j in range(10):
 rot=w**j
 for k,o,u,p in big:
  if k!=k0 or u!=rot*u0:continue
  delta=o-rot*o0
  if all((kk,delta+rot*oo,rot*uu) in lookup for kk,oo,uu in small):
   print('PASS exact supertile embedding', 'rotation',j,'translation',delta,'rhombs',len(small),flush=True)
   if '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps({'single_seed':0,'deflations':9,'rotation_exponent':j,'translation_K':[str(x) for x in delta.vector()],'selected_rhombs':[[kk,[str(x) for x in oo.vector()],[str(x) for x in uu.vector()]] for kk,oo,uu in small]},indent=2)+'\n')
   raise SystemExit(0)
raise AssertionError('No single-supertile embedding at this prescribed level')
