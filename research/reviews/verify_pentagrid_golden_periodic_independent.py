#!/usr/bin/env python3
"""Fresh exact AA clipping check; imports no pentagrid search implementation."""
import json
from itertools import product
from pathlib import Path
from sage.all import AA, QQ, QQbar, matrix, vector

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'research/certificates'
phi=(1+AA(5).sqrt())/2
z=QQbar(phi/2)+QQbar.gen()*QQbar(AA(10-2*AA(5).sqrt()).sqrt()/4)
assert z**4-z**3+z**2-z+1 == 0
assert z.imag()>0 and QQ(4)/5<z.real()<QQ(81)/100

def point(q):
    return vector(AA,(AA(QQbar(q).real()),AA(QQbar(q).imag())))

def decode(row):
    return point(sum(QQ(c)*z**i for i,c in enumerate(row)))

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def area(p):
    return sum(cross(a,b) for a,b in zip(p,p[1:]+p[:1]))/2 if p else AA(0)

def convex(p):
    assert area(p)>0
    for i,a in enumerate(p):
        edge=p[(i+1)%5]-a
        assert all(cross(edge,w-a)>0 for j,w in enumerate(p)
                   if j not in (i,(i+1)%5))

def clip(subject,boundary):
    result=subject
    for a,b in zip(boundary,boundary[1:]+boundary[:1]):
        if not result:
            break
        out=[]
        for p,q in zip(result,result[1:]+result[:1]):
            sp=cross(b-a,p-a); sq=cross(b-a,q-a)
            if sp>=0:
                out.append(p)
            if (sp<0 and sq>0) or (sp>0 and sq<0):
                out.append(p+sp/(sp-sq)*(q-p))
            elif sp<0 and sq==0:
                out.append(q)
        result=out
    return result

WORDS={'U':(1,3,4,4,3),'V':(2,2,4,3,4),'W':(3,3,3,3,3)}

def verify_closure_domain():
    certificate=json.loads((CERT/'pentagrid-golden-metric-closure.json').read_text())
    assert certificate['field']['polynomial']=='x^4-x^3+x^2-x+1'
    records={row['name']:row for row in certificate['records']}
    assert set(records)==set(WORDS) and len(certificate['records'])==3
    found={}
    for name,angles in WORDS.items():
        dirs=[QQbar(1)]
        for m in angles[:-1]:
            dirs.append(dirs[-1]*z**(5-m))
        assert dirs[-1]*z**(5-angles[-1])==1
        record=records[name]
        assert record['angles_after_sides_in_pi_over_5']==list(angles)
        assert record['normalized_exponent_vectors_tested']==781
        saved={tuple(row['side_exponents']):row for row in record['closed']}
        assert len(saved)==len(record['closed'])
        rows=[]
        for powers in product(range(4),repeat=5):
            if min(powers)!=0:
                continue
            lengths=[QQbar(phi)**e for e in powers]
            if sum(l*d for l,d in zip(lengths,dirs))!=0:
                continue
            p=[point(0)]
            for length,direction in zip(lengths[:-1],dirs[:-1]):
                p.append(p[-1]+point(length*direction))
            convex(p)
            for i in range(5):
                before=p[i]-p[(i+1)%5]
                after=p[(i+2)%5]-p[(i+1)%5]
                assert before.dot_product(after)==lengths[i].real()*lengths[(i+1)%5].real()*AA((z**angles[i]).real())
            assert powers in saved
            assert [decode(row) for row in saved[powers]['vertices']]==p
            rows.append(list(powers))
        assert {tuple(row) for row in rows}==set(saved)
        found[name]=rows
    return found

