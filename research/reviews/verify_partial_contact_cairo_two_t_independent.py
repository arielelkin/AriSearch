#!/usr/bin/env python3
"""Independent exact reconstruction of the changed Cairo pair and event graph."""
from itertools import combinations_with_replacement
from sage.all import QuadraticField, vector
K = QuadraticField(3, 'w')
w = K.gen()
a, b, c, d, e, f = K(1), K(2), 2*w-1, w-1, K(3), 3-w
words = [(a,b,c,d,e), (a,c,d,b,f)]
dirs = [vector(K,t) for t in [(1,0),(0,1),(-w/2,K(1)/2),
                              (-K(1)/2,-w/2),(K(1)/2,-w/2)]]
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
for word in words:
    assert all(x>0 for x in word)
    assert len(set(word))==5
    points=[vector(K,[0,0])]
    for length,direction in zip(word,dirs): points.append(points[-1]+length*direction)
    assert points[-1] == points[0]
    points=points[:-1]
    for i in range(5):
        edge=points[(i+1)%5]-points[i]
        assert edge.dot_product(edge)==word[i]**2
        for j in range(5):
            if j not in {i,(i+1)%5}:
                assert cross(edge,points[j]-points[i])>0
slots=[]
for species,word in enumerate(words):
    for i,j in [(0,1),(2,3)]:
        slots.extend([(species,i,j,word[i],word[j]),
                      (species,j,i,word[j],word[i])])
events=[]
for x,y in combinations_with_replacement(slots,2):
    if x[3]==y[3]:events.append((x[3],x[4],y[4]))
assert len(slots)==8 and len(events)==12
sums={r+s for u,r,s in events}
assert sums=={2*a,2*b,2*c,2*d,b+c,a+d}
assert len(sums)==6 and e not in sums and f not in sums
compatible={(x,x) for x in (a,b,c,d)}
for u,r,s in events:
    for v,t,q in events:
        if r+s != t+q:continue
        for m,n in [(r,s),(s,r)]:
            for M,Q in [(t,q),(q,t)]:
                if 0<m<M<m+n and Q<n:
                    compatible.update([(m,M),(M,m)])
assert compatible=={(x,x) for x in (a,b,c,d)}|{(a,d),(d,a),(b,c),(c,b)}
# An e seam forces both exposed rays to the {a,d} component.
isolated=[(word[1],word[2]) for word in words]
assert all(not (x in {a,d} and y in {a,d}) for x,y in isolated)
assert e!=f and e not in {a,b,c,d} and f not in {a,b,c,d}
print('PASS: 2 exact convex pentagons; 8 slots; 12 events; 6 distinct sums; complete compatibility graph and isolated-corner obstruction')
