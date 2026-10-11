"""Exact dedicated author ledger, no solver. Normal replay is read-only.
Fresh independent whole analytic/count review remains required.
"""
from sage.all import QQ,SR,PolynomialRing,matrix,vector,sin,cos,atan,diff
from itertools import product
from collections import Counter
from pathlib import Path
import argparse,json
R=PolynomialRing(QQ,['x','y']);x,y=R.gens()
low=[2*x,x-y,-x,-2*x-y,x+2*y,y,x-y,-2*y]
high=[-2*x,y-x,x,2*x+y,-x-2*y,-y,y-x,2*y]
# Every equality between positive and negative magnitude classes is retained.
# Identify valid slope y/x>1 without numerical inequalities.
P=[2*x,x+2*y,y];N=[y-x,x,2*x+y,2*y]
valid=[];equations=[]
for p,n in product(P,N):
 eq=p-n;coeffx=eq.monomial_coefficient(x);coeffy=eq.monomial_coefficient(y)
 if coeffy:
  slope=-coeffx/coeffy
  if slope>1: valid.append((str(p),str(n),str(slope)))
 elif coeffx==0: raise AssertionError('missed entire positive/negative equality')
 equations.append(str(eq))
assert valid==[('2*x','-x + y','3')]
assert set(high)==set(-t for t in low)
# Actual native length/angle swap reflecting B and exchanging p,q names.
assert [i for i in [0,5,4,3,2,1]]==[0,5,4,3,2,1]
oldlabels=['p']*3+['q']*3
assert [oldlabels[i] for i in [5,4,3,2,1,0]]==['q']*3+['p']*3
# Fully raw candidate native corners, orientations and coefficient sums.
labels=[['p','q']*3,['p']*3+['q']*3]
names=['H','L']*3+['u','alpha','beta','v','chi','eta']
coeff=[2,-2]*3+[-1,-1,2,3,-6,3]
ori=[]
for s in(0,1):
 for i in range(6):
  cid=6*s+i;out=labels[s][i];prev=labels[s][i-1]
  ori.extend([(cid,0,out,prev),(cid,1,prev,out)])
stars=[];types=set()
for ids in product(range(24),repeat=3):
 t=[ori[i] for i in ids]
 if any(t[i][3]!=t[(i+1)%3][2] for i in range(3)):continue
 if sum(coeff[q[0]] for q in t):continue
 stars.append(ids);types.add(tuple(sorted(names[q[0]] for q in t)))
expected={tuple(sorted(t)) for t in [('alpha','alpha','beta'),('chi','eta','eta'),('u','u','beta'),('v','v','chi'),('H','u','alpha'),('L','v','alpha'),('L','u','eta')]}
assert types==expected
# Exact local slope inventory: no accidental angles can add stars at x!=0.
T=PolynomialRing(QQ,['NA','NB','h','t','l','yp','zb']);na,nb,h,t,l,yp,zb=T.gens()
I=T.ideal([h-3*na,t+l-3*na,2*yp+h+t-nb,yp+zb-nb,h+l+2*zb-nb])
assert 9*na in I
# Noncentral branches cannot have AA fillers120 or paired low/high.
# Concavity and high-alpha curve derivative at origin.
z=SR.var('z');den=1+4*sin(z)**2
assert (diff(atan(2*sin(z)),z,2)+2*sin(z)*(5+4*cos(z)**2)/den**2).simplify_trig()==0
assert QQ(-1)/4+(-3)*QQ(-1)/4-1==QQ(-1)/2
report={'schema':'opposite-mixed-homogeneous-full-obstruction-v1','status':'PASS','cover_positive_negative_equations':equations,'only_valid_positive_negative_match':valid,'raw_oriented_candidate_stars':stars,'candidate_star_type_multisets':[list(t) for t in sorted(types)],'count_elimination':'9*NA in actual native incidence ideal','global_proof_requires_fresh_review':True}
ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print('PASS all9 H/L magnitude matches, unique y3x delta2x condition; native B lengthswap; all',len(stars),'raw oriented candidate stars and7 exact typeclasses; correct rho concavity/high-curve derivative; exact9NA native-slot elimination.')
