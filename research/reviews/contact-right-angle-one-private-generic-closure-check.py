"""Independent exact affine-line verifier for the 60 one-private dimer cones.
Does not import producer or enumerate active-zero subsets.
"""
from sage.all import QQ,AA,PolynomialRing,NumberField,matrix,vector
from itertools import permutations,combinations
from pathlib import Path
import json
Z=PolynomialRing(QQ,'z');z=Z.gen();K=NumberField(8*z**4-8*z**2+1,'c',embedding=((2+AA(2).sqrt())/4).sqrt());c=K.gen();r=4*c*c-2;t=r/(4*c)
TAGS=('x','y','u','v','w','H');INDEX={s:i for i,s in enumerate(TAGS)}
expected={(H,a)+m+(b,) for H in('H',) for a,b in(('u','v'),('v','u')) for m in set(permutations(('x','x','y','y','w')))}
cert=json.loads(Path('research/certificates/contact-structure-one-private-dimer-words.json').read_text())
assert len(expected)==60 and len(cert['records'])==60 and {tuple(rec['word']) for rec in cert['records']}==expected
D=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
F=[]
for i,j in combinations(range(6),2):
 row=[K(0)]*6;row[i]=1;row[j]=-1;F.append((TAGS[i]+'='+TAGS[j],vector(K,row)))
for s in('x','y','w'):
 for a in('u','v'):
  row=[K(0)]*6;row[INDEX[s]]=1;row[INDEX[a]]=-2;F.append((s+'=2'+a,vector(K,row)))
positive=0;negative=0
for rec in cert['records']:
 word=rec['word'];rows=[[c,-c,1/r,-1/r,0,0],[-t,-t,1/r,1/r,-1,0]]
 for axis in(0,1):
  row=[K(0)]*6
  for i,tag in enumerate(word):row[INDEX[tag]]+=D[i][axis]
  rows.append(row)
 A=matrix(K,rows);M=A.stack(matrix(K,1,6,[1]*6));rhs=vector(K,[0,0,0,0,1])
 assert A.rank()==rec['closure_rank']==4 and M.rank()==5 and rec['normalized_dimension']==1
 # Solve affine line and intersect all coordinate halfspaces, independently of active-zero vertex search.
 base=M.solve_right(rhs);direction=M.right_kernel().basis()[0]
 lowers=[];uppers=[]
 for b,d in zip(base,direction):
  if AA(d)>0:lowers.append(-b/d)
  elif AA(d)<0:uppers.append(-b/d)
  else:assert AA(b)>=0
 assert lowers and uppers
 low=max(lowers,key=AA);high=min(uppers,key=AA);assert AA(low)<=AA(high)
 ends=[base+low*direction,base+high*direction]
 actual={tuple(point) for point in ends};saved=[vector(K,[K(s) for s in row]) for row in rec['vertices']]
 assert actual=={tuple(point) for point in saved}
 assert all(A*point==vector(K,[0]*4) and sum(point)==1 and all(AA(z)>=0 for z in point) for point in saved)
 zeros=[TAGS[i] for i in range(6) if all(point[i]==0 for point in ends)]
 equal=[name for name,row in F if all(row.dot_product(point)==0 for point in ends)]
 assert rec['forced_zero_coordinates']==zeros and rec['forced_forbidden_equalities']==equal
 if zeros or equal:
  assert rec['status']=='NO_POSITIVE_DISTINCT_NONDOUBLED_CLOSURE' and 'witness' not in rec
  negative+=1
 else:
  assert rec['status']=='POSITIVE_GENERIC_CLOSURE'
  p=vector(K,[K(rec['witness'][tag]) for tag in TAGS])
  assert A*p==vector(K,[0]*4) and sum(p)==1 and all(AA(z)>0 for z in p)
  assert all(row.dot_product(p)!=0 for _,row in F)
  beta=rec['weight_beta'];weights=[K(beta)**j for j in range(len(saved))]
  assert p==sum((s*v for s,v in zip(weights,saved)),vector(K,[0]*6))/sum(weights)
  positive+=1
assert positive==cert['positive_generic_words']==48 and negative==12 and cert['words_tested']==60
print(json.dumps({'status':'PASS','words':60,'positive_generic_closures':positive,'rejected_generic_closures':negative,'method':'independent affine-line interval intersection','plane_tiling_claim':False}))
