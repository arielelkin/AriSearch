"""Exact first-gate audit of Astra's mixed P5/Q5 midpoint proposal."""
from itertools import product
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from sage.all import AA, QQ, CyclotomicField

K=CyclotomicField(60)
z=K.gen()
I=z**15
u=lambda d:z**(d//6)
re=lambda w:(w+w.conjugate())/2
im=lambda w:(w-w.conjugate())/(2*I)
cr=lambda a,b:re(a)*im(b)-im(a)*re(b)
dt=lambda a,b:re(a)*re(b)+im(a)*im(b)
def solve(a,b,w):
    d=cr(a,b)
    return cr(w,b)/d,cr(a,w)/d
def poly(ds,ls):
    p=[K(0)]
    for d,l in zip(ds,ls):p.append(p[-1]+l*u(d))
    assert p[-1]==0
    return tuple(p[:-1])
def sep(A,B):
    """True iff strict interiors overlap; exact separating-axis test."""
    for C in (A,B):
        for i in range(len(C)):
            x,y=C[i],C[(i+1)%len(C)]
            valsA=[AA(cr(y-x,p-x)) for p in A]
            valsB=[AA(cr(y-x,p-x)) for p in B]
            if max(valsA)<=min(valsB) or max(valsB)<=min(valsA):return False
    return True
def place(poly,i,j,A,B,flip):
    src=lambda w:w.conjugate() if flip else w
    unit=(B-A)/(src(poly[j])-src(poly[i]))
    assert unit*unit.conjugate()==1
    return tuple(A+unit*(src(p)-src(poly[i])) for p in poly)

PD=(0,84,144,192,252)
QD=(0,96,132,204,240)
p0,p4=solve(u(0),u(252),-u(144)-(u(84)+u(192))/5)
q1,q2=solve(u(96),u(132),-2*u(0)-3*u(240)-u(204)/5)
PL=(p0,K(QQ(1)/5),K(1),K(QQ(1)/5),p4)
QL=(K(2),q1,q2,K(QQ(1)/5),K(3))
P=poly(PD,PL);Q=poly(QD,QL)
assert all(AA(a)>0 for a in PL+QL)
assert all(AA(cr(R[(i+1)%5]-R[i],R[(i+2)%5]-R[(i+1)%5]))>0 for R in (P,Q) for i in range(5))
ANGLE={'P':(72,96,120,132,120),'Q':(60,84,144,108,144)}
SHAPE={'P':(P,PL),'Q':(Q,QL)}
def rao_hits(angles,lengths):
    src=Path('research/searches/convex-substitution-shapes.py')
    spec=spec_from_file_location('rao_route_b',src)
    mod=module_from_spec(spec);spec.loader.exec_module(mod)
    hits=[]
    for typ,(aeqs,leqs) in mod.RAO.items():
        for sign in (1,-1):
            for off in range(5):
                amap=[(off+sign*i)%5 for i in range(5)]
                a=[angles[i] for i in amap]
                if not all(sum(c*x for c,x in zip(row,a))==36*target for row,target in aeqs):continue
                smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
                if all(sum((c*lengths[i] for c,i in zip(row,smap)),K(0))==0 for row in leqs):
                    hits.append((typ,sign,off))
    return hits

def endpoint_completions(existing,E,start_ray,start_len,end_ray,end_len,gap,sequences):
    """Enumerate all full corners in a named vertex sector of gap degrees."""
    out=[]
    ratio=(end_ray/end_len)/(start_ray/start_len)
    signs=[s for s in (-1,1) if ratio==u(s*gap)]
    assert len(signs)==1,(gap,ratio)
    sign=signs[0]
    def rec(tiles,trail,ray,raylen,remaining,seq):
        if remaining==0:
            if not seq and cr(ray,end_ray)==0 and AA(dt(ray,end_ray))>0:
                out.append((trail,tiles))
            return
        if not seq:return
        for typ in (seq[0][0],):
            poly,lens=SHAPE[typ]
            for j in (seq[0][1],):
                theta=ANGLE[typ][j]
                if theta>remaining:continue
                for neighbor in ((j-1)%5,(j+1)%5):
                    sn=(j-1)%5 if neighbor==(j-1)%5 else j
                    for flip in (0,1):
                        src=lambda w:w.conjugate() if flip else w
                        delta=src(poly[neighbor]-poly[j])
                        unit=ray*lens[sn]/(raylen*delta)
                        assert unit*unit.conjugate()==1
                        C=tuple(E+unit*(src(p)-src(poly[j])) for p in poly)
                        other=(j+1)%5 if neighbor==(j-1)%5 else (j-1)%5
                        other_slot=j if neighbor==(j-1)%5 else (j-1)%5
                        if (C[other]-E)/lens[other_slot] != (ray/raylen)*u(sign*theta):continue
                        if any(sep(C,Z) for Z in existing+tiles):continue
                        rec(tiles+(C,),trail+((typ,j,neighbor,flip),),C[other]-E,lens[other_slot],remaining-theta,seq[1:])
    for seq in sequences:
        if sum(ANGLE[t][j] for t,j in seq)==gap:
            rec((),(),start_ray,start_len,gap,seq)
    return out

print('P lengths',*[str(AA(v)) for v in PL])
print('Q lengths',*[str(AA(v)) for v in QL])
print('exact closure, positivity, strict convexity: PASS')
print('Rao pentagon monohedral type hits P/Q',rao_hits(ANGLE['P'],PL),rao_hits(ANGLE['Q'],QL))
A,B=Q[4],Q[0]
assert (B-A)*(B-A).conjugate()==9
print('host side Q4 endpoints',A,B)

# Q side 4 runs from vertex 4 to vertex 0. In each order put guest side 2
# of P and side 0 of Q on opposite sides of the host side at a common point.
for order in (0,1):
    M=A+(B-A)*(QQ(1)/3 if order==0 else QQ(2)/3)
    # first guest from A to M / second from M to B
    first=('P',P,3,2) if order==0 else ('Q',Q,1,0)
    second=('Q',Q,0,1) if order==0 else ('P',P,2,3)
    print('ORDER',order,'midpoint',M)
    for f1,f2 in product((0,1),repeat=2):
        X=place(first[1],first[2],first[3],A,M,f1)
        Y=place(second[1],second[2],second[3],M,B,f2)
        overlaps=(sep(Q,X),sep(Q,Y),sep(X,Y))
        if any(overlaps):
            print(' branch',f1,f2,'overlap',overlaps)
            continue
        # Midpoint P120 and Q60, outgoing rays are incident sides 1 and 4.
        T=X if first[0]=='P' else Y
        U=X if first[0]=='Q' else Y
        assert T[2]==M and U[0]==M
        pr=T[1]-M; qr=U[4]-M
        straight=(cr(pr,qr)==0 and AA(dt(pr,qr))>0)
        E=M+pr
        # E is P side1 endpoint, Q side4 interior if straight.
        onQ=(cr(qr,E-M)==0 and AA(dt(qr,E-M))>0 and AA(dt(qr,E-M))<AA(dt(qr,qr)))
        print(' branch',f1,f2,'nonoverlap midpoint-straight',straight,'P1-end-on-Q4',onQ,'E',E)
        if straight and onQ:
            # Exact orientation from E to P0 and to the far end of guest Q4.
            outP=T[0]-E
            outQ=U[4]-E
            print('  short-end gap angle 84; Q1 is unique native corner')
            ec=[]
            for jnext,other in ((0,2),(2,0)):
                for flip in (0,1):
                    # Avoid square roots in the placement: map a full source side
                    # to the direction and require unit scale by its own length.
                    src=lambda w:w.conjugate() if flip else w
                    source=src(Q[jnext]-Q[1])
                    target=outP*(QL[0] if jnext==0 else QL[1])/PL[0]
                    C=tuple(E+target/source*(src(p)-src(Q[1])) for p in Q)
                    ray2=C[other]-E
                    aligned=(cr(ray2,outQ)==0 and AA(dt(ray2,outQ))>0)
                    ov=tuple(sep(C,Z) for Z in (Q,T,U))
                    if aligned:
                        print('  Q1 completion',jnext,flip,'nonoverlap',not any(ov),'overlaps',ov,'next Q1 side endpoint',C[jnext])
                        if not any(ov):ec.append(((jnext,flip),C))
            left_guest= X[4] if order==0 else X[2]
            right_guest=Y[2] if order==0 else Y[4]
            gapA=84 if order==0 else 132
            gapB=216 if order==0 else 168
            lenA=PL[3] if order==0 else QL[1]
            lenB=QL[1] if order==0 else PL[3]
            seqA=((('Q',1),),) if order==0 else ((('P',3),),)
            seqB=((('Q',3),('Q',3)),(('P',1),('P',2)),(('P',2),('P',1))) if order==0 else ((('Q',1),('Q',1)),(('P',0),('P',1)),(('P',1),('P',0)))
            ca=endpoint_completions((Q,X,Y),A,Q[3]-A,QL[3],left_guest-A,lenA,gapA,seqA)
            cb=endpoint_completions((Q,X,Y),B,Q[1]-B,QL[0],right_guest-B,lenB,gapB,seqB)
            print('  host endpoint A completions',len(ca),[v[0] for v in ca[:8]])
            print('  host endpoint B completions',len(cb),[v[0] for v in cb[:8]])
            together=[(ta,tb) for ta,tb in product(ca,cb) if all(not sep(a,b) for a,b in product(ta[1],tb[1]))]
            print('  simultaneous host endpoint completions',len(together))
            allthree=next(((e[0],a[0],b[0]) for e,a,b in product(ec,ca,cb)
                           if all(not sep(e[1],v) for v in a[1]+b[1])
                           and all(not sep(v,w) for v,w in product(a[1],b[1]))),None)
            print('  simultaneous short endpoint and both host endpoints witness',allthree)

for mode,G,ai,an,alen,bi,bn,blen,gapA,gapB,seqA,seqB in (
    ('mirror',place(Q,4,0,A,B,1),4,3,QL[3],0,1,QL[0],72,240,
     ((('P',0),),),((('P',2),('P',2)),)),
    ('halfturn',place(Q,4,0,B,A,0),0,1,QL[0],4,3,QL[3],156,156,
     ((('P',0),('Q',1)),(('Q',1),('P',0))),
     ((('P',0),('Q',1)),(('Q',1),('P',0))))):
    assert G[ai]==A and G[bi]==B
    print('Q/Q whole-host',mode,'nonoverlap',not sep(Q,G))
    ca=endpoint_completions((Q,G),A,Q[3]-A,QL[3],G[an]-A,alen,gapA,seqA)
    cb=endpoint_completions((Q,G),B,Q[1]-B,QL[0],G[bn]-B,blen,gapB,seqB)
    pair=next(((a[0],b[0]) for a,b in product(ca,cb)
               if all(not sep(v,w) for v,w in product(a[1],b[1]))),None)
    print('Q/Q',mode,'endpoint A/B completions',len(ca),len(cb),'simultaneous witness',pair)
