#!/usr/bin/env python3
"""Exact arithmetic ledger for the unrestricted Y-pair obstruction.

Domain: ten indexed native vertices and sides, six exact angle labels,
all multisets of two through five native angles and one through two
angles totaling a flat sector. No placement search and no solver.
Sage AA supplies exact real-algebraic inequalities. The irrationality of
atan(2)/pi is imported from the reviewed interface source, not inferred
numerically here. Run with assertions enabled.
"""
from itertools import combinations_with_replacement
from sage.all import AA

POLYGONS = [
    ('P', [(0,0),(2,0),(3,2),(2,3),(0,2)], 'rabba'),
    ('Q', [(2,3),(1,4),(-1,4),(-2,3),(0,2)], 'cggcd'),
]
VECTORS = {'r':(2,0),'a':(4,-1),'b':(1,1),
           'c':(3,-1),'g':(3,0),'d':(0,2)}
COS = {'r':AA(0), 'a':-1/AA(5).sqrt(), 'b':-1/AA(10).sqrt(),
       'c':1/AA(10).sqrt(), 'g':-1/AA(2).sqrt(), 'd':AA(-3)/5}
SIDES = []
ARMS = {}
for species, vertices, word in POLYGONS:
    for i, point in enumerate(vertices):
        previous, nxt = vertices[i-1], vertices[(i+1)%5]
        u = tuple(previous[j]-point[j] for j in range(2))
        v = tuple(nxt[j]-point[j] for j in range(2))
        u2, v2 = sum(x*x for x in u), sum(x*x for x in v)
        assert v[0]*u[1]-v[1]*u[0] > 0  # strict convexity
        cosine = AA(sum(x*y for x,y in zip(u,v)))/AA(u2*v2).sqrt()
        label = word[i]
        assert cosine == COS[label]
        arms = tuple(sorted(((u2,word[i-1]),(v2,word[(i+1)%5]))))
        assert label not in ARMS or ARMS[label] == arms
        ARMS[label] = arms
        SIDES.append((species,i,v2,label,word[(i+1)%5]))

assert all(-1 < x < AA(1)/2 for x in COS.values())  # angles in (pi/3,pi)
assert COS['c'] == max(COS.values())  # c is least
# Cos(pi - alpha) = -cos(alpha), hence these residuals are less than c.
assert all(-COS[label] > COS['c'] for label in ('a','d','g'))

def angle_multisets(target, sizes):
    return {''.join(w) for n in sizes
            for w in combinations_with_replacement(sorted(VECTORS), n)
            if tuple(sum(VECTORS[x][j] for x in w) for j in (0,1)) == target}

stars = angle_multisets((8,0), range(2,6))
flats = angle_multisets((4,0), range(1,3))
assert stars == {'aad','abg','ggr','rrrr','bcrr','ccdr','bbcc'}
assert flats == {'rr','bc'}
assert {w for w in stars if all(x in w for x in ('r','g'))} == {'ggr'}
assert {w for w in stars if all(x in w for x in ('a','g'))} == {'abg'}
assert {w for w in stars if all(x in w for x in ('a','b'))} == {'abg'}
assert not any('a' in w and set(w) <= set('rab') for w in stars)
assert {tuple(sorted((a,b))) for _,_,l,a,b in SIDES if l == 4} == {('a','r'),('g','g')}
assert {tuple(sorted((a,b))) for _,_,l,a,b in SIDES if l == 2} == {('b','b'),('c','g')}
assert ARMS['r'] == ((4,'a'),(4,'a'))
assert ARMS['g'] == ((2,'c'),(4,'g'))
assert ARMS['b'] == ((2,'b'),(5,'a'))
assert ARMS['a'] == ((4,'r'),(5,'b'))

short = AA(2).sqrt()
long = AA(5).sqrt()
minimum = min(AA(side[2]).sqrt() for side in SIDES)
assert minimum == short
assert 2*minimum > 2  # GG cannot split into two entire guest sides
assert 0 < short < 2
assert 0 < 2-short < minimum  # C inside RA forces overhanging B arm past A
assert short < long  # B cannot use reviewed full-mate BB on host AB
assert not any(l == 2 and a == b == 'g' for _,_,l,a,b in SIDES)
# The final contradiction needs both endpoints of the SAME P's BB.
p_vertices, p_word = POLYGONS[0][1:]
r_index = p_word.index('r')
a_indices = {(r_index-1)%5,(r_index+1)%5}
b_indices = set()
for a_i in a_indices:
    assert p_word[a_i] == 'a'
    neighbors = {(a_i-1)%5,(a_i+1)%5}
    b_i, = neighbors - {r_index}
    assert p_word[b_i] == 'b'
    b_indices.add(b_i)
assert b_indices == {2,3}
assert any(a == b == 'b' and i in b_indices and (i+1)%5 in b_indices
           for species,i,l,a,b in SIDES if species == 'P')
print('PASS: exact geometry; seven native/two flat stars; GG full-mate and RA guard inequalities; actual-P endpoint propagation.')
print('Scope: arithmetic ledger supporting the written unrestricted theorem, using the separately reviewed full-BB-mate theorem.')
