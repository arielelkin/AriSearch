#!/usr/bin/env python3
"""Generic exact affine gluing identities for the seven-motif Q12 family.

The coefficient field is cyclotomic24. ell and rho are formal variables,
so side identities are checked for every real ell and every rho=exp(-ip),
not only over a finite sample. Convexity and the area/covering argument are
analytic obligations in the accompanying lemma. No producer import.
"""
import json
from sage.all import CyclotomicField,PolynomialRing


def main():
    if not __debug__:raise RuntimeError('Assertions are proof relevant.')
    K=CyclotomicField(24);zz=K.gen();omega=zz**8
    ring=PolynomialRing(K,names=('ell','rho'));ell,rho=ring.gens()
    radius=zz+zz**(-1)
    p=[ring(0),ell,ell+zz**5*rho,ell*omega-zz**15*rho,ell*omega]
    qc=ell+radius*rho;s=(1+omega)*qc
    u=(omega-1)*qc;v=(omega**2-1)*qc
    motifs=[[qc+(p[2]-qc)*zz**(2*j) for j in range(12)]]
    motifs += [[omega**j*x for x in p] for j in range(3)]
    motifs += [[s-omega**j*x for x in p] for j in range(3)]
    # Entry (Q side, opposite motif, opposite P side, lattice offset).
    table=[(0,1,1,0,0),(1,3,3,0,0),(2,6,1,-1,1),(3,5,3,-1,1),
           (4,2,1,-1,0),(5,1,3,-1,0),(6,4,1,-1,0),(7,6,3,-1,0),
           (8,3,1,0,-1),(9,2,3,0,-1),(10,5,1,0,0),(11,4,3,0,0)]
    pairs=[(0,r,i,k,n,m) for r,i,k,n,m in table]
    for j in range(3):
        pairs.append((1+j,4,1+(j+1)%3,0,0,0))
        pairs.append((4+j,4,4+(j+1)%3,0,0,0))
    for j,(n,m) in enumerate(((0,0),(0,1),(-1,1))):
        pairs.append((1+j,2,4+j,2,n,m))
    assert len(pairs)==21
    used=set()
    corners=[(i,j) for i,p in enumerate(motifs) for j in range(len(p))]
    parent={c:c for c in corners}
    def root(c):
        while parent[c]!=c:
            parent[c]=parent[parent[c]];c=parent[c]
        return c
    def join(a,b):parent[root(a)]=root(b)
    for i,j,k,l,n,m in pairs:
        assert (i,j) not in used and (k,l) not in used
        used|={(i,j),(k,l)}
        a,b=motifs[i][j],motifs[i][(j+1)%len(motifs[i])]
        c,d=motifs[k][l]+n*u+m*v,motifs[k][(l+1)%len(motifs[k])]+n*u+m*v
        assert a==d and b==c,(i,j,k,l,n,m)
        join((i,j),(k,(l+1)%len(motifs[k])))
        join((i,(j+1)%len(motifs[i])),(k,l))
    assert len(used)==42
    classes={}
    for c in corners:classes.setdefault(root(c),[]).append(c)
    groups=sorted(sorted(g) for g in classes.values())
    assert len(groups)==14 and all(len(g)==3 for g in groups)
    triple_P=0;QPP=0
    for g in groups:
        q=[c for c in g if c[0]==0]
        pp=[c for c in g if c[0]!=0]
        if not q:
            assert len(pp)==3 and all(c[1]==0 for c in pp)
            triple_P+=1
        else:
            assert len(q)==1 and len(pp)==2
            assert sorted(c[1] for c in pp) in ([1,4],[2,3])
            QPP+=1
    assert triple_P==2 and QPP==12
    print(json.dumps({'scope':'generic affine gluing over cyclotomic24[ell,rho]',
                      'paired_edges':pairs,'vertex_classes':groups,
                      'two_PPP_beta_stars':triple_P,'twelve_QPP_complement_stars':QPP},
                     indent=2,sort_keys=True))


if __name__=='__main__':main()
