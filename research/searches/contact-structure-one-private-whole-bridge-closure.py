"""Two exact structurally forced whole-R/S bridge closure systems."""
from sage.all import QQ,AA,PolynomialRing,NumberField,matrix,vector
from sage.env import SAGE_VERSION
import sys,json
R=PolynomialRing(QQ,"z");z=R.gen();K=NumberField(8*z**4-8*z**2+1,"c",embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c)
names=("x","y","u","v","w","H")
dirs=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
words=(("H","u","x","x","y","y","x","v"),("H","u","y","y","x","x","x","v"))
expected=vector(K,[1,1,-4*c**3+2*c**2+4*c-1,-4*c**3+2*c**2+4*c-1,1,-8*c**3+4*c**2+6*c-2])
assert all(AA(z)>0 for z in expected)
records=[]
for word in words:
 rows=[[c,-c,1/r,-1/r,0,0],[-t,-t,1/r,1/r,-1,0],[-1,0,0,0,1,0]]
 for coordinate in(0,1):
  row=[K(0)]*6
  for i,name in enumerate(word):row[names.index(name)]+=dirs[i][coordinate]
  rows.append(row)
 A=matrix(K,rows);assert A.rank()==5 and A*expected==vector(K,[0]*5)
 assert len(A.right_kernel().basis())==1
 basis=A.right_kernel().basis()[0];assert basis/basis[0]==expected
 records.append({"word":list(word),"rows":[[str(z) for z in row] for row in A.rows()],"rank":5,"normalized_positive_kernel":dict(zip(names,[str(z) for z in expected])),"forced_equalities":["x=y=w","u=v"],"status":"EXCLUDED_FROM_NONSYMMETRIC_OTHER_LENGTHS_DISTINCT_DOMAIN"})
print(json.dumps({"field_polynomial_coefficients":[1,0,-8,0,8],"field_isolating_interval":["9/10","1"],"software":{"sage":SAGE_VERSION,"python":sys.version.split()[0]},"scope":"exactly two rooted necessary dimer words on w=x; reflection dual w=y; not all one-private or all bridge-alias metrics","records":records},indent=2))
