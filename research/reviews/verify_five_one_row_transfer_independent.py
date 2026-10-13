#!/usr/bin/env python3
"""Independent endpoint-derived side maps and closure reversal algebra."""
from itertools import product
import sympy as s
P=list(product(range(6),(1,-1)))
AC=(0,1,2,0,1,2);BC=(1,0,0,0,0,0);BM=(0,1,2,2,1,0)
def nativecorner(p,k):return (p[0]+p[1]*k)%6
def nativeside(p,k):
    endpoints=frozenset((nativecorner(p,k),nativecorner(p,k+1)))
    matches=[i for i in range(6) if frozenset((i,(i+1)%6))==endpoints]
    assert len(matches)==1;return matches[0]
A=[p for p in P if {nativeside(p,5),nativeside(p,2)}=={0,3}]
B=[p for p in P if {nativeside(p,5),nativeside(p,2)}=={1,4}]
assert A==[(0,-1),(1,1),(3,-1),(4,1)]
assert B==[(1,-1),(2,1),(4,-1),(5,1)]
maps={}
for p in A:
    assert all(AC[nativecorner(p,k)]==2 for k in (1,4))
    choices=[q for q in A if nativeside(p,5)==nativeside(q,2)
             and AC[nativecorner(p,0)]==AC[nativecorner(q,2)]
             and AC[nativecorner(p,5)]==AC[nativecorner(q,3)]]
    assert len(choices)==1;maps[p]=choices[0]
assert maps=={(0,-1):(4,1),(1,1):(3,-1),(3,-1):(1,1),(4,1):(0,-1)}
assert all(maps[maps[p]]==p for p in A)
for p,q in product(B,repeat=2):
    assert BM[nativeside(p,5)]==BM[nativeside(q,2)]==1
    assert BC[nativecorner(p,0)]==BC[nativecorner(q,2)]==0
    assert BC[nativecorner(p,5)]==BC[nativecorner(q,3)]==0
E=s.symbols("E",nonzero=True);m,n,p,q=s.symbols("m n p q",real=True)
f=m+p*E+n*E**2+n*E**3+q*E**4+m*E**5
assert s.cancel(f-E**5*f.subs(E,1/E)-(p-q)*(E-E**4))==0
x=s.symbols("x",real=True);y=720-5*x;z=4*x-360;r=360-2*x;special=10*x-1080
assert s.expand(x+y+z)==360
assert s.expand(2*x+r)==s.expand(2*y+special)==s.expand(z+2*r)==360
print("PASS: endpoint-derived12 native maps, fourA/fourB row states, fullA two-cycles, all16 independent BB transfers and exact closure reversal")
