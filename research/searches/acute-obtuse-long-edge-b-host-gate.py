#!/usr/bin/env python3
"""Controlled h>A0 continuation: actual B-host cap, then immediate endpoint kill."""
import argparse,itertools,json,runpy
from pathlib import Path
from sage.all import AA,QQ
d=runpy.run_path('research/searches/acute-obtuse-long-edge-feature.py')
C,S,g=d['C'],d['S'],d['g'];A,B=d['A'],d['B'];joint=A+B
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 ad=[0,79,144,354,490];a1=AA(QQ(1)/10);a2=AA(1)
 a3=(a1*S(79)+a2*S(144))/(-S(490)-S(354));a4=a3
 a0=-sum(l*C(j) for l,j in zip([a1,a2,a3,a4],ad[1:]));al=[a0,a1,a2,a3,a4]
 bd=[0,71,159,425,440];b0=3*a0/2;b1=AA(QQ(1)/2);b4=a2
 rx=-(b0+b1*C(71)+b4*C(440));ry=-(b1*S(71)+b4*S(440));det=C(159)*S(425)-S(159)*C(425)
 b2=(rx*S(425)-ry*C(425))/det;b3=(C(159)*ry-S(159)*rx)/det;bl=[b0,b1,b2,b3,b4]
 assert min(al+bl)>0 and b0>max(al) and b3>max(al+[b0,b1,b2,b4])
 assert min(b2,b4)>a1
 pa=d['polygon'](al,ad);pb=d['polygon'](bl,bd);assert d['strict'](pa) and d['strict'](pb)
 q=(b0-a0,AA(0));assert 0<q[0]<b0
 host=[(x,-y) for x,y in pb];host.reverse()
 alpha=[d['plus'](q,p) for p in pa]
 beta=[d['plus'](q,d['rotate'](d['minus'](p,pa[3]),496)) for p in pa]
 gamma_native=[d['plus'](q,(-x,y)) for x,y in pb];gamma=gamma_native[::-1]
 patches={'host_B':host,'A65':alpha,'A75':beta,'B40':gamma}
 assert all(d['strict'](p) for p in patches.values())
 assert all(g.area2(g.clip(p,t))==0 for p,t in itertools.combinations(patches.values(),2))
 assert alpha[0]==beta[3]==gamma_native[0]==q
 assert alpha[4]==beta[4] and beta[2]==gamma_native[4]
 assert alpha[1]==(b0,0) and gamma_native[1]==(-a0,0)
 flat=d['stars'](joint,360);full=d['stars'](joint,720)
 assert flat==[[130,150,80]]
 assert [s for s in full if 289 in s]==[[281,150,289]]
 assert d['stars'](joint,720-2*345)==[]
 assert d['stars'](joint,720-345-94)==[[281]]
 assert d['stars'](joint,360-295)==[] # A147.5 cannot end in a straight sector.
 assert [s for s in full if 224 in s]==[[224,224,272],[130,224,272,94]]
 out={'scope':'Controlled h=3A0/2 branch, exact B-host four-tile module; rejected by two hosted contacts per B after endpoint exclusion of full B3 joins. No plane existence claim.','status':'REJECTED_BY_TWO_B_HOSTS','angles_doubled_degrees':{'A':A,'B':B},'exact_parameters':'A1=1/10,A2=1,A3=A4; B0=3A0/2,B1=1/2,B4=A2; remaining lengths use the original exact closure formulas','exact_coordinate_formulas':{'q':'(B0-A0,0)','host_B':'reflect_x(B)','A65':'A+q','A75':'Rotate248deg(A-A_vertex3)+q','B40':'(-Bx,By)+q'},'A_lengths_display':[str(x) for x in al],'B_lengths_display':[str(x) for x in bl],'module_coordinates_display':{n:[[str(x),str(y)] for x,y in p] for n,p in patches.items()},'exact_checks':{'B0_longer_than_all_A_edges':True,'B3_strictly_longest':True,'B2_and_B4_longer_than_A1':True,'strict_convex_closure_disjoint_module':True},'B3_full_join_exclusion':{'reflection_completion':[],'halfturn_completion':[[281]],'geometric_obstruction':'Forced A140.5 has incident A1 ending at A147.5. That side faces B2 or B4, both longer; A147.5 would lie inside a B side and cannot be completed with a flat180 incidence.'},'host_budget':['Every B0 hosts T: at B144.5 only A140.5/A75 neighbours occur; their incident sides are shorter than B0','Every B3 hosts T: it is strictly longest and both full B3 joins are excluded','H>=2b, b>=H since every flat T consumes the unique B40','b=0; every A112 full star consumes B136 and at most2A112, giving a<=2b=0','Finitewindow O(R) errors contradict area Omega(R^2)']}
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_B_host_module':'PASS','B_lengths':[str(x) for x in bl],'global_status':'UNTILEABLE_BY_TWO_B_HOSTS'}))
if __name__=='__main__':main()
