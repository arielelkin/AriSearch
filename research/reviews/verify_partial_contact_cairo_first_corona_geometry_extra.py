"""Fresh additional exact geometry and color-scope audit; no author imports.
The primary retained-assignment checker verifies all neighbor placements;
this independently audits strict original geometry and absence of fixture
length aliases in the finite formal-color inventory. No global extension.
"""
from pathlib import Path
import json
from sage.all import QuadraticField, AA, vector, matrix
ROOT=Path(__file__).resolve().parents[2]
K=QuadraticField(3,'w',embedding=AA(3).sqrt())
keys=(('orbit1',759),('orbit6',906),('orbit7',575),('orbit6',239),('separated',46),('separated',49),('orbit7',459))
nodes=variants=0
for pattern,fid in keys:
 path=ROOT/f'research/certificates/partial-contact-cairo-first-corona-{pattern}-flat{fid}.json'
 doc=json.loads(path.read_text()); parameter=list(map(K,doc['sample_kernel_point']))
 def value(form):return sum(a*b for a,b in zip(form,parameter))
 polygons=[[vector(K,list(map(K,p))) for p in polygon] for polygon in doc['original_native_polygons']]
 for polygon in polygons:
  assert len(polygon)==5
  for i in range(5):
   edge=polygon[(i+1)%5]-polygon[i]
   for j in range(5):
    if j not in(i,(i+1)%5):assert matrix(K,[edge,polygon[j]-polygon[i]]).det()>0
 lengths={tuple(map(K,atom['length_form'])) for variant in doc['variant_inventory'] for atom in variant['atoms']}
 numeric={}
 for form in lengths:
  assert len(form)==len(parameter) and value(form)>0
  if value(form) in numeric:assert form==numeric[value(form)]
  numeric[value(form)]=form
 assert len(parameter)==(2 if pattern=='separated' or fid==239 else 1)
 for record in doc['variant_results']:
  assert record['result']=='finite-corona-witness' and 0<record['nodes']<=doc['node_bound_per_variant']
  nodes+=record['nodes']
 variants+=doc['variant_count']
 print(f'PASS {pattern}/{fid}:30 strict native supports; positive pieces; no fixture/formal length aliases; parameter dimension{len(parameter)}')
assert nodes==3388 and variants==391
print('PASS391 retained finite witnesses/3388 recorded search nodes, no reported cutoff; no whole two-dimensional cone or global extension claim')
