"""SUPERSEDED historical P5/Q9 hub gate; collision assertions below are false.

The overlap function uses u(90)=u(84) and orders elements of an unordered
cyclotomic field. For the corrected exact obstruction, run
research/reviews/p5q9-hub-hostile-check-2026-10-20.py instead.
"""
from itertools import product
from sage.all import CyclotomicField, AA

K = CyclotomicField(30)
z = K.gen()
u = lambda d: z ** (d // 12)
conj = lambda x: x.conjugate()
real = lambda x: (x + conj(x)) / 2
sgn = lambda x: (AA(x) > 0) - (AA(x) < 0)

A = u(144) + u(276)
B = u(72) + u(216)
D = A * conj(B) - conj(A) * B
b = (B - conj(B)) / D
c = (conj(A) - A) / D
assert b == conj(b) and c == conj(c)
assert sgn(b) == sgn(c) == 1
assert 1 + b*A + c*B == 0

P_lengths = (K(1), c, b, c, b)
P_dirs = (0,72,144,216,276)
Q_lengths = (K(1), b, c) * 3
Q_dirs = (0,36,96,120,156,216,240,276,336)

def polygon(lengths, dirs):
    out = [K(0)]
    for length, d in zip(lengths, dirs):
        out.append(out[-1] + length*u(d))
    assert out[-1] == 0
    vertices = tuple(out[:-1])
    for i in range(len(vertices)):
        e = vertices[(i+1)%len(vertices)] - vertices[i]
        f = vertices[(i+2)%len(vertices)] - vertices[(i+1)%len(vertices)]
        assert sgn(real(conj(e)*f* u(270))) == 1
    return vertices

P = polygon(P_lengths, P_dirs)
Q = polygon(Q_lengths, Q_dirs)

def put(poly, i, a, j, d, reflect=False):
    """Map source oriented edge i->i+1 to target vertices a->d."""
    start = poly[i]
    edge = poly[(i+1)%len(poly)]-start
    target = d-a
    assert target*conj(target) == edge*conj(edge)
    if reflect:
        lam = target/conj(edge)
        return tuple(a+lam*conj(x-start) for x in poly)
    lam = target/edge
    return tuple(a+lam*(x-start) for x in poly)

def overlap(X,Y):
    """Positive-area intersection for convex polygons, exact strict SAT."""
    for poly in (X,Y):
        for i in range(len(poly)):
            edge = poly[(i+1)%len(poly)] - poly[i]
            axis = edge*u(90)
            p = [real(conj(axis)*x) for x in X]
            q = [real(conj(axis)*x) for x in Y]
            if sgn(max(p)-min(q)) <= 0 or sgn(max(q)-min(p)) <= 0:
                return False
    return True

def attach_P_to_Q(j, bit):
    # Q edge j, P side 0. Opposite-interior placement has two endpoint orders.
    if bit == 0:
        return put(P,0,Q[(j+1)%9],j,Q[j])
    return put(P,0,Q[j],j,Q[(j+1)%9],reflect=True)

def cap_at(v, qray, pray, patch, full_edge=False):
    """Enumerate one-corner tiles filling exactly the residual endpoint wedge."""
    qlen = next(L for L in (K(1),b,c) if qray*conj(qray)==L*L)
    plen = next(L for L in (K(1),b,c) if pray*conj(pray)==L*L)
    target_q_unit = qray / qlen
    target_p_unit = pray / plen
    ans=[]
    for name,poly,lens in (("P",P,P_lengths),("Q",Q,Q_lengths)):
        for k in range(len(poly)):
            for side in ("next","prev"):
                src=poly[(k+1)%len(poly)]-poly[k] if side=="next" else poly[(k-1)%len(poly)]-poly[k]
                src_len=lens[k] if side=="next" else lens[(k-1)%len(poly)]
                other=poly[(k-1)%len(poly)]-poly[k] if side=="next" else poly[(k+1)%len(poly)]-poly[k]
                other_len=lens[(k-1)%len(poly)] if side=="next" else lens[k]
                if full_edge and (src_len != qlen or other_len != plen):
                    continue
                for refl in (False,True):
                    lam=target_q_unit/(conj(src)/src_len if refl else src/src_len)
                    mapped_other=lam*(conj(other) if refl else other)
                    if sgn(real(conj(target_p_unit)*mapped_other)) <= 0:
                        continue
                    if mapped_other*conj(target_p_unit) != conj(mapped_other)*target_p_unit:
                        continue
                    placed=tuple(v+lam*(conj(x-poly[k]) if refl else x-poly[k]) for x in poly)
                    if not any(overlap(placed,existing) for existing in patch):
                        if all(placed != item[4] for item in ans):
                            ans.append((name,k,side,refl,placed))
    return ans

print('field',K)
print('b,c',b,c,AA(b),AA(c))
print('P area / Q area',AA(real(sum(conj(P[i])*P[(i+1)%5]*u(270) for i in range(5))/2)), AA(real(sum(conj(Q[i])*Q[(i+1)%9]*u(270) for i in range(9))/2)))
print('P lengths',P_lengths,'Q lengths',Q_lengths)

for bits in product((0,1),repeat=3):
    Ps=[attach_P_to_Q(j,bit) for j,bit in zip((0,3,6),bits)]
    patch=(Q,*Ps)
    legal=not any(overlap(patch[i],patch[j]) for i in range(4) for j in range(i+1,4))
    caps=[]
    if legal:
        for t,j in enumerate((0,3,6)):
            pp=Ps[t]
            if bits[t]==0:
                endpoints=((j,1,(j-1)%9,2),((j+1)%9,0,(j+2)%9,4))
            else:
                endpoints=((j,0,(j-1)%9,4),((j+1)%9,1,(j+2)%9,2))
            for qv,pv,qother,pother in endpoints:
                v=Q[qv]
                assert pp[pv]==v
                qray=Q[qother]-v
                pray=pp[pother]-v
                opts=cap_at(v,qray,pray,patch,full_edge=True)
                caps.append((qv,pv,opts))
    print('hub',bits,'legal',legal,'full-edge caps',[(qv,pv,[(o[0],o[1],o[2],o[3]) for o in opts]) for qv,pv,opts in caps])
    assert legal
    assert [len(opts) for _,_,opts in caps] == sum(([2,2] if bit else [0,0] for bit in bits),[])
    if bits == (1,1,1) and legal:
        arm_words=[tuple(x-p[0] for x in p) for p in Ps]
        orbit_matches=[[[i for i,w in enumerate(arm_words) if tuple(x-o[4][0] for x in o[4])==w] for o in opts] for _,_,opts in caps]
        assert all(not match for row in orbit_matches for match in row)
        print('cap translation-orbit matches to three arms',orbit_matches)
        new_Q=[]
        for _,_,opts in caps:
            row=[]
            for o in opts:
                pp=o[4]
                qq=put(Q,0,pp[0],0,pp[1],reflect=not o[3])
                row.append((qq,not any(overlap(qq,e) for e in patch)))
            new_Q.append(row)
        print('cap P0 owner Q avoids four-tile hub',[[good for _,good in row] for row in new_Q])
        paths=[]
        def rec(k,images,choices):
            if k==6:
                paths.append((tuple(choices),len(images)))
                return
            for h,o in enumerate(caps[k][2]):
                image=o[4]
                if image in images:
                    rec(k+1,images,choices+[h])
                elif not any(overlap(image,e) for e in images):
                    rec(k+1,images+[image],choices+[h])
        rec(0,list(patch),[])
        assert len(paths)==64 and set(n for _,n in paths)=={10}
        print('prescribed six-cap assemblies',len(paths),'unique image counts',sorted(set(p[1] for p in paths)),'sample',paths[:8])
        surviving=[]
        for choice,_ in paths:
            Ps6=[caps[i][2][choice[i]][4] for i in range(6)]
            Qs6=[new_Q[i][choice[i]][0] for i in range(6)]
            allpoly=list(patch)+Ps6+Qs6
            if all(not overlap(allpoly[i],allpoly[j]) for i in range(len(allpoly)) for j in range(i+1,len(allpoly))):
                surviving.append(choice)
        print('six caps plus their six compulsory Q owners',len(surviving),'sample',surviving[:8])
        assert len(surviving)==64
