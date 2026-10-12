#!/usr/bin/env python3
"""Exact rationalized angle closure for the I/C and I/I local seam ledger.

All I/C and I/I closures are tested (only one has five length classes). Full column rank
excludes all nonzero length vectors away from exact roots of the gcd of maximal
minors. No sampled-angle inference or global extension claim is made.
"""
import json
import sys
from collections import Counter
from sage.all import AA, QuadraticField, PolynomialRing, matrix

K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()
R=PolynomialRing(K,'t');t=R.gen();F=R.fraction_field()
c=F(1-t*t)/F(1+t*t);s=F(2*t)/F(1+t*t)
base=[(K(1),K(0)),(K(1)/2,r/2),(-K(1)/2,r/2),(-K(1),K(0)),
      (-K(1)/2,-r/2),(K(1)/2,-r/2)]

def angle(j,m):
    a,b=F(1),F(0)
    for _ in range(abs(m)):
        a,b=a*c-b*s,a*s+b*c
    if m<0:b=-b
    x,y=base[j%6]
    return (x*a-y*b,x*b+y*a)

AD=[angle(j,m) for j,m in [(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,1)]]
BD={'C':[angle(j,m) for j,m in [(0,0),(1,2),(2,4),(3,2),(4,0),(5,-2)]],
    'I':[angle(j,m) for j,m in [(0,0),(1,2),(2,0),(3,2),(4,0),(5,-2)]]}

def polynomial_record(f):
    return [str(z) for z in f.list()]

LOW=AA(3).sqrt()-2;HIGH=2-AA(3).sqrt()

def domain_roots(f):
    if not f:return []
    return [z for z in f.roots(AA,multiplicities=False) if LOW<z<HIGH and z!=0]

def evaluated(M,z):
    return matrix(AA,[[v.numerator()(z)/v.denominator()(z) for v in rr] for rr in M.rows()])

def positive_kernel(Q):
    basis=Q.right_kernel().basis()
    assert len(basis)<=1, 'This narrow positivity checker requires nullity <=1.'
    if not basis:return False
    v=basis[0]
    return all(x>0 for x in v) or all(x<0 for x in v)

def positive_domain_check(M):
    rank=M.rank();basis=M.right_kernel().basis()
    if len(basis)>1:
        g=R(0)
        for minor in M.minors(rank):g=g.gcd(R(minor.numerator()))
        g=g.monic()
        if not domain_roots(g):
            for i in range(M.ncols()):
                for j in range(i+1,M.ncols()):
                    v=next((v for v in basis if v[i]),None)
                    if v is None:continue
                    ratio=v[j]/v[i]
                    if any(w[j]!=ratio*w[i] for w in basis):continue
                    boundaries=sorted(set(domain_roots(R(ratio.numerator()))+domain_roots(R(ratio.denominator()))+[AA(0)]))
                    if domain_roots(R(ratio.denominator())):continue
                    samples=[(a+b)/2 for a,b in zip([LOW]+boundaries,boundaries+[HIGH])]
                    if all(ratio.numerator()(z)/ratio.denominator()(z)<=0 for z in samples+boundaries):
                        return {'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
                                'generic_rank_drop_minor_gcd':polynomial_record(g),
                                'opposed_coordinate_relation':{'coordinates':[i,j],'ratio':str(ratio),
                                    'numerator':polynomial_record(R(ratio.numerator())),
                                    'denominator':polynomial_record(R(ratio.denominator())),
                                    'sign_partition_samples':[str(z) for z in samples]},
                                'verdict':'NO_STRICTLY_POSITIVE_LENGTH_VECTOR_AT_ANY_ADMISSIBLE_ANGLE'}
        return {'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
                'verdict':'UNRESOLVED_MULTI_DIMENSIONAL_KERNEL'}
    g=R(0)
    for minor in M.minors(rank):g=g.gcd(R(minor.numerator()))
    g=g.monic();points=set(domain_roots(g));data=[]
    if basis:
        for v in basis[0]:
            points.update(domain_roots(R(v.numerator())))
            points.update(domain_roots(R(v.denominator())))
    points=sorted(points|{AA(0)})
    for z in points:
        if z==0:continue
        Q=evaluated(M,z);ok=positive_kernel(Q)
        data.append({'type':'point','parameter':str(z),'minimal_polynomial':str(z.minpoly()),
                     'rank':int(Q.rank()),'kernel_basis':[[str(v) for v in rr] for rr in Q.right_kernel().basis()],
                     'positive_kernel_exists':ok})
    endpoints=[LOW]+points+[HIGH]
    for left,right in zip(endpoints,endpoints[1:]):
        z=(left+right)/2;Q=evaluated(M,z);ok=positive_kernel(Q)
        data.append({'type':'open_interval','left':str(left),'right':str(right),
                     'test_parameter':str(z),'positive_kernel_exists':ok})
    return {'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
            'generic_rank_drop_minor_gcd':polynomial_record(g),
            'partition_checks':data,'verdict':'POSITIVE_KERNEL_ON_DOMAIN_SUBSET' if any(q['positive_kernel_exists'] for q in data) else 'NO_STRICTLY_POSITIVE_LENGTH_VECTOR_AT_ANY_ADMISSIBLE_ANGLE'}

def main(source,out):
    ledger=json.load(open(source));rows=[]
    for pair in ledger['rows']:
        b=pair['B']
        if b not in BD:continue
        stats=Counter();records=[]
        for row in pair['distinct_closures']:
            eq=row['closure'];k=max(eq)+1
            M=matrix(F,4,k)
            for species,directions in enumerate([AD,BD[b]]):
                for j,(x,y) in enumerate(directions):
                    M[2*species,eq[6*species+j]]+=x
                    M[2*species+1,eq[6*species+j]]+=y
            rank=int(M.rank());g=R(0)
            if rank==k:
                for minor in M.minors(k):
                    num=R(minor.numerator())
                    g=g.gcd(num)
                g=g.monic()
                roots=domain_roots(g)
                verdict='NO_NONZERO_VECTOR_ALL_ADMISSIBLE_ANGLES' if not roots else 'FINITE_EXCEPTIONS'
            else:
                roots=[];verdict='GENERIC_KERNEL'
            rec={'closure':eq,'ring_count':row['count'],'number_of_length_classes':k,
                 'generic_rank':rank,'matrix':[[str(M[i,j]) for j in range(k)] for i in range(4)],
                 'maximal_minor_numerator_gcd':polynomial_record(g),
                 'admissible_exceptional_roots':[{'interval_value':str(z),'minimal_polynomial':str(z.minpoly())} for z in roots],
                 'verdict':verdict}
            if verdict!='NO_NONZERO_VECTOR_ALL_ADMISSIBLE_ANGLES':
                rec['positive_length_gate']=positive_domain_check(M)
            records.append(rec);stats[verdict]+=row['count']
        rows.append({'A':'I','B':b,'ring_weighted_stats':dict(stats),'closure_records':records})
        print('I',b,dict(stats),flush=True)
    result={'scope':'All I/C and I/I local seam closures; exact generic rank, isolated minor roots, and full-domain nullity-one positivity gates; no global adjacency enumeration',
            'parameter':'t=tan((p-120 degrees)/2); sqrt(3)-2<t<2-sqrt(3), t!=0',
            'A_side_direction_base_60_and_theta_multipliers':[(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,1)],
            'B_side_direction_base_60_and_theta_multipliers':{'C':[(0,0),(1,2),(2,4),(3,2),(4,0),(5,-2)],'I':[(0,0),(1,2),(2,0),(3,2),(4,0),(5,-2)]},
            'rows':rows}
    with open(out,'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
