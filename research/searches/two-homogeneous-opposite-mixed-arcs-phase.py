"""Exact author ledger; no solver or author imports. Read-only unless --output requested.
Global boundary/compactness and analytic interval proofs require fresh review.
"""
from sage.all import QQ, SR, PolynomialRing, matrix, vector, sin, cos, atan, diff
from itertools import combinations, product
import argparse,json
from pathlib import Path
R=PolynomialRing(QQ,['a','e','u','d','x','y','z']);a,e,u,d,x,y,z=R.gens()
v=a+e-u; beta=360-2*a;chi=360-2*e
res={name:[2*u+g-360,u+v+g-360,2*v+g-360] for name,g in [('alpha',a),('beta',beta),('chi',chi),('eta',e)]}
assert res['beta']==[2*(u-a),e-a,2*(e-u)]
assert res['chi']==[2*(u-e),a-e,2*(a-u)]
forms={name:[360-u-g,360-v-g] for name,g in [('alpha',a),('beta',beta),('chi',chi),('eta',e)]}
assert forms['beta']==[2*a-u,a-e+u]
assert forms['chi']==[2*e-u,e-a+u]
assert [forms['beta'][i]+forms['chi'][j] for i,j in product(range(2),repeat=2)]==[2*v,a+e,a+e,2*u]
expected={
 'u': {'alpha':([x,2*x-y,3*x-2*y],[-x,-2*x+y]),'beta':([-2*x,-x-y,-2*y],[2*x,x+y]),'chi':([2*y,x+y,2*x],[-2*y,-x-y]),'eta':([-y,x-2*y,2*x-3*y],[y,-x+2*y])},
 'v': {'alpha':([3*x-2*y,2*x-y,x],[-2*x+y,-x]),'beta':([-2*y,-x-y,-2*x],[x+y,2*x]),'chi':([2*x,x+y,2*y],[-x-y,-2*y]),'eta':([2*x-3*y,x-2*y,-y],[-x+2*y,y])},
 'sum': {'alpha':([x-2*z,x,x+2*z],[-x+z,-x-z]),'beta':([-2*x-2*z,-2*x,-2*x+2*z],[2*x+z,2*x-z]),'chi':([2*x-2*z,2*x,2*x+2*z],[-2*x+z,-2*x-z]),'eta':([-x-2*z,-x,-x+2*z],[x+z,x-z])}}
for locus,sub in [('u',{a:120+x,e:120-y,u:120}),('v',{a:120+x,e:120-y,u:120+x-y}),('sum',{a:120+x,e:120-x,u:120-z})]:
 for name in res:
  assert ([q.subs(sub) for q in res[name]],[q.subs(sub)-120 for q in forms[name]])==expected[locus][name]
# Pure trivalent hom multisets: six pairwise plane intersections all centered.
planes=[((1,0),120),((2,1),360),((1,2),360),((0,1),120)]
for (co,rhs),(co2,rhs2) in combinations(planes,2):
 assert matrix(QQ,[co,co2]).solve_right(vector(QQ,[rhs,rhs2]))==vector(QQ,[120,120])
# Binary ray-cycle parity; all reflected homogeneous/mixed corner classes retained.
for rays in product('pq',repeat=3):
 assert sum(rays[j]!=rays[(j+1)%3] for j in range(3)) in (0,2)
# Analytic derivatives, radians.
w=SR.var('w'); den=1+4*sin(w)**2
assert (diff(atan(2*sin(w)),w)-2*cos(w)/den).simplify_trig()==0
assert (diff(atan(2*sin(w)),w,2)+2*sin(w)*(5+4*cos(w)**2)/den**2).simplify_trig()==0
# Complete half-angle curve: denominator identity and numerator factors.
T=PolynomialRing(QQ,'t');t=T.gen();D=1+8*t*t-t**4;N=t*(3*t*t-1);F=t**4+3*t**3-8*t*t-t-1
sa=2*t/(1+t*t);ca=(1-t*t)/(1+t*t)
assert sa*(1-2*ca)/(2*ca+4*sa*sa)==N/D
assert D-N==-F
assert D*D+4*N*N==(t*t+1)**2*(t**4+18*t*t+1)
assert F(1)==-6 and F(2)==5 and F.derivative()(1)==-4
assert F.derivative(2)==12*t*t+18*t-16
# Count elimination at y=2x: equations [2Yp+Yq=NB,3Yp+2Yq=2NB].
assert matrix(QQ,[[2,1],[3,2]]).solve_right(vector(QQ,[1,2]))==vector(QQ,[0,1])
report={'schema':'exact-opposite-mixed-homogeneous-ledger-v1','status':'PASS','checks':['rho first and second derivatives','all12 B-only nonpure residuals','all8 native A-cover forms','all3 locus tables','all6 homogeneous plane intersections','all8 binary ray cycles','complete half-angle rational identity and denominator','exact y=2x count elimination'],'tables':{k:{name:[[str(t) for t in rows[0]],[str(t) for t in rows[1]]] for name,rows in value.items()} for k,value in expected.items()}}
ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print('PASS exact opposite mixed-homogeneous phase derivatives, exceptional-curve identities, exhaustive local angle tables, binary parity, homogeneous capacities and count eliminations. Global analytic/count manuscript still needs fresh review.')
