"""Exact changed Cairo pair and finite necessary two-T event comparisons.
No plane tiling enumeration. See corresponding lemma for full finite scope.
"""
from sage.all import QuadraticField
from itertools import combinations_with_replacement, product

K = QuadraticField(3, "w")
w = K.gen()
a,b,c,d,e,f = map(K, (1,2,2*w-1,w-1,3,3-w))
P=(a,b,c,d,e)
Q=(a,c,d,b,f)


def sub(x,y):
    return (x[0]-y[0], x[1]-y[1])


def cross(x,y):
    return x[0]*y[1]-x[1]*y[0]


def verify_polygon(L):
    A,B,C,D,E=L
    assert E == w*C+D-2*A
    assert B-C == w*(D-A)
    assert all(x>0 for x in L) and len(set(L))==5
    v=((K(0),K(0)),(A,K(0)),(A,B),(A-w*C/2,B+C/2),(-E/2,w*E/2))
    for i in range(5):
        edge=sub(v[(i+1)%5],v[i])
        nxt=sub(v[(i+2)%5],v[(i+1)%5])
        assert sum(x*x for x in edge)==L[i]**2
        assert edge[0]*nxt[0]+edge[1]*nxt[1] == (0 if i in(0,2) else K(1)/2)*L[i]*L[(i+1)%5]
        for j in range(5):
            if j not in (i,(i+1)%5):
                assert cross(edge,sub(v[j],v[i]))>0


for L in (P,Q):
    verify_polygon(L)
assert set(P)!=set(Q)
slots=[]
for species,L in enumerate((P,Q)):
    for i,j in ((0,1),(2,3)):
        slots.extend(((species,i,L[i],L[j]),(species,j,L[j],L[i])))
assert len(slots)==8
events=[]
for x,y in combinations_with_replacement(slots,2):
    if x[2]==y[2]:
        events.append((x[2],x[3],y[3]))
assert len(events)==12
sums={r+s for u,r,s in events}
assert sums=={2*a,2*b,2*c,2*d,a+d,b+c}
assert len(sums)==6
assert e not in sums and f not in sums and e!=f
unequal=set()
for (u,r,s),(v,t,z) in product(events,repeat=2):
    if r+s!=t+z:
        continue
    for m in(r,s):
        for M in(t,z):
            if m<M:
                n=r+s-m
                q=t+z-M
                assert m+n==M+q and q<n
                unequal.add((m,M))
assert unequal=={(d,a),(b,c)}
component={a,d}
assert all(not set((L[1],L[2])).issubset(component) for L in(P,Q))
# Only-Q event comparison cannot yield any unequal match or e subdivision.
qslots=[s for s in slots if s[0]==1]
qevents=[(x[2],x[3],y[3]) for x,y in combinations_with_replacement(qslots,2) if x[2]==y[2]]
assert len(qevents)==4
assert len({r+s for u,r,s in qevents})==4
assert all(f!=r+s for u,r,s in qevents)
assert len(set(Q[:4]))==4
print("PASS: exact changed Cairo pair; 12 events; six sums; two necessary unequal arm pairs; e-seam beta obstruction")
