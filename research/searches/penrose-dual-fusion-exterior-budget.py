#!/usr/bin/env python3
"""Same 1296-union fixture domain; exact integer exterior-angle budget.
Floating values choose integer candidates, exact cos comparisons certify them.
"""
import json,math
from pathlib import Path
from itertools import product
from functools import lru_cache
from sage.all import CyclotomicField,QQbar,AA
D=json.loads(Path('research/certificates/penrose-dual-fusion-angle-palette.json').read_text())
K=CyclotomicField(10);w=K.gen();embed=K.hom([QQbar.zeta(10)])
def decode(v):return sum(K(c)*w**i for i,c in enumerate(v))
zeta=QQbar.zeta(360)
@lru_cache(None)
def cosine(d):return AA((zeta**d).real())
bounds=[]
for i,r in enumerate(D['exact_angle_sources']):
    z=embed(decode(r['raw_ratio']));z=z/(z*z.conjugate()).real().sqrt()
    c=AA(-z.real()) # cos(pi-alpha)
    d=math.floor(180-math.degrees(math.acos(float(z.real()))))
    while c>cosine(d):d-=1
    while c<=cosine(d+1):d+=1
    assert 0<=d<180 and c<=cosine(d) and c>cosine(d+1)
    bounds.append(d)
signatures=[]
for row in D['point_choices']:
    s=tuple(tuple(c['angle_ids']) for c in row['choices'])
    if s not in signatures:signatures.append(s)
assert len(signatures)==6
minimum=10**9;witness=None;count=0;cost_hist={}
for choices in product(*signatures):
    count+=1;union=set().union(*(set(c) for c in choices));cost=sum(bounds[i] for i in union)
    cost_hist[cost]=cost_hist.get(cost,0)+1
    if cost<minimum:minimum=cost;witness=sorted(union)
assert count==1296
out={'domain':'same35point compiler,6 signatures,1296 independent local-choice unions',
     'exact_floor_rule':'d<=pi-alpha<d+1 degrees iff -Re(unit)<=cos(d*pi/180) and -Re(unit)>cos((d+1)*pi/180)',
     'floor_exterior_degrees':bounds,'enumerated_products':count,'minimum_integer_lower_bound':minimum,
     'minimum_witness_angle_ids':witness,'cost_histogram':dict(sorted(cost_hist.items())),
     'two_convex_shape_exterior_budget_degrees':720,'excludes_every_two_convex_shape_compiler':minimum>720,
     'scope':'all35 retained rhombpoints degree3/4; original rays only; flat pi sectors allowed/ignored'}
print(json.dumps(out,indent=2))
