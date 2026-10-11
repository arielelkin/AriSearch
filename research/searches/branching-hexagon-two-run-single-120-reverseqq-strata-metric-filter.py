"""Complete actual-phase filter of single120 reverseqq exceptional strata.
Read-only normally; explicit --output writes. Actual positive branches use reviewed cones.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction
from sage.all import QQ,matrix,vector,PolynomialRing

def filter_strata(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-two-run-single-120-reverseqq-strata-slot-balance.json'
    data=json.loads(source.read_text());assert data['generator_subset_count']==470 and data['consistent_flat_count']==52
    assert data['counts']=={'unsat':34,'sat':14} and len(data['records'])==48
    for rec in data['linear_envelope_infeasible_flats']:assert vector(QQ,(0,1,0,0)) in matrix(QQ,rec['flat_basis']).row_space()
    assert len(data['linear_envelope_infeasible_flats'])==4
    for rec in data['records']:
        d,b,rho=map(QQ,rec['linear_envelope_sample']);assert 0<d<30 and 0<b<180 and 0<rho<90 and rho+b>120-d
        assert all(sum(x*y for x,y in zip(row,[1,d,b,rho]))==0 for row in matrix(QQ,rec['flat_basis']).rows())
    conditions={'beta120':(120,0,-1,0),'rho60':(60,0,0,-1),'beta_plus_rho180':(180,0,-1,-1)}
    def active(b,d=None):
        ans=[]
        for i,row in enumerate(data['planes']):
            constant=row[0]+b*row[2]+60*row[3]
            if d is None:
                if constant==0 and row[1]==0:ans.append(i)
            elif constant+row[1]*d==0:ans.append(i)
        return ans
    roots=set()
    for row in data['planes']:
        if row[1]:
            root=-Fraction(row[0]+60*row[2]+60*row[3],row[1])
            if 0<root<30:roots.add(root)
    assert roots=={Fraction(15)}
    patterns=[{'beta':120,'delta_domain':'0<delta<30','active_equations':active(120),'positive_transfer':'global reflection of periodic firstcurve'},
              {'beta':60,'delta_domain':'0<delta<30,delta!=15','active_equations':active(60),'positive_transfer':'reflectB to reviewed complementaryppcone atalpha60'},
              {'beta':60,'delta_domain':'delta15','active_equations':active(60,15),'positive_transfer':'same complementaryppcone'}]
    assert [p['active_equations'] for p in patterns]==[[3,6,11],[3],[3,8]]
    records=[]
    for rec in data['records']:
        if rec['status']!='sat':continue
        space=matrix(QQ,rec['flat_basis']).row_space()
        forced=[n for n,p in conditions.items() if vector(QQ,p) in space];assert forced
        matching=[p for p in patterns if p['active_equations']==rec['active_exception_equations']]
        records.append({'stratum_index':rec['index'],'forced_phase_conditions':forced,'active_exception_equations':rec['active_exception_equations'],
                        'actual_metric_possible':bool(matching),'actual_branches':matching})
    assert [r['stratum_index'] for r in records if r['actual_metric_possible']]==[38,39,43]
    T=PolynomialRing(QQ,names=('u','v'));u,v=T.gens();F=T.fraction_field();sa=F(2*u)/(1+u*u);ca=F(1-u*u)/(1+u*u);sb=F(2*v)/(1+v*v);cb=F(1-v*v)/(1+v*v)
    den=(1+u*u)*(1+v*v);assert (sa-sb)*den==2*(u-v)*(1-u*v)
    assert (sb-(sb*ca-cb*sa)-sa)*den==4*u*v*(u-v)
    out={'source_strata':source.name,'four_linear_infeasible_flats_force_delta0':True,'all48_envelope_samples_verified_exact':True,
         'all14_SAT_phase_filters':records,'full_actual_branch_active_sets':patterns,'actual_surviving_strata':[38,39,43],
         'rational_phase_numerators':{'same':'2(u-v)(1-uv)','cross':'4uv(u-v)','denominator':'(1+u^2)(1+v^2)'},
         'phase_domain':'u=sqrt3;v=tan(beta/2)>0finite;0beta180;Pbeta has positive real and imaginaryparts and neverzero',
         'rho60_branches':'beta120 OR beta60;bothstrictgeometry;beta60 givesm3=180-delta, p2cosdelta',
         'beta_plus_rho180_branches':'onlybeta120',
         'scope':'complete reverseqq actualphasefilter, threeactive strata on two reviewedpositivecurves;independentreviewrequired'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS14SATreverseqqphasefilters;actualstrata38/39/43;positivebranchesbeta60or120');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();filter_strata(args.output)
