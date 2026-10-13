#!/usr/bin/env python3
"""Independent symbolic areas and exact G*sample; only3 small valuation rows.
Reads retained ideal bases; imports no producer and refactors no large norm.
"""
from pathlib import Path
import json
from sage.all import QQ,ZZ,QQbar,AA,NumberField,CyclotomicField,PolynomialRing,matrix
root=Path(__file__).resolve().parents[2]
c=json.loads((root/"research/certificates/ammann-area-rank-three-perturbation.json").read_text())
# Universal area identities from the reviewed indexed vertex lists.
K=CyclotomicField(10);w=K.gen();R=PolynomialRing(K,("s","t"));s,t=R.gens()
def tiles(J,w):
    jp=1+w**4*(J-1);jpp=w+w**6*(J-w)
    kp=w**2+w**6*(J-1);lp=1+w**7*(J-1-w);j2=1+w+w**2-J
    return ((0,jp,1,J,w,jpp),(0,jp,1,lp,kp),(kp,lp,1+w**2,j2,w**2))
conj=lambda p:R({e:a.conjugate() for e,a in R(p).dict().items()})
A=[]
for P in tiles(s+t*w,w):
    A.append(R(sum((conj(P[i])*R(P[(i+1)%len(P)])-R(P[i])*conj(P[(i+1)%len(P)]))
                   /(2*(w-w.conjugate())) for i in range(len(P)))))
phi=w+w.conjugate();f=(s*s+phi*s*t+t*t+(phi-2)*t)/2
assert A==[R(1),R(phi-f),R(f)]
# Nonzero rational coefficient minor (constant1,constantphi,s^2).
rows=[]
for p in A:
    vals=[]
    for monomial in (R(1),s*s):
        q=list(K(p.monomial_coefficient(monomial)));b=q[2]
        assert q[1]==0 and q[3]==-b
        vals.extend((q[0]-b,b))
    rows.append([vals[0],vals[1],vals[2]])
assert matrix(QQ,rows).det()==QQ(1)/2
# Independently build actual vertices in QQbar, with positive square root.
z=QQbar.zeta(10);r=QQbar(2).sqrt();N=1000
ss=QQbar(QQ(9)/20);tt=QQbar(QQ(3)/4)+r/N
assert 0<ss.real()<1 and 0<tt.real()<1
P=tuple(tuple(QQbar(q) for q in p) for p in tiles(ss+tt*z,z))
det=lambda a,b:AA((a.conjugate()*b).imag())
assert sum(len(p)*(len(p)-2) for p in P)==54
assert all(det(p[(i+1)%len(p)]-p[i],p[j]-p[i])>0
           for p in P for i in range(len(p)) for j in range(len(p)) if j not in(i,(i+1)%len(p)))
J=ss+tt*z;kp=P[1][-1];lp=P[1][-2]
L=((J-1-z),(J-1),(J-z),(kp-lp))
assert len({q*q.conjugate() for q in L})==4
# Define the degree8 absolute field independently with fixed exact embedding.
QX=PolynomialRing(QQ,"x");x=QX.gen()
poly=x**8-2*x**7-5*x**6+8*x**5+19*x**4-28*x**3-5*x**2+22*x+31
alpha=z+r
assert poly(alpha)==0 and poly.is_irreducible()
F=NumberField(poly,"a",embedding=alpha)
areas=tuple(F(sum(det(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/(2*AA(z.imag()))) for p in P)
assert matrix(QQ,[list(a) for a in areas]).rank()==3
phi=F(z+z.conjugate());q2=F(r)
ff=F(-QQ(147)/400+QQ(1)/N**2)+QQ(87)/160*phi+(-QQ(1)/(4*N)+QQ(29)/(40*N)*phi)*q2
assert areas==(F(1),phi-ff,ff)
# In the independent real basis1,phi,sqrt2,phi*sqrt2, a minor=-1/(4N).
minor=matrix(QQ,[[1,0,0],[QQ(147)/400-QQ(1)/N**2,QQ(73)/160,QQ(1)/(4*N)],
                       [-QQ(147)/400+QQ(1)/N**2,QQ(87)/160,-QQ(1)/(4*N)]]).det()
assert minor==-QQ(1)/(4*N)
rho=((P[0][0]-P[0][1])/(P[0][2]-P[0][1]),
     (P[0][4]-P[0][5])/(P[0][0]-P[0][5]),
     (P[1][3]-P[1][4])/(P[1][0]-P[1][4]))
q=[F(a/a.conjugate()) for a in rho]
selected=((281,(0,0,-1)),(3391,(1,0,0)),(401,(1,-1,-1)))
checked=[]
for norm,row in selected:
    candidates=[i for i,p in enumerate(c["primes"]) if ZZ(p["norm"])==norm
                and tuple(QQ(a) for a in c["valuation_rows"][i])==row]
    assert len(candidates)==1
    rec=c["primes"][candidates[0]]
    ideal=F.ideal([F([QQ(a) for a in v]) for v in rec["basis"]])
    assert ideal.norm()==norm and ideal.is_prime()
    actual=tuple(a.valuation(ideal) for a in q);assert actual==row
    checked.append(actual)
assert matrix(QQ,checked).det()==1
assert c["area_Q_rank"]==c["angle_valuation_rank"]==3
assert c["strict_support_count"]==54 and c["G1_four_lengths_distinct"]
assert [[str(a) for a in q] for q in areas]==c["area_coordinates"]
print("PASS universal symbolic Qarea rank3; explicit N1000 has54 supports,G1 and three small-prime angle valuations determinant1, hence G* and Q-independent areas")
