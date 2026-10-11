#!/usr/bin/env python3
"""Twelve exact closures and the forced regular-pentagon collar of a Q chain.

Native Q angles108 at0 and gap in2,3,4; otherwise144. One private edge
is chosen at each alpha corner. All other sides are unit. This is a
complete twelve-case domain up to dihedral alpha-gap normalization, not
an unbounded tiling search. Two unknown lengths are solved exactly. A
parallel branch is rejected if inconsistent or if private equality is forced.

For each eligible branch, construct the unique regular P across all six
unit sides of both Q-chain motifs, normalize duplicates modulo its two-step
period, and check every potentially overlapping integer chain shift exactly.
The mandatory-P assertion here uses the reviewed defect-free chain limit.
A positive overlap would exclude this metric branch; zero overlaps do not
establish a plane extension. For the two outgoing-private representatives,
eight exact maps place Q at a prescribed third-Q side of a forced P.
Only maps with parallel axes survive the proved chain geometry; their
joint forced collars are checked with the same complete shift domain.
Zero-overlap, area-equal bands are retained for a separate global assembly
proof. No random seed, solver, or timeout is used.
"""
from sage.all import AA, QQ, QQbar, RIF, vector, matrix, ceil, floor
from itertools import product
import json

Z = QQbar.zeta(10)
I = QQbar.gen()


def vdir(k):
    z = Z**k
    return vector(AA,[z.real(),z.imag()])


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def area(poly):
    if len(poly)<3:
        return AA(0)
    return sum(cross(poly[j],poly[(j+1)%len(poly)]) for j in range(len(poly)))/2


def clip(subject,clipper):
    result=list(subject)
    for j in range(len(clipper)):
        if not result:
            break
        old,result=result,[]
        edge=clipper[(j+1)%len(clipper)]-clipper[j]
        previous=old[-1]
        hp=cross(edge,previous-clipper[j])
        for current in old:
            hc=cross(edge,current-clipper[j])
            if (hp>=0)!=(hc>=0):
                result.append(previous+(current-previous)*hp/(hp-hc))
            if hc>=0:
                result.append(current)
            previous,hp=current,hc
    return result


def exact(x):
    x=AA(x)
    if x in QQ:
        return {'rational':str(QQ(x))}
    interval=x.interval(RIF)
    lo,hi=interval.lower().exact_rational(),interval.upper().exact_rational()
    poly=x.minpoly()
    assert sum(lo<r<hi for r in poly.roots(AA,multiplicities=False))==1
    return {'polynomial_coefficients':[str(QQ(c)) for c in poly.list()],
            'isolating_interval':[str(lo),str(hi)]}


def points(poly):
    return [[exact(c) for c in p] for p in poly]


def convex(poly):
    return area(poly)>0 and all(cross(poly[(j+1)%len(poly)]-poly[j],poly[k]-poly[j])>0
                               for j in range(len(poly)) for k in range(len(poly))
                               if k not in (j,(j+1)%len(poly)))


def regular_across(poly,j):
    origin=poly[(j+1)%len(poly)]
    first=poly[j]-origin
    result=[origin]
    z=QQbar(first[0])+I*QQbar(first[1])
    for k in range(5):
        unit=z*Z**(2*k)
        result.append(result[-1]+vector(AA,[unit.real(),unit.imag()]))
    assert result[-1]==result[0] and convex(result[:-1])
    return result[:-1]


def canonical(poly,u):
    center=sum(poly,vector(AA,[0,0]))/len(poly)
    shift=floor(center.dot_product(u)/u.dot_product(u))
    return tuple(sorted(tuple(p-shift*u) for p in poly))


def shifts(a,b,u):
    den=u.dot_product(u)
    ax=[p.dot_product(u)/den for p in a]
    bx=[p.dot_product(u)/den for p in b]
    lo=ceil(min(ax)-max(bx))
    hi=floor(max(ax)-min(bx))
    return range(int(lo),int(hi)+1)


def chain_collisions(polys,u):
    collisions=[]
    comparisons=0
    for i,j in product(range(len(polys)),repeat=2):
        for n in shifts(polys[i],polys[j],u):
            if i==j and n==0:
                continue
            intersection=clip(polys[i],[p+n*u for p in polys[j]])
            overlap=area(intersection)
            comparisons+=1
            if overlap>0:
                collisions.append({'first':i,'second':j,'shift':n,
                                   'intersection':points(intersection),
                                   'overlap_area':exact(overlap)})
    return comparisons,collisions




