#!/usr/bin/env python3
"""Independent 56-triple reconstruction via native-colour multiplicities."""
import json
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

def direction(coeff):
    a,b=coeff[0]-coeff[2],coeff[1]-coeff[2]
    if a==b==0:return None
    scale=a or b
    return Fraction(a,scale),Fraction(b,scale)
root=Path(__file__).resolve().parents[2]
cert=json.loads((root/"research/certificates/two-hexagon-ternary-resonance-ledger.json").read_text())
groups={};base=[]
for t in combinations_with_replacement(range(6),3):
    c=[0,0,0]
    for k in t:c[k%3]+=1 if k<3 else -2
    key=direction(c)
    if key is None:base.append(list(t))
    else:groups.setdefault(key,[]).append(list(t))
assert base==cert["identities"] and len(groups)==12
actual={}
for row in cert["lines"]:
    a,b=row["line"];scale=a or b
    key=(Fraction(a,scale),Fraction(b,scale))
    assert key not in actual
    actual[key]=row["extra_triples"]
    f,ij=row["family"],row["indices"]
    c=[0,0,0]
    if f=="angle120":c[ij[0]]=1
    elif f=="equal_angles":c[ij[0]]=1;c[ij[1]]=-1
    else:
        assert f=="one_ABB" and len(ij)==2 and ij[0]!=ij[1]
        i,j=ij;c[i]=1;c[j]=-4
        assert row["extra_triples"]==[sorted((i,3+j,3+j))]
        q=row["potential"]
        assert len(q)==6 and q[3:]==[-2*x for x in q[:3]]
        assert sum(q[:3])==0 and all(sum(q[k] for k in t)==0 for t in base)
        assert sum(q[k] for k in row["extra_triples"][0])==row["extra_score"]==5
    assert direction(c)==key
assert actual==groups
assert sum(row["family"]=="one_ABB" for row in cert["lines"])==6
print("PASS: independent multiplicity projection reconstructs56 triples,12 lines,6 sole-ABB stars and all zero-tile positive-star potentials")

# Complete type-constant potential-removal classification, assuming base stars0.
residual=0
for row in cert["lines"]:
    if row["family"]=="one_ABB":continue
    normal=row["line"]
    multiples=[]
    for triple in row["extra_triples"]:
        c=[0,0,0]
        for k in triple:c[k%3]+=1 if k<3 else -2
        a,b=c[0]-c[2],c[1]-c[2]
        q=Fraction(a,normal[0]) if normal[0] else Fraction(b,normal[1])
        assert (a,b)==(q*normal[0],q*normal[1])
        multiples.append(q)
    assert min(multiples)<0<max(multiples)
    residual+=1
assert residual==6
print("PASS: each of six residual lines has opposite score signs; full-language nonnegativity forces every extra score0")
