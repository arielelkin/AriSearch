"""Hostile exact next-endpoint and H0 cover checks for q=1 resonance."""
from itertools import product
from sage.all import AA, CyclotomicField
from importlib.util import spec_from_file_location,module_from_spec
K=CyclotomicField(36); z=K.gen(); I=z**9
def u(d): return z**(d//10)
def re(w):return (w+w.conjugate())/2
def im(w):return (w-w.conjugate())/(2*I)
def cross(a,b):return re(a)*im(b)-im(a)*re(b)
def dot(a,b):return re(a)*re(b)+im(a)*im(b)
def solve(a,b,w):
    den=cross(a,b)
    assert den!=0
    return cross(w,b)/den,cross(a,w)/den
def polygon(ds,ls):
    V=[K(0)]
    for d,l in zip(ds,ls):V.append(V[-1]+l*u(d))
    assert V[-1]==0
    V=tuple(V[:-1]);n=len(V)
    assert all(AA(l)>0 for l in ls)
    assert all(AA(cross(V[(i+1)%n]-V[i],V[(i+2)%n]-V[(i+1)%n]))>0 for i in range(n))
    return V
def overlap(A,B):
    for C in (A,B):
        for x,y in zip(C,C[1:]+C[:1]):
            pa=[AA(cross(y-x,a-x)) for a in A]
            pb=[AA(cross(y-x,b-x)) for b in B]
            if max(pa)<=min(pb) or max(pb)<=min(pa):return False
    return True
def place(V,i,j,A,B,flip):
    f=lambda w:w.conjugate() if flip else w
    unit=(B-A)/(f(V[j])-f(V[i]))
    assert unit*unit.conjugate()==1
    return tuple(A+unit*(f(w)-f(V[i])) for w in V)
def same_ray(a,b):return cross(a,b)==0 and AA(dot(a,b))>0

a=K(3)/2;q=K(1);r=K(1)/2
p,s=solve(u(0),u(200),-a*u(50)-q*u(150)-r*u(280))
L=p+q
c,e=solve(u(180),u(280),-L-u(50)-u(100)-r*u(230))
PL=(p,a,q,s,r); HL=(L,K(1),K(1),c,r,e)
P=polygon((0,50,150,200,280),PL)
H=polygon((0,50,100,180,230,280),HL)
assert q==a-r and AA(p)>1 and AA(s)>3 and AA(c)>AA(L)
assert AA(e)>1 and AA(e)<AA(a)
print('p,s,L,c,e:',*[AA(x) for x in (p,s,L,c,e)])

# Named P0+P2 split. Independently enumerate its two orders, side
# directions and reflection flags, checking exact strict interior overlap.
splits=[]
for order in (0,1):
    parts=((0,1,0,p),(2,3,p,L)) if order==0 else ((2,3,0,q),(0,1,q,L))
    for rev0,rev1,flip0,flip1 in product((0,1),repeat=4):
        copies=[]
        for (i,j,A,B),rev,flip in zip(parts,(rev0,rev1),(flip0,flip1)):
            copies.append(place(P,j,i,A,B,flip) if rev else place(P,i,j,A,B,flip))
        X,Y=copies
        if overlap(H,X) or overlap(H,Y) or overlap(X,Y):continue
        splits.append((order,X,Y))
print('nonoverlapping named split placements:',len(splits))
assert len(splits)==2
assert sorted(order for order,_,_ in splits)==[0,1]

# Simpler exact corner mapper: normalize by known target ray length.
def cap_images(V,lens,j,E,rayA,lenA,rayB):
    out=[];n=len(V)
    for neighbor in ((j-1)%n,(j+1)%n):
        other=(j+1)%n if neighbor==(j-1)%n else (j-1)%n
        side=(j-1)%n if neighbor==(j-1)%n else j
        for flip in (0,1):
            f=lambda w:w.conjugate() if flip else w
            unit=rayA*lens[side]/(lenA*f(V[neighbor]-V[j]))
            assert unit*unit.conjugate()==1
            C=tuple(E+unit*(f(w)-f(V[j])) for w in V)
            if same_ray(C[other]-E,rayB) and C not in out:out.append(C)
    return out

for order,X,Y in splits:
    A=X if order==0 else Y    # P0 host segment, P4 short edge
    B=Y if order==0 else X    # P2 host segment, P1 long edge
    E=A[4]; F=B[1]
    assert E==B[2]+(F-B[2])*r/a
    assert (F-E)*(F-E).conjugate()==q*q
    caps=cap_images(P,PL,2,E,A[3]-E,s,F-E)
    legal=[C for C in caps if not any(overlap(C,T) for T in (H,A,B))]
    resonant=[C for C in legal if C[3]==F]
    print('order',order,'P80 caps total/legal/resonant:',len(caps),len(legal),len(resonant))
    assert len(resonant)==1
    C=resonant[0]
    assert C[3]==B[1]
    # Native 130+130 at F leaves a single 100-degree cap.  The two
    # exposed rays go toward B vertex0 along P0 and C vertex4 along P3.
    gap_caps=[]
    for species,V,lens,angles in (
        ('P',P,PL,(100,130,80,130,100)),
        ('H',H,HL,(100,130,130,100,130,130))):
        for j in range(len(V)):
            if angles[j]!=100:continue
            for D in cap_images(V,lens,j,F,B[0]-F,p,C[4]-F):
                if any(overlap(D,T) for T in (H,A,B,C)):continue
                gap_caps.append((species,j,D))
            for D in cap_images(V,lens,j,F,C[4]-F,s,B[0]-F):
                if any(overlap(D,T) for T in (H,A,B,C)):continue
                if (species,j,D) not in gap_caps:gap_caps.append((species,j,D))
    print('order',order,'F 100-degree nonoverlap cap germs:',
          [(species,j) for species,j,_ in gap_caps])
    next_ok=[]; next_bad=[]
    for species,j,D in gap_caps:
        ls=PL if species=='P' else HL
        ang=(100,130,80,130,100) if species=='P' else (100,130,130,100,130,130)
        n=len(D)
        endpoint_data=[]
        for neighbor in ((j-1)%n,(j+1)%n):
            side=(j-1)%n if neighbor==(j-1)%n else j
            ray=D[neighbor]-F
            target=p if same_ray(ray,B[0]-F) else s
            old_far_angle=100  # B vertex0 or C vertex4
            assert same_ray(ray,B[0]-F) or same_ray(ray,C[4]-F)
            if AA(ls[side])<AA(target):
                residual=180-ang[neighbor]
                remainder=target-ls[side]
            elif AA(ls[side])>AA(target):
                residual=180-old_far_angle
                remainder=ls[side]-target
            else:residual=0;remainder=K(0)
            endpoint_data.append((side,neighbor,residual,remainder))
        record=(species,j,tuple(endpoint_data))
        (next_bad if any(t[2]==50 for t in endpoint_data) else next_ok).append(record)
    print('order',order,'F caps immediate 50-gap bad/survive:',len(next_bad),len(next_ok))
    print('surviving F cap germs:',
          [(species,j,tuple((side,neighbor,residual,AA(rem))
                            for side,neighbor,residual,rem in data))
           for species,j,data in next_ok])
    assert len(gap_caps)==8 and len(next_ok)==3 and len(next_bad)==5
    # Each residual 80 at a T must be P vertex2.  Its two incident side
    # lengths are q=1 and a=3/2, and both far vertices have angle130.
    # If the remaining straight ray is shorter than q or longer than a,
    # either choice creates a 50-degree T at the next endpoint.
    for species,j,data in next_ok:
        remainders=[rem for side,neighbor,residual,rem in data if residual==80]
        assert remainders
        assert all(AA(rem)<AA(q) or AA(rem)>AA(a) for rem in remainders)
    assert AA(s-r)>AA(a) and AA(s-p)<AA(q) and AA(p-r)>AA(a)
    print('order',order,'all three surviving F caps fail at forced P80 next T')

# Whole-side H0/H0 mirror case still has both H1=1 rays at the 130 endpoint.
# Every native 100-degree corner has an incident side >1, hence a 50 gap.
corner100=((r,p),(s,r),(e,L),(K(1),c))
assert all(any(AA(v)>1 for v in pair) for pair in corner100)
print('H0/H0 mirror excluded by 50-degree endpoint gap')

angles={'P':(100,130,80,130,100),'H':(100,130,130,100,130,130)}
lens={'P':PL,'H':HL}
halfturn=[]
for typ in ('P','H'):
    ang=angles[typ]; ls=lens[typ];n=len(ls)
    for v in range(n):
        if ang[v]!=130:continue
        incident=((v-1)%n,v)
        for along_one,along_e in (incident,incident[::-1]):
            def far(side): return (v-1)%n if side==(v-1)%n else (v+1)%n
            x,y=ls[along_one],ls[along_e]
            if AA(x)>1 or AA(y)>AA(e):continue
            if AA(x)<1 and ang[far(along_one)]>100:continue
            if AA(y)<AA(e) and ang[far(along_e)]>100:continue
            halfturn.append((typ,v,along_one,along_e))
assert halfturn==[('H',2,1,2)]
# Its H2=1 side terminates at H vertex3=100 inside H5.  At that T,
# P80 must follow remaining H5 of length e-1<q=1 (and <a=3/2),
# so the H130 terminal vertex lies inside the P side: 50 gap.
assert AA(e-1)>0 and AA(e-1)<AA(q)<AA(a)
print('H0/H0 halfturn sole cap',halfturn,'fails at next H5 endpoint')

# H3 is the sole native side longer than H0.  A full cover can only align
# H0 vertex1 (130 degrees) to one H3 endpoint.  At H0 vertex0 the T gap
# forces P80.  One incident side q ends before H5 (P130 inside flat H5),
# the other a overruns H5 (H130 inside flat P1).  Either leaves 50 degrees.
assert AA(c)>AA(L)
assert AA(a)>AA(e) and AA(q)<AA(e)
print('H3 full H0 cover excluded by either P80 side against H5')

# Conditional P-only omission screen using the repository's reviewed Rao
# table; no hit is not an independent classification proof.
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
Pang=(100,130,80,130,100);hits=[]
for typ,(aeqs,leqs) in mod.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            word=[Pang[(off+sign*i)%5] for i in range(5)]
            if not all(sum(co*x for co,x in zip(row,word))==36*target for row,target in aeqs):continue
            side=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
            if all(sum((co*PL[j] for co,j in zip(row,side)),K(0))==0 for row in leqs):
                hits.append((typ,sign,off))
assert hits==[]
print('P-only Rao hits: none (conditional on imported classification)')
