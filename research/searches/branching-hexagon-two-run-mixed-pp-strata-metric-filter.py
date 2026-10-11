"""Exact actual-phase filter of complete mixed21pp star-stratum balance records.
Read-only normally; explicit --output writes. SAT never implies a tiling.
"""
import argparse,json
from pathlib import Path
from sage.all import QQ,matrix,vector,PolynomialRing

def filter_strata(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-two-run-mixed-pp-strata-slot-balance.json'
    data=json.loads(source.read_text())
    assert data['generator_subset_count']==1562 and data['consistent_flat_count']==99
    assert data['counts']=={'unsat':71,'sat':22} and len(data['records'])==93
    rejected=data['linear_envelope_infeasible_flats'];assert len(rejected)==6
    for r in rejected:assert vector(QQ,(0,1,0,0)) in matrix(QQ,r['flat_basis']).row_space()
    for rec in data['records']:
        d,a,rho=map(QQ,rec['linear_envelope_sample']);assert 0<d<30 and 90<a<180 and 0<rho<90 and a-rho+d<120
        assert all(sum(x*y for x,y in zip(row,[1,d,a,rho]))==0 for row in matrix(QQ,rec['flat_basis']).rows())
    conditions={'alpha120':(120,0,-1,0),'alpha_plus_rho180':(180,0,-1,-1),'rho_equals_2alpha_minus180':(180,0,-2,1)}
    active=[]
    for i,p in enumerate(data['planes']):
        assert p[0]+120*p[2]+60*p[3]==0
        if p[1]==0:active.append(i)
    assert active==[4,5,12,16,17]
    records=[]
    for rec in data['records']:
        if rec['status']!='sat':continue
        space=matrix(QQ,rec['flat_basis']).row_space()
        forced=[name for name,row in conditions.items() if vector(QQ,row) in space];assert forced
        possible=rec['active_exception_equations']==active
        records.append({'stratum_index':rec['index'],'forced_actual_phase_conditions':forced,
                        'active_exception_equations':rec['active_exception_equations'],'actual_metric_possible':possible,
                        'metric_reduction':'alpha120rho60;extraoromittedactiveequationsfailfordelta>0' if not possible else 'knownperiodicfirstcurve'})
    assert [r['stratum_index'] for r in records if r['actual_metric_possible']]==[73]
    R=PolynomialRing(QQ,'u');u=R.gen();F=R.fraction_field();s=F(2*u)/(1+u*u);c=F(1-u*u)/(1+u*u)
    sumphase=s+2*s*c;doublephase=2*s*(2*c*c-1)-2*s*c
    assert sumphase*(1+u*u)**2==2*u*(3-u*u)
    assert doublephase*(1+u*u)**3==-8*u**3*(3-u*u)
    assert doublephase==2*s*(2*c+1)*(c-1)
    out={'source_strata':source.name,'all_six_linear_infeasible_flats_force_delta0':True,'all93_linear_samples_verified_exact':True,
         'all22_SAT_phase_filters':records,'metric_active_equations':active,'actual_surviving_stratum':73,
         'positive_geometry':'alpha120,beta120,rho60,p=cos(delta),0delta30',
         'exact_phase_polynomials':{'Palpha':'1+2i*sin(alpha)','exp_i_alpha_P_imag':'2u(3-u^2)/(1+u^2)^2',
                                   'exp_minus_2i_alpha_P_imag':'-8u^3(3-u^2)/(1+u^2)^3'},
         'half_angle_domain':'u=tan(alpha/2)>1 finite since90<alpha<180;strictlypositive1+u^2;Palpha realpart1 neverzero',
         'all_factor_roots':'u0 excluded;u^2=3 givesalpha120;cosalpha1 excluded;no poles and no vanishingPalpha',
         'scope':'complete actualmetricphasefilter after71strongduals;independentreviewrequiredbeforewhole-slicepromotion'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS22SATphasefilters exactQ[u]identities;onlyactualstratum73 alpha120rho60');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();filter_strata(args.output)
