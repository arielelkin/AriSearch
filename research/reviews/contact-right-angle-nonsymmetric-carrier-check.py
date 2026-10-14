"""Independent AA polygon-clipping verifier for one asymmetric periodic carrier.
Replay: mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/contact-right-angle-nonsymmetric-carrier-check.py
"""
from sage.all import AA,QQ,vector,ceil,floor

def det(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):
    return sum(det(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if poly else AA(0)
def clipping(first,second):
    if area(second)<0: second=list(reversed(second))
    out=list(first)
    for j in range(len(second)):
        a=second[j]; direction=second[(j+1)%len(second)]-a
        if not out:break
        prev=out[-1]; pd=det(direction,prev-a); updated=[]
        for here in out:
            hd=det(direction,here-a)
            if (pd<0)!=(hd<0):
                updated.append(prev+(here-prev)*pd/(pd-hd))
            if hd>=0:updated.append(here)
            prev=here;pd=hd
        out=updated
    return out
r=AA(2).sqrt(); c=((2+r)/4).sqrt(); t=((2-r)/4).sqrt()
x=AA(1);y=AA(2);v=AA(QQ(5)/2);u=v+r*c
w=(u+v)/r-t*(x+y);h=AA(3)
assert min(x,y,u,v,w,h)>0 and len({x,y,u,v,w})==5
assert h not in {x,y,u,v,w}
assert not {x,y,w}.intersection({2*u,2*v})
A=vector(AA,[0,-w]);B=A+vector(AA,[x*c,-x*t])
C=B+vector(AA,[u/r,u/r]);D=C+vector(AA,[-v/r,v/r])
E=D+vector(AA,[-y*c,-y*t]);assert E==vector(AA,[0,0])
P=[A,B,C,D,E]; Q=[vector(AA,[0,0])]
steps=[(-v/r,v/r),(-h,0),(-u/r,-u/r),(0,-w),(v/r,-v/r),(h,0),(u/r,u/r),(0,w)]
for step in steps[:-1]:Q.append(Q[-1]+vector(AA,step))
assert Q[-1]+vector(AA,steps[-1])==Q[0]
P2=[A+B-z for z in P]
U=vector(AA,[(u-v)/r,(u+v)/r+w])
V=vector(AA,[x*c+(u+v)/r+h,-w-x*t-(v-u)/r])
covolume=det(V,U);assert covolume>0
polys=[Q,P,P2]
for poly in polys:
    assert area(poly)>0
    for i in range(len(poly)):
        for j in range(len(poly)):
            if j not in (i,(i+1)%len(poly)):
                assert det(poly[(i+1)%len(poly)]-poly[i],poly[j]-poly[i])>0
assert area(Q)+area(P)+area(P2)==covolume
lattice_coords=[[(det(z,U)/covolume,det(V,z)/covolume) for z in poly] for poly in polys]
checks=0
for i,p in enumerate(polys):
    for j,q in enumerate(polys):
        lows=[]; highs=[]
        for k in (0,1):
            lows.append(ceil(min(z[k] for z in lattice_coords[i])-max(z[k] for z in lattice_coords[j])))
            highs.append(floor(max(z[k] for z in lattice_coords[i])-min(z[k] for z in lattice_coords[j])))
        for m in range(lows[0],highs[0]+1):
            for n in range(lows[1],highs[1]+1):
                if i==j and m==n==0:continue
                shifted=[z+m*V+n*U for z in q]
                intersection=clipping(p,shifted)
                assert area(intersection)==0,(i,j,m,n)
                checks+=1
assert checks==22
print("Independent exact AA/clipping carrier verification passed: 22 exhaustive overlap candidates, convexity and covolume")
