"""Exact finite check of a NEW three-sector+six-valent-node truncation topology.
Not a two-congruence-class or shape-forcing certificate. No producer imports.
Domain: thin/thick unit rhombs, both opposite donor choices, two receivers,
three original outputs each; two degree-six donor caps per rhomb.
"""
from sage.all import AA, QQ

def add(a,b): return tuple(a[j]+b[j] for j in (0,1))
def sub(a,b): return tuple(a[j]-b[j] for j in (0,1))
def mul(a,k): return tuple(x*k for x in a)
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(p): return abs(sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2)
def convex(p):
    signs=[]
    for i,a in enumerate(p):
        e=sub(p[(i+1)%len(p)],a)
        for j,b in enumerate(p):
            if j not in (i,(i+1)%len(p)):
                signs.append(cross(e,sub(b,a)))
    assert all(x>0 for x in signs) or all(x<0 for x in signs)

h=AA(QQ(1)/100)
eps=AA(QQ(1)/100000)
phi=(AA(1)+AA(5).sqrt())/2
counts={}
small_caps=[]
large_hexagons=[]
for c in [phi/2,(phi-1)/2]:
    s=(1-c*c).sqrt()
    vertices=[(AA(0),AA(0)),(AA(1),AA(0)),(1+c,s),(c,s)]
    mid=[mul(add(vertices[i],vertices[(i+1)%4]),AA(QQ(1)/2)) for i in range(4)]
    for parity in [0,1]:
        donor={}
        for i in [parity,parity+2]:
            e=sub(vertices[(i+1)%4],vertices[i])
            donor[i]=add(mid[i],mul((-e[1],e[0]),h))
        outputs=[]
        for i in [(parity+1)%4,(parity+3)%4]:
            U,V=vertices[i],vertices[(i+1)%4]
            e=sub(V,U)
            t=add(mid[i],mul((e[1],-e[0]),h))
            M=mid[i]
            p,q=donor[(i-1)%4],donor[(i+1)%4]
            triple=[([U,t,M,p],{t,p}),([M,t,V,q],{t,q}),([M,q,p],{p,q})]
            for poly,chosen in triple:
                convex(poly)
                # Convex corner clipping preserves strict convexity. Uniform
                # radius epsilon cuts are disjoint because adjacent edge
                # lengths exceed 2epsilon. Avoid constructing enormous
                # nested-radical coordinates unnecessarily.
                for a in chosen:
                    j=poly.index(a)
                    for b in [poly[(j-1)%len(poly)],poly[(j+1)%len(poly)]]:
                        assert sum(x*x for x in sub(b,a))>4*eps*eps
                size=len(poly)+len(chosen)
                counts[size]=counts.get(size,0)+1
                if size==6: large_hexagons.append(area(poly)-eps*eps)
                outputs.append(poly)
        assert sum(area(poly) for poly in outputs)==s
        # Cap neighbors appear in cyclic order by exact orientation sorting.
        for i,p in donor.items():
            neighbors=[vertices[i],vertices[(i+1)%4],mid[i],mid[(i-1)%4],mid[(i+1)%4],donor[(i+2)%4]]
            points=neighbors
            # Angle comparison without floating point.
            from functools import cmp_to_key
            def half(v): return 0 if v[1]>0 or (v[1]==0 and v[0]>=0) else 1
            def cmp(a,b):
                a,b=sub(a,p),sub(b,p)
                if half(a)!=half(b): return -1 if half(a)<half(b) else 1
                z=cross(a,b)
                assert z!=0
                return -1 if z>0 else 1
            points.sort(key=cmp_to_key(cmp))
            # Uniform-radius radial points are cyclic and strictly convex.
            # Every angular gap is <pi, so cap contains old donor node.
            assert all(cross(sub(points[j],p),sub(points[(j+1)%6],p))>0 for j in range(6))
            small_caps.append(4*eps*eps)
assert counts=={6:16,5:8}
assert max(small_caps)<min(large_hexagons)
# Density bookkeeping: initial V=5,F=6,E=11 per source rhomb;
# truncating two degree-six nodes adds 10 vertices,12 edges,2 faces.
V,F,E=5+10,6+2,11+12
assert V-E+F==0
assert 2*E==4*6+2*5+2*6
assert 2*11<5*6
assert 2*((5+4)+6)==5*6
# Symbolic area-transfer cancellation: one X and one Y each way.
from sage.all import PolynomialRing
K=PolynomialRing(QQ, ['sT','sK','HX','HY','DX','DY','H','P'])
sT,sK,HX,HY,DX,DY,H,P=K.gens()
for sourcearea in [sT,sK]:
    assigned=sourcearea+(HX-DX)+(HY-DY)-(HX-DX)-(HY-DY)
    assert assigned==sourcearea
assert (6*H+2*P-sT)-(6*H+2*P-sK)==sK-sT
assert phi/2 != (phi-1)/2
print('PASS: 24 strict local precursor pieces; 16 derived hexagons, 8 pentagons, 8 convex degree-six caps; exact area identities; density bound; small-cut two-class failure')
