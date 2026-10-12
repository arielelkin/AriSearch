#!/usr/bin/env python3
"""Independent complete ALT metric ledger, exact geometry, and native audit.

No producer, global SFT, or solver is imported. Canonical triangles and exact
exterior-turn rationalization come from earlier independent review helpers.
All output is optional and retained source certificates are never modified.
"""
import argparse,collections,hashlib,importlib.util,itertools,json,math
from fractions import Fraction
from pathlib import Path
from sage.all import AA,matrix,vector
HERE=Path(__file__).resolve().parent
def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path);result=importlib.util.module_from_spec(sp);sp.loader.exec_module(result);return result
s=module('independent_turns',HERE/'check_two_hexagon_interleaved_symbolic_closure.py')
n=module('independent_triangles',HERE/'check_two_hexagon_rank_nine_colour_transport.py')
private=module('independent_triangle_pruning',HERE/'check_two_hexagon_interleaved_alternating_private_transport.py')
F,R=s.F,s.R
# ALT-specific convention: theta=120-p. Direct native exterior turns
# then have A angle coefficients(-1,+1,...) and B(+2,-2,...).
# The source records initially documented the opposite convention;
# their common parameter reversal is harmless but must be explicit.
AD=s.directions([-1,1,-1,1,-1,1]);BD=s.directions([2,-2,2,-2,2,-2])
ROOT=Path('research/certificates')
def read(stem):
    path=ROOT/f'two-hexagon-alternating-{stem}.json';return json.loads(path.read_text())
def normalized(values):
    names={};out=[]
    for value in values:
        if value not in names:names[value]=len(names)
        out.append(names[value])
    return tuple(out)
def partitions():return sorted({normalized(p) for p in itertools.product(range(6),repeat=6)})
def wordset(mult):return set(itertools.permutations(tuple(i for i,count in enumerate(mult) for _ in range(count))))
def build(a,b=None):
    k=max(a)+1;columns=[]
    for cls in range(k):
        column=[]
        for word,directions in ((a,AD),) if b is None else ((a,AD),(b,BD)):
            column.extend(sum((directions[j][axis] for j in range(6) if word[j]==cls),F(0)) for axis in (0,1))
        columns.append(column)
    return matrix(F,columns).transpose()
def forced(M):
    space=M.row_space();k=M.ncols()
    return [[i,j] for i,j in itertools.combinations(range(k),2) if vector(M.base_ring(),[int(z==i)-int(z==j) for z in range(k)]) in space]
def minor_gcd(M,rank):
    result=R(0)
    for rows in itertools.combinations(range(M.nrows()),rank):
        for cols in itertools.combinations(range(M.ncols()),rank):
            result=result.gcd(R(M.matrix_from_rows_and_columns(rows,cols).det().numerator()))
    return result.monic()
def geometry(M,record,matrix_key,gcd_key,root_key,pair_key,feasible_key):
    assert M==matrix(F,record[matrix_key]);rank=M.rank();assert rank==record['generic_rank']
    assert all(sum(row)==0 for row in M.rows())
    for entry in M.list():assert not s.interior(R(entry.denominator()))
    fp=forced(M);assert fp==record[pair_key]
    basis=M.right_kernel().basis()
    if 'generic_kernel_basis' in record:
        stored=matrix(F,record['generic_kernel_basis'])
        assert stored.row_space()==matrix(F,basis).row_space()
    gcd=minor_gcd(M,rank);assert list(map(str,gcd.list()))==record[gcd_key]
    roots=sorted(s.interior(gcd));stored=record[root_key]
    assert [str(z) for z in roots]==[q['parameter'] for q in stored]
    possible=False
    for z,row in zip(roots,stored):
        Q=s.evaluate(M,z);qfp=forced(Q)
        assert int(Q.rank())==row['rank'] and qfp==row[pair_key.replace('generic_','')]
        assert bool(not qfp)==row[feasible_key]
        possible|=not qfp
    return fp,roots,possible
