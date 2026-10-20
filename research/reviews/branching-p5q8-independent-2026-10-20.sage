"""Independent exact audit of the two branching P5/Q8 neighborhood obstructions.

Replay with: mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/branching-p5q8-independent-2026-10-20.sage
Does not import the searched construction's code.
"""
from itertools import product
from sage.all import AA, QQ, QQbar, matrix, vector

PA=(100,110,100,120,110)
QA=(150,130,140,130,140,120,140,130)
z=QQbar.zeta(36)
O=vector(AA,(0,0))

def turns(ang):
    theta=0
    out=[]
    for j in range(len(ang)):
        w=z**(theta//10)
        out.append(vector(AA,(w.real(),w.imag())))
        theta+=180-ang[(j+1)%len(ang)]
    return out

PD,QD=turns(PA),turns(QA)

def close(dirs, fixed, i, j):
    rhs=-sum((v*dirs[k] for k,v in fixed.items()),O)
    M=matrix(AA,[[dirs[i][0],dirs[j][0]],[dirs[i][1],dirs[j][1]]])
    a,b=M.solve_right(rhs)
    ret=dict(fixed); ret[i]=a; ret[j]=b
    return [ret[k] for k in range(len(dirs))]

def shape(lengths,dirs):
    v=[O]
    for a,d in zip(lengths,dirs): v.append(v[-1]+a*d)
    assert v[-1]==O
    return v[:-1]

def cross(u,v): return u[0]*v[1]-u[1]*v[0]

def image(source, labels, targets):
    """Map three source vertices to three targets by a checked isometry."""
    s0,s1,s2=[source[i] for i in labels]
    t0,t1,t2=targets
    S=matrix(AA,[[*(s1-s0)],[*(s2-s0)]]).transpose()
    T=matrix(AA,[[*(t1-t0)],[*(t2-t0)]]).transpose()
    if S.det()==0: return None
    M=T*S.inverse()
    if M.transpose()*M != matrix.identity(AA,2): return None
    return [t0+M*(v-s0) for v in source]

def collision(x,y):
    for poly in (x,y):
        for j in range(len(poly)):
            e=poly[(j+1)%len(poly)]-poly[j]
            n=vector(AA,(-e[1],e[0]))
            a=[n.dot_product(v) for v in x]
            b=[n.dot_product(v) for v in y]
            if max(a)<=min(b) or max(b)<=min(a): return False
    return True

def seam(p, side, mate, mirror):
    """Across p[side]--p[side+1], map mate's directed edge with both parities."""
    S=[vector(AA,(v[0],-v[1])) for v in p] if mirror else p
    a,b=p[side],p[(side+1)%5]
    # With mirrored source, same direction puts its interior across the edge.
    ta,tb=(a,b) if mirror else (b,a)
    u=S[mate]; v=S[(mate+1)%5]
    e=v-u; f=tb-ta
    if e.dot_product(e)!=f.dot_product(f): return None
    M=matrix(AA,[[e.dot_product(f),-cross(e,f)],
                  [cross(e,f),e.dot_product(f)]])/e.dot_product(e)
    return [ta+M*(x-u) for x in S]

def q_options(q, center, neighbor, p, side, mate, mirror, end):
    ci=(side+end)%5
    ni=(mate+end)%5 if mirror else (mate+1-end)%5
    V=center[ci]
    assert V==neighbor[ni]
    ra=center[(ci-1)%5] if end==0 else center[(ci+1)%5]
    rb=neighbor[(ni-1)%5] if ni==mate else neighbor[(ni+1)%5]
    vacancy=360-PA[ci]-PA[ni]
    ans=[]
    for j,a in enumerate(QA):
        if a!=vacancy: continue
        for r,s in ((ra,rb),(rb,ra)):
            tile=image(q,(j,(j+1)%8,(j-1)%8),(V,r,s))
            if tile is not None and not collision(tile,center) and not collision(tile,neighbor) and tile not in ans:
                ans.append(tile)
    return ans

pz=close(PD,{0:AA(0),3:AA(0),4:AA(1)},1,2)
po=close(PD,{0:AA(1),3:AA(1),4:AA(1)},1,2)
t=(AA(1)-pz[1])/(po[1]-pz[1])
PL=close(PD,{0:t,3:t,4:AA(1)},1,2)
P=shape(PL,PD)
assert PL[1]==1 and all(x>0 for x in PL)

for k,rev,extra in ((1,False,{2:QQ(1)/5,3:QQ(1)/5,6:QQ(1)/5}),
                    (7,True,{1:QQ(1)/5,2:QQ(1)/5,3:QQ(3)/2})):
    fixed={0:AA(1),7:AA(1), **extra}
    fixed[(k-1)%8]=PL[2] if rev else PL[1]
    fixed[k]=PL[1] if rev else PL[2]
    QL=close(QD,fixed,4,5)
    assert all(x>0 for x in QL) and all(x!=t for x in QL)
    Q=shape(QL,QD)
    for b0,f0,b3,f3 in product((0,3),(False,True),(0,3),(False,True)):
        n0=seam(P,0,b0,f0); n3=seam(P,3,b3,f3)
        assert n0 is not None and n3 is not None
        opts=[q_options(Q,P,n0,P,0,b0,f0,0),
              q_options(Q,P,n0,P,0,b0,f0,1),
              q_options(Q,P,n3,P,3,b3,f3,0),
              q_options(Q,P,n3,P,3,b3,f3,1)]
        counts=tuple(map(len,opts))
        if f0 or f3:
            assert 0 in counts
            continue
        assert not collision(n0,n3)
        expected={(0,0):(2,2,1,2),(0,3):(2,2,1,1),
                  (3,0):(2,1,1,2),(3,3):(2,1,1,1)}[(b0,b3)]
        assert counts==expected,(k,b0,b3,counts,expected)
        # The two Q tiles required at center vertices 1 and 3 cannot coincide;
        # every distinct image pair has a positive-area intersection.
        assert all(x!=y and collision(x,y) for x in opts[1] for y in opts[2])
        print('AUDIT',k,rev,b0,b3,counts,'distinct universal conflict',flush=True)
print('PASS: both exact branching metrics are locally impossible')
