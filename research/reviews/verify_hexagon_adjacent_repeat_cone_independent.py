#!/usr/bin/env python3
"""Fresh complex-coordinate audit of the branching repeated-side hexagons.
No author imports. Reconstruct walks, derive side twins, close link holonomy,
check the full branch cone, and exhaust the exact fixture overlap domain.
"""
import ast
import json
from pathlib import Path
from itertools import product, combinations_with_replacement
from sage.all import AA, QQ, QQbar, CyclotomicField, PolynomialRing, matrix

K=CyclotomicField(6);w=K.gen();R=PolynomialRing(K,('p','q','a','c'));p,q,a,c=R.gens()
def cj(t):return R({tuple(e):v.conjugate() for e,v in R(t).dict().items()})
def cross(x,y):return (cj(x)*y-x*cj(y))/(w-w.conjugate())
def walk(lengths):
    out=[R(0)]
    for i,length in enumerate(lengths):out.append(out[-1]+length*w**i)
    assert out.pop()==0
    return out
def parse(text):
    # The certificate gives real x and sqrt(3)*rational y. Interpret h as
    # i*sqrt(3)=2w-1 in y coordinates, then combine x+y into one complex point.
    env={'p':p,'q':q,'a':a,'c':c,'h':R(2*w-1)}
    def rec(node):
        if isinstance(node,ast.Constant):return R(QQ(node.value))
        if isinstance(node,ast.Name):return env[node.id]
        if isinstance(node,ast.UnaryOp):
            v=rec(node.operand)
            if isinstance(node.op,ast.USub):return -v
            if isinstance(node.op,ast.UAdd):return v
        if isinstance(node,ast.BinOp):
            x,y=rec(node.left),rec(node.right)
            if isinstance(node.op,ast.Add):return x+y
            if isinstance(node.op,ast.Sub):return x-y
            if isinstance(node.op,ast.Mult):return x*y
            if isinstance(node.op,ast.Div):return x/y
            if isinstance(node.op,ast.Pow):return x**int(y)
        raise ValueError('Unexpected certificate expression')
    return R(rec(ast.parse(text.replace('^','**'),mode='eval').body))
def point(row):
    x,y=map(parse,row);assert cj(x)==x and cj(y)==-y
    return x+y

