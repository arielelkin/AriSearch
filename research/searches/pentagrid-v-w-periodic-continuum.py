"""Exact V/W four-face periodic family and complete sqrt2 fixture checks."""
from sage.all import AA, QQ, QQbar, CyclotomicField, RIF, ceil, floor
from itertools import product
from pathlib import Path
import json

K=CyclotomicField(10);z=K.gen();phi=z+1/z
PAIRS=((0,1,1,1),(0,2,2,0),(0,3,1,3),(0,4,3,4),(0,0,2,2),
       (1,2,3,0),(1,4,2,4),(1,0,3,2),(2,1,3,1),(2,3,3,3))
SHIFTS=((0,0),(0,0),(1,0),(1,0),(0,1),(0,0),(-1,0),(0,-1),(0,-1),(1,-1))
ANGLES=((4,2,2,4,3),(4,2,2,4,3),(3,3,3,3,3),(3,3,3,3,3))

def geometry(b,c,root=z,golden=phi):
    E=golden*(b+c);D=2*golden*b+golden**2*c;H=2*b+golden**2*c
    q=[0]
    for l,k in [(b,0),(E,1),(E,3),(b,4),(b,5),(E,6),(E,8),(b,9)]:
        q.append(q[-1]+l*root**k)
    assert q[-1]==0
    q=q[:-1]
    assert q[4]==D*root**2
    w=[0]
    for l,k in [(b,0),(H,2),(b,4),(E,6),(E,8)]:w.append(w[-1]+l*root**k)
    assert w[-1]==0
    w=w[:-1]
    V=[q[3],q[4],q[0],q[1],q[2]]
    motifs=[V,[q[4]-p for p in V],[b-p for p in w],[q[5]+p for p in w]]
    u=2*b+E*root-D*root**2
    v=2*golden*E*root**2
    return motifs,u,v,q,w

def ncross(a,b):return (a.conjugate()*b-a*b.conjugate())/(z-z.conjugate())
def narea(p):return sum(ncross(p[j],p[(j+1)%len(p)]) for j in range(len(p)))/2

def coeff(p):
    v=[str(QQ(x)) for x in K(p).list()]
    return v+['0']*(4-len(v))

def symbolic():
    probes=[geometry(K(1),K(0)),geometry(K(0),K(1))]
    for motifs,u,v,q,w in probes:
        for (i,a,j,d),(n,m) in zip(PAIRS,SHIFTS):
            assert motifs[i][a]==motifs[j][(d+1)%5]+n*u+m*v
            assert motifs[i][(a+1)%5]==motifs[j][d]+n*u+m*v
    # Retain the full quadratic coefficients, not sampled positivity claims.
    area_values=[]
    for b,c in [(K(1),K(0)),(K(0),K(1)),(K(1),K(1))]:
        motifs,u,v,q,w=geometry(b,c)
        E=phi*(b+c)
        assert ncross(u,v)==2*phi*E*(2*phi*b+E)
        assert sum(narea(p) for p in motifs)==ncross(u,v)
        assert 2*narea(motifs[0])==narea(q)
        assert narea(motifs[0])==(3*phi+2)*b*b+(4*phi+2)*b*c+(phi+K(1)/2)*c*c
        assert narea(motifs[2])==(3*phi+1)*b*b+(4*phi+2)*b*c+(phi+K(1)/2)*c*c
        area_values.append([narea(motifs[0]),narea(motifs[2])])
    area_coeff=[]
    for i in range(2):
        a,b=area_values[0][i],area_values[1][i]
        mix=area_values[2][i]-a-b
        area_coeff.append([str(a),str(mix),str(b)])
    involution={}
    for i,a,j,d in PAIRS:
        assert (i,a) not in involution and (j,d) not in involution
        involution[(i,a)]=(j,d);involution[(j,d)]=(i,a)
    assert len(involution)==20
    perm={x:(y[0],(y[1]+1)%5) for x,y in involution.items()}
    rem=set(perm);links=[]
    while rem:
        start=min(rem);cur=start;cyc=[]
        while cur not in cyc:
            cyc.append(cur);rem.remove(cur);cur=perm[cur]
        assert cur==start
        assert sum(ANGLES[f][j] for f,j in cyc)==10
        links.append(cyc)
    assert len(links)==6
    multisets=[sorted(ANGLES[f][j] for f,j in link) for link in links]
    assert multisets.count([2,2,3,3])==2 and multisets.count([3,3,4])==4
    reach={0}
    for _ in range(4):
        for i,a,j,d in PAIRS:
            if i in reach:reach.add(j)
            if j in reach:reach.add(i)
    assert len(reach)==4
    return {'parameter_domain':'b>0,c>0','V_lengths':'(b,2*phi*b+phi^2*c,b,phi*(b+c),phi*(b+c))',
            'W_lengths':'(b,2*b+phi^2*c,b,phi*(b+c),phi*(b+c))',
            'formal_motif_coefficients_b_c':[[[coeff(probes[0][0][i][j]),coeff(probes[1][0][i][j])] for j in range(5)] for i in range(4)],
            'formal_lattice_coefficients_b_c':[[coeff(probes[0][i]),coeff(probes[1][i])] for i in (1,2)],
            'side_pairs':PAIRS,'seam_integer_shifts':SHIFTS,'ordered_corner_links':links,
            'vertex_angles_in_pi_over_5':ANGLES,'quadratic_normalized_area_coefficients_b2_bc_c2_V_W':area_coeff,
            'normalized_lattice_determinant':'2*phi*E*(2*phi*b+E), E=phi*(b+c)'}

