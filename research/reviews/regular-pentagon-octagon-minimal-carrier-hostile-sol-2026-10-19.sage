# Independent exact checker: no producer code imported or executed.
from sage.all import *
from itertools import permutations
import json
from pathlib import Path
K=CyclotomicField(20, 'z'); z=K.gen(); S=PolynomialRing(K,'t'); t=S.gen()
def cj(a): return S([c.conjugate() for c in S(a)])
def wedge(a,b): return (cj(a)*b-cj(b)*a)/(2*z**5)
def positive_poly(a, strict_constant=False):
    a=S(a)
    assert all(QQbar(c).imag()==0 and QQbar(c).real()>=0 for c in a)
    assert a!=0
    if strict_constant: assert QQbar(a[0]).real()>0
sizes=[5,5,8]; offsets=[0,5,10]
face=lambda d: 0 if d<5 else (1 if d<10 else 2)
nextdart=lambda d: offsets[face(d)]+(d-offsets[face(d)]+1)%sizes[face(d)]
# Union the two endpoint identifications of every edge independently.
def vertices(pairs):
    uf=list(range(18))
    def root(x):
        while uf[x]!=x: x=uf[x]
        return x
    for a,b in pairs:
        for x,y in [(a,nextdart(b)),(nextdart(a),b)]: uf[root(x)]=root(y)
    return sorted([sorted(d for d in range(18) if root(d)==r) for r in set(root(d) for d in range(18))])
pp=[0,2,5,7]; pq=[1,3,4,6,8,9]
matchings=[[(pp[0],pp[i]),tuple(d for j,d in enumerate(pp) if j not in (0,i))] for i in (1,2,3)]
results={}
for word,private in [('AAABBABB',{3,6}),('AABBAABB',{2,6})]:
    count=[0,0,0]; good=[]
    for reflected in (False,True):
        types=list('AAAABAAAAB')+[word[(-i)%8] if reflected else word[i] for i in range(8)]
        hidden={i for i in range(8) if (-(i+1))%8 in private} if reflected else private
        public=[10+i for i in range(8) if i not in hidden]
        for m in matchings:
            for images in permutations(public):
                count[0]+=1
                pairs=m+list(zip(pq,images))+[tuple(10+i for i in sorted(hidden))]
                if any(types[a]!=types[nextdart(b)] or types[nextdart(a)]!=types[b] for a,b in pairs): continue
                count[1]+=1
                vs=vertices(pairs)
                if any(tuple(sorted('P' if d<10 else types[d] for d in v)) not in [('A','P','P'),('B','B','P')] for v in vs): continue
                count[2]+=1; good.append((reflected,sorted(tuple(sorted(p)) for p in pairs)))
    results[word]=(count,good)
assert results['AAABBABB'][0]==[4320,48,0]
assert results['AABBAABB'][0]==[4320,48,4]
data=json.loads(Path('research/searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.json').read_text())['results']
for word,(count,good) in results.items():
    assert count==[data[word]['counts'][k] for k in ['pairings','endpoint_compatible','stars']]
    assert sorted(good)==sorted((r['reflected'],sorted(tuple(sorted(p)) for p in r['pairs'])) for r in data[word]['records'])
# Independent isolated metric reconstruction by linear closure.
w0='AAABBABB'; dirs=[K(1)]
for i in range(1,8): dirs.append(dirs[-1]*z**(2 if w0[i]=='A' else 3))
length=-sum(dirs[i] for i in range(8) if i not in (3,6))/(dirs[3]+dirs[6])
assert length==-z**7+z**5-z**3+2*z
assert QQbar(length).imag()==0 and QQbar(length).real()>0
assert dirs[3]==z**7 and dirs[6]==z**15 and dirs[3]!=-dirs[6]
QI=[S(0)]
for i in range(8): QI.append(QI[-1]+(length if i in (3,6) else 1)*dirs[i])
assert QI[-1]==0; QI=QI[:-1]
for i in range(8):
    for j in range(8):
        if j not in [i,(i+1)%8]: positive_poly(wedge(QI[(i+1)%8]-QI[i],QI[j]-QI[i]))
# Reconstruct first positive carrier from native geometry, never parse producer coordinates.
P=[S(sum(z**(4*j) for j in range(i))) for i in range(5)]
Q=[S(0)]; direction=K(1); word='AABBAABB'
for i in range(8):
    Q.append(Q[-1]+(t if i in (2,6) else 1)*direction)
    direction*=z**(2 if word[(i+1)%8]=='A' else 3)
assert Q[-1]==0; Q=Q[:-1]
# All supporting inequalities, exact throughout the open parameter half-line.
for i in range(8):
    edge=Q[(i+1)%8]-Q[i]
    for j in range(8):
        if j not in [i,(i+1)%8]: positive_poly(wedge(edge,Q[j]-Q[i]))
T=[P,[1-v for v in P],[1+z**4-z**4*v for v in Q]]
L=[S(z**6+z**4+z**2),S((z**7-z**5+z**3-z)*t+2*z**6-1)]
pairs=[(0,5),(2,7),(1,10),(3,13),(4,15),(6,14),(8,17),(9,11),(12,16)]
coeff=[(0,0),(1,0),(0,0),(0,1),(-1,1),(-1,1),(-1,0),(0,0),(-1,0)]
coord=lambda d:T[face(d)][d-offsets[face(d)]]
for (a,b),(u,v) in zip(pairs,coeff):
    assert coord(a)-coord(nextdart(b))==u*L[0]+v*L[1]
    assert coord(nextdart(a))-coord(b)==u*L[0]+v*L[1]
vs=vertices(pairs)
assert len(vs)==6 and all(len(v)==3 for v in vs)
# Check the corner link really is one 3-cycle at each union-find vertex.
alpha={a:b for a,b in pairs}; alpha.update({b:a for a,b in pairs})
for v in vs:
    start=v[0]; walk=[]; d=start
    while d not in walk: walk.append(d); d=nextdart(alpha[d])
    assert d==start and sorted(walk)==v
    assert sum(108 if d<10 else (144 if word[d-10]=='A' else 126) for d in v)==360
area=lambda poly:sum(wedge(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2
for poly in T: positive_poly(area(poly),True)
det=wedge(*L); positive_poly(det,True)
assert det==sum(area(poly) for poly in T)
assert 3-9+len(vs)==0
print('PASS: independent 4320-case domains, exact first carrier, all t>0 convexity, links, shifts, positive determinant and degree-one area identity')
