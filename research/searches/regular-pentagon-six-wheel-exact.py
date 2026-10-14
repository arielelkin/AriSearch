"""Two exact fixtures: regular-parent six-wheel and exceptional four-Q carrier; no seven-child search.
Replay through mise exec -- conda run --no-capture-output -n arisearch sage.
The accompanying corner-potential proof excludes any P child in a Q image.
"""
from sage.all import AA, QQbar, QQ, vector, matrix

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(P): return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2
def check(P):
    for i,a in enumerate(P):
        b=P[(i+1)%len(P)]
        for j,c in enumerate(P):
            if j not in (i,(i+1)%len(P)): assert cross(b-a,c-a)>0

def intersection(P,Q):
    output=list(P)
    for a,b in zip(Q,Q[1:]+Q[:1]):
        if not output: break
        prev=output[-1]; dp=cross(b-a,prev-a); out=[]
        for cur in output:
            dc=cross(b-a,cur-a)
            if (dp<0)!=(dc<0): out.append(prev+(cur-prev)*dp/(dp-dc))
            if dc>=0: out.append(cur)
            prev=cur; dp=dc
        output=out
    return output

def cos_angle(P,i):
    a=P[(i-1)%len(P)]-P[i]; b=P[(i+1)%len(P)]-P[i]
    return a.dot_product(b)/(a.dot_product(a)*b.dot_product(b)).sqrt()
r=AA(5).sqrt(); phi=(1+r)/2; rho=2/phi**3
z=QQbar.zeta(5)
V=[vector(AA,[(z**i).real(),(z**i).imag()]) for i in range(5)]
M=[(V[i]+V[(i+1)%5])/2 for i in range(5)]
P=[rho*m for m in M]
Q=[[V[i],M[i],rho*M[i],rho*M[(i-1)%5],M[(i-1)%5]] for i in range(5)]
faces=[P]+Q
for F in [V]+faces: check(F)
for i,F in enumerate(faces):
    for G in faces[i+1:]:
        I=intersection(F,G)
        assert not I or area(I)==0
assert sum(area(F) for F in faces)==area(V)
assert area(V)==phi**4*area(P)
assert area(Q[0])==(phi**4-1)*area(P)/5
c108=(1-r)/4; c126=-(10-2*r).sqrt()/4
assert [cos_angle(P,i) for i in range(5)]==[c108]*5
assert [cos_angle(Q[0],i) for i in range(5)]==[c108,0,c126,c126,0]
# Compact exhaustive scalar star domain, derived directly from min angle90.
full=[(a,b,c) for a in range(5) for b in range(5) for c in range(5) if 6*a+5*b+7*c==20]
flat=[(a,b,c) for a in range(3) for b in range(3) for c in range(3) if 6*a+5*b+7*c==10]
assert full==[(0,4,0),(1,0,2)]
assert flat==[(0,2,0)]
print("Exact six-wheel: convex faces, pairwise disjointness, complete parent area, phi^4 ratio, all angle cosines passed")
print("Exact full/flat angle stars passed; every Q-parent image has zero P children by corner potential")

L=(T:=Q[0])[1]-T[0]
Llength=L.norm(); Rlength=(T[2]-T[1]).norm(); Clength=(T[3]-T[2]).norm()
assert Rlength < Llength
assert Clength < 2*Llength
print("Exact proposed rho lies in the analytically untileable R<L,C<2L region")

# Explicit four-Q periodic carrier at the sole surviving exceptional rho.
c36=(1+r)/4; s36=(10-2*r).sqrt()/4
rho0=1-s36/c36
Q0=[V[0],M[0],rho0*M[0],rho0*M[4],M[4]]
check(Q0)
A=Q0[4]; B=Q0[0]; CV=Q0[1]; D=Q0[2]; EE=Q0[3]
h=D+EE
u=CV-A; v=h-CV-A
assert cross(u,v)>0
assert u.dot_product(v)==0
assert u.dot_product(u)==v.dot_product(v)
Z=[vector(AA,[0,0]),u,u+v,v]
K=[B-A,D-A,h-B-A,EE-A]
for i in range(4): assert (K[i]-Z[i]).norm()==(Z[(i+1)%4]-K[i]).norm()
diag=u+v
S=2*diag.column()*diag.row()/diag.dot_product(diag)-matrix.identity(AA,2)
MK=[S*K[(3-i)%4] for i in range(4)]
assert K[1]==MK[3]+u and K[2]==MK[0]+v
assert K[3]==MK[1]-u and K[0]==MK[2]-v
centre=(u+v)/2
for profiles in (K,MK):
    for i in range(4):
        assert cross(profiles[i]-Z[i],centre-Z[i])>0
        assert cross(Z[(i+1)%4]-profiles[i],centre-profiles[i])>0
period1=u+v; period2=u-v
assert abs(cross(period1,period2))==4*area(Q0)
print("Exceptional rho four-Q square-checkerboard motif: exact profile matching, positive fan homotopy, covolume passed")
