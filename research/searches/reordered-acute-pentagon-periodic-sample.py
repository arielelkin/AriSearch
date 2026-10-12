#!/usr/bin/env python3
"""Nonempty normalized two-parameter coordinate region for the carrier."""
import argparse,json,runpy
from pathlib import Path
from sage.all import AA,QQ
helpers=runpy.run_path('research/searches/acute-obtuse-long-edge-feature.py')
C,S=helpers['C'],helpers['S']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 t=AA(QQ(1)/10);d=AA(QQ(1)/5);a2=AA(1);a1=t;a3=d
 ad=[0,79,289,354,490]
 a4=-(a1*S(79)+a2*S(289)+a3*S(354))/S(490)
 a0=-sum(l*C(j) for l,j in zip([a1,a2,a3,a4],ad[1:]));al=[a0,a1,a2,a3,a4]
 bd=[0,71,159,425,440];b0=a2;b1=a0;b3=a3
 rx=-(b0+b1*C(71)+b3*C(425));ry=-(b1*S(71)+b3*S(425))
 det=C(159)*S(440)-S(159)*C(440)
 b2=(rx*S(440)-ry*C(440))/det;b4=(C(159)*ry-S(159)*rx)/det;bl=[b0,b1,b2,b3,b4]
 assert min(al+bl)>0
 pa=helpers['polygon'](al,ad);pb=helpers['polygon'](bl,bd)
 assert helpers['strict'](pa) and helpers['strict'](pb)
 assert al[0]==bl[1] and al[2]==bl[0] and al[3]==bl[3]
 out={'status':'PASS','scope':'Exact positive strictly convex coordinate sample and open two-parameter carrier cone; periodic plane realization supplied by the separately checked four-face flat torus.','field':'Q(zeta720), exp(2*pi*i/720), evaluated exactly in QQbar/AA; display decimals are not used for proof','parameters':'A2=1,A1=t>0,A3=d>0; sample t=1/10,d=1/5','trig_definition':'Cj=cos(j*pi/360), Sj=sin(j*pi/360)','A_direction_doubled_degrees':ad,'B_direction_doubled_degrees':bd,'formulas':['A4=-(t*S79+S289+d*S354)/S490','A0=-(t*C79+C289+d*C354+A4*C490)','B0=1,B1=A0,B3=d','rx=-(B0+B1*C71+B3*C425), ry=-(B1*S71+B3*S425)','D=C159*S440-S159*C440','B2=(rx*S440-ry*C440)/D','B4=(C159*ry-S159*rx)/D','p0=(0,0); p_(i+1)=p_i+side_i*(C(direction_i),S(direction_i))'],'cone':'All lengths positive and every strict supporting determinant positive. These hold at the sample and persist in an open neighbourhood of(t,d).','A_lengths_display':[str(x) for x in al],'B_lengths_display':[str(x) for x in bl],'A_vertices_display':[[str(x),str(y)] for x,y in pa],'B_vertices_display':[[str(x),str(y)] for x,y in pb],'exact_closure_convexity_aliases':True,'carrier_certificate':'research/certificates/reordered-acute-pentagon-four-face-carrier.json','periodic_domain':'2A+2B'}
 out['scope']='Exact positive strictly convex coordinate sample and open normalized two-parameter region, a slice of the homogeneous three-parameter length cone; periodic plane realization supplied by the separately checked four-face flat torus.'
 out['normalized_parameter_region']=out.pop('cone')
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','A_lengths':[str(x) for x in al],'B_lengths':[str(x) for x in bl],'periodic_domain':'2A+2B'}))
if __name__=='__main__':main()
