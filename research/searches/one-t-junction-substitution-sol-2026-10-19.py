"""One fixed dual pair; finite host/flat redesign, exact all-dihedral angle gate."""
import json, time, hashlib, argparse
from pathlib import Path
from collections import defaultdict, Counter
import z3
from fractions import Fraction
BASE=Path(__file__).with_name("corner-branching-substitution-sol-2026-10-19.json")
OUT=Path(__file__).with_suffix(".json")

def designs(d,parent):
    out=[]
    for host in d["boundary"]:
        old=d["corner_words"][host]
        # T lies strictly inside a native side with both endpoints interior.
        for k,f in enumerate(old):
            if not f.startswith("f"): continue
            prev,nxt=old[k-1],old[(k+1)%len(old)]
            if not (prev.startswith("f") and nxt.startswith("f")):continue
            words={v:list(w) for v,w in d["corner_words"].items()}
            # Insert the formerly split parent corner inside the host boundary arc.
            words[host].insert(1,"u0")
            ordered=[x for v in d["boundary"] for x in words[v] if x.startswith("u")]
            rename={x:"u"+str(j) for j,x in enumerate(ordered)}
            words={v:[rename.get(x,x) for x in w] for v,w in words.items()}
            native={v:[x for x in w if not(v==host and x==f)] for v,w in words.items()}
            roles={"u"+str(j):j for j in range(5 if parent=="P" else 7)}
            seams=d["seams"]
            nodes=defaultdict(list)
            for v,w in words.items():
                for x in w:nodes[x].append(v)
            assert all(len(nodes[x])==(3 if x.startswith("f") else 2 if x.startswith("t") else 1) for x in nodes)
            assert all(len(native[v])==(5 if d["species"][v]=="P" else 7) for v in words)
            assert sum(map(len,native.values()))== (69 if parent=="P" else 66)
            assert len(seams)==(29 if parent=="P" else 27)
            assert len(d["faces"])==(17 if parent=="P" else 16)
            assert len(d["boundary"])==(7 if parent=="P" else 6)
            assert sum(map(len,native.values()))==3*len(d["faces"])-1+2*len(d["boundary"])+len(roles)
            assert len(set(tuple(sorted(s["children"])) for s in seams))==len(seams)
            assert all(d["species"][v]=="P" for v in words if v not in d["boundary"])
            for seam in seams:
                directions=[]
                for v in seam["children"]:
                    w=words[v]; ends=set(seam["endpoints"])
                    directions.append(next((w[j],w[(j+1)%len(w)]) for j in range(len(w)) if {w[j],w[(j+1)%len(w)]}==ends))
                assert directions[0]==directions[1][::-1]
            out.append(dict(host=host,flat=f,host_side_endpoints=[prev,nxt],corner_words=native,expanded_words=words,parent_corner_roles=roles,seams=seams,species=d["species"],boundary=d["boundary"],faces=d["faces"]))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--timeout-ms",type=int,default=180000);ap.add_argument("--parent",choices=["P","Q"]);args=ap.parse_args()
    src=json.loads(BASE.read_text());maps={p:designs(d,p) for p,d in src.items() if not args.parent or p==args.parent}
    solver=z3.Solver();solver.set(timeout=args.timeout_ms,random_seed=0)
    angles={s:[z3.Real(s+str(j)) for j in range(n)] for s,n in [("P",5),("Q",7)]}
    for s,aa in angles.items():solver.add(z3.Sum(aa)==(3 if s=="P" else 5),*[z3.And(a>0,a<1) for a in aa])
    choices={};selectors={}
    for p,variants in maps.items():
        choose=z3.Int("map_"+p);choices[p]=choose;solver.add(choose>=0,choose<len(variants))
        # Same independent dihedral selector domain for every child across variants.
        for v,s in variants[0]["species"].items():
            n=len(angles[s]);sel=z3.Int("phase_"+p+"_"+v);selectors[p,v]=sel;solver.add(sel>=0,sel<2*n)
        for j,d in enumerate(variants):
            nodes=defaultdict(list);cs=[]
            for v,w in d["corner_words"].items():
                aa=angles[d["species"][v]];n=len(aa);sel=selectors[p,v]
                vals=[z3.Real(f"v_{p}_{j}_{v}_{k}") for k in range(n)]
                cs.append(z3.Or(*[z3.And(sel==2*phase+r,*[vals[k]==aa[(phase+eps*k)%n] for k in range(n)]) for phase in range(n) for r,eps in enumerate([1,-1])]))
                for x,value in zip(w,vals):nodes[x].append(value)
            nodes[d["flat"]].append(z3.RealVal(1))
            for x,vv in nodes.items():
                target=2 if x.startswith("f") else 1 if x.startswith("t") else angles[p][int(x[1:])]
                cs.append(z3.Sum(vv)==target)
            solver.add(z3.Implies(choose==j,z3.And(*cs)))
    start=time.monotonic();status=solver.check()
    result=dict(status=str(status),elapsed_seconds=time.monotonic()-start,timeout_ms=args.timeout_ms,z3_version=z3.get_version_string(),seed=0,input_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),formula_sha256=hashlib.sha256(solver.sexpr().encode()).hexdigest(),variant_counts={p:len(v) for p,v in maps.items()},maps=maps)
    if status==z3.sat:
        m=solver.model();result["angles_pi"]={s:[str(m.eval(x)) for x in aa] for s,aa in angles.items()};result["chosen_maps"]={p:m.eval(c).as_long() for p,c in choices.items()};result["assignment"]={p:{v:[m.eval(c).as_long()//2,[1,-1][m.eval(c).as_long()%2]] for (pp,v),c in selectors.items() if pp==p} for p in maps}
        a={s:list(map(Fraction,v)) for s,v in result["angles_pi"].items()}
        for p,j in result["chosen_maps"].items():
            d=maps[p][j];nodes=defaultdict(list)
            for v,w in d["corner_words"].items():
                phase,eps=result["assignment"][p][v];aa=a[d["species"][v]]
                for k,x in enumerate(w):nodes[x].append(aa[(phase+eps*k)%len(aa)])
            assert len(nodes[d["flat"]])==2 and sum(nodes[d["flat"]])==1
            nodes[d["flat"]].append(Fraction(1))
            for x,vv in nodes.items():assert sum(vv)==(2 if x.startswith("f") else 1 if x.startswith("t") else a[p][int(x[1:])])
        result["fraction_verification"]="PASS"
    if status==z3.unknown:result["reason_unknown"]=solver.reason_unknown()
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="maps"},indent=2))
if __name__=="__main__":main()
