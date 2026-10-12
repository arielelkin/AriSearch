#!/usr/bin/env python3
"""Exact A-only closure and ACTUAL length-partition filter for ALT angles.

Every class-length closure kernel contains the all-ones vector. A native
equality partition is feasible exactly when no pair of class coordinates
is forced equal in that kernel (small generic positive perturbation).
Rank-drop parameter roots are retained exactly; no native rings generated.
"""
import importlib.util
import itertools
import json
import sys
from collections import Counter
from sage.all import AA,matrix

spec=importlib.util.spec_from_file_location('rational_angles','research/searches/two-hexagon-interleaved-symbolic-closure.py')
angle=importlib.util.module_from_spec(spec);spec.loader.exec_module(angle)
AD=[angle.angle(j,m) for j,m in [(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1)]]

def forced_pairs(basis,k):
    return [[i,j] for i,j in itertools.combinations(range(k),2)
            if all(v[i]==v[j] for v in basis)]

def two_value_subset_audit():
    omega=[(1,0),(0,1),(-1,-1)]
    sixth_angles={(1,0):0,(1,1):60,(0,1):120,(-1,0):180,(-1,-1):240,(0,-1):300}
    def multiply(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
    rows=[]
    for mask in range(64):
        even=tuple(sum(omega[j//2][i] for j in (0,2,4) if mask>>j&1) for i in range(2))
        odd=tuple(sum(omega[(j-1)//2][i] for j in (1,3,5) if mask>>j&1) for i in range(2))
        rec={'subset_mask':mask,'even_root_sum':even,'odd_root_sum':odd,'proper_nonempty':mask not in (0,63)}
        if even==(0,0) and odd==(0,0):rec['verdict']='ZERO_FOR_EVERY_ALPHA'
        elif even==(0,0) or odd==(0,0):rec['verdict']='NO_ALPHA'
        else:
            assert odd[0]**2-odd[0]*odd[1]+odd[1]**2==1
            conjugate=(odd[0]-odd[1],-odd[1]);ratio=multiply((-even[0],-even[1]),conjugate)
            rec.update({'required_exp_i_alpha':ratio,'required_alpha_degrees':sixth_angles[ratio],
                        'verdict':'ONLY_SIXTH_ROOT_ALPHA'})
        rows.append(rec)
    assert [r['subset_mask'] for r in rows if r['proper_nonempty'] and r['verdict']=='ZERO_FOR_EVERY_ALPHA']==[21,42]
    return rows

def main(source,path):
    ledger=json.load(open(source));rows=[];stats=Counter();words=Counter()
    for row in ledger['rows']:
        eq=row['A_native_side_partition'];k=max(eq)+1;M=matrix(angle.F,2,k)
        for j,(x,y) in enumerate(AD):M[0,eq[j]]+=x;M[1,eq[j]]+=y
        assert all(sum(M[i,j] for j in range(k))==0 for i in range(2))
        rank=int(M.rank());basis=M.right_kernel().basis();forced=forced_pairs(basis,k)
        g=angle.R(0)
        for v in M.minors(rank):g=g.gcd(angle.R(v.numerator()))
        g=g.monic();exceptions=[]
        for z in angle.domain_roots(g):
            Q=angle.evaluated(M,z);qb=Q.right_kernel().basis();fp=forced_pairs(qb,k)
            exceptions.append({'parameter':str(z),'minimal_polynomial':str(z.minpoly()),
                               'rank':int(Q.rank()),'forced_equal_class_pairs':fp,
                               'actual_partition_feasible':not fp})
        verdict='GENERIC_ACTUAL_PARTITION' if not forced else 'FINITE_FEASIBLE_ANGLE_EXCEPTIONS' if any(r['actual_partition_feasible'] for r in exceptions) else 'NO_ADMISSIBLE_ACTUAL_PARTITION'
        rec={'A_native_side_partition':eq,'length_classes':k,'closure_matrix':[[str(v) for v in rr] for rr in M.rows()],
             'generic_rank':rank,'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
             'generic_forced_equal_class_pairs':forced,
             'generic_rank_minor_numerator_gcd':angle.polynomial_record(g),
             'admissible_rank_drop_angles':exceptions,'verdict':verdict,
             'ledger_native_B_word_count':row['deduplicated_B_native_word_count']}
        rows.append(rec);stats[verdict]+=1;words[verdict]+=row['deduplicated_B_native_word_count']
    result={'scope':'203 actual native A-side equality partitions for ALT angles, all admitted parameters via exact rank-drop isolation; no native-ring/global metric claim',
            'angle_direction_pairs':[(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1)],
            'parameter':'t=tan((120-p)/2),sqrt(3)-2<t<2-sqrt(3),t!=0',
            'partition_stats':dict(stats),'ledger_B_word_weighted_stats':dict(words),'rows':rows}
    result['two_value_subset_audit']=two_value_subset_audit()
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print(dict(stats),dict(words),flush=True)
    print('byk',{k:dict(Counter(r['verdict'] for r in rows if r['length_classes']==k)) for k in range(1,7)},flush=True)
    print('admissible rank drops',[(r['A_native_side_partition'],r['admissible_rank_drop_angles']) for r in rows if r['admissible_rank_drop_angles']],flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
