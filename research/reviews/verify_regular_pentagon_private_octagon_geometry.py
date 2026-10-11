#!/usr/bin/env python3
"""Independent exact audit; never imports the geometry producer.

Overlap decisions use separating axes, rather than polygon clipping.
Intersections used for retained areas are reconstructed from support-line
intersections and a monotone convex hull. Run in the arisearch environment.
"""
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path

from sage.all import AA, QQ, QQbar, PolynomialRing, ceil, floor

if not __debug__:
    raise RuntimeError("Assertions are required")

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'research/certificates/regular-pentagon-private-octagon-geometry.json'
R = PolynomialRing(QQ, 'x')
Z = QQbar.zeta(10)
assert Z**4-Z**3+Z**2-Z+1 == 0 and Z.real()>0 and Z.imag()>0
PHI=(AA(1)+AA(5).sqrt())/2
SINE=AA(Z.imag())


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(c,a): return (c*a[0],c*a[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def direction(k): return (AA((Z**k).real()),AA((Z**k).imag()))
def complex_point(p): return QQbar(p[0])+QQbar.gen()*QQbar(p[1])
def real_point(z): return (AA(z.real()),AA(z.imag()))
def transform(poly,L,t):
    return [add((L[0][0]*p[0]+L[0][1]*p[1],
                 L[1][0]*p[0]+L[1][1]*p[1]),t) for p in poly]
def translate(poly,t): return [add(p,t) for p in poly]
def edges(poly): return [(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))]
def area(poly): return sum(cross(a,b) for a,b in edges(poly))/2 if len(poly)>2 else AA(0)
def ccw(poly): return poly if area(poly)>0 else list(reversed(poly))


@lru_cache(None)
def decode_algebraic(coeffs,lo,hi):
    f=R([QQ(c) for c in coeffs]); low,high=QQ(lo),QQ(hi)
    assert low<high and f.is_irreducible() and f.is_monic()
    roots=[r for r,m in f.roots(AA) if low<r<high and m==1]
    assert len(roots)==1
    assert roots[0].minpoly()==f
    return roots[0]


def number(d):
    if 'rational' in d:
        assert set(d)=={'rational'}
        return AA(QQ(d['rational']))
    assert set(d)=={'polynomial_coefficients','isolating_interval'}
    return decode_algebraic(tuple(d['polynomial_coefficients']),*d['isolating_interval'])


def point(p): return tuple(number(x) for x in p)
def polygon(p): return [point(x) for x in p]


def strict_convex(poly):
    assert area(poly)>0
    for i,(a,b) in enumerate(edges(poly)):
        assert all(cross(sub(b,a),sub(p,a))>0
                   for j,p in enumerate(poly) if j not in (i,(i+1)%len(poly)))


def interior_overlap(a,b):
    """Strict SAT: equality permits boundary contact, with no positive area."""
    for x,y in edges(a)+edges(b):
        e=sub(y,x); n=(-e[1],e[0])
        pa=[dot(n,p) for p in a]; pb=[dot(n,p) for p in b]
        if max(min(pa),min(pb))>=min(max(pa),max(pb)):
            return False
    return True


def hull(points):
    points=sorted(set(points))
    if len(points)<3: return points
    def half(ps):
        out=[]
        for p in ps:
            while len(out)>1 and cross(sub(out[-1],out[-2]),sub(p,out[-1]))<=0:
                out.pop()
            out.append(p)
        return out
    return half(points)[:-1]+half(list(reversed(points)))[:-1]


def constraints(poly):
    # n.p >= h for each interior left support half-plane.
    out=[]
    for a,b in edges(ccw(poly)):
        e=sub(b,a); n=(-e[1],e[0]); out.append((n,dot(n,a)))
    return out


def support_intersection(cs):
    points=[]
    for (n,h),(m,k) in combinations(cs,2):
        det=cross(n,m)
        if not det: continue
        p=((h*m[1]-n[1]*k)/det,(n[0]*k-h*m[0])/det)
        if all(dot(v,p)>=w for v,w in cs): points.append(p)
    return hull(points)


def same_edge(a,b): return set(a)==set(b)


def regular_across(poly,j):
    a,b=edges(poly)[j]; e=complex_point(sub(a,b)); p=complex_point(b)
    out=[]
    for k in range(5):
        out.append(real_point(p)); p+=e*Z**(2*k)
    assert p==complex_point(b)
    strict_convex(out)
    return out


def same_mod_period(a,b,u):
    if len(a)!=len(b): return False
    ca=mul(QQ(1)/len(a),tuple(map(sum,zip(*a))))
    cb=mul(QQ(1)/len(b),tuple(map(sum,zip(*b))))
    delta=sub(cb,ca)
    if cross(u,delta): return False
    t=dot(u,delta)/dot(u,u)
    return t in QQ and QQ(t).denominator()==1 and set(translate(a,delta))==set(b)


def unique_mod_period(polys,u):
    out=[]
    for p in polys:
        p=ccw(p)
        if not any(same_mod_period(p,q,u) for q in out): out.append(p)
    return out


def shifts_1d(a,b,u):
    # Necessary projection bounds, covering every integer possible overlap.
    aa=[dot(u,p)/dot(u,u) for p in a]
    bb=[dot(u,p)/dot(u,u) for p in b]
    return range(int(ceil(min(aa)-max(bb))),int(floor(max(aa)-min(bb)))+1)


def check_chain(polys,u):
    count=0; collisions=[]
    for i,a in enumerate(polys):
        for j,b in enumerate(polys):
            for n in shifts_1d(a,b,u):
                if i==j and n==0: continue
                count+=1
                if interior_overlap(a,translate(b,mul(n,u))): collisions.append((i,j,n))
    return count,collisions


def endpoint_maps(Q,j,P,k):
    """All four endpoint/parity maps; keep the two opposite-side maps."""
    qa,qb=edges(Q)[j]; pa,pb=edges(P)[k]
    eq,ep=complex_point(sub(qb,qa)),complex_point(sub(pb,pa))
    out=[]
    for reflected,reverse in product((False,True),repeat=2):
        target=pa if not reverse else pb
        target_end=pb if not reverse else pa
        r=complex_point(sub(target_end,target))/(eq.conjugate() if reflected else eq)
        x,y=AA(r.real()),AA(r.imag())
        L=((x,y),(y,-x)) if reflected else ((x,-y),(y,x))
        t=sub(target,transform([qa],L,(AA(0),AA(0)))[0])
        mapped=transform(Q,L,t)
        vals=[cross(sub(pb,pa),sub(p,pa)) for p in mapped]
        # P is left of its CCW edge: neighboring Q must be right.
        if max(vals)==0 and min(vals)<0:
            assert all(dot(row,row)==1 for row in L)
            assert dot(L[0],L[1])==0
            out.append((-1 if reflected else 1,L,t))
    assert len(out)==2 and {s[0] for s in out}=={-1,1}
    return out


def plane_check(motif,u,w):
    det=cross(u,w); assert det!=0
    def coords(poly):
        return [(cross(p,w)/det,cross(u,p)/det) for p in poly]
    count=0
    for i,a in enumerate(motif):
        ac=coords(a)
        for j,b in enumerate(motif):
            bc=coords(b)
            ranges=[range(int(ceil(min(p[k] for p in ac)-max(p[k] for p in bc))),
                          int(floor(max(p[k] for p in ac)-min(p[k] for p in bc)))+1)
                    for k in (0,1)]
            for m,n in product(*ranges):
                if i==j and m==n==0: continue
                count+=1
                assert not interior_overlap(a,translate(b,add(mul(m,u),mul(n,w))))
    assert sum(area(p) for p in motif)==abs(det)
    return count


def audit():
    data=json.loads(CERT.read_text()); rows=data['rows']
    assert len(rows)==12
    domain={(d,i,j) for d in (2,3,4) for i in (7,0) for j in (d-1,d)}
    assert {(r['alpha_gap'],*r['private_sides']) for r in rows}==domain
    q=(AA(5)-AA(5).sqrt())/2
    closed_table={(2,7,1):(q,AA(5).sqrt()),(2,0,1):(PHI,PHI),
                  (2,0,2):(AA(5).sqrt(),q),(3,7,2):(PHI,AA(2)),
                  (3,7,3):(AA(0),AA(0)),(3,0,2):(q,q),
                  (3,0,3):(AA(2),PHI),(4,7,4):(AA(1),AA(1)),
                  (4,0,3):(AA(1),AA(1))}
    eligible={}; probes=0; full_plane=0
    for record in rows:
        d=record['alpha_gap']; ix,iy=record['private_sides']
        dirs=[direction(j+(j>=d)) for j in range(8)]
        total=tuple(map(sum,zip(*dirs))); det=cross(dirs[ix],dirs[iy])
        if not det:
            assert dirs[ix]==mul(-1,dirs[iy])
            status=('parallel closure forces equal private lengths' if total==(0,0)
                    else 'parallel closure inconsistent')
            if total!=(0,0): assert cross(total,dirs[ix])!=0
            assert record['status']==status
            continue
        x=1-cross(total,dirs[iy])/det
        y=1-cross(dirs[ix],total)/det
        assert (x,y)==closed_table[(d,ix,iy)]
        assert [number(p) for p in record['private_lengths']]==[x,y]
        status=('nonpositive side' if min(x,y)<=0 else 'private side unit' if 1 in (x,y)
                else 'private lengths equal' if x==y else 'eligible geometry')
        assert record['status']==status
        if status!='eligible geometry': continue
        lengths=[AA(1)]*8; lengths[ix],lengths[iy]=x,y
        Q=[(AA(0),AA(0))]
        for j in range(8): Q.append(add(Q[-1],mul(lengths[j],dirs[j])))
        assert Q.pop()==(0,0)
        strict_convex(Q); assert Q==polygon(record['Q_vertices'])
        a=mul(QQ(1)/2,add(*edges(Q)[ix])); b=mul(QQ(1)/2,add(*edges(Q)[iy]))
        u=mul(2,sub(b,a)); assert u!= (0,0) and point(record['chain_period'])==u
        second=[sub(mul(2,b),p) for p in Q]
        collar=unique_mod_period([regular_across(q,j) for q in (Q,second)
                                 for j in range(8) if lengths[j]==1],u)
        assert len(collar)==record['collar_count_modulo_period']==8
        assert collar==[polygon(p) for p in record['collar_pentagons']]
        base=[Q,second]+collar
        comparisons,collisions=check_chain(base,u)
        assert comparisons==record['exhaustive_chain_comparisons']
        assert not collisions and record['forced_chain_collisions']==[]
        eligible[(d,ix,iy)]=(Q,lengths)
        if 'third_Q_contact_probe' not in record: continue
        probes+=1; probe=record['third_Q_contact_probe']
        j=probe['P_Q_side']; P=regular_across(Q,j)
        known=[k for k in range(5) if any(same_edge(edges(P)[k],e) for e in edges(second))]
        assert known==[4] and probe['P_known_second_Q_side']==4
        assert j==d-1 and probe['P_third_Q_side']==2
        # Side 2 is the only slot nonadjacent to already required Q slots 0,4.
        remaining=[k for k in range(5) if k not in (0,4)
                   and (k-1)%5 not in (0,4) and (k+1)%5 not in (0,4)]
        assert remaining==[2]
        beta=[k for k in range(8) if lengths[k]==1 and k not in (0,d)
              and (k+1)%8 not in (0,d)]
        assert len(beta)==4
        candidates={(k,parity):(L,t) for k in beta
                    for parity,L,t in endpoint_maps(Q,k,P,2)}
        assert len(candidates)==8
        assert {(s['Q_side'],s['orientation_parity']) for s in probe['rows']}==set(candidates)
        for s in probe['rows']:
            L,t=candidates[(s['Q_side'],s['orientation_parity'])]
            newaxis=transform([a],L,t)[0]
            direction_new=transform([sub(b,a)],L,(AA(0),AA(0)))[0]
            if cross(direction_new,sub(b,a)):
                assert s['status']=='axis not parallel'
                continue
            assert [[number(x) for x in row] for row in s['linear_matrix']]==list(map(list,L))
            assert point(s['translation'])==t
            sep=cross(u,sub(newaxis,a)); assert sep!=0
            joint=unique_mod_period(base+[transform(p,L,t) for p in base],u)
            comparisons,collisions=check_chain(joint,u)
            assert comparisons==s['joint_comparisons']
            assert len(collisions)==s['joint_collision_count']
            if collisions:
                assert s['status']=='forced collar overlap'
                first=s['first_collision']; ijm=(first['first'],first['second'],first['shift'])
                assert ijm==collisions[0]
                i,j,m=ijm; common=support_intersection(constraints(joint[i])+
                       constraints(translate(joint[j],mul(m,u))))
                assert area(common)==number(first['overlap_area'])>0
                assert area(common)==AA(Z.imag())
                assert set(common)==set(hull(polygon(first['intersection'])))
                if d==2: assert i==1 and j>=len(base) and len(joint[j])==8
                continue
            assert d==3 and s['status']=='complete periodic band'
            sign=1 if sep>0 else -1
            n=mul(sign,(-u[1],u[0]))
            band=[(n,dot(n,a)),(mul(-1,n),-dot(n,newaxis))]
            pieces=[support_intersection(constraints(p)+band) for p in joint]
            retained=[(p,piece) for p,piece in zip(joint,pieces) if area(piece)>0]
            assert len(retained)==s['band_tile_count']==8
            assert [p for p,piece in retained]==[polygon(p) for p in s['band_tiles']]
            assert all(set(piece)==set(hull(polygon(other)))
                       for (p,piece),other in zip(retained,s['band_pieces']))
            assert sum(area(piece) for p,piece in retained)==abs(sep)
            assert number(s['band_area'])==number(s['band_covolume'])==abs(sep)
            if 'whole_plane_witness' in s:
                full_plane+=1; w=s['whole_plane_witness']
                assert L==((1,0),(0,1))
                motif=[Q,second]+[p for p,piece in retained if len(p)==5]
                assert len(motif)==6 and [len(p) for p in motif]==[8,8,5,5,5,5]
                source_motif=[Q,second,regular_across(Q,1),regular_across(Q,2),
                              regular_across(second,5),regular_across(second,6)]
                assert motif==source_motif
                assert u==((1+3*PHI)/2,SINE*(2+3*PHI))
                assert t==(PHI+2,-2*PHI*SINE)
                assert area(Q)==SINE*(9*PHI+8)/2
                assert all(area(p)==SINE*(3*PHI+1)/2 for p in motif[2:])
                assert abs(cross(u,t))==5*SINE*(3*PHI+2)
                assert motif==[polygon(p) for p in w['motif']]
                assert [point(v) for v in w['lattice']]==[u,t]
                assert plane_check(motif,u,t)==w['complete_lattice_overlap_comparisons']==36
                assert number(w['area_sum'])==number(w['lattice_covolume'])==abs(cross(u,t))
    assert set(eligible)=={(2,7,1),(2,0,2),(3,7,2),(3,0,3)}
    assert probes==2 and full_plane==1
    for d in (2,3):
        outgoing,ol=eligible[(d,0,d)]; incoming,il=eligible[(d,7,d-1)]
        assert ol[0]==il[d-1] and ol[d]==il[7]
        # Reflection relabeling k -> d-k; direct isometry of all 8 vertices.
        origin=incoming[d]; src=complex_point(sub(outgoing[1],outgoing[0]))
        target=complex_point(sub(incoming[(d-1)%8],origin))
        r=target/src.conjugate(); assert r*r.conjugate()==1
        for k in range(8):
            image=add(real_point(r*complex_point(outgoing[k]).conjugate()),origin)
            assert image==incoming[(d-k)%8]
    print('VALID: 12 exact closures; 4 eligible mirror cases; two complete 8-map probes;')
    print('gap-2 forced Q overlaps; gap-3 6-tile plane witness with 36 lattice checks and exact area.')


if __name__=='__main__': audit()
