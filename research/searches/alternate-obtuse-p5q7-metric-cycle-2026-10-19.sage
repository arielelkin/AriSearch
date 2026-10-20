# Exact cyclotomic tangential realization and cross-edge gate.
import json
from pathlib import Path
K=CyclotomicField(144);z=K.gen();I=z**36
P=[95,105,110,115,115];Q=[125,125,125,125,130,130,140]
def cot_half(a):
 w=z**(a//5*2) # exp(i*a degrees), because z has 2.5 degree argument
 return I*(w+1)/(w-1)
def realization(A):
 # unit-incircle support lines, outward normals turn by 180-A[next].
 N=[K(1)]
 for a in A[1:]:N.append(N[-1]*z**((180-a)*2//5))
 V=[]
 for i in range(len(A)):
  u=N[i-1];v=N[i]
  # consecutive supports Re(conj(n)*point)=1
  vertex=2*u*v/(u+v)
  assert (vertex/u+(vertex/u).conjugate())/2==1
  assert (vertex/v+(vertex/v).conjugate())/2==1
  V.append(vertex)
 lengths=[cot_half(A[i])+cot_half(A[(i+1)%len(A)]) for i in range(len(A))]
 for i,l in enumerate(lengths):
  d=V[(i+1)%len(A)]-V[i]
  assert d*d.conjugate()==l*l
  assert AA(l)>0
 for v in V:
  for n in N:assert AA((v/n+(v/n).conjugate())/2)<=1
 return V,lengths
VP,LP=realization(P);VQ,LQ=realization(Q)
matching=[(i,j) for i,a in enumerate(LP) for j,b in enumerate(LQ) if a==b]
assert matching==[]
out=dict(P=P,Q=Q,field='CyclotomicField(144); z=exp(2*pi*i/144)',vertices_P=[str(v) for v in VP],vertices_Q=[str(v) for v in VQ],side_lengths_P=[str(v) for v in LP],side_lengths_Q=[str(v) for v in LQ],cross_equalities=matching,strict_convexity=True,status='Exact convex pair; killed by no cross-type equal edge length. No plane tiling.')
Path('research/searches/alternate-obtuse-p5q7-metric-cycle-2026-10-19.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('Exact convex realization: PASS; cross-edge equalities:',matching,'; tiling candidate: KILLED')
