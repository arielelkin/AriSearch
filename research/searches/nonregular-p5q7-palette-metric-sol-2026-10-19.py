"""One fixed native-word metric gate; run with Sage-enabled Python. No patch search."""
from itertools import combinations_with_replacement
from sage.all import AA, CyclotomicField, matrix, vector
import json

K = CyclotomicField(72)
z = K.gen()
i = z**18
re = lambda x: (x+x.conjugate())/2
im = lambda x: (x-x.conjugate())/(2*i)
cross = lambda x,y: re(x)*im(y)-im(x)*re(y)
cos = lambda exponent: re(z**exponent)
L = 2*(cos(7)-cos(13))
P_angles = (115,115,100,110,100)
Q_angles = (130,130,130,125,125,125,135)
P_dirs = (0,13,29,43,59)
Q_dirs = (0,10,20,31,42,53,62)
u = [z**e for e in Q_dirs]
rhs = -sum(u[j] for j in (0,2,4,6))-u[5]
M = matrix(K,[[re(u[1]),re(u[3])],[im(u[1]),im(u[3])]])
a,b = M.solve_right(vector(K,[re(rhs),im(rhs)]))
P_lengths = (L,K(1),K(1),K(1),K(1))
Q_lengths = (K(1),a,K(1),b,K(1),K(1),K(1))
assert all(AA(t)>0 for t in P_lengths+Q_lengths)
assert len(set((L,K(1),a,b))) == 4

def polygon(angles,dirs,lengths):
    assert sum(angles)==180*(len(angles)-2)
    assert all((dirs[j]-dirs[j-1])%72 == (180-angles[j])//5 for j in range(len(dirs)))
    vs=[K(0)]
    for e,l in zip(dirs,lengths):
        vs.append(vs[-1]+l*z**e)
    assert vs[-1]==0
    vs.pop()
    n=len(vs)
    for j in range(n):
        edge=vs[(j+1)%n]-vs[j]
        for k in range(n):
            if k not in (j,(j+1)%n):
                assert AA(cross(edge,vs[k]-vs[j]))>0
    return vs
P=polygon(P_angles,P_dirs,P_lengths)
Q=polygon(Q_angles,Q_dirs,Q_lengths)
# Complete unlabelled angle resonance domain, respecting species.
pa=(100,110,115)
qa=(125,130,135)
stars=[]
for k in range(4):
    for pp in combinations_with_replacement(pa,k):
        for qq in combinations_with_replacement(qa,3-k):
            if sum(pp+qq)==360:
                stars.append((pp,qq))
assert stars==[((100,),(125,135)),((100,),(130,130)),((110,),(125,125)),((110,115),(135,)),((115,115),(130,))]
# P115 corners are PPQ. Number of PPQ corners in any P equals twice
# its number of PP edges, hence even; its lone110 cannot also be PPQ.
# Native corner support checks use unordered incident length labels.
def corners(angles,lengths):
    return [(angle,frozenset((lengths[j-1],lengths[j]))) for j,angle in enumerate(angles)]
pc=corners(P_angles,P_lengths)
qc=corners(Q_angles,Q_lengths)
assert pc==[(115,frozenset((L,1))),(115,frozenset((L,1))),(100,frozenset((1,))),(110,frozenset((1,))),(100,frozenset((1,)))]
assert qc==[(130,frozenset((1,))),(130,frozenset((1,a))),(130,frozenset((1,a))),(125,frozenset((1,b))),(125,frozenset((1,b))),(125,frozenset((1,))),(135,frozenset((1,)))]
# Explicit triangle-of-seams witnesses for every native corner index.
# Each entry is [three tile species/corner indices, three seam lengths].
witnesses=[([('P',0),('P',1),('Q',0)],[L,1,1]),
           ([('P',2),('Q',1),('Q',2)],[1,a,1]),
           ([('P',3),('Q',3),('Q',4)],[1,b,1]),
           ([('P',4),('Q',5),('Q',6)],[1,1,1])]
covered=set()
for cs,ls in witnesses:
    assert sum((P_angles if s=='P' else Q_angles)[j] for s,j in cs)==360
    for k,(s,j) in enumerate(cs):
        c=(pc if s=='P' else qc)[j]
        assert c[1]==frozenset((ls[k-1],ls[k]))
        covered.add((s,j))
assert covered==set([('P',j) for j in range(5)]+[('Q',j) for j in range(7)])
# Every native edge has a mate consistent at both endpoints with the
# forced corner categories. This remains strictly weaker than a corona.
P_target=(115,115,100,110,100)
Q_target=(115,100,100,110,110,100,100)
for pe,qe in [(1,0),(2,2),(3,4),(4,6)]:
    assert P_lengths[pe]==Q_lengths[qe]
    pends=(P_target[pe],P_target[(pe+1)%5])
    qends=(Q_target[qe],Q_target[(qe+1)%7])
    assert pends==qends or pends==qends[::-1]
# Three QQ edges admit congruent endpoint-compatible mates. Side 5 must
# swap its 125/135 endpoints via a half-turn; this assertion is only local.
for j in (1,3,5):
    assert Q_angles[j]+Q_angles[(j+1)%7] in (250,260)

def data(t):
    return {'cyclotomic_basis':str(t),'minimal_polynomial':str(t.minpoly()),'approx':float(AA(t))}
print(json.dumps({'status':'exact_metric_and_native_corner_support_only',
 'field':'Q(zeta_72), embedding zeta_72=exp(2*pi*i/72)',
 'P_angles':P_angles,'Q_angles':Q_angles,'P_direction_exponents':P_dirs,
 'Q_direction_exponents':Q_dirs,'L':data(L),'a':data(a),'b':data(b),
 'P_coordinates':[str(t) for t in P], 'Q_coordinates':[str(t) for t in Q],
 'all_angle_stars':stars,'corner_witness_count':len(witnesses),
 'obligation':'Actual infinite compatible assignment or explicit periodic escape; no corona/patch/torus search performed.'},indent=2))
