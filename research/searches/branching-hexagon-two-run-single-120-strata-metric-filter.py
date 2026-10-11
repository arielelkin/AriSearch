"""Exact phase-filter for every retained SAT exceptional star stratum.
Read-only replay, explicit--output writes. No metric inference from primal SAT.
"""
import argparse,json
from pathlib import Path
from sage.all import QQ,matrix,vector,PolynomialRing

def filter_strata(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-two-run-single-120-strata-slot-balance.json'
    r=json.loads(source.read_text());assert r['generator_subset_count']==470 and r['consistent_flat_count']==52
    assert r['counts']=={'unsat':34,'sat':14} and len(r['records'])==48
    for rejected in r['linear_envelope_infeasible_flats']:
        assert vector(QQ,(0,1,0,0)) in matrix(QQ,rejected['flat_basis']).row_space()
    assert len(r['linear_envelope_infeasible_flats'])==4
    for rec in r['records']:
        d,b,phase=map(QQ,rec['linear_envelope_sample']);assert 0<d<30 and 0<b<180 and 0<phase<90 and phase+b>120+d
        assert all(sum(x*y for x,y in zip(row,[1,d,b,phase]))==0 for row in matrix(QQ,rec['flat_basis']).rows())
    conditions={'beta120':(120,0,-1,0),'rho60':(60,0,0,-1),'rho_plus_beta180':(180,0,-1,-1)}
    metricactive=[]
    for i,p in enumerate(r['planes']):
        assert p[0]+120*p[2]+60*p[3]==0
        if p[1]==0:metricactive.append(i)
    assert metricactive==[1,6,9]
    rows=[]
    for rec in r['records']:
        if rec['status']!='sat':continue
        A=matrix(QQ,rec['flat_basis']);space=A.row_space()
        forced=[name for name,row in conditions.items() if vector(QQ,row) in space];assert forced
        possible=rec['active_exception_equations']==metricactive
        rows.append({'stratum_index':rec['index'],'forced_phase_conditions':forced,'active_exception_equations':rec['active_exception_equations'],
                     'actual_metric_possible':possible,'metric_reduction':'beta120rho60;extraoromittedactiveequationsfailfordelta>0' if not possible else 'knownperiodicfirstcurve'})
    survivors=[x['stratum_index'] for x in rows if x['actual_metric_possible']];assert survivors==[33]
    T=PolynomialRing(QQ,names=('u','v'));u,v=T.gens();F=T.fraction_field();sa=F(2*u)/(1+u*u);ca=F(1-u*u)/(1+u*u);sb=F(2*v)/(1+v*v);cb=F(1-v*v)/(1+v*v)
    den=(1+u*u)*(1+v*v)
    same=(sa-sb)*den;cross=(sb-(sb*ca-cb*sa)-sa)*den
    assert same==2*(u-v)*(1-u*v);assert cross==4*u*v*(u-v)
    out={'source_strata':source.name,'four_linear_infeasible_flats_all_force_delta0':True,'all48_linear_samples_verified_exact':True,'all14_SAT_phase_filters':rows,'metric_active_equations':metricactive,'actual_surviving_stratum':33,
         'positive_geometry':'beta120,rho60,p=cos(delta),0delta30',
         'rational_half_angle_numerators':{'same':'2*(u-v)*(1-u*v)','cross':'4*u*v*(u-v)','denominator':'(1+u^2)*(1+v^2)'},
         'phase_domain':'u=tan(120/2)=sqrt3>0;v=tan(beta/2)>0finite;0beta180;no denominator poles',
         'rho60_branches':'v=u=>beta120 OR uv=1=>beta60;beta60 has m3=180+delta>180 and is inadmissible',
         'rho_plus_beta180_branches':'v=u=>beta120 only (u,v positive)',
         'scope':'complete SATmetricfilter after all34strongduals;freshreviewrequired beforewhole-slicepromotion'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS14SATphasefilters exacthalf-anglepolynomials;onlyactualstratum33 beta120rho60');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();filter_strata(args.output)
