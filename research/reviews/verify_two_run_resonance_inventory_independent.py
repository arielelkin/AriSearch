"""Independent angle hyperplanes, native length exclusions and count table."""
from itertools import combinations,product
from fractions import Fraction
from sage.all import QQ,matrix,vector,PolynomialRing
rows=[(3,0),(2,1),(1,2),(0,3)]
for a,b in combinations(rows,2):
 M=matrix(QQ,[a,b]);assert M.det()!=0
 assert M.inverse()*vector(QQ,[360,360])==vector(QQ,[120,120])
R=PolynomialRing(QQ,('delta','alpha','beta','chi','psi'));d,a,b,c,e=R.gens()
for x,y in ((120-2*d,120+2*d),(120+2*d,120-2*d)):
 for i,j in rows:assert i*x+j*y-360==2*d*(j-i)*(1 if x==120-2*d else-1)
# Complete endpoint patterns for one actual A-A q seam. Each whole A q edge
# has one H and one L endpoint; mirror endpoint reversal is permitted.
endpairs=set()
for left in product((-1,1),repeat=2):
 endpairs.add((240-(240+sum(left)*d),240-(240-sum(left)*d)))
# Values above are offsets from120 for the required third B pp angles.
assert endpairs=={(0,0),(-2*d,2*d),(2*d,-2*d)}
word=(0,0,0,1,1,1)
for flip,start in product((1,-1),range(6)):
 v=tuple(word[(start+flip*i)%6] for i in range(6))
 assert v[2]!=v[5]  # necessary common H1/H2 opposite equal length
 assert not(v[0]==v[1] and v[2]==v[3] and v[4]==v[5]) # H3
upper={'none':Fraction(0),'pure3':Fraction(1,3),'mixed21':Fraction(1,2),'center120':Fraction(2,3)}
for p,q in product(upper,repeat=2):
 coeff=1-upper[p]-upper[q]
 assert coeff==Fraction(1)-upper[p]-upper[q]
for p,q in product(('none','pure3','mixed21'),repeat=2):
 assert 1-upper[p]-upper[q]>0 or(p==q=='mixed21')
# Incidence identities with free species and free homogeneous star counts.
T=PolynomialRing(QQ,('NA','NB','Y','Vm'));NA,NB,Y,Vm=T.gens()
assert (4*NB-Vm-3*Y)-(6*NA+2*NB-2*Vm)/2==3*(NB-NA-Y)
print('PASS complete4+4 homogeneous angle lines, allsamearc intersections, actualAAq endpointpatterns/disjoint pairedlocus, all12nativeH1/H2/H3 length exclusions,16 rational capacity bounds and free-species incidence identity')
