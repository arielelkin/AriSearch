#!/usr/bin/env python3
"""Exact remaining ALT/ALT geometry under native colour-preserving D3².

Enumerates only the proved native metric word domain; never native SFT rings.
Canonical joint words retain shared length-class labels and full orbit weights.
"""
import importlib.util
import json
import sys
from collections import Counter
from itertools import combinations
from sage.all import matrix

spec=importlib.util.spec_from_file_location('joint_metric_angles','research/searches/two-hexagon-interleaved-symbolic-closure.py')
angle=importlib.util.module_from_spec(spec);spec.loader.exec_module(angle)
AD=[angle.angle(j,m) for j,m in [(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1)]]
BD=[angle.angle(j,m) for j,m in [(0,0),(1,2),(2,0),(3,2),(4,0),(5,2)]]
SIDE_MAPS=[tuple((r+j)%6 for j in range(6)) for r in (0,2,4)]+[
           tuple((r-j-1)%6 for j in range(6)) for r in (0,2,4)]

def words(mult):
    def walk(p,left):
        if len(p)==6:
            yield tuple(p);return
        for j,n in enumerate(left):
            if n:
                rest=list(left);rest[j]-=1
                yield from walk(p+[j],rest)
    yield from walk([],list(mult))

def canonical(a,b):
    variants=[]
    for amap in SIDE_MAPS:
        old=[a[j] for j in amap];names={};aa=[]
        for j in old:
            if j not in names:names[j]=len(names)
            aa.append(names[j])
        bb=[names[j] for j in b]
        for bmap in SIDE_MAPS:variants.append((tuple(aa),tuple(bb[j] for j in bmap)))
    return min(variants)

def force_pairs(basis,k):
    return [[i,j] for i,j in combinations(range(k),2) if all(v[i]==v[j] for v in basis)]

def main(ledger_path,strata_path,path):
    ledger=json.load(open(ledger_path));strata=json.load(open(strata_path))
    allowed={tuple(r['A_native_side_partition']) for r in strata['rows']
             if r['length_classes']>=4 and r['verdict']=='GENERIC_ACTUAL_PARTITION'}
    orbits=Counter();total=0
    for row in ledger['rows']:
        a=tuple(row['A_native_side_partition'])
        if a not in allowed:continue
        n=0
        for rec in row['distinct_B_multiplicity_ledgers']:
            for b in words(rec['B_native_multiplicities']):orbits[canonical(a,b)]+=1;n+=1
        assert n==row['deduplicated_B_native_word_count'];total+=n
    assert total==20970
    print('metric words',total,'D3xD3 orbits',len(orbits),'byk',dict(Counter(max(a)+1 for a,b in orbits)),flush=True)
    records=[];stats=Counter();weighted=Counter()
    for index,((a,b),weight) in enumerate(sorted(orbits.items())):
        k=max(a)+1;M=matrix(angle.F,4,k)
        for sp,(eq,directions) in enumerate([(a,AD),(b,BD)]):
            for j,(x,y) in enumerate(directions):M[2*sp,eq[j]]+=x;M[2*sp+1,eq[j]]+=y
        assert all(sum(M[i,j] for j in range(k))==0 for i in range(4))
        rank=int(M.rank())
        basis=[(angle.F(1),)*k] if rank==k-1 else list(M.right_kernel().basis())
        fp=force_pairs(basis,k);g=angle.R(0)
        for v in M.minors(rank):g=g.gcd(angle.R(v.numerator()))
        g=g.monic();roots=[]
        for z in angle.domain_roots(g):
            Q=angle.evaluated(M,z);qb=Q.right_kernel().basis();qfp=force_pairs(qb,k)
            roots.append({'parameter':str(z),'minimal_polynomial':str(z.minpoly()),'rank':int(Q.rank()),
                          'forced_equal_class_pairs':qfp,'actual_classes_possible':not qfp})
        verdict='GENERIC_ACTUAL_CLASS_KERNEL' if not fp else 'FINITE_FEASIBLE_ANGLE_EXCEPTIONS' if any(r['actual_classes_possible'] for r in roots) else 'NO_ADMISSIBLE_ACTUAL_METRIC'
        records.append({'id':index,'A_native_side_partition':a,'B_native_side_word':b,
                        'native_word_orbit_weight':weight,'matrix':[[str(v) for v in rr] for rr in M.rows()],
                        'generic_rank':rank,'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
                        'generic_forced_equal_class_pairs':fp,'rank_minor_numerator_gcd':angle.polynomial_record(g),
                        'admissible_rank_drop_angles':roots,'verdict':verdict})
        stats[verdict]+=1;weighted[verdict]+=weight
        if index%100==0:print('processed',index+1,'of',len(orbits),dict(stats),flush=True)
    result={'scope':'Complete necessary remaining 61 Apartitions/20970 Bwords; canonicalize joint metric geometry by independent native colour-preserving D3 actions; exact generic classmerge and rankdrop exceptions, no native rings',
            'source_metric_ledger':ledger_path,'source_A_strata':strata_path,'native_side_maps':SIDE_MAPS,
            'native_word_count':total,'joint_metric_orbit_count':len(orbits),'orbit_stats':dict(stats),
            'native_word_weighted_stats':dict(weighted),'rows':records}
    with open(path,'w') as f:json.dump(result,f,indent=2)
    print('FINAL',dict(stats),dict(weighted),flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2],sys.argv[3])
