"""Independent AA/clipping full-neighbor census for two exact distance3 metrics.
Replay: mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/contact-right-angle-distance-three-ring-check.py
Domains: two stated exact polygons; all16fullside neighbor choices each.
"""
from sage.all import AA,QQ,vector,matrix
from itertools import product

def det(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return sum(det(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if poly else AA(0)
def clipping(first,second):
    if area(second)<0: second=list(reversed(second))
    out=list(first)
    for j in range(len(second)):
        a=second[j]; direction=second[(j+1)%len(second)]-a
        if not out:break
        prev=out[-1];pd=det(direction,prev-a);updated=[]
        for here in out:
            hd=det(direction,here-a)
            if (pd<0)!=(hd<0):updated.append(prev+(here-prev)*pd/(pd-hd))
            if hd>=0:updated.append(here)
            prev=here;pd=hd
        out=updated
    return out

def convex(poly):
    for i in range(len(poly)):
        for j in range(len(poly)):
            if j not in(i,(i+1)%len(poly)):
                assert det(poly[(i+1)%len(poly)]-poly[i],poly[j]-poly[i])>0

def key(poly):return frozenset(tuple(z) for z in poly)
def ete(p,q):
    for point in p:
        for j in range(len(q)):
            left=q[j];right=q[(j+1)%len(q)]
            if det(point-left,right-left)==0 and (point-left).dot_product(point-right)<0:return False
    for point in q:
        for j in range(len(p)):
            left=p[j];right=p[(j+1)%len(p)]
            if det(point-left,right-left)==0 and (point-left).dot_product(point-right)<0:return False
    return True
r=AA(2).sqrt();c=((2+r)/4).sqrt();t=((2-r)/4).sqrt()
x=AA(1);y=AA(2);v=AA(QQ(5)/2);u=v+r*c;w=(u+v)/r-t*(x+y)
A=vector(AA,[0,-w]);B=A+vector(AA,[x*c,-x*t])
C=B+vector(AA,[u/r,u/r]);D=C+vector(AA,[-v/r,v/r])
P=[A,B,C,D,vector(AA,[0,0])];convex(P)
assert all(z not in (2*u,2*v) for z in(x,w,y))
dirs=[(1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)]

def attach(poly,edge_index,left,right,centre):
    start=poly[edge_index]; source=poly[(edge_index+1)%len(poly)]-start
    images={}
    for first,last in((left,right),(right,left)):
        target=last-first;normal=vector(AA,[-target[1],target[0]])
        assert source.dot_product(source)==target.dot_product(target)
        for sign in(-1,1):
            image=[first+target*((point-start).dot_product(source)/source.dot_product(source))+normal*(sign*det(source,point-start)/source.dot_product(source)) for point in poly]
            if area(clipping(image,centre))==0:images.setdefault(key(image),image)
    assert len(images)==2
    return list(images.values())

for equal in(False,True):
    if equal:
        h=v+w-u+r*(w-u); lengths=[h,u,u,h,v,w,w,v]
    else:
        h0=u+w-v+r*(w-u);h3=r*(w-v)+w+v-u
        lengths=[h0,u,v,h3,u,w,w,v]
    assert all(z>0 for z in lengths)
    assert lengths[0] not in(x,y,u,v,w) and lengths[3] not in(x,y,u,v,w)
    assert x not in lengths and y not in lengths
    Q=[vector(AA,[0,0])]
    for length,direction in zip(lengths[:-1],dirs[:-1]):Q.append(Q[-1]+length*vector(AA,direction))
    assert Q[-1]+lengths[-1]*vector(AA,dirs[-1])==Q[0];convex(Q)
    options=[]
    for i in range(8):
        left=Q[i];right=Q[(i+1)%8]
        if i in(0,3):
            raw=[]
            for edge_index in((0,3) if equal else(i,)):
                raw.extend(attach(Q,edge_index,left,right,Q))
            unique={}
            for image in raw:unique.setdefault(key(image),image)
            candidates=list(unique.values())
        else:
            index={u:1,v:2,w:4}[lengths[i]]
            candidates=attach(P,index,left,right,Q)
            if lengths[i] in(u,v):
                acute=left if(i-1)%8 in(0,3) else right
                candidates=[poly for poly in candidates if poly[2]==acute]
        options.append(candidates)
    assert [len(z) for z in options]==[2,1,1,2,1,2,2,1]
    valid=[];tested=0
    for choices in product(*(range(len(z)) for z in options)):
        ring=[options[i][choices[i]] for i in range(8)];tested+=1
        if all(area(clipping(ring[i],ring[j]))==0 and ete(ring[i],ring[j]) for i in range(8) for j in range(i)):
            valid.append(ring)
    assert tested==16 and len(valid)==(1 if equal else 0)
    if equal:
        M=matrix(AA,[[-2*c*c+1,2*c*c-1],[2*c*c-1,2*c*c-1]])
        offset=vector(AA,[-8*c**3+5*c*c+3*c-AA(QQ(5)/2),4*c**3-15*c*c-3*c+5])
        halfturn=vector(AA,[8*c**3-10*c+10,20*c*c+2*c-5])
        S=lambda z:M*z+offset
        T=lambda z:-z+halfturn
        assert M*M==matrix.identity(AA,2) and M.det()==-1
        assert key(valid[0][0])==key([S(z) for z in Q])
        assert key(valid[0][3])==key([T(z) for z in Q])
        assert key([S(T(z)) for z in Q])==key(Q)
        period=M*offset+offset
        assert period==vector(AA,[-8*c**3+6*c-5,-20*c*c-2*c+5]) and period!=vector(AA,[0,0])
print("Independent exact distance3 ring checker passed: mixed0/16, equal1/16, all rigid-map/period identities")
