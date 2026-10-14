"""Exact six-profile reconstruction of the OPEN UBC exercise incidence diagram.
This is an internally defined geometry fixture, not verified Danzer parameters.
No universal decoder or aperiodicity assertion is made.
Replay: mise exec -- conda run --no-capture-output -n arisearch sage research/searches/current-exact-convex-source-six-profile.py
Finite domain: one exact profile for each rhomb, six named polygons.
"""
from sage.all import AA, QQ, vector

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def J(a): return vector(AA,[-a[1],a[0]])
def kink(V,i,t,h):
    d=V[(i+1)%4]-V[i]
    return V[i]+t*d+h*J(d)
def area(P): return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2

def check(P):
    # All vertices strictly on the left of every directed support edge:
    # this proves the cyclic polygon is genuine and strictly convex.
    for i in range(len(P)):
        a,b=P[i],P[(i+1)%len(P)]
        assert a != b
        for j,c in enumerate(P):
            if j not in (i,(i+1)%len(P)):
                assert cross(b-a,c-a)>0, (i,j,cross(b-a,c-a))
    assert area(P)>0

def signature(P):
    # Complete cyclic intervertex distances, canonicalized under rotations
    # and reversal: exact criterion for congruence of convex polygons.
    n=len(P)
    def sig(order):
        return tuple((P[order[i]]-P[order[j]]).dot_product(P[order[i]]-P[order[j]]) for i in range(n) for j in range(i+1,n))
    return min(sig([(s+orient*i)%n for i in range(n)]) for s in range(n) for orient in (-1,1))

r=AA(5).sqrt()
c36=(1+r)/4; s36=(10-2*r).sqrt()/4
c18=(10+2*r).sqrt()/4; s18=(r-1)/4
O=vector(AA,[0,0]); eps=QQ(1)/100
u=vector(AA,[c36,-s36]); v=vector(AA,[c36,s36])
V=[O,u,u+v,v]
# Two outward and two inward kink profiles as in the thick-rhomb drawing.
t=[QQ(1)/2,QQ(1)/2,QQ(1)/2,QQ(1)/2]
K=[kink(V,i,t[i],(-eps if i<2 else eps)) for i in range(4)]
S0=(K[0]+V[1])/2; S1=(V[1]+K[1])/2
X=QQ(35)/100*u+QQ(35)/100*v
Y=QQ(65)/100*u+QQ(65)/100*v
thick=[[V[0],K[0],S0,X,K[3]], [S0,V[1],S1,Y,X], [S1,K[1],V[2],K[2],Y], [K[2],V[3],K[3],X,Y]]
a=vector(AA,[c18,-s18]); b=vector(AA,[c18,s18]); W=[O,a,a+b,b]
L=[kink(W,i,QQ(1)/2,(-eps if i%2==0 else eps)) for i in range(4)]
thin=[[W[0],L[0],W[1],L[1],L[3]],[L[3],L[1],W[2],L[2],W[3]]]
def intersection(P,Q):
    output=list(P)
    for a,b in zip(Q,Q[1:]+Q[:1]):
        if not output: break
        previous=output[-1]; prevdist=cross(b-a,previous-a)
        new=[]
        for current in output:
            curdist=cross(b-a,current-a)
            if (prevdist<0) != (curdist<0):
                new.append(previous+(current-previous)*(prevdist/(prevdist-curdist)))
            if curdist>=0: new.append(current)
            previous=current; prevdist=curdist
        output=new
    return output
for P in thick+thin: check(P)
for faces in (thick,thin):
    for i,P in enumerate(faces):
        for Q in faces[i+1:]:
            I=intersection(P,Q)
            assert not I or area(I)==0
assert sum(area(P) for P in thick)==area([z for i in range(4) for z in (V[i],K[i])])
assert sum(area(P) for P in thin)==area([z for i in range(4) for z in (W[i],L[i])])
print("exact convexity and area identities passed for six incidence faces")
print("thick congruence classes:", len(set(signature(P) for P in thick)))
print("thin congruence classes:",len(set(signature(P) for P in thin)))
print("all congruence classes:",len(set(signature(P) for P in thick+thin)))
print("WARNING: boundary profile compatibility with Penrose arrows and universal decoding remain unproved")

# The attempted opposite-midpoint thin-class identification has a monohedral
# Type-2 escape. Its old vertices 0 and 2 have supplementary angles, and
# all four source-profile sides (everything except the new seam) are equal.
P=thin[0]
def angle_data(P,i):
    a=P[(i-1)%len(P)]-P[i]; b=P[(i+1)%len(P)]-P[i]
    norm=(a.dot_product(a)*b.dot_product(b)).sqrt()
    return a.dot_product(b)/norm, abs(cross(a,b))/norm
c0,s0=angle_data(P,0); c2,s2=angle_data(P,2)
assert c0==-c2 and s0==s2
lengths=[(P[(i+1)%5]-P[i]).dot_product(P[(i+1)%5]-P[i]) for i in range(5)]
assert lengths[0]==lengths[1]==lengths[2]==lengths[4]
assert signature(thin[0])==signature(thin[1])
print("thin congruence collapse has exact supplementary nonadjacent angles and four equal profile sides: Type 2")

# Explicit four-P periodic motif, independent of the Type-2 classification.
# Parent-grid basis a,b from above; reflection S across the long diagonal.
def S(z): return vector(AA,[z[0],-z[1]])
C=(a+b)/2
assert eps < s18/(2*c18) # tan(18deg)/2
# All fan triangles retain orientation throughout displacement homotopy.
for reflected in (False,True):
    for i in range(4):
        e=W[(i+1)%4]-W[i]
        midpoint=(W[i]+W[(i+1)%4])/2
        K=L[i]
        if reflected:
            # Reflection fixes the parent but reverses the cyclic boundary.
            K=S(L[(3-i)%4])
        assert cross(K-W[i],C-W[i])>0
        assert cross(W[(i+1)%4]-K,C-K)>0
# Checkerboard partners have coincident kinked edges after translation.
# Reflected source parent reindexed by its old original CCW side order.
mirrorL=[S(L[(3-i)%4]) for i in range(4)]
assert L[1]==mirrorL[3]+a
assert L[2]==mirrorL[0]+b
assert L[3]==mirrorL[1]-a
assert L[0]==mirrorL[2]-b
period1=a+b; period2=a-b
assert abs(cross(period1,period2))==4*area(thin[0])
print("explicit checkerboard four-P lattice motif: coincident profiles, positive fan determinants, covolume passed")
