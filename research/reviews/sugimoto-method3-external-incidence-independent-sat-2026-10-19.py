import runpy
import sympy as s
f=runpy.run_path("research/searches/sugimoto-method3-two-class-first-gate-2026-10-19.py")
X=f["X"]; V=f["V"]; words=f["words"]
E=s.expand
sub=lambda a,b:(E(a[0]-b[0]),E(a[1]-b[1]))
dot=lambda a,b:E(a[0]*b[0]+a[1]*b[1])
cross=lambda a,b:E(a[0]*b[1]-a[1]*b[0])
polys=[[V[x] for x in w] for w in words.values()]
def sat(p,q):
 for poly in (p,q):
  for a,b in zip(poly,poly[1:]+poly[:1]):
   e=sub(b,a); n=(-e[1],e[0])
   pp=[dot(x,n) for x in p]; qq=[dot(x,n) for x in q]
   if max(pp)<=min(qq) or max(qq)<=min(pp): return True
 return False
assert all(sat(p,q) for k,p in enumerate(polys) for q in polys[k+1:])
dirs=[60,120,210,270,180,240,330,270,0,300,30,90,90,150]
angles=[(180-(dirs[k]-dirs[k-1]))%360 for k in range(14)]
assert angles==[270,120,90,120,270,120,90,240,90,240,90,120,180,120]
for i in range(1,15):
 assert sub(X[i+1],X[i])==(s.cos(s.pi*dirs[i-1]/180),s.sin(s.pi*dirs[i-1]/180))
print("INDEPENDENT: directions, angles, convex-child interior disjointness verified")
count=0
for i,js in [(8,[2,4,6,12,14]),(10,[2,4,6,12,14]),(1,[3,7,9,11]),(5,[3,7,9,11])]:
 seen=[]
 for j in js:
  d=(dirs[i-2]+180-dirs[j-1])%360
  c=s.cos(s.pi*d/180); z=s.sin(s.pi*d/180)
  rot=lambda p:(E(c*p[0]-z*p[1]),E(z*p[0]+c*p[1]))
  t=sub(X[i],rot(X[j])); move=lambda p:tuple(E(a+b) for a,b in zip(rot(p),t))
  assert move(X[j])==X[i]
  assert sub(move(X[j%14+1]),X[i])==sub(X[i-1 if i>1 else 14],X[i])
  assert sub(move(X[j-1 if j>1 else 14]),X[i])==sub(X[i+1],X[i])
  signature=tuple(move(X[k]) for k in range(1,15))
  assert signature not in seen;seen.append(signature)
  moved=[[move(p) for p in q] for q in polys]
  assert all(sat(p,q) for p in polys for q in moved),(i,j)
  assert E(c*c+z*z)==1
  count+=1
  print("INDEPENDENT PASS",i,j,d)
assert count==18
print("INDEPENDENT PASS: all 18, 450 convex-pair SAT checks")
