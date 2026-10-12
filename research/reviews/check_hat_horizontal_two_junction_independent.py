#!/usr/bin/env python3
"""Exact fresh hat two-junction audit; no producer imports or sampling proof."""
from sage.all import AA, QQ, NumberField, PolynomialRing, vector
from collections import Counter
T=PolynomialRing(QQ,'t');t=T.gen()
K=NumberField(t*t-3,'r',embedding=AA(3).sqrt());r=K.gen()
R=PolynomialRing(K,'b');b=R.gen();half=QQ(1)/2
H=[(0,0),(-r*b/2,-b/2),(-r*b/2+half,-b/2-r/2),
   (-r*b/2+QQ(5)/2,-b/2-r/2),(-r*b/2+3,-b/2),(3,-b),
   (r*b/2+3,-b/2),(r*b/2+QQ(5)/2,-b/2+r/2),
   (r*b/2+QQ(3)/2,-b/2+r/2),(r*b/2+QQ(3)/2,b/2+r/2),
   (QQ(3)/2,b+r/2),(1,b),(0,b)]
H=[vector(R,p) for p in H]
V=vector(R,((r*b+1)/2,(r-b)/2))
def det(v,w):return v[0]*w[1]-v[1]*w[0]
assert H[8]-V==vector(R,(1,0))
assert H[7]-V==vector(R,(2,0))
assert V-H[11]==(r*b-1)*vector(R,(half,-r/2))
P=[V,H[8],H[9],H[10],H[11]]
turns=[det(P[i]-P[i-1],P[(i+1)%5]-P[i]) for i in range(5)]
assert turns==[(3*b-r)/2,b,r*b*b/2,b,(3*b-r)/2]
units=[vector(K,z) for z in [(1,0),(0,1),(-r/2,half),(-half,-r/2),(half,-r/2)]]
assert all(e.dot_product(e)==1 for e in units)
assert [-units[i-1].dot_product(units[i]) for i in range(5)]==[-half,0,-half,0,-half]
# The only allowable outgoing h0 directions are330 and0; F=b.
W1=vector(R,(r*b/2,-b/2));W2=vector(R,(b,0))
assert det(W1-H[4],H[0]-W1)==(r*b-3)*b/2
assert det(H[4]-H[3],W1-H[4])==-r*(r*b-3)/2
assert all(z(r)==0 for z in W1-H[4])
assert (V-W1).dot_product(V-W1)==1
assert (V-W2).dot_product(V-W2)-1==b*((2-r)*b-1)
assert 1/(2-r)==2+r
turn2=det(H[4]-H[3],W2-H[4])
assert turn2==(3*r-(1+r)*b)/2
assert turn2(2+r)==-QQ(5)/2
# Independent exact nonempty strict partition sample.
HH=[vector(K,[z(r) for z in p]) for p in H]
VV=vector(K,(2,0));WW=vector(K,(QQ(7)/6,-r/6))
polys=[[HH[0],HH[1],HH[2],HH[3],HH[4],WW],
       [HH[4],HH[5],HH[6],HH[7],VV,WW],
       [HH[8],HH[9],HH[10],HH[11],VV],
       [HH[11],HH[12],HH[0],WW,VV]]
for p in polys:
    for i in range(len(p)):
        e=p[(i+1)%len(p)]-p[i]
        assert all(det(e,p[j]-p[i])>0 for j in range(len(p)) if j not in (i,(i+1)%len(p)))
def separate(p,q):
    return any(all(det(p[(i+1)%len(p)]-p[i],v-p[i])<=0 for v in q) for i in range(len(p)))
for i,p in enumerate(polys):
    for q in polys[i+1:]:assert separate(p,q) or separate(q,p)
def area2(p):return sum(det(p[i],p[(i+1)%len(p)]) for i in range(len(p)))
assert sum(map(area2,polys))==area2(HH)>0
# Cancel all interior seams; split the suppressed flat h8 on h7->V.
boundary=Counter()
for p in polys:
    for i in range(len(p)):
        x,y=p[i],p[(i+1)%len(p)]
        split=[(x,HH[8]),(HH[8],y)] if x==HH[7] and y==VV else [(x,y)]
        for a,c in split:boundary[(tuple(a),tuple(c))]+=1
for (x,y),n in list(boundary.items()):
    m=min(boundary[(x,y)],boundary[(y,x)])
    boundary[(x,y)]-=m;boundary[(y,x)]-=m
assert +boundary==Counter((tuple(HH[i]),tuple(HH[(i+1)%13])) for i in range(13))
print('PASS: exact hat coordinates; convex P2 branch and angles; both W contradictions; strict disjoint partition sample and boundary')
