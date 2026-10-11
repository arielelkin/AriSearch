#!/usr/bin/env python3
"""Independent exact clipping audit of forced Robinson boundary triangles/rhombs.

Imports no producer code. The reused integer boundary module is the reviewer's
independent verifier. Geometry is reconstructed directly in the cyclotomic
field; clipping replaces producer SAT, and dot products replace edge ratios.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import importlib.util
import json
from pathlib import Path
from sage.all import CyclotomicField, QQ

_spec=importlib.util.spec_from_file_location("independent_height",Path(__file__).with_name(
    "verify_pentagrid_robinson_height_boundary_independent.py"))
height=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(height)
K=CyclotomicField(10)
z=K.gen()
phi=z+z**(-1)
SCALE=z-z.conjugate()


@lru_cache(maxsize=None)
def sign(v):
    """Sign in the physical embedding, using its real subfield Q(phi)."""
    c=list(K(v))+[QQ(0)]*4
    assert c[1]==0 and c[3]==-c[2],c
    A,B=c[0]-c[2],c[2]
    a,b=2*A+B,B                 # 2*v=a+b*sqrt(5)
    if b==0:return (a>0)-(a<0)
    if a>=0 and b>0:return 1
    if a<=0 and b<0:return -1
    result=a*a-5*b*b if a>0 else 5*b*b-a*a
    assert result!=0
    return (result>0)-(result<0)


@lru_cache(maxsize=None)
def cross(a,b):
    # Physical cross divided by positive sin(pi/5).
    return (a.conjugate()*b-a*b.conjugate())/SCALE


def dot(a,b):return (a.conjugate()*b+a*b.conjugate())/2

def area2(poly):
    return sum((cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1])),K(0)) if poly else K(0)


def cleaned(vertices):
    out=[]
    for p in vertices:
        if not out or p!=out[-1]:out.append(p)
    if len(out)>1 and out[0]==out[-1]:out.pop()
    return tuple(out)


@lru_cache(maxsize=None)
def clipped_area2(subject,clipper):
    polygon=subject
    for a,b in zip(clipper,clipper[1:]+clipper[:1]):
        if not polygon:break
        out=[]
        edge=b-a
        for p,q in zip(polygon,polygon[1:]+polygon[:1]):
            cp,cq=cross(edge,p-a),cross(edge,q-a)
            ip,iq=sign(cp)>=0,sign(cq)>=0
            if ip!=iq:
                # Intersection of segment p,q with clipper supporting line.
                out.append(p+(q-p)*cp/(cp-cq))
            if iq:out.append(q)
        polygon=cleaned(out)
    value=area2(polygon)
    assert sign(value)>=0
    return value


def interior_overlap(p,q):
    # Translation-normalized caching; no projection/SAT decision is used.
    origin=p[0]
    return clipped_area2(tuple(v-origin for v in p),tuple(v-origin for v in q))!=0


def partial_contact(p,q):
    for vertices,edges in ((p,q),(q,p)):
        for w in vertices:
            for a,b in zip(edges,edges[1:]+edges[:1]):
                if cross(b-a,w-a)==0 and sign(dot(w-a,w-b))<0:
                    return w,a,b
    return None


def strict_convex(poly):
    assert sign(area2(poly))>0
    for i,(a,b) in enumerate(zip(poly,poly[1:]+poly[:1])):
        for j,p in enumerate(poly):
            if j not in (i,(i+1)%len(poly)):
                assert sign(cross(b-a,p-a))>0


def parent(name):
    return ((K(0),phi**3,z+z**2+z**3,z**2+z**3,z**3) if name=="U" else
            (K(0),K(1),1+(1+3*phi)*z**3,2*phi**2*z**3,2*phi*z**4))


def construct(name,words):
    _,directions,_,_=height.FIXTURES[name]
    P=parent(name)
    triangles=[];rhombs=[];d=[0]*10
    for x,word,k in zip(P,words,directions):
        for symbol in word:
            length={"u":K(1),"l":phi,"s":phi-1}[symbol]
            y=x+length*z**k
            if symbol!="u":
                offset=1 if symbol=="l" else 2
                apex=x+z**(k+offset)
                t=(x,y,apex)
                r=(x,x+y-apex,y,apex)
                assert (apex-x)*(apex-x).conjugate()==1
                assert (apex-y)*(apex-y).conjugate()==1
                for a,b in zip(r,r[1:]+r[:1]):assert (b-a)*(b-a).conjugate()==1
                strict_convex(t);strict_convex(r)
                triangles.append(t);rhombs.append(r)
                pair=tuple(sorted(((k-offset)%5,(k+offset)%5)))
                d[height.PAIRS.index(pair)]+=1
            x=y
    # Check every side endpoint independently, including the last closure.
    for i,(word,k) in enumerate(zip(words,directions)):
        end=P[i]+sum((({"u":K(1),"l":phi,"s":phi-1}[c])*z**k for c in word),K(0))
        assert end==P[(i+1)%5]
    return triangles,rhombs,d


def canonical(words):return tuple(tuple(w) for w in words)

def decode(c):return sum((QQ(v)*z**j for j,v in enumerate(c)),K(0))

def geometry_equals(polys,retained):
    assert len(polys)==len(retained)
    assert all(tuple(decode(c) for c in saved)==poly for poly,saved in zip(polys,retained))


def main():
    root=Path(__file__).parents[1]
    diagonal=json.loads((root/"certificates"/"pentagrid-robinson-diagonal-boundary.json").read_text())
    completion=json.loads((root/"certificates"/"pentagrid-robinson-boundary-completion.json").read_text())
    for name,(lengths,directions,angles,_) in height.FIXTURES.items():
        strict_convex(parent(name))
        stages=Counter();complete=Counter();half_survivors=set();full_survivors=set();first_rejection=None
        for words in product(*(height.words(a,b) for a,b in lengths)):
            stages["all"]+=1
            vertices=height.boundary_lift(words,directions)
            if vertices[-1]!=(0,)*5:continue
            q=height.shoelace(vertices)
            if min(q)<0 or not height.passes_fans(words,angles):continue
            stages["height_wedge_fans"]+=1
            triangles,rhombs,d=construct(name,words)
            if any(n<c or (n-c)%2 for n,c in zip(q,d)):continue
            stages["diagonal_count_and_parity"]+=1
            if not all(clipped_area2(t,parent(name))==area2(t) for t in triangles):continue
            stages["forced_triangles_contained"]+=1
            if any(interior_overlap(a,b) for a,b in combinations(triangles,2)):continue
            stages["forced_triangles_disjoint"]+=1
            half_survivors.add(words)
            complete["diagonal_boundary_survivors"]+=1
            if any(interior_overlap(a,b) for a,b in combinations(rhombs,2)):continue
            complete["complete_boundary_rhombs_disjoint"]+=1
            contact=next((t for a,b in combinations(rhombs,2) if (t:=partial_contact(a,b))),None)
            if contact:
                if first_rejection is None:first_rejection=(words,contact)
                continue
            complete["also_no_partial_rhomb_contacts"]+=1
            full_survivors.add(words)
        assert dict(stages)==diagonal["fixtures"][name]["stages"]
        assert half_survivors=={canonical(w) for w in diagonal["fixtures"][name]["surviving_boundary_words"]}
        assert dict(complete)==completion["fixtures"][name]["stages"]
        assert full_survivors=={canonical(w) for w in completion["fixtures"][name]["surviving_boundary_words"]}
        witness=diagonal["fixtures"][name]["first_witness"]
        triangles,rhombs,d=construct(name,witness["side_words"])
        geometry_equals(triangles,witness["forced_triangles"])
        assert d==witness["boundary_diagonal_counts"]
        assert list(height.shoelace(height.boundary_lift(witness["side_words"],directions)))==witness["oriented_triangle_counts"]
        witness=completion["fixtures"][name]["first_witness"]
        _,rhombs,_=construct(name,witness["side_words"])
        geometry_equals(rhombs,witness["completed_rhombs"])
        print(name,"diagonal",dict(stages),"completion",dict(complete),flush=True)
        if first_rejection:
            word,(w,a,b)=first_rejection
            print(name,"one rejected boundary",word,"strict side-interior parameter",str((w-a)/(b-a)),flush=True)
    print("Independent exact clipping audit passed; neither shape excluded, no extension claim.",flush=True)


if __name__=="__main__":
    if not __debug__:raise RuntimeError("Run without optimization")
    main()
