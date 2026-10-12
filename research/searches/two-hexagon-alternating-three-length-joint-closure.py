#!/usr/bin/env python3
"""The 270 balanced three-length ALT/ALT words: joint exact closure only."""
import importlib.util
import itertools
import json
import sys
from collections import Counter
from sage.all import matrix

spec=importlib.util.spec_from_file_location('joint_angles','research/searches/two-hexagon-interleaved-symbolic-closure.py')
angle=importlib.util.module_from_spec(spec);spec.loader.exec_module(angle)
AD=[angle.angle(j,m) for j,m in [(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1)]]
BD=[angle.angle(j,m) for j,m in [(0,0),(1,2),(2,0),(3,2),(4,0),(5,2)]]

def forced_pairs(basis):
    return [[i,j] for i,j in itertools.combinations(range(3),2) if all(v[i]==v[j] for v in basis)]

def main(source,path):
    strata=json.load(open(source));partitions=[r['A_native_side_partition'] for r in strata['rows']
                                             if r['length_classes']==3 and r['verdict']=='GENERIC_ACTUAL_PARTITION']
    words=[w for w in itertools.product(range(3),repeat=6) if Counter(w)=={0:2,1:2,2:2}]
    assert len(partitions)==3 and len(words)==90
    rows=[];stats=Counter()
    for a in partitions:
        for b in words:
            M=matrix(angle.F,4,3)
            for sp,(eq,directions) in enumerate([(a,AD),(b,BD)]):
                for j,(x,y) in enumerate(directions):M[2*sp,eq[j]]+=x;M[2*sp+1,eq[j]]+=y
            assert all(sum(M[i,j] for j in range(3))==0 for i in range(4))
            rank=int(M.rank());basis=M.right_kernel().basis();fp=forced_pairs(basis)
            g=angle.R(0)
            for v in M.minors(rank):g=g.gcd(angle.R(v.numerator()))
            g=g.monic();roots=[]
            for z in angle.domain_roots(g):
                Q=angle.evaluated(M,z);qb=Q.right_kernel().basis();qfp=forced_pairs(qb)
                roots.append({'parameter':str(z),'minimal_polynomial':str(z.minpoly()),'rank':int(Q.rank()),
                              'forced_equal_class_pairs':qfp,'all_three_actual_values_possible':not qfp})
            verdict='NO_ACTUAL_THREE_LENGTH_METRIC' if fp and not any(r['all_three_actual_values_possible'] for r in roots) else 'RESIDUE'
            rec={'A_native_side_partition':a,'B_native_side_word':b,'matrix':[[str(v) for v in rr] for rr in M.rows()],
                 'generic_rank':rank,'generic_kernel_basis':[[str(v) for v in rr] for rr in basis],
                 'generic_forced_equal_class_pairs':fp,'rank_minor_numerator_gcd':angle.polynomial_record(g),
                 'admissible_rank_drop_angles':roots,'verdict':verdict}
            rows.append(rec);stats[verdict]+=1
    out={'scope':'Three actual A side lengths in the complete ALT/ALT metric domain: three A mirror partitions x90 B words, shared-length polygon closure only',
         'parameter':'t=tan((120-p)/2), sqrt(3)-2<t<2-sqrt(3),t!=0',
         'A_direction_pairs':[(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1)],
         'B_direction_pairs':[(0,0),(1,2),(2,0),(3,2),(4,0),(5,2)],
         'stats':dict(stats),'rows':rows}
    with open(path,'w') as f:json.dump(out,f,indent=2)
    print(len(rows),dict(stats),flush=True)
    print('exceptions',[(r['A_native_side_partition'],r['B_native_side_word'],r['admissible_rank_drop_angles']) for r in rows if r['admissible_rank_drop_angles']],flush=True)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
