"""Exact small-patch gate for one rational P5/P5 half-side design.

Run: mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-p5p5-halfside-2026-10-20.py
"""
from fractions import Fraction as F
from itertools import product

P = ((0, 0), (5, 0), (6, 2), (3, 5), (-1, 3))
Q = ((0, 0), (5, 0), (6, 2), (2, 3), (-2, 1))


def sub(a, b): return (a[0]-b[0], a[1]-b[1])
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def cross(a, b): return a[0]*b[1]-a[1]*b[0]
def dot(a, b): return a[0]*b[0]+a[1]*b[1]
def norm2(a): return dot(a, a)
def edges(poly): return tuple((poly[i], poly[(i+1)%len(poly)]) for i in range(len(poly)))
def area2(poly): return sum(cross(a, b) for a, b in edges(poly))
def turns(poly):
    return tuple(cross(sub(b,a), sub(c,b)) for a,b,c in
                 ((poly[i-1],poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))))
def angle_dots(poly):
    return tuple(dot(sub(poly[i-1],poly[i]),sub(poly[(i+1)%len(poly)],poly[i]))
                 for i in range(len(poly)))
def consecutive_supplementary(poly):
    es=[sub(b,a) for a,b in edges(poly)]
    return tuple(i for i in range(len(poly)) if cross(es[(i-1)%len(poly)],es[(i+1)%len(poly)])==0)
def signature(poly):
    return tuple((norm2(sub(b,a)), dot(sub(a, poly[i-1]), sub(b,a)),
                  cross(sub(a, poly[i-1]), sub(b,a)))
                 for i,(a,b) in enumerate(edges(poly)))


def mapped(poly, source_edge, target, reflect):
    """Map a source edge to target with rational orthogonal transform."""
    u,v = source_edge
    s = sub(v,u); t = sub(target[1],target[0]); d=norm2(s)
    assert d == norm2(t)
    def linear(p):
        x,y=p
        if reflect: y=-y
        sx,sy=s
        if reflect: sy=-sy
        # orthogonal rotation taking (sx,sy) to t
        c=F(dot((sx,sy),t),d); z=F(cross((sx,sy),t),d)
        return (c*x-z*y,z*x+c*y)
    lu=linear(u)
    return tuple(add(sub(linear(p),lu),target[0]) for p in poly)


def interiors_intersect(a,b):
    # Separating-axis theorem; equality permits a boundary contact.
    for poly in (a,b):
        for x,y in edges(poly):
            v=sub(y,x)
            pa=[cross(v,sub(p,x)) for p in a]
            pb=[cross(v,sub(p,x)) for p in b]
            if max(pa)<=min(pb) or max(pb)<=min(pa): return False
    return True

def open_ray(poly,mid,host_vector):
    i=poly.index(mid)
    rays=(sub(poly[i-1],mid),sub(poly[(i+1)%len(poly)],mid))
    outside=[r for r in rays if cross(host_vector,r)!=0]
    assert len(outside)==1
    return outside[0]

def completed_midpoint(q1,q2,mid,host_vector):
    u=open_ray(q1,mid,host_vector); v=open_ray(q2,mid,host_vector)
    return cross(u,v)==0 and dot(u,v)>0


def half_contacts(q=Q):
    a,b=P[3],P[4] # length sqrt(20) side
    mid=((F(a[0])+b[0])/2,(F(a[1])+b[1])/2)
    # Each Q edge lies on half the P side, with Q exterior to P.
    ret=[]
    for first,second in ((a,mid),(mid,b)):
        choices=[]
        for j,(u,v) in enumerate(edges(q)):
            if norm2(sub(v,u)) != 5: continue
            for direction,reflection in product((0,1),(0,1)):
                target=(first,second) if direction==0 else (second,first)
                placed=mapped(q,(u,v),target,reflection)
                if not interiors_intersect(P,placed):
                    choices.append((j,direction,reflection,placed))
        ret.append(choices)
    return mid,ret


def main():
    import sys
    if '--scan' in sys.argv:
        hits=[]
        for c,d,e,f in product(range(2,9),range(2,9),range(-2,5),range(1,8)):
            q=((0,0),(5,0),(6,2),(c,d),(e,f))
            if min(turns(q))<=0 or area2(q)==area2(P): continue
            if 20 in (norm2(sub(b,a)) for a,b in edges(q)): continue
            if consecutive_supplementary(q) or max(angle_dots(q))<=0: continue
            _,choices=half_contacts(q)
            pairs=[(a,b) for a,b in product(*choices) if not interiors_intersect(a[3],b[3])]
            if pairs:
                mid=((F(P[3][0])+P[4][0])/2,(F(P[3][1])+P[4][1])/2)
                full=[(a,b) for a,b in pairs if completed_midpoint(a[3],b[3],mid,sub(P[4],P[3]))]
                hits.append((q,len(pairs),full))
        print('total filtered exact small-domain hit count',len(hits))
        print('completed midpoint fixtures',sum(bool(full) for q,n,full in hits))
        for q,n,full in hits:
            if full: print(q,n,len(full),full[0][0][:3],full[0][1][:3])
        return
    assert all(x>0 for x in turns(P)) and all(x>0 for x in turns(Q))
    assert area2(P)!=area2(Q)
    print('P',P,'area2',area2(P),'turns',turns(P),'angle_dots',angle_dots(P),'side2',tuple(norm2(sub(b,a)) for a,b in edges(P)))
    print('Q',Q,'area2',area2(Q),'turns',turns(Q),'angle_dots',angle_dots(Q),'side2',tuple(norm2(sub(b,a)) for a,b in edges(Q)))
    print('consecutive supplementary indices',consecutive_supplementary(P),consecutive_supplementary(Q))
    mid, choices=half_contacts()
    print('midpoint',mid,'individual placement counts',tuple(map(len,choices)))
    whole=[]
    pe=edges(P)[3]
    for j,qe in enumerate(edges(Q)):
        if norm2(sub(*qe))!=20: continue
        for direction,reflection in product((0,1),(0,1)):
            target=pe if direction==0 else pe[::-1]
            placed=mapped(Q,qe,target,reflection)
            if not interiors_intersect(P,placed): whole.append((j,direction,reflection,placed))
    print('whole-side P/Q alternatives',tuple(x[:3] for x in whole))
    assert whole
    pairs=[]
    for c,d in product(*choices):
        if not interiors_intersect(c[3],d[3]): pairs.append((c,d))
    print('nonoverlap half-side Q,Q placement pairs',len(pairs))
    assert len({(c[3],d[3]) for c,d in pairs})==len(pairs)
    for c,d in pairs:
        print('pair branch IDs',c[:3],d[:3])
    if pairs:
        c,d=pairs[0]
        print('first exact patch Q1',c[3],'Q2',d[3])
    print('scope: only two Qs, full native Q edges, and the two halves of this P side')


if __name__=='__main__': main()
