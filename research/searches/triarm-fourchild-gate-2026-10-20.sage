"""Exact scalar and convexity gate for radial tH=3P, tP=3P+H."""
from sage.all import *
from itertools import combinations

Qz = PolynomialRing(QQ, 'z'); z = Qz.gen()
K = NumberField(z**4 - 3*z**2 - 3, 't', embedding=1.95); t = K.gen()
assert t > 0 and t**4 == 3*t*t + 3
counts = [(i,j,k) for i in range(4) for j in range(4-i) for k in range(4-i-j)]
assert len(counts) == 20
eq = {}
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
    assert len(rows)==60
    eq[target]=rows

def solve(e,f):
    u,v,w=e; U,V,W=f
    d=v*W-V*w
    if not d: return None
    return ((-u*W+U*w)/d,(-v*U+V*u)/d)

def feasible(a,b):
    a,b=AA(a),AA(b); q=AA(3).sqrt()
    return a>0 and b>0 and a+b>=q and abs(a-b)<=q

def normalize(e):
    q=next(c for c in e if c)
    return tuple(c/q for c in e)

common_lines=set(normalize(e) for e,d in eq['one']).intersection(
    normalize(e) for e,d in eq['a']).intersection(normalize(e) for e,d in eq['b'])
assert not common_lines
assert all(any(e) for target in eq for e,d in eq[target])
metrics=set()
for pair in combinations(eq,2):
    third=next(q for q in eq if q not in pair)
    for e,_ in eq[pair[0]]:
        for f,_ in eq[pair[1]]:
            ab=solve(e,f)
            if ab is None or not feasible(*ab): continue
            a,b=ab
            if any(u+v*a+w*b==0 for (u,v,w),_ in eq[third]): metrics.add(ab)
print('isolated scalar metrics:',len(metrics))
assert metrics=={(-t**3+4*t,t**3-3*t),
                 ((t**3-t)/5,3*(t*t-1)/5),
                 (t**3-3*t,t*t-3),
                 (t,t**3-3*t),
                 (t**3/3,t*t)}

q3=AA(3).sqrt()
R=lambda p:(-p[0]/2-q3*p[1]/2,q3*p[0]/2-p[1]/2)
add=lambda p,q:(p[0]+q[0],p[1]+q[1])
sub=lambda p,q:(p[0]-q[0],p[1]-q[1])
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
def convex(poly):
    return all(cross(sub(poly[(i+1)%len(poly)],poly[i]),
                     sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))>0
               for i in range(len(poly)))

convex_metrics=[]
for a,b in sorted(metrics,key=lambda ab:(float(AA(ab[0])),float(AA(ab[1])))):
    ar,br=AA(a),AA(b)
    y=(ar*ar+3-br*br)/(2*q3); x2=ar*ar-y*y
    branches=[]
    for sign in ((1,) if x2==0 else (-1,1)):
        v=(sign*x2.sqrt(),y)
        O=(AA(0),AA(0)); S=(AA(1),AA(0)); T=R(S)
        V=add(S,v); W=sub(T,R(v))
        P=[O,S,V,W,T]
        G=[V,W,R(V),R(W),R(R(V)),R(R(W))]
        turnsP=[cross(sub(P[(i+1)%5],P[i]),sub(P[(i+2)%5],P[(i+1)%5])) for i in range(5)]
        turnsG=[cross(sub(G[(i+1)%6],G[i]),sub(G[(i+2)%6],G[(i+1)%6])) for i in range(6)]
        print('CANDIDATE',a,b,'sign',sign,'turnsP', [float(q) for q in turnsP], 'turnsG',[float(q) for q in turnsG])
        if convex(P) and convex(G): branches.append(sign)
    if branches: convex_metrics.append((a,b,branches))
print('strictly convex metrics:',len(convex_metrics))
assert not convex_metrics
for a,b,branches in convex_metrics:
    print('METRIC',a,b,'approx',float(AA(a)),float(AA(b)),'branches',branches)
    for target in eq:
        words=[d for (u,v,w),d in eq[target] if u+v*a+w*b==0]
        print(' ',target,words)
