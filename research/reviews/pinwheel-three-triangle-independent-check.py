"""Independent exact three-triangle enumeration; no producer imports."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

def minus(a,b): return (a[0]-b[0],a[1]-b[1])
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def times(s,a): return (s*a[0],s*a[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def wedge(a,b): return a[0]*b[1]-a[1]*b[0]
def edges(t): return list(zip(t,t[1:]+t[:1]))
def norm(v): return dot(v,v)
def hull(points):
    ps=sorted(set(points)); lower=[]; upper=[]
    for p in ps:
        while len(lower)>1 and wedge(minus(lower[-1],lower[-2]),minus(p,lower[-1]))<=0: lower.pop()
        lower.append(p)
    for p in reversed(ps):
        while len(upper)>1 and wedge(minus(upper[-1],upper[-2]),minus(p,upper[-1]))<=0: upper.pop()
        upper.append(p)
    return tuple(lower[:-1]+upper[:-1])
def area(p): return sum(wedge(a,b) for a,b in edges(p))/2

def disjoint(a,b):
    for u,v in edges(a)+edges(b):
        e=minus(v,u); n=(-e[1],e[0]); aa=[dot(p,n) for p in a];bb=[dot(p,n) for p in b]
        if max(aa)<=min(bb) or max(bb)<=min(aa): return True
    return False

def inside_segment(p,u,v):
    return wedge(minus(p,u),minus(v,u))==0 and dot(minus(p,u),minus(p,v))<0

def ete(a,b):
    return not any(inside_segment(p,u,v) for p in a for u,v in edges(b)) and not any(inside_segment(p,u,v) for p in b for u,v in edges(a))

BASE=((F(0),F(0)),(F(2),F(0)),(F(0),F(1)))
def attachments(u,v,parent):
    e=minus(v,u); J=(-e[1],e[0]); out=set()
    for a,b,c in permutations(BASE):
        f=minus(b,a)
        if norm(f)!=norm(e):continue
        alpha=dot(minus(c,a),f)/norm(f)
        beta=wedge(f,minus(c,a))/norm(f)
        for sign in (-1,1):
            w=plus(u,plus(times(alpha,e),times(sign*beta,J)))
            cand=hull((u,v,w))
            if disjoint(cand,parent):out.add(cand)
    assert len(out)==2
    return out

def signature(p):
    # Unordered point sets: all vertex permutations, independent of cyclic canonicalization.
    return min(tuple(norm(minus(q[i],q[j])) for i in range(len(q)) for j in range(i)) for q in permutations(p))

def main():
    patches={tuple((BASE,))}; counts=[1]
    for k in (2,3):
        new=set()
        for patch in patches:
            for old in patch:
                for u,v in edges(old):
                    for cand in attachments(u,v,old):
                        if all(disjoint(cand,t) for t in patch):new.add(tuple(sorted(patch+(cand,))))
        patches=new;counts.append(len(patches))
    nonete=[p for p in patches if not all(ete(p[i],p[j]) for i in range(3) for j in range(i))]
    convex={}
    convex_ete={}
    for patch in patches:
        h=hull([v for t in patch for v in t])
        if area(h)==3:
            convex[signature(h)]=h
            if patch not in nonete:convex_ete[signature(h)]=h
    cert=json.loads(Path('research/certificates/pinwheel-three-triangle-convex-clusters.json').read_text())
    saved={}
    for item in cert['classes']:
        p=tuple(tuple(F(x) for x in v) for v in item['boundary'])
        tris=[tuple(tuple(F(x) for x in v) for v in t) for t in item['triangles']]
        assert all(sorted(norm(minus(a,b)) for a,b in edges(t))==[1,4,5] and area(t)==1 for t in tris)
        assert all(disjoint(tris[i],tris[j]) for i in range(3) for j in range(i))
        assert all(ete(tris[i],tris[j]) for i in range(3) for j in range(i))
        assert p==hull([v for t in tris for v in t]) and area(p)==3
        assert item['side_count']==len(p)
        sup=[i for i in range(len(p)) if wedge(minus(p[i],p[i-1]),minus(p[(i+2)%len(p)],p[(i+1)%len(p)]))==0 and dot(minus(p[i],p[i-1]),minus(p[(i+2)%len(p)],p[(i+1)%len(p)]))<0]
        assert sup==item['adjacent_supplementary_indices']
        saved[signature(p)]=p
    assert counts==cert['raw_patch_counts']
    assert set(saved)==set(convex)==set(convex_ete)
    p=next(p for p in saved.values() if len(p)==5)
    other=[minus(plus(p[3],p[4]),v) for v in p]
    H=hull(list(p)+other)
    assert area(H)==6 and disjoint(p,hull(other)) and len(H)==6
    assert all(plus(H[i],H[(i+3)%6])==plus(H[0],H[3]) for i in range(3))
    a=minus(H[1],H[0]);b=minus(H[2],H[1]);c=minus(H[3],H[2]);v=plus(a,b);w=plus(b,c)
    det=wedge(v,w)
    assert abs(det)==area(H)
    coords=[(wedge(z,w)/det,wedge(v,z)/det) for z in H]
    bounds=[int(max(z[k] for z in coords)-min(z[k] for z in coords)) for k in (0,1)]
    for i in range(-bounds[0],bounds[0]+1):
        for j in range(-bounds[1],bounds[1]+1):
            if i or j:
                shift=plus(times(i,v),times(j,w))
                assert disjoint(H,tuple(plus(z,shift) for z in H))
    print(json.dumps({'raw_counts':counts,'non_edge_to_edge_raw_patches':len(nonete),'convex_classes':len(convex),'convex_edge_to_edge_classes':len(convex_ete),'pentagon_double_area':str(area(H)),'lattice_vectors':[[str(t) for t in v],[str(t) for t in w]]}))
if __name__=='__main__':main()
