#!/usr/bin/env python3
"""Independent exterior-turn construction and exact full-domain closure audit."""
import argparse,collections,hashlib,importlib.util,itertools,json
from pathlib import Path
from sage.all import AA,QuadraticField,PolynomialRing,matrix
K=QuadraticField(3,'r',embedding=AA(3).sqrt());r=K.gen()
R=PolynomialRing(K,'t');t=R.gen();F=R.fraction_field()
LOW=AA(3).sqrt()-2;HIGH=2-AA(3).sqrt()
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def directions(angle_coefficients):
    half=(F(1-t*t)/F(1+t*t),F(2*t)/F(1+t*t));v=(F(1),F(0));answer=[v]
    for coefficient in angle_coefficients[1:]:
        turn=(F(K(1)/2),F(r/2));rotation=half if coefficient<0 else (half[0],-half[1])
        for _ in range(abs(coefficient)):turn=mul(turn,rotation)
        v=mul(v,turn);answer.append(v)
    return answer
def roots(p):return set(p.roots(AA,multiplicities=False)) if p else set()
def interior(p):return {v for v in roots(p) if LOW<v<HIGH and v!=0}
def evaluate(M,z):return matrix(AA,[[v.numerator()(z)/v.denominator()(z) for v in row] for row in M.rows()])
def positive(Q):
    basis=Q.right_kernel().basis();assert len(basis)<=1
    return bool(basis) and (all(v>0 for v in basis[0]) or all(v<0 for v in basis[0]))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--only',choices=('C','I'));ap.add_argument('--transport');args=ap.parse_args()
    ledgerpath=Path('research/certificates/two-hexagon-interleaved-local-side-gate.json')
    sourcepath=Path('research/certificates/two-hexagon-interleaved-symbolic-closure.json')
    ledger=json.loads(ledgerpath.read_text());cert=json.loads(sourcepath.read_text())
    AD=directions([1,1,-1,1,-1,-1]);BD={'C':directions([-2,-2,-2,2,2,2]),'I':directions([-2,-2,2,-2,2,2])}
    summary=[];tested_points=0;tested_intervals=0
    for pair in cert['rows']:
        b=pair['B'];local=next(row for row in ledger['rows'] if row['B']==b)
        if args.only and b!=args.only:continue
        stored={tuple(row['closure']):row for row in pair['closure_records']}
        assert set(stored)=={tuple(row['closure']) for row in local['distinct_closures']}
        stats=collections.Counter();excluded=0;generic_nullity_one=0;allowed=[]
        for row in local['distinct_closures']:
            eq=row['closure'];record=stored[tuple(eq)];k=max(eq)+1
            columns=[]
            for lengthclass in range(k):
                column=[]
                for species,dd in enumerate((AD,BD[b])):
                    column.extend(sum((dd[j][axis] for j in range(6) if eq[6*species+j]==lengthclass),F(0)) for axis in (0,1))
                columns.append(column)
            M=matrix(F,columns).transpose();assert M==matrix(F,record['matrix'])
            rank=M.rank();assert rank==record['generic_rank'] and k==record['number_of_length_classes']
            assert row['count']==record['ring_count']
            for entry in M.list():assert not interior(R(entry.denominator()))
            gcd=R(0)
            for rows in itertools.combinations(range(4),rank):
                for cols in itertools.combinations(range(k),rank):
                    gcd=gcd.gcd(R(M.matrix_from_rows_and_columns(rows,cols).det().numerator()))
            gcd=gcd.monic();basis=M.right_kernel().basis()
            if rank==k:
                assert list(map(str,gcd.list()))==record['maximal_minor_numerator_gcd']
                expected='FINITE_EXCEPTIONS' if interior(gcd) else 'NO_NONZERO_VECTOR_ALL_ADMISSIBLE_ANGLES'
            else:expected='GENERIC_KERNEL';generic_nullity_one+=len(basis)==1
            assert record['verdict']==expected;stats[expected]+=row['count']
            if expected=='NO_NONZERO_VECTOR_ALL_ADMISSIBLE_ANGLES':excluded+=row['count'];continue
            gate=record['positive_length_gate']
            if len(basis)>1:
                assert [[str(v) for v in rr] for rr in basis]==gate['generic_kernel_basis']
                if gate['verdict']=='UNRESOLVED_MULTI_DIMENSIONAL_KERNEL':allowed.append(tuple(eq));continue
                assert gate['verdict']=='NO_STRICTLY_POSITIVE_LENGTH_VECTOR_AT_ANY_ADMISSIBLE_ANGLE'
                assert list(map(str,gcd.list()))==gate['generic_rank_drop_minor_gcd'] and not interior(gcd)
                relation=gate['opposed_coordinate_relation'];i,j=relation['coordinates'];ratio=F(relation['ratio'])
                assert all(vector[j]==ratio*vector[i] for vector in basis)
                assert not interior(R(ratio.denominator()))
                poles=set().union(*(interior(R(entry.denominator())) for vector in basis for entry in vector))
                for z in poles:
                    Q=evaluate(M,z);assert Q.rank()==rank
                    q=ratio.numerator()(z)/ratio.denominator()(z)
                    assert all(vector[j]==q*vector[i] for vector in Q.right_kernel().basis());tested_points+=1
                endpoints=[LOW]+sorted(interior(R(ratio.numerator()))|{AA(0)})+[HIGH]
                for left,right in zip(endpoints,endpoints[1:]):
                    z=(left+right)/2;assert ratio.numerator()(z)/ratio.denominator()(z)<=0;tested_intervals+=1
                for z in endpoints[1:-1]:assert ratio.numerator()(z)/ratio.denominator()(z)<=0
                excluded+=row['count'];continue
            assert list(map(str,gcd.list()))==gate['generic_rank_drop_minor_gcd']
            assert [[str(v) for v in rr] for rr in basis]==gate['generic_kernel_basis']
            points=interior(gcd)
            for vector in basis:
                for entry in vector:points|=interior(R(entry.numerator()))|interior(R(entry.denominator()))
            retained=gate['partition_checks'];pointrows=[q for q in retained if q['type']=='point']
            assert sorted(str(v) for v in points)==sorted(q['parameter'] for q in pointrows)
            any_positive=False
            for z in points:
                Q=evaluate(M,z);ok=positive(Q);any_positive|=ok;tested_points+=1
                check=next(q for q in pointrows if q['parameter']==str(z))
                assert Q.rank()==check['rank'] and ok==check['positive_kernel_exists']
            endpoints=[LOW]+sorted(points|{AA(0)})+[HIGH]
            intervals=[q for q in retained if q['type']=='open_interval']
            assert len(intervals)==len(endpoints)-1
            for (left,right),check in zip(zip(endpoints,endpoints[1:]),intervals):
                assert str(left)==check['left'] and str(right)==check['right']
                ok=positive(evaluate(M,(left+right)/2));any_positive|=ok
                assert ok==check['positive_kernel_exists'];tested_intervals+=1
            assert gate['verdict']==('POSITIVE_KERNEL_ON_DOMAIN_SUBSET' if any_positive else 'NO_STRICTLY_POSITIVE_LENGTH_VECTOR_AT_ANY_ADMISSIBLE_ANGLE')
            if any_positive:allowed.append(tuple(eq))
            else:excluded+=row['count']
        assert dict(stats)==pair['ring_weighted_stats']
        if b=='I':assert excluded==local['native_ring_count']
        summary.append({'B':b,'closures':len(stored),'native_rings_excluded':excluded,'unresolved_native_ring_count':local['native_ring_count']-excluded,'allowed_closures':allowed,'rank_strata':dict(stats),'generic_nullity_one_closures':generic_nullity_one})
    assert {r['B'] for r in summary}==({args.only} if args.only else {'C','I'})
    transport_check=None
    if args.transport:
        assert not args.only or args.only=='C'
        transport_path=Path(args.transport);transport=json.loads(transport_path.read_text())
        spec=importlib.util.spec_from_file_location('independent_native_seams',Path(__file__).with_name('check_two_hexagon_interleaved_local_side_gate.py'))
        local=importlib.util.module_from_spec(spec);spec.loader.exec_module(local);g=local.g
        allowed=set(next(row for row in summary if row['B']=='C')['allowed_closures'])
        assert allowed==set(map(tuple,transport['allowed_native_side_closures']))
        states=[]
        for bi,bp in enumerate(g.P):
            bw=g.placed(g.WORDS['C'],bp);choices=[]
            for z in g.D:
                incidences=[inc for inc in g.INC if z in inc]
                choices.append([i for i,p in enumerate(g.P) if all(g.placed(g.WORDS['I'],p)[inc[z]]==bw[inc[(0,0)]] for inc in incidences)])
            for aa in itertools.product(*choices):
                eq=local.closure(bp,[g.P[i] for i in aa])
                if eq in allowed:states.append({'B':bi,'A_ring':list(aa),'closure':list(eq)})
        assert states==transport['states'] and len(states)==96
        relations=[]
        for delta in g.DELTA:
            overlaps=[(i,j) for i,x in enumerate(g.D) for j,y in enumerate(g.D) if x==g.add(delta,y)]
            relations.append({(i,j) for i,a in enumerate(states) for j,b in enumerate(states) if all(a['A_ring'][p]==b['A_ring'][q] for p,q in overlaps)})
        assert relations==[set(map(tuple,rel)) for rel in transport['compatibility']]
        alive=set(range(len(states)));trace=[]
        while alive:
            bad=[]
            for i in sorted(alive):
                for k in range(6):
                    direction=g.DELTA.index(g.sub(g.DELTA[(k+1)%6],g.DELTA[k]))
                    left={j for a,j in relations[k] if a==i and j in alive};right={j for a,j in relations[(k+1)%6] if a==i and j in alive}
                    if not any((j,l) in relations[direction] for j in left for l in right):bad.append([i,k]);break
            if not bad:break
            trace.append(bad);alive-={i for i,k in bad}
        assert trace==transport['triangle_deletion_rounds'] and sorted(alive)==transport['survivors']==[] and transport['verdict']=='EMPTY'
        transport_check={'native_ring_superset':len(states),'triangle_deletion_rounds':len(trace),'survivors':0,'source_sha256':hashlib.sha256(transport_path.read_bytes()).hexdigest()}
    result={'status':'PASSED','full_domain_rows':summary,'exceptional_points_checked':tested_points,'sign_intervals_checked':tested_intervals,'source_sha256':hashlib.sha256(sourcepath.read_bytes()).hexdigest(),'local_ledger_sha256':hashlib.sha256(ledgerpath.read_bytes()).hexdigest(),'scope':'Correct exact local exclusion and conservative residual closure ledger; I/I excluded, I/C may need global transport, no conclusion for I/ALT'}
    result['contiguous_global_transport']=transport_check
    if transport_check:result['scope']='All I/C and I/I pairs impossible via exact geometry and necessary spatial transport; I/ALT remains open'
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