def enc(x):
    x=AA(x)
    if x in QQ:return {'rational':str(QQ(x))}
    p=x.minpoly();iv=x.interval(RIF);lo=iv.lower().exact_rational();hi=iv.upper().exact_rational()
    assert sum(lo<r<hi for r in p.roots(AA,multiplicities=False))==1
    return {'polynomial_coefficients':[str(QQ(t)) for t in p.list()], 'isolating_interval':[str(lo),str(hi)]}

def fixture():
    root=QQbar.zeta(10);golden=(root+1/root).real();c=AA(2).sqrt()
    motifs,u,v,q,w=geometry(QQbar(1),QQbar(c),root,QQbar(golden))
    def pt(p):return (AA(QQbar(p).real()),AA(QQbar(p).imag()))
    polys=[[pt(p) for p in poly] for poly in motifs];u,v=pt(u),pt(v)
    def sub(p,q):return p[0]-q[0],p[1]-q[1]
    def cross(p,q):return p[0]*q[1]-p[1]*q[0]
    def area(p):return sum(cross(a,b) for a,b in zip(p,p[1:]+p[:1]))/2
    for p in polys:
        assert area(p)>0
        assert all(cross(sub(p[(i+1)%5],p[i]),sub(p[j],p[i]))>0 for i in range(5) for j in range(5) if j not in [i,(i+1)%5])
    det=cross(u,v);assert det>0
    lattice=[[ (cross(p,v)/det,cross(u,p)/det) for p in poly] for poly in polys]
    def separated(a,b):
        for p in (a,b):
            for x,y in zip(p,p[1:]+p[:1]):
                e=sub(y,x)
                pa=[cross(e,q) for q in a];pb=[cross(e,q) for q in b]
                if max(pa)<=min(pb) or max(pb)<=min(pa):return True
        return False
    checks=[]
    for i,j in product(range(4),repeat=2):
        bounds=[range(int(ceil(min(p[k] for p in lattice[i])-max(p[k] for p in lattice[j]))),int(floor(max(p[k] for p in lattice[i])-min(p[k] for p in lattice[j])))+1) for k in (0,1)]
        for n,m in product(*bounds):
            if i==j and n==m==0:continue
            shift=[(p[0]+n*u[0]+m*v[0],p[1]+n*u[1]+m*v[1]) for p in polys[j]]
            assert separated(polys[i],shift),(i,j,n,m)
            checks.append([i,j,n,m])
    assert sum(area(p) for p in polys)==det
    return {'b':enc(1),'c':enc(c),'motifs':[[[enc(x) for x in p] for p in poly] for poly in polys],
            'lattice':[[enc(x) for x in p] for p in (u,v)],'areas':[enc(area(p)) for p in polys],
            'determinant':enc(det),'complete_overlap_comparisons':checks,'comparison_count':len(checks)}

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions must be enabled.')
    out={'status':'adversarially reviewed VALID; research/reviews/pentagrid-v-w-periodic-continuum-review.md','field':'Q(z), z^4-z^3+z^2-z+1=0, z=exp(pi*i/5)',
         'symbolic_family':symbolic(),'irrational_fixture':fixture()}
    # Preserve the original generation-status metadata in the retained JSON;
    # the current theorem and its fresh review are linked in the lemma.
    print(json.dumps(out,indent=2))
