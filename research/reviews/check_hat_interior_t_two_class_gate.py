#!/usr/bin/env python3
"""Independent midpoint branch equations and strict-support audit."""
import argparse,hashlib,importlib.util,itertools,json
from pathlib import Path
from sage.all import AA
sp=importlib.util.spec_from_file_location('independent_changed_hat',Path(__file__).with_name('check_hat_three_pentagon_one_hexagon_gate.py'))
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
K,r,R,b,u,v,H,g=old.K,old.r,old.R,old.b,old.u,old.v,old.H,old.g
V=(u,v);W=tuple((H[4][i]+V[i])/2 for i in (0,1))
P={'P0':H[:5]+[W],'P1':H[4:9]+[V],'P2':[V]+H[8:12],'P3':[H[0],W,V,H[11],H[12]]}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/hat-interior-t-two-class-feature-gate.json');cert=json.loads(path.read_text())
    assert {n:[[R(z) for z in p] for p in A] for n,A in cert['polygons_at_forced_midpoint'].items()}=={n:[list(p) for p in A] for n,A in P.items()}
    L=old.distance(H[4],V);G=old.distance(H[8],V);F=old.distance(H[0],W);J=old.distance(H[11],V)
    lengths=lambda A:[old.distance(x,y) for x,y in zip(A,A[1:]+A[:1])]
    assert lengths(P['P0'])==[b*b,1,4,1,L/4,F]
    assert lengths(P['P1'])==[b*b,b*b,1,1,G,L]
    assert lengths(P['P2'])==[G,b*b,b*b,1,J]
    assert lengths(P['P3'])==[F,L/4,J,1,b*b]
    equations={'A':[b-1,L-4,F-G],'B':[L-4,G-1,F-b*b]}
    records={row['branch']:row for row in cert['branches']};assert set(records)==set(equations)
    count=0
    for branch,eq in equations.items():
        I=R.ideal(eq);assert I.dimension()==0
        assert list(map(str,I.groebner_basis()))==records[branch]['groebner_basis']
        points=I.variety(AA);assert len(points)==2
        exact=[]
        for sol in points:
            values=tuple(sol[x] for x in (b,u,v));assert values[0]>0
            assert all(polynomial(*values)==0 for polynomial in eq)
            polys={n:old.evaluate(A,*values) for n,A in P.items()}
            failed=[(n,i,z) for n,A in polys.items() for i,z in enumerate(old.supports(A)) if z<=0]
            assert failed;exact.append(tuple(map(str,values)));count+=1
        assert set(exact)=={tuple(row['b_u_v']) for row in records[branch]['real_points']}
        assert all(not row['strict_convex'] and row['failed_supports'] for row in records[branch]['real_points'])
    assert count==4 and not cert['strict_two_class_survivors']
    vals=(K(1),K(9)/5,K(0));sample={n:[tuple(K(z(*vals)) for z in p) for p in A] for n,A in P.items()}
    assert {n:[[str(z) for z in p] for p in A] for n,A in sample.items()}==cert['sample_polygons']
    assert all(all(z>0 for z in old.supports(A)) for A in sample.values())
    for A,B in itertools.combinations(sample.values(),2):assert g.area2(g.clip(A,B))==0
    outline=[tuple(K(z(*vals)) for z in p) for p in H]
    assert g.same(g.boundary(list(sample.values())),g.simplify(outline))
    ww=tuple(K(z(*vals)) for z in W);hh=tuple(K(z(*vals)) for z in H[4]);vv=(vals[1],vals[2])
    assert ww==tuple((x+y)/2 for x,y in zip(hh,vv)) and hh!=vv
    result={'status':'PASSED','necessary_midpoint_branch_count':2,'exact_real_points':4,'strict_two_class_survivors':0,'positive_strict_convex_partition_sample':['1','9/5','0'],'genuine_flat_interior_contact':True,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Specified straight-side interior-T topology only; side multisets force midpoint before exact branch gate'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
