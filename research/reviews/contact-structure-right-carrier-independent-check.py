"""Exact independent Q(sqrt(2)) carrier lattice verifier; no author imports.
Run via the research environment Python (SageMath is importable).
"""
from sage.all import QuadraticField,AA,ceil,floor
import json
K=QuadraticField(2,'r',embedding=AA(2).sqrt()); r=K.gen();a=1+r;W=2*a+1
Q=tuple((K(x),K(y)) for x,y in ((a,1),(1,a),(-1,a),(-a,1),(-a,-1),(-1,-a),(1,-a),(a,-1)))
P=tuple((K(x),K(y)) for x,y in ((0,-1),(1,-r),(a,0),(1,r),(0,1)))
def add(v,w):return(v[0]+w[0],v[1]+w[1])
def sub(v,w):return(v[0]-w[0],v[1]-w[1])
def mul(t,v):return(t*v[0],t*v[1])
def cross(v,w):return v[0]*w[1]-v[1]*w[0]
def dot(v,w):return v[0]*w[0]+v[1]*w[1]
def edges(p):return list(zip(p,p[1:]+p[:1]))
def area(p):return abs(sum(cross(u,v) for u,v in edges(p))/2)
def exact_disjoint(p,q):
    for u,v in edges(p)+edges(q):
        e=sub(v,u);n=(-e[1],e[0]);pp=[dot(z,n) for z in p];qq=[dot(z,n) for z in q]
        if AA(max(pp,key=AA))<=AA(min(qq,key=AA)) or AA(max(qq,key=AA))<=AA(min(pp,key=AA)):return True
    return False

assert area(Q)==8+8*r and area(P)==3+r
for poly in (Q,P):
    for i,z in enumerate(poly):
        e=sub(z,poly[i-1]);f=sub(poly[(i+1)%len(poly)],z)
        assert AA(cross(e,f))>0
        d=dot(e,f);n=dot(e,e)*dot(f,f)
        if poly==Q: assert AA(d)>0 and d*d==n/2 and dot(e,e)==4
        elif i==2: assert d==0
        else: assert AA(d)>0 and d*d==n*(2-r)/4
v=(W,a);w=(K(0),2*a);det=cross(v,w)
reps=(Q,tuple(add(z,(a,K(0))) for z in P),tuple(add((-z[0],z[1]),(a+1,a)) for z in P[::-1]))
assert sum(area(p) for p in reps)==det==14+10*r
coords=[[(cross(z,w)/det,cross(v,z)/det) for z in p] for p in reps]
checks=0
for i,p in enumerate(reps):
    for j,q in enumerate(reps):
        lo=[int(ceil(AA(min((z[k] for z in coords[i]),key=AA)-max((z[k] for z in coords[j]),key=AA)))) for k in (0,1)]
        hi=[int(floor(AA(max((z[k] for z in coords[i]),key=AA)-min((z[k] for z in coords[j]),key=AA)))) for k in (0,1)]
        for m in range(lo[0],hi[0]+1):
            for n in range(lo[1],hi[1]+1):
                if i==j and m==n==0:continue
                shift=add(mul(m,v),mul(n,w));translated=tuple(add(z,shift) for z in q)
                assert exact_disjoint(p,translated),(i,j,m,n)
                checks+=1
print(json.dumps({'status':'PASS','exact_field':'Q(sqrt(2)), positive embedding','fundamental_areas':[str(area(p)) for p in reps],'determinant':str(det),'potential_overlap_checks':checks}))
