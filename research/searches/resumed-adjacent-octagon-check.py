from sage.all import *
# Exact concrete 2Q+4P periodic motif, no enumeration.
r=AA(5).sqrt();phi=(1+r)/2
c36=phi/2;s36=(10-2*r).sqrt()/4
rot=matrix(AA,[[c36,-s36],[s36,c36]])
u=[rot**k*vector(AA,[1,0]) for k in range(10)]
a=phi+2;b=AA(1);c=AA(1);d=AA(1);x=2*phi**2;y=a
lengths=[d,a,b,c,d,c,b,a];dirs=[0,2,3,4,5,6,7,8]
Q=[vector(AA,[0,0])]
for ell,k in zip(lengths,dirs):Q.append(Q[-1]+ell*u[k])
assert Q[-1]==Q[0];Q.pop()
T=Q[5]-Q[0];assert T[0]==0 and T[1]>0
B=Q[4];D=Q[3];X=D+x*u[1];Y=X+b*u[3];Z=Y-y*u[0]
assert Z==Q[2]+T and B==Z+a*u[7]
P=[B,D,X,Y,Z];L=D+X
S=vector(AA,[2*(L[0]-d),0]);assert S[0]>0
Pm=[L-v for v in P]
reflect=lambda v:vector(AA,[d-v[0],v[1]])
Qr=[L-v for v in Q]
motif=[Q,Qr,P,Pm,[reflect(v)+S for v in reversed(P)],[reflect(v)+S for v in reversed(Pm)]]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(p):return sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))/2 if len(p)>2 else AA(0)
def strict(p):return all(cross(p[(i+1)%len(p)]-p[i],p[(i+2)%len(p)]-p[(i+1)%len(p)])>0 for i in range(len(p)))
assert all(strict(p) for p in motif)
assert sum(area(p) for p in motif)==cross(S,T)
# Exact Sutherland-Hodgman convex clipping, independently of construction identities.
def clip(poly,carrier):
    out=poly[:]
    for k in range(len(carrier)):
        aa=carrier[k];bb=carrier[(k+1)%len(carrier)];edge=bb-aa
        old=out;out=[]
        if not old:return out
        for i in range(len(old)):
            vv=old[i];ww=old[(i+1)%len(old)]
            sv=cross(edge,vv-aa);sw=cross(edge,ww-aa)
            if sv>=0:out.append(vv)
            if (sv<0 and sw>0) or (sv>0 and sw<0):out.append(vv+(ww-vv)*(sv/(sv-sw)))
    return out
bounds=lambda p:(min(v[0] for v in p),max(v[0] for v in p),min(v[1] for v in p),max(v[1] for v in p))
checks=0
for i,A in enumerate(motif):
    ax0,ax1,ay0,ay1=bounds(A)
    for j,Bp in enumerate(motif):
        bx0,bx1,by0,by1=bounds(Bp)
        mx0=ceil((ax0-bx1)/S[0]);mx1=floor((ax1-bx0)/S[0])
        ny0=ceil((ay0-by1)/T[1]);ny1=floor((ay1-by0)/T[1])
        for m in range(mx0,mx1+1):
            for n in range(ny0,ny1+1):
                if i==j and m==0 and n==0:continue
                shifted=[v+m*S+n*T for v in Bp]
                assert area(clip(A,shifted))==0,(i,j,m,n)
                checks+=1
# Angle cosines and sidewords independently from vertices.
cos108=(1-r)/4;cos144=-(1+r)/4
for poly,expected in [(P,[cos108]*5),(Q,[cos108,cos108]+[cos144]*6)]:
    got=[]
    for k in range(len(poly)):
        aa=poly[(k-1)%len(poly)]-poly[k];bb=poly[(k+1)%len(poly)]-poly[k]
        got.append(aa.dot_product(bb)/(aa.norm()*bb.norm()))
    assert got==expected
assert [(P[(i+1)%5]-P[i]).norm() for i in range(5)]==[c,x,b,y,a]
print('PASS: exact strict 2Q+4P motif, angle words, area identity, and',checks,'complete bounding-box overlap checks')
