"""Independent exact clipping verification of retained seven-tile witness."""
import json
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
U=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
WORDS={'A':(2,1,2,1,2,1),'B':(2,2,3,1,3,2)}
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def make(name,r,eps,shift):
    x,y=map(F,shift); result=[]
    for k in range(6):
        result.append((x,y)); l=WORDS[name][(r+eps*k)%6]
        x+=l*U[k][0]; y+=l*U[k][1]
    assert (x,y)==result[0]
    return result

def intersection(P,Q):
    result=P[:]
    for a,b in zip(Q,Q[1:]+Q[:1]):
        edge=sub(b,a); prior=result; result=[]
        if not prior:break
        for p,q in zip(prior,prior[1:]+prior[:1]):
            dp=cross(edge,sub(p,a)); dq=cross(edge,sub(q,a))
            if dp>=0:result.append(p)
            if (dp<0<dq) or (dq<0<dp):
                t=dp/(dp-dq)
                result.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return result

def area2(P):return abs(sum(cross(p,q) for p,q in zip(P,P[1:]+P[:1]))) if P else 0
cert=json.loads(Path('research/searches/hexagon-imbalance-cocycle-corona-sol-2026-10-19.json').read_text())
polygons=[make('B',0,1,(0,0))]+[make(s['name'],s['r'],s['eps'],s['shift']) for s in cert['first']]
assert all(area2(P)>0 for P in polygons)
for P,Q in combinations(polygons,2):
    assert area2(intersection(P,Q))==0
    for R,S in ((P,Q),(Q,P)):
        for v in R:
            for a,b in zip(S,S[1:]+S[:1]):
                if cross(sub(b,a),sub(v,a))==0:
                    # Rational proportional parameter using a nonzero coordinate.
                    j=0 if a[0]!=b[0] else 1
                    t=(v[j]-a[j])/(b[j]-a[j])
                    assert not 0<t<1
P=polygons[0]
for k,Q in enumerate(polygons[1:]):
    assert Q[(k+4)%6]==P[k]
    assert Q[(k+3)%6]==P[(k+1)%6]
    R=polygons[1+(k+1)%6]
    # Adjacent ring tiles share a reversed full edge.
    assert any(Q[i]==R[(j+1)%6] and Q[(i+1)%6]==R[j]
               for i in range(6) for j in range(6))
print('PASS: independent rational clipping, all 21 polygon pairs, 6 central and 6 ring seams, no split-side contacts')
