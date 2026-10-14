#!/usr/bin/env python3
"""Exact offset mixed parent and the homogeneous-right-corner obstruction."""
import argparse
import json
import sys
from pathlib import Path
from sage.all import AA, NumberField, PolynomialRing, QQ, vector


def produce():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled")
    R=PolynomialRing(QQ,"g")
    K=NumberField(R.gen()**4-10*R.gen()**2+1,"g",embedding=AA(2).sqrt()+AA(3).sqrt())
    g=K.gen(); s=(g-1/g)/2; r=(g+1/g)/2
    assert s*s==2 and r*r==3 and s>0 and r>0
    def V(x,y): return vector(K,[x,y])
    def cross(a,b): return a[0]*b[1]-a[1]*b[0]
    def area(F): return sum(cross(a,b) for a,b in zip(F,F[1:]+F[:1]))/2
    def enc(x):
        c=list(K(x)); return [str(a) for a in c]+["0"]*(4-len(c))
    def poly(F): return [[enc(x) for x in p] for p in F]
    def convex(F):
        return all(cross(F[(i+1)%len(F)]-a,z-a)>0 for i,a in enumerate(F)
                   for j,z in enumerate(F) if j not in (i,(i+1)%len(F)))
    P=[V(0,0),V(3,0),V(4,r),V(QQ(7)/2,3*r/2),V(0,1/r)]
    Q=[V(0,0),V(3,0),V(3+1/(s*r),1/(s*r)),V(3+1/(s*r),7/r+1/(s*r)),
       V(s,7/r+1/(s*r)),V(0,7/r+1/(s*r)-s)]
    angles={"P":[90,120,120,90,120],"Q":[90,135,135,90,135,135]}
    shapes={"P":P,"Q":Q}
    assert convex(P) and convex(Q) and area(P)==10/r and area(P)!=area(Q)
    for name,F in shapes.items():
        for i,a in enumerate(angles[name]):
            left=F[i-1]-F[i]; right=F[(i+1)%len(F)]-F[i]
            dot=left.dot_product(right); norms=left.dot_product(left)*right.dot_product(right)
            if a==90: assert dot==0
            elif a==120: assert dot<0 and 4*dot*dot==norms
            elif a==135: assert dot<0 and 2*dot*dot==norms
            else: raise AssertionError("Unexpected angle")
    # A strict partial seam: both ends are native90 corners in a host side.
    t=K(1); Qhat=[V(t,0)-q for q in Q]
    assert all(p[1]>=0 for p in P) and all(q[1]<=0 for q in Qhat)
    assert P[0][0]<Qhat[0][0]<P[1][0]
    assert Qhat[1][0]<P[0][0]<Qhat[0][0]
    boundary=[Qhat[0]]+P[1:]+[P[0]]+Qhat[1:]
    assert len(boundary)==11 and area(boundary)==area(P)+area(Q)
    turns=[cross(boundary[(i+1)%11]-boundary[i],boundary[(i+2)%11]-boundary[(i+1)%11]) for i in range(11)]
    assert all(x!=0 for x in turns) and sum(x<0 for x in turns)==2
    # Every exact convex right corner has orthogonal incident unit rays.
    corner_records=[]
    for name,F in shapes.items():
        A=angles[name]
        for i,a in enumerate(A):
            if a!=90: continue
            n=len(F); left=(i-1)%n; right=(i+1)%n
            assert (F[left]-F[i]).dot_product(F[right]-F[i])==0
            for hand in (0,1):
                ends=[left,right] if hand==0 else [right,left]
                far=[A[j] for j in ends]
                native_sides=[(F[j]-F[i]).dot_product(F[j]-F[i]) for j in ends]
                # Host rays end respectively at120 and135. Native far corners
                # cannot be in a flat host in either possible length order.
                remainders=[360-host-guest for host,guest in zip([120,135],far)]
                assert 105 in remainders
                corner_records.append({"type":name,"corner":i,"hand":hand,
                    "far_corners":ends,"far_angles":far,
                    "squared_arm_lengths":[enc(x) for x in native_sides],
                    "equal_endpoint_remainders":remainders,"status":"FORBIDDEN_105_ENDPOINT"})
    def fill(n):
        return any(90*a+120*b+135*c+180*d==n
                   for a in range(5) for b in range(4) for c in range(3) for d in range(3))
    forbidden=[45,60,105,150]
    assert all(not fill(n) for n in forbidden)
    assert fill(90) and fill(120) and fill(135) and fill(180)
    return {"field":{"polynomial":"g^4-10*g^2+1","embedding":"sqrt(2)+sqrt(3)","basis":["1","g","g^2","g^3"]},
        "atoms":{name:{"vertices":poly(F),"angles":angles[name],"area":enc(area(F))} for name,F in shapes.items()},
        "parent":{"offset":enc(t),"Q_halfturn_vertices":poly(Qhat),"boundary":poly(boundary),
                  "corners":11,"reflex_corners":2,"native_seam_endpoints":["P0 in Qside0","Q0 in Pside0"],
                  "area":enc(area(boundary)),"status":"EXACT_DISJOINT_MIXED_PARTIAL_PARENT"},
        "palette":{"forbidden_remainders":forbidden,"flat_sector":180,"least_native_angle":90},
        "wedge_domain":{"host_far_angles":[120,135],"right_corner_guests":corner_records,
                        "length_orders_per_ray":["shorter","equal","longer"],"survivors":0},
        "contact_interval_domain":[{"Q_left":"strictly below P90","Q_right":"inside P side, native90","kind":"STAGGERED_HOST_SWITCH"},
                                   {"Q_left":"equal P90, native135","Q_right":"inside P side, native90","kind":"ALIGNED_Q_CONTAINMENT"}],
        "repair":{"Q_base":"b>3","offset":"t=b-3, 0<t<3","other_lengths":"u,7/r,b+(u-2)/s,2,7/r+(u-2)/s",
                  "result":"SAME_MIXED_120_135_WEDGE_OBSTRUCTION_FOR_ALL_POSITIVE_METRICS"},
        "scope":"No positive-length P/Q contact for these native angle words at any strictly convex positive metric. Fixed P omission is excluded by reviewed Cairo theorem. Q-only existence is not classified.",
        "completion":"EXACT_OBSTRUCTION_TO_THIS_MIXED_PARTIAL_PARENT_SCHEME"}


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--output",type=Path)
    args=parser.parse_args(); data=json.dumps(produce(),sort_keys=True,indent=2)+"\n"
    if args.output: args.output.write_text(data)
    else: print(data,end="")

if __name__=="__main__": main()
