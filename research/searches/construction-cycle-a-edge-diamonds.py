#!/usr/bin/env python3
"""Retained exact ONE-seam/ONE-kink evidence. No atlas or congruence search.
Print JSON; accepts no candidate parameters. Assertion-enabled Sage required.
"""
import json
from sage.all import CyclotomicField, QQ, QQbar, AA
K=CyclotomicField(10);w=K.gen();emb=K.hom([QQbar.zeta(10)])
def cross(a,b):return (a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def sign(a):return int(AA(emb(a)).sign())
def enc(a):return [str(c) for c in K(a).vector()]
def area2(P):return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))
def turns(P):return [sign(cross(P[(i+1)%len(P)]-P[i],P[(i+2)%len(P)]-P[(i+1)%len(P)])) for i in range(len(P))]
J=QQ(1)/2+QQ(4)/5*w;Jp=1+w**4*(J-1);Jpp=w+w**6*(J-w)
k=w**2+w**6*(J-1);l=1+w**7*(J-1-w)
H=[K(0),Jp,K(1),J,w,Jpp];P1=[K(0),Jp,K(1),l,k]
u=Jp/k
assert u*u.conjugate()==1
assert u*k==Jp
HP1=[u*z for z in P1]
cH=sum(H)/6;cP=sum(HP1)/5
assert all(sign(cross(H[(i+1)%6]-H[i],cH-H[i]))==1 for i in range(6))
assert all(sign(cross(HP1[(i+1)%5]-HP1[i],cP-HP1[i]))==1 for i in range(5))
assert sign(cross(Jp,cH))==1 and sign(cross(Jp,cP))==-1
Q=[K(0),cP,Jp,cH]
assert turns(Q)==[1,1,1,1]
assert area2(Q)==area2([K(0),Jp,cH])+area2([Jp,K(0),cP])
U,V=Jp,cH;epsilon=QQ(1)/1000
M=(U+V)/2-epsilon*(w-w.conjugate())*(V-U)
T=[Jp,K(1),cH]
assert all(sign(cross(T[(i+1)%3]-T[i],M-T[i]))==1 for i in range(3))
Qrepair=[K(0),cP,Jp,M,cH]
assert turns(Qrepair)==[1,1,1,1,1]
assert sign(cross(M-U,V-M))==1
assert sign(cross(M-V,U-M))==-1
# Neighbor's local fan triangle loses the cap along the reversed interface.
Trepair=[Jp,K(1),cH,M]
assert turns(Trepair)[2]==-1
cap=[U,V,M]
assert sign(area2(cap))==-1
assert area2(Qrepair)-area2(Q)==-area2(cap)
assert area2(Qrepair)+area2(Trepair)==area2(Q)+area2(T)
# Classical convex-quadrilateral carrier has independent diagonal periods.
t1=Q[2]-Q[0];t2=Q[3]-Q[1]
assert cross(t1,t2)!=0
out={"domain":"J=1/2+4/5w; one required H0-P1K seam; one kink epsilon=1/1000; no atlas/congruence enumeration",
 "field":"Q(w), Phi10=w^4-w^3+w^2-w+1; w=exp(i*pi/5)",
 "source_H":[enc(z) for z in H],"placed_P1":[enc(z) for z in HP1],
 "unit_placement":enc(u),"centroids":{"H":enc(cH),"P1":enc(cP)},
 "diamond":[enc(z) for z in Q],"diamond_turn_signs":turns(Q),"diamond_area2":enc(area2(Q)),
 "repair":{"epsilon":str(epsilon),"U":enc(U),"V":enc(V),"M":enc(M),
 "new_diamond":[enc(z) for z in Qrepair],"turn_signs":turns(Qrepair),
 "M_strictly_inside_neighbor_fan_triangle":True,"neighbor_local_turn_at_M":-1,
 "area_reassignment_exact":True},
 "quadrilateral_omission_periods":[enc(t1),enc(t2)],
 "scope":"Infinite covering is analytic and finite many supports, possibly nonconvex. Exact computation certifies this one convex crossed diamond and failed pentagonal kink only; not a two-shape covering."}
print(json.dumps(out,indent=2))
