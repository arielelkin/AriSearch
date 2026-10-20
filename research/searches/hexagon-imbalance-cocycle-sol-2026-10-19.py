#!/usr/bin/env python3
"""Exact minimal-dual-face gate. No plane extension search."""
import sympy as S
h,a,b=S.symbols("h a b", real=True)
c=h+a
u=[S.Matrix([1,0]),S.Matrix([S.Rational(1,2),S.sqrt(3)/2]),S.Matrix([-S.Rational(1,2),S.sqrt(3)/2]),S.Matrix([-1,0]),S.Matrix([-S.Rational(1,2),-S.sqrt(3)/2]),S.Matrix([S.Rational(1,2),-S.sqrt(3)/2])]
A=[c,h,c,h,c,h]
B=[c,c,c+b,c-b,c+b,c]
def clean(v): return v.applyfunc(S.simplify)
def vertices(lengths):
    q=[S.zeros(2,1)]
    for k,l in enumerate(lengths): q.append(q[-1]+l*u[k])
    assert clean(q[-1])==S.zeros(2,1)
    return q[:-1]
# All twelve states of both symbols close and have the stated signed imbalance.
for lengths,delta in [(A,a),(B,b)]:
    for r in range(6):
        for eps in [-1,1]:
            ls=[lengths[(r+eps*k)%6] for k in range(6)]
            vertices(ls)
            for k in range(6):
                assert S.simplify(ls[k]-ls[(k+3)%6]-(-1)**(r+k)*delta)==0
ls=[B,A,[A[(k+1)%6] for k in range(6)]]
q=list(map(vertices,ls))
j=[0,2,4]
t=[-q[i][j[i]] for i in range(3)]
# Oriented dual triangle B -> A0 -> A1 -> B; source side k.
seams=[(0,1,5),(1,2,1),(2,0,3)]
Ds=[]
for f,g,k in seams:
    assert S.simplify(ls[f][k]-ls[g][(k+3)%6])==0
    D=q[f][k]-q[g][(k+4)%6]
    assert clean(D-(t[g]-t[f]))==S.zeros(2,1)
    assert clean(t[f]+q[f][(k+1)%6]-t[g]-q[g][(k+3)%6])==S.zeros(2,1)
    Ds.append(D)
assert clean(sum(Ds,S.zeros(2,1)))==S.zeros(2,1)
print("PASS: 24 phase/parity states; 3 exact seams; zero dual triangle holonomy")
print("A=(h+a,h,h+a,h,h+a,h), B=(c,c,c+b,c-b,c+b,c), c=h+a")
print("Positive noncentral domain: h>0, a>0, 0<abs(b)<c")
print("Triangle signed imbalance sum = b (not constrained to zero)")
print("Fixture h=a=b=1: A=(2,1,2,1,2,1), B=(2,2,3,1,3,2)")
