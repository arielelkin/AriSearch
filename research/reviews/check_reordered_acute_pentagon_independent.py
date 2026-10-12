#!/usr/bin/env python3
"""Fresh reordered-pentagon census, eligible-host and torus audit.
No producer imports. The retained certificate is data, not executable code.
"""
from itertools import combinations_with_replacement
from collections import Counter
from pathlib import Path
import json

ang=(130,281,150,295,224,80,289,272,94,345)
def census(total):
    return [r for n in range(1,total//min(ang)+1)
            for r in combinations_with_replacement(range(10),n)
            if sum(ang[i] for i in r)==total]
flat=census(360);full=census(720)
assert flat==[(0,2,5)]
assert len(full)==9
assert set(full)=={
             (0,3,3),(0,4,7,8),(0,0,7,8,8),(0,0,2,2,5,5),
             (1,2,6),(1,8,9),(3,5,9),(4,4,7),(5,)*9}
def supported(*pair):return any(not Counter(pair)-Counter(r) for r in full)
eligible={j for r in flat for j in r}
assert eligible=={0,2,5}
for pair in [(4,6),(4,9),(1,1),(1,3),(4,1),(4,3),(4,2),(2,9),(4,5),(1,0),(3,7)]:
    assert not supported(*pair),pair
assert supported(3,9) and supported(4,4) and supported(1,2)
# Host endpoints can either complete at the outer corner or, if eligible,
# end EARLIER in the outer ray. This expressly includes omitted A2/B4 cases.
hosts=[]
for species in range(2):
    for side in range(5):
        endpoints=(species*5+side,species*5+(side+1)%5)
        if any(all(h in eligible or supported(o,h) for o,h in zip((4,3),order))
               for order in (endpoints,endpoints[::-1])):
            hosts.append((species,side))
assert hosts==[(0,2),(0,3),(0,4),(1,3),(1,4)]
# Exhaust seam choices at P and D against complete far support.
def incident(c):
    sp,j=divmod(c,5)
    return [(sp*5+(j-1)%5,sp*5+(j-1)%5),(sp*5+j,sp*5+(j+1)%5)]
def seams(c,d):
    return [(i,j) for i,a in incident(c) for j,b in incident(d) if supported(a,b)]
assert seams(3,5)==[(2,5)]        # A2/B0
assert seams(2,6)==[(2,5)]        # A2/B0
assert seams(3,9)==[(2,9),(3,8)]  # A2/B4 or A3/B3, prior P choice selects latter
assert seams(2,1)==[(1,1),(2,0)]  # prior D beta/delta choice selects A1/A1
# Read torus pairs and reconstruct corner links directly.
data=json.loads(Path('research/certificates/reordered-acute-pentagon-four-face-carrier.json').read_text())
pairs=[(tuple(p),tuple(q)) for p,q in data['edge_pairs_reversed_boundary']]
expected=[((0,1),(1,1)),((0,4),(1,4)),((2,2),(3,2)),((2,4),(3,4)),
          ((0,0),(2,1)),((1,0),(3,1)),((0,2),(3,0)),((1,2),(2,0)),
          ((0,3),(2,3)),((1,3),(3,3))]
assert pairs==expected
assert Counter(h for pq in pairs for h in pq)==Counter((f,i) for f in range(4) for i in range(5))
next_corner={};adj={f:set() for f in range(4)}
for (f,i),(g,j) in pairs:
    next_corner[(f,i)]=(g,(j+1)%5)
    next_corner[(g,j)]=(f,(i+1)%5)
    adj[f].add(g);adj[g].add(f)
assert set(next_corner)==set(next_corner.values())
unseen=set(next_corner);cycles=[]
while unseen:
    start=min(unseen);c=start;cycle=[]
    while c not in cycle:
        cycle.append(c);c=next_corner[c]
    assert c==start
    unseen-=set(cycle);cycles.append(cycle)
assert len(cycles)==6
assert {frozenset(c) for c in cycles}=={frozenset(tuple(v) for v in r['corners']) for r in data['vertices']}
vertex_types=[]
for cycle in cycles:
    vals=[ang[5*(f//2)+i] for f,i in cycle]
    assert sum(vals)==720
    vertex_types.append(tuple(sorted(vals)))
assert Counter(vertex_types)=={(150,281,289):2,(80,295,345):2,(94,130,224,272):2}
seen={0};todo=[0]
while todo:
    for g in adj[todo.pop()]-seen:seen.add(g);todo.append(g)
assert seen==set(range(4))
assert len(cycles)-len(pairs)+4==0
# Every glued seam is either same-species/same-native-index or one of3aliases.
aliases={(0,6),(2,5),(3,8)}
for (f,i),(g,j) in pairs:
    a=5*(f//2)+i;b=5*(g//2)+j
    assert a==b or (min(a,b),max(a,b)) in aliases
print('PASS: exact support; all five eligible-endpoint host types; P/D seams; independent six vertex cycles and all torus metric aliases')

# Ancillary exact nonempty normalized metric region, independently solved.
from sage.all import AA, QQ, QQbar, matrix, vector
zeta=QQbar.zeta(720)
directionA=(0,79,289,354,490);directionB=(0,71,159,425,440)
def edge_units(ds):return [vector(AA,(AA((zeta**j).real()),AA((zeta**j).imag()))) for j in ds]
def angle_word(ds):return tuple(360-((ds[i]-ds[i-1])%720) for i in range(5))
assert angle_word(directionA)==ang[:5]
assert angle_word(directionB)==ang[5:]
ea,eb=edge_units(directionA),edge_units(directionB)
MA=matrix(AA,[[ea[0][j],ea[4][j]] for j in range(2)])
MB=matrix(AA,[[eb[2][j],eb[4][j]] for j in range(2)])
assert MA.det()!=0 and MB.det()!=0
def lengths(t,d):
    a0,a4=MA.solve_right(-(t*ea[1]+ea[2]+d*ea[3]))
    al=[a0,t,AA(1),d,a4]
    b2,b4=MB.solve_right(-(eb[0]+a0*eb[1]+d*eb[3]))
    bl=[AA(1),a0,b2,d,b4]
    assert sum((l*e for l,e in zip(al,ea)),vector(AA,(0,0)))==vector(AA,(0,0))
    assert sum((l*e for l,e in zip(bl,eb)),vector(AA,(0,0)))==vector(AA,(0,0))
    assert al[0]==bl[1] and al[2]==bl[0] and al[3]==bl[3]
    return al,bl
# Basis checks establish the published affine formulas identically in t,d.
for t,d in [(AA(0),AA(0)),(AA(1),AA(0)),(AA(0),AA(1))]:
    al,bl=lengths(t,d)
    assert al[4]==-(t*ea[1][1]+ea[2][1]+d*ea[3][1])/ea[4][1]
    rx=-(bl[0]+bl[1]*eb[1][0]+bl[3]*eb[3][0])
    ry=-(bl[1]*eb[1][1]+bl[3]*eb[3][1])
    determinant=eb[2][0]*eb[4][1]-eb[2][1]*eb[4][0]
    assert bl[2]==(rx*eb[4][1]-ry*eb[4][0])/determinant
    assert bl[4]==(eb[2][0]*ry-eb[2][1]*rx)/determinant
al,bl=lengths(AA(QQ(1)/10),AA(QQ(1)/5))
assert all(l>0 for l in al+bl)
def determinant(v,w):return v[0]*w[1]-v[1]*w[0]
for ls,units in [(al,ea),(bl,eb)]:
    es=[l*e for l,e in zip(ls,units)]
    ps=[vector(AA,(0,0))]
    for e in es[:-1]:ps.append(ps[-1]+e)
    assert all(determinant(es[i],ps[j]-ps[i])>0 for i in range(5) for j in range(5) if j not in (i,(i+1)%5))
sample=json.loads(Path('research/certificates/reordered-acute-pentagon-periodic-sample.json').read_text())
assert sample['A_direction_doubled_degrees']==list(directionA)
assert sample['B_direction_doubled_degrees']==list(directionB)
assert sample['exact_closure_convexity_aliases'] is True
print('PASS: independent exact positive sample, native angle order, two closure systems, all strict supports, aliases, and affine parameter formulas')
