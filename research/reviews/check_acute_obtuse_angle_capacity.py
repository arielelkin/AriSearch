#!/usr/bin/env python3
"""Independently check complete angular fragments, not coordinate geometry."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

A=(130,281,295,150,224)
B=(80,289,272,94,345)

def sums(values,target):
    values=tuple(sorted(values));out=[]
    def visit(i,remaining,prefix):
        if remaining==0:
            out.append(tuple(prefix));return
        if i==len(values):return
        value=values[i]
        for count in range(remaining//value+1):
            visit(i+1,remaining-count*value,prefix+[value]*count)
    visit(0,target,[])
    return sorted(out)

def normalized(rows):return sorted(tuple(sorted(row)) for row in rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    p=Path('research/certificates/acute-obtuse-long-edge-feature.json');raw=p.read_bytes();d=json.loads(raw)
    assert d['angles_doubled_degrees']=={'A':list(A),'B':list(B)}
    assert sum(A)==sum(B)==1080
    values=A+B;flat=sums(values,360);full=sums(values,720)
    assert flat==[(80,130,150)] and len(full)==9
    assert normalized(d['all_joint_native_stars']['360'])==flat
    assert normalized(d['all_joint_native_stars']['720'])==full
    for name,angles in [('A',A),('B',B)]:
        assert normalized(d['pure_species_stars'][name]['360'])==sums(angles,360)
        assert normalized(d['pure_species_stars'][name]['720'])==sums(angles,720)
        unsupported=[x for x in angles if not any(x in row for row in sums(angles,360)+sums(angles,720))]
        assert unsupported
    assert sums(values,720-2*281)==[]
    assert sums(values,720-130-281)==[]
    assert sums(values,720-281-295)==[]
    assert [row for row in full if 289 in row]==[(150,281,289)]
    assert all(289 not in row for row in flat)
    assert sums(values,720-94-345)==[(281,)]
    assert sums(values,720-2*345)==[]
    ledger=d['formal_2A_1B_corner_ledger']
    assert normalized(ledger[:1])==flat
    assert all(tuple(sorted(row)) in full for row in ledger[1:])
    assert Counter(x for row in ledger for x in row)==Counter(list(A)*2+list(B))
    result={'scope':'complete angle stars, whole-edge angular obstructions and corner-capacity incidence only; exact coordinate/maximum/minimum inequalities are separate obligations',
            'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'flat_stars_doubled_degrees':flat,'full_stars_doubled_degrees':full,
            'monohedral_corner_coverage':'both fail',
            'formal_ledger':'2A+1B valid but insufficient for forced-host capacity',
            'hosted_capacity_hypotheses':'angular components VALID',
            'shortest_A1_hypotheses':'angular components VALID'}
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
