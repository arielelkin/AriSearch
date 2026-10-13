#!/usr/bin/env python3
"""Exhaust all 56 angle-type triples; exact line classification, not geometry."""
import argparse
import json
from collections import defaultdict
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path

# deviations from 120: A=(u,v,-u-v), B=-2A
DEV=((1,0),(0,1),(-1,-1),(-2,0),(0,-2),(2,2))
BASE=((0,0,3),(0,1,2),(1,1,4),(2,2,5),(3,4,5))

def primitive(a,b):
    g=gcd(a,b)
    a,b=a//g,b//g
    return (-a,-b) if a<0 or (a==0 and b<0) else (a,b)

def reconstruct():
    lines=defaultdict(list)
    identities=[]
    for t in combinations_with_replacement(range(6),3):
        a,b=(sum(DEV[k][j] for k in t) for j in range(2))
        if (a,b)==(0,0): identities.append(list(t))
        else: lines[primitive(a,b)].append(list(t))
    assert tuple(map(tuple,identities))==BASE
    assert len(lines)==12
    records=[]
    named={}
    for i in range(3):
        named[primitive(*DEV[i])]=('angle120',[i])
    for i in range(3):
        for j in range(i+1,3):
            named[primitive(*(DEV[i][k]-DEV[j][k] for k in range(2)))]=('equal_angles',[i,j])
    for i in range(3):
        for j in range(3):
            if i==j: continue
            key=primitive(*(DEV[i][k]-4*DEV[j][k] for k in range(2)))
            assert key not in named
            named[key]=('one_ABB',[i,j])
    assert set(lines)==set(named)
    for key,triples in sorted(lines.items()):
        family,indices=named[key]
        row={'line':list(key),'family':family,'indices':indices,'extra_triples':triples}
        if family=='one_ABB':
            i,j=indices
            assert triples==[sorted((i,3+j,3+j))]
            # p_i=1,p_j=-1,p_other=0: sum p=0, extra score=5.
            p=[0,0,0];p[i]=1;p[j]=-1
            potential=p+[-2*x for x in p]
            assert all(sum(potential[k] for k in t)==0 for t in BASE)
            assert sum(potential[k] for k in triples[0])==5
            assert sum(potential[:3])==sum(potential[3:])==0
            row['potential']=potential
            row['extra_score']=5
            row['parameter']='112.5 < A_j < 126; A_j != 120'
        records.append(row)
    return {'domain':'56 multisets of 3 among six angle types; 90<A_i<180; sum A_i=360',
            'identities':identities,'lines':records,
            'counts':{'triples':56,'identity_triples':5,'lines':12,'ABB_only_lines':6},
            'scope':'Exact angle/contact-balance classification only; no polygon realizability inferred'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    data=reconstruct()
    if args.check: assert json.loads(args.check.read_text())==data
    if args.output: args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: 56 triples, five identities, twelve resonance lines, six single-ABB positive potentials')
if __name__=='__main__':main()
