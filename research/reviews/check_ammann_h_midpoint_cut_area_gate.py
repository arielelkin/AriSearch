#!/usr/bin/env python3
"""Exact two-boundary-word cut geometry and retained-boundary area exclusion.
No producer import or solver; monohedral census is not needed for this gate.
"""
import json,argparse
from pathlib import Path
from sage.all import CyclotomicField,QQ,QQbar,AA,matrix,vector
F=CyclotomicField(10);w=F.gen();e=F.hom([QQbar.zeta(10)])
def decode(v):return sum(F(c)*w**i for i,c in enumerate(v))
def cross(a,b):return(a.conjugate()*b-a*b.conjugate())/(w-w.conjugate())
def area(P):return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2
D=json.loads(Path('research/certificates/ammann-h-midpoint-two-pentagon-cut.json').read_text())
H=[decode(v) for v in D['source']];P,Q=([decode(v) for v in row['vertices']] for row in D['tiles'])
J=QQ(1)/2+QQ(4)/5*w;jp=1+w**4*(J-1);jpp=w+w**6*(J-w);k=w**2+w**6*(J-1);l=1+w**7*(J-1-w);j2=1+w+w**2-J
assert H==[0,jp,1,J,w,jpp]
q=(H[0]+H[1])/2;r=(H[3]+H[4])/2
assert P==[q,H[1],H[2],H[3],r] and Q==[r,H[4],H[5],H[0],q]
for T in(H,P,Q):
 assert all(AA(e(cross(T[(i+1)%len(T)]-T[i],T[j]-T[i])))>0 for i in range(len(T)) for j in range(len(T)) if j not in(i,(i+1)%len(T)))
assert area(P)+area(Q)==area(H)==1
assert cross(H[1]-H[0],r-q)!=0 and cross(H[4]-H[3],q-r)!=0
phi=w+w.conjugate()
expected=[QQ(559)/800-QQ(9)/80*phi,QQ(241)/800+QQ(9)/80*phi]
assert [area(P),area(Q)]==expected
source=[[0,jp,1,l,k],[k,l,1+w**2,j2,w**2]]
expected_source=[QQ(71)/200+QQ(2)/5*phi,-QQ(71)/200+QQ(3)/5*phi]
assert [area(t) for t in source]==expected_source
M=matrix(QQ,[[QQ(559)/800,QQ(241)/800],[-QQ(9)/80,QQ(9)/80]])
solutions=[M.solve_right(vector(QQ,a)) for a in((QQ(71)/200,QQ(2)/5),(-QQ(71)/200,QQ(3)/5))]
assert list(solutions[0])==[-QQ(1289)/1800,QQ(5111)/1800]
assert list(solutions[1])==[-QQ(1177)/600,QQ(2023)/600]
assert all(s[0]<0 for s in solutions)
out={'domain':'one exactH6 midpoint chord; targetP/Q areas inQ(phi); sourceP1/P2 arbitrary finite nonnegativeinteger target dissections within retainedsourceboundaries',
     'target_area_basis_1_phi':[['559/800','-9/80'],['241/800','9/80']],
     'source_area_basis_1_phi':[['71/200','2/5'],['-71/200','3/5']],
     'coefficient_matrix_determinant':str(M.det()),
     'unique_rational_P_Q_counts':[[str(v) for v in s] for s in solutions],
     'nonnegative_integer_area_feasible':False,'two_genuine_convex_pentagons':True,'cut_endpoint_ray_degree':3,
     'scope':'excludes retainedsourceboundary source-by-source compiler, notcrossboundary reassembly or arbitraryplane tilings ofP/Q'}
parser=argparse.ArgumentParser();parser.add_argument('--check',type=Path);args=parser.parse_args()
if args.check:
 assert json.loads(args.check.read_text())==out
 print('PASS: exact two genuine pentagons and degree3 cut endpoints; both sourceP1/P2 require negativeP counts, excluding retained-boundary compiler.')
else:print(json.dumps(out,indent=2))
