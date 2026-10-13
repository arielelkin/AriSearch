#!/usr/bin/env python3
from itertools import product
AC=(0,1,2,0,1,2);BC=(1,0,0,0,0,0);Bmetric=(0,1,2,2,1,0)
P=list(product(range(6),(1,-1)))
def side(r,s,k):return(r+k)%6 if s==1 else(r-k-1)%6
corner=lambda c,r,s,k:c[(r+s*k)%6]
A=[(r,s) for r,s in P if {side(r,s,5),side(r,s,2)}=={0,3}]
B=[(r,s) for r,s in P if {side(r,s,5),side(r,s,2)}=={1,4}]
assert A==[(0,-1),(1,1),(3,-1),(4,1)]
assert B==[(1,-1),(2,1),(4,-1),(5,1)]
transitions={}
for r,s in A:
    successors=[(u,v) for u,v in A if side(r,s,5)==side(u,v,2)
        and corner(AC,r,s,0)==corner(AC,u,v,2)
        and corner(AC,r,s,5)==corner(AC,u,v,3)]
    assert len(successors)==1;transitions[(r,s)]=successors[0]
assert transitions=={(0,-1):(4,1),(1,1):(3,-1),(3,-1):(1,1),(4,1):(0,-1)}
assert all(transitions[transitions[a]]==a for a in A)
for r,s in B:
    assert Bmetric[side(r,s,5)]==Bmetric[side(r,s,2)]==1
    assert all(corner(BC,r,s,k)==0 for k in(0,2,3,5))
print("PASS12nativeplacements=>fourA/fourB rowstates;uniqueArow two-cycle transitions;allB choices have constantBB metric and r/r endpoints")
