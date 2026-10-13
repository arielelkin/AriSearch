#!/usr/bin/env python3
"""Independent symbolic closure gate for all generic complementary angles.

Finite domain: all 11 dihedral bracelets of 001122, with unit side lengths.
Question: can any non-012012 word close at generic angles?
The elimination certificate is resultant with the reciprocal polynomial,
which must also vanish for unit-modulus turn variables.
"""
from itertools import permutations
import sympy as s
u,v=s.symbols("u v")
turn=(u,v,-1/(u*v))
def canon(w):
    return min(t[k:]+t[:k] for t in (w,w[::-1]) for k in range(6))
words=sorted({canon(w) for w in permutations((0,0,1,1,2,2))})
assert len(words)==11
factor_cases={
 (0,0,1,2,2,1):(v+1)*(u**2*v+1)/(u*v),
 (0,0,2,1,1,2):(u-v)*(u*v-1)/(u*v),
 (0,1,0,2,1,2):(u**2*v+1)/u,
 (0,1,1,0,2,2):(u+1)*(u*v**2+1)/u,
 (0,1,2,0,2,1):(u*v**2+1)/(u*v),
 (0,1,2,1,0,2):(u-v)/u,
}
expected_resultants={
 (0,0,1,1,2,2):(u+1)**6*(u**2-u+1),
 (0,0,1,2,1,2):-(u+1)**2*(u**2-u+1),
 (0,1,0,1,2,2):2*u**2*(u+1)**2*(u**2-u+1),
 (0,1,1,2,0,2):2*(u+1)**2*(u**2-u+1),
}
for w in words:
    direction=residue=s.Integer(1)
    for c in w[1:]:
        direction*=turn[c]
        residue+=direction
    residue=s.factor(residue)
    if w==(0,1,2,0,1,2):
        assert residue==0
    elif w in factor_cases:
        assert s.cancel(residue-factor_cases[w])==0
    else:
        p=s.cancel(residue).as_numer_denom()[0]
        reciprocal=s.cancel(p.subs({u:1/u,v:1/v})).as_numer_denom()[0]
        result=s.factor(s.resultant(p,reciprocal,v))
        assert s.expand(result-expected_resultants[w])==0
print("PASS: all 11 symbolic bracelets; noncentral closure requires equal angle colours or angle 120 degrees, hence nongeneric.")
