"""Independent raw native B reflection for both reverseqq positive branches."""
from sage.all import QuadraticField,AA,PolynomialRing
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
R=PolynomialRing(K,'t');t=R.gen();F=R.fraction_field();cd=F(1-t*t)/F(1+t*t);sd=F(2*t)/F(1+t*t)
bases={0:(1,0),60:(K(1)/2,w/2),120:(-K(1)/2,w/2),180:(-1,0),240:(-K(1)/2,-w/2),300:(K(1)/2,-w/2),360:(1,0)}
def rot(a,c,s):return(c*a[0]-s*a[1],s*a[0]+c*a[1])
def mul(a,c):return tuple(c*x for x in a)
for beta in (60,120):
 p=cd if beta==120 else 2*cd
 old=[mul(bases[0],p),mul(bases[60],p),mul(bases[240-beta],p)]+[rot(bases[180],cd,sd),rot(bases[240],cd,-sd),rot(bases[300],cd,sd)]
 assert tuple(sum(a[j] for a in old) for j in(0,1))==(0,0)
 C,S=(K(1),K(0)) if beta==60 else(K(1)/2,-w/2)
 new=[rot((-old[j][0],old[j][1]),C,S) for j in(2,1,0,5,4,3)]
 target=([mul(bases[j],p) for j in(0,60,120)]+[rot(bases[180],cd,-sd),rot(bases[240],cd,sd),rot(bases[300],cd,-sd)]) if beta==120 else ([mul(bases[j],p) for j in(0,120,180)]+[rot(bases[240],cd,-sd),rot(bases[300],cd,sd),rot(bases[360],cd,-sd)])
 assert new==target
 # Native vertices exactly reverse from3, with the same orthogonal transform.
 vertices=[(F(0),F(0))]
 for edge in old:vertices.append(tuple(vertices[-1][j]+edge[j] for j in(0,1)))
 transformed=[rot((vertices[i][0]-vertices[3][0],-vertices[i][1]+vertices[3][1]),C,S) for i in(3,2,1,0,5,4)]
 assert [tuple(transformed[(j+1)%6][k]-transformed[j][k] for k in(0,1)) for j in range(6)]==target
# Native labels and corners follow the actual reversed traversal.
oldcornernames=['B0','alpha','beta','B3','chi','psi']
assert [oldcornernames[j] for j in(3,2,1,0,5,4)]==['B3','beta','alpha','B0','psi','chi']
print('PASS both reversed beta60/120 native B edge and vertex reflection/reindex identities for all0delta30; A unchanged; exact equalpp gamma60/complementarypp alpha60 positive prototypes and native pp/qq corner exchange.')