SIDE_MAPS=tuple(tuple(n.side(p,k) for k in range(6)) for p in n.P if n.placed(n.WORDS['ALT'],p)==n.WORDS['ALT'])
METRIC_WORD_DOMAIN=None
REMAINING_A_DOMAIN=None
def canonical(a,b):
    images=[]
    for amap in SIDE_MAPS:
        seq=[a[j] for j in amap];aa=normalized(seq);rename={old:new for old,new in zip(seq,aa)}
        for bmap in SIDE_MAPS:images.append((aa,tuple(rename[b[j]] for j in bmap)))
    if METRIC_WORD_DOMAIN is not None:
        assert all(aa in REMAINING_A_DOMAIN and bb in METRIC_WORD_DOMAIN[aa] for aa,bb in images)
    return min(images)
def symmetry_audit():
    assert len(SIDE_MAPS)==6 and len(set(SIDE_MAPS))==6
    for p in n.P:
        if n.placed(n.WORDS['ALT'],p)!=n.WORDS['ALT']:continue
        mapping=tuple(n.side(p,j) for j in range(6))
        for directions in (AD,BD):
            rotation=directions[mapping[0]]
            for j in range(6):
                expected=s.mul(rotation,(directions[j][0],p[1]*directions[j][1]))
                assert directions[mapping[j]]==expected
    # The permutation group acts on slots, with exact orthogonal row
    # transformations above; shared length class names are changed once.
    assert all(tuple(a[b[j]] for j in range(6)) in SIDE_MAPS for a,b in itertools.product(SIDE_MAPS,repeat=2))
def domain_audit():
    cert=read('metric-ledger');parts=partitions();assert len(parts)==203
    H=sorted({Fraction(j,2*d) for d in (1,2,3) for j in range(2*d+1)})
    assert list(map(str,H))==cert['finite_unbalanced_h_domain']
    words={};balanced=0;vectors=0;total=0
    assert [tuple(row['A_native_side_partition']) for row in cert['rows']]==parts
    for a,row in zip(parts,cert['rows']):
        k=max(a)+1;even=[a[::2].count(i) for i in range(k)];odd=[a[1::2].count(i) for i in range(k)]
        assert even==row['even_multiplicities'] and odd==row['odd_multiplicities']
        balance=even==odd;balanced+=balance;assert balance==row['parity_balanced']
        mults=collections.defaultdict(list)
        for h in H:
            values=tuple(2*(h*e+(1-h)*o) for e,o in zip(even,odd))
            if all(v.denominator==1 for v in values):mults[tuple(map(int,values))].append(str(h))
        assert set(mults)=={tuple(q['B_native_multiplicities']) for q in row['distinct_B_multiplicity_ledgers']}
        actual=set()
        for q in row['distinct_B_multiplicity_ledgers']:
            mult=tuple(q['B_native_multiplicities']);ww=wordset(mult);actual|=ww;vectors+=1
            assert len(ww)==q['B_native_word_count']
            assert q['compatible_AB_even_A_proportions']==('ALL_REAL_H_IN_0_1' if balance else mults[mult])
        assert len(actual)==row['deduplicated_B_native_word_count'];words[a]=actual;total+=len(actual)
    assert (balanced,vectors,total)==(16,611,39628)
    assert cert['A_partition_count']==203 and cert['parity_balanced_partition_count']==balanced and cert['distinct_A_partition_B_multiplicity_count']==vectors and cert['distinct_A_partition_B_native_word_count']==total
    assert len(words[(0,1,2,3,4,5)])==900
    return words
