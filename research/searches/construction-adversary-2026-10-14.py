"""Exact counterexample checks used inside the 2026-10-14 construction loop.
The Python API accepts Sage exact real polygon coordinates, indexed cyclically.
Explicit periodic witnesses are conclusive; failed restricted witness searches
return NO_WITNESS_IN_DOMAIN, never an aperiodicity or untileability verdict.
"""
from sage.all import AA, QQ, QQbar, matrix, vector
from itertools import product, combinations
import argparse, json
from pathlib import Path

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(P): return sum(cross(a,b) for a,b in zip(P,P[1:]+P[:1]))/2

def ccw(P):
    P=list(P)
    assert area(P)!=0
    return P if area(P)>0 else list(reversed(P))

def strict_convex(P):
    F=ccw(P)
    return all(cross(F[(i+1)%len(F)]-a,z-a)>0
               for i,a in enumerate(F) for j,z in enumerate(F)
               if j not in (i,(i+1)%len(F)))

def intersection(P,Q):
    out=ccw(P); Q=ccw(Q)
    for a,b in zip(Q,Q[1:]+Q[:1]):
        if not out: break
        last=out[-1]; dl=cross(b-a,last-a); new=[]
        for point in out:
            dp=cross(b-a,point-a)
            if (dl<0)!=(dp<0): new.append(last+(point-last)*dl/(dl-dp))
            if dp>=0:new.append(point)
            last=point;dl=dp
        out=new
    return out

def disjoint_interiors(P,Q):
    assert strict_convex(P) and strict_convex(Q)
    # Independent separating-axis formulation; no winding assumption.
    for F in [P,Q]:
        for a,b in zip(F,F[1:]+F[:1]):
            n=vector(AA,[-(b-a)[1],(b-a)[0]])
            pp=[n.dot_product(p) for p in P];qq=[n.dot_product(q) for q in Q]
            if max(pp)<=min(qq) or max(qq)<=min(pp):return True
    return False

def congruent(P,Q):
    if len(P)!=len(Q):return False
    n=len(P)
    return any(all((P[i]-P[j]).dot_product(P[i]-P[j])==
                   (Q[(s+d*i)%n]-Q[(s+d*j)%n]).dot_product(Q[(s+d*i)%n]-Q[(s+d*j)%n])
                   for i in range(n) for j in range(n)) for s in range(n) for d in [-1,1])

def native_attachments(P,A,B):
    """Every indexed full-side attachment, including aliases and reflections.
    Preserve original source vertex indexing; only geometric dedup users may
    quotient distinct records with identical vertex sets afterwards.
    """
    result=[];target=B-A
    for i,a in enumerate(P):
        b=P[(i+1)%len(P)];e=b-a
        if e.dot_product(e)!=target.dot_product(target):continue
        for reverse in [False,True]:
            ta,tb=(B,A) if reverse else (A,B);f=tb-ta
            E=matrix(AA,[[e[0],-e[1]],[e[1],e[0]]])
            for determinant in [-1,1]:
                F=matrix(AA,[[f[0],-determinant*f[1]],[f[1],determinant*f[0]]])*E.inverse()
                image=[ta+F*(p-a) for p in P]
                centre=sum(image,vector(AA,[0,0]))/len(image)
                if cross(target,centre-A)<0:
                    result.append({'native_side':i,'determinant':determinant,
                                   'reverse_endpoints':reverse,'vertices':image})
    return result

def periodic_witness(prototypes,representatives,L,U):
    """Verify an explicit unsplit full-native-edge lattice witness.
    A complete reversed boundary and area/covolume1 prove a plane tiling.
    This checks supplied shifts without a finite translation-radius bound.
    """
    if cross(L,U)==0:return {'status':'INVALID_WITNESS','reason':'singular lattice'}
    reps=[ccw(F) for F in representatives]
    if not all(strict_convex(F) and any(congruent(F,P) for P in prototypes) for F in reps):
        return {'status':'INVALID_WITNESS','reason':'invalid shape/congruence'}
    basis=matrix(AA,[list(L),list(U)]).transpose();inverse=basis.inverse()
    edges={(f,i):(a,F[(i+1)%len(F)]) for f,F in enumerate(reps) for i,a in enumerate(F)}
    partners={}
    for label,(a,b) in edges.items():
        matches=[]
        for other,(c,d) in edges.items():
            shift=inverse*(a-d)
            if all(z in QQ and QQ(z).denominator()==1 for z in shift) and b==c+basis*shift:
                if other==label and all(z==0 for z in shift):continue
                matches.append((other,tuple(int(QQ(z)) for z in shift)))
        if len(matches)!=1:return {'status':'INVALID_WITNESS','reason':'unpaired or multiply paired full edge','edge':list(label),'matches':len(matches)}
        partners[label]=matches[0]
    for label,(other,shift) in partners.items():
        assert partners[other]==(label,tuple(-z for z in shift))
    if sum(area(F) for F in reps)!=abs(cross(L,U)):
        return {'status':'INVALID_WITNESS','reason':'area/covolume differs from one'}
    return {'status':'PERIODIC_ESCAPE','representatives':len(reps),'atomic_edges':len(edges),
            'pairs':[[list(label),list(other),list(shift)] for label,(other,shift) in sorted(partners.items())]}

