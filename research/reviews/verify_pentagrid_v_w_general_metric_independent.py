#!/usr/bin/env python3
"""Fresh V/W audit: native walks, derived seams/links, complete fixture SAT.
No author producer or certificate imported. No finite search supports the
all-metric theorem: polynomial identities and positive closure do that.
"""
from itertools import combinations, product
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, matrix, vector

K=CyclotomicField(10);z=K.gen();phi=z+1/z
R=PolynomialRing(K,('x','y','f'));x,y,f=R.gens()
def walk(lengths,directions):
    vertices=[R(0)]
    for length,direction in zip(lengths,directions):
        vertices.append(vertices[-1]+length*z**direction)
    assert vertices.pop()==0
    return vertices
def conjugate(p):
    return R({tuple(exponents):coefficient.conjugate()
              for exponents,coefficient in R(p).dict().items()})
def cross(a,b):
    return (conjugate(a)*b-a*conjugate(b))/(z-z.conjugate())

def main():
    r=phi*(x+f)-y;e=f+phi*(x-y)
    H=y+phi*(f-x);E=f+phi*(y-x)
    assert E+e==2*f
    assert r==x/phi+f+(x+f/phi-y)
    V=walk([x,r,y,e,f],[4,7,0,1,3]);V=[p-V[2] for p in V]
    W=walk([y,H,x,E,f],[0,2,4,6,8])
    motifs=[V,[r*z**2-p for p in V],[y-p for p in W],
            [r*z**2-y+p for p in W]]
    u=motifs[0][3]-motifs[1][4]
    v=motifs[0][0]-motifs[2][3]
    assert u==2*y+e*z-r*z**2 and v==2*phi*f*z**2
    assert cross(u,v)==2*phi*f*(phi*(x+y)+f)
    assert cross(u,v)==sum(sum(cross(p[i],p[(i+1)%5])
                              for i in range(5))/2 for p in motifs)
    # Derive every reversed side and lattice displacement from native walks.
    slots=list(product(range(4),range(5)));twin={}
    for i,a in slots:
        matches=[]
        for j,b in slots:
            if (i,a)==(j,b):continue
            if motifs[i][(a+1)%5]-motifs[i][a]!=motifs[j][b]-motifs[j][(b+1)%5]:continue
            for n,t in product(range(-1,2),repeat=2):
                if motifs[i][a]==motifs[j][(b+1)%5]+n*u+t*v:
                    matches.append((j,b,n,t))
        assert len(matches)==1,((i,a),matches)
        twin[i,a]=matches[0]
    for (i,a),(j,b,n,t) in twin.items():
        assert twin[j,b]==(i,a,-n,-t)
    unseen=set(slots);links=[];angles=[4,2,2,4,3]
    while unseen:
        start=min(unseen);cur=start;cycle=[];shift=[0,0]
        while cur not in cycle:
            cycle.append(cur);j,b,n,t=twin[cur]
            shift[0]+=n;shift[1]+=t;cur=(j,(b+1)%5)
        assert cur==start and shift==[0,0]
        assert sum(angles[a] if i<2 else 3 for i,a in cycle)==10
        unseen.difference_update(cycle);links.append(cycle)
    assert sorted(map(len,links))==[3,3,3,3,4,4]
    adjacent={i:{j for (ii,a),(j,b,n,t) in twin.items() if ii==i} for i in range(4)}
    reached={0}
    while reached!=set(range(4)):
        expanded=reached|{j for i in reached for j in adjacent[i]}
        assert expanded!=reached;reached=expanded
    # Verify the full cone by all rank-two active pairs, exact algebraic signs.
    normal=matrix(K,[[1,0,0],[0,1,0],[0,0,1],[-phi,1,phi],
                     [-phi,phi,1],[phi,-1,phi],[phi,-phi,1]])
    real=lambda a:AA(QQbar(a).real())
    N=matrix(AA,[[real(a) for a in row] for row in normal.rows()]);rays=[]
    for a,b in combinations(range(7),2):
        active=matrix(AA,[N[a],N[b]])
        if active.rank()!=2:continue
        q=active.right_kernel().basis()[0];q=q/next(c for c in q if c)
        if all(row.dot_product(q)>=0 for row in N.rows()) and q not in rays:rays.append(q)
    p=real(phi);s=AA(5).sqrt()
    expected=[vector(AA,q) for q in [(0,0,1),(0,1,p),(1,0,p),(1,1/p,1/p),(1,p*p/s,1/(p*s))]]
    assert len(rays)==5 and all(q in rays for q in expected)
    for j in [0,1,3,4,6]:
        on=[q for q in rays if N[j].dot_product(q)==0]
        assert matrix(AA,on).rank()==2
        witness=sum(on,vector(AA,[0,0,0]))
        assert all(N[k].dot_product(witness)>0 for k in [0,1,3,4,6] if k!=j)
    # Exact complete overlap domain for the asymmetric fixture, independent SAT.
    substitutions={x:QQ(2),y:QQ(1),f:QQ(3)}
    ev=lambda p:QQbar(R(p).subs(substitutions))
    polygons=[list(map(ev,p)) for p in motifs];pu,pv=ev(u),ev(v)
    cr=lambda a,b:AA((a.conjugate()*b).imag())
    determinant=cr(pu,pv);assert determinant>0
    separated=lambda P,Q:any(all(cr(P[(i+1)%5]-P[i],q-P[i])<=0 for q in Q) for i in range(5))
    boxes=[]
    for P in polygons:
        for i in range(5):
            assert all(cr(P[(i+1)%5]-P[i],P[j]-P[i])>0 for j in range(5) if j not in (i,(i+1)%5))
        coordinates=[(cr(q,pv)/determinant,cr(pu,q)/determinant) for q in P]
        boxes.append([(min(q[d] for q in coordinates),max(q[d] for q in coordinates)) for d in (0,1)])
    count=0
    for i,j in product(range(4),repeat=2):
        domains=[range(int((boxes[i][d][0]-boxes[j][d][1]).ceil()),int((boxes[i][d][1]-boxes[j][d][0]).floor())+1) for d in (0,1)]
        for n,t in product(*domains):
            if i==j and n==t==0:continue
            Q=[q+n*pu+t*pv for q in polygons[j]]
            assert separated(polygons[i],Q) or separated(Q,polygons[i]),(i,j,n,t)
            count+=1
    assert count==32
    print('PASS independent V/W native walks, 20 derived side twins, 6 closed links, full 3D cone, formal covolume and 32 complete exact fixture separations')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
