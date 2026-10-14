#!/usr/bin/env python3
"""Fresh exact local obstruction, independent of CP-SAT and atom producer."""
from itertools import combinations_with_replacement, permutations, product
from sage.all import AA, QQ

polygons=[('P',[(0,0),(2,0),(3,2),(2,3),(0,2)],'rabba'),
          ('Q',[(2,3),(1,4),(-1,4),(-2,3),(0,2)],'cggcd')]
for typ,vertices,_ in polygons:
    for i,(x,y) in enumerate(vertices):
        if typ=='P':
            assert (y,x)==vertices[(-i)%5]
        else:
            assert (-x,y)==vertices[(3-i)%5]
angle_vectors={'r':(2,0),'a':(4,-1),'b':(1,1),'c':(3,-1),'g':(3,0),'d':(0,2)}
cosines={'r':AA(0),'a':-1/AA(5).sqrt(),'b':-1/AA(10).sqrt(),
         'c':1/AA(10).sqrt(),'g':-1/AA(2).sqrt(),'d':AA(-3)/5}
arms={}
sides=[]
for typ,vertices,word in polygons:
    for i,(point,label) in enumerate(zip(vertices,word)):
        previous=vertices[i-1];nxt=vertices[(i+1)%5]
        vectors=[tuple(v[j]-point[j] for j in range(2)) for v in (previous,nxt)]
        norms=[sum(q*q for q in v) for v in vectors]
        cosine=AA(sum(x*y for x,y in zip(*vectors)))/(AA(norms[0]*norms[1]).sqrt())
        assert cosine==cosines[label]
        assert -1 < cosine < AA(1)/2
        assert vectors[1][0]*vectors[0][1]-vectors[1][1]*vectors[0][0] > 0
        signature=tuple(sorted(((norms[0],word[i-1]),(norms[1],word[(i+1)%5]))))
        assert label not in arms or arms[label]==signature
        arms[label]=signature
        sides.append((typ,i,norms[1],label,word[(i+1)%5]))

angle_stars=[]
for k in range(2,6):
 for word in combinations_with_replacement(sorted(angle_vectors),k):
  if tuple(sum(angle_vectors[t][j] for t in word) for j in range(2))==(8,0):
   angle_stars.append(word)
assert {''.join(w) for w in angle_stars}=={'aad','abg','ggr','bbcc','bcrr','ccdr','rrrr'}
star_rays={}
for word in angle_stars:
    rays=set()
    for order in set(permutations(word)):
        for flips in product((0,1),repeat=len(order)):
            oriented=[arms[t][::-1] if f else arms[t] for t,f in zip(order,flips)]
            if all(oriented[i][1][0]==oriented[(i+1)%len(order)][0][0] for i in range(len(order))):
                for i,t in enumerate(order):
                    rays.add((tuple(sorted((t,order[(i+1)%len(order)]))),oriented[i][1][0]))
    if rays:
        star_rays[''.join(word)]=rays
assert set(star_rays)=={'aad','abg','ggr','bbcc','rrrr'}
assert star_rays['ggr']=={(('g','g'),2),(('g','r'),4)}
assert star_rays['abg']=={(('a','b'),5),(('b','g'),2),(('a','g'),4)}
all_rays=set().union(*star_rays.values())
assert (('g','g'),4) not in all_rays
assert (('a','r'),4) not in all_rays
# Native side occurrences, retaining endpoints and multiplicities.
assert {tuple(sorted((a,b))) for _,_,s,a,b in sides if s==4}=={('a','r'),('g','g')}
assert {tuple(sorted((a,b))) for _,_,s,a,b in sides if s==5}=={('a','b'),('c','d')}
assert {tuple(sorted((a,b))) for _,_,s,a,b in sides if s==2}=={('b','b'),('c','g')}
# Follow one Q GG4 seam. Q-Q is impossible because its GG4 ray is absent.
# It must meet P RA4, putting that P's R at GGR. Both R4 rays meet G4,
# and every G4 native side has G at its other end: both P A corners are ABG.
assert arms['r']==((4,'a'),(4,'a'))
assert [other for s,other in arms['g'] if s==4]==['g']
assert {star for star,rays in star_rays.items() if (('a','g'),4) in rays}=={'abg'}
# At ABG the A5 ray meets B5; every B5 side has A at its far end.
# Hence both B corners of the original P become ABG as well.
assert [other for s,other in arms['b'] if s==5]==['a']
assert {star for star,rays in star_rays.items() if (('a','b'),5) in rays}=={'abg'}
# Both ends of original P BB2 would now require a G on the other side,
# but no native GG2 side exists. This is the contradiction.
assert (('b','g'),2) in star_rays['abg']
assert not any(s==2 and a==b=='g' for _,_,s,a,b in sides)
# P alone has no full star at its A corner (and none at B).
assert not any('a' in star and set(star)<=set('rab') for star in star_rays)
assert (QQ(-6)/5).denominator()==5
print('PASS: exact actual angles, seven-to-five ray atlas, forced far endpoints, no native GG2; no full-edge cover')
