"""Exact necessary boundary-length gate for the direct three-arm P/H dissection.

Run: mise exec -- conda run --no-capture-output -n arisearch sage research/searches/triarm-metric-compatibility-gate-2026-10-20.sage
"""
from sage.all import *
from itertools import combinations, product

Qx = PolynomialRing(QQ, 'x')
x = Qx.gen()
K = NumberField(x**4 - 4*x**2 - 3, 't', embedding=2.15)
t = K.gen()
assert AA(t) > 2 and AA(t) < 3

# Each equation has form c0 + ca*a + cb*b = 0. A convex child can
# contribute at most one side to a straight parent edge. This enlarged
# domain even permits any choice of four P sides and one H side per edge.
counts = [(i,j,k) for i in range(5) for j in range(5-i)
          for k in range(5-i-j)]
assert len(counts) == 35
equations = {}
for target in ('one', 'a', 'b'):
    rows = []
    for i,j,k in counts:
        for h in ('none', 'b/t', '2a/t'):
            c0,ca,cb = K(i),K(j),K(k)
            if h == 'b/t': cb += 1/t
            elif h == '2a/t': ca += 2/t
            if target == 'one': c0 -= t
            elif target == 'a': ca -= t
            else: cb -= t
            rows.append(((c0,ca,cb),(i,j,k,h)))
    equations[target] = rows
    assert len(rows) == 105

def root_of_two(e,f):
    (u,v,w), (U,V,W) = e,f
    det = v*W - V*w
    if not det: return None
    a = (-u*W + U*w)/det
    b = (-v*U + V*u)/det
    return (a,b)

def positive(z):
    return AA(z) > 0

def feasible_metric(a,b):
    # Circle intersection: b=|v-i*sqrt(3)|, a=|v|.
    # Include collinear circle intersections (one branch) as well.
    return (AA(a+b) >= AA(3).sqrt() and
            AA(a-b).abs() <= AA(3).sqrt())

all_metrics = set()
for t1,t2 in combinations(('one','a','b'),2):
    t3 = next(q for q in ('one','a','b') if q not in (t1,t2))
    by_solution = {}
    for e,d in equations[t1]:
        for f,D in equations[t2]:
            z = root_of_two(e,f)
            if z is None: continue
            a,b = z
            if not (positive(a) and positive(b)): continue
            if not feasible_metric(a,b): continue
            matches = [F for g,F in equations[t3] if g[0]+g[1]*a+g[2]*b == 0]
            if matches:
                by_solution.setdefault(z,[]).append((d,D,matches))
    print('pair',t1,t2,'complete positive circle-feasible metrics:',len(by_solution))
    all_metrics.update(by_solution)
    for (a,b),cert in by_solution.items():
        print(' a=',a,'b=',b,'approx=',a.n(),b.n(),'cert=',cert[:2])

# Rank-deficient systems may have a one-dimensional metric family; list
# coefficient-proportional rows and test the remaining target independently.
for target in ('one','a','b'):
    print('zero rows',target,[d for e,d in equations[target] if e==(0,0,0)])

def line_key(e):
    z = next(c for c in e if c)
    return tuple(c/z for c in e)
line_sets = []
for target in ('one','a','b'):
    line_sets.append(set(line_key(e) for e,d in equations[target]))
print('rank-one metric lines common to all three edge targets:',
      line_sets[0] & line_sets[1] & line_sets[2])

sqrt3 = AA(3).sqrt()
R = lambda p: (-p[0]/2-sqrt3*p[1]/2, sqrt3*p[0]/2-p[1]/2)
add = lambda p,q: (p[0]+q[0],p[1]+q[1])
sub = lambda p,q: (p[0]-q[0],p[1]-q[1])
cross = lambda p,q: p[0]*q[1]-p[1]*q[0]
def convex(poly):
    c=[cross(sub(poly[(i+1)%len(poly)],poly[i]),
             sub(poly[(i+2)%len(poly)],poly[(i+1)%len(poly)]))
       for i in range(len(poly))]
    return all(z>0 for z in c),[z.n(digits=6) for z in c]

zeta = QQbar.zeta(360)
def cos_degree(d):
    return AA((zeta**d+zeta**(-d))/2)
def cosine_at(poly,i):
    u=sub(poly[(i-1)%len(poly)],poly[i]);w=sub(poly[(i+1)%len(poly)],poly[i])
    return (u[0]*w[0]+u[1]*w[1]) / (
        (u[0]**2+u[1]**2).sqrt()*(w[0]**2+w[1]**2).sqrt())
def exact_angle_bin(c):
    if c==cos_degree(120): return '120'
    for lo,hi in ((57,59),(64,70),(121,123),(170,176)):
        if cos_degree(hi)<c<cos_degree(lo): return '(%s,%s)'%(lo,hi)
    raise AssertionError('angle outside certified bins')

for a,b in sorted(all_metrics,key=lambda z:float(AA(z[0]))):
    ar,br=AA(a),AA(b)
    y=(ar**2+3-br**2)/(2*sqrt3)
    xx=ar**2-y**2
    print('METRIC',a,b,'x2=',xx.n())
    for sign in (-1,1):
        v=(sign*xx.sqrt(),y)
        O=(AA(0),AA(0)); S=(AA(1),AA(0)); T=R(S)
        V=add(S,v);W=sub(T,R(v))
        P=[O,S,V,W,T]
        G=[V,W,R(V),R(W),R(R(V)),R(R(W))]
        pc,pturn=convex(P);gc,gturn=convex(G)
        print(' branch',sign,'v=',tuple(z.n(digits=8) for z in v),
              'Pconvex=',pc,'Gconvex=',gc,
              'Pturns=',pturn,'Gturns=',gturn)
        if pc and gc:
            binsP=[exact_angle_bin(cosine_at(P,i)) for i in range(5)]
            binsH=[exact_angle_bin(cosine_at(G,i)) for i in range(6)]
            print('  EXACT ANGLE BINS',binsP,binsH)
            assert binsP.count('120')==1 and '120' not in binsH
            assert binsP[0]=='120'
            # No sum of >=2 available corner angles equals 120: two
            # smallest are <118, one smallest plus any other is >121,
            # and three smallest exceed 171. Thus O has one P corner.
            def angles(poly):
                ans=[]
                for i in range(len(poly)):
                    u=sub(poly[(i-1)%len(poly)],poly[i]);w=sub(poly[(i+1)%len(poly)],poly[i])
                    cosine=(u[0]*w[0]+u[1]*w[1]) / (
                        (u[0]**2+u[1]**2).sqrt()*(w[0]**2+w[1]**2).sqrt())
                    ans.append(float(acos(float(cosine))*180/pi))
                return ans
            print('  P angles',angles(P),'H angles',angles(G))
            for target in ('one','a','b'):
                print('  boundary',target,[d for e,d in equations[target]
                      if e[0]+e[1]*a+e[2]*b==0])
            unit_options=[d for e,d in equations['one']
                          if e[0]+e[1]*a+e[2]*b==0]
            assert unit_options and all(d[0]==0 for d in unit_options)
            print('  CERTIFIED O-CORNER OBSTRUCTION: P at O forces length 1'
                  ' side on each parent unit edge; no unit-edge equation'
                  ' permits a length 1 side.')
