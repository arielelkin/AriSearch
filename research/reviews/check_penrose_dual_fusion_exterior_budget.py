#!/usr/bin/env python3
"""Exact lower-bound certificate check, no floats and no producer import."""
import json,runpy
from pathlib import Path
from itertools import product
from functools import lru_cache
from sage.all import QQbar,AA
# Independently reconstructs all geometry and local choices before budget use.
base=runpy.run_path('research/reviews/check_penrose_dual_fusion_angle_palette.py')
C=json.loads(Path('research/certificates/penrose-dual-fusion-exterior-budget.json').read_text())
A=base['A'];bounds=C['floor_exterior_degrees'];assert len(A)==len(bounds)==26
z=QQbar.zeta(360)
@lru_cache(None)
def cosine(d):return AA((z**d).real())
for a,d in zip(A,bounds):
    assert isinstance(d,int) and 0<=d<180
    c=AA(-a.real())
    assert c<=cosine(d) and c>cosine(d+1)
minimum=10**9;hist={};count=0;witness=None
for choices in product(*base['signatures']):
    count+=1;union=set().union(*(set(c) for c in choices));cost=sum(bounds[i] for i in union)
    hist[str(cost)]=hist.get(str(cost),0)+1
    if cost<minimum:minimum=cost;witness=sorted(union)
assert count==1296==C['enumerated_products']
assert minimum==837==C['minimum_integer_lower_bound']
assert witness==C['minimum_witness_angle_ids'] and hist==C['cost_histogram']
assert C['two_convex_shape_exterior_budget_degrees']==720
assert C['excludes_every_two_convex_shape_compiler'] and minimum>720
print('PASS: all26 exterior floors checked algebraically without floats; all1296 products require >=837 degrees, exceeding the720-degree budget of any two convex polygons.')
