#!/usr/bin/env python3
"""Exact rational-angle feature, cheap monohedral and four-tile contact gates."""
import argparse,itertools,json,importlib.util
from pathlib import Path
from sage.all import AA,QQ,QQbar
sp=importlib.util.spec_from_file_location('clip_geometry',Path('research/reviews/check_hat_eight_kite_convex_clusters.py'))
g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
A=[130,281,295,150,224];B=[80,289,272,94,345] # Doubled degrees.
def stars(angles,target):
 return [list(c) for k in range(1,target//min(angles)+1) for c in itertools.combinations_with_replacement(angles,k) if sum(c)==target]
zeta=QQbar.zeta(720)
def C(j):return AA((zeta**j).real())
def S(j):return AA((zeta**j).imag())
def rotate(p,j):return (C(j)*p[0]-S(j)*p[1],S(j)*p[0]+C(j)*p[1])
def plus(p,q):return tuple(x+y for x,y in zip(p,q))
def minus(p,q):return tuple(x-y for x,y in zip(p,q))
def polygon(lengths,directions):
 p=(AA(0),AA(0));out=[]
 for l,j in zip(lengths,directions):out.append(p);p=plus(p,(l*C(j),l*S(j)))
 assert p==(0,0);return out
def strict(P):return all(g.cross(g.subtract(P[(i+1)%len(P)],P[i]),g.subtract(z,P[i]))>0 for i in range(len(P)) for j,z in enumerate(P) if j not in(i,(i+1)%len(P)))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 joint=A+B
 joint_stars={str(t):stars(joint,t) for t in(360,720)}
 assert joint_stars['360']==[[130,150,80]]
 assert [c for c in joint_stars['720'] if 289 in c]==[[281,150,289]]
 assert not stars(joint,720-2*A[1]) and not stars(joint,720-A[0]-A[1])
 pure={n:{str(t):stars(angles,t) for t in(360,720)} for n,angles in [('A',A),('B',B)]}
 assert pure['A']['360']==pure['B']['360']==[]
 assert pure['A']['720']==[[130,295,295]] and pure['B']['720']==[[80]*9]
 assert sum(A)==sum(B)==1080
 ledger=[[130,150,80],[295,295,130],[281,289,150],[224,224,272],[281,94,345]]
 assert sorted(sum(ledger,[]))==sorted(A+A+B)
 assert [sum(x) for x in ledger]==[360,720,720,720,720]
 # A edge3=edge4 supports the A75/A65 contact; A edge0 is strictly longest.
 ad=[0,79,144,354,490];a1=AA(QQ(1)/10);a2=AA(1)
 a3=(a1*S(79)+a2*S(144))/(-S(490)-S(354))
 a4=a3;a0=-sum(l*C(j) for l,j in zip([a1,a2,a3,a4],ad[1:]))
 al=[a0,a1,a2,a3,a4];assert min(al)>0 and a0>max(al[1:])
 bd=[0,71,159,425,440];b0=a0/2;b1=AA(QQ(1)/2);b4=a2
 rx=-(b0+b1*C(71)+b4*C(440));ry=-(b1*S(71)+b4*S(440))
 det=C(159)*S(425)-S(159)*C(425)
 b2=(rx*S(425)-ry*C(425))/det;b3=(C(159)*ry-S(159)*rx)/det
 bl=[b0,b1,b2,b3,b4];assert min(bl)>0 and max(bl)<a0
 pa=polygon(al,ad);pb=polygon(bl,bd);assert strict(pa) and strict(pb)
 q=(a0-b0,AA(0));assert 0<q[0]<a0
 host=[(x,-y) for x,y in pa];host.reverse() # Restore CCW for exact clipping.
 gamma=[plus(q,p) for p in pb]
 beta=[plus(q,rotate((t[0],-t[1]),584)) for p in pa for t in [minus(p,pa[3])]]
 beta.reverse()
 alpha=[plus(q,(-x,y)) for x,y in pa];alpha.reverse()
 patches={'host_A':host,'B40':gamma,'A75':beta,'A65':alpha}
 assert all(strict(p) for p in patches.values())
 assert all(g.area2(g.clip(p,t))==0 for p,t in itertools.combinations(patches.values(),2))
 # Direct unreversed native placements for exact endpoint seam assertions.
 beta_native=[plus(q,rotate((t[0],-t[1]),584)) for p in pa for t in [minus(p,pa[3])]]
 alpha_native=[plus(q,(-x,y)) for x,y in pa]
 assert gamma[0]==beta_native[3]==alpha_native[0]==q
 assert gamma[4]==beta_native[2] # B4=A2, ray40, far corner172.5+147.5.
 assert beta_native[4]==alpha_native[4] # A3=A4, ray115, far corner112+112.
 assert gamma[1]==(a0,0) # Host140.5/B144.5 coincide, residual75.
 assert alpha_native[1]==(-b0,0)
 assert 0<q[0]<a0 # Host65 lies strictly inside the reflected cap long side.
 out={'scope':'Angle-ledger and actual four-tile partial-contact module only. No full-plane existence, recurrence, recognition or aperiodicity claim.','angles_doubled_degrees':{'A':A,'B':B},'designated_A_edge':0,'same_native_pairing_completion_lists':{'reflection_at_A140.5':stars(joint,158),'halfturn_at_A65_plus_A140.5':stars(joint,309)},'pure_species_stars':pure,'formal_2A_1B_corner_ledger':ledger,'field':'Q(zeta_720), zeta_720=exp(2*pi*i/720); all computation in exact QQbar/AA; decimals below are display only','definition':'C(j)=cos(j*pi/360), S(j)=sin(j*pi/360)','A_directions_doubled_degrees':ad,'B_directions_doubled_degrees':bd,'A_length_formulas':['a0=-(a1*C79+a2*C144+a3*C354+a4*C490)','a1=1/10','a2=1','a3=(a1*S79+a2*S144)/(-S490-S354)','a4=a3'],'B_length_formulas':['b0=a0/2','b1=1/2','rx=-(b0+b1*C71+b4*C440); ry=-(b1*S71+b4*S440); D=C159*S425-S159*C425','b2=(rx*S425-ry*C425)/D','b3=(C159*ry-S159*rx)/D','b4=a2'],'native_coordinate_formula':'p0=(0,0); p_(i+1)=p_i+length_i*(C(direction_i),S(direction_i))','module_coordinate_formulas':{'q':'(a0-b0,0)','host_A':'reflect_x(A)','B40':'B+q','A75':'Rotate(292deg)(reflect_x(A-A_vertex3))+q','A65':'(-A_x,A_y)+q'},'A_lengths_display':[str(x) for x in al],'B_lengths_display':[str(x) for x in bl],'module_coordinates_display':{n:[[str(x),str(y)] for x,y in p] for n,p in patches.items()},'all_exact_positive_closure_convexity_and_disjointness_checks':True,'endpoint_remainders_degrees':{'host_A140.5_plus_B144.5':75,'B172.5_plus_A147.5':40,'two_A112':136,'host_A65_plus_flat':115},'next_gate':'Complete endpoint stars and test cap propagation/periodic extension. A finite module is insufficient.'}
 out.update({'status':'REJECTED_BY_HOSTED_T_BUDGET','scope':'Exact four-tile local module retained; constrained metric family globally untileable by hosted-T/native-corner budget.','all_joint_native_stars':joint_stars,'A0_strictly_longer_than_every_other_edge':True,'hosted_T_density_contradiction':['H>=a: every A0 hosts an interior T','a>=H+b: each T and each B144.5 consumes a distinct A75','b>=H: each T consumes B40','b=0 then a=0 contradicts positive tile density'],'next_gate':'No further plane search: hosted-T budget excludes every tiling of this constrained family.'})
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_module':'PASS','global_status':'UNTILEABLE_BY_HOSTED_T_BUDGET'}))
if __name__=='__main__':main()
