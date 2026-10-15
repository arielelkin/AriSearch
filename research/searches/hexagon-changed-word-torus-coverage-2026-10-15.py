#!/usr/bin/env python3
"""Exact weighted-row sufficient-witness comparison for one A5/B5 family.
Reads retained source and fixed-four-face atlases; no geometry/solver search.
Coverage proves angle implication only; flat-torus bridge is a separate proof.
JSON stdout; only explicit --output PATH mutates retained evidence.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json

ROOT=Path(__file__).resolve().parents[2]
CERTS=ROOT/'research/certificates'

def star_row(st):return [F(st.count(i)) for i in range(12)]+[F(2)]

def source_rows(stars):
    return [[F(i<6) for i in range(12)]+[F(4)],
            [F(i>=6) for i in range(12)]+[F(4)]]+[star_row(st) for st in stars]

def basis_with_weights(rows):
    n=len(rows);basis={}
    for j,source in enumerate(rows):
        row=list(source);weights=[F(i==j) for i in range(n)]
        for pivot,(b,w) in sorted(basis.items()):
            q=row[pivot]
            if q:
                row=[a-q*c for a,c in zip(row,b)]
                weights=[a-q*c for a,c in zip(weights,w)]
        pivot=next((i for i,x in enumerate(row) if x),None)
        if pivot is not None:
            q=row[pivot]
            basis[pivot]=([a/q for a in row],[a/q for a in weights])
    return basis

def express(row,basis,n):
    row=list(row);weights=[F(0)]*n
    for pivot,(b,w) in sorted(basis.items()):
        q=row[pivot]
        if q:
            row=[a-q*c for a,c in zip(row,b)]
            weights=[a+q*c for a,c in zip(weights,w)]
    return None if any(row) else [str(x) for x in weights]

def build():
    source=json.loads((CERTS/'hexagon-changed-word-connected-support-gate-2026-10-15.json').read_text())
    atlas=json.loads((CERTS/'hexagon-shared-repeat-four-face-atlas-2026-10-15.json').read_text())
    key='all_endpoint_closed_cornercover_masks'
    supports=[{'mask':mask,'stars':[st for i,st in enumerate(source['full_star_atlas']) if mask>>i&1]}
              for mask in source[key]]
    records=[];residual=[]
    for support in supports:
        stars=support['stars'];rows=source_rows(stars)
        basis=basis_with_weights(rows)
        for i,witness in enumerate(atlas['witnesses']):
            combinations=[express(star_row(st),basis,len(rows)) for st in witness['angle_support']]
            if all(c is not None for c in combinations):
                records.append({'source_mask':support['mask'],'source_stars':stars,
                    'torus_index':i,'target_stars':witness['angle_support'],
                    'row_combinations':combinations})
                break
        else:residual.append(support)
    return {'schema':'CHANGED_WORD_TORUS_ROW_COVERAGE_V1',
        'source_domain_key':key,'source_support_count':len(supports),
        'source_row_order':'A total4, B total4, then listed source stars total2',
        'covered':records,'uncovered':residual,
        'scope':'exact angle-row implications to explicit fixed-four-face torus witnesses; no absence inference'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args()
    encoded=json.dumps(build(),indent=2,sort_keys=True)+'\n'
    if a.output:Path(a.output).write_text(encoded)
    print(encoded,end='')

if __name__=='__main__':main()
