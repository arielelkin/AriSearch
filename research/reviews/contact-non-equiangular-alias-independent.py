"""Independent exact alias-ring audit: direct native isometries and SAT overlap."""
from sage.all import AA, vector, matrix
from itertools import product
r=AA(2).sqrt(); c=((2+r)/4).sqrt(); t=((2-r)/4).sqrt()
x=w=AA(1);u=c;v=1+t;y=r-1/(r*c);lengths=(x,u,v,y,w)
def vec(a):return vector(AA,a)
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def perp(a):return vec((-a[1],a[0]))
P=[vec((0,0))]
for L,d in zip(lengths,((c,-t),(1/r,1/r),(-1/r,1/r),(-c,-t),(0,-1))):P.append(P[-1]+L*vec(d))
assert P.pop()==P[0]
k=r-1;z=k*c/(1+k);h=(1-k*c)/(1-k)
Q=[vec(p) for p in ((z,-z),(h,h-1),(1+r/2,r/2),(1+r/2,1+r/2),(1,1+r),(0,1+r),(-r/2,1+r/2),(-r/2,r/2))]
Ql=[(Q[(i+1)%8]-Q[i]).norm() for i in range(8)]
assert Ql==[2*c-1,u,1,1,1,1,1,v]
assert len(set(lengths))==4 and Ql[0] not in lengths
assert all(a>0 and a not in (2*u,2*v) for a in list(lengths)+Ql)
for F in (P,Q):
 for i in range(len(F)):
  a,b=F[i],F[(i+1)%len(F)]
  assert all(det(b-a,p-a)>0 for j,p in enumerate(F) if j not in (i,(i+1)%len(F)))
def allmates(A,B):
    e=B-A; result={}
    for s in range(5):
        p,q=P[s],P[(s+1)%5];f=q-p
        if f.dot_product(f)!=e.dot_product(e):continue
        src=matrix(AA,[list(f),list(perp(f))]).transpose()
        for first,last in ((A,B),(B,A)):
            g=last-first
            for sign in (-1,1):
                dst=matrix(AA,[list(g),list(sign*perp(g))]).transpose()
                M=dst*src.inverse()
                assert M.transpose()*M==matrix.identity(AA,2)
                T=[first+M*(p0-p) for p0 in P]
                if det(e,sum(T,vec((0,0)))/5-A)<0:
                    result[tuple(sorted(tuple(a) for a in T))]=(T,s)
    return list(result.values())
def other(T,at,second):
    j=T.index(at)
    return next(T[k] for k in ((j-1)%5,(j+1)%5) if T[k]!=second)
def disjoint(F,G):
    for S in (F,G):
        for i,p in enumerate(S):
            n=perp(S[(i+1)%len(S)]-p)
            a=[n.dot_product(z) for z in F];b=[n.dot_product(z) for z in G]
            if max(a)<=min(b) or max(b)<=min(a):return True
    return False
Pu=[T for T,s in allmates(Q[1],Q[2]) if T[2]==Q[1]]
Pv=[T for T,s in allmates(Q[7],Q[0]) if T[2]==Q[0]]
assert len(Pu)==len(Pv)==1
Qmate=[Q[0]+Q[1]-p for p in Q]
opts=[allmates(Q[i],Q[i+1]) for i in range(2,7)]
assert [len(o) for o in opts]==[4]*5
patterns=[]
for choices in product(range(4),repeat=5):
    picked=[options[j] for options,j in zip(opts,choices)]
    guests=[Pu[0]]+[T for T,s in picked]+[Pv[0]]
    if not all(other(guests[j-1],Q[j+1],Q[j])==other(guests[j],Q[j+1],Q[(j+2)%8]) for j in range(1,7)):continue
    tiles=[Q,Qmate]+guests
    if not all(disjoint(F,G) for i,F in enumerate(tiles) for G in tiles[i+1:]):continue
    word=''.join('X' if s==0 else 'W' for T,s in picked)
    assert all(s in (0,4) for T,s in picked)
    witnesses=[]
    pairs=[sorted((Ql[j-1],Ql[j])) for j in range(2,8)]
    for j in range(1,7):
        L,R=guests[j-1:j+1];at=Q[j+1];far=other(L,at,Q[j])
        assert far==other(R,at,Q[(j+2)%8])
        if L.index(far)==2 or R.index(far)==2:continue
        need=sorted(((other(L,far,at)-far).norm(),(other(R,far,at)-far).norm()))
        if need not in pairs:witnesses.append(need)
    assert witnesses
    patterns.append(word)
assert sorted(patterns)==sorted(('XXXXW','XXWWW','WWXXW','WWWWW'))
print('PASS: independent full4^5 native-ring census; four SAT-disjoint rings; every ring missing a required far Q135 pair')