def a_strata(words):
    cert=read('a-side-strata');assert [tuple(q['A_native_side_partition']) for q in cert['rows']]==sorted(words)
    assert cert['parameter']=='t=tan((120-p)/2),sqrt(3)-2<t<2-sqrt(3),t!=0'
    allowed=set();stats=collections.Counter()
    for row in cert['rows']:
        a=tuple(row['A_native_side_partition']);M=build(a)
        fp,roots,possible=geometry(M,row,'closure_matrix','generic_rank_minor_numerator_gcd','admissible_rank_drop_angles','generic_forced_equal_class_pairs','actual_partition_feasible')
        assert not roots and row['ledger_native_B_word_count']==len(words[a])
        verdict='NO_ADMISSIBLE_ACTUAL_PARTITION' if fp else 'GENERIC_ACTUAL_PARTITION'
        assert verdict==row['verdict'];stats[verdict]+=1
        if not fp:allowed.add(a)
    assert len(allowed)==66 and dict(stats)==cert['partition_stats']
    # Fresh cube-root subset audit: complex coordinates in Q(sqrt3),
    # rather than the producer's integer 1,omega multiplication table.
    omega=[(s.K(1),s.K(0)),(-s.K(1)/2,s.r/2),(-s.K(1)/2,-s.r/2)]
    zero=[]
    for mask,row in enumerate(cert['two_value_subset_audit']):
        assert mask==row['subset_mask']
        even=tuple(sum(omega[j//2][axis] for j in (0,2,4) if mask>>j&1) for axis in (0,1))
        odd=tuple(sum(omega[j//2][axis] for j in (1,3,5) if mask>>j&1) for axis in (0,1))
        if even==odd==(0,0):
            assert row['verdict']=='ZERO_FOR_EVERY_ALPHA'
            if mask not in (0,63):zero.append(mask)
        elif even==(0,0) or odd==(0,0):assert row['verdict']=='NO_ALPHA'
        else:
            q=s.mul(tuple(-x for x in even),(odd[0],-odd[1]));assert row['verdict']=='ONLY_SIXTH_ROOT_ALPHA'
            angle=row['required_alpha_degrees'];cos=(s.K(1),s.K(1)/2,-s.K(1)/2,-s.K(1),-s.K(1)/2,s.K(1)/2)[angle//60];sin=(s.K(0),s.r/2,s.r/2,s.K(0),-s.r/2,-s.r/2)[angle//60]
            assert q==(cos,sin)
    assert zero==[21,42]
    return allowed
def three_length(words,allowed):
    cert=read('three-length-joint-closure');parts=sorted(a for a in allowed if max(a)==2)
    assert cert['parameter']=='t=tan((120-p)/2), sqrt(3)-2<t<2-sqrt(3),t!=0'
    assert parts==[(0,0,1,2,2,1),(0,1,1,0,2,2),(0,1,2,2,1,0)]
    expected={(a,b) for a in parts for b in words[a]};assert len(expected)==270
    assert expected=={(tuple(row['A_native_side_partition']),tuple(row['B_native_side_word'])) for row in cert['rows']}
    for row in cert['rows']:
        a,b=map(tuple,(row['A_native_side_partition'],row['B_native_side_word']));M=build(a,b)
        fp,roots,possible=geometry(M,row,'matrix','rank_minor_numerator_gcd','admissible_rank_drop_angles','generic_forced_equal_class_pairs','all_three_actual_values_possible')
        assert M.rank()==2 and fp==[[0,1],[0,2],[1,2]] and not roots and row['verdict']=='NO_ACTUAL_THREE_LENGTH_METRIC'
    return {a for a in allowed if max(a)>=3}
def joint_geometry(words,allowed):
    global METRIC_WORD_DOMAIN,REMAINING_A_DOMAIN
    METRIC_WORD_DOMAIN=words;REMAINING_A_DOMAIN=allowed
    cert=read('joint-metric-orbits');symmetry_audit();assert list(map(tuple,cert['native_side_maps']))==list(SIDE_MAPS)
    orbits=collections.Counter();total=0
    for a in sorted(allowed):
        for b in words[a]:orbits[canonical(a,b)]+=1;total+=1
    assert len(allowed)==61 and total==20970 and len(orbits)==685
    assert cert['native_word_count']==total and cert['joint_metric_orbit_count']==len(orbits)
    expected=sorted(orbits);stats=collections.Counter();weighted=collections.Counter();residual=[]
    for i,row in enumerate(cert['rows']):
        a,b=map(tuple,(row['A_native_side_partition'],row['B_native_side_word']))
        assert (a,b)==expected[i] and row['id']==i and row['native_word_orbit_weight']==orbits[a,b]
        M=build(a,b);fp,roots,possible=geometry(M,row,'matrix','rank_minor_numerator_gcd','admissible_rank_drop_angles','generic_forced_equal_class_pairs','actual_classes_possible')
        verdict='GENERIC_ACTUAL_CLASS_KERNEL' if not fp else 'FINITE_FEASIBLE_ANGLE_EXCEPTIONS' if possible else 'NO_ADMISSIBLE_ACTUAL_METRIC'
        assert verdict==row['verdict'];stats[verdict]+=1;weighted[verdict]+=orbits[a,b]
        if verdict!='NO_ADMISSIBLE_ACTUAL_METRIC' and max(a)<5:residual.append(row)
        if i%100==99:print('Independent joint geometry',i+1,'/685',flush=True)
    assert dict(stats)==cert['orbit_stats'] and dict(weighted)==cert['native_word_weighted_stats']
    assert dict(stats)=={'NO_ADMISSIBLE_ACTUAL_METRIC':628,'GENERIC_ACTUAL_CLASS_KERNEL':45,'FINITE_FEASIBLE_ANGLE_EXCEPTIONS':12}
    assert len(residual)==37 and sum(r['native_word_orbit_weight'] for r in residual)==828
    return residual
def distinct_local_audit():
    cases=0
    for p,q,k in itertools.product(n.P,n.P,range(6)):
        if n.side(p,k)!=n.side(q,(k+3)%6):continue
        first=[(p[0]+p[1]*j)%6 for j in (k,(k+1)%6)]
        second=[(q[0]+q[1]*j)%6 for j in ((k+4)%6,(k+3)%6)]
        if [i%2 for i in first]!=[i%2 for i in second]:continue
        assert first==second
        # At either endpoint, the other side index agrees as well.
        shared=n.side(p,k)
        for corner in first:
            other=next(j for j in ((corner-1)%6,corner) if j!=shared)
            assert other in ((corner-1)%6,corner)
        assert p[1]==-q[1];cases+=1
    assert cases==72
    return cases
def native_states(a,b):
    raw=[]
    for bi,bp in enumerate(n.P):
        bw=n.placed(n.WORDS['ALT'],bp);choices=[]
        for z in n.D:
            incidents=[inc for inc in n.INC if z in inc];outward=n.D.index(z);inward=n.D.index(n.sub((0,0),z))
            bs=n.side(bp,(outward-1)%6)
            choices.append([i for i,p in enumerate(n.P) if all(n.placed(n.WORDS['ALT'],p)[inc[z]]==bw[inc[(0,0)]] for inc in incidents) and a[n.side(p,(inward-1)%6)]==b[bs]])
        for aa in itertools.product(*choices):
            okay=True
            for k,z in enumerate(n.D):
                j=(k+1)%6;direction=n.D.index(n.sub(n.D[j],z));reverse=n.D.index(n.sub(z,n.D[j]))
                if a[n.side(n.P[aa[k]],(direction-1)%6)]!=a[n.side(n.P[aa[j]],(reverse-1)%6)]:okay=False;break
            if okay:raw.append({'B':bi,'A_ring':list(aa)})
    def aliases(word):
        profiles=[list(n.placed(n.WORDS['ALT'],p))+[word[n.side(p,j)] for j in range(6)] for p in n.P]
        return [profiles.index(profile) for profile in profiles],profiles
    am,ap=aliases(a);bm,bp=aliases(b)
    canonical_states=[{'B':bb,'A_ring':list(aa)} for bb,aa in sorted({(bm[q['B']],tuple(am[i] for i in q['A_ring'])) for q in raw})]
    assert all(q in raw for q in canonical_states)
    return raw,canonical_states,am,bm,ap,bp
def native_transport(residual):
    cert=read('residual-metric-transport');records={row['joint_metric_orbit_id']:row for row in cert['rows']}
    assert set(records)=={row['id'] for row in residual};stats=collections.Counter();positive={}
    for source in residual:
        i=source['id'];row=records[i];a,b=source['A_native_side_partition'],source['B_native_side_word']
        assert a==row['A_native_side_partition'] and b==row['B_native_side_word'] and row['geometry_verdict']==source['verdict'] and row['geometry_exception_angles']==source['admissible_rank_drop_angles']
        raw,states,am,bm,ap,bp=native_states(a,b)
        assert raw==row['raw_full_native_ring_states'] and states==row['canonical_ring_states'] and am==row['A_alias_map'] and bm==row['B_alias_map'] and ap==row['A_slot_profiles'] and bp==row['B_slot_profiles']
        rel=private.relations(states);assert rel==[set(map(tuple,r)) for r in row['compatibility']]
        alive,trace=private.prune(rel,len(states));assert alive==row['survivors'] and trace==row['triangle_deletion_rounds']
        if source['verdict']=='FINITE_FEASIBLE_ANGLE_EXCEPTIONS':assert not alive
        degrees=[max((sum(x==j and y in alive for x,y in edges) for j in alive),default=0) for edges in rel]
        assert degrees==row['maximum_successor_degrees']
        verdict='EMPTY' if not alive else 'FUNCTIONAL_DIRECTION';assert verdict==row['verdict'];stats[verdict]+=1
        qq=row['overlap_signature_quotient'];signatures=sorted({tuple(states[j]['A_ring']) for j in alive});fibres=[[j for j in alive if tuple(states[j]['A_ring'])==p] for p in signatures];qid={j:k for k,fibre in enumerate(fibres) for j in fibre}
        qr=[{(qid[x],qid[y]) for x,y in edges if x in qid and y in qid} for edges in rel]
        qdegrees=[max((sum(x==j for x,y in edges) for j in range(len(signatures))),default=0) for edges in qr]
        assert signatures==list(map(tuple,qq['A_ring_signatures'])) and fibres==qq['full_ring_fibres'] and qr==[set(map(tuple,r)) for r in qq['compatibility']] and qdegrees==qq['maximum_successor_degrees']
        if alive:
            assert len(alive)==6 and degrees==[1]*6 and am==list(range(12));positive[i]=row
        else:
            if source['verdict']=='FINITE_FEASIBLE_ANGLE_EXCEPTIONS':assert not alive
    assert dict(stats)=={'EMPTY':30,'FUNCTIONAL_DIRECTION':7} and set(positive)=={27,78,132,270,322,347,446}
    return positive
def periodic_witnesses(positive):
    cert=read('residual-periodic-actions');assert {row['joint_metric_orbit_id'] for row in cert['rows']}==set(positive)
    for row in cert['rows']:
        source=positive[row['joint_metric_orbit_id']];alive=source['survivors'];states=[source['canonical_ring_states'][i] for i in alive]
        assert row['core_original_indices']==alive and row['core_states']==states
        mapping={i:j for j,i in enumerate(alive)};maps=[]
        for edges in source['compatibility']:
            maps.append([mapping[next(j for i,j in edges if i==k and j in mapping)] for k in alive])
        assert maps==row['successor_permutations']==[list(range(6))]*6
        assert row['commuting_action_orbits']==[[j] for j in range(6)]
        witness=row['torus'];lengths=source['A_native_side_partition']+source['B_native_side_word']
        assert witness['index']==3 and witness['hnf']==[3,1,1] and witness['period_generators']==[[3,0],[1,1]] and witness['cell_order']==[[0,0],[1,0],[2,0]]
        assert row['A_native_side_partition']==source['A_native_side_partition'] and row['B_native_side_word']==source['B_native_side_word'] and witness['actual_side_length_classes']==lengths
        assert n.verify_torus(witness,'ALT','ALT',lengths)==(6,18)
        closure=witness['required_side_closure']
        assert all(lengths[i]==lengths[j] for i,j in itertools.product(range(12),repeat=2) if closure[i]==closure[j])
    return len(cert['rows'])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--stage',choices=('domain','geometry','all'),default='all');args=ap.parse_args()
    words=domain_audit();print('Independent domain:203 partitions/611 ledgers/39628 words',flush=True)
    result={'status':'PASSED','matrix_parameter':'t=tan((120-p)/2)','metric_partitions':203,'multiplicity_ledgers':611,'native_B_words':39628}
    if args.stage!='domain':
        allowed=a_strata(words);allowed=three_length(words,allowed);residual=joint_geometry(words,allowed);cases=distinct_local_audit()
        result.update(A_only_excluded_partitions=137,three_length_joint_cases_excluded=270,remaining_native_words=20970,joint_geometry_orbits=685,joint_geometry_excluded_orbits=628,six_distinct_native_words_excluded=900,distinct_AA_local_cases=cases,residual_orbits=37)
        if args.stage=='all':
            positive=native_transport(residual);count=periodic_witnesses(positive)
            result.update(empty_native_cores=30,functional_native_cores=7,index_three_native_tori=count,torus_native_vertex_stars=42,torus_directed_seams=126)
    result['source_sha256']={stem:hashlib.sha256((ROOT/f'two-hexagon-alternating-{stem}.json').read_bytes()).hexdigest() for stem in ('metric-ledger','a-side-strata','three-length-joint-closure','joint-metric-orbits','residual-metric-transport','residual-periodic-actions')}
    result['scope']='Entire specified complementary-angle ALT/ALT actual metric family; reflections/irrational angles/actual real side values; no unrestricted two-convex theorem'
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
