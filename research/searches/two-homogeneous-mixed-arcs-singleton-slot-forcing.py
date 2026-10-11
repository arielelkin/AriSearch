"""Exact local/algebra ledger; no solver, no author imports. Global proof in lemma."""
from sage.all import QQ, PolynomialRing, matrix, vector
from itertools import combinations,product
R=PolynomialRing(QQ,['a','c','t']);a,c,t=R.gens()
u,v=c+t,a-t;b,ps=360-2*a,360-2*c
beta=[2*u+b-360,u+v+b-360,2*v+b-360]
psi=[2*u+ps-360,u+v+ps-360,2*v+ps-360]
assert beta==[2*(c-a+t),c-a,-2*t]
assert psi==[2*t,a-c,2*(a-c-t)]
planes=[((1,0),120),((2,1),360),((1,2),360),((0,1),120)]
for (x,z),(y,w) in combinations(planes,2):
 assert matrix(QQ,[x,y]).solve_right(vector(QQ,[z,w]))==vector(QQ,[120,120])
for rays in product('pq',repeat=3):
 assert sum(rays[j]!=rays[(j+1)%3] for j in range(3)) in(0,2)
assert u+b==360-(2*a-c-t)
assert v+b==360-(a+t)
assert u+ps==360-(c-t)
assert v+ps==360-(2*c-a+t)
print('PASS all6 B-only singleton-slot angle residuals, six homogeneous-plane intersections, all8 binary ray cycles and4 exact A-neighbor necessary angle forms. Monotonic phase and unbounded boundary proof require lemma review.')
