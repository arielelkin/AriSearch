#!/usr/bin/env python3
"""Exact7680 repeated-U sixwheel native boundary/closure cases."""
from sage.all import QQ,AA,PolynomialRing,NumberField,matrix,Polyhedron
from itertools import combinations,product
from pathlib import Path
import argparse,json

def build(progress=False):
    R=PolynomialRing(QQ,'t');t=R.gen();f=t**4-2*t**2-4
    apos=[r for r in f.roots(AA,multiplicities=False) if 1<r<2][0]
    F=NumberField(f,'a',embedding=apos);a=F.gen();phi=a*a/2
    closure=matrix(F,[[2,-phi,-phi,1-phi,phi-1],[0,1,-1,-phi,-phi]])
    def coeff(x):
        z=list(x);return [str(c)for c in z]+['0']*(4-len(z))
    def basis(K):return [[coeff(x)for x in row]for row in K.basis_matrix().rows()]
    records=[];singulars=[];positive=[];assignment_count=0
    for native in product((0,2),(1,),(0,2),(3,4),(3,4)):
        for center_large,nlarge in [(False,2),(True,1)]:
            for big in combinations(range(5),nlarge):
                scales=[a if i in big else F(1)for i in range(5)]
                for refl in product((0,1),repeat=5):
                    M=matrix(F,5,5)
                    for i in range(5):
                        M[i,i]=a*a
                        M[i,(native[i]-1)%5 if refl[i] else native[i]]-=scales[i]
                        e=(i+1)%5
                        M[i,native[e] if refl[e] else (native[e]-1)%5]-=scales[e]
                    key={'native_indices':list(native),'central_large':center_large,
                         'large_corners':list(big),'reflections':list(refl)}
                    det=M.det();row=dict(key,determinant_coefficients=coeff(det));records.append(row)
                    if det:continue
                    K=M.right_kernel();N=M.stack(closure);J=N.right_kernel()
                    sr=dict(key,boundary_rank=int(M.rank()),boundary_kernel=basis(K),
                         closure_rank=int(N.rank()),closure_kernel=basis(J),
                         positive_feasible=False)
                    if J.dimension()==1:
                        v=J.basis()[0];s=sum(v)
                        if s and all(AA(x/s)>0 for x in v):
                            sr['positive_feasible']=True;sr['normalized_witness']=[coeff(x/s)for x in v]
                    elif J.dimension()>1:
                        # Exact bounded normalized polyhedron in l0,...,l4,delta.
                        eqns=[[AA(0)]+[AA(x)for x in r]+[AA(0)]for r in N.rows()]
                        eqns+=[[-AA(1)]+[AA(1)]*5+[AA(0)]]
                        ieqs=[[AA(0)]+[AA(int(i==j))for j in range(5)]+[-AA(1)]for i in range(5)]
                        ieqs+=[[AA(0)]+[AA(0)]*5+[AA(1)]]
                        P=Polyhedron(eqns=eqns,ieqs=ieqs,base_ring=AA,backend='field')
                        sr['polyhedron_empty']=P.is_empty()
                        if not P.is_empty():
                            v=max(P.vertex_generator(),key=lambda v:v[5]);delta=v[5]
                            sr['max_delta_exact']=str(delta)
                            if delta>0:
                                sr['positive_feasible']=True
                                # Algebraic defining data, not decimal AA display.
                                sr['normalized_witness_algebraic']=[{'minimal_polynomial':str(x.minpoly()),'isolating_interval':str(x.interval())}for x in v[:5]]
                    singulars.append(sr)
                    if sr['positive_feasible']:positive.append(sr)
        assignment_count+=1
        if progress:print('Completed native assignment',assignment_count,'of16;cases',len(records),'singular',len(singulars),'positive',len(positive),flush=True)
    assert len(records)==7680 and assignment_count==16
    return {'minimal_polynomial':'t^4-2*t^2-4','positive_root_interval':[1,2],
      'after_side_word':[1,3,4,4,3],'vertex_before_side_word':[3,1,3,4,4],
      'case_count':7680,'singular_count':len(singulars),'positive_count':len(positive),
      'records':records,'singular_cases':singulars,'positive_cases':positive}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--progress',action='store_true')
    ar=ap.parse_args();data=build(ar.progress)
    if ar.output:ar.output.write_text(json.dumps(data,indent=2)+'\n')
    if ar.check:assert json.loads(ar.check.read_text())==data
    print('COMPLETE:',data['case_count'],'cases;',data['singular_count'],'singular;',data['positive_count'],'positive closure/boundary solutions.')
