"""Exact homogeneous-star resonance and binary-word monohedral necessary filters.
Read-only replay by default; --output explicitly retains the inventory.
Classification completeness is an imported theorem, not checked by this script.
"""
import argparse,json,itertools
from fractions import Fraction
from pathlib import Path

def inventory(output=None):
    multisets=[(m,3-m) for m in range(4)]
    lines=[]
    for arc,names in [('pp',['alpha','beta']),('qq',['chi','psi'])]:
        for m,n in multisets:
            lines.append({'arc':arc,'variables':names,'coefficients':[m,n],'rhs':360,'multiset':[m,n]})
    intersections=[]
    for x,y in itertools.combinations(multisets,2):
        m,n=x;u,v=y;det=m*v-n*u;assert det
        a=Fraction(360*(v-n),det);b=Fraction(360*(m-u),det)
        assert (a,b)==(120,120)
        intersections.append({'multisets':[x,y],'intersection':[str(a),str(b)]})
    paired=[]
    for m,n in multisets:
        coeff=2*(n-m);assert coeff
        paired.append({'multiset':[m,n],'angle_sum':'360'+('+' if coeff>0 else '')+str(coeff)+'*delta','delta_coefficient':coeff})
    words=[]
    for shift in range(6):
        for flip in [False,True]:
            w=['p' if ((shift+(-i if flip else i))%6)<3 else 'q' for i in range(6)]
            assert w[2]!=w[5]
            bad=[(i,i+1) for i in [0,2,4] if w[i]!=w[i+1]];assert bad
            words.append({'shift':shift,'reflected':flip,'B_native_word':w,'H1_H2_opposite_pair':[2,5],'H1_H2_unequal':True,'H3_unequal_adjacent_pairs':bad})
    caps={'none':Fraction(0),'pure3':Fraction(1,3),'mixed21':Fraction(1,2),'center120':Fraction(2,3)}
    bounds=[]
    for pp,qq in itertools.product(caps,repeat=2):
        cap=caps[pp]+caps[qq]
        bounds.append({'pp':pp,'qq':qq,'Yp_plus_Yq_upper_per_B':str(cap),'corner_count_lower_A_per_B':str(1-cap),'corner_count_alone_excludes_B_only':cap<1})
    out={'scope':'all fixed strict convex binary p!=q A-alternating/B-two-run shapes; angles0..180;delta0..30',
         'homogeneous_resonance_lines':lines,'same_arc_all_pairwise_intersections':intersections,
         'AAq_possible_angle_locus':['alpha=120','beta=120','(alpha,beta)=(120-2delta,120+2delta)','(alpha,beta)=(120+2delta,120-2delta)'],
         'paired_AAq_has_no_pp_homogeneous_star':paired,
         'all12_native_reindexings_B_monohedral_family_rejections':words,
         'classification_source':'https://arxiv.org/html/2508.01404v2 (Main Theorem;Introduction H1,H2,H3)',
         'frequency_identity':'N_B-N_A=Y_ppp+Y_qqq+O(R)',
         'frequency_upper_bound_strata':bounds,
         'checks':'8properlines;all6samearcintersectionsonly120120;4pairedAAqtriplecoefficientsnonzero;all12BwordreindexingsfailH1H2H3necessarylengthconditions;16exactrationalfrequencyboundstrata'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS8resonancelines,6samearcintersectionpairs,4pairedAAqcoefficients,12binarymonohedralwordrejections,16frequencystrata');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();inventory(args.output)
