#!/usr/bin/env python3
"""Finite native seam gate plus exact cyclotomic closure; no bounded tiling search."""
from itertools import permutations, product, combinations_with_replacement
from collections import Counter, defaultdict
import json, sys
from sage.all import CyclotomicField, QQbar, AA

A=(0,1,2,0,1,2)
SIDES=(0,0,1,2,3,4) # L,M,P,Q,V; five mutually distinct actual lengths
BANGLES=(134,118,108)
K=CyclotomicField(360); z=K.gen(); imaginary=z**90

def canonical(w):
    return min(v[k:]+v[:k] for v in (w,w[::-1]) for k in range(6))
def arms(i): return (SIDES[(i-1)%6],SIDES[i])
def sin(d): return (z**d-z**(-d))/(2*imaginary)
def support(lengths,directions):
    vertices=[K(0)]
    for l,d in zip(lengths,directions): vertices.append(vertices[-1]+l*z**d)
    assert vertices[-1]==0
    cross=lambda a,b: (a.conjugate()*b-a*b.conjugate())/(2*imaginary)
    embedding=K.hom([QQbar.zeta(360)],QQbar)
    assert all(AA(embedding(cross(vertices[(i+1)%6]-vertices[i],vertices[j]-vertices[i])).real())>0
               for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
    return vertices[:-1]

def main(path):
    bracelets=sorted({canonical(w) for w in permutations((0,0,1,1,2,2))})
    assert len(bracelets)==11
    angles=(113,121,126,134,118,108)
    triples=[t for t in combinations_with_replacement(range(6),3) if sum(angles[i] for i in t)==360]
    assert triples==[(0,0,3),(0,1,2),(1,1,4),(2,2,5),(3,4,5)]
    c0,c1,c2=sin(54),sin(113),sin(59)
    assert c0-c1*z**59+c2*z**113==0
    # Coefficients of L,M,lambda, kept exact over K.
    forms=[(1,0,0),(0,1,0),(1,0,-c0),(1,0,c1),(0,1,-c2)]
    lengths=[4,6,4-c0,4+c1,6-c2]
    assert len(set(lengths))==5
    embedding=K.hom([QQbar.zeta(360)],QQbar)
    assert all(AA(embedding(l).real())>0 for l in lengths)
    support([lengths[t] for t in SIDES],(0,59,113,180,239,293))
    seam=[]
    for flip in (False,True):
        pairs=[(0,2),(1,1)] if flip else [(0,1),(1,2)]
        endpoints=[]
        for i,j in pairs:
            # Other arms after deleting the matched sides A0 and A1.
            ai=SIDES[5] if i==0 else SIDES[1]
            aj=SIDES[0] if j==1 else SIDES[2]
            rem=360-angles[A[i]]-angles[A[j]]
            native=[k for k in range(6) if angles[A[k]]==rem]
            completions=[k for k in native if sorted(arms(k))==sorted((ai,aj))]
            endpoints.append(dict(A_corners=[i,j],required_angle=rem,exposed_classes=[ai,aj],
                                  candidate_A_corners=native,A_completions=completions,
                                  forced_B_pair=[ai,aj] if rem in BANGLES else None))
        seam.append(dict(endpoint_bijection='reversed' if flip else 'parallel',endpoints=endpoints))
    assert not any(e['A_completions'] for s in seam for e in s['endpoints'])
    # Every orientation of every native AAA triple, including reflections.
    pure=[]
    for corners in product((0,3),(1,4),(2,5)):
        for signs in product((1,-1),repeat=3):
            rays=[arms(i)[::s] for i,s in zip(corners,signs)]
            if all(rays[k][1]==rays[(k+1)%3][0] for k in range(3)):
                pure.append([corners,signs])
    assert not pure
    fans=[]
    for colour in range(3):
        entries=[]
        for i,j in product((colour,colour+3),repeat=2):
            for ai,aj in product(range(2),repeat=2):
                if arms(i)[ai]==arms(j)[aj]:
                    pair=(arms(i)[1-ai],arms(j)[1-aj])
                    assert pair[0]==pair[1]
                    entries.append(dict(A_corners=[i,j],AA_class=arms(i)[ai],B_pair=pair))
        fans.append(entries)
    allowed=[set(e['B_pair'][0] for e in es) for es in fans]
    assert set.intersection(*allowed)=={0}
    rows=[]
    for w in bracelets:
        directions=[0]
        for k in range(1,6): directions.append(directions[-1]+180-BANGLES[w[k]])
        residue=sum((z**d for d in directions),K(0))
        # Constant-class B closure keeps all L,M,lambda: positive scale times residue.
        family_constant_closed=[i for i in range(5) if residue==0]
        # Relaxed sample-only all 5^6 words, exact meet-in-the-middle, no spatial premises.
        halves=[]
        for ds in (directions[:3],directions[3:]):
            table=defaultdict(list)
            for word in product(range(5),repeat=3):
                table[sum((lengths[t]*z**d for t,d in zip(word,ds)),K(0))].append(word)
            halves.append(table)
        closed=[a+b for value,aa in halves[0].items() for a in aa for b in halves[1].get(-value,[])]
        if residue==0:
            assert set(closed)=={word+word for word in product(range(5),repeat=3)}
        rows.append(dict(B_word=w,directions=directions,equilateral_closure_polynomial=str(residue),
                         family_constant_closed_classes=family_constant_closed,
                         relaxed_sample_assignments_checked=5**6,relaxed_sample_closed_words=closed))
        print(''.join(map(str,w)), 'equilateral', residue==0, 'sample closures',len(closed),flush=True)
    assert [r['B_word'] for r in rows if r['family_constant_closed_classes']]==[(0,1,2,0,1,2)]
    # Single-cell translation carrier for the surviving equilateral B.
    bw=(0,1,2,0,1,2)
    assert all(sum(BANGLES[bw[(k+d)%6]] for d in (0,2,4))==360 for k in range(6))
    result=dict(scope='five distinct A classes; A012012; generic ternary stars; fixed exact angles for closure only',
                class_names=['L','M','P=L-lambda*sin54','Q=L+lambda*sin113','V=M-lambda*sin59'],
                A_side_classes=SIDES,angle_triples=triples,seam_bijections=seam,
                AAA_oriented_cases_checked=64,AAA_survivors=pure,AAB_fans=fans,
                B_allowed_constant_classes_by_colour=[sorted(s) for s in allowed],
                forced_mixed_B_class=0,B_closure_rows=rows,
                relaxed_sample_parameters=[4,6,1],
                family_verdict='NO_CONNECTED_MIXED_DEFECT_FREE_FIELD; ANY_TILEABLE_PAIR_HAS_MONOHEDRAL_PERIODIC_ESCAPE',
                interface_successors=[],periodic_B_carrier=dict(native_word=bw,side_class=0,
                    cell_periods=[[1,0],[0,1]],native_placement=[0,1]))
    with open(path,'w') as f: json.dump(result,f,indent=2)
if __name__=='__main__': main(sys.argv[1])
