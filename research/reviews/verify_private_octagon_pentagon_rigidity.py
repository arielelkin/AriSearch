#!/usr/bin/env python3
"""Supplementary independent exact audit of all10 repeated-length cases.

The full every-tiling theorem is analytically reviewed in the companion
Markdown record; this checker verifies only the universal pentagon algebra.
No producer imports or numerical branches. Kernels are over exact real
coefficients embedded in Q(zeta20), not a bounded metric parameter sample.
"""
from itertools import combinations
from sage.all import CyclotomicField,matrix,vector

def main():
    K=CyclotomicField(20);zeta=K.gen();ii=zeta**5;w=zeta**4
    C=[(w**j+w**(-j))/2 for j in range(5)]
    S=[(w**j-w**(-j))/(2*ii) for j in range(5)]
    closure=matrix(K,[C,S]);assert closure.rank()==2
    for i,j in combinations(range(5),2):
        rho=[(i+j-h)%5 for h in range(5)]
        other=next((p,rho[p]) for p in range(5) if p<rho[p] and {p,rho[p]}!={i,j})
        repeat=vector(K,[int(h==i)-int(h==j) for h in range(5)])
        M=closure.stack(matrix(K,[repeat]));assert M.rank()==3
        p,q=other
        other_repeat=vector(K,[int(h==p)-int(h==q) for h in range(5)])
        assert M.stack(matrix(K,[other_repeat])).rank()==3
        for L in M.right_kernel().basis():
            assert all(t.conjugate()==t for t in L)
            assert all(L[h]==L[rho[h]] for h in range(5))
            V=[K(0)]
            for h in range(5):V.append(V[-1]+L[h]*w**h)
            assert V[-1]==0
            offset=V[(i+j+1)%5]
            reflect=lambda x:-w**(i+j)*x.conjugate()+offset
            assert all(reflect(V[h])==V[(i+j+1-h)%5] for h in range(5))
            assert reflect(reflect(K(0)))==0
        print((i,j),"forces",other,"real closure kernel dimension2; reflected walk verified",flush=True)
    print("PASS all10 equality pairs; explicit reflection r(x)=-w^(i+j)conj(x)+v_(i+j+1).",flush=True)

if __name__=="__main__":
    if not __debug__:raise RuntimeError("Assertions required")
    main()
