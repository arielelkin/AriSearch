#!/usr/bin/env python3
"""Exact local counterexample to unique-B-star => unique A neighbour ring."""
import argparse,hashlib,importlib.util,itertools,json
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ring=load('independent_canonical_ring',HERE/'check_two_hexagon_balanced_rank_five_ring.py')
algebra=load('independent_affine_algebra',HERE/'two-hexagon-inherited-escape-check.py')
T={(0,1,6),(0,2,7),(1,2,8),(3,3,9),(4,4,10),(5,5,11)}
EXPECTED={(8,3,3,8,10,6),(8,11,11,8,10,6)}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
 assert algebra.closure(T)==T and len(algebra.basis(tuple(sorted(T))))-2==5
 assert all(sum(c in t for t in T)==1 for c in range(6,12))
 assert [sum(Q(1,3)*t.count(c) for t in T) for c in range(12)]==[Q(2,3)]*6+[Q(1,3)]*6
 offsets=(1,10,100,1000,10000,-11111,-11,-101,-110,-2000,-20000,22222)
 angles=tuple(Q(120)+Q(d,1000) for d in offsets)
 assert len(set(angles))==12 and all(0<a<180 for a in angles)
 assert sum(angles[:6])==sum(angles[6:])==720
 assert {t for t in algebra.TRIPLES if sum(angles[c] for c in t)==360}==T
 ring.T=T;constraints,solutions=ring.rings((0,1));assert set(solutions)==EXPECTED
 # Different A states at position1 carry different actual native corner
 # angles at a slot, so this is not a mere repeated-angle label ambiguity.
 assert angles[ring.native(ring.A[3],3)]!=angles[ring.native(ring.A[11],3)]
 result={'status':'PASSED','T':sorted(T),'exact_rank':5,'closed_triples':6,'B_placement':[0,1],'A_alphabet':ring.A,'A_rings':solutions,'angles_degrees':list(map(str,angles)),'positive_weights':['1/3']*6,'scope':'Closed angle-feasible balanced type with nonunique local A rings; no joint metric or infinite realization claimed'}
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
