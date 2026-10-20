#!/usr/bin/env python3
"""One analytic private-edge hierarchy design gate. No patch/quotient search."""
from itertools import product
import json
U=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def closes(w):return all(sum(w[k]*U[k][j] for k in range(6))==0 for j in [0,1])
def states(w):
 for r,e in product(range(6),[-1,1]):yield r,e,tuple(w[(r+e*k)%6] for k in range(6))
def corners(w):return {tuple(sorted((w[k-1],w[k]))) for k in range(6)}
A=(5,3,3,4,4,2);B=(1,3,3,2,2,4)
assert not closes((5,2,3,4,4,3)) # discarded preliminary invalid word
assert closes(A) and closes(B)
assert [A[0]-A[3],A[2]-A[5],A[4]-A[1]]==[1,1,1]
assert [B[0]-B[3],B[2]-B[5],B[4]-B[1]]==[-1,-1,-1]
assert not any(w==B for r,e,w in states(A))
assert len(set(w for r,e,w in states(A)))==12
assert len(set(w for r,e,w in states(B)))==12
for w in [A,B]:assert all(closes(z) and min(z)>0 for r,e,z in states(w))
CA,CB=corners(A),corners(B)
for w,C in [(A,CA),(B,CB)]:
 left,right=w[-1],w[1]
 halfturn=[tuple(sorted((left,right)))]*2
 reflection=[(left,left),(right,right)]
 # Both physical private-edge mating options have legal endpoint corners
 # in the mixed pair, but each lacks at least one in its own species.
 for ends in [halfturn,reflection]:
  assert all(t in CA|CB for t in ends)
  assert any(t not in C for t in ends)
# Existing four-parameter periodic cone membership. Write each length m+k*d
# as coefficient k: every formula p+a-c etc has coefficient 1 on m.
# Thus membership equality checks on k hold identically for all m,d.
AA=(2,0,0,1,1,-1);BB=(-2,0,0,-1,-1,1)
checks=0;matches=[]
for swap,(X,Y) in enumerate([(AA,BB),(BB,AA)]):
 for rx,ex,x in states(X):
  for ry,ey,y in states(Y):
   p,a,q,c=x[0],x[1],x[2],x[4]
   b=p+a-c;d=q+a-c;r=p+2*(a-c);s=q+2*(a-c)
   checks+=1
   if x==(p,a,q,b,c,d) and y==(r,c,s,b,a,d):matches.append((swap,rx,ex,ry,ey))
assert checks==288 and not matches
out=dict(A=A,B=B,closure=True,dihedral_states_per_species=12,private_lengths=[5,1],AA_boundary_halfturn=A[1:]*2,AA_boundary_reflection=A[1:]+A[:0:-1],BB_boundary_halfturn=B[1:]*2,BB_boundary_reflection=B[1:]+B[:0:-1],AA_endpoint_halfturn=[[2,3],[2,3]],AA_endpoint_reflection=[[2,2],[3,3]],BB_endpoint_halfturn=[[3,4],[3,4]],BB_endpoint_reflection=[[4,4],[3,3]],both_monohedral_options_excluded=True,prior_cone_memberships=matches,prior_cone_checks=checks,infinite_assignment=False,periodic_escape=False,recursive_boundary_substitution=False)
print(json.dumps(out,indent=2))
