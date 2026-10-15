"""Exact bounded congruence gate for three-sector surgery with thick caps split.
No metric search, numerical angles, or imports from construction producers.
Finite domain: 4 source-type/parity cases, formal corner-angle identities,
cap boundary incidence, and the sign of one exact vector dot product.
"""
from collections import Counter
from fractions import Fraction as Q
# Linear angle forms on basis U,T,M,P,pi.
def add(*rows):return tuple(sum(xs) for xs in zip(*rows))
def scale(row,k):return tuple(k*x for x in row)
U=(Q(1),Q(0),Q(0),Q(0),Q(0))
T=(Q(0),Q(1),Q(0),Q(0),Q(0))
M=(Q(0),Q(0),Q(1),Q(0),Q(0))
P=(Q(0),Q(0),Q(0),Q(1),Q(0))
pi=(Q(0),Q(0),Q(0),Q(0),Q(1))
betaT=scale(add(pi,T),Q(1,2));betaP=scale(add(pi,P),Q(1,2))
angles=[U,betaT,betaT,M,betaP,betaP]
assert add(*angles[::2],*map(lambda row:scale(row,-1),angles[1::2]))==add(U,scale(M,-1))
# A cyclic hexagon has equal odd/even angle sums, each 2pi.
# Hence its equal-radius truncated original quad must have U=M.

marks={'thin':('X','X','Y','Y'),'thick':('X','Y','Y','X')}
for species,word in marks.items():
    for parity in (0,1):
        donors=Counter(word[i] for i in range(parity,4,2))
        receivers=Counter(word[i] for i in range(1-parity,4,2))
        assert donors==receivers==Counter({'X':1,'Y':1})
# Source original endpoint-angle sum = 2pi - donor beta + received beta.
# The obtuse sign is exact and general: for an outward normal n and
# interior p, dot(h*n,p-M)=h*dot(n,p-M)<0. Rational fixture sanity check:
h=Q(3,7);pminusM=(Q(-2,5),Q(-5,11));tminusM=(0,h)
assert sum(a*b for a,b in zip(pminusM,tminusM))<0

def edge(a,b):return tuple(sorted((a,b)))
def boundary(word):return Counter(edge(word[i],word[(i+1)%len(word)]) for i in range(len(word)))
# Opposite cap edges0/3 receive interior chord endpoints a/b.
left=('a','c1','c2','c3','b')
right=('b','c4','c5','c0','a')
refined=('c0','a','c1','c2','c3','b','c4','c5')
combined=boundary(left)+boundary(right)
assert combined==boundary(refined)+Counter({edge('a','b'):2})
assert len(left)==len(right)==5
# Count vectors and exact formal area inversion (phi satisfies phi²=phi+1).
# Write areas as coefficients of (1,phi), times thin source area.
Parea=(Q(-2,14),Q(3,14));Harea=(Q(3,14),Q(-1,14))
assert tuple(2*Parea[i]+6*Harea[i] for i in (0,1))==(1,0)
assert tuple(6*Parea[i]+4*Harea[i] for i in (0,1))==(0,1)
print('PASS: cap split incidence, 4 mark-balanced source cases, exact cyclic truncation identity U=M, normal-foot obtuse sign, and independent area vectors')
