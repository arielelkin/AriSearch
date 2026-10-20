"""Exact coordinate/incidence audit of the Method 3 t=3/5 fixture."""
import sympy as s

def simp(x):
    return s.simplify(s.expand_trig(x))
def sub(a,b):
    return tuple(simp(x-y) for x,y in zip(a,b))
def cross(a,b):
    return simp(a[0]*b[1]-a[1]*b[0])
def dot(a,b):
    return simp(a[0]*b[0]+a[1]*b[1])
X={1:(s.S.Zero,s.S.Zero)}
for i,d in enumerate([60,120,210,270,180,240,330,270,0,300,30,90,90,150],1):
    X[i+1]=tuple(simp(a+b) for a,b in zip(X[i],(s.cos(s.pi*d/180),s.sin(s.pi*d/180))))
assert X[15]==X[1]
t=s.Rational(3,5)
V={f'X{i}':x for i,x in X.items() if i<15}
for name,j,v in [('Q',6,(1,0)),('R',8,(s.sqrt(3)/2,s.Rational(1,2))),('S',10,(s.Rational(1,2),s.sqrt(3)/2)),('T',12,(0,1))]:
    V[name]=tuple(simp(a+t*b) for a,b in zip(X[j],v))
words={'A':['X3','X4','X5','X1','X2'],'B':['X7','X8','R','Q','X6'],'C':['X9','X10','S','R','X8'],'D':['X11','X12','T','S','X10'],'H':['X14','X1','X5','Q','R','S','T']}
angles={k:[90,120,105,105,120] for k in 'ABCD'}
angles['H']=[120,165,165,75,150,150,75]
edges={}
areas={}
for k,w in words.items():
    z=[V[x] for x in w]
    for i,a in enumerate(angles[k]):
        u=sub(z[i-1],z[i]); v=sub(z[(i+1)%len(z)],z[i])
        assert cross(v,u)>0,(k,i)
        assert simp(dot(u,v)-s.sqrt(dot(u,u)*dot(v,v))*s.cos(s.pi*a/180))==0,(k,i)
    areas[k]=simp(sum(cross(z[i],z[(i+1)%len(z)]) for i in range(len(z)))/2)
    for i,x in enumerate(w):
        y=w[(i+1)%len(w)]
        edges.setdefault(tuple(sorted((x,y))),[]).append((k,angles[k][i],angles[k][(i+1)%len(w)]))
internal={e for e,c in edges.items() if len(c)==2}
assert internal=={tuple(sorted(e)) for e in [('X5','X1'),('Q','R'),('R','S'),('S','T'),('X8','R'),('X10','S')]}
for e,cs in edges.items():
    if len(cs)==1:
        assert max(cs[0][1:])>=120,(e,cs)
source_area=simp(sum(cross(X[i],X[i+1]) for i in range(1,15))/2)
assert simp(sum(areas.values())-source_area)==0
assert areas['B']==areas['C']==areas['D']
for k in 'CD':
    zs=[[V[x] for x in words[j]] for j in ('B',k)]
    ds=[[simp(dot(sub(z[i],z[j]),sub(z[i],z[j]))) for i in range(5) for j in range(5)] for z in zs]
    assert ds[0]==ds[1]
print('PASS: exact t=3/5 angles, strict convexity, incidences, exposed-side gate, congruences and area identity')
