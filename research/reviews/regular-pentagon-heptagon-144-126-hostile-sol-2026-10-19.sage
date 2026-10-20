from sage.all import *
from itertools import product
import json
# Independent coordinates and intersection engine: real algebraic polyhedra.
z=QQbar.zeta(20)
xy=lambda x:(AA(x.real()),AA(x.imag()))
t=AA(2*(z+z.conjugate())/2)
assert t>0
q=[QQbar(0)]
for i in range(7): q.append(q[-1]+(1 if i%2==0 else t)*z**(3*i))
assert q.pop()==0
p=[QQbar(0)]
for i in range(5): p.append(p[-1]+z**(4*i))
assert p.pop()==0
# Explicit orientation preserving/reversing endpoint maps, both placing outside.
def attach(poly,s,j,rev):
 a,b=q[j],q[(j+1)%7]; c,d=poly[s],poly[(s+1)%len(poly)]
 if rev: return [a+(b-a)*((v-c)/(d-c)).conjugate() for v in poly]
 return [b+(a-b)*(v-c)/(d-c) for v in poly]
def body(v): return Polyhedron(vertices=[xy(x) for x in v],base_ring=AA)
def hit(a,b): return a.intersection(b).dim()==2
base=[body(q)]+[body(attach(p,0,j,True)) for j in (0,2,4,6)]
assert all(not hit(base[i],base[j]) for i in range(5) for j in range(i))
opt={j:[body(attach(q,s,j,r)) for s in (1,3,5) for r in (False,True)] for j in (1,3,5)}
assert all(not hit(x,b) for v in opt.values() for x in v for b in base)
compat={(a,b,i,j):not hit(opt[a][i],opt[b][j]) for a,b in ((1,3),(1,5),(3,5)) for i in range(6) for j in range(6)}
survivors=[list(c) for c in product(range(6),repeat=3) if compat[1,3,c[0],c[1]] and compat[1,5,c[0],c[2]] and compat[3,5,c[1],c[2]]]
assert len(survivors)==216
cert=json.load(open('research/searches/regular-pentagon-heptagon-144-126-first-gate-sol-2026-10-19.json'))
assert survivors==cert['simultaneous_stars']
assert len(cert['joins'])==18 and all(not x['overlaps'] for x in cert['joins'])
print('VALID: independent AA polyhedron checks; base, 18 joins, 216 triples')
