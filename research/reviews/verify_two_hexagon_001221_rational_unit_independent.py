#!/usr/bin/env python3
"""Independent isolated algebraic V and exact A/B vertices; no author imports."""
import json
from pathlib import Path
from itertools import combinations_with_replacement
from sage.all import QQ,QQbar,AA,PolynomialRing,QuadraticField
R=PolynomialRing(QQ,"X");X=R.gen()
# Explicit rational coefficients, ascending; from retained degree12 defining polynomial.
coeff=(1,-QQ(113)/25,QQ(14833)/2000,QQ(11961)/2500,-QQ(366807)/62500,
       QQ(395647)/312500,QQ(66847)/125000,QQ(395647)/312500,
       -QQ(366807)/62500,QQ(11961)/2500,QQ(14833)/2000,-QQ(113)/25,1)
f=R(coeff)
assert f.degree()==12 and f.is_irreducible()
roots=f.roots(QQbar,multiplicities=False)
assert len(roots)==12
inside=[q for q in roots if QQ(299)/1000<q.real()<QQ(300)/1000
        and QQ(954)/1000<q.imag()<QQ(955)/1000]
assert len(inside)==1
v=inside[0];u=(QQbar(3)+4*QQbar.zeta(4))/5;w=-1/(u*v)
assert f(v)==0
# Derive the closure numerator independently over Q(i) by determinant ratios.
C=QuadraticField(-1,"J");J=C.gen();RR=PolynomialRing(C,"T");FF=RR.fraction_field();t=FF.gen()
us=FF((3+4*J)/5);ws=-1/(us*t)
SS=(1+us,us*t*(1+t),-t*(1+ws))
SC=(1+1/us,(1+1/t)/(us*t),-(1+1/ws)/t)
cc=lambda i,j:SC[i]*SS[j]-SS[i]*SC[j]
LL=(FF(1),cc(2,0)/cc(1,2),cc(0,1)/cc(1,2))
turn=(us,t,ws);edge=FF(1);closure=LL[0]
for col,side in zip((0,1,2,2,1),(0,1,2,1,0)):
    edge*=-1/turn[col]**2;closure+=LL[side]*edge
numerator=closure.numerator().monic()
conjugate=RR([q[0]-q[1]*J for q in numerator])
assert numerator.degree()==6
assert R([QQ(q) for q in numerator*conjugate])==f
assert numerator.gcd(numerator.derivative()).degree()==0
QR=PolynomialRing(QQbar,"Y")
qp=QR([QQbar(q[0])+QQbar(q[1])*QQbar.zeta(4) for q in numerator])
assert qp(v)==0
admissible=[]
for q in roots:
    if not(q.real()>0 and q.imag()>0 and q*q.conjugate()==1):continue
    z=-1/(u*q)
    if not(z.real()>0 and z.imag()>0 and z*z.conjugate()==1):continue
    if qp(q)==0:admissible.append(q)
assert admissible==[v]
assert all(q.real()>0 and q.imag()>0 and q*q.conjugate()==1 for q in (u,v,w))
def det(a,b):return AA((a.conjugate()*b).imag())
S=(1+u,u*v*(1+v),-v*(1+w))
h=(det(S[1],S[2]),det(S[2],S[0]),det(S[0],S[1]))
length=tuple(QQbar(q/h[0]) for q in h)
assert all(q.imag()==0 and q.real()>0 for q in length) and len(set(length))==3
Aword=(0,0,1,1,2,2);Bword=(0,0,1,2,2,1)
Alength=(length[0],length[0],length[1],length[1],length[2],length[2])
# Derive B lengths solely from unordered AB endpoint palette.
palette={tuple(sorted((Aword[i],Aword[(i+1)%6]))):Alength[i] for i in range(6)}
Blength=tuple(palette[tuple(sorted((Bword[i],Bword[(i+1)%6])))] for i in range(6))
Aangle=tuple(-1/q for q in (u,v,w));Bangle=tuple(q*q for q in (u,v,w))
P=[]
for word,turns,ls in ((Aword,(u,v,w),Alength),(Bword,tuple(-1/q**2 for q in (u,v,w)),Blength)):
    es=[QQbar(1)]
    for i in word[1:]:es.append(es[-1]*turns[i])
    verts=[QQbar(0)]
    for le,e in zip(ls,es):verts.append(verts[-1]+le*e)
    assert verts[-1]==0
    assert all(det(verts[i+1]-verts[i],verts[j]-verts[i])>0
               for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
    P.append(verts[:6])
allangle=Aangle+Bangle
triples=[list(t) for t in combinations_with_replacement(range(6),3)
         if allangle[t[0]]*allangle[t[1]]*allangle[t[2]]==1]
assert triples==[[0,0,3],[0,1,2],[1,1,4],[2,2,5],[3,4,5]]
for word,ang,ls in ((Aword,Aangle,Alength),(Bword,Bangle,Blength)):
    for offset in range(6):
        for eps in (1,-1):
            at=lambda i:ang[word[(offset+eps*i)%6]]
            le=lambda i:ls[(offset+i)%6] if eps==1 else ls[(offset-i-1)%6]
            assert not(at(0)*at(1)*at(2)==1 and le(2)==le(5))
            assert not(at(0)*at(1)*at(3)==1 and le(1)==le(3) and le(2)==le(5))
            assert not(all(at(i)==QQbar.zeta(3) for i in (0,2,4))
                       and le(0)==le(1) and le(2)==le(3) and le(4)==le(5))
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/two-hexagon-001221-rational-unit-slice.json").read_text())
assert c["root_count"]==6 and len(c["retained_unit_acute_roots"])==1
row=c["retained_unit_acute_roots"][0]
assert R(row["V_minpoly"].replace("x","X"))==f
assert row["actual_triples"]==triples and row["exact_generic_star_language"]
assert row["A_strictly_convex"] and row["B_strictly_convex"]
assert row["A_monohedral_classes"]==row["B_monohedral_classes"]==[]
print("PASS: irreducible degree12 V uniquely isolated in rational rectangle; exact A/B closure,48 strict supports, five stars,24 dihedral monohedral exclusions")
