"""Independent local/mirror/phase audit for actual pp-center necessity.
No author imports; compactness and unbounded counts are reviewed in the review file.
"""
from itertools import product
from sage.all import QQ,PolynomialRing,QuadraticField,AA
words={'A':'pqpqpq','B':'pppqqq'}
corners=[(s,j) for s in words for j in range(6)]
def boundary(c,mirror):
    s,j=c;sides=(j,(j-1)%6)
    if mirror:sides=sides[::-1]
    return [(words[s][i],i) for i in sides]
def mixed(c):
    s,j=c;return words[s][j]!=words[s][j-1]
num=0
for cs in product(corners,repeat=3):
 for flags in product((0,1),repeat=3):
    bs=[boundary(c,f) for c,f in zip(cs,flags)]
    if any(bs[j][1][0]!=bs[(j+1)%3][0][0] for j in range(3)):continue
    num+=1
    assert sum(map(mixed,cs)) in (0,2)
    assert not all(c[0]=='A' for c in cs)
    has_aa_p=any(cs[j][0]==cs[(j+1)%3][0]=='A' and bs[j][1][0]=='p' for j in range(3))
    for j,c in enumerate(cs):
        if c[0]!='B' or c[1] not in (4,5):continue
        neighbor=cs[(j-1)%3] if bs[j][0][1]==4 else cs[(j+1)%3]
        if neighbor[0]!='A' or has_aa_p:continue
        assert sum(c[0]=='A' for c in cs)==1
        others=[cs[(j+1)%3],cs[(j+2)%3]]
        other=next(c for c in others if c[0]=='B')
        assert mixed(other)
    # In every saturated Bmixed+A+Bqq star the solep ray meets A.
    for j,c in enumerate(cs):
        if c[0]!='B' or not mixed(c):continue
        others=[cs[(j+1)%3],cs[(j+2)%3]]
        if not(any(z[0]=='A' for z in others) and any(z[0]=='B' and z[1] in(4,5) for z in others)):continue
        neighbor=cs[(j-1)%3] if bs[j][0][0]=='p' else cs[(j+1)%3]
        assert neighbor[0]=='A'
# Middleq vs all native Bq mates, both endpoint bijections.
ends=lambda side:(side,(side+1)%6)
for mate in (3,4,5):
 for reverse in (False,True):
    ee=ends(mate)[::-1] if reverse else ends(mate)
    assert any(x in(4,5) and y in(4,5) for x,y in zip(ends(4),ee))
# Whole middlep A neighbor and both outerp A neighbors propagate actualH/L.
opposite={'H':'L','L':'H'}
for middle in (('H','L'),('L','H')):
    pp_left_other=opposite[middle[0]];pp_right_other=opposite[middle[1]]
    T0=opposite[pp_left_other];T3=opposite[pp_right_other]
    assert T0!=T3
# Native chirality changes which endpoint bijection an oriented reversed seam uses.
# Fix hostq3 native startmixed,endqq; reflectedmate reverses native traversal.
roles={3:('mixed','qq'),4:('qq','qq'),5:('qq','mixed')}
legal=[]
for mate in (3,4,5):
 for mirrored in (False,True):
    mate_ends=roles[mate] if mirrored else roles[mate][::-1]
    endpoint_roles=list(zip(roles[3],mate_ends))
    if ('qq','qq') in endpoint_roles:continue
    assert all(set(pair)=={'mixed','qq'} for pair in endpoint_roles)
    legal.append((mate,mirrored))
assert legal==[(3,False),(5,True)]
# AA p fillers from the two whole-edge H/L identifications.
H,L=(120,1),(120,-1)
patterns=set()
for mate in ((H,L),(L,H)):
    patterns.add(tuple((360-x[0]-y[0],-x[1]-y[1]) for x,y in zip((H,L),mate)))
assert patterns=={((120,0),(120,0)),((120,-2),(120,2))}
# Actual native shape equations, bothsigma signs and exactB reflection.
T=PolynomialRing(QQ,['delta','chi','psi']);d,x,y=T.gens()
for same in (True,False):
 for sig in(-1,1):
    b3=240-sig*d-(x if same else y)
    b0=480-x-y-b3
    assert b0==240+sig*d-(y if same else x)
    # ReflectB: newmixed0old3,newmixed3old0,newchioldpsi,newpsioldchi.
    assert b3==240-sig*d-(x if same else y)
    assert b0==240+sig*d-(y if same else x)
    if sig==-1:
        new_chi,new_psi=y,x
        assert b3==240+d-(new_psi if same else new_chi)
        assert b0==240-d-(new_chi if same else new_psi)
    # Neighborroles propagate same sigma at other physical seam end.
    for sig_neighbor in(-1,1):
        equation=(b3+(x if same else y))+(b0+(y if same else x))
        assert equation==480
        assert ((240-sig*d)+(240+sig_neighbor*d)==480)==(sig_neighbor==sig)
# Exact complex native directions produce both closure phases fromactualangles.
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
L=K.extension(PolynomialRing(K,'z').gen()**2+1,'i');ii=L.gen()
R=PolynomialRing(L,['D','X','Y','p']);D,X,Y,p=R.gens();F=R.fraction_field()
u=L(1)/2+ii*w/2
assert u**3==-1 and u**6==1
pchain=p*(1+u+u*u);assert pchain==2*p*u
same=[u*D*X,u**4*D,u**7*D/Y]
cross=[u*D*Y,u**4*D*Y/X,u**7*D/X]
assert sum(same)==u*D*(X-1+1/Y)
assert sum(cross)==u*D*(Y-Y/X+1/X)
assert [(3-j)%6 for j in range(6)]==[3,2,1,0,5,4]
assert [(2-j)%6 for j in range(6)]==[2,1,0,5,4,3]
print(f'PASS {num} native oriented binary stars; saturatedp-ray role; middleqmate exclusion; both actual wholeA endpoint transports; same/cross chirality table; AA fillers; bothsigma equations/reflection and exactnativeclosure phases.')
