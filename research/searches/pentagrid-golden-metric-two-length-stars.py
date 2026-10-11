#!/usr/bin/env python3
"""Exact necessary full-vertex signatures for one two-length U/V pair."""
from itertools import product
from math import prod
import argparse
import json
from pathlib import Path

ANGLE_UNITS=(1,3,4,2,4,3)
CORNER_NAMES=("U36_LL","U108_LS","U144_SS","V72_LL","V144_LS","V108_SS")

def certificate():
    stars=[]
    for n in product(*(range(10//w+1)for w in ANGLE_UNITS)):
        if sum(w*c for w,c in zip(ANGLE_UNITS,n))!=10:continue
        switches=n[1]+n[4]
        if switches%2:continue
        if not switches and (n[0]+n[3]>0)and(n[2]+n[5]>0):continue
        stars.append(list(n))
    u144=[n for n in stars if n[2]]
    assert u144==[[0,0,1,0,0,2],[0,2,1,0,0,0]]
    v_only=[n for n in stars if not any(n[:3])]
    assert all(not n[5]for n in v_only)
    return {"U_angles_after_sides":[1,3,4,4,3],"U_side_labels":["L","L","S","S","S"],"V_angles_after_sides":[2,2,4,3,4],"V_side_labels":["L","L","L","S","S"],"lengths":{"L":"phi^3","S":"1"},"corner_order":list(CORNER_NAMES),"domain":"n_i integer 0..floor(10/angle_i); angle dot n=10; numerical length cycle must be connected and Eulerian","raw_integer_vectors":prod(10//w+1 for w in ANGLE_UNITS),"stars":stars,"U144_stars":u144,"V_only_stars":v_only,"U_side_joining_two144_corners":3,"neither_tile_has_side_joining_two108_corners":True}

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
    payload=json.dumps(certificate(),indent=2)+"\n"
    if args.output:Path(args.output).write_text(payload)
    else:print(payload,end="")
