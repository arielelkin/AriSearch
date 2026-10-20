import sympy as s,json
from pathlib import Path
z=s.Symbol('z');phi=s.cyclotomic_poly(30,z)
def red(a):
 n,d=s.fraction(s.cancel(a));return s.rem(n*s.invert(d,phi,z),phi,z).expand()
def zz(n):return red(z**(n%30))
H=1+zz(3)+zz(-3)
k=red(H*(zz(3)-zz(-3))/(zz(5)-zz(-5)))
ell=red(H*(zz(2)-zz(-2))/(zz(5)-zz(-5)))
print('phi',phi,'k',k)
r=json.loads(Path('research/searches/resonance-minimal-carrier-sol-2026-10-19.json').read_text())[0]['survivors'][0]
angles=[[9]*5,[9]*5,[12,12,10,10,10,10,11]]*1
angles.append(angles[-1]);off=[0,5,10,17];V=[];edges=[]
for f,row in enumerate(angles):
 d=r['rotations'][str(f)];v=[s.Integer(0)];ee=[]
 for i in range(len(row)):
  if i:d=(d+15-row[i])%30
  length=(k if i==3 else ell) if f>=2 and i in (3,4) else 1
  ee.append(red(length*zz(d)));v.append(red(v[-1]+ee[-1]))
 assert v[-1]==0
 V.append(v[:-1]);edges.append(ee)
face=lambda a:0 if a<5 else 1 if a<10 else 2 if a<17 else 3
T={0:s.Integer(0)};pending=r['pairs'][:]
while len(T)<4:
 for a,b in pending:
  f,g=face(a),face(b);i,j=a-off[f],b-off[g]
  delta=red(V[f][i]-V[g][j]-edges[g][j])
  if f in T and g not in T:T[g]=red(T[f]+delta)
  if g in T and f not in T:T[f]=red(T[g]-delta)
sh=[]
for a,b in pending:
 f,g=face(a),face(b);i,j=a-off[f],b-off[g]
 assert red(edges[f][i]+edges[g][j])==0
 sh.append(red(T[f]+V[f][i]-T[g]-V[g][j]-edges[g][j]))
non=[x for x in sh if x!=0];u=non[0]
num=lambda x:complex(s.N(x.subs(z,s.exp(s.I*s.pi/15))))
v=next(x for x in non if abs((num(x)/num(u)).imag)>1e-5)
coef=lambda a:s.Matrix([red(a).coeff(z,i) for i in range(8)])
M=s.Matrix.hstack(coef(u),coef(v))
print('T',T,'basis',u,v)
print('shifts',[list(M.gauss_jordan_solve(coef(x))[0]) for x in sh])
Path('research/searches/resonance-minimal-carrier-sol-2026-10-19-metric.json').write_text(json.dumps(dict(phi=str(phi),k=str(k),ell=str(ell),translations={str(f):str(a) for f,a in T.items()},basis=[str(u),str(v)],shifts=[list(map(int,M.gauss_jordan_solve(coef(x))[0])) for x in sh]),indent=2)+'\n')

conj=lambda a:red(a.subs(z,zz(-1)))
cross=lambda a,b:red(conj(a)*b-a*conj(b))
area=red(sum(cross(V[f][i],edges[f][i]) for f in range(4) for i in range(len(V[f]))))
det=cross(u,v)
assert red(area-2*det)==0
assert det!=0
print('area equals lattice determinant:',red(area-2*det)==0,'area equals negative determinant:',red(area+2*det)==0)
