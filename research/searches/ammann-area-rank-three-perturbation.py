#!/usr/bin/env python3
"""Finite exact gate: one algebraic perturbation N=1000, no patch search.
Question: do54 strict supports, G1 and rank3 angle valuations certify this
rank3-area sample inside the already reviewed G*forcing domain?
Outcome rank3=>explicit area-rigid source; deficient valuation rank is not
proof of nongenericity. All3 normalized areas derived symbolically separately.
"""
import argparse,json
from pathlib import Path
from sage.all import QQ,QQbar,AA,NumberField,matrix
N=1000
z=QQbar.zeta(10);root2=QQbar(2).sqrt();alpha=z+root2
F=NumberField(alpha.minpoly(),"a",embedding=alpha)
w=F(z);r=F(root2);embed=F.hom([alpha],QQbar)
cj=F.hom([F(alpha.conjugate())],F)
s=F(QQ(9)/20);t=F(QQ(3)/4)+r/N;J=s+t*w
jp=1+w**4*(J-1);jpp=w+w**6*(J-w)
kp=w**2+w**6*(J-1);lp=1+w**7*(J-1-w);j2=1+w+w**2-J
T=((F(0),jp,F(1),J,w,jpp),(F(0),jp,F(1),lp,kp),(kp,lp,1+w**2,j2,w**2))
cross=lambda a,b:(cj(a)*b-a*cj(b))/(w-cj(w))
positive=lambda q:AA(embed(q).real())>0
assert positive(s) and positive(1-s) and positive(t) and positive(1-t)
assert all(positive(cross(P[(i+1)%len(P)]-P[i],P[k]-P[i]))
           for P in T for i in range(len(P)) for k in range(len(P)) if k not in(i,(i+1)%len(P)))
lens=((J-1-w)*cj(J-1-w),(J-1)*cj(J-1),(J-w)*cj(J-w),(kp-lp)*cj(kp-lp))
assert len(set(lens))==4 and all(positive(q) for q in lens)
phi=w+cj(w)
areas=tuple(sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2 for P in T)
f=(s*s+phi*s*t+t*t+(phi-2)*t)/2
assert areas==(F(1),phi-f,f)
# Rational independence in the absolute degree8 field.
M=matrix(QQ,[list(q) for q in areas]);assert M.rank()==3
rho=(-jp/(1-jp),(w-jpp)/(-jpp),(lp-kp)/(-kp))
angles=tuple(q/cj(q) for q in rho)
factors=[];primes=set()
for i,q in enumerate(angles):
    factor=list(F.ideal(q).factor());factors.append(factor)
    primes.update(P for P,e in factor)
    print("angle factor",i,"prime count",len(factor),flush=True)
primes=sorted(primes,key=str)
valuation=matrix(QQ,[[q.valuation(P) for q in angles] for P in primes])
rank=valuation.rank();print("valuation rank",rank,flush=True)
assert rank==3
out={"finite_domain":"one N=1000 perturbation;54 strict supports,four G1 lengths,three angle principal-ideal factorizations",
 "s":"9/20","t":"3/4+sqrt(2)/1000","absolute_field_polynomial":str(F.polynomial()),
 "w_coordinates":[str(q) for q in w],"sqrt2_coordinates":[str(q) for q in r],
 "area_coordinates":[[str(c) for c in q] for q in areas],"area_Q_rank":3,
 "strict_support_count":54,"G1_four_lengths_distinct":True,
 "primes":[{"repr":str(P),"norm":str(P.norm()),"basis":[[str(c) for c in q] for q in P.basis()]} for P in primes],
 "valuation_rows":[[str(c) for c in row] for row in valuation.rows()],"angle_valuation_rank":rank,
 "scope":"exact generic unmarked Ammann source sample;area rank implies fixed cluster content,no variable-content geometric enumeration"}
p=argparse.ArgumentParser();p.add_argument("--output",type=Path);args=p.parse_args()
if args.output:args.output.write_text(json.dumps(out,indent=2)+"\n")
print("PASS explicit degree8 rank3-area G* sample;54 supports,G1,three independent angle valuation vectors")
