#!/usr/bin/env python3
"""One fixed source-free pentagon/hexagon repair and all mixed native parents."""
import argparse
import json
from pathlib import Path
import sys
from sage.all import AA, NumberField, PolynomialRing, QQ, matrix, vector


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled.")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    R=PolynomialRing(QQ,"g")
    K=NumberField(R.gen()**4-10*R.gen()**2+1,"g",embedding=AA(2).sqrt()+AA(3).sqrt())
    g=K.gen();s=(g-1/g)/2;r=(g+1/g)/2
    assert s*s==2 and r*r==3 and s>0 and r>0
    def V(x,y):return vector(K,[x,y])
    def cross(a,b):return a[0]*b[1]-a[1]*b[0]
    def area(P):return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2
    def encode(x):
        c=list(K(x));return [str(a) for a in c]+["0"]*(4-len(c))
    def polygon(P):return [[encode(x) for x in p] for p in P]
    def convex(P):
        return all(cross(P[(i+1)%len(P)]-a,z-a)>0
                   for i,a in enumerate(P) for j,z in enumerate(P)
                   if j not in (i,(i+1)%len(P)))
    def disjoint(P,Q):
        for F in (P,Q):
            for a,b in zip(F,F[1:]+F[:1]):
                n=V(-(b-a)[1],(b-a)[0]); pp=[n.dot_product(p) for p in P];qq=[n.dot_product(q) for q in Q]
                if max(pp)<=min(qq) or max(qq)<=min(pp):return True
        return False
    P=[V(0,0),V(3,0),V(4,r),V(QQ(7)/2,3*r/2),V(0,1/r)]
    Q=[V(0,0),V(3,0),V(3+1/(s*r),1/(s*r)),V(3+1/(s*r),7/r+1/(s*r)),
       V(s,7/r+1/(s*r)),V(0,7/r+1/(s*r)-s)]
    assert convex(P) and convex(Q) and area(P)==10/r and area(P)!=area(Q)
    def flatten(F):
        F=list(F)
        while True:
            removed=False
            for i in range(len(F)):
                a,b,c=F[i-1],F[i],F[(i+1)%len(F)]
                if cross(b-a,c-b)==0 and (b-a).dot_product(c-b)>0:
                    F.pop(i);removed=True;break
            if not removed:return F
    # One bounded partial-contact completion gate: no radius enlargement.
    shapes={"P":P,"Q":Q}
    angles={"P":[90,120,120,90,120],"Q":[90,135,135,90,135,135]}
    lengths={"P":[K(3),K(2),K(1),7/r,1/r],
             "Q":[K(3),1/r,7/r,3+(1/r-2)/s,K(2),7/r+(1/r-2)/s]}
    def incident_length(name,i,j):
        n=len(shapes[name])
        assert (i-j)%n in (1,n-1)
        return lengths[name][i if j==(i+1)%n else j]
    def corner_images(name,i,point,ray0,ray1):
        F=shapes[name];n=len(F)
        a=(F[(i-1)%n]-F[i])/incident_length(name,i,(i-1)%n)
        b=(F[(i+1)%n]-F[i])/incident_length(name,i,(i+1)%n)
        source=matrix(K,[list(a),list(b)]).transpose()
        result=[]
        for reverse in (False,True):
            targets=(ray1,ray0) if reverse else (ray0,ray1)
            M=matrix(K,[list(t) for t in targets]).transpose()*source.inverse()
            assert M.transpose()*M==matrix.identity(K,2)
            image=[point+M*(q-F[i]) for q in F]
            result.append((reverse,image))
        return result
    def arm(name,native,image,unit):
        n=len(image)
        for j in ((native-1)%n,(native+1)%n):
            L=incident_length(name,native,j)
            if (image[j]-image[native])/L==unit:return j,L
        raise AssertionError("Missing prescribed corner arm")
    def can_fill(degrees):
        return any(90*a+120*b+135*c+180*d==degrees
                   for a in range(5) for b in range(4) for c in range(3) for d in range(3))
    def patch_endpoint_palette(parts):
        points=set(tuple(p) for name,image in parts for p in image)
        for point in points:
            point=V(*point);total=0
            for name,image in parts:
                if point in image:
                    total+=angles[name][image.index(point)];continue
                for a,b in zip(image,image[1:]+image[:1]):
                    if cross(b-a,point-a)==0 and (point-a).dot_product(point-b)<0:
                        total+=180;break
            if total>360 or not can_fill(360-total):return False
        return True
    def blocked(L1,far1,L2,far2):
        # If the shorter side terminates within a flat longer tile side, its
        # native angle must participate in a180-star. Only90+90 is possible.
        return ((L1<L2 and far1!=90) or (L2<L1 and far2!=90)
                or (L1==L2 and not can_fill(360-far1-far2)))
    rays=[V(1,0),V(-QQ(1)/2,r/2),V(-QQ(1)/2,-r/2)]
    central_options=[]
    for sector in range(3):
        options=[]
        for native in (1,2,4):
            for reverse,image in corner_images("P",native,V(0,0),rays[sector],rays[(sector+1)%3]):
                options.append((native,reverse,image))
        central_options.append(options)
    from itertools import product
    star_records=[]
    for chosen in product(*central_options):
        copies=[c[2] for c in chosen]
        assert all(disjoint(copies[i],copies[j]) for i in range(3) for j in range(i))
        completions=[];failure=None
        for ray_index,unit in enumerate(rays):
            left=(ray_index-1)%3;right=ray_index
            li,llen=arm("P",chosen[left][0],copies[left],unit)
            ri,rlen=arm("P",chosen[right][0],copies[right],unit)
            if llen==rlen:
                if blocked(llen,angles["P"][li],rlen,angles["P"][ri]):
                    failure="MATCHED_RAY_ENDPOINT_PALETTE";break
                continue
            short,long=(left,right) if llen<rlen else (right,left)
            si,slen=(li,llen) if llen<rlen else (ri,rlen)
            hi,hlen=(ri,rlen) if llen<rlen else (li,llen)
            if angles["P"][si]!=90:
                failure="SHORT_RAY_END_IS_120";break
            point=copies[short][si]
            remaining=hlen-slen
            other=next(j for j in ((si-1)%5,(si+1)%5) if j!=chosen[short][0])
            plen=incident_length("P",si,other)
            perpendicular=(copies[short][other]-point)/plen
            assert perpendicular.dot_product(unit)==0
            guests=[]
            for name in ("P","Q"):
                for native,a in enumerate(angles[name]):
                    if a!=90:continue
                    for reverse,image in corner_images(name,native,point,unit,perpendicular):
                        along,gl=arm(name,native,image,unit)
                        across,gp=arm(name,native,image,perpendicular)
                        if blocked(remaining,angles["P"][hi],gl,angles[name][along]):continue
                        if blocked(plen,angles["P"][other],gp,angles[name][across]):continue
                        if not all(disjoint(image,F) for F in copies):continue
                        guests.append({"type":name,"native_corner":native,"reverse_arms":reverse,
                                       "vertices":polygon(image),
                                       "host_switch":gl>remaining,
                                       "host_remaining":encode(remaining),"guest_along_host":encode(gl)})
            if not guests:
                failure="NO_90_GUEST_COMPLETION";break
            completions.append({"ray":ray_index,"short_copy":short,"long_copy":long,"guests":guests})
        joint=[]
        if failure is None:
            for guest_choices in product(*(completion["guests"] for completion in completions)):
                guest_shapes=[(guest["type"],[[K(sum(QQ(c)*g**i for i,c in enumerate(x))) for x in point] for point in guest["vertices"]]) for guest in guest_choices]
                guest_shapes=[(name,[vector(K,p) for p in image]) for name,image in guest_shapes]
                # One actual tile may complete two T vertices. Geometric
                # duplicates are one occurrence, rather than an overlap.
                unique={}
                for name,image in guest_shapes:
                    key=frozenset(tuple(p) for p in image)
                    unique.setdefault(key,(name,image))
                guest_shapes=list(unique.values())
                if not all(disjoint(guest_shapes[i][1],guest_shapes[j][1]) for i in range(len(guest_shapes)) for j in range(i)):continue
                if not patch_endpoint_palette([("P",F) for F in copies]+guest_shapes):continue
                joint.append([{k:guest[k] for k in ("type","native_corner","reverse_arms","vertices","host_switch")} for guest in guest_choices])
            if not joint:failure="NO_JOINT_ENDPOINT_LEGAL_COMPLETION"
        star_records.append({"native_corners":[c[0] for c in chosen],"reverse_arms":[c[1] for c in chosen],
                             "central_P_vertices":[polygon(F) for F in copies],
                             "status":failure or "LOCAL_COMPLETION_SURVIVOR",
                             "ray_completions":completions,"joint_completions":joint})
    parents=[];attachments=0
    for i,a in enumerate(P):
        b=P[(i+1)%5];target=b-a
        for j,c in enumerate(Q):
            d=Q[(j+1)%6];edge=d-c
            if edge.dot_product(edge)!=target.dot_product(target):continue
            for reverse in (False,True):
                ta,tb=(b,a) if reverse else (a,b);f=tb-ta
                E=matrix(K,[[edge[0],-edge[1]],[edge[1],edge[0]]])
                for determinant in (-1,1):
                    M=matrix(K,[[f[0],-determinant*f[1]],[f[1],determinant*f[0]]])*E.inverse()
                    image=[ta+M*(q-c) for q in Q]
                    centre=sum(image,V(0,0))/6
                    if cross(target,centre-a)>=0:continue
                    attachments+=1
                    assert disjoint(P,image)
                    ccw=image if determinant==1 else image[::-1]
                    k=ccw.index(a)
                    assert ccw[(k-1)%6]==b
                    boundary=[P[(i+1+t)%5] for t in range(5)]+[ccw[(k+t)%6] for t in range(1,5)]
                    assert area(boundary)==area(P)+area(Q)
                    boundary=flatten(boundary)
                    turns=[cross(boundary[(t+1)%len(boundary)]-boundary[t],boundary[(t+2)%len(boundary)]-boundary[(t+1)%len(boundary)]) for t in range(len(boundary))]
                    reflex=sum(t<0 for t in turns)
                    endpoint_failures=[]
                    for native,point in ((i,a),((i+1)%5,b)):
                        qnative=image.index(point)
                        total=angles["P"][native]+angles["Q"][qnative]
                        if not can_fill(360-total):
                            endpoint_failures.append({"P_corner":native,"Q_corner":qnative,
                                                      "angle_sum":total,"remaining":360-total})
                    assert endpoint_failures
                    parents.append({"P_native_side":i,"Q_native_side":j,"determinant":determinant,
                                    "reverse_endpoints":reverse,"Q_placement":polygon(image),
                                    "boundary":polygon(boundary),"corners":len(boundary),"reflex_corners":reflex,
                                    "status":"NONCONVEX_PARENT" if reflex else "CONVEX_PARENT_OUTSIDE_DOMAIN",
                                    "plane_extension":"IMPOSSIBLE_NATIVE_SEAM_ENDPOINT",
                                    "endpoint_failures":endpoint_failures})
    result={"field":{"polynomial":"g^4-10*g^2+1","embedding":"g=sqrt(2)+sqrt(3)",
                     "coefficient_order":"1,g,g^2,g^3"},
            "atoms":{"P_vertices":polygon(P),"Q_vertices":polygon(Q),
                     "P_angles_degrees":[90,120,120,90,120],"Q_angles_degrees":[90,135,135,90,135,135],
                     "P_area":encode(area(P)),"Q_area":encode(area(Q))},
            "counts":{"native_attachments":attachments,"nonconvex_parents":sum(p["reflex_corners"]>0 for p in parents)},
            "parents":parents,"inflation":2,"inflated_atomic_counts":[4,4],
            "partial_contact_gate":{"domain":"216 oriented PPP120 stars; one90-guest completion per unequal ray",
                                    "records":star_records,
                                    "survivors":sum(t["status"]=="LOCAL_COMPLETION_SURVIVOR" for t in star_records),
                                    "P4_survivors":sum(t["status"]=="LOCAL_COMPLETION_SURVIVOR" and 4 in t["native_corners"] for t in star_records)},
            "completion":"COMPLETE: ALL_FULL_EDGE_PARENTS_NONEXTENDIBLE; BOUNDED_T_TEST_RETAINED"}
    output=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:args.output.write_text(output)
    else:print(output,end="")


if __name__=="__main__":main()
