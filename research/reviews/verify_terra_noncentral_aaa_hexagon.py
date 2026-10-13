#!/usr/bin/env python3
"""Exact single counterexample, independent of the native-word producer."""
from sage.all import CyclotomicField,QQbar,AA
K=CyclotomicField(360);z=K.gen();h=K.hom([QQbar.zeta(360)],QQbar)
angles=(113,113,121,121,126,126)
dirs=(0,67,126,185,239,293)
cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(2*z**90)
S=(1+z**67,z**126+z**185,z**239+z**293)
v=(cross(S[1],S[2]),cross(S[2],S[0]),cross(S[0],S[1]))
lengths=tuple(v[i//2]/v[0] for i in range(6))
real=lambda x:AA(h(x).real())
assert all(real(l)>0 for l in lengths)
assert len(set(lengths))==3
verts=[K(0)]
for l,d in zip(lengths,dirs):verts.append(verts[-1]+l*z**d)
assert verts[-1]==0
assert all(real(cross(verts[i+1]-verts[i],verts[j]-verts[i]))>0
           for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
# Native AAA corners0,2,4 have arms(c,a),(a,b),(b,c).
assert sum(angles[i] for i in (0,2,4))==360
assert lengths[0]==lengths[1] and lengths[2]==lengths[3] and lengths[4]==lengths[5]
assert any(lengths[i]!=lengths[i+3] for i in range(3))
# Reinhardt family conditions in Zhu-Wang-Yan arXiv2508.01404v2, Introduction.
for k in range(6):
    for sign in (1,-1):
        angle=lambda i:angles[(k+sign*i)%6]
        side=lambda i:lengths[(k+i)%6] if sign==1 else lengths[(k-i-1)%6]
        assert not (sum(angle(i) for i in (0,1,2))==360 and side(2)==side(5))
        assert not (sum(angle(i) for i in (0,1,3))==360 and side(1)==side(3) and side(2)==side(5))
        assert not (all(angle(i)==120 for i in (0,2,4)) and side(0)==side(1) and side(2)==side(3) and side(4)==side(5))
print("PASS exact positive strictly convex A001122 with legalAAA, noncentral, outside all three monohedral hexagon classes")
print("class lengths:",*[real(lengths[i]) for i in (0,2,4)])
