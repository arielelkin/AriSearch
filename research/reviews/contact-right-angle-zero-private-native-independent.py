"""Independent finite native-word review; exact scope3^8 words, no metrics."""
from sage.all import QuadraticField, AA, matrix
from itertools import product
K=QuadraticField(2,"r",embedding=AA(2).sqrt());r=K.gen()
directions=[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]
def valid_masks(W):
 out=[]
 for start in range(8):
  V=W[start:]+W[:start]
  # One x/y bevel must be consistently exposed at every PPQ transition.
  if V[1] in[0,1] and V[1]==V[2] and V[4] in[0,1] and V[4]==V[7] and V[5]==V[6]==2:
   out.append(tuple(sorted((start,(start+3)%8))))
  if V[1] in[0,1] and V[3]==1-V[1] and V[5] in[0,1] and V[7]==1-V[5] and V[2]==V[6]==2:
   out.append(tuple(sorted((start,(start+4)%8))))
 return set(out)
residual=set()
for W in product(range(3),repeat=8):
 if sorted(W.count(i) for i in range(3))!=[2,3,3]:continue
 masks=valid_masks(W)
 if not masks:continue
 M=matrix(K,[[sum(directions[j][axis] for j in range(8) if W[j]==label) for label in range(3)] for axis in range(2)])
 if M.rank()==2:
  z=M.right_kernel().basis()[0]
  positive=all(AA(x)>0 for x in z) or all(AA(x)<0 for x in z)
  assert not positive or len(set(z))<3
  continue
 assert M.rank()==1
 row=next(x for x in M.rows() if x)
 nonzero=[i for i,z in enumerate(row) if z]
 if len(nonzero)<3:
  assert len(nonzero)==2 and row[nonzero[0]]==-row[nonzero[1]]
  continue
 assert len(masks)==1
 i,j=next(iter(masks));assert(j-i)%8==4 and W[i]!=W[j]
 for q in[i,j]:assert W[(q-1)%8]==W[(q+1)%8] in[0,1]
 residual.add(W)
assert len(residual)==32
print("PASS: all6561 native words examined,32 rotated321 residual words, every residual has one opposite QQmask and same acute tag at each seam's endpoints")
# Twelve422 clean source words; check H/H eligible masks, not numerical rays.
count=0
for H in range(3):
 for a in[0,1]:
  b=1-a
  for W,expected in[((H,a,a,H,b,2,2,b),{(0,3)}),((H,a,2,b,H,a,2,b),{(0,4),(2,6)} if H==2 else{(0,4)})]:
   masks={q for q in valid_masks(W) if W[q[0]]==W[q[1]]==H}
   assert masks==expected
   if len(expected)==1:
    sigma=(lambda i:(3-i)%8) if next(iter(expected))==(0,3) else(lambda i:(i+4)%8)
   else:sigma=lambda i:(2-i)%8
   assert all(W[i]==W[sigma(i)] for i in range(8))
   count+=1
assert count==12
print("PASS: all12 clean422 words, eligible H/H masks and actual dihedral side-word symmetries")
