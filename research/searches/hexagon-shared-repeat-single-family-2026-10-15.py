#!/usr/bin/env python3
"""Exact native-endpoint obstruction for one A5/B5 numerical word pair.
All five labels denote distinct positive lengths. No metric search or solver.
JSON stdout is nondestructive; only --output PATH writes the certificate.
"""
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
import argparse
import json

WORDS=((0,1,0,2,3,4),(0,2,0,3,1,4))

def build():
    corners=defaultdict(list)
    for f,w in enumerate(WORDS):
        for i in range(6):
            corners[tuple(sorted((w[i],w[(i+1)%6])))].append(6*f+i)
    stars=set()
    for rays in combinations(range(5),3):
        pairs=list(combinations(rays,2))
        if all(p in corners for p in pairs):
            stars.update(tuple(sorted(s)) for s in product(*(corners[p] for p in pairs)))
    stars=sorted(stars)
    def far(c,label):
        f,i=divmod(c,6);w=WORDS[f]
        assert (w[i]==label) != (w[(i+1)%6]==label)
        return 6*f+((i-1)%6 if w[i]==label else (i+1)%6)
    failures=[]
    for st in stars:
        if 1 not in st:continue
        r_corners=[c for c in st if 0 in (WORDS[c//6][c%6],WORDS[c//6][(c%6+1)%6])]
        assert len(r_corners)==2 and 1 in r_corners
        pair=tuple(sorted(far(c,0) for c in r_corners))
        assert not any(pair[0] in s and pair[1] in s for s in stars)
        failures.append({'star':st,'ray_label':0,'far_corner_pair':pair})
    assert [r['star'] for r in failures]==[(1,5,10),(1,8,9),(1,10,11)]
    assert [r['far_corner_pair'] for r in failures]==[(0,2),(2,7),(2,6)]
    assert len(stars)==12
    return {'schema':'SHARED_REPEAT_HEXAGON_NATIVE_ENDPOINT_OBSTRUCTION_V1',
        'A':WORDS[0],'B':WORDS[1],'labels':'five pairwise distinct positive lengths',
        'corner_convention':'after side i, A0..5 B6..11',
        'complete_star_atlas':stars,'obstructed_corner':1,'all_corner_stars_fail':failures,
        'scope':'no full-side trivalent tiling; unrestricted exclusion uses reviewed defect-free limit'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    encoded=json.dumps(build(),indent=2,sort_keys=True)+'\n'
    if args.output:Path(args.output).write_text(encoded)
    print(encoded,end='')

if __name__=='__main__':main()
