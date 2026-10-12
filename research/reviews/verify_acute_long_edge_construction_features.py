#!/usr/bin/env python3
"""Exact local acute-pentagon construction features, not a tiling proof.
Checks geometry before any motif enumeration; no SAT or numeric geometry.
"""
import argparse
import itertools
import json
from pathlib import Path
from sage.all import AA, QQ, QuadraticField

K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()


def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def cross(x,y):return x[0]*y[1]-x[1]*y[0]
def dot(x,y):return x[0]*y[0]+x[1]*y[1]

def area(P):return sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2

def convex(P):
    assert area(P)>0
    for i in range(len(P)):
        edge=sub(P[(i+1)%len(P)],P[i])
        assert all(cross(edge,sub(P[j],P[i]))>0 for j in range(len(P)) if j not in (i,(i+1)%len(P)))


def disjoint(P,Q):
    P=P if area(P)>0 else P[::-1]
    Q=Q if area(Q)>0 else Q[::-1]
    return any(all(cross(sub(V[(i+1)%len(V)],V[i]),sub(p,V[i]))<=0 for p in U)
               for V,U in ((P,Q),(Q,P)) for i in range(len(V)))


def pentagon(c,d,e):
    c,d,e=map(K,(c,d,e)); b=e+(d-c)/r;a=e+(c+2*d)/r
    assert min(a,b,c,d,e)>0
    directions=[(1,0),(-K(1)/2,r/2),(-r/2,K(1)/2),(-r/2,-K(1)/2),(-K(1)/2,-r/2)]
    lengths=[a,b,c,d,e];P=[(K(0),K(0))]
    for h,u in zip(lengths,directions):P.append(add(P[-1],(h*u[0],h*u[1])))
    assert P[-1]==(0,0);P=P[:-1];convex(P)
    cosine=[K(1)/2,K(1)/2,-r/2,-K(1)/2,-r/2]
    for i in range(5):
        incoming=sub(P[i-1],P[i]);outgoing=sub(P[(i+1)%5],P[i])
        assert dot(incoming,outgoing)==lengths[i-1]*lengths[i]*cosine[i]
    return P,lengths


def transform(P,cosine,sine,translation=(0,0),reflect=False):
    out=[]
    for x,y in P:
        if reflect:y=-y
        out.append(add((cosine*x-sine*y,sine*x+cosine*y),translation))
    return out


def translate_corner(P,cosine,sine,corner,point,reflect=False):
    R=transform(P,cosine,sine,reflect=reflect)
    return transform(P,cosine,sine,sub(point,R[corner]),reflect)


def encode_number(x):
    return [[int(QQ(c).numerator()),int(QQ(c).denominator())] for c in K(x).list()]


def encode_poly(P):return [[encode_number(x),encode_number(y)] for x,y in P]



def boundary_arcs(polys):
    vertices={v for P in polys for v in P}; arcs=set()
    for P in polys:
        if area(P)<0:P=P[::-1]
        for i,u in enumerate(P):
            v=P[(i+1)%len(P)]; edge=sub(v,u); norm=dot(edge,edge)
            points=sorted((dot(sub(p,u),edge)/norm,p) for p in vertices
                          if cross(edge,sub(p,u))==0 and 0<=dot(sub(p,u),edge)<=norm)
            for (_,p),(_,q) in zip(points,points[1:]):
                if (q,p) in arcs:arcs.remove((q,p))
                else:arcs.add((p,q))
    successors={}
    for p,q in arcs:
        assert p not in successors;successors[p]=q
    start=min(successors);v=start;boundary=[]
    while True:
        boundary.append(v);v=successors[v]
        if v==start:break
    assert len(boundary)==len(arcs)
    assert area(boundary)==sum(abs(area(P)) for P in polys)
    return arcs,boundary


