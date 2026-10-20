"""Exact tangential P5/Q7 T-contact trial and cheap omission gates."""
from sage.all import AA, CyclotomicField
from importlib.util import spec_from_file_location, module_from_spec
from itertools import combinations_with_replacement

K = CyclotomicField(72)
z = K.gen()
I = z**18
def u(d):
    assert d % 5 == 0
    return z**(d//5)
def re(v): return (v+v.conjugate())/2
def im(v): return (v-v.conjugate())/(2*I)
def cot(d): return re(u(d))/im(u(d))
def cross(v,w): return re(v)*im(w)-im(v)*re(w)
def polygon(angles, lengths):
    directions=[0]
    for a in angles[1:]: directions.append(directions[-1]+180-a)
    edges=[lengths[j]*u(directions[j]) for j in range(len(angles))]
    assert sum(edges,K(0))==0
    vertices=[K(0)]
    for edge in edges[:-1]: vertices.append(vertices[-1]+edge)
    assert all(AA(cross(edges[j],edges[(j+1)%len(edges)]))>0 for j in range(len(edges)))
    return vertices, directions

pa=(80,110,100,120,130)
qa=(120,130,130,130,130,130,130)
cp={a:cot(a//2) for a in set(pa+qa)}
pl0=tuple(cp[pa[j]]+cp[pa[(j+1)%5]] for j in range(5))
pl=pl0
ql0=tuple(cp[qa[j]]+cp[qa[(j+1)%7]] for j in range(7))
host=pl[4]+pl[2]
scale=host/ql0[3]
ql=tuple(scale*x for x in ql0)
P,pdir=polygon(pa,pl)
Q,qdir=polygon(qa,ql)
assert pdir==[0,70,150,210,260]
assert qdir==[0,50,100,150,200,250,300]
assert ql[3]==pl[4]+pl[2]

# Q side 3 is placed from 0 to host, with Q above it.  The two
# orientation-reversed P copies occupy its lower half-plane.
Qpatch=[(v-Q[3])*u(-150) for v in Q]
Pleft=[(v-P[4]).conjugate()*u(260) for v in P]
Pright=[pl[4]+(v-P[2]).conjugate()*u(150) for v in P]

def disjoint_interiors(A,B):
    # Exact separating-axis test in the distinguished real embedding.
    for C in (A,B):
        for j in range(len(C)):
            e=C[(j+1)%len(C)]-C[j]
            axis=I*e
            av=[AA(re(v*axis.conjugate())) for v in A]
            bv=[AA(re(v*axis.conjugate())) for v in B]
            if max(av)<=min(bv) or max(bv)<=min(av): return True
    return False

patch=[Qpatch,Pleft,Pright]
assert all(disjoint_interiors(patch[i],patch[j]) for i in range(3) for j in range(i+1,3))
assert Pleft[0]==Pright[2]==K(pl[4])
assert pa[0]+pa[2]==180
assert qa[3]+pa[4]+pa[2]==360
assert qa[4]+pa[3]+pa[1]==360

# Every possible 80-degree corner completion is either a flat-side T
# with 100, or one of these all-corner four-stars.  The latter two are
# killed at the first unequal side endpoint, with no assumption of
# whole-edge contacts.
all_angles=pa+qa
assert min(all_angles)==80
assert AA(max(pl[1],pl[2]))<AA(min(pl[0],pl[4]))
assert AA(max(pl[2],pl[3]))<AA(min(pl[0],pl[4]))
assert AA(max(pl))<AA(ql[0])
assert 180-pa[1]==70 and 180-pa[3]==60 and 180-pa[4]==50
assert 180-qa[1]==50
stars80=[]
for n in (3,4):
    stars80 += [v for v in combinations_with_replacement(sorted(set(all_angles)),n)
                if 80 in v and sum(v)==360]
assert stars80==[(80,80,80,120),(80,80,100,100)]
# At the displayed left endpoint, a forced P100 cap must put either
# P1 or P2 along Q side 2.  Both end strictly inside that Q side, and
# their far angles are 110 or 120, leaving an impossible 70/60 wedge.
assert AA(max(pl[1],pl[2]))<AA(ql[2])

# Monohedral Q: the 130-degree corners cannot be completed using only
# 120/130-degree corners, even allowing partial contacts (all >90).
assert not any(130+a+b==360 for a in (120,130) for b in (120,130))

# P-only: run the repository's reviewed 15-family Rao gate, including
# every cyclic and reversed relabelling.
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
hits=[]
for typ,(angle_eqs,length_eqs) in mod.RAO.items():
    for sign in (1,-1):
        for offset in range(5):
            amap=[(offset+sign*i)%5 for i in range(5)]
            if not all(sum(coef*pa[j] for coef,j in zip(row,amap))==36*target
                       for row,target in angle_eqs): continue
            smap=[(offset+i)%5 if sign==1 else (offset-i-1)%5 for i in range(5)]
            if all(sum((coef*pl[j] for coef,j in zip(row,smap)),K(0))==0
                   for row in length_eqs): hits.append((typ,sign,offset))

print('P angles',pa,'P lengths',list(map(AA,pl)))
print('Q angles',qa,'Q lengths',list(map(AA,ql)))
print('Q host edge',AA(host),'P split lengths',AA(pl[4]),AA(pl[2]))
print('Exact closure, convexity, three-tile nonoverlap: PASS')
print('P-only Rao hits:',hits)
print('Q-only: impossible by 130-degree corner star')
print('Displayed split: both reflected P100 caps leave 70/60-degree wedge')
print('Every P80 corner: only an 80+100 T-contact survives local side lengths')
