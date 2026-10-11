"""Independent finite native-contact audit. No author imports or solver calls.
Run: conda run --no-capture-output -n arisearch python research/reviews/verify_branching_hexagon_one_noncentral_homogeneous_arc_independent.py
The unbounded boundary proof is reviewed separately; this checks its finite local ledger.
"""
from itertools import product, combinations
from sage.all import QQ, QuadraticField, AA, PolynomialRing, matrix, vector
words = {"A": tuple("pqpqpq"), "B": tuple("pppqqq")}
corners = [(species,j) for species in words for j in range(6)]
def boundaries(corner, mirror):
    species,j = corner
    sides = (j,(j-1)%6)
    if mirror: sides=sides[::-1]
    return tuple((words[species][s],s) for s in sides)
def compatible(cs,flags):
    bs=[boundaries(c,f) for c,f in zip(cs,flags)]
    return all(bs[j][1][0]==bs[(j+1)%3][0][0] for j in range(3))
def mixed(c):
    species,j=c
    return words[species][j]!=words[species][(j-1)%6]
def aa_p(cs,flags):
    bs=[boundaries(c,f) for c,f in zip(cs,flags)]
    return any(cs[j][0]==cs[(j+1)%3][0]=='A' and bs[j][1][0]=='p' for j in range(3))
star_count=0
for cs in product(corners,repeat=3):
    for flags in product((0,1),repeat=3):
        if not compatible(cs,flags): continue
        star_count+=1
        n=sum(map(mixed,cs))
        assert n in (0,2)
        assert not all(s=='A' for s,j in cs)
        if not aa_p(cs,flags):
            for k,c in enumerate(cs):
                if c[0]!='B' or c[1] not in (4,5): continue
                # Native qq slot has an A neighbor across native middle-q side4.
                bs=[boundaries(z,f) for z,f in zip(cs,flags)]
                mate_prev=cs[(k-1)%3]
                mate_next=cs[(k+1)%3]
                middle_mate=mate_prev if bs[k][0][1]==4 else mate_next
                if middle_mate[0]!='A': continue
                others=[cs[(k+1)%3],cs[(k+2)%3]]
                assert sum(z[0]=='A' for z in others)==1
                other_b=next(z for z in others if z[0]=='B')
                assert mixed(other_b)
        # If neither species A-A seam is allowed, every A is paired with one
        # other mixed B corner and one homogeneous B corner.
        if sum(s=='A' for s,j in cs)==1:
            others=[c for c in cs if c[0]=='B']
            assert sum(map(mixed,others))==1
# Both end bijections of a whole A side, each with native H/L endpoints.
H,L=(QQ(120),QQ(1)),(QQ(120),QQ(-1))
fillers=set()
for mate in ((H,L),(L,H)):
    fillers.add(tuple((360-x[0]-y[0],-x[1]-y[1]) for x,y in zip((H,L),mate)))
assert fillers=={((120,0),(120,0)),((120,-2),(120,2))}
# Four homogeneous pp planes: intersections are exactly alpha=beta=120.
planes=[((1,0),120),((2,1),360),((1,2),360),((0,1),120)]
for (r,c),(s,d) in combinations(planes,2):
    assert matrix(QQ,[r,s]).solve_right(vector(QQ,[c,d]))==vector(QQ,[120,120])
# Pure alpha star: each native corner1 exposes side0 and1. All eight reflection
# assignments are checked independently. Excluding1/1 leaves only0/1 seams.
allowed=[]
cs=(('B',1),)*3
for flags in product((0,1),repeat=3):
    bs=[boundaries(c,f) for c,f in zip(cs,flags)]
    seam_pairs=[(bs[k][1][1],bs[(k+1)%3][0][1]) for k in range(3)]
    if (1,1) in seam_pairs: continue
    assert all(set(z)=={0,1} for z in seam_pairs)
    assert len(set(flags))==1
    allowed.append(flags)
assert set(allowed)=={(0,0,0),(1,1,1)}
# Native whole-seam ends. A side1/1 B mate always has an endpoint containing
# beta; a third pp slot cannot complete a pure3alpha star if beta!=120.
endpoints=lambda side:(side,(side+1)%6)
for j in (0,1):
    mate=endpoints(1)[::1 if j==0 else -1]
    assert any(2 in pair for pair in zip(endpoints(1),mate))
# If a0/1 seam is charged at alpha/alpha, its far end is mixed0/beta2.
for a,b in ((0,1),(1,0)):
    for reverse in (False,True):
        ends=list(zip(endpoints(a),endpoints(b)[::-1] if reverse else endpoints(b)))
        if (1,1) in ends:
            far=next(z for z in ends if z!=(1,1))
            assert set(far)=={0,2}
# Every B q side has >=oneqq endpoint; middle4 has two. Both bijections give
# >=oneqq/qq endpoint, which requires a forbidden homogeneousqq triple.
for mate_side in (3,4,5):
    for reverse in (False,True):
        es=endpoints(mate_side)[::-1] if reverse else endpoints(mate_side)
        assert any(x in (4,5) and y in (4,5) for x,y in zip(endpoints(4),es))
assert all(sum(4 in ((j-1)%6,j) for j in (corner,))==1 for corner in (4,5))
# Exact algebra behind the two count contradictions. Variables denote the
# O(R)-free leading parts only; the review accounts for bounded discrepancies.
R=PolynomialRing(QQ,['NA','NB','Vm','Y','E']);na,nb,vm,y,e=R.gens()
I=R.ideal([2*vm-6*na-2*nb,4*nb-vm-3*y])
assert na-nb+y in I
J=R.ideal([na-nb+y,3*na-3*nb+2*e])
assert 3*y-2*e in J
# Fresh exact rational half-angle derivation of common-scale A length swap.
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()
T=PolynomialRing(K,['t','p']);t,p=T.gens();F=T.fraction_field()
c,s=F(1-t*t)/(1+t*t),F(2*t)/(1+t*t)
def rot(z,C,S):return (C*z[0]-S*z[1],S*z[0]+C*z[1])
bases=[(1,0),(K(1)/2,w/2),(-K(1)/2,w/2),(-1,0),(-K(1)/2,-w/2),(K(1)/2,-w/2)]
def raw_edges(P):
    return [tuple((P if j%2==0 else 1)*v for v in (rot(z,c,s) if j%2 else z)) for j,z in enumerate(bases)]
old=raw_edges(p)
C,S=-c/2-w*s/2,w*c/2-s/2
new=[tuple(-v/p for v in rot((old[(-j-1)%6][0],-old[(-j-1)%6][1]),C,S)) for j in range(6)]
assert new==raw_edges(F(1)/p)
Bword=words['B']
assert tuple({'p':'q','q':'p'}[Bword[(j+3)%6]] for j in range(6))==Bword
# Reflection around the p block reverses native slots and exchanges both arcs.
assert [(3-j)%6 for j in range(6)]==[3,2,1,0,5,4]
assert [(2-j)%6 for j in range(6)]==[2,1,0,5,4,3]
print(f'PASS {star_count} oriented label-compatible native stars; binary ledgers, AA endpoints, all6 homogeneous-plane intersections, all8 pure-star reflection assignments, native whole-side end bijections, exact count eliminations and all6 swapped A edge identities.')
