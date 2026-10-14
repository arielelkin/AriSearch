#!/usr/bin/env python3
"""Independent exact native-star/count gate; no atom-module imports."""
from itertools import combinations_with_replacement, permutations, product
from fractions import Fraction as F

angles = {'r':(2,0),'a':(4,-1),'b':(1,1),'c':(3,-1),'g':(3,0),'d':(0,2)}
stars = []
for k in range(2,6):
    for word in combinations_with_replacement(sorted(angles), k):
        if tuple(sum(angles[t][i] for t in word) for i in range(2)) == (8,0):
            stars.append(''.join(word))
assert set(stars) == {'rrrr','ggr','aad','bbcc','abg','bcrr','ccdr'}
corners = [list(zip('rabba',[(0,0),(2,0),(3,2),(2,3),(0,2)])),
           list(zip('cggcd',[(2,3),(1,4),(-1,4),(-2,3),(0,2)]))]
length4_edges = []
arms = {}
for face in corners:
    found = []
    for i,(label,point) in enumerate(face):
        nxt, other = face[(i+1)%5]
        squared = sum((point[j]-other[j])**2 for j in range(2))
        if squared == 4:
            found.append((label,nxt))
        previous = face[i-1][1]
        previous_squared = sum((point[j]-previous[j])**2 for j in range(2))
        signature = tuple(sorted((previous_squared,squared)))
        assert label not in arms or arms[label] == signature
        arms[label] = signature
    length4_edges.append(found)
assert {frozenset(e) for e in length4_edges[0]} == {frozenset('ra')}
assert {frozenset(e) for e in length4_edges[1]} == {frozenset('gg')}
def length_compatible(word):
    for order in set(permutations(word)):
        for flips in product((0,1), repeat=len(order)):
            oriented = [arms[t][::-1] if flip else arms[t] for t,flip in zip(order,flips)]
            if all(oriented[i][1] == oriented[(i+1)%len(order)][0] for i in range(len(order))):
                return True
    return False
stars = [word for word in stars if length_compatible(word)]
assert set(stars) == {'rrrr','ggr','aad','bbcc','abg'}
equal_count_stars = {'ggr','aad','bbcc'}
def admits(pair, allowed):
    return any(all(word.count(t) >= pair.count(t) for t in pair) for word in allowed)
assert not admits('ra', stars)
assert admits('rr',stars) and not admits('rr',equal_count_stars)
assert admits('ag',stars) and not admits('ag',equal_count_stars)
# At g the two arms have squared lengths 2 and 4, whereas r has 4 and 4.
# Thus the gg adjacency in an rgg star is forced onto length sqrt(2),
# never the Q's length-2 gg side. The latter must meet a P ra side.
# Counting its r and a endpoints gives 2*x=q and t=q.
for w in range(1,4):
 p,q,x,y,z,t = 6*w,4*w,2*w,4*w,4*w,4*w
 assert (x+4*w,2*y+t,2*z+t,2*z,2*x+t,y)==(p,2*p,2*p,2*q,2*q,q)
 assert 2*x==q and t==q
 assert (x+y+z+t+w) - 5*(p+q)/2 + (p+q)==0
# Independent solving of native incidence counts in the declared 2P+2Q domain.
solutions=[]
for x in range(7):
 for y in range(7):
  for z in range(7):
   for t in range(7):
    for w in range(7):
     if (x+4*w,2*y+t,2*z+t,2*z,2*x+t,y)==(2,4,4,4,4,2):
      solutions.append((x,y,z,t,w))
assert solutions == [(2,2,2,0,0)]
# θ=atan(2): a rational θ/π would make exp(2iθ) a root of unity,
# whose trace 2*cos(2θ) would be an algebraic integer. Here trace=-6/5.
assert F(2)*(F(1)-F(4))/(F(1)+F(4)) == F(-6,5)
print('PASS: exhaustive exact native stars; 2P+2Q count solution; every P length-2 contact obstructed')
