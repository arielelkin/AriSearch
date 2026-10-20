"""Exact local parent-placement ambiguity, not an extension certificate."""
import runpy
from pathlib import Path
import sympy as s
f=runpy.run_path(str(Path(__file__).with_name('sugimoto-method3-two-class-first-gate-2026-10-19.py')))
X,V,words=f['X'],f['V'],f['words']
simp,sub,cross=f['simp'],f['sub'],f['cross']
dirs=[60,120,210,270,180,240,330,270,0,300,30,90,90,150]
children=[[V[n] for n in w] for w in words.values()]
def rotate(p,d):
 c=s.cos(s.pi*d/180); z=s.sin(s.pi*d/180)
 return (simp(c*p[0]-z*p[1]),simp(z*p[0]+c*p[1]))
def separated(p,q):
 # A CCW convex polygon lies in the closed left halfplanes of its edges.
 # One edge with the other polygon entirely on the right separates interiors.
 for a in (p,q):
  b=q if a is p else p
  for u,v in zip(a,a[1:]+a[:1]):
   if all(cross(sub(v,u),sub(w,u))<=0 for w in b):return True
 return False
count=0
for i,js in [(8,[2,4,6,12,14]),(10,[2,4,6,12,14]),(1,[3,7,9,11]),(5,[3,7,9,11])]:
 for j in js:
  d=(dirs[(i-2)%14]+180-dirs[j-1])%360
  z=sub(X[i],rotate(X[j],d))
  def move(p):
   r=rotate(p,d)
   return tuple(simp(a+b) for a,b in zip(r,z))
  assert move(X[j])==X[i]
  # The two rays of the inserted corner coincide with the missing sector.
  assert (dirs[(j-2)%14]+180+d-dirs[i-1])%360==0
  moved=[[move(p) for p in q] for q in children]
  assert all(separated(p,q) for p in children for q in moved),(i,j,d)
  print(f'X{i} <- X{j}: rotation {d}; translation {z}')
  count+=1
assert count==18
print('PASS: 18 distinct orientation-preserving locally nonoverlapping parent placements; no global extension asserted')