def main():
    closure_words=verify_closure_domain()
    U=[point(q) for q in (0,QQbar(phi)**3,z+z**2+z**3,z**2+z**3,z**3)]
    W=[point(q) for q in (0,1,1+z**2,z+z**3,z**3)]
    convex(U);convex(W)
    rawU=[QQbar(0),QQbar(phi)**3,z+z**2+z**3,z**2+z**3,z**3]
    rawW=[QQbar(0),QQbar(1),1+z**2,z+z**3,z**3]
    P=[U,[point(-q+QQbar(phi)**3) for q in rawU],
       [point(z*q+z**2+z**3) for q in rawW],
       [point(z**2*q+z**3) for q in rawW]]
    for p in P:
        convex(p)
    u=point(z+z**2+z**3);v=point(4-z+z**2-5*z**3)
    lattice=matrix(AA,[[u[0],v[0]],[u[1],v[1]]])
    determinant=lattice.det()
    assert determinant==-(8+12*phi)*AA(z.imag())<0
    assert area(U)==(7+9*phi)/2*AA(z.imag())
    assert area(W)==(1+3*phi)/2*AA(z.imag())
    assert sum(area(p) for p in P)==abs(determinant)
    certificate=json.loads((CERT/'pentagrid-golden-metric-periodic.json').read_text())
    assert [decode(row) for row in certificate['U_vertices']]==U
    assert [decode(row) for row in certificate['W_vertices']]==W
    assert [decode(row) for row in certificate['lattice']]==[u,v]
    assert [[decode(row) for row in p] for p in certificate['placed_polygons']]==P
    assert decode(certificate['normalized_lattice_determinant'])==point(determinant/AA(z.imag()))
    assert certificate['area_identity_exact'] is True

    # Derive the complete overlap domain using the inverse lattice matrix,
    # then clip polygons instead of reusing the author's separating-axis test.
    inverse=lattice.inverse()
    boxes=[]
    for p in P:
        coordinates=[inverse*w for w in p]
        boxes.append([(min(w[k] for w in coordinates),max(w[k] for w in coordinates)) for k in (0,1)])
    tests=[]
    for i,j in product(range(4),repeat=2):
        limits=[range(int((boxes[i][k][0]-boxes[j][k][1]).ceil()),
                      int((boxes[i][k][1]-boxes[j][k][0]).floor())+1) for k in (0,1)]
        for m,n in product(*limits):
            if i==j and m==n==0:
                continue
            moved=[w+m*u+n*v for w in P[j]]
            assert area(clip(P[i],moved))==0,(i,j,m,n)
            tests.append([i,j,m,n])
    assert tests==certificate['exact_overlap_shift_tests']
    assert len(tests)==certificate['exact_overlap_shift_test_count']==38

    # Independently reconstruct the corner permutation and seam translations.
    torus=json.loads((CERT/'pentagrid-golden-metric-four-face-tori.json').read_text())
    rows=[r for r in torus['records'] if r['status']=='witness_found']
    assert len(rows)==1
    row=rows[0]
    assert row['B_angle_name']=='W' and row['B_side_exponents']==[0]*5
    witness=row['witness'];assert witness['reflected']==[False]*4
    mates={}
    for a,b in witness['side_pairs']:
        a=tuple(a);b=tuple(b)
        assert a not in mates and b not in mates and a!=b
        mates[a]=b;mates[b]=a
    assert set(mates)==set(product(range(4),range(5)))
    for (f,i),(g,j) in mates.items():
        offset=P[f][i]-P[g][(j+1)%5]
        assert offset==P[f][(i+1)%5]-P[g][j]
        assert all(c in QQ and QQ(c).denominator()==1 for c in inverse*offset)
    permutation={a:(b[0],(b[1]+1)%5) for a,b in mates.items()}
    unseen=set(permutation);cycles=[]
    vertex_angles=[(3,1,3,4,4)]*2+[(3,3,3,3,3)]*2
    while unseen:
        first=min(unseen);cycle=[];current=first
        while current in unseen:
            unseen.remove(current);cycle.append(current);current=permutation[current]
        assert current==first
        assert sum(vertex_angles[f][i] for f,i in cycle)==10
        cycles.append(frozenset(cycle))
    assert set(cycles)=={frozenset(map(tuple,c)) for c in witness['corner_classes']}
    assert len(cycles)==6
    connected={0}
    while True:
        larger=connected|{g for (f,i),(g,j) in mates.items() if f in connected}
        if larger==connected:
            break
        connected=larger
    assert len(connected)==4
    print(json.dumps({'verdict':'valid exact periodic whole-plane witness',
                      'normalized_metrics_tested':2343,
                      'closed_metrics':{name:len(rows) for name,rows in closure_words.items()},
                      'complete_overlap_tests':len(tests),'corner_links':len(cycles),
                      'rank_two_lattice':True,'motif_area_equals_covolume':True},indent=2))

if __name__=='__main__':
    main()
