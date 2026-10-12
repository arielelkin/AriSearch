#!/usr/bin/env python3
"""Independent all30distance-system audit of the specific hat(b,u) cut.
No producer import; explicit boundary words reconstructed independently.
"""
import argparse,hashlib,importlib.util,itertools,json
from pathlib import Path
from sage.all import PolynomialRing,AA,QQ
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('independent_hat_geometry',HERE/'check_hat_eight_kite_convex_clusters.py');geometry=importlib.util.module_from_spec(sp);sp.loader.exec_module(geometry)
K,r=geometry.K,geometry.r;R=PolynomialRing(K,'b,u',order='lex');b,u=R.gens()
H=[(0,0),(-r*b/2,-b/2),(-r*b/2+QQ(1)/2,-b/2-r/2),(-r*b/2+QQ(5)/2,-b/2-r/2),(-r*b/2+3,-b/2),(3,-b),(r*b/2+3,-b/2),(r*b/2+QQ(5)/2,-b/2+r/2),(r*b/2+QQ(3)/2,-b/2+r/2),(r*b/2+QQ(3)/2,b/2+r/2),(QQ(3)/2,b+r/2),(1,b),(0,b)]
H=[tuple(map(R,p)) for p in H];V=(u,H[7][1])
P={'P6':[H[i] for i in (0,1,2,3,4)],'P9':[H[0],H[4],V,H[11],H[12]],'P48':[H[i] for i in (4,5,6,7)]+[V],'P192':[V]+[H[i] for i in (8,9,10,11)]}
def parse(s):return R(s.replace('r',str(r)))
def distance(p,q):return sum((a-z)**2 for a,z in zip(p,q))
def evaluate(p):return K(R(p)(r,K(2)))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();path=Path('research/certificates/hat-four-pentagon-deformation-gate.json');raw=path.read_bytes();data=json.loads(raw)
 assert {name:[[parse(x),parse(y)] for x,y in seq] for name,seq in data['tiles'].items()}=={name:[list(p) for p in seq] for name,seq in P.items()}
 expected={(left,right,d,s) for left,right in itertools.combinations(('P6','P48','P192'),2) for d in (1,-1) for s in range(5)}
 actual={(row['pair'][0],row['pair'][1],row['direction'],row['shift']) for row in data['rows']};assert actual==expected and len(data['rows'])==30
 nonunit=0
 for row in data['rows']:
  A,B=map(P.get,row['pair']);d,s=row['direction'],row['shift']
  # Cartesian full squared-distance equations, with ten vertex pairs.
  equations=[distance(A[i],A[j])-distance(B[(s+d*i)%5],B[(s+d*j)%5]) for i,j in itertools.combinations(range(5),2)]
  I=R.ideal(equations);G=tuple(I.groebner_basis());stored=tuple(parse(x) for x in row['groebner_basis'])
  assert G==stored and I.dimension()==row['dimension']
  if I.dimension()==-1:assert G==(R(1),) and not row['real_points']
  else:
   assert I.dimension()==0 and G==(b-r,u-2);nonunit+=1
   assert all(evaluate(p)==0 for p in equations)
   assert len(row['real_points'])==1 and row['real_points'][0]['all_four_strictly_convex']
 assert nonunit==6
 polygons={name:[tuple(evaluate(x) for x in p) for p in seq] for name,seq in P.items()};outline=[tuple(evaluate(x) for x in p) for p in H]
 for polygon in polygons.values():
  assert geometry.area2(polygon)>0 and all(geometry.turn(polygon[i-1],polygon[i],polygon[(i+1)%5])>0 for i in range(5))
  assert all(geometry.cross(geometry.subtract(z,y),geometry.subtract(p,y))>=0 for y,z in zip(polygon,polygon[1:]+polygon[:1]) for p in polygon)
 for A,B in itertools.combinations(polygons.values(),2):assert geometry.area2(geometry.clip(A,B))==0 and geometry.congruent(A,B)
 assert geometry.same(geometry.boundary(list(polygons.values())),geometry.simplify(outline))
 original=json.loads(Path('research/certificates/hat-eight-kite-convex-cluster-gate.json').read_text());old={row['mask']:[geometry.point(p) for p in row['hull']] for row in original['convex_subsets']}
 assert all(geometry.congruent(old[9],polygon) for polygon in polygons.values())
 result={'status':'PASSED','source_sha256':hashlib.sha256(raw).hexdigest(),'pair_distance_systems':30,'unit_ideals':24,'sole_point_correspondences':6,'sole_parameter_point':['sqrt(3)','2'],'all_four_strict_convex_at_sole_point':True,'sole_point_exact_partition_and_congruence':True,'scope':'Explicitfourpentagonboundarywords only; degenerations reduce<=4intrinsiccorners or invalidtiles; no sourceforcing assumption'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