def omission_search(P):
    """One constructive triangle/quadrilateral domain; not pentagon recognition."""
    if not strict_convex(P):return {'status':'INVALID_POLYGON'}
    F=ccw(P);n=len(F)
    if n==3:
        second=[F[1]+F[2]-p for p in F]
        return periodic_witness([F],[F,second],F[1]-F[0],F[2]-F[0])
    if n==4:
        second=[F[0]+F[1]-p for p in F]
        return periodic_witness([F],[F,second],F[2]-F[0],F[3]-F[1])
    # Finite two-copy halfturn domain: every anchor side, every pair of
    # native seam-midpoint gains as candidate lattice generators.
    attempts=0
    for anchor in range(n):
        centre_sum=F[anchor]+F[(anchor+1)%n]
        second=[centre_sum-p for p in F]
        gains=[F[i]+F[(i+1)%n]-centre_sum for i in range(n) if i!=anchor]
        for L,U in combinations(gains,2):
            if cross(L,U)==0:continue
            attempts+=1
            answer=periodic_witness([F],[F,second],L,U)
            if answer['status']=='PERIODIC_ESCAPE':
                answer['domain']='two-copy native-halfturn seam-gain lattice'
                answer['anchor_side']=anchor;answer['attempts']=attempts
                return answer
    return {'status':'NO_WITNESS_IN_DOMAIN','domain':'two-copy native-halfturn seam-gain lattices','attempts':attempts,'sides':n}

def straight_side_inflation_gate(parent,children,angles,inflation):
    """Exact no-flat-star necessary gate for a fixed polygonal dissection.
    Parent may be nonconvex; all children must be genuine convex polygons.
    """
    flat=angle_stars(angles,QQ(1))
    if flat:return {'status':'NOT_EXCLUDED_BY_STRAIGHT_SIDE_GATE','flat_stars':flat}
    parent_max=max((b-a).norm() for a,b in zip(parent,parent[1:]+parent[:1]))
    child_max=max((b-a).norm() for F in children for a,b in zip(F,F[1:]+F[:1]))
    if inflation*parent_max>child_max:
        return {'status':'NO_DISSECTION_IN_FIXED_NO_FLAT_DOMAIN','reason':'inflated genuine parent side exceeds every native child edge'}
    return {'status':'NOT_EXCLUDED_BY_STRAIGHT_SIDE_GATE','flat_stars':[]}

def angle_stars(angles,total):
    result=[]
    for counts in product(*(range(int(total/a)+1) for a in angles)):
        if sum(a*n for a,n in zip(angles,counts))==total:result.append(list(counts))
    return result

def palette_obstruction(angles):
    full=angle_stars(angles,QQ(2));flat=angle_stars(angles,QQ(1))
    return {'status':'UNTILEABLE_ANGLE_PALETTE' if not full and not flat else 'NOT_EXCLUDED_BY_ANGLE_PALETTE',
            'full_stars':full,'flat_stars':flat}

def regular(n):
    z=QQbar.zeta(n)
    return [vector(AA,[(z**k).real(),(z**k).imag()]) for k in range(n)]

