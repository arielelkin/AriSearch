"""Exact vertex elimination and branch-cone projection for fixed one-T maps."""
import json, hashlib, time, argparse
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
import z3
HERE=Path(__file__)
SOURCE=HERE.with_name("one-t-junction-substitution-sol-2026-10-19.json")

def branch_rows(d,parent,assignment):
    """Exact shared-angle projection of one fixed dihedral branch: rows [a|b]."""
    nodes=defaultdict(list)
    for v,w in d["corner_words"].items():
        s=d["species"][v]; n=5 if s=="P" else 7
        phase,eps=assignment[v]
        for k,x in enumerate(w):nodes[x].append((0 if s=="P" else 5)+(phase+eps*k)%n)
    rows=[]
    for x,indices in sorted(nodes.items()):
        row=[F(0)]*13
        for i in indices:row[i]+=1
        if x.startswith("u"):row[(0 if parent=="P" else 5)+int(x[1:])]-=1
        else:row[-1]=F(1 if x.startswith("t") or x==d["flat"] else 2)
        rows.append(row)
    for start,n,total in [(0,5,3),(5,7,5)]:
        row=[F(0)]*13
        for i in range(start,start+n):row[i]=1
        row[-1]=total;rows.append(row)
    return rows

def supplementary_projection(d,parent,assignment):
    """Eliminate one shared angle coordinate using the T supplementary row.

    Return reduced affine rows and the affine expression for the omitted angle.
    The remaining coordinates retain 0<a<1; expression must also lie in (0,1).
    """
    rows=branch_rows(d,parent,assignment)
    nodes=sorted({x for w in d["corner_words"].values() for x in w})
    t=rows[nodes.index(d["flat"])]; assert t[-1]==1
    pivot=next(i for i,c in enumerate(t[:12]) if c)
    expression=[-c/t[pivot] for c in t[:12]]+[t[-1]/t[pivot]]
    expression[pivot]=0
    reduced=[]
    for row in rows:
        factor=row[pivot]/t[pivot]
        r=[x-factor*y for x,y in zip(row,t)]
        assert r[pivot]==0
        reduced.append(r[:pivot]+r[pivot+1:])
    return dict(omitted_coordinate=pivot,expression=[str(x) for x in expression],
                reduced_rows=[[str(x) for x in r] for r in reduced],
                strict_expression_bounds=["0 < expression", "expression < 1"])

def rref(rows):
    a=[list(map(F,r)) for r in rows];p=0
    for c in range(12):
        q=next((j for j in range(p,len(a)) if a[j][c]),None)
        if q is None:continue
        a[p],a[q]=a[q],a[p];t=a[p][c];a[p]=[x/t for x in a[p]]
        for j in range(len(a)):
            if j!=p and a[j][c]:
                t=a[j][c];a[j]=[x-t*y for x,y in zip(a[j],a[p])]
        p+=1
    return [r for r in a if any(r)]

def check_witness(maps,result):
    aa=[F(x) for s in ["P","Q"] for x in result["angles_pi"][s]]
    assert all(0<x<1 for x in aa)
    allrows=[]
    for p in ["P","Q"]:
        d=maps[p][result["chosen_maps"][p]]
        rows=branch_rows(d,p,result["assignment"][p]);allrows+=rows
        assert all(sum(x*y for x,y in zip(r[:12],aa))==r[-1] for r in rows)
    reduced=rref(allrows)
    assert all(sum(x*y for x,y in zip(r[:12],aa))==r[-1] for r in reduced)
    return [[str(x) for x in r] for r in reduced]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");args=ap.parse_args()
    source=json.loads(SOURCE.read_text());maps=source["maps"];out=HERE.with_suffix(".json")
    if args.check:
        result=json.loads(out.read_text());assert result["status"]=="sat"
        assert check_witness(maps,result)==result["joint_projected_rref"];print("PASS exact projected branch witness");return
    solver=z3.Solver();solver.set(timeout=180000,random_seed=0)
    angles={s:[z3.Real(s+str(j)) for j in range(n)] for s,n in [("P",5),("Q",7)]}
    for s,aa in angles.items():solver.add(z3.Sum(aa)==(3 if s=="P" else 5),*[z3.And(a>0,a<1) for a in aa])
    choices={}; selectors={}
    for p,variants in maps.items():
        choose=z3.Int("map_"+p);choices[p]=choose;solver.add(choose>=0,choose<len(variants))
        for j,d in enumerate(variants):
            slots={};nodes=defaultdict(list);cs=[]
            for v,w in d["corner_words"].items():
                for k,x in enumerate(w):nodes[x].append((v,k))
            # All node equations concern disjoint native slots. Eliminate one
            # slot at every node, including a T supplementary slot and all
            # private parent-corner slots. Remaining variables are unrestricted.
            for x,items in sorted(nodes.items()):
                free=[]
                for v,k in items[:-1]:
                    slots[v,k]=z3.Real(f"s_{p}_{j}_{v}_{k}");free.append(slots[v,k])
                target=angles[p][int(x[1:])] if x.startswith("u") else z3.RealVal(1 if x.startswith("t") or x==d["flat"] else 2)
                slots[items[-1]]=target-z3.Sum(free)
            for v,w in d["corner_words"].items():
                aa=angles[d["species"][v]];n=len(aa);bs=[]
                for phase in range(n):
                    for eps in [1,-1]:
                        b=z3.Bool(f"b_{p}_{j}_{v}_{phase}_{eps}");bs.append(b)
                        cs.append(z3.Implies(b,z3.And(*[slots[v,k]==aa[(phase+eps*k)%n] for k in range(n)])))
                cs.append(z3.PbEq([(b,1) for b in bs],1));selectors[p,j,v]=bs
            solver.add(z3.Implies(choose==j,z3.And(*cs)))
    formula=solver.sexpr();HERE.with_suffix(".smt2").write_text(formula+"\n(check-sat)\n")
    result=dict(input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),formula_precheck_sha256=hashlib.sha256(formula.encode()).hexdigest(),timeout_ms=180000,seed=0,z3_version=z3.get_version_string(),variant_counts={p:len(v) for p,v in maps.items()},projection="disjoint-node pivot substitution; fixed-phase branch shared-angle affine rows")
    start=time.monotonic();status=solver.check();result.update(status=str(status),elapsed_seconds=time.monotonic()-start)
    if status==z3.sat:
        m=solver.model();result["angles_pi"]={s:[str(m.eval(x)) for x in aa] for s,aa in angles.items()};result["chosen_maps"]={p:m.eval(c).as_long() for p,c in choices.items()};result["assignment"]={}
        for p,j in result["chosen_maps"].items():
            result["assignment"][p]={}
            for v in maps[p][j]["corner_words"]:
                index=next(i for i,b in enumerate(selectors[p,j,v]) if z3.is_true(m.eval(b)))
                result["assignment"][p][v]=[index//2,[1,-1][index%2]]
        result["joint_projected_rref"]=check_witness(maps,result);result["fraction_verification"]="PASS"
    if status==z3.unknown:result["reason_unknown"]=solver.reason_unknown()
    result["coverage_ledger"]=[dict(P_map=i,Q_map=j,status="unresolved" if status==z3.unknown else ("excluded" if status==z3.unsat else "not_individually_decided")) for i in range(8) for j in range(6)]
    result["scheduling_note"]="Single aggregate check launched before later 30-second branch scheduling instruction; parent permitted completion; no branch retries."
    result["formula_smt2_sha256"]=hashlib.sha256(HERE.with_suffix(".smt2").read_bytes()).hexdigest()
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(json.dumps(result,indent=2))
if __name__=="__main__":main()
