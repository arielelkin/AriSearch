"""Exact first-cut gate. No SMT, numerical LP, or feasibility relaxation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json, hashlib, time, math, argparse
HERE=Path(__file__)
SOURCE=HERE.with_name("one-t-junction-substitution-sol-2026-10-19.json")
CAP_STATES=100000
CAP_SECONDS=180

def canonical(rows):
    a=[list(map(F,r)) for r in rows]; pivot=0
    # Full augmented RREF, including the RHS column.
    for col in range(13):
        q=next((i for i in range(pivot,len(a)) if a[i][col]),None)
        if q is None: continue
        a[pivot],a[q]=a[q],a[pivot]
        z=a[pivot][col];a[pivot]=[x/z for x in a[pivot]]
        for i in range(len(a)):
            if i!=pivot and a[i][col]:
                z=a[i][col];a[i]=[x-z*y for x,y in zip(a[i],a[pivot])]
        pivot+=1
    return tuple(tuple(r) for r in a if any(r))

def run():
    start=time.monotonic()
    def guard(n=0):
        if n>=CAP_STATES or time.monotonic()-start>=CAP_SECONDS:
            raise RuntimeError("predeclared cap reached; no completed-cut claim")
    d=json.loads(SOURCE.read_text())["maps"]["P"][0]
    children=sorted(d["corner_words"])
    inc=defaultdict(list)
    for v in children:
        for k,x in enumerate(d["corner_words"][v]):inc[x].append((v,k))
    best=None; assessed=0; minimum_cuts=[]
    for mask in range(1,2**len(children)-1):
        guard()
        s={v for i,v in enumerate(children) if mask>>i&1}
        front=tuple(sorted(x for x,slots in inc.items() if any(v in s for v,k in slots) and any(v not in s for v,k in slots)))
        raw=math.prod(10 if d["species"][v]=="P" else 14 for v in s)
        score=(len(front),raw,len(s),tuple(sorted(s)))
        if best is None or score<best:best=score;chosen=tuple(sorted(s));frontier=front
        assessed+=1
    s=set(chosen);remaining=tuple(v for v in children if v not in s)
    complete=sorted(x for x,slots in inc.items() if all(v in s for v,k in slots))
    domains=[[(phase,eps) for phase in range(5 if d["species"][v]=="P" else 7) for eps in (1,-1)] for v in chosen]
    states={};prefixes=0
    witness=[F(3,5)]*5+[F(5,7)]*7
    entries=[]
    for values in product(*domains):
        guard(len(states));assignment=dict(zip(chosen,values))
        def coordinate(v,k):
            species=d["species"][v];n=5 if species=="P" else 7
            phase,eps=assignment[v]
            return (0 if species=="P" else 5)+(phase+eps*k)%n
        rows=[]
        for offset,n,total in ((0,5,3),(5,7,5)):
            row=[0]*13
            for j in range(offset,offset+n):row[j]=1
            row[-1]=total;rows.append(row)
        for x in complete:
            row=[0]*13
            for v,k in inc[x]:row[coordinate(v,k)]+=1
            if x in d["parent_corner_roles"]:row[d["parent_corner_roles"][x]]-=1
            else:row[-1]=1 if x.startswith("t") or x==d["flat"] else 2
            rows.append(row)
        boundary=tuple((x,tuple((v,k,coordinate(v,k)) for v,k in inc[x] if v in s)) for x in frontier)
        affine=canonical(rows)
        key=(remaining,boundary,affine)
        assert all(0<a<1 for a in witness)
        assert all(sum(c*a for c,a in zip(row[:12],witness))==row[-1] for row in rows)
        states.setdefault(key,dict(assignment=assignment,multiplicity=0))["multiplicity"]+=1
        entries.append(dict(assignment=assignment,unfinished_native_incidences=boundary,rref=[[str(x) for x in row] for row in affine]))
        prefixes+=1
    assert prefixes==best[1]
    assert len(states)==prefixes # Exact stopping gate, no further traversal.
    return dict(status="STOP_NO_NONTRIVIAL_MERGING",parent="P",map_index=0,input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),caps=dict(states=CAP_STATES,aggregate_seconds=CAP_SECONDS),subsets_assessed=assessed,selection_score=best,assigned_children=chosen,remaining_children=remaining,frontier_nodes=frontier,completed_nodes=complete,raw_prefix_count=prefixes,distinct_exact_states=len(states),maximum_multiplicity=max(v["multiplicity"] for v in states.values()),strict_partial_certificate=[str(x) for x in witness],entries=entries,elapsed_seconds=time.monotonic()-start,full_parent_cover=False,shared_parent_witness=False)

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");args=ap.parse_args()
    result=run();out=HERE.with_suffix(".json")
    if args.check:
        old=json.loads(out.read_text())
        result.pop("elapsed_seconds");old.pop("elapsed_seconds")
        assert json.loads(json.dumps(result))==old
        print("PASS exact replay: 8190 cuts, 10 prefixes, 10 states")
    else:
        out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
        print(json.dumps({k:v for k,v in result.items() if k!="entries"},indent=2))
