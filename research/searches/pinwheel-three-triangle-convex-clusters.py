"""Exact finite domain: connected edge-to-edge unions of three 1-2-sqrt(5) triangles."""
from fractions import Fraction as F
import argparse, json
from pathlib import Path


def add(a,b): return (a[0]+b[0], a[1]+b[1])
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def mul(a,t): return (a[0]*t,a[1]*t)
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(poly): return sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))/2

def hull(points):
    points=sorted(set(points))
    out=[]
    for seq in (points,points[::-1]):
        chain=[]
        for v in seq:
            while len(chain)>1 and cross(sub(chain[-1],chain[-2]),sub(v,chain[-1]))<=0: chain.pop()
            chain.append(v)
        out.extend(chain[:-1])
    return tuple(out)

def interior_disjoint(a,b):
    for poly in (a,b):
        for u,v in zip(poly,poly[1:]+poly[:1]):
            n=(-sub(v,u)[1],sub(v,u)[0])
            aa=[dot(x,n) for x in a]; bb=[dot(x,n) for x in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa): return True
    return False

def edges(t): return list(zip(t,t[1:]+t[:1]))
def reflect(p,u,v):
    e=sub(v,u); d=sub(p,u)
    return add(u,sub(mul(e,2*dot(d,e)/dot(e,e)),d))

def placements(t,u,v):
    # A triangle with this native edge on u--v has exactly two opposite-side copies.
    a=tuple(reflect(p,u,v) for p in t)
    b=tuple(sub(add(u,v),p) for p in t)
    return [hull(a),hull(b)]

def encoding(poly): return [[str(x),str(y)] for x,y in poly]

def canonical(poly):
    # Full rational squared-distance matrix handles all translations/rotations/reflections.
    n=len(poly); values=[]
    for rev in (poly,poly[::-1]):
        for k in range(n):
            q=rev[k:]+rev[:k]
            values.append(tuple(dot(sub(q[i],q[j]),sub(q[i],q[j])) for i in range(n) for j in range(i)))
    return min(values)

def main():
    parser=argparse.ArgumentParser(); group=parser.add_mutually_exclusive_group(); group.add_argument('--output',type=Path); group.add_argument('--check',type=Path); args=parser.parse_args()
    base=((F(0),F(0)),(F(2),F(0)),(F(0),F(1)))
    patches={tuple(sorted((base,)))}
    counts=[len(patches)]
    for size in (2,3):
        next_patches=set()
        for patch in patches:
            for t in patch:
                for u,v in edges(t):
                    for candidate in placements(t,u,v):
                        if all(interior_disjoint(candidate,old) for old in patch):
                            next_patches.add(tuple(sorted(patch+(candidate,))))
        patches=next_patches; counts.append(len(patches))
    convex={}
    for patch in sorted(patches):
        h=hull([p for t in patch for p in t])
        if area(h)==3:
            key=canonical(h)
            if key not in convex:
                supplementary=[]
                # Adjacent corner sum pi iff their entering/leaving boundary edges are parallel opposite-directed.
                for k in range(len(h)):
                    e=sub(h[k],h[k-1]); f=sub(h[(k+2)%len(h)],h[(k+1)%len(h)])
                    if cross(e,f)==0 and dot(e,f)<0: supplementary.append(k)
                convex[key]={'boundary':encoding(h),'triangles':[encoding(t) for t in patch], 'side_count':len(h),'adjacent_supplementary_indices':supplementary}
    result={'domain':'three congruent 1-2-sqrt5 right triangles; connected full-side adjacency, edge-to-edge contacts; all rotations/reflections', 'raw_patch_counts':counts,'convex_congruence_class_count':len(convex),'classes':list(convex.values())}
    if args.check:
        assert json.loads(args.check.read_text())==result, 'retained certificate differs'
    elif args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    else:
        print(json.dumps(result))
    if args.check or args.output:
        print(json.dumps({'raw_patch_counts':counts,'classes':len(convex),'side_counts':[x['side_count'] for x in convex.values()],'supplementary':[x['adjacent_supplementary_indices'] for x in convex.values()]}))

if __name__=='__main__': main()
