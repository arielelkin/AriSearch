#!/usr/bin/env python3
"""Bounded four-face torus witness search, not an aperiodicity test."""
from itertools import product
from math import prod
from pathlib import Path
import importlib.util
import json
import sys

spec=importlib.util.spec_from_file_location("metric",Path(__file__).with_name("pentagrid-golden-metric.py"))
metric=importlib.util.module_from_spec(spec);spec.loader.exec_module(metric)

def matching_count(n):
    return prod(range(1,n,2))

def reflected_data(word,exponents,reflected):
    angles=[word[(i-1)%5] for i in range(5)]
    if not reflected:
        return list(exponents),angles
    return list(reversed(exponents)),[angles[(-i)%5] for i in range(5)]

def search(word_b,e_b):
    word_a=metric.WORDS["U"];e_a=(3,3,0,0,0)
    total_domain=0; leaves=0; branches=0
    # The U used here has a reflection symmetry, proved in the record.
    for refl_b0,refl_b1 in product((False,True),repeat=2):
        faces=[reflected_data(word_a,e_a,False),reflected_data(word_a,e_a,False),reflected_data(word_b,e_b,refl_b0),reflected_data(word_b,e_b,refl_b1)]
        labels=[faces[f][0][j] for f in range(4) for j in range(5)]
        base_angles=[faces[f][1][j] for f in range(4) for j in range(5)]
        domain=prod(matching_count(labels.count(label)) for label in set(labels))
        total_domain+=domain
        def rec(remaining,parent,angle,pairs):
            nonlocal branches,leaves
            if not remaining:
                leaves+=1
                roots={find(i,parent) for i in range(20)}
                if any(angle[r]!=10 for r in roots):return None
                reachable={0}
                for _ in range(4):
                    for i,j in pairs:
                        if i//5 in reachable:reachable.add(j//5)
                        if j//5 in reachable:reachable.add(i//5)
                if len(reachable)!=4:return None
                return {"reflected":[False,False,refl_b0,refl_b1],"side_pairs":[[[i//5,i%5],[j//5,j%5]] for i,j in pairs],"corner_classes":[[[i//5,i%5] for i in range(20) if find(i,parent)==r] for r in sorted(roots)]}
            # Rarest remaining edge label gives exact pruning, no symmetry identification.
            i=min(remaining,key=lambda q:sum(labels[t]==labels[q] for t in remaining))
            for j in remaining:
                if j==i or labels[j]!=labels[i]:continue
                branches+=1
                p=parent[:];a=angle[:]
                i1=(i//5)*5+(i+1)%5;j1=(j//5)*5+(j+1)%5
                if not merge(i,j1,p,a) or not merge(i1,j,p,a):continue
                out=rec(tuple(t for t in remaining if t not in (i,j)),p,a,pairs+[(i,j)])
                if out is not None:return out
            return None
        witness=rec(tuple(range(20)),list(range(20)),base_angles,[])
        if witness is not None:
            return {"status":"witness_found","complete":False,"matching_domain_for_processed_reflection_assignments":total_domain,"completed_matchings_reaching_final_test":leaves,"recursive_pair_branches_tested":branches,"witness":witness}
    return {"status":"no_witness_in_complete_four_face_domain","complete":True,"matching_domain":total_domain,"completed_matchings_reaching_final_test":leaves,"recursive_pair_branches_tested":branches}

def find(i,parent):
    while i!=parent[i]:i=parent[i]
    return i

def merge(i,j,parent,angle):
    i=find(i,parent);j=find(j,parent)
    if i!=j:
        parent[j]=i;angle[i]+=angle[j]
    return angle[i]<=10

if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument("--output");args=parser.parse_args()
    out=[]
    data=metric.certificate()
    for record in data["records"]:
        if record["name"]=="U":continue
        for poly in record["closed"]:
            e=poly["side_exponents"]
            result=search(tuple(record["angles_after_sides_in_pi_over_5"]),tuple(e))
            result.update({"B_angle_name":record["name"],"B_side_exponents":e})
            out.append(result)
            print(record["name"],e,result["status"],flush=True,file=sys.stderr)
    cert={"domain":"two U and two B faces, B is each listed fixed normalized golden-power metric, sides matched only at full edges with equal lengths, U unreflected by intrinsic symmetry, all four reflection assignments of B; pairings may join same-face sides","records":out}
    payload=json.dumps(cert,indent=2)+"\n"
    if args.output: Path(args.output).write_text(payload)
    else: print(payload,end="")