def convex_intersection(P,Q):
    P=P if area(P)>0 else P[::-1]
    Q=Q if area(Q)>0 else Q[::-1]
    clipped=list(P)
    for i,u in enumerate(Q):
        v=Q[(i+1)%len(Q)];edge=sub(v,u)
        result=[]
        if not clipped:break
        previous=clipped[-1];pv=cross(edge,sub(previous,u))
        for current in clipped:
            cv=cross(edge,sub(current,u))
            if (pv>=0)!=(cv>=0):
                alpha=pv/(pv-cv)
                result.append(add(previous,(alpha*(current[0]-previous[0]),alpha*(current[1]-previous[1]))))
            if cv>=0:result.append(current)
            previous,pv=current,cv
        clipped=[]
        for x in result:
            if not clipped or clipped[-1]!=x:clipped.append(x)
        if len(clipped)>1 and clipped[0]==clipped[-1]:clipped.pop()
    return clipped

def old_budget():
    full=[]
    for flat in range(2):
        for n60,n90,n150 in itertools.product(range(7),repeat=3):
            if not n60+n90+n150:continue
            if 60*n60+90*n90+150*n150+180*flat!=360:continue
            potential=2*n60-n150
            assert potential>=0
            if n60 and potential==0:assert (n60,n90,n150,flat)==(1,0,2,0)
            full.append(dict(native60=n60,native90=n90,native150=n150,flat=flat,potential=potential))
    phi=(1+AA(5).sqrt())/2;s3=AA(3).sqrt()
    A=-5*s3/2-AA(1)/8+AA(5).sqrt()/8+5*AA(15).sqrt()/4
    B0=-AA(15).sqrt()/24+s3/8+AA(1)/4+AA(5).sqrt()/4
    Bmin=B0-s3*(s3-phi)**2/6
    assert AA(3)/4<A/B0<A/Bmin<AA(4)/5
    return dict(native_weights={'60':2,'90':0,'150':-1},tile_sum=0,
                allowed_vertex_types=full,acute_cap_potential=6,
                old_endpoint_deficit_degrees=30,minimum_native_angle=60,
                old_fixed_family_area_ratio_interval=['3/4','4/5'],
                inflation_phi_area_route_excluded=True)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    args=p.parse_args()
    A,LA=pentagon(4,3,1)
    B,LB=pentagon(2*r-K(10)/3,2*r-K(10)/3,10/r-2)
    a,b,c,d,e=LA
    assert LB[0]==c and LB[4]==a-d
    assert LA[2]!=LA[4] and LA[1]!=LA[3]
    assert LB[2]!=LB[4] and LB[1]!=LB[3]
    # Exact three-tile 180+120+60 module with an unsplit cross seam.
    q=(d,K(0))
    A120=translate_corner(A,r/2,-K(1)/2,3,q)
    B60=transform(B,K(1)/2,-r/2,q)
    assert A120[4]==A[0] and B60[4]==A[1]
    assert A120[2]==B60[1]
    module3=[A,A120,B60]
    assert all(disjoint(P,Q) for P,Q in itertools.combinations(module3,2))
    # Genuine four-tile acute partial contact, with a reflected child.
    q4=(a-e,K(0));assert 0<q4[0]<a
    P180=transform(A,-1,0,q4)
    Pmirror=transform(A,K(1)/2,-r/2,q4,True)
    P300=transform(A,K(1)/2,-r/2,q4)
    module4=[A,P180,Pmirror,P300]
    assert P180[4]==Pmirror[4]
    assert Pmirror[1]==P300[1]
    assert P300[4]==A[1]
    assert P180[1]==(-e,0)
    assert all(disjoint(P,Q) for P,Q in itertools.combinations(module4,2))
    # Reapply the cap to the first rotated tile's partially occupied a.
    # It reuses the original source and adds precisely two upper copies.
    P120mirror=transform(A,-K(1)/2,r/2,reflect=True)
    P120=transform(A,-K(1)/2,r/2)
    module6=module4+[P120mirror,P120]
    assert all(disjoint(P,Q) for P,Q in itertools.combinations(module6,2))
    assert A[4]==P120mirror[4]
    assert P120mirror[1]==P120[1]
    assert P120[4]==P180[1]
    arcs,boundary=boundary_arcs(module6)
    assert len(boundary)==18
    # Exact positive-width periodic strip: copies share one whole c edge.
    period=(K(5)*r/3+1,r+1)
    translated=[transform(P,1,0,period) for P in module6]
    assert all(disjoint(P,Q) for P in module6 for Q in translated)
    matched=[(p,q) for p,q in arcs if (sub(q,period),sub(p,period)) in arcs]
    assert len(matched)==1
    assert dot(sub(matched[0][1],matched[0][0]),sub(matched[0][1],matched[0][0]))==c*c
    allvertices={v for P in module6 for v in P}
    projection_width=max(dot(v,period) for v in allvertices)-min(dot(v,period) for v in allvertices)
    period_norm=dot(period,period)
    assert period_norm<projection_width<2*period_norm
    # The natural full-c/A to long-a/B bridge is physically unique because
    # B is symmetric across its a-side perpendicular bisector.
    assert {(LB[0]-x,y) for x,y in B}==set(B)
    exposed_c=sorted((p,q) for p,q in arcs
                     if dot(sub(q,p),sub(q,p))==c*c
                     and (sub(q,period),sub(p,period)) not in arcs
                     and (add(q,period),add(p,period)) not in arcs)
    assert len(exposed_c)==4
    bridges=[]
    for p,q in exposed_c:
        direction=sub(p,q)
        bridges.append(transform(B,direction[0]/LB[0],direction[1]/LB[0],q))
    overlap_witnesses=[]
    for bi,bridge in enumerate(bridges):
        for n in (-1,0,1):
            for ai,P in enumerate(module6):
                shifted=transform(P,1,0,(n*period[0],n*period[1]))
                if disjoint(bridge,shifted):continue
                intersection=convex_intersection(bridge,shifted)
                assert len(intersection)>=3 and area(intersection)>0
                point=(sum(x for x,y in intersection)/len(intersection),
                       sum(y for x,y in intersection)/len(intersection))
                for polygon in (bridge,shifted):
                    if area(polygon)<0:polygon=polygon[::-1]
                    assert all(cross(sub(polygon[(i+1)%len(polygon)],polygon[i]),sub(point,polygon[i]))>0
                               for i in range(len(polygon)))
                overlap_witnesses.append(dict(B_bridge_index=bi,A_cell_period=n,A_face_index=ai,
                                               intersection=encode_poly(intersection),
                                               strict_interior_point=[encode_number(x) for x in point]))
    assert len(overlap_witnesses)==2
    # Hence shifts by >=2 periods are strictly separated by projection,
    # and shifts by one period were checked polygon by polygon above.
    result=dict(scope='Exact feature and endpoint gates only; global existence, mixed periodic exclusion and unrestricted forcing remain unresolved',
                field='Q(r), r=sqrt(3), coefficient basis1,r',
                angle_word=[60,60,150,120,150],
                A_parameters=[encode_number(v) for v in (4,3,1)],
                B_parameters=[encode_number(v) for v in (2*r-K(10)/3,2*r-K(10)/3,10/r-2)],
                A_lengths=[encode_number(v) for v in LA],B_lengths=[encode_number(v) for v in LB],
                three_tile_module=[encode_poly(P) for P in module3],
                three_tile_junction=[encode_number(v) for v in q],
                three_tile_sectors=[180,120,60],
                four_tile_module=[encode_poly(P) for P in module4],
                four_tile_junction=[encode_number(v) for v in q4],
                four_tile_sectors=[180,60,60,60],
                four_tile_remaining_endpoint_sectors=[120,150,60,240],
                six_tile_module=[encode_poly(P) for P in module6],
                six_tile_boundary=encode_poly(boundary),
                cap_propagation_arrests=True,
                strip_period=[encode_number(v) for v in period],
                strip_shared_edge=[[encode_number(x),encode_number(y)] for x,y in matched[0]],
                strip_nonadjacent_copies_separated=True,
                strip_is_full_plane_tiling=False,
                B_bridge_edges=[[encode_poly([p,q])] for p,q in exposed_c],
                B_bridge_polygons=[encode_poly(P) for P in bridges],
                B_bridge_geometry_unique_up_to_native_reflection=True,
                B_bridge_overlaps=overlap_witnesses,
                full_c_to_B_a_bridge_rejected=True,
                old_family_gates=old_budget())
    normalized=json.loads(json.dumps(result))
    if args.check:assert json.loads(args.check.read_text())==normalized
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact strict convexity, angles, closure, pairwise-disjoint 3/4/6-tile modules and infinite periodic strip, native seams, exact B bridge overlap witnesses, old acute budget and area-route gates. NO plane tiling or forcing claim.')

if __name__=='__main__':main()