def controls():
    square=[vector(AA,p) for p in [(0,0),(1,0),(1,1),(0,1)]]
    winding=[]
    for a in [square,list(reversed(square))]:
        for b in [square,list(reversed(square))]:
            I=intersection(a,b);assert area(I)==1
            assert not disjoint_interiors(a,b);winding.append(True)
    near=[p+vector(AA,[QQ(1)/2,0]) for p in square]
    far=[p+vector(AA,[1,0]) for p in square]
    assert not disjoint_interiors(square,near) and disjoint_interiors(square,far)
    square_fit=native_attachments(square,vector(AA,[0,0]),vector(AA,[1,0]))
    assert len(square_fit)==8 and {r['native_side'] for r in square_fit}==set(range(4))
    assert {r['determinant'] for r in square_fit}=={-1,1}
    omit=omission_search(square);assert omit['status']=='PERIODIC_ESCAPE'
    damaged=periodic_witness([square],[square],vector(AA,[2,0]),vector(AA,[0,1]))
    assert damaged['status']=='INVALID_WITNESS'
    # Independently reconstruct the reviewed right-P / regular-Q8 carrier.
    r=AA(2).sqrt();s=r;a=1+s;d=1+s;W=2*a+1
    Q=[vector(AA,p) for p in [(a,1),(1,d),(-1,d),(-a,1),(-a,-1),(-1,-d),(1,-d),(a,-1)]]
    P=[vector(AA,p) for p in [(0,-1),(1,-s),(1+s,0),(1,s),(0,1)]]
    reps=[Q,[p+vector(AA,[a,0]) for p in P],
          [vector(AA,[-p[0]+a+1,p[1]+d]) for p in P]]
    carrier=periodic_witness([P,Q],reps,vector(AA,[W,d]),vector(AA,[0,2*d]))
    assert carrier['status']=='PERIODIC_ESCAPE'
    untileable=palette_obstruction([QQ(3)/5,QQ(3)/4]);assert untileable['status']=='UNTILEABLE_ANGLE_PALETTE'
    assert strict_convex(regular(5)) and strict_convex(regular(8))
    return {'winding_controls':winding,'square_alias_attachments':len(square_fit),
            'overlap_and_tangent_controls':'PASS','square_omission':omit,
            'damaged_periodic_witness':damaged,'reviewed_right_palette_carrier':carrier,
            'regular_pentagon_regular_octagon_untileable':untileable}

def pentagon_hexagon_application():
    r2=AA(2).sqrt();r3=AA(3).sqrt();r6=r2*r3
    P=[vector(AA,z) for z in [(0,0),(3,0),(4,r3),(QQ(7)/2,3*r3/2),(0,1/r3)]]
    Q=[vector(AA,z) for z in [(0,0),(3,0),(3+1/r6,1/r6),(3+1/r6,7/r3+1/r6),(r2,7/r3+1/r6),(0,7/r3+1/r6-r2)]]
    assert strict_convex(P) and strict_convex(Q)
    p_angles=[QQ(1)/2,QQ(2)/3,QQ(2)/3,QQ(1)/2,QQ(2)/3]
    q_angles=[QQ(1)/2,QQ(3)/4,QQ(3)/4,QQ(1)/2,QQ(3)/4,QQ(3)/4]
    palette=[QQ(1)/2,QQ(2)/3,QQ(3)/4]
    records=[]
    for j,a in enumerate(Q):
        b=Q[(j+1)%6]
        for item in native_attachments(P,a,b):
            i=item['native_side'];T=item['vertices'];bad=[]
            for target,point in [(j,a),((j+1)%6,b)]:
                pi=next(k for k,z in enumerate(T) if z==point)
                remaining=2-p_angles[pi]-q_angles[target]
                possibilities=angle_stars(palette,remaining) if remaining>=0 else []
                # The third sector may instead be a flat host.
                if remaining!=1 and not possibilities:bad.append(target)
            records.append({'Q_side':j,'P_side':i,'determinant':item['determinant'],
                            'reverse_endpoints':item['reverse_endpoints'],
                            'forbidden_endpoint_indices':bad})
    omissionP=omission_search(P);omissionQ=omission_search(Q)
    return {'candidate':'mixed pentagon/hexagon nonconvex-parent repair',
            'strict_convexity':'PASS','P_omission':omissionP,'Q_omission':omissionQ,
            'native_mixed_attachments':records,
            'admissible_attachment_count':sum(not r['forbidden_endpoint_indices'] for r in records),
            'scope':'endpoint failures exclude only those full native seams; absent periodic witness is inconclusive'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output');parser.add_argument('--check')
    args=parser.parse_args();result={'schema':'construction-adversary-v1','controls':controls(),'live_pentagon_hexagon':pentagon_hexagon_application()}
    if args.check:assert json.loads(Path(args.check).read_text())==result
    if args.output:
        with Path(args.output).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
