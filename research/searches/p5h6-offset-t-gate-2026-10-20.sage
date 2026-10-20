"""Exact bounded geometry gate for the changed P5/H6 offset seam."""
from itertools import product
from sage.all import AA, CyclotomicField

K = CyclotomicField(36)
z = K.gen()
I = z**9
u = lambda d: z**(d//10)
re = lambda w: (w+w.conjugate())/2
im = lambda w: (w-w.conjugate())/(2*I)
cr = lambda a,b: re(a)*im(b)-im(a)*re(b)
dot = lambda a,b: re(a)*re(b)+im(a)*im(b)

def solve(a,b,w):
    d=cr(a,b)
    assert d != 0
    return cr(w,b)/d,cr(a,w)/d

def polygon(dirs,lens):
    out=[K(0)]
    for d,l in zip(dirs,lens):out.append(out[-1]+l*u(d))
    assert out[-1]==0
    out=tuple(out[:-1]);n=len(out)
    assert all(AA(l)>0 for l in lens)
    assert all(AA(cr(out[(i+1)%n]-out[i],out[(i+2)%n]-out[(i+1)%n]))>0 for i in range(n))
    return out

def overlap(A,B):
    # Strict interior intersection of strictly convex polygons by SAT.
    for C in (A,B):
        for i in range(len(C)):
            x,y=C[i],C[(i+1)%len(C)]
            pa=[AA(cr(y-x,a-x)) for a in A]
            pb=[AA(cr(y-x,b-x)) for b in B]
            if max(pa)<=min(pb) or max(pb)<=min(pa):return False
    return True

def place(poly,i,j,A,B,flip):
    f=lambda w:w.conjugate() if flip else w
    unit=(B-A)/(f(poly[j])-f(poly[i]))
    assert unit*unit.conjugate()==1
    return tuple(A+unit*(f(w)-f(poly[i])) for w in poly)

def same_ray(a,b):return cr(a,b)==0 and AA(dot(a,b))>0
def strict_between(A,B,X):
    direction=B-A
    return cr(direction,X-A)==0 and AA(dot(X-A,direction))>0 and AA(dot(B-X,direction))>0

p,q=solve(u(0),u(150),-u(50)-K(3)/2*u(200)-u(280)/2)
L=p+q
c,e=solve(u(180),u(280),-L*u(0)-u(50)-u(100)-u(230)/2)
PL=(p,K(1),q,K(3)/2,K(1)/2)
HL=(L,K(1),K(1),c,K(1)/2,e)
P=polygon((0,50,150,200,280),PL)
H=polygon((0,50,100,180,230,280),HL)
assert len(set((p,q,L,c,e,K(1),K(1)/2,K(3)/2)))==8

print('Exact P/H closure, positivity, convexity: PASS')
print('p,q,L,c,e:',[AA(x) for x in (p,q,L,c,e)])

split=[]
for order in (0,1):
    M=p if order==0 else q
    # Each side may be sent to each oriented subsegment, with both chiralities.
    parts=((0,1,0,p),(2,3,p,L)) if order==0 else ((2,3,0,q),(0,1,q,L))
    for rev0,rev1,flip0,flip1 in product((0,1),repeat=4):
        choices=[]
        for (i,j,A,B),rev,flip in zip(parts,(rev0,rev1),(flip0,flip1)):
            V=place(P,j,i,A,B,flip) if rev else place(P,i,j,A,B,flip)
            choices.append(V)
        X,Y=choices
        if overlap(H,X) or overlap(H,Y) or overlap(X,Y):continue
        # Save actual interior-disjoint branches, including branches that do
        # not make the desired 100/80 flat midpoint.
        split.append((order,rev0,rev1,flip0,flip1,X,Y))
print('Nonoverlap split placements of 32:',len(split))
assert len(split)==2
for order,r0,r1,f0,f1,X,Y in split:
    M=p if order==0 else q
    first,second=(X,Y)
    # For the intended order, the midpoint native corners are P0 and P2.
    intended=(order==0 and first[0]==M and second[2]==M) or (order==1 and first[2]==M and second[0]==M)
    print('split',order,r0,r1,f0,f1,'intended',intended)
    assert intended

def corner_placements(poly,lens,j,E,rayA,lenA,rayB,lenB):
    """All reflected/unreflected native corner placements in a fixed wedge."""
    result=[]
    n=len(poly)
    for neighbor,target,target_len in ((j-1,rayA,lenA),(j+1,rayA,lenA),
                                       (j-1,rayB,lenB),(j+1,rayB,lenB)):
        neighbor%=n
        other=(j+1)%n if neighbor==(j-1)%n else (j-1)%n
        side=(j-1)%n if neighbor==(j-1)%n else j
        for flip in (0,1):
            f=lambda w:w.conjugate() if flip else w
            unit=target*lens[side]/(target_len*f(poly[neighbor]-poly[j]))
            assert unit*unit.conjugate()==1
            C=tuple(E+unit*(f(w)-f(poly[j])) for w in poly)
            other_target=rayB if target==rayA else rayA
            if same_ray(C[other]-E,other_target):
                key=tuple(C)
                if key not in (item[0] for item in result):
                    result.append((key,j,neighbor,flip))
    return result

for order,r0,r1,f0,f1,X,Y in split:
    A=X if order==0 else Y       # side0 P, short unit P4
    B=Y if order==0 else X       # side2 P, long unit P1
    M=p if order==0 else q
    E=A[4]
    assert A[0]==B[2]==M
    assert E==M+(B[1]-M)/2
    assert same_ray(A[3]-E,B[1]-E) is False
    caps=corner_placements(P,PL,2,E,A[3]-E,PL[3],B[1]-E,K(1)/2)
    legal=[x for x in caps if not any(overlap(x[0],T) for T in (H,A,B))]
    print('order',order,'short-end P80 exact candidate/legal:',len(caps),len(legal),
          [(j,neighbor,flip) for _,j,neighbor,flip in legal])
    for C,j,neighbor,flip in legal:
        continuation=1 if same_ray(C[1]-E,B[1]-E) else 3
        assert same_ray(C[continuation]-E,B[1]-E)
        seam_length=K(1)/2
        new_length=PL[1] if continuation==1 else PL[2]
        print(' short cap',j,neighbor,flip,'native continuation side',
              1 if continuation==1 else 2,'length',AA(new_length),
              'signed excess beyond old endpoint',AA(new_length-seam_length))
        if continuation==3:
            assert AA(K(1)/2-q)>0
            assert strict_between(E,B[1],C[3])
            print('  obstruction: cap P3(130) strictly inside original P side1')
        else:
            assert strict_between(E,C[1],B[1])
            print('  obstruction: original P1(130) strictly inside cap P side1')
        print('  remaining angle: 360-180-130=50 < min native angle 80')
    assert len(legal)==2
print('STOP: neither H0 split can occur in a complete plane tiling')
