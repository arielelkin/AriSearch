"""Exact boundary gate for tH=3P, tP=2P+H; run with sage under arisearch."""
from sage.all import *
from itertools import combinations

Qx=PolynomialRing(QQ,'x'); x=Qx.gen()
K=NumberField(x*x-3,'t',embedding=1.73); t=K.gen()
assert t>0 and t*t==3
counts=[(i,j,k) for i in range(3) for j in range(3-i) for k in range(3-i-j)]
assert len(counts)==10
eq={}
for target in ('one','a','b'):
    rows=[]
    for i,j,k in counts:
        for h in ('none','b/t','2a/t'):
            c0,ca,cb=K(i),K(j),K(k)
            if h=='b/t': cb+=1/t
            if h=='2a/t': ca+=2/t
            if target=='one': c0-=t
            elif target=='a': ca-=t
            else: cb-=t
            rows.append(((c0,ca,cb),(i,j,k,h)))
    assert len(rows)==30
    eq[target]=rows

def solve(e,f):
    u,v,w=e; U,V,W=f
    d=v*W-V*w
    if not d: return None
    return ((-u*W+U*w)/d,(-v*U+V*u)/d)

def good(a,b):
    a,b=AA(a),AA(b)
    return a>0 and b>0 and a+b>=AA(3).sqrt() and abs(a-b)<=AA(3).sqrt()

def key(e):
    z=next(c for c in e if c)
    return tuple(c/z for c in e)

for target in eq:
    assert not any(e==(0,0,0) for e,d in eq[target])
assert not set(key(e) for e,d in eq['one']).intersection(
    key(e) for e,d in eq['a']).intersection(key(e) for e,d in eq['b'])

metrics=set()
for q,r in combinations(eq,2):
    s=next(z for z in eq if z not in (q,r))
    for e,d in eq[q]:
        for f,D in eq[r]:
            ab=solve(e,f)
            if ab is None or not good(*ab): continue
            a,b=ab
            if any(u+v*a+w*b==0 for (u,v,w),_ in eq[s]):
                metrics.add(ab)
print('scalar metric candidates',len(metrics))

root3=AA(3).sqrt()
R=lambda p:(-p[0]/2-root3*p[1]/2,root3*p[0]/2-p[1]/2)
add=lambda p,q:(p[0]+q[0],p[1]+q[1])
sub=lambda p,q:(p[0]-q[0],p[1]-q[1])
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
def convex(poly):
    return all(cross(sub(poly[(i+1)%len(poly)],poly[i]),sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))>0 for i in range(len(poly)))

convex_metrics=[]
for a,b in sorted(metrics,key=lambda ab:(float(AA(ab[0])),float(AA(ab[1])))):
    ar,br=AA(a),AA(b)
    y=(ar*ar+3-br*br)/(2*root3); x2=ar*ar-y*y
    branches=[]
    for sign in ((1,) if x2==0 else (-1,1)):
        xx=sign*x2.sqrt(); v=(xx,y)
        O=(AA(0),AA(0)); S=(AA(1),AA(0)); T=R(S)
        V=add(S,v);W=sub(T,R(v))
        P=[O,S,V,W,T]
        G=[V,W,R(V),R(W),R(R(V)),R(R(W))]
        if convex(P) and convex(G): branches.append(sign)
    print('metric',a,b,'approx',ar.n(digits=10),br.n(digits=10),'convex branches',branches)
    if branches: convex_metrics.append((a,b,branches))
