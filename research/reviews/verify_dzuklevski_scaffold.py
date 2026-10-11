"""Exact fixed instance of the Figure-7 diagram scaffold, not a forcing check.
Replay: conda run --no-capture-output -n arisearch python3 research/reviews/verify_dzuklevski_scaffold.py
"""
import json
from itertools import combinations
from sage.all import AA, QQ, matrix, vector, Polyhedron
from sage.env import SAGE_VERSION

half = QQ(1) / 2
h = AA(3).sqrt() / 2
t, depth = QQ(7) / 10, QQ(4) / 15

def point(x, y):
    return vector(AA, [x, y])

def quarter_turn(x):
    return point(-x[1], x[0])

def determinant(a, b):
    return a[0]*b[1] - a[1]*b[0]

v = [point(*x) for x in [(0,0), (h,half), (2*h,0),
     (2*h+half,-h), (2*h,-2*h), (h,-2*h-half),
     (0,-2*h), (half,-h)]]
signs = [1,-1,-1,1,1,-1,-1,1]
a = []
for i, s in enumerate(signs):
    e = v[(i+1)%8] - v[i]
    a.append(v[i] + (1-t if s == 1 else t)*e + s*depth*quarter_turn(e))
Q, R = point(QQ(3)/4, -QQ(4)/3), point(QQ(37)/50, -QQ(5)/4)
C, P = point(0,0), point(-half+t,h-depth)
B, D = point(half,h), point(1,0)
out = B + (1-t)*(D-B) + depth*quarter_turn(D-B)
rot = matrix(AA, [[-half,h],[-h,-half]])
polygons = {
  1: [C,P,B,out,D,rot*P],
  4: [Q,v[4],a[4],v[5],a[5]],
  5: [Q,a[5],v[6],a[6],R],
  6: [R,a[2],v[3],a[3],v[4],Q],
  7: [v[7],a[1],v[2],a[2],R,a[6]],
  8: [v[7],a[7],v[0],a[0],v[1],a[1]],
}

def area(p):
    return abs(sum(determinant(p[i],p[(i+1)%len(p)]) for i in range(len(p))) / 2)

def squared_edges(p):
    return sorted((p[(i+1)%len(p)]-p[i]).dot_product(p[(i+1)%len(p)]-p[i]) for i in range(len(p)))

turn_signs = {}
for k,p in polygons.items():
    turn_signs[k] = [int(determinant(p[(i+1)%len(p)]-p[i],
          p[(i+2)%len(p)]-p[(i+1)%len(p)]).sign()) for i in range(len(p))]
    assert all(s == -1 for s in turn_signs[k])
    hull = Polyhedron(vertices=[list(x) for x in p],base_ring=AA,backend='field')
    assert hull.n_vertices() == len(p)
    assert hull.dim() == 2
    assert hull.volume() == area(p)

for i,j in combinations(polygons,2):
    assert squared_edges(polygons[i]) != squared_edges(polygons[j])
right_hulls = {k:Polyhedron(vertices=[list(x) for x in polygons[k]],base_ring=AA,backend='field') for k in [4,5,6,7,8]}
intersections = {}
for i,j in combinations(right_hulls,2):
    dim = right_hulls[i].intersection(right_hulls[j]).dim()
    assert dim <= 1
    intersections[f'{i},{j}'] = int(dim)
coarse_boundary = [z for pair in zip(v,a) for z in pair]
assert sum(area(polygons[k]) for k in right_hulls) == area(coarse_boundary)
left_polygons = [polygons[1], [rot*x for x in polygons[1]], [rot*rot*x for x in polygons[1]]]
left_hulls = [Polyhedron(vertices=[list(x) for x in p],base_ring=AA,backend='field') for p in left_polygons]
assert all(left_hulls[i].intersection(left_hulls[j]).dim() <= 1 for i,j in combinations(range(3),2))
assert sum(area(p) for p in left_polygons) == 3*h
print(json.dumps({'scope':'one exact diagram-family instance; no angle-sum forcing or plane-tilability check',
  'sage':SAGE_VERSION, 'side_counts':{k:len(p) for k,p in polygons.items()},
  'turn_signs':turn_signs, 'distinct_squared_edge_multisets':True,
  'right_pairwise_intersection_dimensions':intersections,
  'right_area_identity':True, 'left_threefold_partition_checks':True},indent=2))
