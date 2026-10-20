from sage.all import *
# Independent witness check: do not import the search or its certificate.
w=QQbar.zeta(20)
t=w+w.conjugate()
P=[sum((w**(4*j) for j in range(i)),QQbar(0)) for i in range(5)]
Q=[sum(((t if j%2 else 1)*w**(3*j) for j in range(i)),QQbar(0)) for i in range(7)]
assert sum(((t if j%2 else 1)*w**(3*j) for j in range(7)),QQbar(0))==0
assert set(w**8*z.conjugate() for z in Q)==set(Q)
faces=[P,[1-z for z in P],[1-w**6*z for z in Q],[w**6*z for z in Q]]
v=lambda z:vector(AA,[z.real(),z.imag()])
faces=[[v(z) for z in f] for f in faces]
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
L=[v(2*w**4+w**2+2),v(3*w**6-w**4+w**2-3)]
M=matrix(AA,2,2,lambda i,j:L[j][i]); det=M.det()
assert det!=0
poly=[]
areas=[]
for f in faces:
 n=len(f)
 # Strong convexity certificate: every other vertex strictly left of each edge.
 assert all(cross(f[(i+1)%n]-f[i],f[j]-f[i])>0 for i in range(n) for j in range(n) if j not in (i,(i+1)%n))
 poly.append(Polyhedron(vertices=f,base_ring=AA))
 areas.append(sum(cross(f[i],f[(i+1)%n]) for i in range(n))/2)
assert abs(det)==sum(areas)
inv=M.inverse()
coords=[[inv*z for z in f] for f in faces]
bounds=[[(min(z[k] for z in f),max(z[k] for z in f)) for k in range(2)] for f in coords]
checked=0
for i in range(4):
 for j in range(4):
  ranges=[range(ceil(bounds[i][k][0]-bounds[j][k][1]),floor(bounds[i][k][1]-bounds[j][k][0])+1) for k in range(2)]
  for a in ranges[0]:
   for b in ranges[1]:
    if i==j and a==b==0:continue
    shifted=Polyhedron(vertices=[z+a*L[0]+b*L[1] for z in faces[j]],base_ring=AA)
    assert poly[i].intersection(shifted).dim()<2,(i,j,a,b)
    checked+=1
# Recover all edge partners directly; require exactly one mate for each dart.
darts=[(i,k) for i,f in enumerate(faces) for k in range(len(f))]
partners={}
for i,k in darts:
 A=faces[i][k]; B=faces[i][(k+1)%len(faces[i])]
 found=[]
 for j,l in darts:
  C=faces[j][l]; D=faces[j][(l+1)%len(faces[j])]
  if B-A != C-D:continue
  shift=inv*(A-D)
  if all(x in ZZ for x in shift):found.append(((j,l),tuple(ZZ(x) for x in shift)))
 assert len(found)==1,((i,k),found)
 partners[(i,k)]=found[0]
for d,(e,s) in partners.items():
 assert partners[e]==(d,tuple(-x for x in s))
assert len(partners)==24
print('VALID independent QQbar/AA Polyhedron witness; translate pairs',checked)
print('signed determinant',det,'area sum',sum(areas))
print('edge pairs',[(d,e,s) for d,(e,s) in partners.items() if d<e])