print('convex metrics',len(convex_metrics))
assert len(convex_metrics)==9
vertical=[]; nonvertical=[]
for a,b,branches in convex_metrics:
    ar,br=AA(a),AA(b)
    y=(ar*ar+3-br*br)/(2*root3); x2=ar*ar-y*y
    v=(x2.sqrt(),y); O=(AA(0),AA(0)); S=(AA(1),AA(0));T=R(S)
    V=add(S,v);W=sub(T,R(v))
    P=[O,S,V,W,T];G=[V,W,R(V),R(W),R(R(V)),R(R(W))]
    def angles(poly):
        ans=[]
        for i in range(len(poly)):
            u=sub(poly[(i-1)%len(poly)],poly[i]); w=sub(poly[(i+1)%len(poly)],poly[i])
            c=(u[0]*w[0]+u[1]*w[1])/((u[0]**2+u[1]**2).sqrt()*(w[0]**2+w[1]**2).sqrt())
            ans.append(float(acos(float(c))*180/pi))
        return ans
    def cosine(poly,i):
        u=sub(poly[(i-1)%len(poly)],poly[i]);w=sub(poly[(i+1)%len(poly)],poly[i])
        return (u[0]*w[0]+u[1]*w[1])/((u[0]**2+u[1]**2).sqrt()*(w[0]**2+w[1]**2).sqrt())
    if x2==0:
        vertical.append((a,b))
        assert [cosine(P,i) for i in range(5)]==[AA(-1)/2,AA(0),AA(-1)/2,AA(-1)/2,AA(0)]
        assert all(cosine(G,i)==AA(-1)/2 for i in range(6))
    else:
        nonvertical.append((a,b))
        for sign in branches:
            vv=(sign*x2.sqrt(),y);VV=add(S,vv);WW=sub(T,R(vv))
            PP=[O,S,VV,WW,T]
            GG=[VV,WW,R(VV),R(WW),R(R(VV)),R(R(WW))]
            assert all(cosine(PP,i)<AA(1)/2 for i in range(5))
            assert all(cosine(GG,i)<AA(1)/2 for i in range(6))
            assert [i for i in range(5) if cosine(PP,i)==AA(-1)/2]==[0]
            assert all(cosine(GG,i)!=AA(-1)/2 for i in range(6))
    print('angles',angles(P),angles(G))
    for target in eq:
        print('boundary',target,[d for (u,v,w),d in eq[target] if u+v*a+w*b==0])
    unit=[d for (u,v,w),d in eq['one'] if u+v*a+w*b==0]
    # Preserve native side identities, including coincident numerical labels.
    # A row has one choice from each of the two P children and H.
    Plens=[K(1),a,b,a,K(1)]
    Hlens=[b/t,2*a/t,b/t,2*a/t,b/t,2*a/t]
    lens={(child,i):(Plens if child<2 else Hlens)[i]
          for child in range(3) for i in range(5 if child<2 else 6)}
    choices=[[(child,i) for i in range(5 if child<2 else 6)]
             for child in range(3)]
    from itertools import product
    edgeopts=[]
    for target in (K(1),a,b,a,K(1)):
        options=[]
        for selected in product(*[[None]+q for q in choices]):
            sides=tuple(q for q in selected if q is not None)
            if sides and sum((lens[q] for q in sides),K(0))==t*target:
                options.append(sides)
        edgeopts.append(options)
    print('native edge option counts',[len(q) for q in edgeopts])
    P120=[i for i in range(5) if cosine(P,i)==AA(-1)/2]
    H120=[i for i in range(6) if cosine(G,i)==AA(-1)/2]
    print('120 child vertices',P120,H120)
    Oposs=[]
    for child in range(3):
        for vi in (P120 if child<2 else H120):
            incoming=(child,(vi-1)%(5 if child<2 else 6))
            outgoing=(child,vi)
            for s0,s4 in ((incoming,outgoing),(outgoing,incoming)):
                if any(s0 in opt for opt in edgeopts[0]) and any(s4 in opt for opt in edgeopts[4]):
                    Oposs.append((child,vi,s0,s4))
    print('O native corner possibilities',Oposs)
    def find_assignment(eidx,used,chosen,Ocorner):
        if eidx==5:
            yield tuple(chosen)
            return
        for opt in edgeopts[eidx]:
            if any(q in used for q in opt): continue
            if eidx==0 and Ocorner[2] not in opt: continue
            if eidx==4 and Ocorner[3] not in opt: continue
            yield from find_assignment(eidx+1,used.union(opt),chosen+[opt],Ocorner)
    assignments=[]
    for c in Oposs:
        assignments.extend((c,z) for z in find_assignment(0,set(),[],c))
    patterns=set(tuple(tuple(q[1] for q in edge if q[0]==2) for edge in z)
                 for c,z in assignments)
    print('O-plus-global-side-budget assignments',len(assignments),'H edge patterns',sorted(patterns))
    if (a,b)==(t/3,2*t/3):
        assert len(assignments)==128 and patterns=={((),(),(),(),())}
        print('PLACEMENT OBSTRUCTION: H has no boundary side. Two convex P children cannot enclose H: from an interior H point, each P subtends an angular interval strictly shorter than 180 degrees.')
    elif (a,b)==((3-t)/2,(3*t-3)/2):
        assert len(assignments)==576
        assert all(len(p[0])==len(p[2])==len(p[4])==1 and
                   not p[1] and not p[3] and
                   all(p[i][0]%2==1 for i in (0,4)) for p in patterns)
        print('PLACEMENT OBSTRUCTION: both parent unit edges require H long sides; parent oriented directions differ 60 degrees, while H long-side directions differ 120 degrees.')
    elif (a,b)==(t/2,t/2):
        assert len(assignments)==6912
        assert all(not p[0] and not p[4] and
                   all(len(p[i])==1 and p[i][0]%2==0 for i in (1,2,3))
                   for p in patterns)
        print('PLACEMENT OBSTRUCTION: middle three parent edges require H short sides; parent oriented directions turn 60 degrees each, while H short-side directions differ 120 degrees.')
    else:
        assert not assignments
        print('BOUNDARY INVENTORY OBSTRUCTION: no native-side assignment across five parent edges and O corner.')
assert len(vertical)==6 and len(nonvertical)==3
print('INTERNALLY CHECKED: no strictly convex metric passes the boundary placement gate')