def plane_overlaps(polys,u,v):
    basis=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    assert basis.det()!=0
    inv=basis.inverse()
    coordinates=[[inv*p for p in poly] for poly in polys]
    comparisons=0
    for i,j in product(range(len(polys)),repeat=2):
        bounds=[]
        for axis in range(2):
            lo=ceil(min(p[axis] for p in coordinates[i])-max(p[axis] for p in coordinates[j]))
            hi=floor(max(p[axis] for p in coordinates[i])-min(p[axis] for p in coordinates[j]))
            bounds.append(range(int(lo),int(hi)+1))
        for n,m in product(*bounds):
            if i==j and n==m==0:
                continue
            assert area(clip(polys[i],[p+n*u+m*v for p in polys[j]]))==0,(i,j,n,m)
            comparisons+=1
    assert sum(area(poly) for poly in polys)==abs(basis.det())
    return comparisons


def same_edge(a,j,b,k):
    return ((a[j]==b[k] and a[(j+1)%len(a)]==b[(k+1)%len(b)]) or
            (a[j]==b[(k+1)%len(b)] and a[(j+1)%len(a)]==b[k]))


def halfplane_clip(poly,value):
    if not poly:
        return []
    result=[]
    previous=poly[-1]
    hp=value(previous)
    for current in poly:
        hc=value(current)
        if (hp>=0)!=(hc>=0):
            result.append(previous+(current-previous)*hp/(hp-hc))
        if hc>=0:
            result.append(current)
        previous,hp=current,hc
    return result


def third_q_candidates(Q,second,collar,lengths,gap,a,b,u):
    """Eight beta/beta side maps at one forced third-Q side, no period search."""
    chosen=None
    for j in range(8):
        if lengths[j]!=1:
            continue
        P=regular_across(Q,j)
        matched=[k for k in (1,4) if any(same_edge(P,k,second,l) for l in range(8))]
        if matched:
            assert len(matched)==1
            chosen=(P,j,matched[0])
            break
    assert chosen is not None
    P,j,paired=chosen
    third=3 if paired==1 else 2
    target=P[(third+1)%5]-P[third]
    eP=QQbar(target[0])+I*QQbar(target[1])
    rows=[]
    beta_sides=[j for j in range(8) if lengths[j]==1 and
                j not in (0,gap) and (j+1)%8 not in (0,gap)]
    assert len(beta_sides)==4
    for side,parity in product(beta_sides,(1,-1)):
        eq=Q[(side+1)%8]-Q[side]
        eQ=QQbar(eq[0])+I*QQbar(eq[1])
        if parity==1:
            r=-eP/eQ
            L=matrix(AA,[[r.real(),-r.imag()],[r.imag(),r.real()]])
            t=P[(third+1)%5]-L*Q[side]
        else:
            r=eP/eQ.conjugate()
            L=matrix(AA,[[r.real(),r.imag()],[r.imag(),-r.real()]])
            t=P[third]-L*Q[side]
        assert L.transpose()*L==matrix.identity(AA,2)
        row={'Q_side':side,'orientation_parity':parity}
        if cross(L*(b-a),b-a)!=0:
            row['status']='axis not parallel'
            rows.append(row)
            continue
        new_axis=L*a+t
        separation=cross(u,new_axis-a)
        row['linear_matrix']=[[exact(c) for c in rr] for rr in L.rows()]
        row['translation']=[exact(c) for c in t]
        if separation==0:
            row['status']='coincident axis'
            rows.append(row)
            continue
        joint=[]
        seen=set()
        for poly in [Q,second]+collar+[[L*v+t for v in poly] for poly in [Q,second]+collar]:
            if area(poly)<0:
                poly=list(reversed(poly))
            key=canonical(poly,u)
            if key not in seen:
                seen.add(key)
                joint.append(poly)
        comparisons,collisions=chain_collisions(joint,u)
        row['joint_comparisons']=comparisons
        row['joint_collision_count']=len(collisions)
        if collisions:
            row['status']='forced collar overlap'
            row['first_collision']=collisions[0]
            rows.append(row)
            continue
        sign=1 if separation>0 else -1
        pieces=[]
        for poly in joint:
            q=halfplane_clip(poly,lambda v:sign*cross(u,v-a))
            q=halfplane_clip(q,lambda v:-sign*cross(u,v-new_axis))
            pieces.append(q)
        actual=sum(area(piece) for piece in pieces)
        expected=abs(separation)
        row.update(status='complete periodic band' if actual==expected else 'band area deficit',
                   band_area=exact(actual),band_covolume=exact(expected),
                   band_tiles=[points(poly) for poly,piece in zip(joint,pieces) if area(piece)>0],
                   band_tile_count=sum(area(piece)>0 for piece in pieces),
                   band_pieces=[points(piece) for piece in pieces if area(piece)>0])
        assert actual<=expected
        assert all(area(piece)==0 or len(poly)!=5 or area(piece)==area(poly)
                   for poly,piece in zip(joint,pieces))
        if actual==expected and L==matrix.identity(AA,2):
            band_p=[poly for poly,piece in zip(joint,pieces) if len(poly)==5 and area(piece)>0]
            assert len(band_p)==4
            motif=[Q,second]+band_p
            phi=(1+AA(5).sqrt())/2
            sine=AA(Z.imag())
            assert gap==3
            assert u==vector(AA,[(1+3*phi)/2,sine*(2+3*phi)])
            assert t==vector(AA,[phi+2,-2*phi*sine])
            assert area(Q)==sine*(9*phi+8)/2
            assert all(area(poly)==sine*(3*phi+1)/2 for poly in band_p)
            expected_p=[regular_across(Q,1),regular_across(Q,2),
                        regular_across(second,5),regular_across(second,6)]
            assert [canonical(poly,u) for poly in band_p]==[canonical(poly,u) for poly in expected_p]
            assert abs(cross(u,t))==5*sine*(3*phi+2)
            count=plane_overlaps(motif,u,t)
            row['whole_plane_witness']={'motif':[points(poly) for poly in motif],
                                       'lattice':[[exact(c) for c in u],[exact(c) for c in t]],
                                       'complete_lattice_overlap_comparisons':count,
                                       'area_sum':exact(sum(area(poly) for poly in motif)),
                                       'lattice_covolume':exact(abs(cross(u,t)))}
        rows.append(row)
    assert len(rows)==8
    return {'P_Q_side':j,'P_known_second_Q_side':paired,'P_third_Q_side':third,'rows':rows}


