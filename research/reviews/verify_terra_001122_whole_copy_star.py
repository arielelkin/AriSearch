#!/usr/bin/env python3
"""Independent exact root isolation and actual three-copy AAA patch."""
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(360);z=K.gen();h=K.hom([QQbar.zeta(360)],QQbar)
re,im=AA(h(z).real()),AA(h(z).imag())
assert re>AA(99)/100 and AA(1745)/100000<im<AA(1746)/100000
cr=lambda p,q:(p.conjugate()*q-p*q.conjugate())/(2*z**90)
S=(1+z**67,z**126+z**185,z**239+z**293)
v=(cr(S[1],S[2]),cr(S[2],S[0]),cr(S[0],S[1]))
a=tuple(v[i//2]/v[0] for i in range(6));p=[K(0)]
for t,d in zip(a,(0,67,126,185,239,293)):p.append(p[-1]+t*z**d)
assert p[-1]==0
P=[p[:6],[z**(-126)*(q-p[4]) for q in p[:6]],[z**113*(q-p[2]) for q in p[:6]]]
for Q,lo,hi in zip(P,(0,113,239),(113,239,360)):
    for q in Q:
        assert AA(h(cr(z**lo,q)).real())>=0
        assert AA(h(cr(q,z**hi)).real())>=0
assert P[0][1]==P[2][1]
assert P[0][5]==P[1][5]
assert P[1][3]==P[2][3]
print("PASS exact root interval and three explicit whole copies in disjoint convex wedges; all ray endpoints match")
