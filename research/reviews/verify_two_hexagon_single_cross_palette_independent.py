#!/usr/bin/env python3
"""Root audit: no author imports; native honeycomb flags and a different exact field."""
import json,sys
from itertools import product,permutations,combinations_with_replacement
from collections import defaultdict
from sage.all import CyclotomicField,QQbar,AA

cert=json.load(open(sys.argv[1]))
classes=(0,0,1,2,3,4)
assert tuple(cert['A_side_classes'])==classes
def canon(w):
    return min(v[k:]+v[:k] for v in (w,w[::-1]) for k in range(6))
assert {tuple(r['B_word']) for r in cert['B_closure_rows']}=={canon(w) for w in permutations((0,0,1,1,2,2))}
assert len(cert['B_closure_rows'])==11
placements=list(product(range(6),(1,-1)))
def corner(p,k): return (p[0]+p[1]*k)%6
def side(p,k): return classes[(p[0]+k if p[1]==1 else p[0]-k-1)%6]
# True corner slots 0,2,4 and all three common-side flags.
valid=[]
for a,b,c in product(placements,repeat=3):
    if {corner(a,0)%3,corner(b,2)%3,corner(c,4)%3}!={0,1,2}: continue
    if side(a,5)==side(b,2) and side(a,0)==side(c,3) and side(b,1)==side(c,4):
        valid.append((a,b,c))
assert not valid and not cert['AAA_survivors']
# AAB: B is at slot4. Shared AA edge uses a5/b2. B arms meet a0/b1.
fan_pairs=[set() for _ in range(3)]
for a,b in product(placements,repeat=2):
    colour=corner(a,0)%3
    if corner(b,2)%3==colour and side(a,5)==side(b,2):
        fan_pairs[colour].add((side(a,0),side(b,1)))
assert fan_pairs==[{(0,0),(1,1),(2,2),(4,4)}, {(0,0),(2,2),(3,3)}, {(0,0),(1,1),(3,3),(4,4)}]
assert set.intersection(*(set(a for a,b in ps) for ps in fan_pairs))=={0}
# Every cyclic B word either has adjacent equal colours (no native A side),
# or has a 0/2 edge, which no L-side of A carries. Both endpoint orders included.
length_L_pairs={frozenset((i%3,(i+1)%3)) for i,x in enumerate(classes) if x==0}
for w in set(permutations((0,0,1,1,2,2))):
    assert any(w[i]==w[(i+1)%6] or frozenset((w[i],w[(i+1)%6])) not in length_L_pairs for i in range(6))
# Exact geometry reconstructed in Q(zeta_720), avoiding producer field/fixtures.
F=CyclotomicField(720); root=F.gen(); unit=lambda d: root**(2*d)
j=root**180
sin=lambda d:(unit(d)-unit(-d))/(2*j)
ls=(F(4),F(6),4-sin(54),4+sin(113),6-sin(59))
assert len(set(ls))==5
assert sin(54)-sin(113)*unit(59)+sin(59)*unit(113)==0
assert sum((ls[classes[i]]*unit(d) for i,d in enumerate((0,59,113,180,239,293))),F(0))==0
angles=(134,118,108)
aa=(113,121,126,134,118,108)
assert [t for t in combinations_with_replacement(range(6),3) if sum(aa[i] for i in t)==360]==[(0,0,3),(0,1,2),(1,1,4),(2,2,5),(3,4,5)]
closed_rows=[]
for row in cert['B_closure_rows']:
    w=row['B_word']; ds=[0]
    for a in w[1:]: ds.append(ds[-1]+180-angles[a])
    residue=sum((unit(d) for d in ds),F(0))
    assert row['family_constant_closed_classes']==(list(range(5)) if residue==0 else [])
    left=defaultdict(list); right=defaultdict(list)
    for word in product(range(5),repeat=3):
        left[sum((ls[t]*unit(d) for t,d in zip(word,ds[:3])),F(0))].append(word)
        right[sum((ls[t]*unit(d) for t,d in zip(word,ds[3:])),F(0))].append(word)
    actual={a+b for v,aa in left.items() for a in aa for b in right.get(-v,[])}
    assert actual=={tuple(t) for t in row['relaxed_sample_closed_words']}
    if residue==0:
        assert actual=={t+t for t in product(range(5),repeat=3)}
        closed_rows.append(tuple(w))
assert closed_rows==[(0,1,2,0,1,2)]
# Exact central B carrier: polygon closure/support and rank-two area identity.
vv=[F(0)]
for d in (0,62,134,180,242,314): vv.append(vv[-1]+unit(d))
assert vv[-1]==0
v=vv[:6]; cross=lambda a,b:(a.conjugate()*b-a*b.conjugate())/(2*j)
embed=F.hom([QQbar.zeta(720)],QQbar)
positive=lambda a: AA(embed(a).real())>0
assert all(positive(cross(v[(i+1)%6]-v[i],v[k]-v[i])) for i in range(6) for k in range(6) if k not in (i,(i+1)%6))
t0=v[0]+v[1]-v[3];t2=v[2]+v[3]-v[3]
area=sum((cross(v[i],v[(i+1)%6]) for i in range(6)),F(0))/2
assert cross(t0,t2)==area and positive(area)
assert v[1]+v[2]-v[3]==t0+t2
for i in range(3):
    tr=v[i]+v[(i+1)%6]-v[3]
    assert v[(i+3)%6]+tr==v[(i+1)%6]
    assert v[(i+4)%6]+tr==v[i]
print('PASS: 1728 native AAA placements, reflected AAB fans, all 90 B words, 11 exact closure gates, 171875 relaxed sample assignments, and central B rank-two carrier. Root audit; no author imports.')