def main():
    if not __debug__:
        raise RuntimeError("Run without optimization: proof checks must execute.")
    rows=[]
    for gap in (2,3,4):
        directions=[vdir(j+(j>=gap)) for j in range(8)]
        total=sum(directions,vector(AA,[0,0]))
        for ix,iy in product((7,0),(gap-1,gap)):
            row={'alpha_gap':gap,'private_sides':[ix,iy]}
            M=matrix(AA,[[directions[ix][k],directions[iy][k]] for k in range(2)])
            if M.det()==0:
                assert directions[ix]==-directions[iy]
                if total==vector(AA,[0,0]):
                    row['status']='parallel closure forces equal private lengths'
                else:
                    assert cross(directions[ix],total)!=0
                    row['status']='parallel closure inconsistent'
                rows.append(row)
                continue
            adjust=M.solve_right(-total)
            lengths=[AA(1)]*8
            lengths[ix]+=adjust[0]
            lengths[iy]+=adjust[1]
            row['private_lengths']=[exact(lengths[ix]),exact(lengths[iy])]
            if not all(length>0 for length in lengths):
                row['status']='nonpositive side'
            elif lengths[ix]==1 or lengths[iy]==1:
                row['status']='private side unit'
            elif lengths[ix]==lengths[iy]:
                row['status']='private lengths equal'
            else:
                Q=[vector(AA,[0,0])]
                for length,direction in zip(lengths,directions):
                    Q.append(Q[-1]+length*direction)
                assert Q[-1]==Q[0]
                Q=Q[:-1]
                assert convex(Q)
                a=(Q[ix]+Q[(ix+1)%8])/2
                b=(Q[iy]+Q[(iy+1)%8])/2
                u=2*(b-a)
                assert u!=vector(AA,[0,0])
                second=[2*b-p for p in Q]
                collar=[]
                seen=set()
                for motif in (Q,second):
                    for j in range(8):
                        if lengths[j]!=1:
                            continue
                        P=regular_across(motif,j)
                        key=canonical(P,u)
                        if key not in seen:
                            seen.add(key)
                            collar.append(P)
                comparisons,collisions=chain_collisions([Q,second]+collar,u)
                if (gap,ix,iy) in ((2,0,2),(3,0,3)) and not collisions:
                    row['third_Q_contact_probe']=third_q_candidates(Q,second,collar,lengths,gap,a,b,u)
                row.update(status='eligible geometry',Q_vertices=points(Q),
                           chain_period=[exact(c) for c in u],
                           collar_pentagons=[points(p) for p in collar],
                           collar_count_modulo_period=len(collar),
                           exhaustive_chain_comparisons=comparisons,
                           forced_chain_collisions=collisions)
            rows.append(row)
    assert len(rows)==12
    assert sum(r['status']=='eligible geometry' for r in rows)==4
    print(json.dumps({'scope':'12 exact closures, mandatory Q-chain collars, and eight third-Q side maps for each of two outgoing-private branches; one whole-plane witness is verified by all lattice overlaps and motif-area=covolume',
                      'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
