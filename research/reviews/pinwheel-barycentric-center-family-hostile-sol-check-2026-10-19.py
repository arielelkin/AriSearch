"""Independent reconstruction; no imports from candidate producers or certificates."""
from fractions import Fraction as R
from functools import cmp_to_key
from pathlib import Path
import json
import sympy as S

def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,k): return tuple(x*k for x in a)
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def on(x,a,b): return det(minus(x,a),minus(b,a))==0 and dot(minus(x,a),minus(x,b))<=0
def frame(t):
    o=next(a for a in t if dot(minus(t[(t.index(a)+1)%3],a),minus(t[(t.index(a)+2)%3],a))==0)
    ends=sorted((a for a in t if a!=o),key=lambda a:dot(minus(a,o),minus(a,o)))
    return o,ends[1],ends[0]
def orient(t):
    return t if det(minus(t[1],t[0]),minus(t[2],t[0]))>0 else t[::-1]
raw=[[(0,0),(2,0),(2,1)],[(2,0),(4,0),(4,1)],[(4,0),(5,0),(4,2)],[(2,1),(4,1),(4,2)],[(2,0),(4,1),(2,1)]]
template=[tuple((R(10-2*x-y,5),R(x-2*y,5)) for x,y in t) for t in raw]
base=((R(0),R(0)),(R(2),R(0)),(R(0),R(1)))
triangles=[base]
for level in range(3):
    nxt=[]
    for t in triangles:
        o,l,s=frame(t)
        nxt += [orient(tuple(plus(o,plus(scale(minus(l,o),x/2),scale(minus(s,o),y))) for x,y in c)) for c in template]
    triangles=nxt
assert len(triangles)==125
assert sum(det(minus(t[1],t[0]),minus(t[2],t[0]))/2 for t in triangles)==1
for t in triangles:
    assert all(det(minus(b,a),minus(x,a))>=0 for x in t for a,b in zip(base,base[1:]+base[:1]))
    o,l,s=frame(t)
    assert dot(minus(l,o),minus(l,o))==4*dot(minus(s,o),minus(s,o))
for i,t in enumerate(triangles):
    for u in triangles[:i]:
        assert any(max(dot(x,n) for x in t)<=min(dot(x,n) for x in u) or max(dot(x,n) for x in u)<=min(dot(x,n) for x in t)
                   for f in (t,u) for a,b in zip(f,f[1:]+f[:1]) for n in [(-(b[1]-a[1]),b[0]-a[0])])
vertices=set(x for t in triangles for x in t)
# Planarized edges as independent oriented cycles for each source face.
faces=[]
for t in triangles:
    cycle=[]
    for a,b in zip(t,t[1:]+t[:1]):
        cycle += sorted((x for x in vertices if x!=b and on(x,a,b)),key=lambda x:dot(minus(x,a),minus(b,a)))
    faces.append((t,cycle))
interior=[v for v in sorted(vertices) if not any(on(v,a,b) for a,b in zip(base,base[1:]+base[:1]))]
assert len(interior)==81
p,q=S.symbols('p q')
def boundary(v,pv,qv):
    pieces=[]
    for t,cycle in faces:
        if v not in cycle: continue
        i=cycle.index(v);o,l,s=frame(t)
        c=plus(o,plus(scale(minus(l,o),pv),scale(minus(s,o),qv)))
        # Face interior is left of its oriented planarized boundary.
        pieces.append((scale(plus(v,cycle[(i+1)%len(cycle)]),R(1,2)),c,scale(plus(v,cycle[i-1]),R(1,2))))
    # Trace oriented arcs, checking exactly one incoming/outgoing arc per seam.
    assert len({a for a,c,b in pieces})==len(pieces)==len({b for a,c,b in pieces})
    assert {a for a,c,b in pieces}=={b for a,c,b in pieces}
    pieces.sort(key=lambda z:z[0]);start=pieces[0][0];cur=start;poly=[]
    while True:
        a,c,b=next(z for z in pieces if z[0]==cur)
        poly.extend((a,c));cur=b
        if cur==start:break
        assert len(poly)<=2*len(pieces)
    assert len(poly)==2*len(pieces)
    return poly
wanted=[((R(1,25),R(2,25)),0),((R(1,25),R(2,25)),2),((R(1,25),R(22,25)),6),((R(1,5),R(1,5)),4)]
f=-4*p*p+3*p-q*q+q/2;g=f-2*p
for (v,i),expr in zip(wanted,[f,g,-g,-f]):
    b=boundary(v,p,q)
    turn=S.expand(det(minus(b[i],b[i-1]),minus(b[(i+1)%len(b)],b[i])))
    assert S.expand(turn-expr/125)==0,(v,i,turn)
print('PASS independent source, planarization, cyclic boundary, F/G/-G/-F identities')

def reduce(poly):
    while True:
        idx=next((i for i in range(len(poly)) if det(minus(poly[i],poly[i-1]),minus(poly[(i+1)%len(poly)],poly[i]))==0),None)
        if idx is None:return poly
        # Verify removed point is between neighbors, not a backtracking spike.
        assert dot(minus(poly[idx],poly[idx-1]),minus(poly[idx],poly[(idx+1)%len(poly)]))<=0
        poly.pop(idx)
def canonical(poly):
    keys=[]
    for seq in (poly,poly[::-1]):
        for j in range(len(seq)):
            z=seq[j:]+seq[:j]
            keys.append(tuple(dot(minus(x,y),minus(x,y)) for i,x in enumerate(z) for y in z[:i]))
    return min(keys)
for name,value,expected in [('centroid',R(1,3),(50,3)),('fifth',R(1,5),(40,2))]:
    convex=[]
    suffix='' if name=='centroid' else '-fifth'
    fixture=json.loads((Path(__file__).parents[1]/'searches'/('pinwheel-barycentric-crossboundary-2026-10-19'+suffix+'.json')).read_text())
    for v in interior:
        b=reduce(boundary(v,value,value))
        assert sum(det(b[i],b[(i+1)%len(b)]) for i in range(len(b)))>0
        turns=[det(minus(b[i],b[i-1]),minus(b[(i+1)%len(b)],b[i])) for i in range(len(b))]
        good=all(x>0 for x in turns)
        row=next(r for r in fixture['cells'] if tuple(map(R,r['source_vertex']))==v)
        assert canonical(b)==canonical([tuple(map(R,x)) for x in row['boundary']])
        assert row['strict_convex']==good
        if good:convex.append(canonical(b))
    assert (len(convex),len(set(convex)))==expected
    print('PASS',name,len(interior),'cells',len(convex),'convex',len(set(convex)),'classes; every fixture cell matched')
