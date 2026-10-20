"""Exact seam-cap reconnaissance for a new P5/Q7 shape-first pair."""
from sage.all import AA, NumberField, PolynomialRing, QQ, matrix, vector
from pathlib import Path
import importlib.util

R = PolynomialRing(QQ, 'x'); x = R.gen()
K = NumberField(x**4 - 10*x**2 + 1, 'z', embedding=AA(2).sqrt()+AA(3).sqrt())
z = K.gen(); r = (z-1/z)/2; s = (z+1/z)/2
assert r*r == 2 and s*s == 3 and r > 0 and s > 0
V = lambda a,b: vector(K,(a,b))
cross = lambda a,b: a[0]*b[1]-a[1]*b[0]
c = s-1
t = 1+3*r/2-s-r*s/2
assert c>0 and t>0 and len({K(1),c,t,s,c+2-t,c-t+3}) == 6
PD = [V(1,0),V((r*s-r)/4,(r*s+r)/4),V(-r/2,r/2),
      V(-(r*s+r)/4,-(r*s-r)/4),V(-1/2,-s/2)]
PL = (K(1),t,c,t,c)
QD = [V(1,0),V(s/2,1/2),V(0,1),V(-s/2,1/2),
      V(-s/2,-1/2),V(0,-1),V(s/2,-1/2)]
QL = (s,c,c+2-t,t,c-t+3,c,K(1))
def polygon(dirs,lens):
    v=[V(0,0)]
    for d,l in zip(dirs[:-1],lens[:-1]): v.append(v[-1]+l*d)
    assert v[-1]+lens[-1]*dirs[-1] == v[0]
    assert all(cross(v[(i+1)%len(v)]-v[i],v[(i+2)%len(v)]-v[(i+1)%len(v)])>0 for i in range(len(v)))
    return v
P=polygon(PD,PL); Q=polygon(QD,QL)

def overlap(a,b):
    for poly in (a,b):
        for i in range(len(poly)):
            e=poly[(i+1)%len(poly)]-poly[i]; n=V(-e[1],e[0])
            aa=[n*v for v in a]; bb=[n*v for v in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):return False
    return True

def place_corner(poly,i,j,k,origin,ray_j,ray_k):
    X=matrix(K,[[*(poly[j]-poly[i])],[*(poly[k]-poly[i])]]).transpose()
    Y=matrix(K,[[*ray_j],[*ray_k]]).transpose()
    M=Y*X.inverse()
    assert M.transpose()*M==matrix.identity(K,2)
    return [origin+M*(v-poly[i]) for v in poly]

# Two Q copies are related by a half-turn around the midpoint of their
# shared length-sqrt(3) side.  The 150+150 gap at each endpoint is 60.
Q0=Q
Q1=[Q[0]+Q[1]-v for v in Q]
O=Q[0]; E=Q[1]
# At O, Q0's outer ray is length 1 and Q1's is length c.
P0=place_corner(P,0,1,4,O,Q0[6]-O,Q1[2]-O)
# At E, Q1's outer ray is length 1 and Q0's is length c.
P1=place_corner(P,0,1,4,E,Q1[6]-E,Q0[2]-E)
base=[Q0,Q1,P0,P1]
assert all(not overlap(base[i],base[j]) for i in range(4) for j in range(i+1,4))

def cap_private_side(host,slot,others):
    """Half-turn mate on a Q private side, with two exact P(120) caps."""
    a,b=host[slot],host[(slot+1)%7]
    mate=[a+b-v for v in host]
    polyset=others+[host,mate]
    if any(overlap(mate,v) for v in others):return 'mate overlaps',None
    caps=[]
    for endpoint in (a,b):
        rays=[]
        for poly in (host,mate):
            ix=poly.index(endpoint)
            for j in ((ix-1)%7,(ix+1)%7):
                v=poly[j]-endpoint
                if v not in (b-a,a-b): rays.append(v)
        assert len(rays)==2
        cr=next(v for v in rays if v*v==c*c)
        tr=next(v for v in rays if v*v==t*t)
        cap=place_corner(P,3,2,4,endpoint,cr,tr)
        if any(overlap(cap,v) for v in polyset+caps):return 'cap overlaps',None
        caps.append(cap)
    return 'legal', [mate,*caps]

for slot in (2,4):
    status,added=cap_private_side(Q0,slot,[Q1,P0,P1])
    print('private Q slot',slot,'with base:',status)
    status2,added2=cap_private_side(Q0,slot,[])
    print('private Q slot',slot,'isolated:',status2)

# Imported reviewed transcription of the fifteen monohedral pentagon types.
spec=importlib.util.spec_from_file_location('rao',Path(__file__).with_name('convex-substitution-shapes.py'))
rao=importlib.util.module_from_spec(spec);spec.loader.exec_module(rao)
PA=(60,105,120,120,135); hits=[]
for typ,(ae,le) in rao.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            amap=[(off+sign*i)%5 for i in range(5)]
            if not all(sum(a*b for a,b in zip(row,[PA[j] for j in amap]))==target*36 for row,target in ae):continue
            smap=([(off+i)%5 for i in range(5)] if sign==1 else [(off-i-1)%5 for i in range(5)])
            if all(sum((coef*PL[j] for coef,j in zip(row,smap)),K(0))==0 for row in le):hits.append((typ,sign,off))
print('P lengths=',PL,'Q lengths=',QL,'Rao hits=',hits)
print('P=',P,'Q=',Q)
print('base four-tile P/Q/Q/P patch legal')
