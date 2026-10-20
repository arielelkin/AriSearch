from sage.all import *
# Independent real-coordinate polynomial checker. No producer imports/JSON inputs.
z=QQbar.zeta(20)
A=PolynomialRing(AA,'x'); x=A.gen()
def v(c): return vector(A,[AA(c.real()),AA(c.imag())])
u=[v(z**j) for j in range(20)]
t=AA((z+z**-1).real()); k=AA((-(z**3+z**15)/z**9).real())
assert t>0 and 0<k<1
zero=vector(A,[0,0])
def polygon(edges):
 out=[]; cur=zero
 for e in edges: out.append(cur); cur=cur+e
 assert cur==zero
 return out
P=polygon([u[4*j] for j in range(5)])
Q=polygon([u[0],x*u[3],u[6],((1-k)*t+k*x)*u[9],u[12],x*u[15],u[18]])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def positive(p):
 assert p and all(c>=0 for c in p.list()) and any(c>0 for c in p.list())
for C in [P,Q]:
 for i in range(len(C)):
  for j in range(len(C)):
   if j not in [i,(i+1)%len(C)]:positive(cross(C[(i+1)%len(C)]-C[i],C[j]-C[i]))
def mul(c,p):
 a,b=v(c);return vector(A,[a*p[0]-b*p[1],b*p[0]+a*p[1]])
def reflection(C,c):
 return {tuple(mul(c,vector(A,[p[0],-p[1]]))) for p in C}=={tuple(p) for p in C}
assert reflection(P,z**6) and reflection(Q,z**8)
one=u[0]
F=[P,[one-p for p in P],[one-mul(z**6,q) for q in Q],[mul(z**6,q) for q in Q]]
L=u[1]*(x-t)+2*u[4]+u[2]+2*one
M=(u[7]-u[5]+u[3]-u[1])*(x-t)+3*u[6]-u[4]+u[2]-3*one
D=cross(L,M); positive(D)
s=AA(((z**3-z**7)/2).real())
assert D==s*x*x+(4+k)*x+2*t+4*s
area2=sum((sum((cross(C[i],C[(i+1)%len(C)]) for i in range(len(C))),A(0)) for C in F),A(0))
assert area2==2*D
pairs=[(0,5),(1,16),(6,23),(4,17),(9,10),(2,21),(3,12),(7,14),(8,19),(11,18),(13,20),(15,22)]
shifts=[(0,0)]*5+[(1,0),(0,1),(-1,0),(0,-1),(0,-1),(1,-1),(1,0)]
darts=[(f,i) for f,C in enumerate(F) for i in range(len(C))]
assert sorted(sum(([a,b] for a,b in pairs),[]))==list(range(24))
mate={};delta={}
for (a,b),(m,n) in zip(pairs,shifts):
 f,i=darts[a];g,j=darts[b];C=F[f];E=F[g]
 assert C[i]-E[(j+1)%len(E)]==m*L+n*M
 assert C[(i+1)%len(C)]-E[j]==m*L+n*M
 mate[a]=b;mate[b]=a;delta[a]=m*L+n*M;delta[b]=-delta[a]
nextdart={d:darts.index((f,(i+1)%len(F[f]))) for d,(f,i) in enumerate(darts)}
left=set(range(24));cycles=[]
while left:
 start=min(left);cycle=[];d=start
 while d not in cycle:
  cycle.append(d);left.remove(d);d=nextdart[mate[d]]
 assert d==start
 assert len(cycle)==3
 assert sum((delta[d] for d in cycle),zero)==zero
 angles=[108 if darts[d][0]<2 else 144 if darts[d][1]==0 else 126 for d in cycle]
 assert sum(angles)==360
 cycles.append(cycle)
assert len(cycles)==8
# Dual adjacency connected, independent of the proposed spanning tree.
seen={0}
while True:
 new=seen|{darts[b][0] for a,b in mate.items() if darts[a][0] in seen}
 if new==seen:break
 seen=new
assert seen==set(range(4))
print('PASS independent AA[x] geometry, 50 convexity tests, 12 full endpoint identifications, 8 stars, positive determinant and area identity; map1 follows by face exchange.')
