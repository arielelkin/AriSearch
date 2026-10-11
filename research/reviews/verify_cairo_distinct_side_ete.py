#!/usr/bin/env python3
"""Exact four-case algebraic audit of the conditional Cairo ETE obstruction."""
from sage.all import QuadraticField,PolynomialRing,AA
from itertools import combinations

def main():
    sums=[(a,b) for a in range(5) for b in range(1,4) if 90*a+120*b==360]
    assert sums==[(0,3)]
    beta_edges=[{1,2},{3,4},{4,0}]
    assert beta_edges[0].isdisjoint(beta_edges[1]|beta_edges[2])
    assert beta_edges[1]&beta_edges[2]=={4}
    edge_set={frozenset(edge) for edge in beta_edges}
    assert not any(all(frozenset(pair) in edge_set for pair in combinations(triple,2))
                   for triple in combinations(range(5),3))
    F=QuadraticField(3,'w',embedding=AA(3).sqrt());w=F.gen()
    R=PolynomialRing(F,('c','d','e'));c,d,e=R.gens()
    a=(w*c+d-e)/2;b=(w*(d+e)-c)/2;L=d+e-w*c
    cases=[(b,a,d,c),(c,a,d,b),(b,d,a,c),(c,d,a,b)]
    for (B0,B1,B2,B3),factor in zip(cases,[2,-4,4,-2]):
        f=w*B2+B3-2*B0
        assert 2*B0-w*B2-B3+f==0
        assert 2*B1-w*(B3+f)+B2==factor*L
    assert a-d==-L/2 and b-c==w*L/2
    print('PASS: exact angle/120-corner graph constraints; all four B closure cases force a=d,b=c.')

if __name__=='__main__':main()
