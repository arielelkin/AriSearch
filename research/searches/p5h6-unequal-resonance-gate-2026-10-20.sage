"""Exact first gates for the unequal P5/H6 seam resonance."""
from importlib.util import spec_from_file_location,module_from_spec
from itertools import product
from sage.all import AA,CyclotomicField

K=CyclotomicField(36);z=K.gen();I=z**9
u=lambda d:z**(d//10)
re=lambda w:(w+w.conjugate())/2
im=lambda w:(w-w.conjugate())/(2*I)
cr=lambda a,b:re(a)*im(b)-im(a)*re(b)
dot=lambda a,b:re(a)*re(b)+im(a)*im(b)
def solve(a,b,w):
    d=cr(a,b);assert d!=0
    return cr(w,b)/d,cr(a,w)/d
def poly(dirs,lens):
    v=[K(0)]
    for d,l in zip(dirs,lens):v.append(v[-1]+l*u(d))
    assert v[-1]==0
    v=tuple(v[:-1]);n=len(v)
    assert all(AA(l)>0 for l in lens)
    assert all(AA(cr(v[(i+1)%n]-v[i],v[(i+2)%n]-v[(i+1)%n]))>0 for i in range(n))
    return v
def overlap(A,B):
    for C in (A,B):
        for i in range(len(C)):
            x,y=C[i],C[(i+1)%len(C)]
            pa=[AA(cr(y-x,a-x)) for a in A]
            pb=[AA(cr(y-x,b-x)) for b in B]
            if max(pa)<=min(pb) or max(pb)<=min(pa):return False
    return True
def place(T,i,j,A,B,flip):
    f=lambda w:w.conjugate() if flip else w
    unit=(B-A)/(f(T[j])-f(T[i]))
    assert unit*unit.conjugate()==1
    return tuple(A+unit*(f(v)-f(T[i])) for v in T)
def same_ray(a,b):return cr(a,b)==0 and AA(dot(a,b))>0
def strict_between(A,B,X):
    direction=B-A
    return cr(direction,X-A)==0 and AA(dot(X-A,direction))>0 and AA(dot(B-X,direction))>0
def corners(T,lens,j,E,ray1,len1,ray2,len2):
    n=len(T);out=[]
    for near,target,targetlen in ((j-1,ray1,len1),(j+1,ray1,len1),
                                  (j-1,ray2,len2),(j+1,ray2,len2)):
        near%=n;other=(j+1)%n if near==(j-1)%n else (j-1)%n
        side=(j-1)%n if near==(j-1)%n else j
        for flip in (0,1):
            f=lambda w:w.conjugate() if flip else w
            unit=target*lens[side]/(targetlen*f(T[near]-T[j]))
            assert unit*unit.conjugate()==1
            V=tuple(E+unit*(f(v)-f(T[j])) for v in T)
            other_ray=ray2 if target==ray1 else ray1
            if same_ray(V[other]-E,other_ray) and V not in (x[0] for x in out):
                out.append((V,j,near,flip))
    return out

a=K(3)/2;r=K(1)/2;q=a-r
p,s=solve(u(0),u(200),-a*u(50)-q*u(150)-r*u(280))
L=p+q
c,e=solve(u(180),u(280),-L-u(50)-u(100)-r*u(230))
PL=(p,a,q,s,r);HL=(L,K(1),K(1),c,r,e)
P=poly((0,50,150,200,280),PL)
H=poly((0,50,100,180,230,280),HL)
assert len(set((p,a,q,s,r,L,c,e)))==8
print('p,a,q,s,r,L,c,e:',[AA(x) for x in (p,a,q,s,r,L,c,e)])
print('Exact closure, positive sides, strict convexity: PASS')

# All 15 Rao families and 10 dihedral relabelings, using reviewed table.
spec=spec_from_file_location('rao','research/searches/convex-substitution-shapes.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
angles=(100,130,80,130,100);hits=[]
for typ,(aeqs,leqs) in mod.RAO.items():
    for sign in (1,-1):
        for off in range(5):
            amap=[(off+sign*i)%5 for i in range(5)]
            if not all(sum(coef*angles[j] for coef,j in zip(row,amap))==36*target
                       for row,target in aeqs):continue
            smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
            if all(sum((coef*PL[j] for coef,j in zip(row,smap)),K(0))==0
                   for row in leqs):hits.append((typ,sign,off))
assert not hits
print('Rao P-only family hits:',hits)

# H-only: every corner angle is 100 or 130. A T-junction cannot use two H
# corners (100+100>180), and a full vertex containing H0=100 needs two 130s.
Hangles=(100,130,130,100,130,130)
Hcorners=[(HL[(i-1)%6],HL[i]) for i in range(6)]
bridges=[]
for i in (1,2,4,5):
    for j in (1,2,4,5):
        for ai,bi in (Hcorners[i],Hcorners[i][::-1]):
            for aj,bj in (Hcorners[j],Hcorners[j][::-1]):
                if ai==e and bi==aj and bj==L:bridges.append((i,j))
assert not bridges
print('H-only H0 length-bridge completions:',bridges)

# Both whole-side H/H orientations remain actual local competitors to the
# proposed split; this is only a two-tile contact, not a periodic carrier.
whole=[]
for reverse,flip in product((0,1),repeat=2):
    T=place(H,1,0,K(0),L,flip) if reverse else place(H,0,1,K(0),L,flip)
    if not overlap(H,T):whole.append((reverse,flip))
print('Whole H0/H0 nonoverlap maps of four:',whole)
assert len(whole)==2
def full_corner_options(E,ray1,len1,ray2,len2,angle,existing):
    choices=[]
    for typ,T,lens,word in (('P',P,PL,(100,130,80,130,100)),
                            ('H',H,HL,(100,130,130,100,130,130))):
        for j in range(len(T)):
            if word[j]!=angle:continue
            for V,j0,near,flip in corners(T,lens,j,E,ray1,len1,ray2,len2):
                if not any(overlap(V,U) for U in existing):
                    choices.append((typ,j0,near,flip,V))
    return choices

mirror=place(H,0,1,K(0),L,1)
halfturn=place(H,1,0,K(0),L,0)
for name,T in (('mirror',mirror),('halfturn',halfturn)):
    if name=='halfturn':
        left=full_corner_options(H[0],H[5]-H[0],e,T[2]-T[1],K(1),130,(H,T))
        right=full_corner_options(H[1],H[2]-H[1],K(1),T[5]-T[0],e,130,(H,T))
        print('Whole H/H halfturn endpoint 130 caps left/right:',len(left),len(right))
    else:
        right=full_corner_options(H[1],H[2]-H[1],K(1),T[2]-T[1],K(1),100,(H,T))
        print('Whole H/H mirror right 100 caps:',len(right))
        # Left 160-degree gap can only consist of two P80 corners.
        E=H[0]
        def one_ray(target,target_length):
            out=[]
            for near in (1,3):
                other=3 if near==1 else 1
                side_length=a if near==1 else q
                for flip in (0,1):
                    f=lambda w:w.conjugate() if flip else w
                    unit=target*side_length/(target_length*f(P[near]-P[2]))
                    V=tuple(E+unit*(f(v)-f(P[2])) for v in P)
                    out.append((V,near,flip,V[other]-E))
            return out
        double=[]
        for C,nc,fc,rayc in one_ray(H[5]-E,e):
            for D,nd,fd,rayd in one_ray(T[5]-E,e):
                if same_ray(rayc,rayd) and not any(overlap(V,U)
                    for V,U in ((C,H),(C,T),(D,H),(D,T),(C,D))):
                    double.append((nc,fc,nd,fd,C,D))
        print('Whole H/H mirror left two-P80 caps of 16:',len(double),
              [entry[:4] for entry in double])
        for nc,fc,nd,fd,C,D in double:
            if nc!=nd:
                short=C[3] if nc==1 else D[3]
                long_end=D[1] if nd==3 else C[1]
                assert strict_between(E,long_end,short)
                print(' mirror unequal internal sides: 130-degree short endpoint, 50-degree gap')
            else:
                next_vertex=3 if nc==1 else 1
                F=C[next_vertex]
                assert F==D[next_vertex]
                other=4 if next_vertex==3 else 0
                other_len=s if next_vertex==3 else p
                next_caps=full_corner_options(F,C[other]-F,other_len,
                                              D[other]-F,other_len,100,(H,T,C,D))
                print(' mirror equal internal sides length',AA(q if nc==1 else a),
                      'next 130+130 100-gap caps:',len(next_caps))

# Named P0(p)+P2(q) split of H0; all side directions and chiralities.
split=[]
for order in (0,1):
    parts=((0,1,0,p),(2,3,p,L)) if order==0 else ((2,3,0,q),(0,1,q,L))
    for rev0,rev1,flip0,flip1 in product((0,1),repeat=4):
        guests=[]
        for (i,j,A,B),rev,flip in zip(parts,(rev0,rev1),(flip0,flip1)):
            guests.append(place(P,j,i,A,B,flip) if rev else place(P,i,j,A,B,flip))
        X,Y=guests
        if not any((overlap(H,X),overlap(H,Y),overlap(X,Y))):
            split.append((order,rev0,rev1,flip0,flip1,X,Y))
assert len(split)==2
print('Nonoverlap P0/P2 split placements of 32:',len(split))

for order,rev0,rev1,flip0,flip1,X,Y in split:
    A=X if order==0 else Y  # P side0; short seam P4 length r
    B=Y if order==0 else X  # P side2; long seam P1 length a
    M=p if order==0 else q
    assert A[0]==B[2]==M
    E=A[4]
    assert E==M+(B[1]-M)*r/a
    assert B[1]-E == (B[1]-M)*(q/a)
    caps=[item for item in corners(P,PL,2,E,A[3]-E,s,B[1]-E,q)
          if not any(overlap(item[0],T) for T in (H,A,B))]
    print('order',order,'legal short P80 caps:',[(j,n,f) for _,j,n,f in caps])
    assert len(caps)==2
    closing=[]
    for C,j,n,f in caps:
        if C[3]==B[1]:
            closing.append((C,j,n,f))
        else:
            assert same_ray(C[1]-E,B[1]-E)
            assert AA(dot(C[1]-B[1],B[1]-E))>0
    assert len(closing)==1
    C,j,n,f=closing[0]
    F=B[1]
    assert C[3]==F
    # Two 130-degree vertices meet at F, leaving a 100-degree sector.
    candidates=[]
    for typ,T,lens,slots in (('P',P,PL,(0,4)),('H',H,HL,(0,3))):
        for vertex in slots:
            for V,j0,near,flip in corners(T,lens,vertex,F,B[0]-F,p,C[4]-F,s):
                if not any(overlap(V,U) for U in (H,A,B,C)):
                    candidates.append((typ,vertex,near,flip,V))
    print('order',order,'closed F P130+P130 100-gap full-corner candidates:',
          [(typ,j0,near,flip) for typ,j0,near,flip,_ in candidates])

print('First-corner counts only; the separate resonant-escape-attack replay kills all F caps')
