"""Exact Rao/H omission gate for the six x=0 convex radial metrics."""
from sage.all import *
import runpy

q=PolynomialRing(QQ,'q'); r=q.gen()
K=NumberField(r*r-3,'t',embedding=1.73); t=K.gen()
RAO=runpy.run_path('research/searches/convex-substitution-shapes.py')['RAO']
metrics=[
    (t/3,2*t/3),
    ((3-t)/2,(3*t-3)/2),
    (t/2,t/2),
    (4*t-6,6-3*t),
    ((3*t-3)/2,(3-t)/2),
    (2*t/3,t/3),
]
angles=[120,90,120,120,90]
assert len(set(metrics))==6
root3=AA(t)
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
def norm(p): return dot(p,p).sqrt()
def cos_at(poly,i):
    u=sub(poly[(i-1)%len(poly)],poly[i]);v=sub(poly[(i+1)%len(poly)],poly[i])
    return dot(u,v)/(norm(u)*norm(v))
for a,b in metrics:
    assert a>0 and b>0 and a+b==t
    ar=AA(a);br=AA(b)
    P=[(AA(0),AA(0)),(AA(1),AA(0)),(AA(1),ar),((root3*ar-1)/2,(root3+ar)/2),(AA(-1)/2,root3/2)]
    assert all(cross(sub(P[(i+1)%5],P[i]),sub(P[(i+2)%5],P[(i+1)%5]))>0 for i in range(5))
    assert [cos_at(P,i) for i in range(5)]==[AA(-1)/2,AA(0),AA(-1)/2,AA(-1)/2,AA(0)]
    assert [norm(sub(P[(i+1)%5],P[i])) for i in range(5)]==[AA(1),ar,br,ar,AA(1)]
    sides=[K(1),a,b,a,K(1)]
    angle_hits=[]; exact_hits=[]
    for typ,(aeqs,leqs) in RAO.items():
        for sign in (1,-1):
            for off in range(5):
                amap=[(off+sign*i)%5 for i in range(5)]
                smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
                an=[angles[j] for j in amap]
                if not all(sum(c*d for c,d in zip(row,an))==36*target for row,target in aeqs): continue
                angle_hits.append((typ,sign,off))
                ln=[sides[j] for j in smap]
                if all(sum(c*d for c,d in zip(row,ln))==0 for row in leqs):
                    exact_hits.append((typ,sign,off))
    print('a=',a,'b=',b,'Rao angle hits=',angle_hits,'Rao exact=',exact_hits,
          'H regular=',b==2*a)