def main():
    root=Path(__file__).resolve().parents[2]
    certificate=json.loads((root/'research/certificates/hexagon-adjacent-repeat-periodic-cone.json').read_text())
    # Solve both closures in the rational basis (1,w), independent of sqrt(3) coordinates.
    coordinates=lambda z:list(K(z).list())+[QQ(0)]*(2-len(K(z).list()))
    units=[coordinates(w**j) for j in range(6)]
    M=matrix(QQ,[[units[3][t],units[5][t],0,0] for t in range(2)]+
                [[units[3][t],units[5][t],units[0][t],units[2][t]] for t in range(2)])
    N=matrix(QQ,[[units[0][t],units[2][t],units[1][t],units[4][t]] for t in range(2)]+
                [[0,0,units[4][t],units[1][t]] for t in range(2)])
    assert M.rank()==4
    solution=-M.inverse()*N
    assert solution==matrix(QQ,[[1,0,1,-1],[0,1,1,-1],[1,0,2,-2],[0,1,2,-2]])
    assert solution==matrix(QQ,certificate['dependent_closure_matrix'])
    b=p+a-c;d=q+a-c;r=p+2*(a-c);s=q+2*(a-c)
    lengths=[[p,a,q,b,c,d],[r,c,s,b,a,d]]
    assert lengths==[[parse(t) for t in row] for row in certificate['native_side_words']]
    A,B=map(walk,lengths)
    faces=[A,[p-z for z in A],[p+d*w**5+z for z in B],[-d*w**5-z for z in B]]
    assert faces==[[point(row) for row in face] for face in certificate['motif_vertices']]
    assert list(map(point,certificate['units']))==[w**j for j in range(6)]
    u=2*p+q+3*a-3*c+d*(1-2*w);v=p-q+(q+2*a)*w
    assert [u,v]==list(map(point,certificate['periods']))
    F=2*p*q+3*p*a+3*q*a+4*a*a-p*c-q*c-4*a*c
    area=lambda P:sum(cross(P[j],P[(j+1)%6]) for j in range(6))/2
    assert cross(u,v)==2*F==sum(map(area,faces))
    assert parse(certificate['area_covolume'])==(w-w.conjugate())*cross(u,v)/2
    # Strict convexity throughout the full positive cone, with no genericity assumption.
    for P,ls in zip((A,B),lengths):
        for j in range(6):
            edge=P[(j+1)%6]-P[j]
            heights=[cross(edge,P[(j+k)%6]-P[j]) for k in (2,3,4,5)]
            assert heights==[ls[j]*ls[(j+1)%6],ls[j]*(ls[(j+1)%6]+ls[(j+2)%6]),
                             ls[j]*(ls[(j+1)%6]+ls[(j+2)%6]),ls[j]*ls[(j-1)%6]]
    # Derive 24 side twins by formal reversed edges and actual lattice displacements.
    slots=list(product(range(4),range(6)));twin={}
    for i,e in slots:
        matches=[]
        for j,f in slots:
            if (i,e)==(j,f):continue
            if faces[i][(e+1)%6]-faces[i][e]!=faces[j][f]-faces[j][(f+1)%6]:continue
            for n,t in product(range(-1,2),repeat=2):
                if faces[i][e]==faces[j][(f+1)%6]+n*u+t*v:matches.append((j,f,n,t))
        assert len(matches)==1,((i,e),matches)
        twin[i,e]=matches[0]
    for (i,e),(j,f,n,t) in twin.items():assert twin[j,f]==(i,e,-n,-t)
    assert len(certificate['seams'])==12
    for seam in certificate['seams']:
        assert twin[tuple(seam['first'])]==tuple(seam['second']+seam['shift'])
    unseen=set(slots);links=[]
    while unseen:
        start=min(unseen);cur=start;cycle=[];shift=[0,0]
        while cur not in cycle:
            cycle.append(cur);j,f,n,t=twin[cur];shift[0]+=n;shift[1]+=t;cur=(j,(f+1)%6)
        assert cur==start and len(cycle)==3 and shift==[0,0]
        assert len({i for i,e in cycle})==3
        unseen.difference_update(cycle);links.append(cycle)
    assert len(links)==8 and links==[[tuple(corner) for corner in link] for link in certificate['circular_corner_links']]
    zero_graph={i:{j for (ii,e),(j,f,n,t) in twin.items() if ii==i and n==t==0} for i in range(4)}
    reached={0}
    while reached!=set(range(4)):
        more=reached|{j for i in reached for j in zero_graph[i]};assert more!=reached;reached=more
    # Complete local star domain; preserve actual label collisions only at excluded c=a.
    wordA=('a','a','c','b','c','a');wordB=('r','c','b','b','a','a')
    pair=lambda x,y:tuple(sorted((x,y)))
    graph=lambda word:{pair(word[j-1],word[j]) for j in range(6)}
    star=lambda rays:{pair(rays[j-1],rays[j]) for j in range(3)}
    GA,GB=graph(wordA),graph(wordB);domain=list(combinations_with_replacement(('a','b','c','r'),3))
    valid=[rays for rays in domain if star(rays)<=GA|GB]
    assert len(domain)==20 and valid==list(map(tuple,certificate['repeat_subfamily']['legal_ray_multisets']))
    assert not any(pair('b','c') in star(rays) for rays in domain if star(rays)<=GA)
    assert not any(pair('r','c') in star(rays) for rays in domain if star(rays)<=GB)
    native_words=[wordA,wordA,wordB,wordB]
    used=[tuple(sorted(native_words[i][e] for i,e in cycle)) for cycle in links]
    assert sorted(used)==sorted([ray for ray in [('a','a','a'),('a','b','c'),('a','c','r'),('b','b','c')] for _ in range(2)])
    for word,expected in ((wordA,(1,1)),(wordB,(1,0))):
        assert tuple(sum(tuple(word[(k+j)%6] for j in range(6))==word for k in range(6)) if mode==0 else
                     sum(tuple(word[(k-j)%6] for j in range(6))==word for k in range(6)) for mode in (0,1))==expected
    repeat=R.hom([a,c,a,c],R);A=list(map(repeat,A));B=list(map(repeat,B))
    bs=2*a-c;rs=3*a-2*c
    assert [a-c,bs-c,a-bs,rs-a,rs-bs,rs-c]==[a-c,2*(a-c),c-a,2*(a-c),a-c,3*(a-c)]
    assert [a-cj(z) for z in A]==[A[j] for j in (1,0,5,4,3,2)]
    assert B[5]==a*w**2
    patches=[[A,[a-z for z in A],[B[5]-z for z in B],[a-B[5]+z for z in B]],
             [A,[w**4*z for z in B],[w**4*cj(z) for z in B],[a-B[5]+z for z in B]]]
    assert patches==[[[point(row) for row in face] for face in branch['vertices']]
                     for branch in certificate['repeat_subfamily']['local_branch_patches']]
    # Formal whole-polygon cone containment for every a>0,0<c<3a/2.
    # Unit normal heights and x bounds are homogeneous linear forms; endpoint
    # evaluation in c/a proves their nonnegativity on the entire open interval.
    def nonnegative(t):
        t=R(t);assert cj(t)==t and all(sum(e)==1 for e in t.dict())
        for v in (QQ(0),QQ(3)/2):
            value=QQbar(t.subs({a:QQ(1),c:v}));assert value.imag()==0
            if AA(value.real())<0:return False
        return True
    def in_sector(P,origin,j,k):
        for z in P:
            assert nonnegative(cross(w**j,z-origin)) and nonnegative(cross(z-origin,w**k))
    for patch in patches:
        in_sector(patch[0],0,0,2);in_sector(patch[1],0,4,0);in_sector(patch[2],0,2,4)
        in_sector(patch[0],a,1,3);in_sector(patch[1],a,3,5);in_sector(patch[3],a,5,1)
        assert all(nonnegative(-(z+cj(z))/2) for z in patch[2])
        assert all(nonnegative((z+cj(z))/2-a) for z in patch[3])
    contacts=[[(0,0,1,0),(0,5,2,5),(1,1,2,4),(0,1,3,4),(1,5,3,5)],
              [(0,0,1,5),(0,5,2,5),(1,0,2,0),(0,1,3,4),(1,4,3,5)]]
    for patch,rows in zip(patches,contacts):
        for i,e,j,f in rows:
            assert {patch[i][e],patch[i][(e+1)%6]}=={patch[j][f],patch[j][(f+1)%6]}
    # Independent exact fixture separating-axis checks, including reflected faces.
    sub={p:QQ(1),q:QQ(3)/4,a:QQ(1),c:QQ(3)/4};ev=lambda z:QQbar(R(z).subs(sub))
    actual=[list(map(ev,P)) for P in faces];pu,pv=ev(u),ev(v)
    cr=lambda x,y:AA((x.conjugate()*y).imag());det=cr(pu,pv);assert det>0
    separated=lambda P,Q:any(max([cr(edge,z) for z in P])<=min([cr(edge,z) for z in Q]) or
                             max([cr(edge,z) for z in Q])<=min([cr(edge,z) for z in P])
                             for poly in (P,Q) for i in range(6) for edge in [poly[(i+1)%6]-poly[i]])
    boxes=[]
    for P in actual:
        coords=[(cr(z,pv)/det,cr(pu,z)/det) for z in P]
        boxes.append([(min(z[j] for z in coords),max(z[j] for z in coords)) for j in range(2)])
    records=[];count=0
    for i,j in product(range(4),repeat=2):
        bounds=[(int((boxes[i][d][0]-boxes[j][d][1]).ceil()),int((boxes[i][d][1]-boxes[j][d][0]).floor())) for d in range(2)]
        shifts=[]
        for n,t in product(*(range(lo,hi+1) for lo,hi in bounds)):
            if i==j and n==t==0:continue
            other=[z+n*pu+t*pv for z in actual[j]];assert separated(actual[i],other),(i,j,n,t)
            shifts.append([n,t]);count+=1
        records.append({'faces':[i,j],'coordinate_integer_bounds':list(map(list,bounds)),'translations':shifts})
    assert records==certificate['exact_fixture']['complete_overlap_domain'] and count==24
    assert count==certificate['exact_fixture']['translated_overlap_comparisons']
    assert len(records)==certificate['exact_fixture']['ordered_face_pairs']==16
    fixture_record=certificate['exact_fixture']
    fixture_area=ev(parse(fixture_record['area_covolume']))
    assert fixture_area.real()==0 and AA(fixture_area.imag())==det
    assert actual==[[ev(point(row)) for row in P] for P in fixture_record['motif_vertices']]
    assert [pu,pv]==[ev(point(row)) for row in fixture_record['periods']]
    local_count=0
    for patch in patches:
        P=list(map(lambda face:list(map(ev,face)),patch))
        for i in range(4):
            for j in range(i+1,4):assert separated(P[i],P[j]);local_count+=1
    assert local_count==12==fixture_record['local_branch_pairwise_separations']
    print('PASS independent 4D closures, strict supporting identities, 24 derived twins, 8 zero-holonomy links, and area/covolume')
    print('PASS full adjacent-repeat branch cone, both endpoint seams, intrinsic reflections, 20 local stars and monohedral obstructions')
    print('PASS retained coordinates and all 16 fixture bounds, 24 complete lattice separations and 12 branch-patch separations')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    main()
