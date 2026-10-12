#!/usr/bin/env python3
"""Independent side-multiset reduction and analytic circle intersections."""
import argparse,hashlib,importlib.util,itertools,json
from pathlib import Path
from sage.all import AA,QQ,PolynomialRing
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('old_hat_review',HERE/'check_hat_four_pentagon_deformation.py')
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
g=old.geometry;K,r=g.K,g.r
R=PolynomialRing(K,'b,u,v');b,u,v=R.gens()
H=[tuple(R(x) for x in p) for p in old.H];V=(u,v)
P={'P6':[H[i] for i in (0,1,2,3,4)],'P9':[H[0],H[4],V,H[11],H[12]],'P48':[H[i] for i in (4,5,6,7,8)]+[V],'P192':[V]+[H[i] for i in (8,9,10,11)]}
def distance(p,q):return sum((x-y)**2 for x,y in zip(p,q))
def supports(A):return [g.cross(g.subtract(A[(i+1)%len(A)],A[i]),g.subtract(z,A[i])) for i in range(len(A)) for j,z in enumerate(A) if j not in (i,(i+1)%len(A))]
def evaluate(A,bb,uu,vv):return [tuple(AA(x(bb,uu,vv)) for x in p) for p in A]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/hat-three-pentagon-one-hexagon-feature-gate.json');cert=json.loads(path.read_text())
    assert {name:[[R(x) for x in p] for p in points] for name,points in cert['polygons'].items()}=={name:[list(p) for p in points] for name,points in P.items()}
    assert {name:[R(s) for s in values] for name,values in cert['strict_support_inequalities'].items()}=={name:supports(A) for name,A in P.items()}
    L=distance(H[0],H[4]);assert L==b*b-3*r*b+9
    assert [distance(x,y) for x,y in zip(P['P6'],P['P6'][1:]+P['P6'][:1])]==[b*b,1,4,1,L]
    assert [distance(P['P192'][i],P['P192'][i+1]) for i in (1,2,3)]==[b*b,b*b,1]
    # Repeated b² in P192 must already be repeated in P6. This union of
    # equations is exact even when additional inventory values coincide.
    S=PolynomialRing(K,'z');z=S.gen()
    allowed=set()
    for polynomial in (z*z-1,z*z-4,3*r*z-9):
        allowed.update(w for w in polynomial.roots(AA,multiplicities=False) if w>0)
    assert allowed=={AA(1),AA(2),AA(r)}
    assert [distance(P['P9'][i],P['P9'][(i+1)%5]) for i in (0,3,4)]==[L,1,b*b]
    # Cancellation of these three entries in the equal multisets leaves
    # exactly squared lengths 1 and 4 on the two variable P9 sides.
    rows={(row['b'],row['squared_Vh4'],row['squared_Vh11']):row for row in cert['circle_cases']};assert len(rows)==6
    points=0;empty_cases=0;failed=[]
    for bb in (K(1),K(2),r):
        centre=tuple(AA(x(bb,0,0)) for x in H[4]);other=tuple(AA(x(bb,0,0)) for x in H[11]);delta=g.subtract(other,centre);D=g.dot(delta,delta)
        for first,second in ((1,4),(4,1)):
            row=rows[str(bb),first,second];lam=(first-second+D)/(2*D);height=AA(first)/D-lam*lam
            if height<0:assert not row['real_points'];empty_cases+=1;continue
            assert height>0;assert len(row['real_points'])==2
            candidates=[]
            for sign in (-1,1):
                h=sign*height.sqrt();uu=centre[0]+lam*delta[0]-h*delta[1];vv=centre[1]+lam*delta[1]+h*delta[0]
                assert g.dot(g.subtract((uu,vv),centre),g.subtract((uu,vv),centre))==first
                assert g.dot(g.subtract((uu,vv),other),g.subtract((uu,vv),other))==second
                polys={name:evaluate(A,bb,uu,vv) for name,A in P.items()}
                bad=[(name,i,str(value)) for name,A in polys.items() for i,value in enumerate(supports(A)) if value<=0]
                assert bad;points+=1;failed.append({'b':str(bb),'squared_radii':[first,second],'failed_supports':len(bad)})
                candidates.append((str(uu),str(vv)))
            assert set(candidates)=={(q['u'],q['v']) for q in row['real_points']}
            assert all(not q['all_strict_convex'] and q['failed_supports'] for q in row['real_points'])
    assert points==8 and empty_cases==2 and not cert['strict_two_class_survivors']
    sample={name:[tuple(K(x(r,2,-r/10)) for x in p) for p in A] for name,A in P.items()}
    assert all(all(value>0 for value in supports(A)) for A in sample.values())
    for A,B in itertools.combinations(sample.values(),2):assert g.area2(g.clip(A,B))==0
    outline=[tuple(K(x(r,2,-r/10)) for x in p) for p in H]
    assert g.same(g.boundary(list(sample.values())),g.simplify(outline))
    result={'status':'PASSED','positive_strict_convex_partition_sample':['sqrt3','2','-sqrt3/10'],'necessary_positive_b_values':['1','2','sqrt3'],'circle_systems':6,'empty_circle_systems':2,'exact_real_points':points,'strict_two_class_survivors':0,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Specified positive-b three-pentagon/one-hexagon cut only; analytic side-multiset superset excludes all strict two-class realizations'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
