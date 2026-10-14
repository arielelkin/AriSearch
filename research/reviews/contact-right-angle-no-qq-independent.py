"""Independent symbolic verifier of the noQQ four-P grouped-Q carrier.
No author imports; coefficient field QQbar from zeta16 rather than NumberField.
Domain: three indeterminates x,y,v;28 edges,14 retained pairs,56 endpoint equations.
Run with sage through mise/conda.
"""
from sage.all import QQbar, AA, PolynomialRing
zeta=QQbar.zeta(16)
c=(zeta+zeta.conjugate())/2
t=(zeta-zeta.conjugate())/(2*QQbar.gen())
r=QQbar(2).sqrt()
assert 8*c**4-8*c**2+1==0 and AA(c)>AA(9)/10 and AA(c)<1
assert r==4*c**2-2 and t==r/(4*c)
S=PolynomialRing(QQbar,('x','y','v'));x,y,v=S.gens()
u=v+r*c*(y-x);w=(u+v)/r-t*(x+y)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def scale(k,a):return(k*a[0],k*a[1])
def neg(a):return scale(-1,a)
def swap(a):return(a[1],a[0])
def ns(a):return(-a[1],-a[0])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def edges(P):return list(zip(P,P[1:]+P[:1]))
def area(P):return sum(cross(a,b) for a,b in edges(P))/2
# Construct P by integrating its native vectors from a different origin.
raw=[(S(0),S(0))]
for ell,d in zip((x,u,v,y,w),((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):
 raw.append(add(raw[-1],scale(ell,d)))
assert raw[-1]==raw[0];raw.pop()
centre=raw[2];P=tuple(sub(p,centre) for p in raw)
a=centre[0];cy=centre[1];zz=w/2-cy
assert zz==(x-y)*(c+t)/2
assert w==2*a-(c+t)*(x+y)
V=(2*a,2*cy-w);U=(2*cy-w,2*a)
reps=[P,tuple(swap(p) for p in P[::-1]),tuple(neg(p) for p in P),tuple(ns(p) for p in P[::-1])]
# Construct Q by its native vectors, independent of the author's vertex formula.
Q=[P[3]];direction=(t,c)
for ell in(y,x,x,y,y,x,x,y):
 Q.append(add(Q[-1],scale(ell,direction)))
 direction=((direction[0]-direction[1])/r,(direction[0]+direction[1])/r)
assert Q[-1]==Q[0];Q.pop();Q=tuple(Q)
assert all(add(Q[i],Q[i+4])==sub(U,V) for i in range(4))
reps.append(Q)
pairs=[((0,0),(4,2),(0,-1)),((0,1),(1,2),(0,0)),((0,2),(3,1),(0,0)),((0,3),(4,7),(0,0)),((0,4),(2,4),(-1,0)),((1,0),(4,4),(1,-1)),((1,1),(2,2),(0,0)),((1,3),(4,1),(0,-1)),((1,4),(3,4),(0,-1)),((2,0),(4,6),(1,0)),((2,1),(3,2),(0,0)),((2,3),(4,3),(1,-1)),((3,0),(4,0),(0,0)),((3,3),(4,5),(1,0))]
seen=set()
for f,g,(m,n) in pairs:
 assert f not in seen and g not in seen;seen.update((f,g))
 A,B=edges(reps[f[0]])[f[1]];C,D=edges(reps[g[0]])[g[1]]
 shift=add(scale(m,V),scale(n,U))
 assert A==add(D,shift) and B==add(C,shift)
assert seen=={(i,j) for i,P0 in enumerate(reps) for j in range(len(P0))}
assert len(seen)==28
assert all(area(rep)==area(P) for rep in reps[:4])
assert 4*area(P)+area(Q)==cross(V,U)==4*(a*a-zz*zz)
print('PASS: independent zeta16 symbolic reconstruction;28 native edges;14 pairs;56 coordinate endpoints; area identity')
