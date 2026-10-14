"""Exact nonsymmetric pentagon / central octagon periodic carrier.
Finite domain: one explicit degree-four metric pair, all possible lattice overlaps.
"""
from sage.all import NumberField,PolynomialRing,QQ,AA,ceil,floor
import json
R=PolynomialRing(QQ,'z');z=R.gen()
K=NumberField(8*z**4-8*z**2+1,'c',embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c)
assert r*r==2 and c*c+t*t==1 and 4*c*t==r and AA(r)>0 and AA(c)>0 and AA(t)>0
x=K(1);y=K(2);v=K(5)/2;u=v+r*c;w=(u+v)/r-t*(x+y);h=K(3)
assert AA(w)>0 and (u-v)/r==c*(y-x)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(s,a):return(s*a[0],s*a[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def edges(p):return list(zip(p,p[1:]+p[:1]))
def area(p):return sum(cross(a,b) for a,b in edges(p))/2
def disjoint(p,q):
    for a,b in edges(p)+edges(q):
        d=sub(b,a);n=(-d[1],d[0]);pp=[dot(a,n) for a in p];qq=[dot(a,n) for a in q]
        if AA(max(pp,key=AA))<=AA(min(qq,key=AA)) or AA(max(qq,key=AA))<=AA(min(pp,key=AA)):return True
    return False
A=(K(0),-w);B=(x*c,-w-x*t);C=add(B,(u/r,u/r));D=add(C,(-v/r,v/r));E=add(D,(-y*c,-y*t));assert E==(0,0)
P=(A,B,C,D,E)
Q=[(K(0),K(0))]
qedges=((-v/r,v/r),(-h,0),(-u/r,-u/r),(0,-w),(v/r,-v/r),(h,0),(u/r,u/r),(0,w))
for e in qedges[:-1]:Q.append(add(Q[-1],e))
Q=tuple(Q);assert add(Q[-1],qedges[-1])==Q[0]
P2=tuple(sub(add(A,B),p) for p in P)
U=((u-v)/r,(u+v)/r+w)
V=(x*c+(u+v)/r+h,-w-x*t-(v-u)/r)
det=cross(V,U)
for poly in (P,Q):
    assert AA(area(poly))>0
    for i,p in enumerate(poly):
        a=sub(p,poly[i-1]);b=sub(poly[(i+1)%len(poly)],p)
        assert AA(cross(a,b))>0
        if poly==P:
            if i==2:assert dot(a,b)==0
            else:assert AA(dot(a,b))>0 and dot(a,b)**2==dot(a,a)*dot(b,b)*t*t
        else:assert AA(dot(a,b))>0 and 2*dot(a,b)**2==dot(a,a)*dot(b,b)
reps=(Q,P,P2)
assert area(Q)+2*area(P)==det and AA(det)>0
# Strong necessary-reduction checks: two private opposite slots and no possible T host.
assert h not in (x,u,v,y,w)
assert all(s not in (2*u,2*v) for s in (x,w,y))
coords=[[(cross(p,U)/det,cross(V,p)/det) for p in poly] for poly in reps]
checks=0
for i,p in enumerate(reps):
    for j,q in enumerate(reps):
        lo=[int(ceil(AA(min((z[k] for z in coords[i]),key=AA)-max((z[k] for z in coords[j]),key=AA)))) for k in (0,1)]
        hi=[int(floor(AA(max((z[k] for z in coords[i]),key=AA)-min((z[k] for z in coords[j]),key=AA)))) for k in (0,1)]
        for m in range(lo[0],hi[0]+1):
            for n in range(lo[1],hi[1]+1):
                if i==j and m==n==0:continue
                shift=add(mul(m,V),mul(n,U))
                assert disjoint(p,tuple(add(a,shift) for a in q)),(i,j,m,n)
                checks+=1
print(json.dumps({'status':'PASS','field':'c is root 8c^4-8c^2+1, 9/10<c<1','lengths':{name:str(value) for name,value in [('x',x),('y',y),('u',u),('v',v),('w',w),('h',h)]},'potential_overlap_checks':checks,'P_has_five_distinct_side_lengths':len({x,u,v,y,w})==5,'Q_private_slots':[1,5],'no_possible_flat_host':True,'covolume':str(det),'lattice':[[str(a) for a in V],[str(a) for a in U]]}))
